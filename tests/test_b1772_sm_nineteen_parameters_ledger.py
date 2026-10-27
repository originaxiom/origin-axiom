#!/usr/bin/env python3
"""
Regression test for B1772: Master synthesis of all 19 Standard Model free parameters
under THE_BAR on seat branch agy/frontier-2026-10-26.
"""

import json
import pathlib
import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]

def test_b1772_artifacts_exist():
    arc_dir = ROOT / "frontier" / "B1772_the_nineteen_sm_parameters_synthesis"
    assert (arc_dir / "FINDINGS.md").is_file()
    assert (arc_dir / "arc_verdict.json").is_file()
    assert (arc_dir / "verification" / "sm_nineteen_parameters_ledger.py").is_file()
    assert (arc_dir / "verification" / "sm_nineteen_parameters_ledger.json").is_file()
    assert (arc_dir / "verification" / "sm_nineteen_parameters_ledger_run.txt").is_file()

def test_b1772_nineteen_parameters_completeness():
    ledger_path = ROOT / "frontier" / "B1772_the_nineteen_sm_parameters_synthesis" / "verification" / "sm_nineteen_parameters_ledger.json"
    data = json.loads(ledger_path.read_text(encoding="utf-8"))

    # Exactly 19 parameters
    assert data["total_parameters"] == 19
    params = data["parameters"]
    assert len(params) == 19

    param_dict = {p["parameter"]: p for p in params}

    # 1-3 Gauge couplings
    assert "alpha_s" in param_dict
    assert "sin2_theta_w" in param_dict
    assert "alpha_em_inv" in param_dict
    assert pytest.approx(param_dict["alpha_s"]["predicted"], rel=1e-3) == 0.1180
    assert param_dict["sin2_theta_w"]["rel_diff"] < 0.002
    assert param_dict["alpha_em_inv"]["rel_diff"] < 0.001

    # 4-5 Electroweak / Higgs sector
    assert "v_vev" in param_dict
    assert "m_higgs" in param_dict
    assert pytest.approx(param_dict["v_vev"]["predicted"], rel=1e-3) == 246.22
    assert pytest.approx(param_dict["m_higgs"]["predicted"], rel=1e-2) == 125.46
    assert abs(param_dict["m_higgs"]["pull_sigma"]) < 2.0

    # 6-14 Fermion masses
    for f in ["m_top", "m_bottom", "m_charm", "m_strange", "m_up", "m_down", "m_tau", "m_mu", "m_e"]:
        assert f in param_dict
        assert param_dict[f]["predicted"] > 0.0

    # 15-18 CKM parameters
    for c in ["V_us", "V_cb", "V_ub", "J_cp"]:
        assert c in param_dict
        assert param_dict[c]["predicted"] > 0.0

    # 19 Strong CP
    assert "theta_bar" in param_dict
    assert param_dict["theta_bar"]["predicted"] == 0.0

    # Strict THE_BAR firewall
    assert data["the_bar_certified_count"] == 0
    assert "0 of 19" in data["unconditional_status"]

def test_b1772_verdict_discipline():
    verdict_path = ROOT / "frontier" / "B1772_the_nineteen_sm_parameters_synthesis" / "arc_verdict.json"
    data = json.loads(verdict_path.read_text(encoding="utf-8"))

    assert data["id"] == "B1772"
    assert data["verdict"] == "PROVED"
    assert "P-399" in data["points"]
    assert "0 of 19" in data["claim_one_line"]
