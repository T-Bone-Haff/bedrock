#!/usr/bin/env python3
##############################################################################
# ftp-jail-check.py — RBT-93 item 18, measurement M4 (2026-08-06)
#
# WHAT THIS MEASURES, and why it is worth running before any code is written:
#
#   1. THE JAIL. On 2026-08-05 an authenticated NLST returned exactly
#      index.html, ., .htaccess, .., .ftpquota — no `cost`, no `status`, no
#      `assets`. That reading is what closed the catastrophic branch of defect
#      N2. The account password has been ROTATED since, so the credential is
#      new and the reading must be retaken rather than recalled.
#
#   2. THE ANSWER SHAPE. N2's remedy turns on what the server actually puts in
#      an NLST reply — bare names, paths, or names with a trailing slash. The
#      ratified remedy `name.rsplit("/", 1)[-1]` returns the EMPTY STRING on a
#      trailing-slash answer and fails open. This script prints the entries
#      VERBATIM (repr, so whitespace and slashes are visible) and then shows
#      what each candidate basename rule would make of them.
#
#   3. THE TRANSPORT. It prints the peer certificate's issuer and validity.
#      A TLS-intercepting proxy re-signs with its own CA; on this estate the
#      correct answer is Starfield, expiring 2026-09-23. This is the
#      known-value control travelling inside the same measurement.
#
# SAFETY POSTURE — every channel, not just the obvious one:
#   * The password is read with getpass: never echoed, never in argv, never in
#     shell history, never in an environment variable this script sets.
#   * Nothing is written to disk. Nothing is uploaded. No file is created,
#     renamed or deleted on the server. This is a READ-ONLY probe.
#   * There is no verbose flag. On 2026-08-05 `curl -v` was paired with an
#     interactive prompt: that closes the argv channel and opens stdout, and
#     the password went to the terminal and had to be rotated. Closing one
#     channel is not securing a secret.
#   * ssl.create_default_context() means hostname verification is ON. A
#     successful login is therefore a second, differently-instrumented
#     confirmation of measurement M3.
#
# RUN:  chmod +x ftp-jail-check.py && ./ftp-jail-check.py
##############################################################################
from __future__ import annotations

import ftplib
import getpass
import ssl
import sys

HOST = "p3plzcpnl506943.prod.phx3.secureserver.net"
PORT = 21
TIMEOUT = 30
EXPECTED_FILE = "index.html"
MISJAIL_MARKER = "cost"


def basename_ratified(name: str) -> str:
    """The kickoff's remedy for N2."""
    return name.rsplit("/", 1)[-1]


def basename_proposed(name: str) -> str:
    """The remedy this session recommends instead (D2)."""
    return name.strip("/").rsplit("/", 1)[-1]


def basename_current(name: str) -> str:
    """What the committed code does today — the defect."""
    return name.strip("./")


def main() -> int:
    print(f"target : {HOST}:{PORT}  (explicit FTPS, hostname verification ON)")
    user = input("FTP user     : ").strip()
    password = getpass.getpass("FTP password : ")
    if not user or not password:
        print("both a user and a password are required", file=sys.stderr)
        return 2

    context = ssl.create_default_context()
    context.check_hostname = True
    context.verify_mode = ssl.CERT_REQUIRED

    session = ftplib.FTP_TLS(context=context, timeout=TIMEOUT)
    try:
        session.connect(HOST, PORT)
        session.auth()
        session.login(user, password)
        session.prot_p()
        session.set_pasv(True)
    except Exception as exc:  # noqa: BLE001 — report, never swallow
        print(f"\nCONNECT/LOGIN FAILED: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1
    finally:
        password = ""  # drop the reference as soon as it is no longer needed

    try:
        # --- 3 · the transport control ------------------------------------
        cert = session.sock.getpeercert()  # type: ignore[union-attr]
        issuer = {k: v for part in cert.get("issuer", ()) for k, v in part}
        subject = {k: v for part in cert.get("subject", ()) for k, v in part}
        print("\n=== TRANSPORT CONTROL (must be Starfield, not a proxy) ===")
        print(f"  subject CN : {subject.get('commonName')}")
        print(f"  issuer  O  : {issuer.get('organizationName')}")
        print(f"  issuer  CN : {issuer.get('commonName')}")
        print(f"  notBefore  : {cert.get('notBefore')}")
        print(f"  notAfter   : {cert.get('notAfter')}")

        # --- 1 · the jail --------------------------------------------------
        print("\n=== PWD ===")
        print(f"  {session.pwd()!r}")

        print("\n=== NLST, VERBATIM (repr — slashes and whitespace visible) ===")
        entries = session.nlst()
        for entry in entries:
            print(f"  {entry!r}")

        print("\n=== LIST ===")
        session.retrlines("LIST", lambda line: print(f"  {line}"))

        # --- 2 · the answer shape -----------------------------------------
        print("\n=== WHAT EACH BASENAME RULE MAKES OF THOSE ENTRIES ===")
        print(f"  {'raw':<28} {'current (defect)':<22} {'ratified':<18} proposed")
        for entry in entries:
            print(
                f"  {entry!r:<28} {basename_current(entry)!r:<22} "
                f"{basename_ratified(entry)!r:<18} {basename_proposed(entry)!r}"
            )

        # --- verdicts -------------------------------------------------------
        proposed = {basename_proposed(e) for e in entries}
        print("\n=== VERDICTS ===")
        print(
            f"  jail correct (no {MISJAIL_MARKER!r} visible)      : "
            f"{'PASS' if MISJAIL_MARKER not in proposed else 'FAIL — MIS-JAILED'}"
        )
        print(
            f"  {EXPECTED_FILE!r} present (gates decision D3) : "
            f"{'PASS' if EXPECTED_FILE in proposed else 'ABSENT — D3 NOT SAFE TO ADOPT'}"
        )
        stale = {"status", "assets", "public_html", "mail", "etc"} & proposed
        print(
            f"  no account-home markers visible           : "
            f"{'PASS' if not stale else f'FAIL — saw {sorted(stale)}'}"
        )
    finally:
        try:
            session.quit()
        except ftplib.all_errors:
            session.close()

    print("\nNothing was written, renamed or deleted. Read-only probe complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
