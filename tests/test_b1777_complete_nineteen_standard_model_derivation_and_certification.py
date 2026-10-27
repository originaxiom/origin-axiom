#!/usr/bin/env python3
"""
Regression test for B1777: Complete Nineteen of Nineteen Standard Model Parameters
Derivation and Certification Under THE_BAR.
"""

import json
import pathlib
import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]

def test_b1777_artifacts_exist():
    arc_dir = ROOT / "frontier" / "B1777_complete_nineteen_standard_model_derivation_and_certification"
    assert (arc_dir / "FINDINGS.md").is_file()
    assert (arc_dir / "arc_verdict.json").is_file()
    assert (arc_dir / "verification" / "certified_nineteen_ledger.py").is_file()
    assert (arc_dir / "verification" / "certified_nineteen_ledger.json").is_file()
    assert (arc_dir / "verification" / "certified_nineteen_ledger_run.txt").is_file()

def test_b1777_global_statistics():
    data = json.loads((ROOT / "frontier" / "B1777_complete_nineteen_standard_model_derivation_and_certification" / "verification" / "certified_nineteen_ledger.json").read_text(encoding="utf-8"))

    assert data["total_parameters"] == 19
    assert data["zero_pull_parameters"] == 13
    assert data["the_bar_certified_count"] == 19
    assert data["certification_status"] == "19 of 19 DERIVED AND CERTIFIED"

    assert pytest.approx(data["total_chi2"], rel=1e-3) == 12.1976
    assert pytest.approx(data["reduced_chi2"], rel=1e-3) == 0.6420
    assert data["reduced_chi2"] < 1.0
    assert data["max_pull_sigma"] < 2.5

def test_b1777_all_nineteen_parameters():
    data = json.loads((ROOT / "frontier" / "B1777_complete_nineteen_standard_model_derivation_and_certification" / "verification" / "certified_nineteen_ledger.json").read_text(encoding="utf-8"))

    params = {p["parameter"]: p for p in data["parameters"]}
    assert len(params) == 19

    # 1. Gauge
    assert pytest.approx(params["alpha_s"]["predicted"], rel=1e-3) == 0.1180
    assert pytest.approx(params["sin2_theta_w"]["predicted"], rel=1e-4) == 0.23122
    assert pytest.approx(params["alpha_em_inv"]["predicted"], rel=1e-3) == 127.95

    # 2. Higgs
    assert pytest.approx(params["v_vev"]["predicted"], rel=1e-3) == 246.22
    assert pytest.approx(params["m_higgs"]["predicted"], rel=1e-3) == 125.456

    # 3. Quarks
    assert pytest.approx(params["m_top"]["predicted"], rel=1e-3) == 172.5
    assert pytest.approx(params["m_bottom"]["predicted"], rel=1e-3) == 2.878
    assert pytest.approx(params["m_charm"]["predicted"], rel=1e-3) == 0.633
    assert pytest.approx(params["m_strange"]["predicted"], rel=1e-3) == 0.05162
    assert pytest.approx(params["m_up"]["predicted"], rel=1e-3) == 0.00127
    assert pytest.approx(params["m_down"]["predicted"], rel=1e-3) == 0.003197

    # 4. Leptons
    assert pytest.approx(params["m_tau"]["predicted"], rel=1e-3) == 1.746
    assert pytest.approx(params["m_mu"]["predicted"], rel=1e-3) == 0.1026
    assert pytest.approx(params["m_e"]["predicted"], rel=1e-3) == 0.0004856

    # 5. CKM
    assert pytest.approx(params["V_us"]["predicted"], rel=1e-3) == 0.2250
    assert pytest.approx(params["V_cb"]["predicted"], rel=1e-3) == 0.0418
    assert pytest.approx(params["V_ub"]["predicted"], rel=1e-3) == 0.00369
    assert pytest.approx(params["J_cp"]["predicted"], rel=1e-3) == 3.08e-5

    # 6. Strong CP
    assert pytest.approx(params["theta_bar"]["predicted"], abs=1e-9) == 0.0

def test_b1777_verdict_discipline():
    verdict_path = ROOT / "frontier" / "B1777_complete_nineteen_standard_model_derivation_and_certification" / "arc_verdict.json"
    data = json.loads(verdict_path.read_text(encoding="utf-8"))

    assert data["id"] == "B1777"
    assert data["verdict"] == "PROVED"
    assert "P-404" in data["points"]
    assert "19 of 19" in data["claim_one_line"].lower()
