#!/usr/bin/env python3
"""
Regression test for B1774: Exact analytic Chowla-Selberg derivation of the
modulus potential ratio t_* = 4.430013 from algebraic apex geometry y_* = sqrt(84)/3.
"""

import json
import math
import pathlib
import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]

def test_b1774_artifacts_exist():
    arc_dir = ROOT / "frontier" / "B1774_analytic_chowla_selberg_derivation_of_modulus_potential_ratio"
    assert (arc_dir / "FINDINGS.md").is_file()
    assert (arc_dir / "arc_verdict.json").is_file()
    assert (arc_dir / "verification" / "analytic_t_star.py").is_file()
    assert (arc_dir / "verification" / "analytic_t_star.json").is_file()
    assert (arc_dir / "verification" / "analytic_t_star_run.txt").is_file()

def test_b1774_analytic_chowla_selberg_formula():
    data = json.loads((ROOT / "frontier" / "B1774_analytic_chowla_selberg_derivation_of_modulus_potential_ratio" / "verification" / "analytic_t_star.json").read_text(encoding="utf-8"))

    # 1. Apex geometry
    y_star = math.sqrt(84.0) / 3.0
    assert pytest.approx(data["y_star"], rel=1e-12) == y_star

    # 2. Leading order formula: 2 pi^2 / sqrt(21)
    t_leading_expected = (2.0 * math.pi**2) / math.sqrt(21.0)
    assert pytest.approx(data["t_leading"], rel=1e-10) == t_leading_expected
    assert pytest.approx(data["t_leading"], rel=1e-5) == 4.307448

    # 3. Exact analytic Chowla-Selberg ratio
    assert pytest.approx(data["t_analytic"], rel=1e-8) == 4.43001302
    assert pytest.approx(data["t_full"], rel=1e-8) == 4.43001298

    # 4. Difference is suppressed by Bessel tail e^(-2 pi y) ~ 4.6e-9
    assert data["diff_analytic"] < 1e-7

    # 5. Inside W154 stability window [3.205, 4.624]
    assert data["in_w154_window"] is True

def test_b1774_verdict_discipline():
    verdict_path = ROOT / "frontier" / "B1774_analytic_chowla_selberg_derivation_of_modulus_potential_ratio" / "arc_verdict.json"
    data = json.loads(verdict_path.read_text(encoding="utf-8"))

    assert data["id"] == "B1774"
    assert data["verdict"] == "PROVED"
    assert "P-401" in data["points"]
    assert "chowla-selberg" in data["claim_one_line"].lower()
