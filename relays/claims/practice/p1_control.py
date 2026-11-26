#!/usr/bin/env python3
"""Practice card P1's failing control (main, 2026-11-26; P-885): B1993's signs_posthoc.py run unchanged but for its moves,
cut to L and L^-1 alone (R and R^-1 dropped), so that the orbits must come apart.
    python3 relays/claims/practice/p1_control.py
Exit 1 with a last line opening "CONTROL FAILS:" when the decisive line does not come out; 0 when it survives; 3 for an
invalid run (a crash included)."""
import contextlib, io, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[3]
f = sorted(ROOT.glob("frontier/B1993_*"))[0] / "verification" / "signs_posthoc.py"
src = f.read_text()
old = "moves = [lambda v: (v[0], v[2], v[0] * v[2] - v[1]), lambda v: (v[2], v[1], v[1] * v[2] - v[0]),\n         lambda v: (v[0], v[0] * v[1] - v[2], v[1]), lambda v: (v[0] * v[1] - v[2], v[1], v[0])]"
if src.count(old) != 1:
    print("CONTROL INVALID: the moves are not as written"); sys.exit(3)
src = src.replace(old, "moves = [lambda v: (v[0], v[2], v[0] * v[2] - v[1]), lambda v: (v[0], v[0] * v[1] - v[2], v[1])]")
out = io.StringIO()
try:
    with contextlib.redirect_stdout(out):
        exec(compile(src, str(f), "exec"), {"__name__": "__main__"})
except Exception as e:
    print("CONTROL INVALID: the changed script raised %s" % type(e).__name__); sys.exit(3)
text = out.getvalue()
print(text.strip().splitlines()[-1])
if "fall into 1 orbit(s) of sizes [210]" in text:
    print("CONTROL DID NOT FAIL: the two orbits survive with R and R^-1 dropped"); sys.exit(0)
print("CONTROL FAILS: as it must, with L and L^-1 alone the readings do not form the two orbits"); sys.exit(1)
