#!/usr/bin/env python3
"""B461 boundary compute: the full L6a4 SL(3) census — 1000 unit-modulus seeded
Newton starts per class, Jacobian classification, PSLQ field recognition."""
import json
import numpy as np
import sympy as sp
import mpmath as mp

np.seterr(all="ignore")
mp.mp.dps = 30
rng = np.random.default_rng(46100)
d = json.load(open('ptolemy_systems.json'))

def build(ci):
    sys_ = d['L6a4']['3'][ci]
    vars_ = [sp.Symbol(v) for v in sys_['vars']]
    eqs = [sp.sympify(e) for e in sys_['eqs']]
    F = sp.lambdify(vars_, eqs, modules='numpy')
    J = sp.lambdify(vars_, sp.Matrix(eqs).jacobian(vars_), modules='numpy')
    return len(vars_), F, J

def newton(nv, F, J, x0, iters=140):
    x = x0.copy()
    for it in range(iters):
        f = np.array(F(*x), dtype=complex)
        Jm = np.array(J(*x), dtype=complex)
        try: dx, *_ = np.linalg.lstsq(Jm, -f, rcond=None)
        except np.linalg.LinAlgError: return None
        x = x + (0.5 if it < 25 else 1.0) * dx
        if not np.all(np.isfinite(x)) or np.max(np.abs(x)) > 1e6: return None
        if np.linalg.norm(f) < 1e-12 and np.linalg.norm(dx) < 1e-12: return x
    return x if np.linalg.norm(np.array(F(*x), dtype=complex)) < 1e-10 else None

for ci in range(len(d['L6a4']['3'])):
    nv, F, J = build(ci)
    sols = []
    for _ in range(1000):
        x0 = np.exp(2j*np.pi*rng.random(nv)) * (0.5 + rng.random(nv))
        x = newton(nv, F, J, x0)
        if x is None: continue
        if np.min(np.abs(x)) < 1e-6: continue
        if any(np.linalg.norm(x - s) < 1e-5 for s in sols): continue
        sols.append(x)
    iso, fam, degs = 0, 0, set()
    for x in sols:
        Jm = np.array(J(*x), dtype=complex)
        r = int(np.linalg.matrix_rank(Jm, tol=1e-8))
        if r >= nv:
            iso += 1
            val = complex(np.sum(x))
            try:
                if abs(val.imag) < 1e-10:
                    p = mp.findpoly(mp.mpf(val.real), 10, maxcoeff=10**5)
                else:
                    # real-subfield probe: minpoly of val + conj(val) (degree lower bound)
                    p = mp.findpoly(mp.mpf(2*val.real), 10, maxcoeff=10**5)
                if p:
                    degs.add(sp.Poly(list(p), sp.Symbol('t')).degree())
            except Exception:
                pass
        else:
            fam += 1
    print(f"class {ci:2d}: nv={nv} solutions={len(sols)} isolated={iso} on-family={fam} "
          f"iso-field-degrees={sorted(degs)}", flush=True)
print("CENSUS DONE", flush=True)
