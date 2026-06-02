"""Tests for B59 SL(4) fixed-line factorization (numerical, method-validated)."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
PROBE_PATH = ROOT / "frontier" / "B59_sl4_factorization" / "probe.py"


def load_probe():
    spec = importlib.util.spec_from_file_location("b59_sl4_factorization", PROBE_PATH)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_b59_checks_pass():
    probe = load_probe()
    assert all(item.ok for item in probe.run_checks())


def test_method_reproduces_sl3_ground_truth():
    # the credibility anchor: the extrapolation method must reproduce B55's c=3 spectrum
    probe = load_probe()
    spec = probe.fixed_line_spectrum(3, seeds=(10,), epss=np.array([0.04, 0.06, 0.08, 0.10, 0.12]))
    phi2 = ((1 + 5 ** 0.5) / 2) ** 2
    target = [1.0, -1.0, phi2, 1 / phi2] + list(np.roots([1, 1, -1])) + list(np.roots([1, -4, -1]))
    assert probe._max_match(spec, target) < 0.02
