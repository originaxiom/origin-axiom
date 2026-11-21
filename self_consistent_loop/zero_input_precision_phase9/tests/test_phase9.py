"""Unit and pytest verification suite for Phase 9:
dP_8 Georgi-Jarlskog Tier-1 Promotion & Zero-Continuous-Input Gauge/Misalignment Audit (`125 / 125` Controls)."""
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

from phase9_toe.p9_1_dp8_georgi_jarlskog import run_gate_p9_1_dp8_georgi_jarlskog
from phase9_toe.p9_2_zero_input_couplings import run_gate_p9_2_zero_input_couplings
from phase9_toe.p9_3_thooft_coleman_misalignment import run_gate_p9_3_thooft_coleman_misalignment
from phase9_toe.p9_4_joint_zero_input_consistency import run_gate_p9_4_joint_zero_input_consistency
from phase9_toe.phase9_engine import verify_all_phase9_seals
import referee_phase9


class TestPhase9Suite(unittest.TestCase):
    """Comprehensive verification tests for Phase 9 gates, seals, Track-A 0-of-19 firewall, and 125/125 referee."""

    def test_01_preregistration_seals_1_to_9_and_v1_lock(self) -> None:
        seals = verify_all_phase9_seals(PROJECT_ROOT)
        self.assertTrue(seals["all_seals_intact"])
        self.assertIn("phase9", seals["phases"])
        self.assertTrue(seals["phases"]["phase9"]["seal_intact"])
        self.assertTrue(seals["track_a_v1_predictions_sha256"]["v1_lock_intact"])

    def test_02_gate_p9_1_and_p9_2_dp8_gj_and_zero_input_couplings(self) -> None:
        g1 = run_gate_p9_1_dp8_georgi_jarlskog()
        self.assertTrue(g1["gate_p9_1_passed"])
        self.assertEqual(g1["su5_georgi_jarlskog_benchmarks"]["dim_antisym_10x10_eq_45"], 45)
        self.assertLess(g1["su5_georgi_jarlskog_benchmarks"]["antisym_45_up_max_diag"], 1e-15)

        g2 = run_gate_p9_2_zero_input_couplings(g1)
        self.assertTrue(g2["gate_p9_2_passed"])
        self.assertLess(g2["two_wall_contino_pilo_benchmark"]["abs_err_50d"], 1e-40)
        self.assertLess(g2["zero_input_fixed_point_track_a"]["haar_10trial_SU3x5_max_err"], 1e-11)

    def test_03_gate_p9_3_and_p9_4_misalignment_and_consistency(self) -> None:
        g1 = run_gate_p9_1_dp8_georgi_jarlskog()
        g3 = run_gate_p9_3_thooft_coleman_misalignment(g1)
        self.assertTrue(g3["gate_p9_3_passed"])
        self.assertLess(g3["coleman_instanton_benchmark_abs_err"], 1e-15)
        self.assertLess(g3["thooft_coleman_misalignment_track_a"]["thooft_tree_phase_cancellation_err"], 1e-14)

        g4 = run_gate_p9_4_joint_zero_input_consistency(g1, g3)
        self.assertTrue(g4["gate_p9_4_passed"])
        self.assertEqual(g4["anomalies_with_E8_singlet"]["BL_3_with_nuc_and_S"], 0)
        self.assertLess(g4["strong_cp_v11"]["minimized_strong_cp_residual_abs"], 1e-14)
        self.assertTrue(g4["strict_scale_ordering_satisfied"])

    def test_04_saved_phase9_ledger_and_36_observable_zero_input_scorecard(self) -> None:
        res_path = PROJECT_ROOT / "outputs" / "phase9_results.json"
        self.assertTrue(res_path.exists())
        prod = json.loads(res_path.read_text(encoding="utf-8"))
        self.assertTrue(prod["all_phase9_gates_passed"])
        self.assertEqual(prod["track_a_empirical_inputs_used"], "0 of 19")
        self.assertEqual(prod["track_b_continuous_fitted_or_calibrated_parameters"], 0)

        g5 = prod["gate_p9_5_track_b_scorecard"]
        self.assertEqual(g5["v11_sm24_tier_summary"]["Tier_1_Precision_Hit"], 17)
        self.assertEqual(g5["v11_sm24_tier_summary"]["Tier_2_Structural_O1_Hit"], 7)
        self.assertEqual(g5["v11_sm24_tier_summary"]["Tier_3_Quantitative_Tension_or_Miss"], 0)
        self.assertEqual(g5["unified_36_observable_summary"]["total_tier1_precision_hits_of_36"], 23)
        self.assertEqual(g5["unified_36_observable_summary"]["total_passing_of_36"], 36)
        self.assertLess(g5["zero_input_misalignment_and_cmb_comparison"]["branch_1B_SD_beta_iso_at_theta_mis_0"], 0.038)

    def test_05_zero_import_referee_125_cumulative_controls(self) -> None:
        verdict = referee_phase9.run_all_referee_checks(PROJECT_ROOT, write_verdict=False)
        self.assertTrue(verdict["all_referee_checks_passed"])
        self.assertTrue(verdict["ast_guardrail_scan"]["passed"])
        self.assertEqual(verdict["phase9_new_controls"]["total"], 20)
        self.assertEqual(verdict["phase9_new_controls"]["caught"], 20)
        self.assertEqual(verdict["planted_fault_controls"]["total"], 125)
        self.assertEqual(verdict["planted_fault_controls"]["caught"], 125)


if __name__ == "__main__":
    unittest.main()
