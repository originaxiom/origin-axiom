"""Unit and pytest verification suite for Phase 6:
Coherent Whitehead Weave, Zero-Anchor Scales, `11D` Horava-Witten Parent, & Cosmological Closure (`65 / 65` Controls)."""
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

from phase6_toe.phase6_engine import verify_all_phase6_seals
from phase6_toe.w1_whitehead_weave import run_gate_p6_1_whitehead_weave
from phase6_toe.w2_zero_anchor_hosotani import run_gate_p6_2_zero_anchor_hosotani
from phase6_toe.w3_horava_witten_11d import run_gate_p6_3_horava_witten_11d
from phase6_toe.w4_cosmology_dark_sector import run_gate_p6_4_cosmology_dark_sector_track_a
import referee_phase6


class TestPhase6Suite(unittest.TestCase):
    """Comprehensive verification tests for Phase 6 gates, seals, Track-A 0-of-19 firewall, and 65/65 referee."""

    def test_01_preregistration_seals_1_to_6_and_v1_lock(self) -> None:
        seals = verify_all_phase6_seals(PROJECT_ROOT)
        self.assertTrue(seals["all_seals_intact"])
        self.assertIn("phase6", seals["phases"])
        self.assertTrue(seals["phases"]["phase6"]["seal_intact"])
        self.assertTrue(seals["track_a_v1_predictions_sha256"]["v1_lock_intact"])

    def test_02_gate_p6_1_whitehead_parent_weave_and_shell1_zero(self) -> None:
        g1 = run_gate_p6_1_whitehead_weave()
        self.assertTrue(g1["gate_p6_1_passed"])
        self.assertTrue(g1["whitehead_parent_m129"]["is_chiral"])
        self.assertLess(g1["whitehead_parent_m129"]["vol_minus_4Catalan_err"], 1e-12)
        self.assertTrue(all(v["mirror_excluded"] for v in g1["whitehead_parent_m129"]["mirror_slope_exclusion"].values()))
        self.assertLess(g1["amphicheiral_shell1_leptogenesis_im_norm"], 1e-15)
        self.assertGreaterEqual(len(g1["same_bundle_overtones_M5"]), 8)

    def test_03_gate_p6_2_zero_anchor_scales_and_hosotani_ewsb(self) -> None:
        g1 = run_gate_p6_1_whitehead_weave()
        g2 = run_gate_p6_2_zero_anchor_hosotani(g1["_Y_weave"])
        self.assertTrue(g2["gate_p6_2_passed"])
        z2 = g2["track_a_zero_anchor_predictions"]
        self.assertGreater(z2["alpha_em_inv_MZ_0"], 125.0)
        self.assertLess(z2["alpha_em_inv_MZ_0"], 135.0)
        self.assertLess(g2["hosotani_1loop_ewsb"]["quadratic_coeff_UV_with_top"], 0.0)
        self.assertGreater(g2["hosotani_1loop_ewsb"]["quadratic_coeff_UV_without_top_plant"], 0.0)

    def test_04_gate_p6_3_11d_horava_witten_parent_and_anomalies(self) -> None:
        g3 = run_gate_p6_3_horava_witten_11d()
        self.assertTrue(g3["gate_p6_3_passed"])
        self.assertEqual(g3["spacetime_dimensions"]["d_total_M_theory"], 11)
        self.assertEqual(g3["horava_witten_boundary_audit"]["e8_wall_anomaly_residual"], 0)
        self.assertEqual(g3["dp9_bianchi_audit"]["n_M5_fivebranes"], 0)
        self.assertEqual(g3["chiral_4d_and_global_anomalies"]["BL_cubed_without_nuR_plant"], -1)
        self.assertEqual(g3["chiral_4d_and_global_anomalies"]["witten_su2_doublets_3gen"] % 2, 0)

    def test_05_gate_p6_4_planck_ratios_and_dynamical_strong_cp(self) -> None:
        g4 = run_gate_p6_4_cosmology_dark_sector_track_a(1.85e-13)
        self.assertTrue(g4["gate_p6_4_passed"])
        p4 = g4["track_a_dimensionless_planck_ratios"]
        self.assertLess(p4["dynamical_strong_cp_theta_eff"], 1e-12)
        self.assertGreater(p4["dynamical_strong_cp_d2V_min"], 0.999999999999)
        self.assertGreater(p4["pq_quality_plant_theta_eff"], 1e-5)

    def test_06_saved_phase6_ledger_and_zero_import_referee_65_controls(self) -> None:
        res_path = PROJECT_ROOT / "outputs" / "phase6_results.json"
        self.assertTrue(res_path.exists())
        prod = json.loads(res_path.read_text(encoding="utf-8"))
        self.assertTrue(prod["all_phase6_gates_passed"])
        self.assertEqual(prod["track_a_empirical_inputs_used"], "0 of 19")
        self.assertEqual(prod["track_b_free_yukawa_mixing_overtone_higgs_seesaw_parameters"], 0)

        g5 = prod["gate_p6_5_track_b_toe_scorecard"]
        self.assertEqual(g5["v8_weave_jq_tier"], "Tier_2_Structural_O1_Hit")
        self.assertGreater(g5["v8_weave_jq"], 9.9e-6)
        self.assertLess(g5["v8_weave_calibration"]["haar_10trial_SU3x5_max_err"], 1e-11)
        self.assertTrue(g5["zero_anchor_w2_comparison"]["all_three_gauge_couplings_tier1"])

        verdict = referee_phase6.run_all_referee_checks(PROJECT_ROOT, write_verdict=True)
        self.assertTrue(verdict["all_referee_checks_passed"])
        self.assertTrue(verdict["ast_guardrail_scan"]["passed"])
        self.assertEqual(verdict["phase6_new_controls"]["total"], 20)
        self.assertEqual(verdict["phase6_new_controls"]["caught"], 20)
        self.assertEqual(verdict["planted_fault_controls"]["total"], 65)
        self.assertEqual(verdict["planted_fault_controls"]["caught"], 65)


if __name__ == "__main__":
    unittest.main()
