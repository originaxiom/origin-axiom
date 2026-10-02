#!/usr/bin/env python3
"""The parabolic point of the branch to 200 digits, and integer relations for its invariants."""
import sys, json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import branch_obstruction as bo, branch_parabolic as bp
from mpmath import mp, mpf, mpc, matrix, nstr, norm, zeros, inverse, findpoly, pslq
bp.print = lambda *a, **k: None
d = json.load(open(HERE / "parabolic_point.json"))["matrices"]
mp.dps = 60
R = {g: matrix([[mpc(mpf(e[0]), mpf(e[1])) for e in row] for row in d[name]]) for g, name in ((1, "x"), (2, "y"), (3, "t"))}
for dps in (120, 230):
    mp.dps = dps
    R = {g: matrix([[mpc(R[g][i, j]) for j in range(3)] for i in range(3)]) for g in (1, 2, 3)}
    for it in range(12):
        R, nb = bp.step(R, [mpc(0), mpc(0)], delta=mpf(10) ** (-(dps // 2)))[:2]
        if nb < mpf(10) ** (-(dps - 25)): break
    print("dps %d: residual %s after %d steps" % (dps, nstr(nb, 3), it + 1), flush=True)
tr = lambda m: m[0, 0] + m[1, 1] + m[2, 2]
vals = {"tr x": tr(R[1]), "tr y": tr(R[2]), "tr x^-1": tr(inverse(R[1])), "tr y^-1": tr(inverse(R[2])), "tr xy": tr(R[1] * R[2])}
out = {}
for name, v in vals.items():
    print(name, "=", nstr(v, 60), flush=True)
    out[name] = dict(value=[nstr(v.real, 190), nstr(v.imag, 190)])
    for part, x in (("re", v.real), ("im", v.imag)):
        if abs(x) < mpf(10) ** (-150): out[name][part] = "0"; continue
        for deg in (6, 12, 18, 24):
            p = findpoly(x, deg, maxcoeff=10 ** 6, tol=mpf(10) ** (-170), maxsteps=10 ** 6)
            if p: out[name][part] = dict(degree=len(p) - 1, polynomial=[int(c) for c in p]); print("   %s part: degree %d polynomial %s" % (part, len(p) - 1, p), flush=True); break
        else: out[name][part] = "no integer polynomial of degree <= 24 with coefficients below 10^6"; print("   %s part: none to degree 24" % part, flush=True)
json.dump(out, open(HERE / "parabolic_point_field.json", "w"), indent=1)
