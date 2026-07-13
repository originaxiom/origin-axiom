"""B565/H1(ii) — the real-form gap: the hyperbolic 4_1 holonomy selects the COMPLEX
F4(C) < E6(C) (as real groups), not any proper real form of E6/F4.

Locks:
  (1) dim bookkeeping: e6 = +Sym^{2m}, m in {1,4,5,7,8,11} (78); f4 = {1,5,7,11} (52);
      coset e6/f4 = {4,8} (26).
  (2) tr Ad_{e6}(rho(a)) = 37437270 + 38799960*sqrt(3)*i  — NON-REAL, hence rho is not
      conjugate into ANY real form of E6 (real forms have real adjoint traces); same for
      f4 (36923200 + 38747580*sqrt(3)*i) killing F4(4)/F4(-20)/F4(-52) for the
      F4(C)-valued composed rep; second witness g = aB.
  (3) rho(meridian ABB) is parabolic (tr -2) => Ad is REGULAR UNIPOTENT in E6:
      Jordan blocks {3,9,11,15,17,23}, (Ad-1)^22 != 0, (Ad-1)^23 = 0 — a second,
      independent kill of the compact forms E6(-78)/F4(-52) (compact => semisimple).
Gate: exact traces tr(a) = -1-sqrt(3)i, tr(aB) = 2-2sqrt(3)i, tr(ABB) = -2 are verified
against SnapPy's geometric rep of the census presentation <a,b | abbbaBAAB> when snappy
is importable (canonical pyenv env); the exact Lie-theory locks run regardless.
"""
import sympy as sp
import pytest

E6_EXP = [1, 4, 5, 7, 8, 11]
F4_EXP = [1, 5, 7, 11]
COSET = [4, 8]


def sym_char(t, d):
    """tr Sym^d(g) as exact polynomial in t = tr(g): s_d = t*s_{d-1} - s_{d-2}."""
    s0, s1 = sp.Integer(1), t
    if d == 0:
        return s0
    for _ in range(d - 1):
        s0, s1 = s1, sp.expand(t * s1 - s0)
    return sp.expand(s1)


T_A = -1 - sp.sqrt(3) * sp.I     # tr rho(a)
T_AB_ = 2 - 2 * sp.sqrt(3) * sp.I  # tr rho(aB)


def test_dims():
    assert sum(2 * m + 1 for m in E6_EXP) == 78
    assert sum(2 * m + 1 for m in F4_EXP) == 52
    assert sum(2 * m + 1 for m in COSET) == 26


def test_snappy_gate():
    snappy = pytest.importorskip("snappy")
    G = snappy.Manifold("4_1").fundamental_group()
    assert G.relators() == ["abbbaBAAB"] and G.meridian() == "ABB"

    def tr(w):
        S = G.SL2C(w)
        return complex(S[0, 0]) + complex(S[1, 1])

    assert abs(tr("a") - complex(sp.N(T_A))) < 1e-9
    assert abs(tr("aB") - complex(sp.N(T_AB_))) < 1e-9
    assert abs(tr("ABB") - (-2)) < 1e-9


def test_nonreal_adjoint_traces():
    trE6 = sp.expand(sum(sym_char(T_A, 2 * m) for m in E6_EXP))
    trF4 = sp.expand(sum(sym_char(T_A, 2 * m) for m in F4_EXP))
    trCo = sp.expand(sum(sym_char(T_A, 2 * m) for m in COSET))
    assert trE6 == 37437270 + 38799960 * sp.sqrt(3) * sp.I
    assert trF4 == 36923200 + 38747580 * sp.sqrt(3) * sp.I
    assert trCo == 514070 + 52380 * sp.sqrt(3) * sp.I
    assert sp.im(trE6) != 0 and sp.im(trF4) != 0 and sp.im(trCo) != 0
    # second witness
    trE6b = sp.expand(sum(sym_char(T_AB_, 2 * m) for m in E6_EXP))
    assert trE6b == 17369035899774 + 17857657649280 * sp.sqrt(3) * sp.I
    assert sp.im(trE6b) != 0


def test_meridian_regular_unipotent():
    # Sym^{2m} of a 2x2 unipotent Jordan block is one Jordan block of size 2m+1;
    # rho(ABB) = -U with U unipotent, and Sym^{even}(-U) = Sym^{even}(U).
    x, y = sp.symbols("x y")
    J = sp.Matrix([[1, 1], [0, 1]])

    def sym_mat(A, d):
        xi = A[0, 0] * x + A[1, 0] * y
        yi = A[0, 1] * x + A[1, 1] * y
        S = sp.zeros(d + 1, d + 1)
        for j in range(d + 1):
            img = sp.expand((x ** (d - j) * y ** j).subs({x: xi, y: yi}, simultaneous=True))
            p = sp.Poly(img, x, y)
            for i in range(d + 1):
                S[i, j] = p.coeff_monomial(x ** (d - i) * y ** i)
        return S

    assert sym_mat(J, 1) == J  # convention gate
    sizes = []
    for m in E6_EXP:
        N = sym_mat(J, 2 * m) - sp.eye(2 * m + 1)
        k, P = 0, sp.eye(2 * m + 1)
        while not P.is_zero_matrix:
            P, k = P * N, k + 1
        sizes.append(k)
    assert sizes == [3, 9, 11, 15, 17, 23]  # regular unipotent in E6
    assert max(sizes) == 23                 # (Ad-1)^22 != 0, (Ad-1)^23 = 0
