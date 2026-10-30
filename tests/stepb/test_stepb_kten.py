"""K over the ten through the cell index (data-free): the tiered, windowed computation equals every row at 32 x 32 Gauss
points; each row's rigorous upper bound bounds its integral; the window's dropped mass is below 2^-30; C_ten = C_six +
bits_CKM; the J sign is never scored (a frame with J -> -J gives the same K)."""
import pytest
pytestmark = pytest.mark.slow
import math, pathlib, sys
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'scripts' / 'stepb')); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import stepb_core as C
import compression as K
from kten import K_ten, K_ten_brute, Integrand, integrals, lse2
from test_stepb_cells import signed_frame, build


def boxed_target(ci, rng, noise):
    i = int(rng.choice(np.nonzero(ci.ok)[0])); x0, x1, y0, y1 = ci.cellr[ci.node[i]]
    t = ci.values_at(i, [(rng.uniform(x0, x1), rng.uniform(y0, y1))])[0] + C.c_shift(3.0) + rng.normal(0, noise, 10)
    t[:6] = np.clip(t[:6], [K.X0 + 0.01, K.Y0 + 0.01] * 3, [K.X1 - 0.01, K.Y1 - 0.01] * 3)
    for s in range(3):
        if t[2 * s + 1] >= t[2 * s]: t[2 * s + 1] = t[2 * s] - 0.05
    return t


def test_tiered_equals_brute_force():
    cen = signed_frame(slope=6.0, seed=1, n_lines=2); F, ci = build(cen, 0.12)
    rng = np.random.default_rng(3); n = 0
    for trial in range(6):
        t = boxed_target(ci, rng, [0.05, 0.5, 2.0][trial % 3])
        r = K_ten(ci, t, C.C_OURS)
        if r["grade"] != "JUDGED":
            continue
        b = K_ten_brute(ci, t, C.C_OURS)
        assert abs(r["L_six"] - b["L_six"]) < 0.02, (r["L_six"], b["L_six"])
        assert abs(r["bits_CKM"] - b["bits_CKM"]) < 0.05, (r["bits_CKM"], b["bits_CKM"])
        assert abs(r["C_ten"] - (r["C_six"] + r["bits_CKM"])) < 1e-12
        assert r["drop_bits_rel"] <= -30
        n += 1
    assert n >= 4


def test_upper_bound_bounds_the_integral():
    cen = signed_frame(slope=6.0, seed=2); F, ci = build(cen, 0.12)
    rng = np.random.default_rng(4)
    for trial in range(4):
        t = boxed_target(ci, rng, 0.3) - C.c_shift(3.0)
        rows = rng.choice(ci.rows, 300, replace=False)
        for six, ckm in ((True, False), (False, True), (True, True)):
            g = Integrand(ci, t, six=six, ckm=ckm)
            I = integrals(ci, rows, g, 32); U = g.upper(rows)
            assert (I <= U + 1e-9).all(), (six, ckm, float((I - U).max()))


def test_j_sign_is_not_scored():
    cen = signed_frame(slope=6.0, seed=1); F, ci = build(cen, 0.12)
    cen2 = signed_frame(slope=6.0, seed=1); cen2.J = -cen2.J; F2, ci2 = build(cen2, 0.12)
    rng = np.random.default_rng(5)
    t = boxed_target(ci, rng, 0.2)
    a, b = K_ten(ci, t, C.C_OURS), K_ten(ci2, t, C.C_OURS)
    assert abs(a["C_ten"] - b["C_ten"]) < 1e-9
