"""B1956's lock: the exact arithmetic, live."""
import pathlib, sys
from fractions import Fraction as Fr
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import agy_exp_checks as C


def test_the_one_loop_relation_and_the_pati_salam_term():
    i, s, d, _ = C.eliminant()
    assert (i, s) == (Fr(23, 134), Fr(109, 201)) and d == (Fr(23, 6), Fr(-111, 10), Fr(109, 15))
    assert C.pati_salam() == Fr(506, 201)


def test_the_fourth_covers_points_and_e8():
    det, n, orders, smith, _ = C.period_four()
    assert det == 45 and n == 45 and orders == {1: 1, 3: 8, 5: 4, 15: 32} and smith == (3, 15)
    assert C.e8_partition() == (240, 46, 32, 162)
