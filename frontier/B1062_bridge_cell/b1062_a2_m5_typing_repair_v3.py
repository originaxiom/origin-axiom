"""A5 typing repair v3 — the v2 route at 60-digit precision (mpmath.polyroots).
v2's 7 fails were precision artifacts: conjugate pairs split verified/failed,
impossible for real-coefficient systems. Everything here runs in mpmath at
dps=60; the numerator's x-coefficients are exact integer polynomials in z,
evaluated at 50-digit z-roots; residuals verified on all four exact equations.
"""
import sympy as sp
from mpmath import mp, mpc, polyroots, fabs

mp.dps = 60
x, y, z = sp.symbols('x y z')

def U(n, s):
    if n < 0: return sp.Integer(0)
    a, b = sp.Integer(1), s
    if n == 0: return a
    for _ in range(n - 1):
        a, b = b, sp.expand(s*b - a)
    return b

m = 5
P5, Q5 = U(m-1, x), U(m-2, x)
P6 = U(m, x)
t_expr = P5*z - Q5*y
tsa    = P6*z - P5*y
C3_, C4_, C5_ = U(m-2, t_expr), U(m-1, t_expr), U(m, t_expr)
eqs = [sp.expand(C4_*tsa - C3_*x - x),
       sp.expand(t_expr - y),
       sp.expand(C5_*tsa - C4_*x - z),
       sp.expand(x**2 + y**2 + z**2 - x*y*z)]

y_sub = P5*z/(1 + Q5)
num1 = sp.expand(sp.numer(sp.together(eqs[0].subs(y, y_sub))))
poly1 = sp.Poly(num1, x)
coeff_poly = [sp.Poly(c, z) for c in poly1.all_coeffs()]   # integer polys in z
print(f"[v3] numerator degree in x: {poly1.degree()}; dps={mp.dps}", flush=True)

DEG18 = sp.Poly(
    [1, -1, 16, -13, 130, -74, 658, -145, 2007, -433, 4147, -798, 5032,
     -779, 2831, -29, 739, -99, 39], z)
zroots = DEG18.nroots(n=50, maxsteps=1000)

def to_mpc(v): return mpc(str(sp.re(v)), str(sp.im(v)))

def ev_poly(P, zc):
    acc = mpc(0)
    for c in P.all_coeffs():
        acc = acc*zc + int(c)
    return acc

# exact equation evaluators via sympy->mpmath on demand (subs + evalf is slow;
# use lambdify with mpmath backend for full-precision residuals)
f_all = [sp.lambdify((x, y, z), e, 'mpmath') for e in eqs]
y_f   = sp.lambdify((x, z), y_sub, 'mpmath')

def etype(c):
    if fabs(c.imag) > mp.mpf('1e-30'): return "lox"
    if fabs(c.real) < 2 - mp.mpf('1e-30'): return "ELL"
    return "par/hyp"

resolved, fails = [], 0
for zr in zroots:
    zc = to_mpc(zr)
    cs = [ev_poly(P, zc) for P in coeff_poly]
    xs = polyroots(cs, maxsteps=200, extraprec=200)
    found = []
    for xc in xs:
        yc = y_f(xc, zc)
        res = max(fabs(f(xc, yc, zc)) for f in f_all)
        if res < mp.mpf('1e-25'):
            found.append((xc, yc, res))
    if not found:
        fails += 1
        print(f"[v3] z=({complex(zc):.6f}): NO verified point", flush=True)
        continue
    tags = sorted({(etype(xc), etype(yc), etype(zc)) for xc, yc, _ in found})
    best = min(f[2] for f in found)
    resolved.append(tags)
    print(f"[v3] z=({complex(zc):.6f}): {len(found)} pt, {tags}, res {float(best):.1e}",
          flush=True)

n_ell = sum(1 for tags in resolved if any('ELL' in t for t in tags))
n_lox = sum(1 for tags in resolved if tags == [("lox", "lox", "lox")])
print(f"[v3] SUMMARY: resolved {len(resolved)}/18, fails {fails}, "
      f"elliptic-bearing {n_ell}, pure-all-lox {n_lox}", flush=True)
print("[v3] CERTIFICATION:",
      "ALL-LOX CERTIFIED — full triple, all 18 roots, deterministic, 60-digit"
      if (fails == 0 and n_ell == 0 and n_lox == 18)
      else "NOT certified — counts stated honestly", flush=True)
