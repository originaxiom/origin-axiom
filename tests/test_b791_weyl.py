"""B791 — locks on the Weyl completeness budget and the Gate-9/Gate-5 mismatch.

The criterion originates with Chat-1; these locks recompute it independently (Humbert volume
from the L-value, not a stored constant). Also locks the two facts that make it usable: the
1+5+6 consistency identity, and the second calibration point at the parent ground state.
"""
import mpmath as mp

VOL_M004 = "2.029883212819307250042405108549"


def _W():
    """Per-sector Weyl coefficient, from the Humbert volume of PSL(2,O_3)\\H^3."""
    mp.mp.dps = 30
    L2chi = (mp.zeta(2, mp.mpf(1) / 3) - mp.zeta(2, mp.mpf(2) / 3)) / 9
    vol_p = mp.mpf(3) ** mp.mpf(1.5) * mp.zeta(2) * L2chi / (4 * mp.pi ** 2)
    return vol_p / (6 * mp.pi ** 2)


def test_weyl_coefficient_and_the_1_5_6_consistency_identity():
    W = _W()
    assert abs(W - mp.mpf("0.0028565")) < mp.mpf("1e-7")
    # THE load-bearing step: ranks 1+5+6 = 12 must reproduce m004's own Weyl count
    assert 1 + 5 + 6 == 12
    assert abs(12 * W - mp.mpf(VOL_M004) / (6 * mp.pi ** 2)) < mp.mpf("1e-25")


def test_per_sector_budget_table():
    W = _W()
    for T, claim in ((5.0, 0.357), (8.0, 1.463), (10.0, 2.857), (12.0, 4.936),
                     (15.2, 10.032), (18.0, 16.659), (20.0, 22.852), (24.5, 42.008)):
        assert abs(W * mp.mpf(T) ** 3 - claim) < 0.002


def test_gate9_cannot_discharge_gate5():
    """Gate 9's sealed interval [0.5,12] yields ~4.94/sector; Gate 5 requires 10."""
    W = _W()
    mu = W * (mp.mpf(12) ** 3 - mp.mpf("0.5") ** 3)
    assert abs(mu - mp.mpf("4.9357")) < mp.mpf("1e-3")
    assert mu < 10                                   # the defect
    r_needed = (mp.mpf(10) / W) ** (mp.mpf(1) / 3)
    assert abs(r_needed - mp.mpf("15.184")) < mp.mpf("1e-2")
    assert abs((r_needed / 12) ** 3 - mp.mpf("2.026")) < mp.mpf("1e-2")


def test_second_calibration_point_is_the_parent_ground_state():
    """lambda_1(parent)=51.014 -> r=7.0721, and Weyl's W(T)=1 lands within 0.35%."""
    W = _W()
    r = mp.sqrt(mp.mpf("51.014") - 1)
    assert abs(r - mp.mpf("7.072058")) < mp.mpf("1e-5")
    T1 = (1 / W) ** (mp.mpf(1) / 3)                  # W(T) = 1
    assert abs(r - T1) / T1 < mp.mpf("0.005")        # 0.344%
    # it IS the ground state: the budget below it is ~1
    assert abs(W * r ** 3 - 1) < mp.mpf("0.02")
    # and it sits at the opposite spectral end from the existing DCHY control
    assert W * mp.mpf("24.5033") ** 3 > 40
    # r-dependent truncation: the mode-budget ratio the gate is designed to probe
    assert abs(mp.mpf("24.5033") / r - mp.mpf("3.465")) < mp.mpf("1e-2")
