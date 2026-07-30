"""B811 — locks the promotion gate against its SEALED family and thresholds."""
import importlib.util
from pathlib import Path

from mpmath import mp, mpf, sqrt

ARC = Path(__file__).resolve().parents[1] / "frontier" / "B811_hint_promotion_gate"
PROMOTE_MAX, KILL_MIN = 3, 20          # sealed in 6fa4c2c6fa027b44


def _m():
    spec = importlib.util.spec_from_file_location("b811", ARC / "gate.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_sealed_thresholds_and_family_bounds_unchanged():
    m = _m()
    assert (m.PROMOTE_MAX, m.KILL_MIN) == (PROMOTE_MAX, KILL_MIN)
    assert list(m.NRANGE) == list(range(-8, 9))
    assert m.ABRANGE == (1, 2, 3, 4, 5) and m.CDRANGE == (-2, -1, 0, 1, 2)


def test_family_contains_all_three_hinted_forms():
    """The prereg's fairness requirement: the null must be able to produce the hints."""
    m = _m()
    fam = m.family()
    mp.dps = 30
    phi = (1 + sqrt(5)) / 2
    for hinted in (1 / (2 * phi**3), phi**-8, mpf(2) / 3):
        assert any(abs(v - hinted) < mpf("1e-11") for v, _ in fam.values()), \
            f"family cannot produce {hinted} -- the null would be unfair to its own hint"


def test_h128_dies_on_the_level_check_independently_of_counting():
    """alpha_s runs with scale; the object is scale-free. Kind mismatch, not a base rate."""
    run = _m().level_check_alpha_s()
    vals = list(run.values())
    assert max(vals) - min(vals) > mpf("0.03"), \
        "alpha_s must vary appreciably with scale for the level check to bite"


def test_h130_null_is_degenerate_for_a_rational_target():
    """Locks the diagnosis: only 2/3 itself lands in the window, so the test measured nothing."""
    m = _m()
    fam = m.family()
    mp.dps = 30
    hits = m.n_hit(fam, mpf(2) / 3, mpf("2e-5"))
    assert len(hits) == 1
    assert abs(hits[0][0] - mpf(2) / 3) < mpf("1e-20"), \
        "the single hit must BE the target -- that is why the phi-family null was inapplicable"
