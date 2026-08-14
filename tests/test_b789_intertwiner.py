"""B789 — locks on the explicit theta-intertwiner (cc3 harvest, verified).

Locks the result AND the three scoping facts, because the scoping is what keeps the claim
honest: the group-level identity is FALSE and Q is rep-dependent. Every assertion recomputes.
"""
import sympy as sp

Z2, Z3 = sp.zeros(2, 2), sp.zeros(3, 3)
omega = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2
u = sp.Symbol("u")

Q = sp.Matrix([[0, 0, 1], [0, sp.Rational(1, 2), 0], [1, 0, 0]])
W = [1, -2, -1, 2]                       # w = a b^-1 a^-1 b
REL_L, REL_R = W + [1], [2] + W          # w a = b w


def sym2(M):
    a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    return sp.Matrix([[a**2, 2*a*b, b**2],
                      [a*c, a*d + b*c, b*d],
                      [c**2, 2*c*d, d**2]])


def ev(word, g):
    M = sp.eye(g[1].shape[0])
    for l in word:
        M = M * g[l]
    return sp.simplify(M)


def _reps():
    A = sp.Matrix([[1, 1], [0, 1]])
    B = sp.Matrix([[1, 0], [-omega, 1]])
    sA, sB = sym2(A), sym2(B)
    return {1: sA, -1: sA.inv(), 2: sB, -2: sB.inv()}


def test_relator_is_derived_and_forces_the_eisenstein_root():
    """w a = b w with w = a b^-1 a^-1 b holds iff u^2+u+1 = 0 (so u = omega)."""
    A = sp.Matrix([[1, 1], [0, 1]])
    Bu = sp.Matrix([[1, 0], [-u, 1]])
    Gu = {1: A, -1: A.inv(), 2: Bu, -2: Bu.inv()}
    R = sp.simplify(ev(REL_L, Gu) - ev(REL_R, Gu))
    cyc = sp.Poly(u**2 + u + 1, u)
    for i in range(2):
        for j in range(2):
            e = sp.simplify(R[i, j])
            if e != 0:
                num = sp.Poly(sp.numer(sp.together(e)), u)
                assert sp.simplify(sp.rem(num, cyc).as_expr()) == 0
    # and it holds exactly at u = omega, on SL(2) and on Sym^2
    G = {1: A, -1: A.inv(), 2: Bu.subs(u, omega), -2: Bu.subs(u, omega).inv()}
    assert sp.simplify(ev(REL_L, G) - ev(REL_R, G)).equals(Z2)
    assert sp.simplify(ev(REL_L, _reps()) - ev(REL_R, _reps())).equals(Z3)


def test_rho2_descends_to_the_knot_group():
    """THE STRENGTHENING: rho_2 = transpose o reversal respects the relator."""
    S = _reps()

    def rho2(word):
        return ev(list(reversed(word)), S).T

    assert sp.simplify(rho2(REL_L) - rho2(REL_R)).equals(Z3)


def test_Q_intertwines_rho2_to_rho1_on_words():
    S = _reps()

    def rho2(word):
        return ev(list(reversed(word)), S).T

    # derivation: Q = S_iota * S_sd^-1
    S_iota = sp.diag(1, -1, 1)
    S_sd = sp.Matrix([[0, 0, 1], [0, -2, 0], [1, 0, 0]])
    assert sp.simplify(S_iota * S_sd.inv() - Q).equals(Z3)
    for word in ([1], [2], [1, 2], [2, 1], [1, 2, -1], [2, -1, -2, 1], [1, 1, 2, -2, -1]):
        assert sp.simplify(Q * rho2(word) * Q.inv() - ev(word, S)).equals(Z3)


def test_scope_group_level_identity_is_false_and_Q_reverses():
    """The abelian obstruction: Q M^T Q^-1 = M for ALL M would force the image abelian."""
    S = _reps()
    ab = sp.simplify(S[1] * S[2])
    ba = sp.simplify(S[2] * S[1])
    assert not sp.simplify(Q * ab.T * Q.inv() - ab).equals(Z3)   # (A) FALSE
    assert sp.simplify(Q * ab.T * Q.inv() - ba).equals(Z3)       # Q reverses
    assert not sp.simplify(ab - ba).equals(Z3)                   # image is non-abelian


def test_scope_Q_is_rep_dependent_not_universal():
    A2, B2 = sp.Matrix([[2, 1], [1, 1]]), sp.Matrix([[1, 0], [3, 1]])
    assert not sp.simplify(Q * sym2(A2).T * Q.inv() - sym2(A2)).equals(Z3)


def test_scope_disc_form_basis_reconciliation():
    D = sp.diag(1, 2, 1)
    S_sd = sp.Matrix([[0, 0, 1], [0, -2, 0], [1, 0, 0]])
    disc = sp.Matrix([[0, 0, 2], [0, -1, 0], [2, 0, 0]])
    assert sp.simplify(2 * (D.inv().T * S_sd * D.inv()) - disc).equals(Z3)
