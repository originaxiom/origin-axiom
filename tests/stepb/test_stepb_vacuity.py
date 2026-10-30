"""The fourth review's vacuity gaps, re-homed on the live generator (cells.py, kten.py, the drivers): each check can fail.
- K's posterior uses the six and c (the CKM bits move when the six move, the four fixed);
- the choices drop undefined mixings;
- check_markov uses the Clopper-Pearson LOWER end (a point estimate would fail where the lower end passes);
- the box's edges: L_raw finite inside, infinite outside;
- S can be false (a far world is not in the support, singly and in a batch);
- a p outside [0, 1] or NaN is refused;
- the null's smear is sigma (the drawn four minus the interpolated four, per quantity)."""
import pytest
pytestmark = pytest.mark.slow
import math, pathlib, sys
import numpy as np
import pytest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'scripts' / 'stepb')); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import stepb_core as C
import compression as K
import outcome as O
import kten
from assemble import Choices
from test_stepb_cells import signed_frame, build
from test_stepb_kten import boxed_target


def test_posterior_uses_the_six_and_c():
    cen = signed_frame(slope=6.0, seed=1); F, ci = build(cen, 0.12)
    rng = np.random.default_rng(11)
    t = boxed_target(ci, rng, 0.1)
    a = kten.K_ten(ci, t, C.C_OURS)
    t2 = t.copy(); t2[:6] = boxed_target(ci, np.random.default_rng(12), 0.1)[:6]          # other six, same four
    b = kten.K_ten(ci, t2, C.C_OURS)
    assert a["grade"] == b["grade"] == "JUDGED"
    assert abs(a["bits_CKM"] - b["bits_CKM"]) > 1e-3
    c = kten.K_ten(ci, t, (1.0,))
    assert abs(c["L_six"] - a["L_six"]) > 1e-3


def test_choices_drop_undefined_mixings():
    cen = signed_frame(); cen.vdef = cen.vdef.copy(); cen.vdef[::7] = False
    F = C.features(cen); ch = Choices(cen, F, sorted({tuple(t) for t in cen.tau}))
    inR = np.zeros(len(F), bool); inR[ch.R[ch.R >= 0]] = True
    assert not inR[~cen.vdef].any() and inR[cen.vdef].all()


def test_check_markov_uses_the_lower_end():
    assert 3 / 1000 > 2 ** -9                     # a point estimate would call this a violation
    assert K.check_markov(3, 1000, 9)              # the CP lower end does not
    assert not K.check_markov(60, 1000, 9)         # a real violation is caught


def test_box_edges():
    s6 = np.full(6, 0.1)
    inside = np.array([K.X1 - 1e-9, K.Y1 - 1e-9] * 3); outside = np.array([K.X1 + 1e-6, K.Y1 - 1e-9] * 3)
    assert math.isfinite(K.L_raw(inside, s6)) and not math.isfinite(K.L_raw(outside, s6))
    assert not math.isfinite(K.L_raw(np.array([K.X0 + 0.1, K.X0 + 0.1] * 3), s6))      # y = x is outside (y < x)


def test_S_can_be_false():
    cen = signed_frame(slope=6.0); F, ci = build(cen)
    far = np.nanmax(np.where(np.isfinite(F), F, np.nan), axis=0) + 50.0
    assert not ci.support(far, C.C_SCAN)["in_support"]
    assert not ci.support_batch(np.stack([far, far - 0.5]), C.C_SCAN)["in_support"].any()


def test_p_bounds_refused():
    for bad in (-0.1, 1.1, float("nan"), None):
        with pytest.raises(ValueError):
            O.legs(True, bad, "JUDGED", 1.0, 0.5, 0.5, True, 53)


def test_null_smear_is_sigma():
    from p2_driver import null_worlds
    cen = signed_frame(slope=4.0); F, ci = build(cen, 0.10)
    sig = np.array([0.10, 0.2, 0.13, 0.12, 0.1, 0.1, 0.1, 0.11, 0.12, 0.15])
    rng = np.random.default_rng(13); W, dropped = null_worlds(ci, sig, rng, 20000); assert dropped == 0
    rng2 = np.random.default_rng(13); C.null_six(rng2, 20000); rows, xs, ys = ci.sample_prior(rng2, 20000)
    resid = W[:, 6:10] - ci.interp_many(rows, xs, ys)[:, 6:10]
    assert np.allclose(resid.std(axis=0), sig[6:10], rtol=0.03) and np.allclose(resid.mean(axis=0), 0, atol=0.01)
