"""A5 typing repair v2 — DETERMINISTIC full-triple typing (no optimization).
Key identity: eq2 (Tb - y = 0) is LINEAR in y: t = P5(x)z - Q5(x)y = y
  =>  y(x, z) = P5(x)·z / (1 + Q5(x)).
Substitute into eq1 (Ta - x) at fixed numeric z-root -> a one-variable
polynomial-like function of x; find its roots via companion-matrix on the
numerator polynomial; verify every candidate on ALL FOUR equations; type.
Complete and deterministic: every (x, y, z) point over each z-root is found.
"""
import numpy as np
import sympy as sp

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
t_expr  = P5*z - Q5*y
tsa     = P6*z - P5*y
C3_, C4_, C5_ = U(m-2, t_expr), U(m-1, t_expr), U(m, t_expr)
eqs = [sp.expand(C4_*tsa - C3_*x - x),          # Ta - x
       sp.expand(t_expr - y),                    # Tb - y
       sp.expand(C5_*tsa - C4_*x - z),           # Tab - z
       sp.expand(x**2 + y**2 + z**2 - x*y*z)]    # Markov

# y as a rational function of (x, z) from eq2
y_sub = P5*z/(1 + Q5)

# eq1 with y substituted -> rational in (x, z); numerator polynomial in x
e1_sub = sp.together(eqs[0].subs(y, y_sub))
num1 = sp.expand(sp.numer(e1_sub))
den1 = sp.expand(sp.denom(e1_sub))
poly1 = sp.Poly(num1, x)
print(f"[v2] eq1 numerator degree in x: {poly1.degree()}", flush=True)

f_all = [sp.lambdify((x, y, z), e, 'numpy') for e in eqs]
denf  = sp.lambdify((x, z), den1, 'numpy')
coeff = [sp.lambdify(z, c, 'numpy') for c in poly1.all_coeffs()]
qf    = sp.lambdify(x, 1 + Q5, 'numpy')
y_f   = sp.lambdify((x, z), y_sub, 'numpy')

DEG18 = sp.Poly(
    [1, -1, 16, -13, 130, -74, 658, -145, 2007, -433, 4147, -798, 5032,
     -779, 2831, -29, 739, -99, 39], z)

def etype(c):
    if abs(c.imag) > 1e-10: return "lox"
    if abs(c.real) < 2 - 1e-10: return "ELL"
    return "par/hyp"

roots = DEG18.nroots(n=30, maxsteps=500)
summary, fails = [], 0
for zr in roots:
    zc = complex(zr)
    cs = np.array([complex(c(zc)) for c in coeff])
    xs = np.roots(cs)
    found = []
    for xc in xs:
        if abs(complex(qf(xc))) < 1e-12:   # y-substitution invalid there
            continue
        yc = complex(y_f(xc, zc))
        res = max(abs(complex(f(xc, yc, zc))) for f in f_all)
        if res < 1e-8:
            found.append((xc, yc, res))
    if not found:
        fails += 1
        print(f"[v2] z={zc:.6f}: NO verified (x,y) on this branch", flush=True)
        continue
    # the geometric component's point(s) over this z-root:
    tags = sorted({(etype(xc), etype(yc), etype(zc)) for xc, yc, _ in found})
    best = min(f[2] for f in found)
    summary.append((zc, tags))
    print(f"[v2] z={zc:.6f}: {len(found)} verified point(s), types {tags}, best res {best:.1e}",
          flush=True)

n_ell = sum(1 for _, tags in summary if any('ELL' in t for t in tags))
n_lox_only = sum(1 for _, tags in summary if tags == [("lox", "lox", "lox")])
print(f"[v2] SUMMARY: z-roots resolved {len(summary)}/18, fails {fails}, "
      f"elliptic-bearing roots {n_ell}, pure-all-lox roots {n_lox_only}", flush=True)
verdict = (fails == 0 and n_ell == 0 and n_lox_only == 18)
print("[v2] CERTIFICATION:",
      "ALL-LOX CERTIFIED — full triple, every root, deterministic route"
      if verdict else "NOT certified — state the counts honestly", flush=True)
