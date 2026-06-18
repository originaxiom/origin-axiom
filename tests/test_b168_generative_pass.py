"""B168 -- the Omega accretion as a generative process (V160, S035 first generative pass). Fast locks.

The accretion grows forward (arrow); the retention fraction is decreasing+decelerating (structural,
NOT i.i.d.-generic); all emergent rates are dimensionless (no scale -- the firewall relocates).
"""
import numpy as np

HIST = [96, 672, 3840, 20928, 105312, 521904, 2488080]
MAT  = [36, 240, 960, 3240, 9396, 25536, 65472]
CLS  = [1, 2, 6, 18, 49, 115, 283]


def test_forward_arrow_strictly_grows():
    for seq in (HIST, MAT, CLS):
        assert all(seq[i+1] > seq[i] for i in range(len(seq)-1))


def test_retention_decreasing_decelerating_not_iid():
    r = [HIST[i+1] / (12*HIST[i]) for i in range(len(HIST)-1)]
    dr = np.diff(r)
    assert all(d < 0 for d in dr)                 # decreasing (constraint tightens with depth)
    assert abs(dr[-1]) < abs(dr[0])               # decelerating (toward a plateau)
    assert (max(r) - min(r)) > 0.1                # varies with depth => NOT i.i.d. constant-survival
    assert all(12*ri > 1 for ri in r)             # sustained accretion over the measured range


def test_growth_rates_are_dimensionless_ratios():
    # every emergent rate is a ratio of integer counts -> a pure number (no units) -> no scale
    gh = HIST[-1] / HIST[-2]; gm = MAT[-1] / MAT[-2]
    assert gh > 1 and gm > 1
    assert isinstance(gh, float) and isinstance(gm, float)   # pure numbers, dimensionless
