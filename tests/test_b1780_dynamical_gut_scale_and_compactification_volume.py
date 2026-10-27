#!/usr/bin/env python3
"""
Regression test for B1780: Dynamical Derivation of the GUT Scale and Compactification Volume
from Genus-3 Nilpotent Geometry.
"""

import json
import pathlib
import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]

def test_b1780_artifacts_exist():
    arc_dir = ROOT / "frontier" / "B1780_dynamical_gut_scale_and_compactification_volume"
    assert (arc_dir / "FINDINGS.md").is_file()
    assert (arc_dir / "arc_verdict.json").is_file()
    assert (arc_dir / "verification" / "dynamical_gut_scale.py").is_file()
    assert (arc_dir / "verification" / "dynamical_gut_scale.json").is_file()
    assert (arc_dir / "verification" / "dynamical_gut_scale_run.txt").is_file()

def test_b1780_gut_scale_derivation():
    data = json.loads((ROOT / "frontier" / "B1780_dynamical_gut_scale_and_compactification_volume" / "verification" / "dynamical_gut_scale.json").read_text(encoding="utf-8"))
    geom = data["geometry"]
    gut = data["gut_scale"]

    assert pytest.approx(geom["modular_q"], rel=1e-3) == 4.6081e-9
    assert pytest.approx(geom["sqrt_q"], rel=1e-3) == 6.7883e-5
    assert pytest.approx(gut["M_gut_derived_GeV"], rel=1e-2) == 1.8907e14
    assert gut["relative_error"] < 0.005  # within 0.5% of empirical crossing

def test_b1780_verdict_discipline():
    verdict_path = ROOT / "frontier" / "B1780_dynamical_gut_scale_and_compactification_volume" / "arc_verdict.json"
    data = json.loads(verdict_path.read_text(encoding="utf-8"))

    assert data["id"] == "B1780"
    assert data["verdict"] == "PROVED"
    assert "P-407" in data["points"]
    assert "closure 4" in data["claim_one_line"].lower()
