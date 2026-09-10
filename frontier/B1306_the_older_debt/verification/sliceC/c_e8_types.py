"""C5 -- fc R64 (the w_{A2} half): on main's own E8 root system (B1275), the Weyl rotation w = s_a s_b of an A2 plane has order 3, fixed dimension 6,
and fixes exactly the 72 roots of the plane's centraliser E6. (The L_g half needs the icosian model: the seat's, re-run only.)"""
import sys, importlib.util, pathlib
from fractions import Fraction as F
# resolve the repository root from this file's own location, so the script runs in any clone
_ROOT = pathlib.Path(__file__).resolve().parents[4]
_E8 = _ROOT / "frontier" / "B1275_e8_family_verified" / "verification" / "e8_family.py"
spec = importlib.util.spec_from_file_location("e8", str(_E8)); e8 = importlib.util.module_from_spec(spec); spec.loader.exec_module(e8)
roots, Rset, a, b, A2, E6, rest = e8.decompose()
def refl(v, r): d = e8.dot(v, r); return tuple(x - d * y for x, y in zip(v, r))   # roots have norm 2
def w(v): return refl(refl(v, b), a)
imgs = {r: w(r) for r in roots}
order = 1; v = tuple(F(1) if i == 0 else F(0) for i in range(8)); u = w(v)
while u != v: u = w(u); order += 1
fixed_roots = [r for r in roots if imgs[r] == r]
import sympy as sp
Wm = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in w(tuple(F(1) if j == i else F(0) for j in range(8)))] for i in range(8)]).T
fixed_dim = 8 - (Wm - sp.eye(8)).rank()
print("order of w:", order, " fixed dimension:", fixed_dim, " fixed roots:", len(fixed_roots), " = the E6 centraliser:", set(fixed_roots) == E6, "(|E6| =", len(E6), ")")
ok = order == 3 and fixed_dim == 6 and set(fixed_roots) == E6 and len(E6) == 72
print("C5 (w_{A2} half):", "PASS" if ok else "FAIL")
