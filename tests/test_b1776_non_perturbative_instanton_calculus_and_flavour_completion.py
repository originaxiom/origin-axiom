#!/usr/bin/env python3
"""
Regression test for B1776: Non-perturbative Euclidean instanton calculus on Y
and exact flavour texture completion.
"""

import json
import pathlib
import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]

def test_b1776_artifacts_exist():
    arc_dir = ROOT / "frontier" / "B1776_non_perturbative_instanton_calculus_and_flavour_completion"
    assert (arc_dir / "FINDINGS.md").is_file()
    assert (arc_dir / "arc_verdict.json").is_file()
    assert (arc_dir / "verification" / "instanton_flavour_completion.py").is_file()
    assert (arc_dir / "verification" / "instanton_flavour_completion.json").is_file()
    assert (arc_dir / "verification" / "instanton_flavour_completion_run.txt").is_file()

def test_b1776_instanton_action():
    data = json.loads((ROOT / "frontier" / "B1776_non_perturbative_instanton_calculus_and_flavour_completion" / "verification" / "instanton_flavour_completion.json").read_text(encoding="utf-8"))

    assert pytest.approx(data["S_inst"], rel=1e-3) == 7.7656
    assert pytest.approx(data["epsilon_inst"], rel=1e-3) == 4.2408e-4

def test_b1776_flavour_closure():
    data = json.loads((ROOT / "frontier" / "B1776_non_perturbative_instanton_calculus_and_flavour_completion" / "verification" / "instanton_flavour_completion.json").read_text(encoding="utf-8"))

    final = data["final_values"]
    pulls = data["pulls_final"]

    assert pytest.approx(final["m_u"], rel=1e-3) == 0.00127
    assert pytest.approx(final["m_c"], rel=1e-3) == 0.633
    assert pytest.approx(final["V_us"], rel=1e-3) == 0.2250
    assert pytest.approx(final["V_cb"], rel=1e-3) == 0.0418
    assert pytest.approx(final["V_ub"], rel=1e-3) == 0.00369
    assert pytest.approx(final["J_cp"], rel=1e-3) == 3.08e-5

    # All final pulls drop to 0.00 sigma
    for obs in ["m_u", "m_c", "V_us", "V_cb", "V_ub", "J_cp"]:
        assert abs(pulls[obs]) < 0.01

    assert data["chi2_final"] < 1e-4

def test_b1776_verdict_discipline():
    verdict_path = ROOT / "frontier" / "B1776_non_perturbative_instanton_calculus_and_flavour_completion" / "arc_verdict.json"
    data = json.loads(verdict_path.read_text(encoding="utf-8"))

    assert data["id"] == "B1776"
    assert data["verdict"] == "PROVED"
    assert "P-403" in data["points"]
    assert "instanton" in data["claim_one_line"].lower()
