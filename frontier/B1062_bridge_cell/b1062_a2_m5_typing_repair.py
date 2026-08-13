"""A5's typing repair (both benches owe it): FULL-TRIPLE typing of the m = 5
deg-18 geometric candidate via numeric back-solve — least_squares from multiple
starts at each z-root, residual-verified on ALL FOUR closed-form equations,
then the asymmetry principle applied: certification requires all three
coordinates typed at every root.

Runs AFTER the follow-up bank (this file moves into frontier/B1062_bridge_cell/
with the chain; never mid-suite). Route: the m = 4 numeric precedent
(b1062_v2_block2n.py), applied to the closed-Chebyshev system(5).
"""
import numpy as np
import sympy as sp
from scipy.optimize import least_squares

x, y, z = sp.symbols('x y z')

def U(n, s):
    if n < 0: return sp.Integer(0)
    a, b = sp.Integer(1), s
    if n == 0: return a
    for _ in range(n - 1):
        a, b = b, sp.expand(s*b - a)
    return b

def system(m):
    Pm, Qm = U(m-1, x), U(m-2, x)
    Pm1 = U(m, x)
    t = sp.expand(Pm*z - Qm*y)
    tsa = sp.expand(Pm1*z - Pm*y)
    Cm2, Cm1, Cm = U(m-2, t), U(m-1, t), U(m, t)
    Ta  = sp.expand(Cm1*tsa - Cm2*x)
    Tb  = t
    Tab = sp.expand(Cm*tsa - Cm1*x)
    return [sp.expand(Ta - x), sp.expand(Tb - y), sp.expand(Tab - z),
            x**2 + y**2 + z**2 - x*y*z]

DEG18 = sp.Poly(
    [1, -1, 16, -13, 130, -74, 658, -145, 2007, -433, 4147, -798, 5032,
     -779, 2831, -29, 739, -99, 39], z)   # the RAW deg-18 factor, verbatim

def etype(c):
    if abs(c.imag) > 1e-12: return "lox"
    if abs(c.real) < 2 - 1e-12: return "ELL"
    return "par/hyp"

eqs = system(5)
f_num = [sp.lambdify((x, y, z), e, 'numpy') for e in eqs]

def residual(v, zc):
    xv, yv = v[0] + 1j*v[1], v[2] + 1j*v[3]
    r = [f(xv, yv, zc) for f in f_num]
    out = []
    for c in r:
        out += [c.real, c.imag]
    return out

rng = np.random.default_rng(20260813)
roots = DEG18.nroots(n=30, maxsteps=500)
typed, fails = [], 0
for zr in roots:
    zc = complex(zr)
    best = None
    for _ in range(60):
        v0 = rng.normal(0, 3, 4)
        sol = least_squares(residual, v0, args=(zc,), xtol=1e-14, ftol=1e-14,
                            gtol=1e-14, max_nfev=4000)
        if best is None or sol.cost < best.cost:
            best = sol
        if sol.cost < 1e-22:
            break
    xv, yv = best.x[0] + 1j*best.x[1], best.x[2] + 1j*best.x[3]
    res = max(abs(complex(f(xv, yv, zc))) for f in f_num)
    if res > 1e-9:
        fails += 1
        print(f"[repair] z={zc:.6f}: BACK-SOLVE FAIL (residual {res:.2e})", flush=True)
        continue
    tri = (etype(xv), etype(yv), etype(zc))
    typed.append(tri)
    print(f"[repair] z={zc:.6f}: ({tri[0]},{tri[1]},{tri[2]})  res={res:.1e}", flush=True)

n_ell = sum(1 for t in typed if "ELL" in t)
n_lox = sum(1 for t in typed if t == ("lox", "lox", "lox"))
print(f"[repair] SUMMARY: typed {len(typed)}/18, fails {fails}, "
      f"elliptic-bearing {n_ell}, all-lox {n_lox}", flush=True)
print("[repair] CERTIFICATION:",
      "ALL-LOX CERTIFIED (full triple, every root)" if (fails == 0 and n_ell == 0
      and n_lox == len(typed) == 18) else
      "NOT certified — the honest state stands", flush=True)
