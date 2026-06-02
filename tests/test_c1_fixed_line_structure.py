"""Tests for B55 c=1 fixed-line structure (general m)."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PROBE_PATH = ROOT / "frontier" / "B55_c1_fixed_line_structure" / "probe.py"


def load_probe():
    spec = importlib.util.spec_from_file_location("b55_c1_fixed_line_structure", PROBE_PATH)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_b55_all_checks_pass():
    probe = load_probe()
    assert all(item.ok for item in probe.run_checks())


def test_symmetric_sector_mod4_symbolic():
    probe = load_probe()
    m, t = sp.symbols("m t")
    for residue in range(4):
        sym, _ = probe._sectors(probe.jacobian_symbolic_class(residue, m))
        assert sp.expand(sym.charpoly(t).as_expr() - probe.expected_symmetric(residue, t)) == 0


def test_antisymmetric_sector_is_charM_for_all_m():
    probe = load_probe()
    m, t = sp.symbols("m t")
    expected = sp.expand((t - 1) * (t + 1) * (t**2 - m * t - 1))
    for residue in range(4):
        _, anti = probe._sectors(probe.jacobian_symbolic_class(residue, m))
        assert sp.expand(anti.charpoly(t).as_expr() - expected) == 0
