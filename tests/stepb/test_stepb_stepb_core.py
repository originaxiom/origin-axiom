"""Unit tests of the generator's core on synthetic censuses (data-free).  Run: python3 -m pytest -q test_stepb_core.py
Each pinned constant is pinned so that a mutation of it fails (the third review's mutation probe)."""
import math
import pathlib, sys

import numpy as np
from scipy.stats import chi2 as CHI2

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'scripts' / 'stepb')); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import stepb_core as C


def synthetic(n=500, seed=1):
    rng = np.random.default_rng(seed)
    m1 = 10 ** rng.uniform(-6, -2, (n, 3)); m2 = 10 ** rng.uniform(-3, -0.5, (n, 3))
    m = np.stack([np.minimum(m1, m2), np.maximum(m1, m2)], axis=2)          # (m1/m3, m2/m3), m1 <= m2
    v = np.stack([10 ** rng.uniform(-1.5, -0.2, n), 10 ** rng.uniform(-2.5, -0.7, n), 10 ** rng.uniform(-3.5, -1.5, n)], 1)
    return C.Census(cfg=np.arange(n) // 4, d=rng.integers(0, 13, n), r=rng.integers(0, 2, n), k=rng.integers(0, 8, n),
                    m=m, v=v, J=rng.choice([-1, 1], n) * 10 ** rng.uniform(-6, -3.5, n), vdef=rng.random(n) > 0.2)


def test_pinned_constants():
    assert C.ALLOW == 0.10
    assert C.C_SCAN == (1 / 3, 1 / 2, 2 / 3, 1.0, 3 / 2, 2.0, 3.0, 4.0, 5.0)
    assert C.C_OURS == (3.0,) and C.C_ARM1 == (1.0,)
    assert abs(C.SUPPORT_THRESHOLD - CHI2.ppf(0.99, 10)) < 1e-12 and abs(C.SUPPORT_THRESHOLD - 23.21) < 0.005
    assert abs(C.THRESHOLD_NINE - 21.67) < 0.005 and abs(C.CKM_LEG_THRESHOLD - 13.28) < 0.005


def test_features_order_swap_and_J():
    c = synthetic(5)
    F = C.features(c)
    assert F.shape == (5, 10)
    assert np.allclose(F[:, 0], np.log(c.m[:, 0, 1])) and np.allclose(F[:, 1], np.log(c.m[:, 0, 0]))   # up: (m2/m3, m1/m3)
    assert np.allclose(F[:, 4], np.log(c.m[:, 2, 1])) and np.allclose(F[:, 5], np.log(c.m[:, 2, 0]))   # lepton
    assert np.allclose(F[:, 6:9], np.log(c.v))
    assert np.allclose(F[:, 9], np.log(np.abs(c.J)))                                                   # |J|, sign unscored


def test_c_shift_matches_b1726_convention():
    s = C.c_shift(3.0)
    assert s.shape == (10,) and s[4] == math.log(3.0) and s[5] == -math.log(3.0) and np.count_nonzero(s) == 2


def test_chi2_by_hand():
    c = synthetic(3); F = C.features(c); sig = np.full(10, 0.2)
    t = F[0] + np.array([0.1, -0.2, 0.0, 0.3, 0.0, 0.0, 0.05, 0.0, -0.1, 0.2])
    assert abs(C.chi2(F, t, sig, 1.0, q=10)[0] - sum((d / 0.2) ** 2 for d in (0.1, 0.2, 0.3, 0.05, 0.1, 0.2))) < 1e-12
    assert abs(C.chi2(F, t, sig, 1.0, q=9)[0] - sum((d / 0.2) ** 2 for d in (0.1, 0.2, 0.3, 0.05, 0.1))) < 1e-12
    assert abs(C.chi2(F, t, sig, 1.0, q=6)[0] - sum((d / 0.2) ** 2 for d in (0.1, 0.2, 0.3))) < 1e-12
    t3 = F[1] + C.c_shift(3.0)
    assert C.chi2(F, t3, sig, 3.0)[1] < 1e-20


def test_support_c_values_and_vdef():
    c = synthetic(400); F = C.features(c); sig = np.full(10, 0.15)
    i = int(np.nonzero(~c.vdef)[0][0])
    s = C.support(c, F, F[i] + C.c_shift(2.0), sig)
    assert s["best_row"] != i                                   # an undefined mixing never supports
    j = int(np.nonzero(c.vdef)[0][0]); t = F[j] + C.c_shift(5.0)
    assert C.support(c, F, t, sig)["in_support"] and C.support(c, F, t, sig)["best_c"] == 5.0
    # at our world's fixed c = 3 the same target is scored without the scan
    s3 = C.support(c, F, t, sig, c_values=C.C_OURS)
    assert s3["best_c"] == 3.0 and s3["min_chi2"] > 0


def test_sigma_from_relative():
    s = C.sigma_from_relative([0.0] * 6, [0.0] * 4)
    assert s.shape == (10,) and np.allclose(s, 0.10)
    s = C.sigma_from_relative([0.3] + [0.0] * 5, [0.0] * 4)
    assert abs(s[0] - math.hypot(0.3, 0.1)) < 1e-15


def test_clopper_pearson_is_the_two_sided_95_upper_end():
    assert abs(C.clopper_pearson_upper(0, 100) - (1 - 0.025 ** (1 / 100))) < 1e-12
    assert C.clopper_pearson_upper(5, 5) == 1.0
    assert C.clopper_pearson_upper(3, 1000) > C.clopper_pearson_upper(3, 1000, conf=0.95)


def test_null_six_box():
    rng = np.random.default_rng(7); T = C.null_six(rng, 20000)
    r2, r1 = np.exp(T[:, 0::2]), np.exp(T[:, 1::2])
    assert (r1 < r2).all()
    assert (np.log10(r2) >= -3).all() and (np.log10(r2) <= -1).all()
    assert (np.log10(r1) >= -6).all() and (np.log10(r1) <= -2.5).all()
    assert np.log10(r1).mean() < -4.2 and abs(np.log10(r2).mean() - (-2.0)) < 0.05
