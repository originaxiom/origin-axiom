"""Tests written to kill the third review's surviving mutants (its probe_d): each pins a value a mutation would change."""
import math, pathlib, sys
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'scripts' / 'stepb')); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import stepb_core as C
import compression as K
import clocks as T


def test_address_bits_pinned():
    assert abs(K.A_DISCRETE - (math.log2(266) + math.log2(12) + 1 + 3 + math.log2(9))) < 1e-12
    assert abs(K.A_DISCRETE - 18.810) < 0.001
    assert abs(K.MISFIT_CONST6 - 6 * 0.5 * math.log2(2 * math.pi)) < 1e-12


def test_L_raw_by_hand():
    s = np.array([0.1, 0.2, 0.15, 0.12, 0.11, 0.13])
    t = np.log(np.array([0.01, 1e-4, 0.02, 1e-3, 0.05, 3e-4]))
    A = K.region_area()
    hand = sum(math.log2(A / (s[2 * k] * s[2 * k + 1])) for k in range(3))
    assert abs(K.L_raw(t, s) - hand) < 1e-12
    assert abs(A - ((2 * math.log(10)) * (3.5 * math.log(10)) - (0.5 * math.log(10)) ** 2 / 2)) < 1e-9     # the box minus the r1 >= r2 corner


def test_T1_threshold_is_one_percent():
    y = 1.0 / (1.0 - 0.75 * 0.997)               # area_cdf(y) = 0.997: two-sided t = 0.006
    r = T.T1(T.area_cdf, y)
    assert abs(r["t"] - 0.006) < 1e-9 and r["grade"] == "NEGATIVE"
    y2 = 1.0 / (1.0 - 0.75 * 0.994)              # t = 0.012
    assert T.T1(T.area_cdf, y2)["grade"] == "CONSISTENT"


