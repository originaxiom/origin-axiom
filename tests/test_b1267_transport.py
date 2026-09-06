"""B1267 — the transport computed: the double-centralizer theorem and the finite-image spectra fast,
the 2T centralizer in the slow lane."""
import sys
from pathlib import Path
import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1267_transport_computed" / "verification"
INST = ROOT / "frontier" / "B1265_spectrum_law_rebuilt" / "verification"
sys.path.insert(0, str(VER))
sys.path.insert(0, str(INST))


@pytest.fixture(scope="module")
def mods():
    import e6_instrument as E
    import spectrum_law as S
    import transport as T
    import transport_quotients as Q
    return E, S, T, Q


def test_centralizer_of_the_principal_sl2_is_zero(mods):
    E, S, T, Q = mods
    e, h, f = E.principal_sl2()
    assert T.centralizer_dim_algebra([e, f]) == 0


def test_the_standard_model_algebra_is_not_a_centralizer_in_e6(mods):
    """c(c(s)) != s for B1252's s = su(3)+su(2)+u(1)_Y, while the Levi containing it IS a centralizer."""
    E, S, T, Q = mods
    import sympy as sp
    from math import lcm
    from fractions import Fraction as F
    sub, Y, rts, Mf = T.sm_subalgebra()
    Ms = sp.Matrix([[sp.Rational(Mf[i][j]) for j in range(6)] for i in range(6)])
    cY = Ms * sp.Matrix([sp.Rational(y) for y in Y])
    hY = [F(int(sp.Rational(c).p), int(sp.Rational(c).q)) for c in cY] + [F(0)] * len(E.ROOTS)
    s_elems = []
    for r in sub:
        s_elems.append(E.vec(T.root_index(r)))
        s_elems.append(E.vec(T.root_index(tuple(-x for x in r))))
    s_elems.append(hY)

    def basis_vecs(ns):
        out = []
        for v in ns:
            L = 1
            for c in v:
                L = lcm(L, int(sp.Rational(c).q))
            out.append([F(int(sp.Rational(c * L).p), int(sp.Rational(c * L).q)) for c in v])
        return out
    cs = basis_vecs(T.centralizer_basis_algebra(s_elems))
    assert len(cs) == 5
    assert T.centralizer_dim_algebra(cs) == 13          # != 12 = dim s
    # the control: the full-rank Levi is its own double centralizer
    ns = (sp.Matrix([list(r) for r in sub]) * Ms).nullspace()
    l_elems = list(s_elems[:-1])
    for n_ in ns:
        cn = Ms * sp.Matrix([sp.Rational(x) for x in n_])
        l_elems.append([F(int(sp.Rational(c).p), int(sp.Rational(c).q)) for c in cn] + [F(0)] * len(E.ROOTS))
    cl = basis_vecs(T.centralizer_basis_algebra(l_elems))
    assert len(cl) == 3 and T.centralizer_dim_algebra(cl) == 14


def test_finite_image_spectra_1_0_0_0_and_the_3(mods):
    E, S, T, Q = mods
    PA, PB = T.perm_rep_A4()
    h0p, h1p = T.h1_frac_rep({1: PA, 2: PB}, {1: PA.T.copy(), 2: PB.T.copy()}, [1, 2], [S.REL])
    assert (h0p, h1p) == (1, 2)                          # trivial + the 3: 1 + 1
    assert T.h1_character(E.ONE)[1] == 1
    assert T.h1_character(E.OMEGA)[1] == 0
    assert T.h1_character(E.Qw(-1))[1] == 0


def test_2T_quotients_72_and_48_in_this_presentation(mods):
    E, S, T, Q = mods
    G = Q.sl2f3()
    homs = [(a, b) for a in G for b in G if Q.word_value(S.REL, a, b) == Q.ID]
    surj = [(a, b) for (a, b) in homs if len(Q.generated([a, b])) == 24]
    assert (len(homs), len(surj)) == (72, 48)


@pytest.mark.slow
def test_centralizer_of_2T_through_the_principal_su2_is_u1_4(mods):
    E, S, T, Q = mods
    e, h, f = E.principal_sl2()
    gens2, elems2 = T.sl2_2T()
    assert len(elems2) == 24
    Re, Rf = E.qw_matrix(E.rho(e)), E.qw_matrix(E.rho(f))
    imgs = [T.sl2_to_e6(g, Re, Rf) for g in gens2]
    one = E.qw_eye(27)
    key = lambda M: tuple((x.x, x.y) for x in M.flatten())
    invs = []
    for g in imgs:
        P, o = g, 1
        while key(P) != key(one):
            P = P.dot(g)
            o += 1
        Qm = one
        for _ in range(o - 1):
            Qm = Qm.dot(g)
        invs.append(Qm)
    assert T.centralizer_dim_group(imgs, invs) == 4
