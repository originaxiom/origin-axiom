"""B1934's lock: both Weil classes split 3 + 2 with determinant 1, a real golden triplet and the spinor doublet; the hand
is the Legendre symbol at the mark; the lepton copy happens exactly at N dividing 5. Each claim has a planted fault that
must fail. It writes nothing."""
import sys, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import level_five_structure as L


def test_both_weil_classes_split_three_plus_two_inside_so3_x_su2():
    for k, exps in ((1, [0, 1, 4]), (2, [0, 2, 3])):
        r = L.check_weil(k)
        assert r["order"] == 120 and r["blocks_invariant"] and r["dets"] == {1.0} and r["real_triplet"]
        assert np.allclose(r["traces_order5"], [(1 - 5 ** .5) / 2, (1 + 5 ** .5) / 2]) and r["minus_I_on_odd"] == -1
        assert r["T_exponents_on_triplet"] == exps


def test_a_linear_phase_in_place_of_the_quadratic_one_is_no_weil_representation():
    T = np.diag([L.W ** x for x in range(L.P)])                             # planted: e(x), not e(x^2)
    S = np.array([[L.W ** (x * y) for y in range(L.P)] for x in range(L.P)]) / np.sqrt(L.P)
    assert len(L.generate([S, T])) != 120


def test_the_hand_is_the_legendre_symbol_and_a_wrong_mark_fails():
    assert L.hand_is_legendre((1, 2))
    assert not L.hand_is_legendre((1, 1))                                   # planted: not on the act's frustrated line


def test_the_lepton_copy_happens_exactly_where_n_divides_five():
    assert L.transposed_orders() == [5]
    planted = dict(L.Y6, L=-2)                                              # planted: a wrong lepton charge
    assert L.transposed_orders(y=planted) != [5]
