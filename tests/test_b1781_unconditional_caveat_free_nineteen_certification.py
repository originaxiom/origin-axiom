#!/usr/bin/env python3
"""
Regression test for B1781: Unconditional Parameter-Free and Caveat-Free
Certification of All Nineteen Standard Model Free Parameters Under THE_BAR.
"""

import json
import pathlib
import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]

def test_b1781_artifacts_exist():
    arc_dir = ROOT / "frontier" / "B1781_unconditional_caveat_free_nineteen_certification"
    assert (arc_dir / "FINDINGS.md").is_file()
    assert (arc_dir / "arc_verdict.json").is_file()
    assert (arc_dir / "verification" / "caveat_free_master_ledger.py").is_file()
    assert (arc_dir / "verification" / "caveat_free_master_ledger.json").is_file()
    assert (arc_dir / "verification" / "caveat_free_master_ledger_run.txt").is_file()

def test_b1781_global_statistics():
    data = json.loads((ROOT / "frontier" / "B1781_unconditional_caveat_free_nineteen_certification" / "verification" / "caveat_free_master_ledger.json").read_text(encoding="utf-8"))

    assert data["total_parameters"] == 19
    assert data["zero_pull_parameters"] == 13
    assert data["the_bar_certified_count"] == 19
    assert "UNCONDITIONALLY DERIVED AND CERTIFIED" in data["certification_status"]

    assert pytest.approx(data["total_chi2"], rel=1e-3) == 6.7867
    assert pytest.approx(data["reduced_chi2"], rel=1e-3) == 0.3572
    assert data["reduced_chi2"] < 0.40
    assert data["max_pull_sigma"] <= 2.01

def test_b1781_all_four_closures_resolved():
    data = json.loads((ROOT / "frontier" / "B1781_unconditional_caveat_free_nineteen_certification" / "verification" / "caveat_free_master_ledger.json").read_text(encoding="utf-8"))
    closures = data["all_four_closures_resolved"]

    assert "B1778" in closures["closure_1_soft_unification"]
    assert "B1778" in closures["closure_2_dynamic_ew_minimization"]
    assert "B1779" in closures["closure_3_ray_singer_torsion_and_md"]
    assert "B1780" in closures["closure_4_dynamical_gut_scale"]

def test_b1781_verdict_discipline():
    verdict_path = ROOT / "frontier" / "B1781_unconditional_caveat_free_nineteen_certification" / "arc_verdict.json"
    data = json.loads(verdict_path.read_text(encoding="utf-8"))

    assert data["id"] == "B1781"
    assert data["verdict"] == "PROVED"
    assert "P-408" in data["points"]
    assert "unconditional 19 of 19" in data["claim_one_line"].lower()
