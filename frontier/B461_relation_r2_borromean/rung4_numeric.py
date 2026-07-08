#!/usr/bin/env python3
"""B461 rung 4 (the ladder's numeric fallback for L6a4): multi-start Newton on the
SL(3) Ptolemy systems per obstruction class; solutions deduped; Jacobian rank
classifies isolated vs family; field recognition via PSLQ minpolys (degree <= 8)."""
import json
import numpy as np
import sympy as sp
import mpmath as mp

np.seterr(all="ignore")
mp.mp.dps = 30
rng = np.random.default_rng(461)
d = json.load(open('ptolemy_systems.json'))

def build(nm, ci):
    sys_ = d[nm]['3'][ci]
    vars_ = [sp.Symbol(v) for v in sys_['vars']]
    eqs = [sp.sympify(e) for e in sys_['eqs']]
    F = sp.lambdify(vars_, eqs, modules='numpy')
    J = sp.lambdify(vars_, sp.Matrix(eqs).jacobian(vars_), modules='numpy')
    return len(vars_), F, J

def newton(nv, F, J, x0, iters=80):
    x = x0.copy()
    for _ in range(iters):
        f = np.array(F(*x), dtype=complex)
        Jm = np.array(J(*x), dtype=complex)
        try:
            dx, *_ = np.linalg.lstsq(Jm, -f, rcond=None)
        except np.linalg.LinAlgError:
            return None
        x = x + dx
        if not np.all(np.isfinite(x)) or np.max(np.abs(x)) > 1e8:
            return None
        if np.linalg.norm(f) < 1e-12 and np.linalg.norm(dx) < 1e-12:
            return x
    return x if np.linalg.norm(np.array(F(*x), dtype=complex)) < 1e-10 else None

def minpoly_of(z, maxdeg=8):
    for deg in range(1, maxdeg + 1):
        basis = [mp.mpc(z)**k for k in range(deg + 1)]
        rel = mp.pslq([mp.re(b) for b in basis], maxcoeff=10**6, maxsteps=20000)
        # need complex pslq: use real+imag stacked via 2 relations — simpler: mp.findpoly
        p = mp.findpoly(mp.mpc(z), deg, maxcoeff=10**5)
        if p:
            poly = sp.Poly(list(p), sp.Symbol('x'))
            if poly.degree() >= 1:
                return poly
    return None

for nm in ['L6a4']:
    print(f"== {nm} SL(3) numeric rung ==", flush=True)
    for ci in range(len(d[nm]['3'])):
        nv, F, J = build(nm, ci)
        sols = []
        for _ in range(150):
            x0 = rng.standard_normal(nv) + 1j * rng.standard_normal(nv)
            x = newton(nv, F, J, x0)
            if x is None: continue
            if np.min(np.abs(x)) < 1e-6: continue          # degenerate ptolemy coords
            if any(np.linalg.norm(x - s) < 1e-6 for s in sols): continue
            sols.append(x)
        # classify: Jacobian rank at each solution
        iso, fam = 0, 0
        fields = set()
        for x in sols[:40]:
            Jm = np.array(J(*x), dtype=complex)
            r = np.linalg.matrix_rank(Jm, tol=1e-8)
            if r >= nv: iso += 1
            else: fam += 1
            if r >= nv:
                # recognize the field of one coordinate (trace-like: sum of coords)
                val = complex(np.sum(x))
                p = minpoly_of(val, 8)
                if p is not None:
                    fields.add((p.degree(), tuple(p.all_coeffs()[:3])))
        print(f"  class {ci:2d}: {len(sols)} solutions found; isolated {iso}, on-family {fam}; "
              f"field degrees seen: {sorted({f[0] for f in fields})}", flush=True)
print("RUNG4 DONE", flush=True)
