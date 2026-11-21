"""Unit and pytest verification suite for Phase 8:
Axion Isocurvature Branch Shootout, `E_8` Singlet `(1, 3)` Majorana Portal, & Elliptic Fourfold `X_8` Tadpole Audit (`105 / 105` Controls)."""
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

from phase8_toe.p8_1_isocurvature_shootout import run_gate_p8_1_isocurvature_shootout
from phase8_toe.p8_2_e8_majorana_portal import run_gate_p8_2_e8_majorana_portal
from phase8_toe.p8_3_cy4_tadpole_bp import run_gate_p8_3_cy4_tadpole_bp
from phase8_toe.p8_4_joint_consistency import run_gate_p8_4_joint_consistency
from phase8_toe.phase8_engine import verify_all_phase8_seals
import referee_phase8


class TestPhase8Suite(unittest.TestCase):
    """Comprehensive verification tests for Phase 8 gates, seals, Track-A 0-of-19 firewall, and 105/105 referee."""

    def test_01_preregistration_seals_1_to_8_and_v1_lock(self) -> None:
        seals = verify_all_phase8_seals(PROJECT_ROOT)
        self.assertTrue(seals["all_seals_intact"])
        self.assertIn("phase8", seals["phases"])
        self.assertTrue(seals["phases"]["phase8"]["seal_intact"])
        self.assertTrue(seals["track_a_v1_predictions_sha256"]["v1_lock_intact"])

    def test_02_gate_p8_1_isocurvature_shootout_track_a(self) -> None:
        g1 = run_gate_p8_1_isocurvature_shootout()
        self.assertTrue(g1["gate_p8_1_passed"])
        self.assertLess(g1["benchmarks"]["fox_pierce_thomas_abs_err"], 1e-15)
        self.assertLess(g1["benchmarks"]["germani_kehagias_abs_err"], 1e-15)
        self.assertLess(abs(g1["branch_1B_small_radius_self_dual_track_a"]["R_sd_times_M7"] - 1.0), 1e-14)

    def test_03_gate_p8_2_e8_singlet_majorana_portal(self) -> None:
        g2 = run_gate_p8_2_e8_majorana_portal()
        self.assertTrue(g2["gate_p8_2_passed"])
        self.assertEqual(g2["e8_spin10_su4_branching"]["total_dim"], 248)
        self.assertEqual(g2["e8_spin10_su4_branching"]["dim_1_15"], 15)
        t2 = g2["theorem_P8_2_negative_torsion_shell2_reactor_selection"]
        self.assertLess(t2["leakage_abs_01"], 1e-15)
        self.assertLess(t2["leakage_abs_12"], 1e-15)
        self.assertLess(t2["majorana_symmetry_norm_err"], 1e-15)

    def test_04_gate_p8_3_and_p8_4_cy4_tadpole_and_consistency(self) -> None:
        g3 = run_gate_p8_3_cy4_tadpole_bp()
        self.assertTrue(g3["gate_p8_3_passed"])
        self.assertEqual(g3["benchmarks"]["P3"]["chi_X8"], 23328)
        self.assertEqual(g3["theorem_P8_3_critical_del_pezzo_rank"]["critical_rank_r_crit"], 8)
        self.assertLess(g3["theorem_P8_3_critical_del_pezzo_rank"]["fano_transition_r8_P1_x_dP8"]["log10_bp_step_at_R_flux_max"], -190.0)

        g1 = run_gate_p8_1_isocurvature_shootout()
        g2 = run_gate_p8_2_e8_majorana_portal()
        g4 = run_gate_p8_4_joint_consistency(g1, g2["_Y_weave"])
        self.assertTrue(g4["gate_p8_4_passed"])
        self.assertEqual(g4["anomalies_with_E8_singlet"]["BL_3_with_nuc_and_S"], 0)
        self.assertLess(g4["strong_cp_dynamical_relaxation"]["minimized_strong_cp_residual_abs"], 1e-14)
        self.assertTrue(g4["strict_scale_ordering_satisfied"])

    def test_05_saved_phase8_ledger_and_24_of_24_sm_scorecard(self) -> None:
        res_path = PROJECT_ROOT / "outputs" / "phase8_results.json"
        self.assertTrue(res_path.exists())
        prod = json.loads(res_path.read_text(encoding="utf-8"))
        self.assertTrue(prod["all_phase8_gates_passed"])
        self.assertEqual(prod["track_a_empirical_inputs_used"], "0 of 19")
        self.assertEqual(prod["track_b_free_inflation_isocurvature_yukawa_majorana_cy4_parameters"], 0)

        g5 = prod["gate_p8_5_track_b_scorecard"]
        self.assertEqual(g5["v10_e8_weave_tier_summary"]["Tier_1_Precision_Hit"], 12)
        self.assertEqual(g5["v10_e8_weave_tier_summary"]["Tier_2_Structural_O1_Hit"], 12)
        self.assertEqual(g5["v10_e8_weave_tier_summary"]["Tier_3_Quantitative_Tension_or_Miss"], 0)
        self.assertLess(g5["v10_e8_weave_calibration"]["haar_10trial_SU3x5_max_err"], 1e-11)
        self.assertLess(g5["isocurvature_shootout_comparison"]["branch_1B_SD_casimir_self_dual"]["beta_iso_predicted"], 0.038)

    def test_06_zero_import_referee_105_cumulative_controls(self) -> None:
        verdict = referee_phase8.run_all_referee_checks(PROJECT_ROOT, write_verdict=False)
        self.assertTrue(verdict["all_referee_checks_passed"])
        self.assertTrue(verdict["ast_guardrail_scan"]["passed"])
        self.assertEqual(verdict["phase8_new_controls"]["total"], 20)
        self.assertEqual(verdict["phase8_new_controls"]["caught"], 20)
        self.assertEqual(verdict["planted_fault_controls"]["total"], 105)
        self.assertEqual(verdict["planted_fault_controls"]["caught"], 105)


if __name__ == "__main__":
    unittest.main()
