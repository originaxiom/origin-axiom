#!/usr/bin/env python3
"""Practice card P1 for the banking seats (main, 2026-11-26; P-885). It runs B1993's signs_posthoc.py unchanged, from the
arc's verification folder, and prints its decisive lines marked DECISIVE:.
    python3 relays/claims/practice/p1_two_orbits.py
Exit 0 when the three decisive lines came out; 1 otherwise."""
import pathlib, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[3]
here = sorted(ROOT.glob("frontier/B1993_*"))[0] / "verification"
r = subprocess.run([sys.executable, "-B", "signs_posthoc.py"], cwd=here, capture_output=True, text=True)
lines = [l.rstrip() for l in r.stdout.splitlines() if l.startswith(("nonzero integer readings", "the other 210 readings"))]
for l in lines:
    print("DECISIVE: " + l)
sys.exit(0 if r.returncode == 0 and len(lines) == 2 else 1)
