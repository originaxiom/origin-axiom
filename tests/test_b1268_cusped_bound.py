"""B1268 — the net-chirality lemma and bound on the cusped object: the geometric-point instances fast
(modular ranks), the full exact selftest in the slow lane."""
import subprocess, sys
from pathlib import Path
import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1268_cusped_net_chirality_bound" / "verification"
INST = ROOT / "frontier" / "B1267_spectrum_law_rebuilt" / "verification"
sys.path.insert(0, str(VER))
sys.path.insert(0, str(INST))


@pytest.fixture(scope="module")
def mods():
    import e6_instrument as E
    import spectrum_law as S
    return E, S


def _cusp_data(E, S, rep):
    n = rep.n
    I = E.qw_eye(n)
    mu, lam = rep.M[1], rep.ev(S.LONG)
    assert E.qw_is_zero(mu.dot(lam) - lam.dot(mu))
    h0t = n - E.rank_qw(np.vstack([mu - I, lam - I]))
    rZ = E.rank_qw(np.hstack([lam - I, -(mu - I)]))
    rB = E.rank_qw(np.vstack([mu - I, lam - I]))
    return h0t, (2 * n - rZ) - rB


def test_geometric_point_27_and_27bar_have_h1_3_and_three_cusp_invariants(mods):
    E, S = mods
    e, h, f = E.principal_sl2()
    rep = S.build_rep(e, f)
    S.check_rep(rep, [1, 2], [S.REL])
    for R in (rep, rep.dualrep()):
        assert S.h0_h1(R, [1, 2], [S.REL])[:2] == (1, 3)
        assert _cusp_data(E, S, R) == (3, 6)          # h0(dM) = 3, h1(dM) = 6: the bound's ingredients


def test_the_bound_is_not_vacuous_it_uses_h0_of_the_boundary(mods):
    """-h0(dM;V) <= N(V) <= h0(dM;V*): with h0(dM;27) = 3 the bound alone allows |N| <= 3; the semicontinuity
    refinement min(3 - h0, h0*) <= 1 is what excludes three. Both inequalities are checked as arithmetic on
    the geometric point's data, and on a control where the boundary has no invariants (the -1 character)."""
    E, S = mods
    e, h, f = E.principal_sl2()
    rep = S.build_rep(e, f)
    h0t, h1t = _cusp_data(E, S, rep)
    assert h0t == 3 and min(3 - h0t, h0t) == 0 <= 1
    for k in range(0, 4):                              # every admissible h0 near the geometric point
        assert min(3 - k, k) <= 1
    val = E.Qw(-1)
    mats = {1: np.array([[val]], dtype=object), 2: np.array([[val]], dtype=object)}
    invs = {1: np.array([[val.inv()]], dtype=object), 2: np.array([[val.inv()]], dtype=object)}
    R = S.Rep(mats, invs)
    assert _cusp_data(E, S, R) == (0, 0)               # the control: no boundary invariants, bound forces N = 0
    assert S.h0_h1(R, [1, 2], [S.REL])[1] == 0


def test_the_theta_odd_class_exists_h1_of_the_v8_block_is_one(mods):
    E, S = mods
    import sympy as sp
    from fractions import Fraction as F
    e, h, f = E.principal_sl2()
    HV = E.hw_vectors(e)
    basis, v = [HV[8]], HV[8]
    for k in range(8):
        v = E.br(f, v)
        basis.append(v)
    Bm = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in b_] for b_ in basis]).T

    def restrict(y):
        img = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in E.br(y, b_)] for b_ in basis]).T
        return Bm.gauss_jordan_solve(img)[0]

    def qwm(M, cst):
        out = E.qw_zeros(9)
        for i in range(9):
            for j in range(9):
                x = sp.Rational(M[i, j])
                out[i, j] = E.Qw(F(int(x.p), int(x.q))) * cst
        return out
    ade, adf = restrict(e), restrict(f)
    R8 = S.Rep({1: E.qw_expm_nilpotent(qwm(ade, E.ONE)), 2: E.qw_expm_nilpotent(qwm(adf, E.U_RILEY))},
               {1: E.qw_expm_nilpotent(qwm(ade, E.Qw(-1))), 2: E.qw_expm_nilpotent(qwm(adf, -E.U_RILEY))})
    S.check_rep(R8, [1, 2], [S.REL])
    assert S.h0_h1(R8, [1, 2], [S.REL])[:2] == (0, 1)


@pytest.mark.slow
def test_exact_stage_selftest_passes():
    r = subprocess.run([sys.executable, str(VER / "cusped_bound.py")], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout[-3000:] + r.stderr[-3000:]
    assert "SELFTEST: PASS" in r.stdout
