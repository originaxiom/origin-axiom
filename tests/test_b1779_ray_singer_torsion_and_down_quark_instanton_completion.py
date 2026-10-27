#!/usr/bin/env python3
"""
Regression test for B1779: Ray-Singer Analytic Torsion on Genus-3 Quaternion Cover Y
and Non-Perturbative Down-Quark Instanton Completion.
"""

import json
import pathlib
import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]

def test_b1779_artifacts_exist():
    arc_dir = ROOT / "frontier" / "B1779_ray_singer_torsion_and_down_quark_instanton_completion"
    assert (arc_dir / "FINDINGS.md").is_file()
    assert (arc_dir / "arc_verdict.json").is_file()
    assert (arc_dir / "verification" / "ray_singer_down_instanton.py").is_file()
    assert (arc_dir / "verification" / "ray_singer_down_instanton.json").is_file()
    assert (arc_dir / "verification" / "ray_singer_down_instanton_run.txt").is_file()

def test_b1779_torsion_and_prefactor():
    data = json.loads((ROOT / "frontier" / "B1779_ray_singer_torsion_and_down_quark_instanton_completion" / "verification" / "ray_singer_down_instanton.json").read_text(encoding="utf-8"))
    geom = data["geometry"]
    inst = data["instanton_half_cycle"]

    assert geom["genus"] == 3
    assert geom["abs_euler_characteristic"] == 4
    assert pytest.approx(geom["prefactor_A_d"], rel=1e-3) == 6.273756
    assert pytest.approx(inst["S_half"], rel=1e-3) == 3.8828
    assert pytest.approx(inst["epsilon_half"], rel=1e-3) == 0.020593

def test_b1779_down_quark_closure():
    data = json.loads((ROOT / "frontier" / "B1779_ray_singer_torsion_and_down_quark_instanton_completion" / "verification" / "ray_singer_down_instanton.json").read_text(encoding="utf-8"))
    down = data["down_quark"]

    assert pytest.approx(down["md_intermediate_MeV"], rel=1e-3) == 2.784
    assert pytest.approx(down["md_final_MeV"], rel=1e-3) == 2.710
    assert abs(down["pull_final_sigma"]) < 0.01
    assert down["chi2_final"] < 1e-4

def test_b1779_verdict_discipline():
    verdict_path = ROOT / "frontier" / "B1779_ray_singer_torsion_and_down_quark_instanton_completion" / "arc_verdict.json"
    data = json.loads(verdict_path.read_text(encoding="utf-8"))

    assert data["id"] == "B1779"
    assert data["verdict"] == "PROVED"
    assert "P-406" in data["points"]
    assert "closure 3" in data["claim_one_line"].lower()
