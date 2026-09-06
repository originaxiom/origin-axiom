"""B1278 — the tower's Wilson lines: H_1(Y_n) by Smith form (Fox's product check), every character's h^1 (numeric
sweep + exact cyclotomic confirmation), the three family characters, the three-generation alphabet K3 (trivial on
Y_3 and Y_6, 145 elements on Y_9), the SM-commuting Wilson-line enumerations (none breaks SU(5) with three
generations on Y_3 or Y_6, the best keep two; on Y_9 they do, with exactly the SM's roots kept).  Y_3 fast; Y_6 and
Y_9 slow-marked."""
import sys
from pathlib import Path
from fractions import Fraction as F
import pytest

ROOT = Path(__file__).resolve().parents[1]
for arc in ("B1267_spectrum_law_rebuilt", "B1268_cusped_net_chirality_bound", "B1269_transport_computed",
            "B1273_the_three_fold_closing", "B1274_the_tower_and_its_doubles", "B1275_the_cubic_made_explicit",
            "B1276_the_relations_the_chain_forces", "B1277_the_vacuum_manifold_of_the_closing",
            "B1278_the_six_fold_closing"):
    sys.path.insert(0, str(ROOT / "frontier" / arc / "verification"))


@pytest.fixture(scope="module")
def X():
    import six_fold_closing as X
    wts, rep = X.C.load()
    lab, hy, wts2 = X.R.sm_labels()
    assert wts2 == wts
    sub, Y, rts, Mf, ip, a1, a2 = X.VM.descent_data()
    sm_roots = sorted(set(a2) | {a1, tuple(-x for x in a1)})
    iN = next(i for i in range(27) if lab[i] == 'S'); inc = next(i for i in range(27) if lab[i] == 'nu^c')
    wN, wnc = [F(x) for x in wts[iN]], [F(x) for x in wts[inc]]
    return X, wts, lab, sm_roots, (rts, ip, wN, wnc)


def test_the_orders_of_the_tower_are_fox_products(X):
    M = X[0]
    assert [M.alexander_order(n) for n in (2, 3, 6, 9, 12)] == [5, 16, 320, 5776, 103680]


def test_y3_reproduces_b1277_and_the_best_wilson_line_keeps_two_generations(X, capsys):
    M, wts, lab, sm_roots, extra = X
    out = M.closing(3, wts, lab, sm_roots, extra=extra)
    text = capsys.readouterr().out
    assert out['tors'] == [4, 4] and out['m'] == 4 and out['dist'] == {0: 13, 1: 3}
    assert out['only_family'] and out['K3'] == [(0, 0, 0, 0)] and len(out['K2']) == 3
    assert out['results']['total'] == 4096 and out['results']['full3'] == 0 and out['results']['best'] == 2
    assert out['results']['su5_kept_full'] == 1
    assert "exact over Q(zeta_4): the 3 characters with h^1 > 0 and 3 zero controls confirmed" in text


@pytest.mark.slow
def test_y6_joins_both_ends_and_still_has_no_three_generation_standard_model(X, capsys):
    M, wts, lab, sm_roots, extra = X
    out = M.closing(6, wts, lab, sm_roots, extra=extra)
    text = capsys.readouterr().out
    assert out['tors'] == [8, 40] and out['order'] == 320 and out['dist'] == {0: 293, 1: 27}
    assert not out['only_family'] and len(out['pos']) == 27 and out['K3'] == [(0,) * 7] and len(out['K2']) == 27
    assert out['results']['full3'] == 0 and out['results']['best'] == 2 and out['results']['total'] == 320 ** 3
    assert "the extra classes: 24 characters of orders {8: 24}" in text


@pytest.mark.slow
def test_y9_carries_the_standard_model_with_three_generations(X, capsys):
    M, wts, lab, sm_roots, extra = X
    out = M.closing(9, wts, lab, sm_roots, extra=extra)
    text = capsys.readouterr().out
    assert out['tors'] == [76, 76] and out['order'] == 5776 and out['dist'] == {0: 5629, 1: 147}
    assert len(out['pos']) == 147 and len(out['K3']) == 145
    assert "the extra classes: 144 characters of orders {38: 108, 19: 36}" in text
    assert "closed under multiplication by the family characters: True (432 of 432 products land in it)" in text
    ks = out['k3_search']
    assert ks['total'] == 145 ** 3 and ks['full3'] == 737568 and ks['bad_kept'] == 0
    assert ks['sm_vacua'] > 0 and ks['full_spectrum'] > 0
    assert "coefficient matrix det = 1, invertible modulo every d_j: True" in text
