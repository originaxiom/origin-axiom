#!/usr/bin/env python3
"""Practice card P3's failing control (main, 2026-11-26; P-885): the same check for an entry equal to 6 in place of 3,
which (3, 3, 3) does not have. Exit 1 with a last line opening "CONTROL FAILS:" when the claim does not come out; 0 when it
does; 3 for an invalid run."""
import pathlib, subprocess, sys
here = pathlib.Path(__file__).resolve().parent
r = subprocess.run([sys.executable, str(here / "p3_threes.py"), "--entry", "6"], capture_output=True, text=True)
if r.returncode not in (0, 1) or "DECISIVE: each has" not in r.stdout:
    print("CONTROL INVALID: the run did not complete"); sys.exit(3)
print(r.stdout.strip().splitlines()[-1])
if r.returncode == 0:
    print("CONTROL DID NOT FAIL: the claim comes out with the entry 6"); sys.exit(0)
print("CONTROL FAILS: as it must, with the entry 6 the claim does not come out"); sys.exit(1)
