#!/usr/bin/env python3
"""B893 completion -- M7: the signature of C (ad-spectrum type per torus direction)
+ M3: the sign of det14 at ALL THREE roots (is the SM wall complex everywhere?)."""
import json
import os
import pickle

import mpmath
import sympy as sp
from mpmath import mp

HERE = os.path.dirname(os.path.abspath(__file__))
B854 = os.path.normpath(os.path.join(HERE, "..", "B854_centralizer_exact",
                                     "e6_centralizer.py"))
CUBIC = [500716339200, -159667200, -28224, 1]
mp.dps = 30
g = {"__file__": B854, "__name__": "b854"}
exec(compile(open(B854).read(), B854, "exec"), g)
DIM, N = g["DIM"], g["N"]
br, hvec, evec, ROOTS = g["br"], g["hvec"], g["evec"], g["ROOTS"]
basis = [hvec(i) for i in range(N)] + [evec(r) for r in ROOTS]
triples = {}
for p in range(DIM):
    for qq in range(DIM):
        v = br(basis[p], basis[qq])
        for r, c in enumerate(v):
            if c:
                triples.setdefault(p, []).append((qq, r, c))


def admat_num(vec):
    A = mp.zeros(DIM, DIM)
    for p in range(DIM):
        vp = vec[p]
        if not vp:
            continue
        vpf = mp.mpf(vp.numerator) / mp.mpf(vp.denominator)
        for qq, r, c in triples.get(p, []):
            A[r, qq] += vpf * mp.mpf(c.numerator) / mp.mpf(c.denominator)
    return A


print("[M7] ad-spectrum type per torus direction...")
res = {"signature": {}}
import random
random.seed(5)
combos = {f"x{n}": g["INV"][n] for n in (8, 14, 16, 22)}
for name, vec in combos.items():
    A = admat_num(vec)
    Mc = mp.matrix(DIM, DIM)
    for i in range(DIM):
        for j in range(DIM):
            Mc[i, j] = mp.mpc(A[i, j])
    E = mpmath.eig(Mc, left=False, right=False)
    nreal = nimag = ncplx = nzero = 0
    for k in range(DIM):
        ev = E[k]
        if abs(ev) < mp.mpf("1e-12"):
            nzero += 1
        elif abs(mp.im(ev)) < abs(ev) * mp.mpf("1e-10"):
            nreal += 1
        elif abs(mp.re(ev)) < abs(ev) * mp.mpf("1e-10"):
            nimag += 1
        else:
            ncplx += 1
    res["signature"][name] = dict(zero=nzero, real=nreal, imag=nimag,
                                  complex=ncplx)
    print(f"    ad({name}): zero {nzero}, real {nreal}, imaginary {nimag}, "
          f"generic-complex {ncplx}")

print("[M3] det14 at all three roots (the c-consumption check)...")
S = os.environ["SCRATCH"]  # session scratchpad holding the solo tower pickle
D = pickle.load(open(os.path.join(S, "b12_tower.pkl"), "rb"))
det14 = D["det14"]
rho = sp.symbols("rho")
MU = 500716339200 * rho**3 - 2075673600 * rho**2 - 4769856 * rho + 2197
roots = sorted(sp.nsolve(MU, rho, x0) for x0 in (-0.002, 0.0004, 0.006))
signs = []
for r0 in roots:
    u = sum(sp.Float(sp.Rational(c), 30) * r0**i
            for i, c in enumerate(det14[0]))
    v = sum(sp.Float(sp.Rational(c), 30) * r0**i
            for i, c in enumerate(det14[1]))
    assert abs(v) < 1e-20, "gamma-part must vanish"
    signs.append(float(u))
    print(f"    root {sp.N(r0, 8)}: det14 = {sp.N(u, 6)}  "
          f"=> a {'IMAGINARY' if u > 0 else 'REAL'}")
res["det14_at_roots"] = signs
res["wall_complex_at_all_roots"] = all(u > 0 for u in signs)
print(f"    THE WALL IS COMPLEX AT ALL THREE ROOTS: "
      f"{res['wall_complex_at_all_roots']}")
json.dump(res, open(os.path.join(HERE, "signature_results.json"), "w"),
          indent=1)
print("done")
