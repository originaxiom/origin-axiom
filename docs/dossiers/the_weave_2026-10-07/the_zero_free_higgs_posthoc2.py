#!/usr/bin/env python3
"""W133, POST HOC, second pass: why the first pass's numerical check failed in h(4, 1) (up to 7.7e10) while h(12, 1)
and h(20, 1) passed to 1e-27. Nothing here was in the rule.

  D1  the same eigenvector points in h(4, 1) at 100 and at 300 digits: per point, the largest relative residual of
      W133's cubic equations (|equation| over the sum of its terms' sizes)
  D2  per point, |N'(g) / eta^(-3) - 1| at tau = 1.5i, 2.5i and 3.5i (larger Im tau makes the series' truncation
      negligible)

    python3 -B the_zero_free_higgs_posthoc2.py      # writes the_zero_free_higgs_posthoc2.json beside itself
"""
import contextlib
import io
import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_zero_free_higgs_posthoc as PH  # noqa: E402  (the first pass: points, ratio; W133's system)

W133 = PH.W133
OUT = HERE / "the_zero_free_higgs_posthoc2.json"


def rel_residual(eqs, gens, p):
    worst = mp.mpf(0)
    for e in eqs:
        terms = sp.Add.make_args(sp.expand(e))
        vals = [complex_val(t, gens, p) for t in terms]
        worst = max(worst, abs(mp.fsum(vals)) / mp.fsum(abs(v) for v in vals))
    return worst


def complex_val(term, gens, p):
    c, mon = term.as_coeff_Mul()
    c = sp.Rational(c)
    v = mp.mpf(c.p) / c.q
    for g, x in zip(gens, p):
        v *= x ** int(sp.degree(mon, g)) if mon != 1 else 1
    return v


def main():
    forms, a, eqs, _, _ = W133.cubic_system(4, 1)
    G = sp.groebner(eqs, *a, order="grevlex", domain=sp.QQ)
    out = {}
    for dps in (100, 300):
        mp.mp.dps = dps
        PH._EV.clear()
        pts, nB, nd, gap = PH.points(G, a)
        res = [rel_residual(eqs, a, p) for p in pts]
        taus = (mp.mpc(0, "1.5"), mp.mpc(0, "2.5"), mp.mpc(0, "3.5"))
        dev = [[abs(PH.ratio(forms, p, 4, t) - 1) for t in taus] for p in pts]
        out[f"{dps} digits"] = {
            "distinct eigenvalues": nd,
            "max relative residual of the cubic equations over the points": float(max(res)),
            "points with relative residual < 1e-20": sum(1 for x in res if x < mp.mpf("1e-20")),
            "max |N'/eta^-3 - 1| at 1.5i, 2.5i, 3.5i": [float(max(d[k] for d in dev)) for k in range(3)],
            "points with |N'/eta^-3 - 1| < 1e-10 at 2.5i": sum(1 for d in dev if d[1] < mp.mpf("1e-10")),
            "the worst point: residual, deviations": [float(res[max(range(len(pts)), key=lambda k: dev[k][0])]),
                                                     [float(x) for x in max(dev, key=lambda d: d[0])]]}
    OUT.write_text(json.dumps({"arc": "W133", "status": "POST HOC, second pass", **out}, indent=1) + "\n",
                   encoding="utf-8")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
