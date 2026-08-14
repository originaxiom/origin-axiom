"""Locks B852 -- B451's instrument could not have found a phase transition.

This arc is NOT preregistered (the numerics were explored first), so its footing is the exact
positive control rather than a seal. These locks therefore weight the control heavily: if the
doubling map stops reproducing its closed form, nothing else here is interpretable.
"""
import importlib.util
from pathlib import Path

import numpy as np

_ROOT = Path(__file__).resolve().parents[1]
_SPEC = importlib.util.spec_from_file_location(
    "b852", _ROOT / "frontier" / "B852_parabolic_pressure" / "pressure.py")
b2 = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(b2)


# ---------------------------------------------------------------------------------------
# The positive control -- the arc's whole footing, since it carries no seal
# ---------------------------------------------------------------------------------------
def test_doubling_map_reproduces_its_exact_closed_form():
    """P(s) = (1-s) log 2, exactly. An unsealed arc leans entirely on a check like this."""
    worst = 0.0
    for s in (0.2, 0.5, 0.8, 1.0, 1.5, 2.0):
        got = b2.pressure(b2.DOUBLING, s, n=32)
        worst = max(worst, abs(got - (1 - s) * np.log(2)))
    assert worst < 1e-9, f"worst error {worst:.2e} -- the instrument is not trustworthy"


def test_uniformly_hyperbolic_pressure_is_analytic():
    """Second differences ~ 0 everywhere, INCLUDING at s=1 where the parabolic model breaks."""
    for s in (0.6, 0.9, 1.0, 1.1, 1.4):
        d2 = b2.second_difference(lambda t: b2.pressure(b2.DOUBLING, t, n=32), s)
        assert abs(d2) < 1e-6, f"kink at s={s}: P''~{d2:.2e}"


# ---------------------------------------------------------------------------------------
# The demonstration
# ---------------------------------------------------------------------------------------
def test_only_the_parabolic_model_has_a_plateau():
    """The transition IS the plateau. Hyperbolic and expanding controls must not show one."""
    assert not b2.has_plateau(b2.DOUBLING), "a horseshoe cannot have a phase transition"
    assert not b2.has_plateau(b2.gauss_branches(120)), "the induced map must lose the transition"
    assert b2.has_plateau(b2.FAREY), "the parabolic model must show one"


def test_inducing_away_the_parabolic_point_destroys_the_transition():
    """Gauss is Farey's jump transformation -- same dynamics, parabolic point removed.

    This is the structural echo of B737-P2 ('Dehn filling removes the cusp => destroys exactly
    this'), reached independently via thermodynamic formalism.
    """
    for s in (1.2, 1.5):
        farey = abs(b2.pressure(b2.FAREY, s, n=48))
        gauss = abs(b2.pressure(b2.gauss_branches(120), s, n=48))
        assert farey < 1e-2, f"Farey must sit on the plateau at s={s}"
        assert gauss > 0.1, f"Gauss must be well off zero at s={s} (got {gauss:.4f})"


def test_the_plateau_sharpens_under_refinement_while_the_positive_branch_does_not_move():
    """What makes the plateau a result rather than a rounding artifact."""
    off = [abs(b2.pressure(b2.FAREY, 1.2, n=n)) for n in (32, 48, 64)]
    assert off[0] > off[1] > off[2], f"plateau residuals must shrink with n: {off}"
    on = [b2.pressure(b2.FAREY, 0.5, n=n) for n in (32, 48, 64)]
    assert max(on) - min(on) < 1e-5, f"the s<1 branch must be converged: {on}"
    assert min(on) > 0.3, "and it must be genuinely positive, not near-zero"


# ---------------------------------------------------------------------------------------
# Honesty locks -- what an unsealed arc must keep saying
# ---------------------------------------------------------------------------------------
def _f():
    return (_ROOT / "frontier" / "B852_parabolic_pressure" / "FINDINGS.md").read_text("utf-8")


def test_the_arc_declares_it_is_not_preregistered():
    t = _f()
    assert "NOT PREREGISTERED" in t
    assert "exploratorily" in t, "the reason must be stated, not just the status"
    assert "worse than none" in t, "and why a retro-seal would be worse"


def test_the_arc_refuses_the_numerological_reading():
    """s=1 for the Farey map says NOTHING about m004's transition location."""
    t = _f()
    assert "model of a parabolic point" in t
    assert "not m004's cross-section" in t or "not m004" in t
    assert "numerology" in t.lower(), "the tempting misreading must be named and refused"


def test_the_arc_does_not_reopen_b451s_own_results():
    t = _f()
    assert "does not re-open B451" in t or "does not re-open b451" in t.lower()


def test_genericity_is_declared_untested():
    t = _f()
    assert "untested" in t.lower()
    assert "One parabolic model was tested" in t or "one parabolic model" in t.lower()
