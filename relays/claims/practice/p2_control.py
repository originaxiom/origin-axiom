#!/usr/bin/env python3
"""Practice card P2's failing control (main, 2026-11-26; P-885): the same check with the modulus 7 in place of 9, which no
solution's entries satisfy. Exit 1 with a last line opening "CONTROL FAILS:" when the claim does not come out; 0 when it
does; 3 for an invalid run."""
import pathlib, subprocess, sys
here = pathlib.Path(__file__).resolve().parent
r = subprocess.run([sys.executable, str(here / "p2_mod9.py"), "--modulus", "7"], capture_output=True, text=True)
if r.returncode not in (0, 1) or "DECISIVE: every entry" not in r.stdout:
    print("CONTROL INVALID: the run did not complete"); sys.exit(3)
print(r.stdout.strip().splitlines()[-1])
if r.returncode == 0:
    print("CONTROL DID NOT FAIL: the claim comes out with the modulus 7"); sys.exit(0)
print("CONTROL FAILS: as it must, with the modulus 7 the claim does not come out"); sys.exit(1)
