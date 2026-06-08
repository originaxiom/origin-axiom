"""Locks for B124 -- reciprocal (lambda,1/lambda) pairs + time-reversal involution.

Sec.1 is GENERIC symplectic structure (the void reciprocal pair / inverse swap); Sec.2 is the metallic-specific
det=-1 sign/chirality residue -- expanding==contracting EXACTLY (no arrow), det=+1 has no negative modes, and the
exact 'excess' constant is bookkeeping-dependent / OPEN (the raw +-1 excess is period-4, NOT floor(n/2)).
"""
import importlib.util
import pathlib

import pytest

_ROOT = pathlib.Path(__file__).resolve().parents[1]


def _load():
    spec = importlib.util.spec_from_file_location(
        "b124_probe", _ROOT / "frontier/B124_time_reversal_reciprocity/probe.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


B124 = _load()


def test_void_reciprocal_time_reversal_generic():
    r = B124.void_reciprocal_time_reversal()
    assert r["void_spectrum_is_phi2_m1_phi-2"]
    assert r["det_is_minus_one"]
    assert r["reciprocal_pair_phi2_phi-2_eq_1"]
    assert r["inverse_map_spectrum_is_reciprocals_swap_stable_unstable"]


def test_expanding_equals_contracting_every_n_both_det():
    # The decisive recompute: NO arrow -- the two time directions have identically many modes.
    assert B124.tower_expanding_equals_contracting(nmax=10)["all_expanding_equals_contracting"]


def test_det_plus_one_has_no_negative_modes():
    r = B124.det_plus_one_has_no_negative_modes(nmax=10)
    assert r["det_plus1_negative_modes_all_zero"]
    assert r["det_minus1_carries_negative_modes"]   # the metallic-specific chirality residue


def test_pm1_excess_is_period4_not_floor():
    r = B124.pm1_excess_is_period4_not_floor(nmax=10)
    assert r["raw_pm1_excess_n2.."] == [-1, 0, 1, 0, -1, 0, 1, 0, -1]
    assert r["is_period4_oscillation"]
    assert not r["raw_excess_equals_floor"]         # do NOT bank floor(n/2) as the exact constant


def test_chirality_not_time_direction():
    r = B124.chirality_not_time_direction()
    assert r["time_direction_symmetric_no_arrow"]   # T preserved
    assert r["chirality_broken_det_minus_one"]      # P broken (det=-1)


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))
