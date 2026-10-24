#!/usr/bin/env python3
"""W151, POST HOC (labelled; written after the one run of the_two_object_route.py was read): Q4's direct evaluation
failed on 16 pairs at y = 6 and 8. The diagnosis, by hand before this script: every one of them has F-6 or F-10 as
a member, whose e1 coefficient is 2^a (1/64, 1/1024), so the census's leading term overtakes only beyond y of
about 9 to 14. This script repeats the direct evaluation (the same kappa = 0.37 + 0.81i, 100 digits) on those pairs
over y windows [6, 8], [10, 12], [14, 16], [20, 24] and [28, 32]. Expected, stated before the run: on [28, 32]
every pair's rounded E equals the census's.

    python3 -B the_two_object_route_posthoc.py      # writes the_two_object_route_posthoc.json beside itself
"""
import contextlib
import io
import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_higgs_invariant_dichotomy as W146  # noqa: E402

OUT = HERE / "the_two_object_route_posthoc.json"
mp.mp.dps = 100
KAPPA = mp.mpc("0.37", "0.81")
WINDOWS = ((6, 8), (10, 12), (14, 16), (20, 24), (28, 32))


def value(name, y):
    base = name[5:] if name.startswith("conj ") else name
    v = W146.record_form(base, mp.mpc(0, y))
    return W146.conj(v) if name.startswith("conj ") else v


def lnI(a, b, y):
    A, B = value(a, y), value(b, y)
    h = [A[k] + KAPPA * B[k] for k in range(3)]
    return mp.log(abs(W146.dot(h, h))) - mp.log(W146.nrm2(h))


def main():
    run = json.loads((HERE / "the_two_object_route.json").read_text(encoding="utf-8"))
    mism = run["Q4"]["direct E at kappa = 0.37 + 0.81i: mismatches"]
    rows, ok = [], True
    for lab, E_census, E_direct in mism:
        a, b = lab.split(" + ")
        per = {}
        for y0, y1 in WINDOWS:
            r = -(lnI(a, b, y1) - lnI(a, b, y0)) / (2 * mp.pi * (y1 - y0)) * 24
            per["[%d, %d]" % (y0, y1)] = mp.nstr(r, 6)
        last = int(mp.nint(mp.mpf(per["[28, 32]"])))
        ok = ok and last == E_census
        rows.append({"pair": lab, "census E": E_census, "direct E at [6, 8], rounded": E_direct,
                     "direct E (24ths) per window": per, "rounded on [28, 32]": last})
    out = {"arc": "W151", "status": "POST HOC (labelled)", "pairs": len(rows), "rows": rows,
           "every pair's rounded E on [28, 32] equals the census's": bool(ok)}
    OUT.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print(out["every pair's rounded E on [28, 32] equals the census's"])


if __name__ == "__main__":
    main()
