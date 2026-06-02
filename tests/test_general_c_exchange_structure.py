"""Tests for B54 general-c exchange structure of the metallic SL(3) trace map."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PROBE_PATH = ROOT / "frontier" / "B54_general_c_exchange_structure" / "probe.py"


def load_probe():
    spec = importlib.util.spec_from_file_location("b54_general_c_exchange_structure", PROBE_PATH)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_b54_all_checks_pass():
    probe = load_probe()
    checks = probe.run_checks()
    assert all(item.ok for item in checks)


def test_exchange_commutes_for_symbolic_c():
    probe = load_probe()
    c = sp.symbols("c")
    exchange = probe.exchange_involution()
    for m_value in (1, 2, 3):
        jacobian = probe.symbolic_jacobian(m_value, c)
        assert sp.simplify(jacobian * exchange - exchange * jacobian) == sp.zeros(8)


def test_c1_sectors_are_eisenstein_and_golden():
    probe = load_probe()
    t = sp.symbols("t")
    symmetric, antisymmetric, off_upper, off_lower = probe.sectors(1, sp.Integer(1))
    assert off_upper == sp.zeros(4) and off_lower == sp.zeros(4)
    assert sp.rem(symmetric.charpoly(t).as_expr(), t**2 - t + 1, t) == 0
    assert sp.rem(antisymmetric.charpoly(t).as_expr(), t**2 - t - 1, t) == 0
