"""Unit and pytest verification suite for Phase 11 (`165 / 165` Cumulative Controls)."""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from phase11_toe.p11_1_h3_huygens_propagator_exactness import run_gate_p11_1_h3_huygens_propagator_exactness
from phase11_toe.p11_2_porti_adjoint_torsion import run_gate_p11_2_porti_adjoint_torsion
from phase11_toe.p11_3_one_loop_overtone_partition import run_gate_p11_3_one_loop_overtone_partition
from phase11_toe.p11_4_joint_consistency import run_gate_p11_4_joint_consistency
from phase11_toe.phase11_engine import verify_all_phase11_seals
import referee_phase11


class TestPhase11Suite(unittest.TestCase):
    """Comprehensive verification tests for Phase 11 gates, seals, Track-A 0-of-19 firewall, and 165/165 referee."""

    def test_01_preregistration_seals_1_to_11_and_v1_lock(self) -> None:
        seals = verify_all_phase11_seals(PROJECT_ROOT)
        self.assertTrue(seals["all_seals_intact"])
        self.assertIn("phase11", seals["phases"])
        self.assertTrue(seals["phases"]["phase11"]["seal_intact"])
        self.assertTrue(seals["track_a_v1_predictions_sha256"]["v1_lock_intact"])

    def test_02_gates_p11_1_to_p11_4_track_a(self) -> None:
        g1 = run_gate_p11_1_h3_huygens_propagator_exactness()
        self.assertTrue(g1["gate_p11_1_passed"])
        self.assertLess(g1["h3_huygens_radial_pde_benchmarks"]["h3_d3_50d_max_pde_residual"], 1e-45)
        self.assertLess(g1["exact_h3_3pt_propagator_track_a"]["haar_10trial_SU3x5_max_err"], 1e-11)

        g2 = run_gate_p11_2_porti_adjoint_torsion(g1)
        self.assertTrue(g2["gate_p11_2_passed"])
        self.assertLess(g2["m004_benchmarks_60d"]["porti_2sqrt3_abs_err"], 1e-35)
        self.assertLess(g2["m004_benchmarks_60d"]["presentation_invariance_tau_err"], 1e-35)

        g3 = run_gate_p11_3_one_loop_overtone_partition(g1, g2)
        self.assertTrue(g3["gate_p11_3_passed"])
        self.assertLess(g3["q_series_benchmarks_50d"]["haar_10trial_branch_11a_max_err"], 1e-11)

        g4 = run_gate_p11_4_joint_consistency(g1, g3)
        self.assertTrue(g4["gate_p11_4_passed"])
        self.assertTrue(g4["strict_scale_ordering_satisfied"])

    def test_03_saved_phase11_ledger_26_tier1_and_four_branch_shootout(self) -> None:
        res_path = PROJECT_ROOT / "outputs" / "phase11_results.json"
        self.assertTrue(res_path.exists())
        prod = json.loads(res_path.read_text(encoding="utf-8"))
        self.assertTrue(prod["all_phase11_gates_passed"])
        self.assertEqual(prod["track_a_empirical_inputs_used"], "0 of 19")
        self.assertEqual(prod["track_b_continuous_fitted_or_calibrated_parameters"], 0)

        g5 = prod["gate_p11_5_track_b_scorecard"]
        comp = g5["four_branch_36_observable_comparison"]
        self.assertEqual(comp["branch_11A_susy_bulk"]["total_tier1_of_36"], 26)
        self.assertEqual(comp["branch_11A_susy_bulk"]["total_passing_of_36"], 36)
        self.assertEqual(comp["branch_11B_gmy_graviton_M5"]["total_misses_of_36"], 0)
        self.assertGreater(comp["branch_11D_topological_cs_porti"]["beta_iso_1B_SD_M5"], 0.50)

    def test_04_zero_import_referee_165_cumulative_controls(self) -> None:
        verdict = referee_phase11.run_all_referee_checks(PROJECT_ROOT, write_verdict=False)
        self.assertTrue(verdict["all_referee_checks_passed"])
        self.assertTrue(verdict["ast_guardrail_scan"]["passed"])
        self.assertEqual(verdict["phase11_new_controls"]["caught"], 20)
        self.assertEqual(verdict["planted_fault_controls"]["total"], 165)
        self.assertEqual(verdict["planted_fault_controls"]["caught"], 165)


if __name__ == "__main__":
    unittest.main()
