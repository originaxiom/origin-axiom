"""agy digest, phases 1-9 / audit_395b27210 / Theorems 10-13: the integer and symbolic claims, checked from first
principles (sympy, exact integers).  Nothing is imported from the agy lane's code.  Data-free; no measured number.

Claims checked (ids match the report's ledger):
  P1a  N = gcd(|-3-2|, |6-1|) = 5; in 2..12 only N = 5 is coprime to {1,-4,2,-3,6} and has (-3,6) == (2,1) mod N
  P1b  U = [[1,2],[2,3]]: U(2,0) == (2,4), U(2,1) == (4,2) = 2(2,1) mod 5; U mod 5 is ONE Jordan block, eigenvalue 2
  A1   U0 = [[3,2],[2,1]]: U0(3,1) == 2(3,1) mod 5; (LR)^3 = [[13,8],[8,5]]; det(A^3 - I) = -16; (A^3-I)(2/5,0) == (-1/5,1/5)
       mod Z^2, not in (1/2)Z^2; A^3 fixes no nonzero 5-torsion point; [[1,2],[6,13]] in Gamma(2) maps (1,1) to (3,3) mod 8
  T10a A_sig^3 = [[13,-8],[-8,5]]; det(A_sig^3 + I) = 20; (A_sig^3 + I)(2/5,1/5) = (4,-2); B = (A_sig^3 - I)/4, U B = -I
  T10b the 5-torsion points x with A_sig^3 x == +-x (mod 5): census over all 24 nonzero points; the lines (2/5, j/5)
  T10c the rank-2 local system: chi(A gamma) = chi(gamma)^-1 on Z^2 and J diag(c, 1/c) J^-1 = diag(1/c, c)
  T10d the determinant-phase arithmetic: the code's phases (2pi/25, -4pi/5, 4pi/5) and the relay's (-2pi/5, 4pi/25, -12pi/25)
  T11a SNF(A_sig^3 - I) = diag(4, 4); H_1(3-fold cyclic cover of m004) from SnapPy
  A2   chi'(k) = (-1)^k exp(i pi k^2/4): same polarization as chi; differs at k = 1, agrees at k = -2
  A2'  det(a0 I + h.Q) = a0^2 + h.h (symbolic, complex entries); a0 = c b, b^2 = h.h, c = -1 -> 2 h.h
  P5   det(x0 I + i x.Q) = x0^2 - |x|^2; the Riley relation over Z[omega] exactly; det rho = 1
  P6   W = conj(U) V^dagger sends V'^T U to I and leaves Y Y^dagger (symbolic shape; numeric generic check)
  T13b with m1 = 0 the symmetric part of Y_4D is h m^T + m h^T - (h.m) I for every a0 (symbolic)
  P8   the template's Hessian at its centre: 10/phi^4 and 8/phi^4
"""
import itertools, math, json, pathlib
import numpy as np
import sympy as sp

OUT = {}
def rec(k, v):
    OUT[k] = v; print(k, ":", v)

# ---------------------------------------------------------------- P1a
charges = [1, -4, 2, -3, 6]
rec("P1a gcd", math.gcd(abs(-3 - 2), abs(6 - 1)))
rec("P1a orders in 2..12 coprime to all charges", [n for n in range(2, 13) if all(math.gcd(abs(q), n) == 1 for q in charges)])
rec("P1a orders in 2..12 with (-3,6)==(2,1) mod N", [n for n in range(2, 13) if (-3 - 2) % n == 0 and (6 - 1) % n == 0])
rec("P1a orders with both", [n for n in range(2, 13) if all(math.gcd(abs(q), n) == 1 for q in charges) and (-5) % n == 0])

# ---------------------------------------------------------------- P1b, A1
def mod5(M, v): return tuple(int(x) % 5 for x in (sp.Matrix(M) * sp.Matrix(v)))
U = sp.Matrix([[1, 2], [2, 3]]); U0 = sp.Matrix([[3, 2], [2, 1]])
rec("P1b U(2,0) mod 5", mod5(U, [2, 0])); rec("P1b U(2,1) mod 5", mod5(U, [2, 1]))
x = sp.symbols("x")
rec("P1b charpoly(U) mod 5", str(sp.Poly(U.charpoly(x).as_expr(), x, modulus=5)))
rec("P1b rank(U - 2I) mod 5 (1 = single Jordan block)", int(sp.Matrix([[(e) % 5 for e in row] for row in (U - 2 * sp.eye(2)).tolist()]).rank(iszerofunc=lambda e: e % 5 == 0)))
eig_U = [v for v in itertools.product(range(5), repeat=2) if v != (0, 0) and mod5(U, v) == tuple((2 * c) % 5 for c in v)]
rec("P1b nonzero v with Uv == 2v mod 5", eig_U)
eig_U_any = [(v, l) for v in itertools.product(range(5), repeat=2) for l in range(1, 5) if v != (0, 0) and mod5(U, v) == tuple((l * c) % 5 for c in v)]
rec("P1b all eigenpairs of U mod 5 (v, lambda)", eig_U_any)
rec("A1 U0(3,1) mod 5", mod5(U0, [3, 1]))
eig_U0 = [(v, l) for v in itertools.product(range(5), repeat=2) for l in range(1, 5) if v != (0, 0) and mod5(U0, v) == tuple((l * c) % 5 for c in v)]
rec("A1 all eigenpairs of U0 mod 5", eig_U0)
LR = sp.Matrix([[2, 1], [1, 1]]); A3 = LR ** 3
rec("A1 (LR)^3", A3.tolist()); rec("A1 det(A^3 - I)", int((A3 - sp.eye(2)).det()))
rec("A1 (A^3 - I) == 4 U0", (A3 - sp.eye(2)) == 4 * U0)
d = (A3 - sp.eye(2)) * sp.Matrix([sp.Rational(2, 5), 0])
dmod = [sp.Rational(c) - sp.floor(c) for c in d]
rec("A1 (A^3 - I)(2/5, 0) mod Z^2", [str(c) for c in dmod])
rec("A1 defect in (1/2)Z^2 ?", all((2 * c).is_integer for c in d))
fixed = [v for v in itertools.product(range(5), repeat=2) if v != (0, 0) and mod5(A3, v) == v]
rec("A1 nonzero 5-torsion points fixed by A^3", fixed)
G = sp.Matrix([[1, 2], [6, 13]])
rec("A1 Gamma(2) witness det, mod 2", (int(G.det()), [[int(e) % 2 for e in r] for r in G.tolist()]))
rec("A1 witness (1,1) -> mod 8", [int(e) % 8 for e in G * sp.Matrix([1, 1])])

# ---------------------------------------------------------------- T10a-c
As = sp.Matrix([[2, -1], [-1, 1]]); As3 = As ** 3
rec("T10a A_sig^3", As3.tolist()); rec("T10a det(A_sig^3 + I)", int((As3 + sp.eye(2)).det()))
w = sp.Matrix([sp.Rational(2, 5), sp.Rational(1, 5)])
rec("T10a (A_sig^3 + I) w", [str(c) for c in (As3 + sp.eye(2)) * w])
Bm = (As3 - sp.eye(2)) / 4
rec("T10a B", Bm.tolist()); rec("T10a U B", (U * Bm).tolist())
Uinv5 = [[int(e) % 5 for e in r] for r in (U.inv()).tolist()]; B5 = [[int(e) % 5 for e in r] for r in Bm.tolist()]
rec("T10a relay's 'B == U^-1 (mod 5)' holds?", Uinv5 == B5)
rec("T10a B == -U^-1 exactly?", Bm == -U.inv())
rec("T10b charpoly(A_sig^3) mod 5", str(sp.Poly(As3.charpoly(x).as_expr(), x, modulus=5)))
pm = {"+x": [], "-x": []}
for v in itertools.product(range(5), repeat=2):
    if v == (0, 0): continue
    im = mod5(As3, v)
    if im == v: pm["+x"].append(v)
    if im == tuple((-c) % 5 for c in v): pm["-x"].append(v)
rec("T10b nonzero 5-torsion v (in units of 1/5) with A_sig^3 v == +v / -v", pm)
rec("T10b the -x set is the line k(2,1)?", sorted(pm["-x"]) == sorted(tuple((k * c) % 5 for c in (2, 1)) for k in range(1, 5)))
rec("T10b lines (2/5, j/5) with A_sig^3 x == +-x", [j for j in range(5) if (2, j) in pm["+x"] + pm["-x"]])
# the same census for the unsigned (LR)^3 (the line convention of B1656 vs the signed one)
pmu = [v for v in itertools.product(range(5), repeat=2) if v != (0, 0) and mod5(A3, v) == tuple((-c) % 5 for c in v)]
rec("T10b unsigned (LR)^3: nonzero v with A^3 v == -v", pmu)
# rank-2 local system: chi(gamma) = exp(2 pi i w.gamma); A_sig^3 symmetric
ok = True
for g in itertools.product(range(-3, 4), repeat=2):
    gv = sp.Matrix(g)
    e1 = (w.T * (As3 * gv))[0]; e0 = (w.T * gv)[0]
    ok &= sp.Rational(e1 + e0).q == 1          # chi(A gamma) chi(gamma) = 1
rec("T10c chi(A_sig^3 gamma) = chi(gamma)^-1 for all gamma in [-3,3]^2", bool(ok))
J = sp.Matrix([[0, 1], [-1, 0]]); c = sp.symbols("c", nonzero=True)
rec("T10c J diag(c,1/c) J^-1 - diag(1/c,c)", (J * sp.diag(c, 1 / c) * J.inv() - sp.diag(1 / c, c)).applyfunc(sp.simplify).tolist())
# ---------------------------------------------------------------- T10d
def red(a): a = sp.nsimplify(a); return sp.Rational(a - 2 * sp.floor((a + 1) / 2))   # to (-1, 1] in units of pi
code = (sp.Rational(2, 25), sp.Rational(-4, 5), sp.Rational(4, 5))
rec("T10d code T8: 3(phi_u + phi_d)/pi mod 2", str(red(3 * (code[0] + code[1]))))
rec("T10d code inversion: 3(-4/5)/pi mod 2", str(red(3 * sp.Rational(-4, 5))))
relay = (sp.Rational(-2, 5), sp.Rational(4, 25), sp.Rational(-12, 25))
rec("T10d relay T8: 3(phi_u + phi_d)/pi = ", str(3 * (relay[0] + relay[1])) + " -> mod 2: " + str(red(3 * (relay[0] + relay[1]))) + " (relay says -4/25)")
rec("T10d relay inversion: 3(-4/5 + 2/5)/pi = ", str(3 * (sp.Rational(-4, 5) + sp.Rational(2, 5))) + " -> mod 2: " + str(red(3 * (sp.Rational(-4, 5) + sp.Rational(2, 5)))) + " (relay says -2/5)")

# ---------------------------------------------------------------- T11a
from sympy.matrices.normalforms import smith_normal_form
rec("T11a SNF(A_sig^3 - I)", smith_normal_form(As3 - sp.eye(2), domain=sp.ZZ).tolist())
rec("T11a SNF((LR)^3 - I)", smith_normal_form(A3 - sp.eye(2), domain=sp.ZZ).tolist())
try:
    import snappy
    M = snappy.Manifold("m004")
    cov = [Cv for Cv in M.covers(3, cover_type="cyclic")]
    rec("T11a SnapPy: 3-fold cyclic covers of m004, homology", [str(Cv.homology()) for Cv in cov])
    rec("T11a SnapPy: all 3-fold covers of m004, homology", sorted(str(Cv.homology()) for Cv in M.covers(3)))
except Exception as e:
    rec("T11a SnapPy", "not run: %r" % e)

# ---------------------------------------------------------------- A2
k = sp.symbols("k", integer=True)
def chi(k): return sp.exp(sp.I * sp.pi * k ** 2 / 4)
def chip(k): return (-1) ** k * chi(k)
pol = []
for a_, b_ in itertools.product(range(-4, 5), repeat=2):
    p1 = sp.simplify(chi(a_ + b_) * sp.conjugate(chi(a_) * chi(b_)) - sp.exp(sp.I * sp.pi * a_ * b_ / 2))
    p2 = sp.simplify(chip(a_ + b_) * sp.conjugate(chip(a_) * chip(b_)) - sp.exp(sp.I * sp.pi * a_ * b_ / 2))
    pol.append(p1 == 0 and p2 == 0)
rec("A2 polarization exp(i pi ab/2) for chi and chi' on [-4,4]^2", all(pol))
rec("A2 chi'(1) - chi(1), chi'(-2) - chi(-2)", [str(sp.simplify(chip(1) - chi(1))), str(sp.simplify(chip(-2) - chi(-2)))])
QI = sp.Matrix([[sp.I, 0], [0, -sp.I]]); QJ = sp.Matrix([[0, 1], [-1, 0]]); QK = QI * QJ
a0, hI, hJ, hK = sp.symbols("a0 hI hJ hK")
detS = sp.expand((a0 * sp.eye(2) + hI * QI + hJ * QJ + hK * QK).det())
rec("A2' det(a0 + h.Q) - (a0^2 + h.h)", str(sp.simplify(detS - (a0 ** 2 + hI ** 2 + hJ ** 2 + hK ** 2))))
bb = sp.symbols("b")
rec("A2' with a0 = -b, b^2 = h.h: det / h.h", str(sp.simplify(((-bb) ** 2 + bb ** 2) / bb ** 2)))

# ---------------------------------------------------------------- P5
x0, x1, x2, x3 = sp.symbols("x0:4", real=True)
X = x0 * sp.eye(2) + sp.I * (x1 * QI + x2 * QJ + x3 * QK)
rec("P5 det(x0 + i x.Q) - (x0^2 - |x|^2)", str(sp.simplify(X.det() - (x0 ** 2 - x1 ** 2 - x2 ** 2 - x3 ** 2))))
rec("P5 X Hermitian", sp.simplify(X - X.H) == sp.zeros(2, 2))
om = sp.symbols("omega")
ra = sp.Matrix([[1, 1], [0, 1]]); rb = sp.Matrix([[1, 0], [-om, 1]])
lhs = ra * rb.inv() * ra.inv() * rb * ra; rhs = rb * ra * rb.inv() * ra.inv() * rb
diff = (lhs - rhs).applyfunc(lambda e: sp.rem(sp.expand(e), om ** 2 + om + 1, om))
rec("P5 Riley: a b^-1 a^-1 b a - b a b^-1 a^-1 b mod (omega^2+omega+1)", diff.tolist())
diff_generic = (lhs - rhs).applyfunc(sp.expand)
rec("P5 Riley relation fails for generic omega (control)", diff_generic != sp.zeros(2, 2))
rec("P5 det rho(a), det rho(b)", [int(ra.det()), int(rb.det())])

# ---------------------------------------------------------------- P6 (numeric, generic)
rng = np.random.default_rng(1)
Y = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
Ue, s, Vh = np.linalg.svd(Y); Ve = Vh.conj().T
W = Ue.conj() @ Ve.conj().T; Yp = Y @ W.conj().T
Up, sp_, Vhp = np.linalg.svd(Yp)
rec("P6 |Y'Y'^dag - YY^dag|max", float(np.max(abs(Yp @ Yp.conj().T - Y @ Y.conj().T))))
rec("P6 |(W V)^T U - I|max", float(np.max(abs((W @ Ve).T @ Ue - np.eye(3)))))
rec("P6 W V is a right singular basis of Y' (|Y'(WV) - U S|max)", float(np.max(abs(Yp @ (W @ Ve) - Ue @ np.diag(s)))))

# ---------------------------------------------------------------- T13b
h = sp.Matrix(sp.symbols("h1:4")); m = sp.Matrix(sp.symbols("m1:4")); A0 = sp.symbols("A0")
def skew(v): return sp.Matrix([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
m1 = sp.symbols("mone")
Y4 = h * m.T + m * h.T - (h.dot(m)) * sp.eye(3) - m1 * skew(h) + A0 * (m1 * sp.eye(3) - skew(m))
symm = ((Y4 + Y4.T) / 2).applyfunc(sp.expand)
rec("T13b sym part at m1 = 0 minus (h m^T + m h^T - (h.m) I)", (symm.subs(m1, 0) - (h * m.T + m * h.T - h.dot(m) * sp.eye(3))).applyfunc(sp.expand) == sp.zeros(3, 3))
rec("T13b sym part at m1 != 0 still depends on a0 (control)", sp.diff(symm, A0) != sp.zeros(3, 3))

# ---------------------------------------------------------------- P8
phi = (1 + sp.sqrt(5)) / 2; xs, ys = sp.symbols("x y", positive=True)
xst, yst = 1 / sp.sqrt(5), phi ** 2
V = 5 * (xs - xst) ** 2 / ys ** 2 + (ys / yst - yst / ys) ** 2
grad = [sp.simplify(sp.diff(V, v).subs({xs: xst, ys: yst})) for v in (xs, ys)]
H = sp.hessian(V, (xs, ys)).subs({xs: xst, ys: yst}).applyfunc(sp.nsimplify).applyfunc(sp.simplify)
rec("P8 gradient at centre", [str(g) for g in grad])
rec("P8 Hessian at centre", [[str(sp.nsimplify(sp.simplify(e))) for e in r] for r in H.tolist()])
rec("P8 Hessian numeric", [[float(e) for e in r] for r in H.tolist()])

pathlib.Path(__file__).with_suffix(".json").write_text(json.dumps(OUT, indent=1, default=str))
