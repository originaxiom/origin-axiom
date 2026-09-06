"""B1265 — the spectrum law rebuilt from rep27.json: the instrument's checks and the cusped rows fast,
one twisted-double row in the slow lane."""
import sys
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1265_spectrum_law_rebuilt" / "verification"
sys.path.insert(0, str(VER))


@pytest.fixture(scope="module")
def E():
    import e6_instrument as E
    return E


@pytest.fixture(scope="module")
def S():
    import spectrum_law as S
    return S


def test_rep27_is_a_representation_of_the_rebuilt_bracket(E):
    assert len(E.POS) == 36 and E.DIM == 78
    assert E.check_representation(trials=150, seed=5) == 0


def test_principal_blocks_17_9_1_and_the_six_dial_slots(E):
    from collections import Counter
    e, h, f = E.principal_sl2()
    Rh = E.rho(h)
    eig = Counter(int(Rh[i, i]) for i in range(27))
    assert eig[16] == 1 and eig[8] == 2 and eig[0] == 3 and eig[-16] == 1
    HV = E.hw_vectors(e)
    assert sorted(HV) == [2, 8, 10, 14, 16, 22]


def test_theta_parity_dichotomy_by_bracket_closure(E):
    e, h, f = E.principal_sl2()
    HV = E.hw_vectors(e)
    assert E.closure_dim([e, h, f, HV[8]]) == 78
    assert E.closure_dim([e, h, f, HV[14]]) == 52     # the control: the criterion can fail


def test_subregular_orbit_70_and_blocks_13_9_5(E):
    from collections import Counter
    es, hs, fs, g2 = E.subregular_sl2()
    assert E.centralizer_dim(es) == 8
    eig = Counter(int(E.rho(hs)[i, i]) for i in range(27))
    assert eig[12] == 1 and eig[8] == 2 and eig[4] == 3 and eig[0] == 3


def test_cusped_rows_h1_is_3_for_27_and_27bar_both_embeddings(E, S):
    e, h, f = E.principal_sl2()
    rep = S.build_rep(e, f)
    S.check_rep(rep, [1, 2], [S.REL])
    assert S.h0_h1(rep, [1, 2], [S.REL])[:2] == (1, 3)
    assert S.h0_h1(rep.dualrep(), [1, 2], [S.REL])[:2] == (1, 3)
    es, hs, fs, _ = E.subregular_sl2()
    reps = S.build_rep(es, fs)
    S.check_rep(reps, [1, 2], [S.REL])
    assert S.h0_h1(reps, [1, 2], [S.REL])[:2] == (0, 3)
    assert S.h0_h1(reps.dualrep(), [1, 2], [S.REL])[:2] == (0, 3)


@pytest.mark.slow
def test_twisted_double_theta_odd_dial_gives_2_for_27_and_27bar(E, S):
    e, h, f = E.principal_sl2()
    HV = E.hw_vectors(e)
    gens = [1, 2, 3]
    rels = [S.relator(1, 2), S.relator(1, 3),
            S.longitude(1, 2) + [-x for x in reversed(S.longitude(1, 3))]]
    R = S.build_rep(e, f, HV[8], E.Qw(1))
    S.check_rep(R, gens, rels)
    assert S.h0_h1(R, gens, rels)[:2] == (0, 2)
    assert S.h0_h1(R.dualrep(), gens, rels)[:2] == (0, 2)
