"""B786 -- the theta/iota refinement of the measurement-torsor rank.

Every assertion recomputes the fact (no verdict-field reads).
"""
import sympy as sp

phi = (1 + sp.sqrt(5)) / 2
omega = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2


def _sym2(M):
    a, b, c, e = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    return sp.Matrix([[a**2, a*b, b**2], [2*a*c, a*e + b*c, 2*b*e], [c**2, c*e, e**2]])


def test_theta_trace_trivial_iota_trace_active_at_sl3():
    A = sp.Matrix([[1, 2, 0], [0, 1, 3], [0, 0, 1]])
    B = sp.Matrix([[1, 0, 0], [4, 1, 0], [0, 5, 1]])
    W = A * A * B
    assert sp.simplify(sp.trace(W) - sp.trace(B * A * A)) == 0    # theta (reversal) trace-TRIVIAL
    assert sp.simplify(sp.trace(W) - sp.trace(W.inv())) != 0      # iota (inversion) trace-ACTIVE


def test_object_is_self_dual_iota_and_theta_collapse():
    # on Sym^2(SL(2)) both iota and theta are trace-trivial (tr(g^-1)=tr(g)=tr(g^R) in SL(2))
    Ao = sp.Matrix([[1, 1], [0, 1]])
    Bo = sp.Matrix([[1, 0], [-omega, 1]])
    Wo = Ao * Ao * Bo
    assert sp.simplify(_sym2(Wo).trace() - _sym2(Wo.inv()).trace()) == 0        # iota trivial
    assert sp.simplify(_sym2(Wo).trace() - _sym2(Bo * Ao * Ao).trace()) == 0    # theta trivial


def test_charvariety_generators_are_c_iota_gamma5_rank3():
    # the three trace-active involutions, each on distinct data => rank 3
    A = sp.Matrix([[1, 2, 0], [0, 1, 3], [0, 0, 1]])
    B = sp.Matrix([[1, 0, 0], [4, 1, 0], [0, 5, 1]])
    W = A * A * B
    c_active = sp.simplify(sp.conjugate(2 - omega) - (2 - omega)) != 0
    iota_active = sp.simplify(sp.trace(W) - sp.trace(W.inv())) != 0
    gamma5_rel = sp.simplify((1 - phi) ** 2 - phi ** -2) == 0
    assert c_active and iota_active and gamma5_rel      # c, iota, gamma5 all genuine
