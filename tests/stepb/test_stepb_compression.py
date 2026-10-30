"""K's pieces on synthetic data (data-free): the box's area, L_raw, the tau mixture, and the no-hypercompression bound
p(C >= c) <= 2^-c for the framework's code on worlds drawn from the primary null."""
import math, pathlib, sys
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'scripts' / 'stepb')); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import stepb_core as C
import compression as K


def test_region_area_by_monte_carlo():
    rng = np.random.default_rng(2); n = 400000
    x = rng.uniform(K.X0, K.X1, n); y = rng.uniform(K.Y0, K.Y1, n)
    mc = (K.X1 - K.X0) * (K.Y1 - K.Y0) * np.mean(y < x)
    assert abs(mc - K.region_area()) / K.region_area() < 0.005


def test_L_raw_inside_and_outside():
    s = np.full(6, 0.2); t = np.log(np.array([0.01, 1e-4, 0.02, 1e-3, 0.05, 3e-4]))
    assert math.isfinite(K.L_raw(t, s)) and K.L_raw(t, s) > 0
    t_bad = t.copy(); t_bad[0] = math.log(0.5)            # r2 above the box
    assert K.L_raw(t_bad, s) == math.inf


