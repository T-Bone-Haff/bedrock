#!/usr/bin/env python3
##############################################################################
# publish-cost.py — RBT-93 item 18, Act 2: the first publish.
#
# ONE-OFF, SUPERVISED, OPERATOR-RUN. Not part of the repository, not committed.
# It exists because the first publish is the single irreversible act in this
# program and it is being done by hand, once, with a human watching.
#
# WHY THE OPERATOR RUNS IT AND NOT AN AGENT. The credential never enters any
# agent's environment, context, transcript or log. getpass reads it into THIS
# process, it goes into this process's own environ, one function call uses it,
# and it is dropped. Never in argv, never in shell history, never written to a
# file, never printed, and no verbose flag is passed anywhere. On 2026-08-05 a
# `curl -v` paired with an interactive prompt closed the argv channel and opened
# stdout; the password went to the terminal and had to be rotated. CLOSING ONE
# CHANNEL IS NOT SECURING A SECRET — enumerate all of them.
#
# WHAT IT GUARDS BEFORE IT ASKS FOR ANYTHING. Every precondition is checked and
# reported BEFORE the credential prompt, so a refusal costs nothing:
#   * the repo is at the expected commit with a clean tree — otherwise the page
#     stamps a commit that does not contain it, which is a page telling a lie
#     about its own provenance
#   * the capture directory exists and the capture target does NOT — the capture is
#     the only retrieval through the authoritative channel this program will get
#     of the bytes about to be destroyed, and nothing may overwrite it
#   * the preserved reconstruction is present at its recorded hash, so the
#     capture has something to be compared against
#
# WHAT IT REPORTS AFTERWARDS. Captured bytes and hash · whether the capture
# agrees with the reconstruction · swap mode · published bytes and hash · the
# unauthenticated GET · and whether the published bytes are the bytes the
# operator approved in the preview, modulo the render clock.
#
# RUN:  chmod +x publish-cost.py && ./publish-cost.py
##############################################################################
from __future__ import annotations

import getpass
import hashlib
import os
import re
import shutil

# One call, resolved path, literal argv, shell=False, no untrusted input.
import subprocess  # nosec B404
import sys
from pathlib import Path

HOME = Path.home()
REPO = HOME / "Documents/GitHub/ops"

# WHERE THE COMPARATOR LIVES, AND WHY IT MOVED. Until 2026-08-06 this pointed at
# ~/Downloads/Rescue/. A parallel HEB-105 session landed that corpus into the
# bedrock repository (PRs #19 and #20, both merged) and moved the loose copies to
# ~/Downloads/_to_delete/. The reconstruction is now COMMITTED and TRACKED, which
# is strictly better than a folder nobody version-controls — but the path this
# script depends on changed under it, and the guards below are what caught that.
BEDROCK = HOME / "Documents/GitHub/bedrock"
EVIDENCE = BEDROCK / "docs/evidence/rescue-2026-08-05-post-freeze"

# The capture goes to a plain working directory, NOT into a git repository:
# writing into bedrock would be an untracked mutation of a repo mid-session, and
# landing this artifact as evidence is a deliberate later act with its own gate.
ACT2 = HOME / "Downloads" / "rbt93-act2"

EXPECTED_COMMIT = "02b0933e86ed7c7f6a22903117c5daab3fe6202e"

RECONSTRUCTION = EVIDENCE / "cost-index-deployed-2026-08-05.html"
RECON_SHA = "acd3485fdd142323c6fb32db4309dec6144a4bd10e8d8a5cce5ab6e14d9f6a6a"
RECON_BYTES = 21400

CAPTURE = ACT2 / "cost-index-captured-2026-08-06.html"
PUBLISHED = ACT2 / "cost-published-2026-08-06.html"
APPROVED = ACT2 / "cost-preview-v0.10.2-02b0933e.html"

RULE = "=" * 74
PAD = " " * 18


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(*args: str) -> str:
    exe = shutil.which("git")
    if exe is None:
        fail("git is not on PATH")
    return subprocess.run(  # nosec B603
        [str(exe), "-C", str(REPO), *args],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()


def normalise(text: str) -> str:
    """Strip only the two fields that must differ between two renders."""
    text = re.sub(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2} UTC", "<TS>", text)
    return re.sub(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", "<TS>", text)


def fail(message: str) -> None:
    print(f"\n  REFUSING: {message}\n", file=sys.stderr)
    raise SystemExit(2)


def preflight() -> None:
    print(RULE)
    print("PRE-FLIGHT — every check runs before the credential prompt")
    print(RULE)

    if not REPO.is_dir():
        fail(f"{REPO} does not exist")

    head = git("rev-parse", "HEAD")
    branch = git("rev-parse", "--abbrev-ref", "HEAD")
    dirty = git("--no-optional-locks", "status", "--porcelain")
    print(f"  repo            {REPO}")
    print(f"  branch          {branch}")
    print(f"  HEAD            {head}")
    print(f"  working tree    {'clean' if not dirty else 'DIRTY'}")

    if head != EXPECTED_COMMIT:
        fail(
            f"HEAD is {head},\n"
            f"            expected {EXPECTED_COMMIT}.\n"
            "  The renderer stamps the page with `git rev-parse HEAD`. Publishing\n"
            "  from a different commit than the one reviewed produces a page whose\n"
            "  provenance line names something other than the bytes it carries."
        )
    if dirty:
        fail(
            "the working tree is dirty.\n"
            "  A dirty tree renders content HEAD does not contain, and the page then\n"
            "  attributes itself to a commit that cannot reproduce it."
        )

    if not ACT2.is_dir():
        fail(f"{ACT2} does not exist — the capture has nowhere to land")
    if not EVIDENCE.is_dir():
        fail(
            f"{EVIDENCE}\n            does not exist. The comparator is committed"
            " evidence in the bedrock repo;\n  if that path has moved again, find it"
            " before anything overwrites the live page."
        )
    if not RECONSTRUCTION.is_file():
        fail(f"{RECONSTRUCTION} is missing — the capture would have no comparator")

    recon_sha, recon_len = sha256(RECONSTRUCTION), RECONSTRUCTION.stat().st_size
    print(f"  reconstruction  {recon_len} bytes  {recon_sha[:16]}…")
    if recon_sha != RECON_SHA or recon_len != RECON_BYTES:
        fail(
            "the preserved reconstruction does not match its recorded hash or size.\n"
            "  That is a finding in its own right and must be understood before\n"
            "  anything overwrites the live page."
        )
    print(f"{PAD}matches the recorded hash and size")

    if CAPTURE.exists():
        fail(
            f"{CAPTURE}\n            already exists. Refusing to overwrite it.\n"
            "  If a previous run reached the capture, that capture is the\n"
            "  irreplaceable artifact — say so before re-running."
        )

    print(f"  capture target  {CAPTURE.name}  (absent, good)")
    print(f"  published copy  {PUBLISHED.name}")
    approved = "present" if APPROVED.is_file() else "ABSENT — comparison skipped"
    print(f"  approved page   {APPROVED.name}  ({approved})")

    for name in ("FTPS_USER", "FTPS_PASSWORD"):
        if os.environ.get(name):
            print(f"  NOTE            {name} is already set; it will be replaced")

    print("\n  Pre-flight passed. Nothing has been sent anywhere yet.")


def report_capture() -> None:
    if not CAPTURE.is_file():
        print("  captured        NO FILE — --capture-existing produced nothing.")
        return
    cap_sha, cap_len = sha256(CAPTURE), CAPTURE.stat().st_size
    print(f"  captured        {cap_len} bytes")
    print(f"{PAD}{cap_sha}")
    print(f"  reconstruction  {RECON_BYTES} bytes")
    print(f"{PAD}{RECON_SHA}")
    if cap_sha == RECON_SHA:
        print("  VERDICT         AGREE — the reconstruction was right, and is now")
        print(f"{PAD}confirmed through the authoritative channel rather")
        print(f"{PAD}than inferred from an ETag and a deterministic strip.")
    else:
        print("  VERDICT         DISAGREE — and this is a FINDING, not a problem.")
        print(f"{PAD}It means the reconstruction was wrong and the ETag,")
        print(f"{PAD}§7's recorded figure and the HTTP strip all missed it.")
        print(f"{PAD}That is worth more than a clean match. Keep both files.")


def report_published() -> None:
    if not PUBLISHED.is_file():
        return
    pub_sha, pub_len = sha256(PUBLISHED), PUBLISHED.stat().st_size
    print(f"\n  published       {pub_len} bytes")
    print(f"{PAD}{pub_sha}")
    print(f"{PAD}(this local copy is byte-identical to what was uploaded:")
    print(f"{PAD} the renderer writes --out and publishes the same bytes)")

    if not APPROVED.is_file():
        return
    same = normalise(PUBLISHED.read_text(encoding="utf-8")) == normalise(
        APPROVED.read_text(encoding="utf-8")
    )
    print(f"\n  approved page   {APPROVED.name}")
    if same:
        print("  VERDICT         IDENTICAL once the render clock is normalised.")
        print(f"{PAD}The bytes now live are the bytes you approved.")
    else:
        print("  VERDICT         DIFFERS beyond the render clock. STOP and diff")
        print(f"{PAD}them before treating this publish as reviewed.")


def main() -> int:
    preflight()

    print(f"\n{RULE}\nCREDENTIAL — not echoed, not stored, not logged\n{RULE}")
    user = input("  FTP user     : ").strip()
    password = getpass.getpass("  FTP password : ")
    if not user or not password:
        fail("both a user and a password are required")

    sys.path.insert(0, str(REPO / "scripts"))
    # Imported after the guards, deliberately: nothing from the renderer is
    # loaded until the repository has been proven to be the one we mean.
    import render_cost as rc  # type: ignore[import-not-found] # noqa: E402

    os.environ["FTPS_USER"] = user
    os.environ["FTPS_PASSWORD"] = password
    del password

    print(f"\n{RULE}\nPUBLISH\n{RULE}")
    try:
        code = int(
            rc.main(
                [
                    "--repo-root",
                    str(REPO),
                    "--out",
                    str(PUBLISHED),
                    "--publish",
                    "--capture-existing",
                    str(CAPTURE),
                ]
            )
        )
    finally:
        os.environ.pop("FTPS_USER", None)
        os.environ.pop("FTPS_PASSWORD", None)

    print(f"\n{RULE}\nVERIFICATION\n{RULE}")

    if code != 0:
        print("  The publish FAILED — read the error above.")
        got = str(CAPTURE) if CAPTURE.exists() else "no"
        print(f"  Capture written: {got}")
        print("  The capture runs before the upload and the live path is only")
        print("  altered after the staged bytes verify, so a failure here means")
        print("  the live page was not touched.")
        return code

    report_capture()
    report_published()

    print(f"\n{RULE}")
    print("  Next: open https://haffeyenterprises.com/cost/ and read the SERVED")
    print("  page. A 401 proves the directory is protected, not that the file is")
    print("  served; a read-back hash proves bytes on disk, not that HTTP serves")
    print("  them. Only the use pass closes that, and it is the operator's.")
    print(RULE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
