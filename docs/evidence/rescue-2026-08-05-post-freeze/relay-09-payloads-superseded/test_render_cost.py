##############################################################################
# File: tests/test_render_cost.py
# Purpose: RBT-64 stage 4b. Derivation tests for scripts/render_cost.py.
#
# WHAT THESE ASSERT, AND WHAT THEY DELIBERATELY DO NOT. They assert DERIVED
#   VALUES — counts, dollars, dates, dispositions — against a FROZEN fixture.
#   They never assert rendered bytes. A whole-page byte comparison is brittle
#   and it is the trap that already proved the wrong file on 2026-08-04: it was
#   sound, and it was faithful to a decoy.
#
# The fixture is frozen at register v0.10.1 (`b7fbff5`) and never read from the
#   live register.md. A test that reads the live file stops being a test the
#   first time someone edits the file, which is the same seam §9 records for the
#   collector's suite.
##############################################################################
from __future__ import annotations

import json
import sys
from decimal import Decimal
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import render_cost as rc  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "fixtures"
REGISTER = (FIXTURES / "register-v0.10.1.md").read_text(encoding="utf-8")
LINES = REGISTER.splitlines()


# --- Header ------------------------------------------------------------------


def test_header_carries_the_version_and_as_of_the_page_stamps():
    header = rc.parse_header(LINES)
    assert rc.plain(header["Version"]) == "0.10.1"
    assert rc.plain(header["As of"]) == "2026-08-05"


# --- §2.1 — the counts strip's source ----------------------------------------


def test_estate_counts_separate_inventory_from_metering():
    """The strip exists to stop these being one claim, so they are counted apart."""
    estate = rc.parse_estate(LINES)
    assert estate["gcp_total"] == 8
    assert estate["gcp_billed"] == 6
    assert estate["accounts_total"] == 3
    assert estate["accounts_billing"] == 2


def test_billing_disabled_projects_are_inventory_and_not_cost_lines():
    """`gen-lang-client-…` and `orbital-citizen-…` are counted, never billed."""
    estate = rc.parse_estate(LINES)
    assert estate["gcp_total"] - estate["gcp_billed"] == 2


# --- §5 — the snapshot -------------------------------------------------------


def test_snapshot_is_the_latest_month_found_by_listing():
    month, meters, totals = rc.parse_snapshot(LINES)
    assert month == "2026-07"
    assert {row["meter"] for row in meters} >= {"Claude Max", "Anthropic API"}
    assert totals["+ estimated"] == Decimal("779.44")


def test_placeholder_rows_are_absent_and_never_zero():
    """`—` means the meter did not bill. A placeholder must not become a zero bar."""
    _, meters, _ = rc.parse_snapshot(LINES)
    names = {row["meter"] for row in meters}
    assert "Firebase Hosting" not in names
    assert "HEX voice stack" not in names


def test_rows_sum_to_the_two_totals_the_register_states():
    """Both, because they are different claims and one alone can agree vacuously."""
    _, meters, totals = rc.parse_snapshot(LINES)
    verified = sum(r["v"] for r in meters if r["p"] not in {"estimated", "unknown"})
    everything = sum(r["v"] for r in meters)
    assert verified == Decimal("766.44")
    assert everything == totals["+ estimated"]


# --- §4 — the date freshness is judged against -------------------------------


def test_freshness_is_judged_on_the_latest_weekly_reading():
    assert rc.parse_weekly_as_of(LINES) == "2026-08-03"


# --- §8 — open items ---------------------------------------------------------


def test_closed_items_do_not_appear():
    numbers = {item["n"] for item in rc.parse_open_items(LINES)}
    for closed in ("1", "1a+1b", "5", "8", "9"):
        assert closed not in numbers


def test_item_6_is_open_despite_being_struck_through_and_marked_closed():
    """The case that decides the disposition signal.

    Item 6's title is struck through and marked CLOSED while its body carries a
    live act and its Blocks cell names a live dependency. A rule keyed to the
    strikethrough — which is the signal a reader reaches for first — silently
    drops it.
    """
    numbers = {item["n"] for item in rc.parse_open_items(LINES)}
    assert "6" in numbers


def test_item_11_is_open_although_it_blocks_nothing():
    """Blocks is not a second disposition signal; an open item may block nothing."""
    numbers = {item["n"] for item in rc.parse_open_items(LINES)}
    assert "11" in numbers


def test_an_item_that_blocks_work_but_names_no_owner_raises():
    """The incoherent asymmetry, as opposed to item 11's ordinary one."""
    broken = REGISTER.replace(
        "| 1c | Disposition 42 GB", "| 1c | Disposition 42 GB", 1
    ).splitlines()
    first, end = rc.locate_table(broken, rc.SECTION_8_PREFIX, rc.COLUMNS_OPEN_ITEMS)
    broken[first] = broken[first].rsplit("|", 3)[0] + "| — | something live |"
    with pytest.raises(rc.RegisterFormatError, match="names no owner"):
        rc.parse_open_items(broken)


def test_summary_is_the_first_sentence_and_not_the_first_bold():
    """Item 3's lead bold is a mid-item aside; its subject is the sentence before."""
    items = {item["n"]: item["item"] for item in rc.parse_open_items(LINES)}
    assert items["3"].startswith("Execute the Aura")
    assert "No longer blocked" not in items["3"]


# --- Header guards -----------------------------------------------------------


def test_a_renamed_column_stops_the_render():
    drifted = REGISTER.replace("| As of | Anthropic API |", "| Date | Anthropic API |")
    with pytest.raises(rc.RegisterFormatError):
        rc.parse_weekly_as_of(drifted.splitlines())


def test_a_malformed_separator_stops_the_render():
    """A data row in the separator's position would be parsed as a header."""
    broken = REGISTER.replace(
        "|---|---|---|---|---|---|", "|---|---|---|---|---|xxx|", 1
    )
    with pytest.raises(rc.RegisterFormatError, match="separator"):
        rc.parse_weekly_as_of(broken.splitlines())


def test_a_missing_section_stops_the_render():
    with pytest.raises(rc.RegisterFormatError):
        rc.parse_estate(["# not the register"])


# --- The data store ----------------------------------------------------------


def test_daily_panel_spans_the_whole_month(tmp_path: Path):
    month, days, through = rc.load_daily(FIXTURES / "data")
    assert month == "2026-08"
    assert len(days) == 31
    assert through == "2026-08-02"


def test_uncovered_days_are_none_and_never_zero():
    """An absent reading and a measured zero are different claims."""
    _, days, _ = rc.load_daily(FIXTURES / "data")
    covered = {day: value for day, value in days if value is not None}
    assert covered == {"01": Decimal("27.03"), "02": Decimal("20.03")}
    assert all(value is None for day, value in days if day not in covered)


def test_a_wrong_schema_stops_the_render(tmp_path: Path):
    payload = json.loads((FIXTURES / "data" / "anthropic-2026-08.json").read_text())
    payload["schema"] = "haffey.ops.anthropic-collector/4"
    (tmp_path / "anthropic-2026-08.json").write_text(json.dumps(payload))
    with pytest.raises(rc.DataStoreError, match="schema"):
        rc.load_daily(tmp_path)


def test_no_data_file_publishes_nothing(tmp_path: Path):
    with pytest.raises(rc.DataStoreError, match="no anthropic"):
        rc.load_daily(tmp_path)


# --- The slot registry, both ways -------------------------------------------


def test_a_marker_no_slot_fills_is_caught():
    with pytest.raises(rc.SlotError, match="markers no slot fills"):
        rc.assert_registry_agrees("<b>#SLOT:NOBODY#</b>", {"USED": "x"})


def test_a_registered_slot_the_template_lost_is_caught():
    """The quieter failure: a fact silently stops appearing."""
    with pytest.raises(rc.SlotError, match="does not use"):
        rc.assert_registry_agrees("<b>#SLOT:USED#</b>", {"USED": "x", "DROPPED": "y"})


def test_no_marker_survives_a_render():
    page = rc.render("<b>#SLOT:A#</b><i>#SLOT:B#</i>", {"A": "1", "B": "2"})
    assert "#SLOT:" not in page
    assert rc.UNFILLED_PREFIX not in page


def test_an_empty_slot_renders_loud_and_is_caught():
    with pytest.raises(rc.SlotError, match="unfilled"):
        rc.render("<b>#SLOT:A#</b>", {"A": ""})


# --- The self-agreement tripwire, three-state -------------------------------


def _slots_for(meters: list[dict[str, object]]) -> dict[str, str]:
    return {"DATA_ARRAY": json.dumps(meters), "UNKNOWN_TAGGED": "0"}


def test_tripwire_agrees_on_the_frozen_fixture():
    _, meters, _ = rc.parse_snapshot(LINES)
    slots = _slots_for(
        [{"m": r["meter"], "v": float(r["v"]), "p": r["p"]} for r in meters]
    )
    assert rc.self_check("<html>ok</html>", REGISTER, slots)["tripwire"] == "agreed"


def test_tripwire_diverges_when_a_row_moves():
    _, meters, _ = rc.parse_snapshot(LINES)
    rows = [{"m": r["meter"], "v": float(r["v"]), "p": r["p"]} for r in meters]
    rows[0]["v"] += 1.0
    with pytest.raises(rc.SelfCheckError, match="DIVERGED"):
        rc.self_check("<html>ok</html>", REGISTER, _slots_for(rows))


def test_could_not_compare_fails_the_job_exactly_like_diverged():
    """The third verdict. An instrument that cannot reach its subject must not
    return a passing value — and must not return a failing one either, so this
    is reported as its own state and then fails."""
    _, meters, _ = rc.parse_snapshot(LINES)
    rows = [{"m": r["meter"], "v": float(r["v"]), "p": r["p"]} for r in meters]
    without_totals = REGISTER.replace(
        "| Verified (`declared` + `measured` + `pulled`) | **766.44** |", ""
    )
    with pytest.raises(rc.SelfCheckError, match="COULD-NOT-COMPARE"):
        rc.self_check("<html>ok</html>", without_totals, _slots_for(rows))


# --- The offline path opens no socket ---------------------------------------


def test_rendering_needs_no_credential_and_no_network(monkeypatch, tmp_path: Path):
    """`--out` is the default and must work with the FTPS environment absent."""
    monkeypatch.delenv(rc.FTPS_USER_ENV, raising=False)
    monkeypatch.delenv(rc.FTPS_PASSWORD_ENV, raising=False)

    def refuse(*args, **kwargs):
        raise AssertionError("the render path opened a socket")

    monkeypatch.setattr(rc.ftplib.FTP_TLS, "connect", refuse)
    slots = rc.build_slots(
        REGISTER, FIXTURES / "data", FIXTURES, rc.datetime.now(rc.timezone.utc)
    )
    assert slots["REGISTER_VERSION"] == "v0.10.1"
    assert slots["GCP_PROJECTS"] == "8"
    assert slots["DAILY_THROUGH"] == "2026-08-02"


# --- The publish path --------------------------------------------------------
#
# Exercised against a fake session rather than a live endpoint. These assert the
# ORDER and the GUARDS — temp-then-rename, read-back-and-hash, and that nothing
# connects before a verified page exists — because those are the properties the
# design turns on, and a live-endpoint test would prove them only on the day it
# ran.


class FakeSession:
    def __init__(self, *, corrupt: bool = False, existing: bytes = b"old page") -> None:
        self.calls: list[str] = []
        self.stored: bytes = b""
        self.corrupt = corrupt
        self.existing = existing

    def cwd(self, path: str) -> None:
        self.calls.append(f"cwd {path}")

    def storbinary(self, command: str, stream: object) -> None:
        self.calls.append(command)
        self.stored = stream.read()  # type: ignore[attr-defined]

    def retrbinary(self, command: str, sink: object) -> None:
        self.calls.append(command)
        name = command.split(" ", 1)[1]
        if name == rc.REMOTE_NAME and not self.stored:
            sink(self.existing)  # type: ignore[operator]
        else:
            sink(b"corrupted" if self.corrupt else self.stored)  # type: ignore[operator]

    def delete(self, name: str) -> None:
        self.calls.append(f"delete {name}")

    def rename(self, old: str, new: str) -> None:
        self.calls.append(f"rename {old} {new}")

    def quit(self) -> None:
        self.calls.append("quit")

    def close(self) -> None:
        self.calls.append("close")


def test_publish_uploads_to_a_temp_name_and_renames(monkeypatch):
    """The live path only ever swaps whole."""
    session = FakeSession()
    monkeypatch.setattr(rc, "connect", lambda: session)
    result = rc.publish(b"<html>new</html>", capture_existing=None)
    assert f"STOR {rc.REMOTE_TEMP}" in session.calls
    assert f"rename {rc.REMOTE_TEMP} {rc.REMOTE_NAME}" in session.calls
    assert session.calls.index(f"STOR {rc.REMOTE_TEMP}") < session.calls.index(
        f"rename {rc.REMOTE_TEMP} {rc.REMOTE_NAME}"
    )
    assert result["published_bytes"] == str(len(b"<html>new</html>"))


def test_publish_fails_when_the_read_back_hash_disagrees(monkeypatch):
    monkeypatch.setattr(rc, "connect", lambda: FakeSession(corrupt=True))
    with pytest.raises(rc.PublishError, match="read-back hash disagrees"):
        rc.publish(b"<html>new</html>", capture_existing=None)


def test_publish_can_capture_the_existing_file_before_overwriting(
    tmp_path, monkeypatch
):
    """The first publish has no rollback unless one is taken here."""
    monkeypatch.setattr(rc, "connect", lambda: FakeSession(existing=b"the live page"))
    target = tmp_path / "captured.html"
    result = rc.publish(b"<html>new</html>", capture_existing=target)
    assert target.read_bytes() == b"the live page"
    assert result["captured_bytes"] == "13"


def test_connect_refuses_without_both_credentials(monkeypatch):
    monkeypatch.delenv(rc.FTPS_USER_ENV, raising=False)
    monkeypatch.delenv(rc.FTPS_PASSWORD_ENV, raising=False)
    with pytest.raises(rc.PublishError, match="must both be set"):
        rc.connect()


def test_a_401_proves_directory_privacy_survived(monkeypatch):
    def raise_401(url, timeout):
        raise rc.urllib.error.HTTPError(url, 401, "Unauthorized", {}, None)

    monkeypatch.setattr(rc.urllib.request, "urlopen", raise_401)
    assert rc.assert_unauthenticated_get_is_401() == "401"


def test_a_200_means_the_page_is_unprotected_and_fails(monkeypatch):
    class Response:
        status = 200

        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

    monkeypatch.setattr(rc.urllib.request, "urlopen", lambda url, timeout: Response())
    with pytest.raises(rc.PublishError, match="expected 401"):
        rc.assert_unauthenticated_get_is_401()


def test_an_unreachable_host_is_not_reported_as_a_pass(monkeypatch):
    """An instrument that cannot reach its subject must not return a passing value."""

    def unreachable(url, timeout):
        raise rc.urllib.error.URLError("no route to host")

    monkeypatch.setattr(rc.urllib.request, "urlopen", unreachable)
    with pytest.raises(rc.PublishError, match="could not reach"):
        rc.assert_unauthenticated_get_is_401()


# --- Entry point -------------------------------------------------------------


def _stage(tmp_path: Path) -> Path:
    (tmp_path / "register.md").write_text(REGISTER, encoding="utf-8")
    (tmp_path / "data").mkdir()
    (tmp_path / "data" / "anthropic-2026-08.json").write_text(
        (FIXTURES / "data" / "anthropic-2026-08.json").read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    template = Path(__file__).resolve().parent.parent / "dashboard.html"
    (tmp_path / "dashboard.html").write_text(
        template.read_text(encoding="utf-8"), encoding="utf-8"
    )
    return tmp_path


def test_main_renders_offline_and_returns_zero(tmp_path: Path):
    root = _stage(tmp_path)
    out = tmp_path / "page.html"
    assert rc.main(["--repo-root", str(root), "--out", str(out)]) == 0
    page = out.read_text(encoding="utf-8")
    assert "#SLOT:" not in page
    assert rc.UNFILLED_PREFIX not in page
    assert "v0.10.1" in page


def test_main_returns_one_and_publishes_nothing_when_the_register_drifts(
    tmp_path: Path,
):
    root = _stage(tmp_path)
    (root / "register.md").write_text(
        REGISTER.replace("| As of | Anthropic API |", "| Date | Anthropic API |"),
        encoding="utf-8",
    )
    out = tmp_path / "page.html"
    assert rc.main(["--repo-root", str(root), "--out", str(out), "--publish"]) == 1
    assert not out.exists()


# --- Remaining guards, each one asserted rather than assumed ----------------


def test_money_returns_none_for_a_placeholder_and_for_nonsense():
    assert rc.money("—") is None
    assert rc.money("") is None
    assert rc.money("not a number") is None
    assert rc.money("**≈ 779.44**") == Decimal("779.44")


def test_plain_removes_struck_through_text_rather_than_unwrapping_it():
    """An unwrapped strikethrough would read as live text on the page."""
    assert rc.plain("~~retired~~ **live**") == "live"
    assert rc.plain("[Notion](https://example.invalid)") == "Notion"


def test_a_table_with_the_right_arity_and_wrong_names_is_drift_not_a_miss():
    drifted = REGISTER.replace(
        "| Meter | Class | $ | Provenance | Note |", "| M | C | D | P | N |"
    )
    with pytest.raises(rc.RegisterFormatError, match="headers are"):
        rc.parse_snapshot(drifted.splitlines())


def test_a_row_of_the_wrong_arity_raises_rather_than_being_padded():
    broken = REGISTER.replace(
        "| 2026-08-03 | 47.05 |", "| 2026-08-03 | 47.05 | extra |", 1
    ).splitlines()
    with pytest.raises(rc.RegisterFormatError, match="cells, expected"):
        rc.parse_weekly_as_of(broken)


def test_a_provenance_tag_outside_the_vocabulary_raises():
    broken = REGISTER.replace(
        "| Claude Max | subscription | 212.00 | `declared` |",
        "| Claude Max | subscription | 212.00 | `guessed` |",
    )
    with pytest.raises(rc.RegisterFormatError, match="not one of"):
        rc.parse_snapshot(broken.splitlines())


def test_a_class_outside_the_vocabulary_raises():
    broken = REGISTER.replace(
        "| Claude Max | subscription | 212.00 |", "| Claude Max | sundry | 212.00 |"
    )
    with pytest.raises(rc.RegisterFormatError, match="carries class"):
        rc.parse_snapshot(broken.splitlines())


def test_a_day_outside_the_files_own_month_raises(tmp_path: Path):
    payload = json.loads((FIXTURES / "data" / "anthropic-2026-08.json").read_text())
    payload["derived"]["dollars_by_day"]["2026-09-01"] = "1.00"
    (tmp_path / "anthropic-2026-08.json").write_text(json.dumps(payload))
    with pytest.raises(rc.DataStoreError, match="outside month"):
        rc.load_daily(tmp_path)


def test_a_data_store_with_no_daily_figures_raises(tmp_path: Path):
    payload = json.loads((FIXTURES / "data" / "anthropic-2026-08.json").read_text())
    payload["derived"]["dollars_by_day"] = {}
    (tmp_path / "anthropic-2026-08.json").write_text(json.dumps(payload))
    with pytest.raises(rc.DataStoreError, match="dollars_by_day"):
        rc.load_daily(tmp_path)


def test_an_unreadable_data_directory_raises(tmp_path: Path):
    with pytest.raises(rc.DataStoreError, match="does not exist"):
        rc.load_daily(tmp_path / "absent")


def test_invalid_json_raises_rather_than_rendering_an_empty_panel(tmp_path: Path):
    (tmp_path / "anthropic-2026-08.json").write_text("{not json")
    with pytest.raises(rc.DataStoreError, match="not valid JSON"):
        rc.load_daily(tmp_path)


def test_source_commit_states_unknown_rather_than_a_plausible_blank(tmp_path: Path):
    assert rc.source_commit(tmp_path) == "unknown"


def test_month_label_is_human_and_the_key_stays_machine():
    assert rc.month_label("2026-07") == "July 2026"
    assert rc.month_label("2026-12") == "December 2026"


def test_publish_tolerates_a_first_publish_with_no_file_to_delete(monkeypatch):
    session = FakeSession()

    def refuse_delete(name: str) -> None:
        raise rc.ftplib.error_perm("550 No such file")

    session.delete = refuse_delete  # type: ignore[method-assign]
    monkeypatch.setattr(rc, "connect", lambda: session)
    assert rc.publish(b"<html>x</html>", capture_existing=None)[
        "published_bytes"
    ] == str(len(b"<html>x</html>"))
