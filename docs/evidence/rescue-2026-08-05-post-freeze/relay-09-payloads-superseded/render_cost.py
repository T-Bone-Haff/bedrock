#!/usr/bin/env python3
##############################################################################
# File: scripts/render_cost.py
# Purpose: RBT-64 stage 4b / register §8 item 18. Renders the /cost page from
#   register.md and the collector's data store, and publishes it over explicit
#   FTPS. It commits nothing — the rendered page is a publication artifact, not
#   a repository one, so the collector's COMMIT_ALLOWLIST is never touched.
#
# ORDER OF OPERATIONS IS LOAD-BEARING: parse -> render -> self-check -> connect.
#   No socket opens until a complete, verified page exists in memory. "Leave the
#   previous page up" is therefore a structural property of this script and not
#   a recovery path it has to execute.
#
# --out FILE is the default and opens no socket and needs no credential.
#   --publish is the only path that connects to anything.
#
# Safety: the FTPS credential arrives via env, never as a command-line
#   argument, and is never logged, printed, or written to a file.
##############################################################################
from __future__ import annotations

import argparse
import calendar

# Explicit FTPS with hostname verification below — not plain FTP.
import ftplib  # nosec B402
import hashlib
import io
import json
import logging
import os
import re
import shutil
import ssl

# One call, resolved path, literal argv, shell=False, no untrusted input.
import subprocess  # nosec B404
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any

LOGGER = logging.getLogger("render_cost")

# --- Publication target -----------------------------------------------------
#
# The node name is `measured` 2026-08-05, not declared. The endpoint presents a
# pool-wide wildcard `*.prod.phx3.secureserver.net` which does NOT name this
# domain: hostname verification fails against haffeyenterprises.com and against
# the PTR name, and passes against this cPanel node. It decays if GoDaddy
# re-hosts the account, so the re-derivation method travels with the value:
# read it from cPanel's address bar or the FTP Accounts page.
FTPS_HOST = "p3plzcpnl506943.prod.phx3.secureserver.net"
FTPS_PORT = 21
# The FTP account is jailed to public_html, so its login directory IS the web
# root. Paths below are relative to that jail, never absolute.
REMOTE_DIR = "cost"
REMOTE_NAME = "index.html"
REMOTE_TEMP = "index.html.tmp-render"
PUBLIC_URL = "https://haffeyenterprises.com/cost/"
FTPS_USER_ENV = "FTPS_USER"
# The NAME of an environment variable, never a value.
FTPS_PASSWORD_ENV = "FTPS_PASSWORD"  # nosec B105
FTP_TIMEOUT_SECONDS = 60

# --- Freshness --------------------------------------------------------------
#
# Judged on §4's latest `As of` — the DATA date — and never on the render
# timestamp, which resets on an unchanged re-render and would report a fresh
# page over stale figures.
STALE_AMBER_DAYS = 8
STALE_RED_DAYS = 15

# --- Slot protocol ----------------------------------------------------------
#
# `#SLOT:NAME#` is the marker. The template is deliberately NOT an openable
# page: `const DATA = #SLOT:DATA_ARRAY#;` is a syntax error, so anyone who opens
# the template meets a broken page rather than a plausible one. If a registered
# slot yields no value the renderer emits `UNFILLED:NAME`, which is loud in the
# output and caught by the post-render assertion below.
SLOT_MARKER = re.compile(r"#SLOT:([A-Z0-9_]+)#")
UNFILLED_PREFIX = "UNFILLED:"

# --- register.md section anchors and their exact column sets ----------------
#
# Every header guard below asserts EQUALITY, never containment. This is the
# collector's posture in scripts/collect_anthropic.py::_locate_table, and it is
# the reason schema drift between register.md and this parser is loud instead of
# silent. A table that gains, loses, or renames a column stops the render.
SECTION_HEADER_PREFIX = "| Field | Value |"
SECTION_2_1_PREFIX = "### 2.1"
SECTION_3_PREFIX = "## 3."
SECTION_4_PREFIX = "## 4."
SECTION_5_PREFIX = "## 5."
SECTION_8_PREFIX = "## 8."

COLUMNS_METERS = ["Meter", "Billing route", "Read path", "Stage"]
COLUMNS_BILLING = ["Project", "Billing account", "Organization"]
COLUMNS_DECLARED = ["Meter", "$/mo", "As of", "Source"]
COLUMNS_SNAPSHOT = ["Meter", "Class", "$", "Provenance", "Note"]
COLUMNS_TOTALS = ["Basis", "$"]
COLUMNS_WEEKLY = ["As of", "Anthropic API", "Aura", "GCP", "Actions", "Provenance"]
COLUMNS_OPEN_ITEMS = ["#", "Item", "Owner", "Blocks"]

SEPARATOR_CELL = re.compile(r"^:?-{3,}:?$")
ABSENT = "—"
MONTH_HEADING = re.compile(r"^###\s+(\d{4})-(\d{2})\s*$")
MONTH_NAMES = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

# --- Data store -------------------------------------------------------------
DATA_SCHEMA = "haffey.ops.anthropic-collector/3"
DATA_FILE = re.compile(r"^anthropic-(\d{4})-(\d{2})\.json$")

# --- Provenance -------------------------------------------------------------
PROVENANCE_TAGS = {"declared", "pulled", "measured", "estimated", "unknown"}
SUBSCRIPTION_CLASS = "subscription"
CONTROLLABLE_CLASS = "controllable"


# --- Errors -----------------------------------------------------------------


class RenderError(Exception):
    """Base for every failure this renderer raises."""


class RegisterFormatError(RenderError):
    """register.md is not in the shape this parser depends on."""


class DataStoreError(RenderError):
    """The collector's data store is absent, or not the schema expected."""


class SlotError(RenderError):
    """The slot registry and the template disagree, or a slot went unfilled."""


class SelfCheckError(RenderError):
    """A rendered page failed a check before any socket was opened."""


class PublishError(RenderError):
    """The publish path failed. No partial page is ever left behind."""


# --- Markdown-to-text -------------------------------------------------------


def plain(text: str) -> str:
    """Reduce register markdown to the text a reader sees.

    The register is prose-and-table, so a cell can carry bold, code spans,
    strikethrough and links. Rendering the markup verbatim would put `**` on the
    page; stripping it silently would let a struck-through phrase read as live
    text. Strikethrough content is therefore REMOVED rather than unwrapped.
    """
    out = re.sub(r"~~.*?~~", "", text)
    out = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", out)
    out = out.replace("**", "").replace("`", "")
    out = re.sub(r"(?<!\w)\*(?!\s)(.+?)(?<!\s)\*(?!\w)", r"\1", out)
    return re.sub(r"\s+", " ", out).strip(" —·-").strip()


def money(cell: str) -> Decimal | None:
    """Parse a register money cell, or None when the meter did not bill.

    `—` means the meter did not exist or did not bill and is NOT zero; a
    placeholder row must not become a zero bar on the chart.
    """
    raw = plain(cell).replace("$", "").replace(",", "").replace("≈", "").strip()
    if not raw or raw == ABSENT:
        return None
    try:
        return Decimal(raw)
    except InvalidOperation:
        return None


# --- Table location ---------------------------------------------------------


def split_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def locate_table(
    lines: list[str], section_prefix: str, expected: list[str], *, occurrence: int = 0
) -> tuple[int, int]:
    """Return (first_data_index, end_index) for a table under a section heading.

    The header guard is what catches schema drift between register.md and this
    renderer. It asserts the exact column set and raises on any difference,
    which is scripts/collect_anthropic.py's posture rather than a new one.

    Args:
        lines: register.md split on newlines.
        section_prefix: Literal heading prefix, e.g. "## 5.".
        expected: The exact column headers this parser depends on.
        occurrence: Which matching table under that heading, zero-based. §2.1
            carries two tables with different shapes.

    Raises:
        RegisterFormatError: If the section, the table, its columns, or its
            separator row are absent or malformed.
    """
    start = next(
        (i for i, line in enumerate(lines) if line.startswith(section_prefix)), None
    )
    if start is None:
        raise RegisterFormatError(f"register.md has no {section_prefix!r} heading")

    seen = -1
    index = start + 1
    while index < len(lines):
        line = lines[index]
        # Stop at the next same-or-higher-level heading so a table in the
        # following section can never be mistaken for one in this section.
        if line.startswith("## ") and not line.startswith(section_prefix):
            break
        if not line.lstrip().startswith("|"):
            index += 1
            continue
        header = split_row(line)
        if header == expected:
            seen += 1
            if seen == occurrence:
                return _validate_and_span(lines, index, expected, section_prefix)
        # A table with the right arity but the wrong names is drift, not a
        # different table, and it must be loud.
        if (
            len(header) == len(expected)
            and header != expected
            and _looks_like_header(lines, index)
        ):
            raise RegisterFormatError(
                f"register.md {section_prefix} has a {len(expected)}-column table whose "
                f"headers are {header} and not {expected}; the renderer depends on them"
            )
        index = _skip_table(lines, index)

    raise RegisterFormatError(
        f"register.md {section_prefix} has no table (occurrence {occurrence}) with columns {expected}"
    )


def _looks_like_header(lines: list[str], index: int) -> bool:
    nxt = index + 1
    if nxt >= len(lines) or not lines[nxt].lstrip().startswith("|"):
        return False
    return all(SEPARATOR_CELL.match(cell) for cell in split_row(lines[nxt]))


def _skip_table(lines: list[str], index: int) -> int:
    while index < len(lines) and lines[index].lstrip().startswith("|"):
        index += 1
    return index


def _validate_and_span(
    lines: list[str], header_index: int, expected: list[str], where: str
) -> tuple[int, int]:
    separator_index = header_index + 1
    if separator_index >= len(lines) or not lines[separator_index].lstrip().startswith(
        "|"
    ):
        raise RegisterFormatError(
            f"register.md {where} table has no separator row beneath its header"
        )
    cells = split_row(lines[separator_index])
    if len(cells) != len(expected) or not all(
        SEPARATOR_CELL.match(cell) for cell in cells
    ):
        raise RegisterFormatError(
            f"register.md {where} separator row is malformed: {lines[separator_index]!r} "
            "— a data row here would be parsed as a header"
        )
    first = separator_index + 1
    end = _skip_table(lines, first)
    return first, end


def rows_of(
    lines: list[str], first: int, end: int, expected: list[str], where: str
) -> list[list[str]]:
    """Return the table's data rows, raising on any row of the wrong arity."""
    out: list[list[str]] = []
    for index in range(first, end):
        cells = split_row(lines[index])
        if len(cells) != len(expected):
            raise RegisterFormatError(
                f"register.md {where} row {index + 1} has {len(cells)} cells, expected {len(expected)}"
            )
        out.append(cells)
    return out


# --- Section parsers --------------------------------------------------------


def parse_header(lines: list[str]) -> dict[str, str]:
    """Return the register's own header table — Version and As of live here."""
    header_index = next(
        (i for i, line in enumerate(lines) if line.startswith(SECTION_HEADER_PREFIX)),
        None,
    )
    if header_index is None:
        raise RegisterFormatError("register.md has no `| Field | Value |` header table")
    first, end = _validate_and_span(lines, header_index, ["Field", "Value"], "header")
    fields = {
        plain(cells[0]): cells[1]
        for cells in rows_of(lines, first, end, ["Field", "Value"], "header")
    }
    for required in ("Version", "As of"):
        if required not in fields:
            raise RegisterFormatError(
                f"register.md header table has no {required!r} row"
            )
    return fields


def parse_estate(lines: list[str]) -> dict[str, int]:
    """Count GCP projects and billing accounts from §2.1.

    The counts strip's whole reason for existing is that inventory and metering
    are different claims, so both halves are counted here rather than inferred
    from the rows that happen to carry dollars.
    """
    first, end = locate_table(lines, SECTION_2_1_PREFIX, COLUMNS_METERS)
    meters = rows_of(lines, first, end, COLUMNS_METERS, "§2.1 meters")
    gcp_total = 0
    gcp_billed = 0
    for cells in meters:
        name = plain(cells[0])
        if not name.startswith("GCP "):
            continue
        gcp_total += 1
        if not _is_unbilled(cells[1]):
            gcp_billed += 1

    first, end = locate_table(lines, SECTION_2_1_PREFIX, COLUMNS_BILLING, occurrence=0)
    accounts = rows_of(lines, first, end, COLUMNS_BILLING, "§2.1 billing accounts")
    total_accounts = 0
    billing_accounts = 0
    for cells in accounts:
        if _is_unbilled(cells[1]):
            # The row that exists to say "these projects have no billing account
            # at all" is not itself an account. §2.1 draws that distinction and
            # has already been caught failing it inside a row that draws it.
            continue
        total_accounts += 1
        if plain(cells[0]).lower().startswith("none"):
            continue
        billing_accounts += 1

    if gcp_total == 0 or total_accounts == 0:
        raise RegisterFormatError(
            "register.md §2.1 yielded no GCP projects or no billing accounts; "
            f"counted {gcp_total} projects and {total_accounts} accounts"
        )
    return {
        "gcp_total": gcp_total,
        "gcp_billed": gcp_billed,
        "accounts_total": total_accounts,
        "accounts_billing": billing_accounts,
    }


def _is_unbilled(cell: str) -> bool:
    text = plain(cell).lower()
    return "billing disabled" in text or text in {"none", "—", ""}


def parse_snapshot(
    lines: list[str],
) -> tuple[str, list[dict[str, Any]], dict[str, Decimal]]:
    """Return (YYYY-MM, meter rows, totals) for §5's LATEST month section.

    §5 is a month-end snapshot series. The latest section is found by listing
    the month headings and taking the maximum, never by assuming the current
    month — a fallback path that runs a few days a year is a path that is never
    tested.
    """
    start = next(
        (i for i, line in enumerate(lines) if line.startswith(SECTION_5_PREFIX)), None
    )
    if start is None:
        raise RegisterFormatError("register.md has no `## 5.` heading")
    end_of_section = next(
        (i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")),
        len(lines),
    )
    months = [
        (match.group(0).split()[-1], i)
        for i, line in enumerate(lines[start:end_of_section], start=start)
        if (match := MONTH_HEADING.match(line))
    ]
    if not months:
        raise RegisterFormatError("register.md §5 has no `### YYYY-MM` month section")
    month, month_index = max(months)

    section = lines[month_index:end_of_section]
    first, end = locate_table(section, "###", COLUMNS_SNAPSHOT)
    meters: list[dict[str, Any]] = []
    for cells in rows_of(section, first, end, COLUMNS_SNAPSHOT, f"§5 {month}"):
        dollars = money(cells[2])
        if dollars is None:
            continue  # placeholder — the meter did not exist or did not bill
        provenance = plain(cells[3]).lower()
        if provenance not in PROVENANCE_TAGS:
            raise RegisterFormatError(
                f"register.md §5 {month} row {plain(cells[0])!r} carries provenance "
                f"{provenance!r}, which is not one of {sorted(PROVENANCE_TAGS)}"
            )
        klass = plain(cells[1]).lower()
        if klass not in {SUBSCRIPTION_CLASS, CONTROLLABLE_CLASS}:
            raise RegisterFormatError(
                f"register.md §5 {month} row {plain(cells[0])!r} carries class {klass!r}"
            )
        meters.append(
            {
                "meter": plain(cells[0]),
                "cls": "sub" if klass == SUBSCRIPTION_CLASS else "ctl",
                "v": dollars,
                "p": provenance,
            }
        )
    if not meters:
        raise RegisterFormatError(
            f"register.md §5 {month} has no meter rows carrying a figure"
        )

    first, end = locate_table(section, "###", COLUMNS_TOTALS)
    totals: dict[str, Decimal] = {}
    for cells in rows_of(section, first, end, COLUMNS_TOTALS, f"§5 {month} totals"):
        value = money(cells[1])
        if value is not None:
            totals[plain(cells[0])] = value
    return month, meters, totals


def parse_weekly_as_of(lines: list[str]) -> str:
    """Return §4's latest `As of` — the date freshness is judged against."""
    first, end = locate_table(lines, SECTION_4_PREFIX, COLUMNS_WEEKLY)
    dates = [
        plain(cells[0])
        for cells in rows_of(lines, first, end, COLUMNS_WEEKLY, "§4")
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", plain(cells[0]))
    ]
    if not dates:
        raise RegisterFormatError("register.md §4 has no dated reading row")
    return max(dates)


def parse_open_items(lines: list[str]) -> list[dict[str, str]]:
    """Return §8's OPEN items only. Closed items do not appear on the page.

    Disposition is read from the OWNER column, NOT from the item's strikethrough
    or a CLOSED marker in its text. Item 6 is why: its title is struck through
    and marked CLOSED while its body carries a still-open act and its Blocks cell
    names a live dependency. A rule keyed to the strikethrough silently drops a
    live item, and the strikethrough is the signal a reader would reach for.

    Blocks is NOT a second disposition signal, and item 11 is why: it is open,
    owned, and blocks nothing, which is an ordinary shape rather than a defect.
    The asymmetry that IS incoherent is the other one — something blocking work
    that nobody owns — and that raises rather than being guessed at.
    """
    first, end = locate_table(lines, SECTION_8_PREFIX, COLUMNS_OPEN_ITEMS)
    items: list[dict[str, str]] = []
    for cells in rows_of(lines, first, end, COLUMNS_OPEN_ITEMS, "§8"):
        number, text = plain(cells[0]), cells[1]
        owner_absent = _is_absent(cells[2])
        blocks_absent = _is_absent(cells[3])
        if owner_absent and not blocks_absent:
            raise RegisterFormatError(
                f"register.md §8 item {number} blocks {plain(cells[3])!r} but names no owner; "
                "the renderer will not guess whether it is open"
            )
        if owner_absent:
            continue
        items.append(
            {
                "n": number,
                "item": summarise_item(text),
                "blocks": "" if blocks_absent else plain(cells[3]),
            }
        )
    if not items:
        raise RegisterFormatError(
            "register.md §8 yielded no open items; every item cannot be closed"
        )
    return items


def _is_absent(cell: str) -> bool:
    """True when a cell carries the register's explicit ABSENT marker.

    Deliberately reads the RAW cell: `plain` strips leading and trailing dashes
    for display, which would erase the very marker this test depends on.
    """
    return cell.strip() in {"", ABSENT}


def summarise_item(text: str) -> str:
    """Reduce an §8 item to its lead phrase.

    §8 items run to paragraphs; the page carries a line. The FIRST SENTENCE is
    the summary, not the first **bold** phrase — item 3 is why: its lead bold is
    "No longer blocked", a mid-item aside, while its subject is the plain
    sentence before it. Bold marks emphasis, and emphasis is not position.

    This heuristic is honest about one limit: it cannot summarise an item that
    carries two dispositions. §8 item 6 renders as its CLOSED half no matter
    which phrase is chosen, because the open half is a clause in its body. That
    is a defect in the item, not in this function, and the remedy is to split
    the item rather than to teach this code to guess.
    """
    flat = plain(text)
    if not flat:
        return ""
    sentence = re.split(r"(?<=[.?])\s", flat)[0]
    return sentence or flat


# --- Data store -------------------------------------------------------------


def load_daily(data_dir: Path) -> tuple[str, list[tuple[str, Decimal | None]], str]:
    """Return (YYYY-MM, [(DD, dollars)], through-date) for the LATEST data file.

    The month is found by LISTING the directory and taking the maximum, never by
    computing today's month with a fallback — the fallback path would run for a
    few days each year and would therefore never be exercised. With no data file
    at all this raises and the render publishes nothing.
    """
    if not data_dir.is_dir():
        raise DataStoreError(f"data directory {data_dir} does not exist")
    candidates = sorted(
        (match.group(0), path)
        for path in data_dir.iterdir()
        if (match := DATA_FILE.match(path.name))
    )
    if not candidates:
        raise DataStoreError(
            f"no anthropic-YYYY-MM.json in {data_dir}; the daily panel has no source"
        )
    name, path = candidates[-1]
    month = name[len("anthropic-") : -len(".json")]

    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise DataStoreError(f"{path} is not valid JSON: {exc}") from exc
    schema = payload.get("schema")
    if schema != DATA_SCHEMA:
        raise DataStoreError(
            f"{path} carries schema {schema!r}, expected {DATA_SCHEMA!r}"
        )
    by_day = payload.get("derived", {}).get("dollars_by_day")
    if not isinstance(by_day, dict) or not by_day:
        raise DataStoreError(
            f"{path} has no derived.dollars_by_day; it is the only source for the daily panel"
        )

    covered: dict[str, Decimal] = {}
    for day, amount in sorted(by_day.items()):
        if not re.fullmatch(rf"{month}-\d{{2}}", day):
            raise DataStoreError(
                f"{path} derived.dollars_by_day carries {day!r}, outside month {month}"
            )
        try:
            covered[day[-2:]] = Decimal(str(amount))
        except InvalidOperation as exc:
            raise DataStoreError(
                f"{path} day {day} carries a non-numeric amount {amount!r}"
            ) from exc

    # The panel spans the WHOLE month, so a partial month reads as a partial
    # month instead of being rescaled to look full. Days the reading does not
    # cover carry None — NOT zero. An absent reading and a measured zero are
    # different claims, and §1's whole premise is that collapsing them is the
    # failure this register exists to prevent.
    year, index = int(month[:4]), int(month[5:7])
    length = calendar.monthrange(year, index)[1]
    days: list[tuple[str, Decimal | None]] = [
        (f"{number:02d}", covered.get(f"{number:02d}"))
        for number in range(1, length + 1)
    ]
    # The last day the DATA covers — a fact about the file, never a judgement
    # about whether the month is complete.
    through = f"{month}-{max(covered)}"
    return month, days, through


# --- Slot computation -------------------------------------------------------


def month_label(month: str) -> str:
    year, mm = month.split("-")
    return f"{MONTH_NAMES[int(mm) - 1]} {year}"


def source_commit(repo_root: Path) -> str:
    """Return the HEAD SHA, or a stated unknown. Never a plausible blank."""
    git = shutil.which("git")
    if git is None:
        return "unknown"
    try:
        result = subprocess.run(  # nosec B603
            [git, "-C", str(repo_root), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"


def build_slots(
    register_text: str, data_dir: Path, repo_root: Path, rendered_at: datetime
) -> dict[str, str]:
    lines = register_text.splitlines()
    header = parse_header(lines)
    estate = parse_estate(lines)
    month, meters, totals = parse_snapshot(lines)
    data_as_of = parse_weekly_as_of(lines)
    open_items = parse_open_items(lines)
    daily_month, days, through = load_daily(data_dir)

    commit = source_commit(repo_root)
    meters = sorted(meters, key=lambda row: row["v"], reverse=True)
    unknown_lines = sum(1 for row in meters if row["p"] == "unknown")
    largest = meters[0]
    runner_up = meters[1] if len(meters) > 1 else None
    version = plain(header["Version"])

    data_array = json.dumps(
        [
            {"m": row["meter"], "cls": row["cls"], "v": float(row["v"]), "p": row["p"]}
            for row in meters
        ],
        ensure_ascii=False,
    )
    daily_array = json.dumps(
        [[day, None if value is None else float(value)] for day, value in days],
        ensure_ascii=False,
    )
    rows = "".join(
        f'<tr><td class="n">{item["n"]}</td><td>{_escape(item["item"])}</td>'
        f"<td>{_escape(item['blocks'])}</td></tr>"
        for item in open_items
    )

    largest_note = (
        f'{_escape(largest["meter"])} — <span id="t-share">—</span> of program spend'
    )
    if runner_up is not None:
        largest_note += f", and larger than {_escape(runner_up['meter'])}"
    largest_note += "."

    return {
        "HEAD_COMMENT": (
            "GENERATED FILE — DO NOT EDIT.\n"
            f"  Rendered by scripts/render_cost.py from register.md v{version}\n"
            f"  at commit {commit}, {rendered_at.strftime('%Y-%m-%dT%H:%M:%SZ')}.\n"
            "  Edit dashboard.html (the template of record) and let CI re-render.\n"
            "  Every number, date, count, state or judgment on this page is derived\n"
            "  from register.md or from data/anthropic-YYYY-MM.json."
        ),
        "REGISTER_VERSION": f"v{version}",
        "GCP_PROJECTS": str(estate["gcp_total"]),
        "GCP_BILLED": str(estate["gcp_billed"]),
        "BILLING_ACCOUNTS": str(estate["accounts_total"]),
        "BILLING_ACTIVE": str(estate["accounts_billing"]),
        "UNKNOWN_TAGGED": str(unknown_lines),
        "SNAPSHOT_MONTH": month_label(month),
        "LARGEST_LINE": f"${largest['v']:,.2f}",
        "LARGEST_LINE_VALUE": f"{largest['v']}",
        "LARGEST_LINE_NOTE": largest_note,
        "DAILY_MONTH": month_label(daily_month),
        "DAILY_MONTH_KEY": daily_month,
        "DAILY_THROUGH": through,
        "DATA_ARRAY": data_array,
        "DAILY_ARRAY": daily_array,
        "OPEN_ITEM_ROWS": rows,
        "DATA_AS_OF": data_as_of,
        "RENDERED_AT": rendered_at.strftime("%Y-%m-%d %H:%M UTC"),
        "SOURCE_COMMIT": commit[:12],
        "STALE_AMBER_DAYS": str(STALE_AMBER_DAYS),
        "STALE_RED_DAYS": str(STALE_RED_DAYS),
    }


def _escape(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


# --- Render -----------------------------------------------------------------


def assert_registry_agrees(template: str, slots: dict[str, str]) -> None:
    """Two-way: every marker is registered, and every registered slot is used.

    One direction alone is half a check. A marker nobody fills ships a literal
    `#SLOT:` to the reader; a registered slot the template has lost means a fact
    silently stopped appearing, which is the quieter and worse failure.
    """
    in_template = set(SLOT_MARKER.findall(template))
    registered = set(slots)
    unregistered = sorted(in_template - registered)
    unused = sorted(registered - in_template)
    problems = []
    if unregistered:
        problems.append(f"template carries markers no slot fills: {unregistered}")
    if unused:
        problems.append(f"registry carries slots the template does not use: {unused}")
    if problems:
        raise SlotError("; ".join(problems))


def render(template: str, slots: dict[str, str]) -> str:
    assert_registry_agrees(template, slots)
    page = SLOT_MARKER.sub(
        lambda match: slots.get(match.group(1)) or f"{UNFILLED_PREFIX}{match.group(1)}",
        template,
    )
    survivors = SLOT_MARKER.findall(page)
    if survivors:
        raise SlotError(f"markers survived rendering: {sorted(set(survivors))}")
    unfilled = re.findall(rf"{UNFILLED_PREFIX}([A-Z0-9_]+)", page)
    if unfilled:
        raise SlotError(f"slots rendered unfilled: {sorted(set(unfilled))}")
    return page


def self_check(page: str, register_text: str, slots: dict[str, str]) -> dict[str, str]:
    """Verify the page before any socket opens.

    The self-agreement tripwire compares the renderer's own row sum against the
    total §5 STATES. It has three verdicts, not two: agreed, diverged, and
    could-not-compare — and the last fails the job exactly like diverged,
    because an instrument that cannot reach its subject must not return a
    passing value.
    """
    if slots["UNKNOWN_TAGGED"] != "0" and "unknown" not in page:
        raise SelfCheckError("page claims unknown-tagged lines exist but shows none")

    data = json.loads(slots["DATA_ARRAY"])
    _, _, totals = parse_snapshot(register_text.splitlines())

    # §5 states TWO totals and they are different claims. Comparing the row sum
    # against one of them alone is how a renderer agrees with the register about
    # a number neither of them means.
    verified_sum = sum(
        Decimal(str(row["v"]))
        for row in data
        if row["p"] not in {"estimated", "unknown"}
    )
    all_sum = sum(Decimal(str(row["v"])) for row in data)
    comparisons = [
        (
            "verified",
            verified_sum,
            next(
                (v for k, v in totals.items() if k.lower().startswith("verified")), None
            ),
        ),
        (
            "with-estimated",
            all_sum,
            next(
                (v for k, v in totals.items() if k.lower().startswith("+ estimated")),
                None,
            ),
        ),
    ]

    results: dict[str, str] = {}
    for name, computed, stated in comparisons:
        if stated is None:
            raise SelfCheckError(
                f"self-agreement tripwire COULD-NOT-COMPARE on {name}: §5 states no such total. "
                "This fails the render; it does not pass it."
            )
        if abs(computed - stated) > Decimal("0.01"):
            raise SelfCheckError(
                f"self-agreement tripwire DIVERGED on {name}: rows sum to {computed} "
                f"against §5's stated {stated}"
            )
        results[name] = f"{computed}"
    return {
        "tripwire": "agreed",
        "row_sum": results["verified"],
        "stated": results["with-estimated"],
    }


# --- Publish ----------------------------------------------------------------


def connect() -> ftplib.FTP_TLS:
    """Open an explicit-FTPS session with hostname verification ON.

    Never pinned: the endpoint presents a pool-wide wildcard that narrows
    identity no further than "a phx3 node", so a fingerprint asserts exactly
    what hostname verification already asserts — and it expires, turning a
    routine rotation into an outage. Never disabled, for the obvious reason.
    """
    user = os.environ.get(FTPS_USER_ENV)
    password = os.environ.get(FTPS_PASSWORD_ENV)
    if not user or not password:
        raise PublishError(
            f"{FTPS_USER_ENV} and {FTPS_PASSWORD_ENV} must both be set in the environment"
        )

    context = ssl.create_default_context()
    context.check_hostname = True
    context.verify_mode = ssl.CERT_REQUIRED
    session = ftplib.FTP_TLS(context=context, timeout=FTP_TIMEOUT_SECONDS)
    session.connect(FTPS_HOST, FTPS_PORT)
    session.auth()  # explicit FTPS: AUTH TLS on the control channel
    session.login(user, password)
    session.prot_p()  # protect the data channel too
    session.set_pasv(True)
    return session


def publish(page: bytes, *, capture_existing: Path | None) -> dict[str, str]:
    """Upload to a temp name and rename, so the live path only swaps whole.

    Nothing here runs until the page in memory has passed every check above.
    """
    result: dict[str, str] = {}
    session = connect()
    try:
        session.cwd(REMOTE_DIR)
        if capture_existing is not None:
            existing = bytearray()
            session.retrbinary(f"RETR {REMOTE_NAME}", existing.extend)
            capture_existing.write_bytes(bytes(existing))
            result["captured_bytes"] = str(len(existing))
            result["captured_sha256"] = hashlib.sha256(bytes(existing)).hexdigest()

        session.storbinary(f"STOR {REMOTE_TEMP}", io.BytesIO(page))
        try:
            session.delete(REMOTE_NAME)
        except ftplib.error_perm:
            pass  # first publish, or the server allows overwrite on rename
        session.rename(REMOTE_TEMP, REMOTE_NAME)

        readback = bytearray()
        session.retrbinary(f"RETR {REMOTE_NAME}", readback.extend)
    finally:
        try:
            session.quit()
        except ftplib.all_errors:  # already includes OSError and EOFError
            session.close()

    local_hash = hashlib.sha256(page).hexdigest()
    remote_hash = hashlib.sha256(bytes(readback)).hexdigest()
    if local_hash != remote_hash:
        raise PublishError(
            f"read-back hash disagrees: local {local_hash}, remote {remote_hash}. "
            f"{len(page)} bytes sent, {len(readback)} read back"
        )
    result["published_sha256"] = local_hash
    result["published_bytes"] = str(len(page))
    return result


def assert_unauthenticated_get_is_401() -> str:
    """Prove Directory Privacy survived the overwrite.

    FLOOR, stated because it is easy to over-read: a 401 is returned by the
    directory BEFORE file resolution, so this proves the protection is in place
    and NOT that the file is served. Only the use pass closes that.
    """
    try:
        # PUBLIC_URL is a module constant on a literal https scheme.
        with urllib.request.urlopen(PUBLIC_URL, timeout=30) as response:  # nosec B310
            raise PublishError(
                f"unauthenticated GET of {PUBLIC_URL} returned {response.status}, expected 401 — "
                "Directory Privacy is not protecting this directory"
            )
    except urllib.error.HTTPError as exc:
        if exc.code != 401:
            raise PublishError(
                f"unauthenticated GET returned {exc.code}, expected 401"
            ) from exc
        return "401"
    except urllib.error.URLError as exc:
        raise PublishError(
            f"unauthenticated GET could not reach {PUBLIC_URL}: {exc}"
        ) from exc


# --- Entry point ------------------------------------------------------------


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render the /cost page from register.md."
    )
    parser.add_argument(
        "--repo-root", type=Path, default=Path(__file__).resolve().parent.parent
    )
    parser.add_argument("--template", type=Path, default=None)
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("cost-index.html"),
        help="Write the rendered page here. Opens no socket and needs no credential.",
    )
    parser.add_argument(
        "--publish",
        action="store_true",
        help="Publish over FTPS. The ONLY path that connects to anything.",
    )
    parser.add_argument(
        "--capture-existing",
        type=Path,
        default=None,
        help="RETR the current live file before overwriting it, and save it here.",
    )
    parser.add_argument("--verbose", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO, format="%(message)s"
    )

    repo_root: Path = args.repo_root
    template_path: Path = args.template or (repo_root / "dashboard.html")
    register_text = (repo_root / "register.md").read_text(encoding="utf-8")
    template = template_path.read_text(encoding="utf-8")
    rendered_at = datetime.now(timezone.utc)

    try:
        slots = build_slots(register_text, repo_root / "data", repo_root, rendered_at)
        page = render(template, slots)
        checks = self_check(page, register_text, slots)
    except RenderError as exc:
        LOGGER.error("%s: %s", type(exc).__name__, exc)
        return 1

    LOGGER.info(
        "rendered %d bytes · tripwire %s (rows %s vs §5 %s) · data as of %s",
        len(page.encode()),
        checks["tripwire"],
        checks["row_sum"],
        checks["stated"],
        slots["DATA_AS_OF"],
    )

    args.out.write_text(page, encoding="utf-8")
    LOGGER.info("wrote %s", args.out)

    if not args.publish:
        return 0

    try:
        result = publish(page.encode("utf-8"), capture_existing=args.capture_existing)
        code = assert_unauthenticated_get_is_401()
    except RenderError as exc:
        LOGGER.error("%s: %s", type(exc).__name__, exc)
        return 1

    LOGGER.info(
        "published %s bytes sha256 %s · unauthenticated GET %s",
        result["published_bytes"],
        result["published_sha256"],
        code,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
