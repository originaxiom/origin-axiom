"""Tests for B51 symbolic-m SL(3) factorization."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PROBE_PATH = ROOT / "frontier" / "B51_sl3_symbolic_m_factorization" / "probe.py"


def load_probe():
    spec = importlib.util.spec_from_file_location("b51_sl3_symbolic_m_factorization", PROBE_PATH)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_b51_all_checks_pass():
    probe = load_probe()
    checks = probe.run_checks()
    assert all(item.ok for item in checks)


def test_derivative_closed_forms_match_initial_values():
    probe = load_probe()
    assert probe.tau_derivative_row(sp.Integer(-1)) == sp.Matrix([[0, 0, 0, 0, 0, 1, 0, 0]])
    assert probe.tau_derivative_row(sp.Integer(0)) == sp.Matrix([[0, 1, 0, 0, 0, 0, 0, 0]])
    assert probe.tau_derivative_row(sp.Integer(1)) == sp.Matrix([[0, 0, 1, 0, 0, 0, 0, 0]])
