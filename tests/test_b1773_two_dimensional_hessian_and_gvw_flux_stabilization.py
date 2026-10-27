#!/usr/bin/env python3
"""
Regression test for B1773: Two-dimensional Hessian evaluation and Gukov-Vafa-Witten
flux stabilization of the axion Re(tau).
"""

import json
import math
import pathlib
import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]

def test_b1773_artifacts_exist():
    arc_dir = ROOT / "frontier" / "B1773_two_dimensional_hessian_and_gvw_flux_stabilization"
    assert (arc_dir / "FINDINGS.md").is_file()
    assert (arc_dir / "arc_verdict.json").is_file()
    assert (arc_dir / "verification" / "two_dim_hessian.py").is_file()
    assert (arc_dir / "verification" / "two_dim_hessian.json").is_file()
    assert (arc_dir / "verification" / "two_dim_hessian_run.txt").is_file()

def test_b1773_2d_hessian_and_flux_stabilization():
    data = json.loads((ROOT / "frontier" / "B1773_two_dimensional_hessian_and_gvw_flux_stabilization" / "verification" / "two_dim_hessian.json").read_text(encoding="utf-8"))

    # 1. Apex geometry
    assert pytest.approx(data["tau_star"][0], rel=1e-4) == 1.0 / 3.0
    assert pytest.approx(data["tau_star"][1], rel=1e-4) == math.sqrt(84.0) / 3.0
    assert data["flux_quanta"] == [1, 3]

    # 2. Pure Eisenstein deficit (axion unstabilized)
    eisen = data["v_eisen_derivatives"]
    assert abs(eisen["dV_dx"]) < 1e-5
    assert abs(eisen["dV_dy"]) < 1e-5
    assert eisen["d2V_dx2"] < 0  # Tachyonic/flat in x
    assert eisen["d2V_dy2"] > 10.0  # Stable radial well
    assert eisen["det_Hessian"] < 0  # Saddle point in 2D

    # 3. Total potential with GVW flux (2D stable minimum)
    tot = data["v_tot_derivatives"]
    assert abs(tot["dV_dx"]) < 1e-5
    assert abs(tot["dV_dy"]) < 1e-5
    assert tot["d2V_dx2"] > 2.0  # Positive axion curvature
    assert tot["d2V_dy2"] > 10.0  # Positive radial curvature
    assert abs(tot["d2V_dxdy"]) < 1e-4  # Decoupled
    assert tot["det_Hessian"] > 40.0  # Strictly positive-definite
    assert data["is_stable_2d"] is True

def test_b1773_verdict_discipline():
    verdict_path = ROOT / "frontier" / "B1773_two_dimensional_hessian_and_gvw_flux_stabilization" / "arc_verdict.json"
    data = json.loads(verdict_path.read_text(encoding="utf-8"))

    assert data["id"] == "B1773"
    assert data["verdict"] == "PROVED"
    assert "P-400" in data["points"]
    assert "Hessian" in data["claim_one_line"]
