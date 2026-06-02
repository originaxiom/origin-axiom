"""Tests for B58 SL(4) factor-count tower test (mechanism + obstruction)."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PROBE_PATH = ROOT / "frontier" / "B58_sl4_tower_test" / "probe.py"


def load_probe():
    spec = importlib.util.spec_from_file_location("b58_sl4_tower_test", PROBE_PATH)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_b58_mechanism_checks_pass():
    probe = load_probe()
    assert all(item.ok for item in probe.run_checks())


def test_sl4_identity_recursion_is_quadruple_root():
    probe = load_probe()
    r = sp.symbols("r")
    assert sp.factor(r**4 - 4 * r**3 + 6 * r**2 - 4 * r + 1) == (r - 1) ** 4
