"""Tests for B56 figure-eight invariant-surface negative control."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PROBE_PATH = ROOT / "frontier" / "B56_figure_eight_invariant_surface" / "probe.py"


def load_probe():
    spec = importlib.util.spec_from_file_location("b56_figure_eight_invariant_surface", PROBE_PATH)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_b56_all_checks_pass():
    probe = load_probe()
    assert all(item.ok for item in probe.run_checks())


def test_no_diagonal_representation_has_invariant_one_quarter():
    probe = load_probe()
    w = sp.symbols("w")
    for root in sp.roots(probe.diagonal_cubic(w)):
        assert sp.simplify(probe.diagonal_invariant(root) - sp.Rational(1, 4)) != 0
