#!/usr/bin/env python3
"""
Regression test for B1782: Cosmological Constant Derivation and Unimodular Quantum Vacuum Decoupling.
"""

import json
import pathlib
import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]

def test_b1782_artifacts_exist():
    arc_dir = ROOT / "frontier" / "B1782_cosmological_constant_and_unimodular_gravity"
    assert (arc_dir / "FINDINGS.md").is_file()
    assert (arc_dir / "arc_verdict.json").is_file()
    assert (arc_dir / "verification" / "cosmological_constant_unimodular.py").is_file()
    assert (arc_dir / "verification" / "cosmological_constant_unimodular.json").is_file()
    assert (arc_dir / "verification" / "cosmological_constant_unimodular_run.txt").is_file()

def test_b1782_cosmological_constant_precision():
    data = json.loads((ROOT / "frontier" / "B1782_cosmological_constant_and_unimodular_gravity" / "verification" / "cosmological_constant_unimodular.json").read_text(encoding="utf-8"))
    cc = data["cosmological_constant"]

    assert pytest.approx(cc["rho_DE_derived_GeV4"], rel=1e-3) == 2.7956e-47
    assert cc["relative_error"] < 0.002  # within 0.2% of observation
    assert abs(cc["pull_sigma"]) < 0.10  # less than 0.1 sigma pull
    assert cc["chi2"] < 0.01

def test_b1782_unimodular_vacuum_decoupling():
    data = json.loads((ROOT / "frontier" / "B1782_cosmological_constant_and_unimodular_gravity" / "verification" / "cosmological_constant_unimodular.json").read_text(encoding="utf-8"))
    uni = data["unimodular_gravity"]

    assert uni["vacuum_energy_decoupled"] is True
    assert uni["trace_free_energy_momentum_residual"] < 1e-10

def test_b1782_verdict_discipline():
    verdict_path = ROOT / "frontier" / "B1782_cosmological_constant_and_unimodular_gravity" / "arc_verdict.json"
    data = json.loads(verdict_path.read_text(encoding="utf-8"))

    assert data["id"] == "B1782"
    assert data["verdict"] == "PROVED"
    assert "P-409" in data["points"]
    assert "cosmological constant" in data["claim_one_line"].lower()
