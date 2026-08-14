"""B785 -- the cc3 gate harvest: locks on the independently-reproduced deliverables.

Each assertion recomputes the claim (no reading of a verdict field); a defect in any
harvested claim makes the corresponding test fail.
"""
import sympy as sp

phi = (1 + sp.sqrt(5)) / 2
psi = sp.Rational(1, 2) - sp.sqrt(5) / 2   # -1/phi


def test_h1_b768_transition_matrix():
    T = sp.Matrix([[1 / phi**2, 1 / phi], [1, 0]])
    assert all(sp.simplify(sum(T.row(i))) == 1 for i in range(2))          # stochastic
    evs = sorted(T.eigenvals().keys(), key=lambda e: -sp.re(sp.N(e)))
    assert sp.simplify(evs[0] - 1) == 0                                     # leading = 1
    assert sp.simplify(evs[1] + 1 / phi) == 0                              # subdominant = -1/phi
    assert sp.simplify((1 - phi)**2 - phi**-2) == 0                        # time=basepoint


def test_h2_b489_binet_torsion():
    for n in range(1, 17):
        L2n = sp.simplify(phi**(2 * n) + psi**(2 * n))
        tors = sp.simplify(sp.Abs(L2n - 2))
        assert sp.simplify(tors - (phi**n - phi**(-n))**2) == 0            # identity, all n
        if n >= 2:
            assert sp.N(tors) >= 5                                          # blocks Gang-Yonekura


def test_h3_l255_symd_spectrum():
    lam, mu = phi, -1 / phi
    for d in range(1, 13):
        got = sorted((sp.simplify(lam**(d - j) * mu**j) for j in range(d + 1)), key=lambda z: sp.N(z))
        pred = sorted((sp.simplify((-1)**j * phi**(d - 2 * j)) for j in range(d + 1)), key=lambda z: sp.N(z))
        assert all(sp.simplify(a - b) == 0 for a, b in zip(got, pred))


def test_excluded_c21_conflation_theta_odd_tangent_is_zero():
    # the guard: the b769/C21 claim that was EXCLUDED. theta(contragredient)-odd part of
    # the geometric-point tangent is 0 -> the Im part is c-odd, NOT theta-odd.
    u = sp.symbols("u")
    omega = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2
    A = sp.Matrix([[1, 1], [0, 1]]); B = sp.Matrix([[1, 0], [-u, 1]])

    def sym2(M):
        a, b, c, e = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
        return sp.Matrix([[a**2, a*b, b**2], [2*a*c, a*e + b*c, 2*b*e], [c**2, c*e, e**2]])
    probe = sp.simplify(sp.diff(sp.expand((A * B).trace()**2 - 1), u).subs(u, omega))
    probe_inv = sp.simplify(sp.diff(sp.expand(sym2((A * B).inv()).trace()), u).subs(u, omega))
    assert sp.simplify(sp.im(probe) - sp.sqrt(3)) == 0        # Im = sqrt(3), c-odd
    assert sp.simplify((probe - probe_inv) / 2) == 0         # theta-odd part = 0 (not aligned)
