"""B160 -- the metallic-quasicrystal bridge (V154). Fast symbolic locks.

Re-confirms (independently of the handoff scripts) the headline kappa=tr[A,B]=2+lambda^2,
the trace-map Fricke-invariance for golden/silver/bronze, and the kappa=-2 figure-eight
parabolic point. FIREWALL: emergent/condensed-matter math, not fundamental physics; the
bridge itself is already banked (B107/B148/K007/K010) -- this locks the verified increments.
"""
import sympy as sp

E, lam = sp.symbols('E lambda')
a, b, c = sp.symbols('a b c')
I2 = sp.eye(2)
Kfr = lambda X, Y, Z: X**2 + Y**2 + Z**2 - X*Y*Z - 2


def test_transfer_matrix_kappa():
    A = sp.Matrix([[E-lam, -1], [1, 0]]); B = sp.Matrix([[E, -1], [1, 0]])
    assert sp.simplify(A.det()) == 1 and sp.simplify(B.det()) == 1
    x, y, z = sp.trace(A), sp.trace(B), sp.expand(sp.trace(A*B))
    assert sp.simplify(z - (x*y - 2)) == 0                       # z = xy - 2
    kap = sp.simplify(sp.trace(A*B*A.inv()*B.inv()))
    assert sp.simplify(kap - (2 + lam**2)) == 0                  # tr[A,B] = 2 + lambda^2
    assert E not in kap.free_symbols                             # independent of E


def test_generic_fricke_commutator_identity():
    # tr[A,B] = x^2+y^2+z^2-xyz-2 on a parametrized SL(2) pair
    p, q, r, s, t, u = sp.symbols('p q r s t u')
    A = sp.Matrix([[p, q], [r, (1 + q*r)/p]])
    B = sp.Matrix([[s, t], [u, (1 + t*u)/s]])
    x, y, z = sp.trace(A), sp.trace(B), sp.trace(A*B)
    lhs = sp.simplify(sp.trace(A*B*A.inv()*B.inv()))
    assert sp.simplify(lhs - (x**2 + y**2 + z**2 - x*y*z - 2)) == 0


def test_fibonacci_and_silver_tracemaps_conserve_fricke():
    # Fibonacci (half-trace) map (a,b,c)->(b,c,2bc-a) conserves Fricke-Vogt I=a^2+b^2+c^2-2abc-1
    Ivog = lambda X, Y, Z: X**2 + Y**2 + Z**2 - 2*X*Y*Z - 1
    assert sp.simplify(Ivog(b, c, 2*b*c - a) - Ivog(a, b, c)) == 0
    # silver map (a,b,c)->(b, bc-a, (b^2-1)c-ab) conserves Fricke kappa
    assert sp.simplify(Kfr(b, b*c - a, (b**2 - 1)*c - a*b) - Kfr(a, b, c)) == 0


def test_bronze_tracemap_conserves_fricke():
    # bronze m=3 map by Cayley-Hamilton M_k^3=(b^2-1)M_k - bI
    ap, bp, cp = b, (b**2 - 1)*c - a*b, (b**2 - 1)*(b*c - a) - b*c
    assert sp.simplify(Kfr(ap, bp, cp) - Kfr(a, b, c)) == 0


def test_kappa_minus_two_is_figure_eight_parabolic():
    # kappa = 2+lambda^2 = -2  <=>  lambda = 2i ; commutator parabolic (single Jordan block, not -I)
    assert sp.simplify(2 + (2*sp.I)**2 - (-2)) == 0
    A = sp.Matrix([[E-lam, -1], [1, 0]]); B = sp.Matrix([[E, -1], [1, 0]])
    C = (A*B*A.inv()*B.inv()).subs(lam, 2*sp.I).subs(E, sp.Rational(1, 2))
    C = sp.simplify(C)
    assert sp.simplify(sp.trace(C) + 2) == 0          # trace -2
    assert sp.simplify(C - (-I2)) != sp.zeros(2)       # not central -I
    assert sp.simplify((C + I2)**2) == sp.zeros(2)     # (C+I)^2 = 0 => parabolic
