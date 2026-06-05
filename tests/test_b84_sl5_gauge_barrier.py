"""B84 (Phase B, V67) -- locking test: the SL(5) barrier is spectrum-level non-convergence (I1 refuted).
SL(4) power sums are seed-invariant (B80 canonical); SL(5) power sums scatter (the gauge-INVARIANT
symmetric functions differ across seeds -> the spectrum itself is seed-dependent). A few F_p calls."""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b84_gb", _ROOT / "frontier" / "B84_sl5_gauge_barrier" / "probe.py")
B84 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B84)


def test_sl4_spectrum_seed_canonical():
    """SL(4): the gauge-invariant power sums are seed-invariant -- why B80's pinv-limit works."""
    assert B84.power_sums_seed_canonical(4, seeds=(20, 33)) is True


def test_sl5_spectrum_scatters_I1_refuted():
    """SL(5): the gauge-INVARIANT power sums scatter across seeds -> the spectrum itself is
    seed-dependent (non-convergence, not a basis ambiguity). I1 refuted."""
    assert B84.power_sums_seed_canonical(5, seeds=(20, 33)) is False
    ps = B84.sl5_power_sums_over_seeds(seeds=(20, 33))
    # tr(DT_0) (the FIRST power sum, basis-independent) already differs across the two seeds
    assert ps[20][0] != ps[33][0], ("tr(DT_0) must differ across seeds", ps)
