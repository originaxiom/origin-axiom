"""Locks the reproducible audit sampler.

The property that matters is not randomness -- it is that the draw is a FUNCTION of (frame, seed)
and of nothing else, so it cannot be steered after the verdicts are visible.
"""
import importlib.util
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "audit_sample", Path(__file__).resolve().parents[1] / "scripts" / "checks" / "audit_sample.py")
aus = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(aus)

FRAME = [f"B{i}_arc" for i in range(100, 200)]


def test_draw_is_reproducible():
    assert aus.draw(FRAME, 30) == aus.draw(FRAME, 30)


def test_draw_is_independent_of_input_order():
    """A caller who reorders the frame must not get a different sample."""
    assert aus.draw(FRAME, 30) == aus.draw(list(reversed(FRAME)), 30)


def test_draw_has_no_replacement_and_correct_size():
    s = aus.draw(FRAME, 30)
    assert len(s) == 30 == len(set(s))
    assert set(s) <= set(FRAME)


def test_draw_tracks_the_frame_not_the_auditor():
    """Change the data and the sample changes; that is the honest direction of dependence."""
    assert aus.draw(FRAME, 30) != aus.draw(FRAME + ["B999_new"], 30)


def test_a_different_seed_gives_a_different_draw():
    """So that quietly re-seeding to get a friendlier set is a visible act, not a silent one."""
    assert aus.draw(FRAME, 30, seed=1) != aus.draw(FRAME, 30, seed=2)


def test_oversized_n_returns_the_whole_frame():
    assert aus.draw(FRAME, 500) == sorted(FRAME)


def test_seed_constant_is_committed():
    assert aus.SEED == 20260730, "the audit seed is part of the preregistration, not a knob"
