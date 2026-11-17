"""B1946's lock: with the same reading S in both sectors the cusp mixing is aligned; the mixed pairings derange it."""
import sys, pathlib
from fractions import Fraction as Fr
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import same_reading as SR


def test_same_reading_aligns_and_mixed_readings_derange():
    pts = [(Fr(1, 5), Fr(2, 5)), (Fr(2, 5), Fr(4, 5)), (Fr(0), Fr(3, 5))]
    r = SR.pair_stats(30.0, pts)
    assert min(d for d, o in r[("S", "S")]) > 1 - 1e-6 and max(o for d, o in r[("S", "S")]) < 1e-3
    for k in (("St", "S"), ("S", "St")):
        assert max(d for d, o in r[k]) < 1e-6, k          # every diagonal entry vanishes: a derangement


def test_the_two_readings_coincide_at_tau_i_and_not_at_a_control():
    import readings_coincide_at_i as RC
    assert RC.diff("0", 1.0, Fr(1, 5), Fr(3, 5), "up") < 1e-20 and RC.diff("0", 1.0, Fr(2, 5), Fr(1, 5), "down") < 1e-20
    assert RC.diff("0", 1.3, Fr(1, 5), Fr(3, 5), "up") > 0.1

