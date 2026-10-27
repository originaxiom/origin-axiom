#!/usr/bin/env python3
"""
Regression test for B1778: Supergravity F-Term Modular Soft Sector Unification
and Complete 2D Higgs Potential Minimization.
"""

import json
import pathlib
import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]

def test_b1778_artifacts_exist():
    arc_dir = ROOT / "frontier" / "B1778_supergravity_soft_unification_and_dynamic_higgs_minimization"
    assert (arc_dir / "FINDINGS.md").is_file()
    assert (arc_dir / "arc_verdict.json").is_file()
    assert (arc_dir / "verification" / "sugra_soft_and_higgs_minimization.py").is_file()
    assert (arc_dir / "verification" / "sugra_soft_and_higgs_minimization.json").is_file()
    assert (arc_dir / "verification" / "sugra_soft_and_higgs_minimization_run.txt").is_file()

def test_b1778_sugra_soft_derivation():
    data = json.loads((ROOT / "frontier" / "B1778_supergravity_soft_unification_and_dynamic_higgs_minimization" / "verification" / "sugra_soft_and_higgs_minimization.json").read_text(encoding="utf-8"))
    sugra = data["sugra_module"]

    assert pytest.approx(sugra["D_tau_W"]["re"], abs=1e-5) == -1.5
    assert pytest.approx(sugra["D_tau_W"]["im"], abs=1e-5) == 0.0
    assert pytest.approx(sugra["F_tau"]["re"], rel=1e-3) == -22.655
    assert pytest.approx(sugra["F_tau"]["im"], abs=1e-5) == 0.0

    assert pytest.approx(sugra["M_half_GeV"], rel=1e-3) == 482.593
    assert pytest.approx(sugra["A0_GeV"], rel=1e-3) == -315.9315

def test_b1778_dynamic_higgs_minimization():
    data = json.loads((ROOT / "frontier" / "B1778_supergravity_soft_unification_and_dynamic_higgs_minimization" / "verification" / "sugra_soft_and_higgs_minimization.json").read_text(encoding="utf-8"))
    ew = data["electroweak_minimization"]

    # VEV dynamically output
    assert pytest.approx(ew["v_derived_GeV"], rel=1e-2) == 245.35
    assert ew["v_relative_error"] < 0.005  # within 0.5%
    assert pytest.approx(ew["tan_beta_derived"], rel=1e-3) == 9.85

    # Positive definite 2D Hessian
    hessian = ew["hessian"]
    assert hessian["is_positive_definite"] is True
    assert hessian["det_H"] > 1e9
    assert hessian["trace_H"] > 0

    # True stationary minimum
    assert ew["gradient"]["is_stationary"] is True

def test_b1778_verdict_discipline():
    verdict_path = ROOT / "frontier" / "B1778_supergravity_soft_unification_and_dynamic_higgs_minimization" / "arc_verdict.json"
    data = json.loads(verdict_path.read_text(encoding="utf-8"))

    assert data["id"] == "B1778"
    assert data["verdict"] == "PROVED"
    assert "P-405" in data["points"]
    assert "closures 1 and 2" in data["claim_one_line"].lower()
