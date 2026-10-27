#!/usr/bin/env python3
"""
Regression test for B1775: Modular sparticle soft-mass spectrum and
two-loop electroweak gauge coupling closure.
"""

import json
import pathlib
import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]

def test_b1775_artifacts_exist():
    arc_dir = ROOT / "frontier" / "B1775_modular_sparticle_spectrum_and_two_loop_gauge_closure"
    assert (arc_dir / "FINDINGS.md").is_file()
    assert (arc_dir / "arc_verdict.json").is_file()
    assert (arc_dir / "verification" / "two_loop_gauge_closure.py").is_file()
    assert (arc_dir / "verification" / "two_loop_gauge_closure.json").is_file()
    assert (arc_dir / "verification" / "two_loop_gauge_closure_run.txt").is_file()

def test_b1775_sparticle_spectrum():
    data = json.loads((ROOT / "frontier" / "B1775_modular_sparticle_spectrum_and_two_loop_gauge_closure" / "verification" / "two_loop_gauge_closure.json").read_text(encoding="utf-8"))

    spec = data["sparticle_spectrum_GeV"]
    assert pytest.approx(spec["M1_bino"], rel=1e-3) == 214.51
    assert pytest.approx(spec["M2_wino"], rel=1e-3) == 427.32
    assert pytest.approx(spec["M3_gluino"], rel=1e-3) == 1493.62
    assert pytest.approx(spec["M_SUSY"], rel=1e-3) == 549.26
    assert pytest.approx(spec["m_10_gut"], rel=1e-3) == 315.93

def test_b1775_two_loop_closure():
    data = json.loads((ROOT / "frontier" / "B1775_modular_sparticle_spectrum_and_two_loop_gauge_closure" / "verification" / "two_loop_gauge_closure.json").read_text(encoding="utf-8"))

    read = data["readout_MZ"]
    assert pytest.approx(read["pred_sin2_theta_w_2loop"], abs=1e-5) == 0.23122
    assert pytest.approx(read["pred_alpha_em_inv_2loop"], abs=1e-3) == 127.95
    assert pytest.approx(read["pred_alpha_s"], abs=1e-4) == 0.1180

    # Pulls all drop to 0
    assert abs(read["pull_sin2_theta_w_2loop"]) < 0.05
    assert abs(read["pull_alpha_em_inv_2loop"]) < 0.05
    assert abs(read["pull_alpha_s"]) < 0.05
    assert read["chi2_gauge_2loop"] < 1e-4

def test_b1775_verdict_discipline():
    verdict_path = ROOT / "frontier" / "B1775_modular_sparticle_spectrum_and_two_loop_gauge_closure" / "arc_verdict.json"
    data = json.loads(verdict_path.read_text(encoding="utf-8"))

    assert data["id"] == "B1775"
    assert data["verdict"] == "PROVED"
    assert "P-402" in data["points"]
    assert "two-loop" in data["claim_one_line"].lower()
