"""B933 DESIGN § 5a, corrected (S274; the web seat's flag in its I-31 relay, harvest row 1507, checked by main): for B933's
operator D = -i [ t (s1 d_x + s2 d_y + s3 d_t) - s3 ] the antiunitary J = s2 . conj COMMUTES with D (it anticommutes with
the bracket, and being antilinear it flips the prefactor -i), and J^2 = -1: Kramers doubling, not lambda <-> -lambda.
The control: the bracket alone anticommutes with J, as B940's Pauli identity says."""
import sympy as sp

x, y, t = sp.symbols("x y t", real=True)
FR = [sp.Function(n, real=True)(x, y, t) for n in ("fr", "fi", "gr", "gi")]
PSI = sp.Matrix([FR[0] + sp.I * FR[1], FR[2] + sp.I * FR[3]])
S1 = sp.Matrix([[0, 1], [1, 0]]); S2 = sp.Matrix([[0, -sp.I], [sp.I, 0]]); S3 = sp.Matrix([[1, 0], [0, -1]])
REAL = {sp.conjugate(sp.Derivative(F, v)): sp.Derivative(F, v) for F in FR for v in (x, y, t)}


def bracket(p):
    return t * (S1 * p.diff(x) + S2 * p.diff(y) + S3 * p.diff(t)) - S3 * p


def D(p):
    return -sp.I * bracket(p)


def J(p):
    return S2 * p.conjugate()


def zero(m):
    return sp.simplify(sp.expand(m).subs(REAL)) == sp.zeros(2, 1)


def test_j_commutes_with_b933s_operator():
    assert zero(J(D(PSI)) - D(J(PSI)))
    assert not zero(J(D(PSI)) + D(J(PSI)))
    assert zero(J(J(PSI)) + PSI)


def test_the_bracket_alone_anticommutes():
    assert zero(J(bracket(PSI)) + bracket(J(PSI)))
