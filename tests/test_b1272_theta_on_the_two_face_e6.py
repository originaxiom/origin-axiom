"""B1272 — the object's mirror on the two-face E6: derived from P mod 5, outer, Cartan signature 3/3 (split:
E6(6) by the real-rank bound), the zero-sum triple it selects; the sl2 mirror search in the slow lane."""
import sys
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]
for arc in ("B1267_spectrum_law_rebuilt", "B1270_e6_from_the_two_faces", "B1272_theta_on_the_two_face_e6"):
    sys.path.insert(0, str(ROOT / "frontier" / arc / "verification"))


@pytest.fixture(scope="module")
def lattice():
    import theta_two_faces as X
    return X, X.Lattice()


def test_the_mirror_is_inner_on_2I_and_inverts_the_two_letters(lattice):
    X, L = lattice
    R5, L5, g5, P5, mul5 = L.f5
    # diag(3,2) has det 6 = 1 mod 5 and conjugates R -> R^-1, L -> L^-1
    assert mul5(mul5(P5, R5), (2, 0, 0, 3)) == (1, 4, 0, 1)
    assert mul5(mul5(P5, L5), (2, 0, 0, 3)) == (1, 0, 4, 1)
    import e6_from_the_two_faces as TF
    h = L.im['h']
    assert TF.orders_of(h, L.one, TF.key) == 4
    Ah = X.ad(h)
    assert TF.key(Ah(L.im['R'])) == TF.key(TF.qconj(L.im['R']))
    assert TF.key(Ah(L.im['L'])) == TF.key(TF.qconj(L.im['L']))


def test_the_three_involutions_and_the_real_rank_bound(lattice, capsys):
    X, L = lattice
    ok, res = X.part_ab(L)
    assert ok
    assert res['mirror']['kind'] == 'outer' and (res['mirror']['fix'], res['mirror']['odd']) == (3, 3)
    assert res['mirror']['allowed'] == ['E6(6)'] and res['mirror']['fixed'] == 6 and res['mirror']['orb2'] == 33
    assert res['inversion']['kind'] == 'outer' and (res['inversion']['fix'], res['inversion']['odd']) == (1, 5)
    assert res['ratio']['kind'] == 'inner' and (res['ratio']['fix'], res['ratio']['odd']) == (4, 2)
    assert 'E6(-26)' not in res['mirror']['allowed']
    return res


def test_the_mirror_selects_one_zero_sum_triple(lattice, capsys):
    X, L = lattice
    ok, res = X.part_ab(L)
    ok2, gr = X.part_c(L, res)
    out = capsys.readouterr().out
    assert gr['mirror'] == (3, 0) and gr['inversion'] == (15, 0) and gr['ratio'] == (0, 7)
    assert "sum of their E6 parts = (0, 0, 0, 0, 0, 0, 0, 0)" in out


@pytest.mark.slow
def test_the_sl2_mirror_search(lattice):
    X, L = lattice
    okd, (types, n_invol, n_inner, n_sym) = X.part_d()
    assert okd and n_inner + n_sym + n_invol == 104
