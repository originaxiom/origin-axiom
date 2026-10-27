#!/usr/bin/env python3
"""
Regression test for B1771: Topological threshold index Delta b_2 = 28 and
forward Standard Model gauge coupling prediction.
"""

import json
import math
import pathlib
import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]

def test_b1771_artifacts_exist():
    arc_dir = ROOT / "frontier" / "B1771_topological_threshold_index_and_forward_gauge_couplings"
    assert (arc_dir / "FINDINGS.md").is_file()
    assert (arc_dir / "arc_verdict.json").is_file()
    assert (arc_dir / "verification" / "forward_gauge_couplings.py").is_file()
    assert (arc_dir / "verification" / "forward_gauge_couplings.json").is_file()
    assert (arc_dir / "verification" / "forward_gauge_couplings_run.txt").is_file()

def test_b1771_forward_gauge_predictions():
    data = json.loads((ROOT / "frontier" / "B1771_topological_threshold_index_and_forward_gauge_couplings" / "verification" / "forward_gauge_couplings.json").read_text(encoding="utf-8"))

    # 1. Geometry and DKL factor
    assert pytest.approx(data["tau_star"][0], rel=1e-4) == 1.0 / 3.0
    assert pytest.approx(data["tau_star"][1], rel=1e-4) == math.sqrt(84.0) / 3.0
    assert pytest.approx(data["dkl_factor"], rel=1e-4) == 1.389298

    # 2. Topological threshold index is exact integer 28
    assert data["delta_b2_topological"] == 28
    assert pytest.approx(data["gap_2_forward"], rel=1e-4) == 3.095591

    # 3. High precision forward predictions at M_Z
    # sin^2 theta_W within 0.1% relative error
    assert pytest.approx(data["pred_sin2_theta_w"], rel=1e-3) == 0.231444
    assert data["rel_diff_sin2_theta_w"] < 0.001  # < 0.1%

    # alpha_EM^-1 within 0.03% relative error
    assert pytest.approx(data["pred_alpha_em_inv"], rel=1e-3) == 127.9872
    assert data["rel_diff_alpha_em_inv"] < 0.0003  # < 0.03%

    # alpha_s matches target 0.1180
    assert pytest.approx(data["pred_alpha_s"], rel=1e-4) == 0.1180

def test_b1771_verdict_discipline():
    verdict_path = ROOT / "frontier" / "B1771_topological_threshold_index_and_forward_gauge_couplings" / "arc_verdict.json"
    data = json.loads(verdict_path.read_text(encoding="utf-8"))

    assert data["id"] == "B1771"
    assert data["verdict"] == "PROVED"
    assert "P-398" in data["points"]
    assert "28" in data["claim_one_line"]
