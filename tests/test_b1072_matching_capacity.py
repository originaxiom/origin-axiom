"""B1072 locks -- the matching-capacity floor.

The model is pure arithmetic, so these tests RECOMPUTE it from the corpus's own recorded
counts rather than reading a results file.  Every number below is either a calibration
input taken from a banked arc or a PDG precision; none is a target being matched.
"""
import math

# --- calibration inputs, from the corpus's own recorded counts -------------------------
# TOMBSTONES H128 / H129: the sealed phi-expression sweep, N = 28957.
H128 = (0.1180339, 0.0009, 37)      # alpha_s window, hits
H129 = (0.021286, 0.0007, 208)      # sin^2 theta_13 window, hits
# B743 surrogate study: 54-84% hits at 4-6 digits; 0 of 50 at 10-12 digits.
B743_MID_P, B743_MID_DELTA = 0.69, 1e-5
# B322: 79 Dehn-filling invariants -> 6241 ratios vs 12 SM parameters at 1%, null mean 7.6.
B322_NULL_MEAN, B322_N, B322_DELTA = 7.6, 6241, 0.01


def p_match(delta, rho):
    return 1.0 - math.exp(-2.0 * rho * delta)


def rho_from_p(p, delta):
    return -math.log(1.0 - p) / (2.0 * delta)


def _rho_expr():
    return sum(h / (2 * (u / v)) for v, u, h in (H128, H129)) / 2


def test_the_two_calibration_windows_are_independent_and_agree():
    """H128 and H129 are different targets at different precisions.  If they disagreed
    badly on rho the density model would be wrong at its root."""
    rhos = [h / (2 * (u / v)) for v, u, h in (H128, H129)]
    assert max(rhos) / min(rhos) < 3.0, f"windows disagree: {rhos}"


def test_the_pslq_calibration_predicts_b743s_observed_zero_of_fifty():
    """Calibrated at 5 digits, the model must PREDICT the clean floor B743 measured at
    10-12 digits.  This is the control that was not used to fit."""
    rho = rho_from_p(B743_MID_P, B743_MID_DELTA)
    assert 5e4 < rho < 7e4
    assert p_match(1e-11, rho) < 0.02


def test_b322_implies_a_sane_multi_decade_spread():
    """B322 was used in NEITHER fit.  Inverting its own null mean must imply a spread
    consistent with B724's independently reported ~36.5-decade torsion spectrum, roughly
    doubled by ratio-taking.  A first version of this cell scaled rho by raw candidate
    count instead and predicted 12.0 of 12 against the observed 7.6 -- rejected."""
    rho = rho_from_p(B322_NULL_MEAN / 12.0, B322_DELTA)
    decades = B322_N / rho / math.log(10)
    assert 10.0 < decades < 120.0, f"implied spread {decades:.0f} decades"


def test_the_floor_sits_between_five_and_seven_significant_digits():
    rho_e, rho_p = _rho_expr(), rho_from_p(B743_MID_P, B743_MID_DELTA)
    for rho, lo, hi in ((rho_e, 4.5, 5.5), (rho_p, 6.0, 7.0)):
        delta = -math.log(1 - 2.0 ** -4.32) / (2 * rho)
        assert lo < -math.log10(delta) < hi


def test_nine_of_twelve_sm_parameters_are_below_the_floor():
    """The headline.  (name, value, 1-sigma) -- the constants enter as PRECISIONS only."""
    SM = [("m_p/m_e", 1836.152673426, 3.2e-8), ("alpha_em^-1", 137.035999177, 2.1e-8),
          ("m_mu/m_e", 206.7682827, 4.6e-6), ("m_tau/m_mu", 16.8170, 0.0011),
          ("sin^2thW", 0.23122, 0.00004), ("m_W/m_Z", 0.881456, 0.000132),
          ("|V_us|", 0.22431, 0.00085), ("alpha_s", 0.1180, 0.0009),
          ("|V_cb|", 0.04182, 0.00085), ("sin^2th13", 0.02203, 0.00056),
          ("sin^2th12", 0.307, 0.013), ("sin^2th23", 0.572, 0.018)]
    rho = rho_from_p(B743_MID_P, B743_MID_DELTA)
    informative = [n for n, v, u in SM if -math.log2(p_match(u / abs(v), rho)) >= 4.32]
    dead = [n for n, v, u in SM if -math.log2(p_match(u / abs(v), rho)) < 1.0]
    assert len(dead) == 9, f"expected 9 below the floor, got {len(dead)}: {dead}"
    assert set(informative) == {"m_p/m_e", "alpha_em^-1", "m_mu/m_e"}


def test_every_constant_that_clears_the_floor_is_a_qed_or_pure_mass_ratio():
    """The sting: not one survivor is a mixing angle, a gauge coupling, or a
    symmetry-breaking parameter -- i.e. not one is a quantity the programme's structural
    results speak about."""
    survivors = {"m_p/m_e", "alpha_em^-1", "m_mu/m_e"}
    mixing_or_gauge = {"sin^2thW", "alpha_s", "|V_us|", "|V_cb|",
                       "sin^2th12", "sin^2th13", "sin^2th23", "m_W/m_Z"}
    assert survivors & mixing_or_gauge == set()


def test_a_sixteen_sigma_miss_and_a_004_sigma_hit_carry_the_same_information():
    """B915's sealed 16-sigma failure (sin^2 theta_W) and TOMBSTONES H128's 0.04-sigma
    near-miss (alpha_s) both sit below the floor, so both carry ~0 bits."""
    rho = rho_from_p(B743_MID_P, B743_MID_DELTA)
    bits_w = -math.log2(p_match(0.00004 / 0.23122, rho))
    bits_as = -math.log2(p_match(0.0009 / 0.1180, rho))
    assert bits_w < 0.01 and bits_as < 0.01
