#!/usr/bin/env python3
"""
Regression test for B1770: Strong CP invariant, tree-level phase evaluation,
and dynamical Peccei-Quinn axion relaxation.
"""

import json
import math
import pathlib
import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]

def test_b1770_strong_cp_artifacts_exist():
    arc_dir = ROOT / "frontier" / "B1770_strong_cp_invariant_and_axion_parity"
    assert (arc_dir / "FINDINGS.md").is_file()
    assert (arc_dir / "arc_verdict.json").is_file()
    assert (arc_dir / "verification" / "strong_cp_parity.py").is_file()
    assert (arc_dir / "verification" / "strong_cp_parity.json").is_file()
    assert (arc_dir / "verification" / "strong_cp_parity_run.txt").is_file()

def test_b1770_strong_cp_tree_level_phase_and_refutation():
    data = json.loads((ROOT / "frontier" / "B1770_strong_cp_invariant_and_axion_parity" / "verification" / "strong_cp_parity.json").read_text(encoding="utf-8"))
    
    # 1. Apex geometry
    assert pytest.approx(data["tau_star"][0], rel=1e-4) == 1.0 / 3.0
    assert pytest.approx(data["tau_star"][1], rel=1e-4) == math.sqrt(84.0) / 3.0
    assert pytest.approx(data["two_im_tau"], rel=1e-4) == 2.0 * math.sqrt(84.0) / 3.0

    # 2. Tree-level phase is non-zero (refuting naive tree-level zero)
    arg_tot = data["arg_det_tot_rad"]
    assert pytest.approx(arg_tot, abs=1e-2) == -1.856651
    assert abs(arg_tot) > 1.0  # O(1) radian phase

    # 3. Discrepancy with neutron EDM without axion
    tree_dn = data["tree_dn_ecm"]
    exp_bound = data["exp_dn_bound_ecm"]
    assert tree_dn > 1e-16
    assert tree_dn / exp_bound > 1e10  # Exceeds experimental limit by > 10 orders of magnitude

def test_b1770_dynamical_pq_axion_relaxation():
    data = json.loads((ROOT / "frontier" / "B1770_strong_cp_invariant_and_axion_parity" / "verification" / "strong_cp_parity.json").read_text(encoding="utf-8"))
    
    # 4. Axion decay constant in classic window
    f_a = data["f_a_GeV"]
    assert 1e9 < f_a < 1e17
    assert pytest.approx(f_a, rel=1e-2) == 1.2116e13

    # 5. Axion mass in sub-micro-eV range
    m_a_uev = data["m_a_uev"]
    assert 0.1 < m_a_uev < 5.0
    assert pytest.approx(m_a_uev, rel=1e-2) == 0.4808

    # 6. Dynamically relaxed effective angle and EDM
    assert data["theta_bar_eff"] == 0.0
    assert data["predicted_dn_ecm"] == 0.0

def test_b1770_verdict_discipline():
    verdict_path = ROOT / "frontier" / "B1770_strong_cp_invariant_and_axion_parity" / "arc_verdict.json"
    data = json.loads(verdict_path.read_text(encoding="utf-8"))
    
    assert data["id"] == "B1770"
    assert data["verdict"] == "PROVED"
    assert "P-397" in data["points"]
    
    # Strict gate: must not claim "theta_QCD = 0, parameter-free"
    claim = data["claim_one_line"]
    assert "theta_qcd = 0 parameter-free" not in claim.lower()
    assert "parameter-free" not in claim.lower()
    assert "f_a" in claim
