"""B606 cells NF-0 and NF-1 (sealed order; the pre-run realization is
banked at #975-class before this ran).

NF-0 (stage-constant gates): N_{Q(zeta5)/Q}(h3) = 1/5 exactly (via the
minimal polynomial); the E6_2 amplitude norm-product = 1/49 exactly.
NF-1 (the sealed scan): the exact identity N(c4) tau8^{k8} = N(c8)
tau4^{k4} over (k4, k8) in {-3..3}^2, as Fractions.
"""
from fractions import Fraction as Fr

import sympy as sp

# ---- NF-0 -------------------------------------------------------------------
phi = (1 + sp.sqrt(5)) / 2
h3 = 1 / (2 * phi) + sp.I * sp.sin(2 * sp.pi / 5) / sp.sqrt(5)
x = sp.symbols('x')
mp = sp.minimal_polynomial(h3, x)
deg = sp.degree(mp, x)
N_h3 = sp.Rational(sp.LC(mp, x)) ** (-1) * mp.subs(x, 0) * (-1) ** deg
N_h3 = sp.nsimplify(sp.simplify(N_h3))
print(f"NF-0(i): minpoly(h3) = {mp} (degree {deg}); "
      f"N(h3) = {N_h3}  [expected 1/5: {sp.simplify(N_h3 - sp.Rational(1,5)) == 0}]",
      flush=True)
assert sp.simplify(N_h3 - sp.Rational(1, 5)) == 0, "NF-0(i) gate failed"

prod = sp.Integer(1)
for jp in (1, 3, 2):
    amp2 = sp.Rational(4, 7) * sp.sin(2 * sp.pi * jp / 7) ** 2
    prod *= amp2
prod = sp.simplify(prod)
# sympy does not collapse the sine product; certify via the classical
# identity sin(pi/7) sin(2pi/7) sin(3pi/7) = sqrt(7)/8 at 60 digits
dev = abs(prod.evalf(60) - sp.Rational(1, 49).evalf(60))
print(f"NF-0(ii): E6_2 amplitude norm-product = 1/49 to 60 digits "
      f"(dev {float(dev):.1e}; exact value = (4/7)^3 (sqrt7/8)^2 by the "
      f"classical product identity)", flush=True)
assert dev < sp.Rational(1, 10) ** 50, "NF-0(ii) gate failed"

# ---- NF-1 -------------------------------------------------------------------
N4 = 2096640
N8 = 536481792000
T4 = 260736
T8 = 100636318520821923840
Nc4 = 4 * N4 ** 2
Nc8 = 4 * N8 ** 2
hits = []
for k4 in range(-3, 4):
    for k8 in range(-3, 4):
        lhs = Fr(Nc4) * Fr(T8) ** k8
        rhs = Fr(Nc8) * Fr(T4) ** k4
        if lhs == rhs:
            hits.append((k4, k8))
print(f"NF-1: exact hits over |k| <= 3: {hits if hits else 'NONE'}",
      flush=True)
print(f"NF-1 residual at k = (0,0): N(c8)/N(c4) = "
      f"{Fr(Nc8, Nc4)} = (N8/N4)^2", flush=True)
verdict = "A/B-nf path (hit found; NF-2 conditional runs)" if hits else \
          "D-nf (all-fail, as the registered pre-run realization predicted)"
print(f"\nB606 VERDICT INPUT: {verdict}", flush=True)
print("B606 CELLS DONE", flush=True)
