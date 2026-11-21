"""Unit and pytest verification suite for Phase 7:
`7D` Radion Plateau Inflation, Kähler Baryogenesis, Adams Cusp/Schwinger Audit, `Pin_-` Lepton Closure, & No-Go Theorems (`85 / 85` Controls)."""
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

from phase7_toe.p7_1_inflation_baryogenesis import run_gate_p7_1_inflation_baryogenesis
from phase7_toe.p7_2_schwinger_adams_cusp import run_gate_p7_2_schwinger_adams_cusp
from phase7_toe.p7_3_lepton_pin_minus import run_gate_p7_3_lepton_pin_minus
from phase7_toe.p7_4_nogo_and_bp_flux import run_gate_p7_4_nogo_and_bp_flux
from phase7_toe.phase7_engine import verify_all_phase7_seals
import referee_phase7


class TestPhase7Suite(unittest.TestCase):
    """Comprehensive verification tests for Phase 7 gates, seals, Track-A 0-of-19 firewall, and 85/85 referee."""

    def test_01_preregistration_seals_1_to_7_and_v1_lock(self) -> None:
        seals = verify_all_phase7_seals(PROJECT_ROOT)
        self.assertTrue(seals["all_seals_intact"])
        self.assertIn("phase7", seals["phases"])
        self.assertTrue(seals["phases"]["phase7"]["seal_intact"])
        self.assertTrue(seals["track_a_v1_predictions_sha256"]["v1_lock_intact"])

    def test_02_gate_p7_2_schwinger_and_adams_cusp(self) -> None:
        g2 = run_gate_p7_2_schwinger_adams_cusp()
        self.assertTrue(g2["gate_p7_2_passed"])
        self.assertLess(g2["contino_pilo_schwinger_benchmark"]["schwinger_m1_quadrature_err_50d"], 1e-35)
        self.assertLess(g2["theorem_P7_2_adams_maximal_cusp"]["adams_volume_abs_err"], 1e-12)
        self.assertGreater(g2["clause_P7_C2_cubic_divergence_audit"]["alpha_GUT_inv_at_covering_2Lc"], 40.0)

    def test_03_gate_p7_3_reactor_solar_sum_rule_and_pin_minus(self) -> None:
        g3 = run_gate_p7_3_lepton_pin_minus()
        self.assertTrue(g3["gate_p7_3_passed"])
        p3a = g3["theorem_P7_3a_reactor_solar_sum_rule"]
        self.assertLess(abs(p3a["gY_zero_plant_w0_sq"] - p3a["gY_zero_plant_w1_sq"]), 1e-15)
        self.assertLess(g3["theorem_P7_3b_monomial_and_spin_parities"]["max_offdiag_norm_across_12_A4_elements"], 1e-15)
        self.assertEqual(g3["theorem_P7_3b_monomial_and_spin_parities"]["shell2_word_parities"], [-1, -1, -1, -1])

    def test_04_gate_p7_1_and_p7_4_inflation_baryo_and_nogo(self) -> None:
        g3 = run_gate_p7_3_lepton_pin_minus()
        g1 = run_gate_p7_1_inflation_baryogenesis(g3["same_bundle_overtones_M5"])
        self.assertTrue(g1["gate_p7_1_passed"])
        self.assertLess(g1["whitehead_kahler_affleck_dine_track_a"]["adiabatic_charge_drift_tau75_to_100"], 0.01)
        self.assertLess(g1["whitehead_kahler_affleck_dine_track_a"]["amphicheiral_zero_cp_plant_charge"], 1e-15)

        g4 = run_gate_p7_4_nogo_and_bp_flux(g3["_Y_weave"][3])
        self.assertTrue(g4["gate_p7_4_passed"])
        self.assertEqual(g4["exact_symbolic_Vbulk_over_MPl2_mrad2"], "5/42")
        self.assertEqual(g4["bousso_polchinski_flux_lattice_audit"]["J_4cycles_M5_x_dP9"], 21)

    def test_05_saved_phase7_ledger_and_v9_pin_weave_scorecard(self) -> None:
        res_path = PROJECT_ROOT / "outputs" / "phase7_results.json"
        self.assertTrue(res_path.exists())
        prod = json.loads(res_path.read_text(encoding="utf-8"))
        self.assertTrue(prod["all_phase7_gates_passed"])
        self.assertEqual(prod["track_a_empirical_inputs_used"], "0 of 19")
        self.assertEqual(prod["track_b_free_inflation_baryo_yukawa_mixing_spin_parameters"], 0)

        g5 = prod["gate_p7_5_track_b_scorecard"]
        self.assertEqual(g5["v9_pin_weave_tier_summary"]["Tier_1_Precision_Hit"], 12)
        self.assertEqual(g5["v9_pin_weave_tier_summary"]["Tier_2_Structural_O1_Hit"], 10)
        self.assertEqual(g5["v9_pin_weave_24_rows"]["abs_J_q"]["tier"], "Tier_2_Structural_O1_Hit")
        self.assertEqual(g5["v9_pin_weave_24_rows"]["delta_m21_sq_over_delta_m31_sq"]["tier"], "Tier_1_Precision_Hit")
        self.assertLess(g5["v9_pin_weave_calibration"]["haar_10trial_SU3x5_max_err"], 1e-11)

    def test_06_zero_import_referee_85_cumulative_controls(self) -> None:
        verdict = referee_phase7.run_all_referee_checks(PROJECT_ROOT, write_verdict=True)
        self.assertTrue(verdict["all_referee_checks_passed"])
        self.assertTrue(verdict["ast_guardrail_scan"]["passed"])
        self.assertEqual(verdict["phase7_new_controls"]["total"], 20)
        self.assertEqual(verdict["phase7_new_controls"]["caught"], 20)
        self.assertEqual(verdict["planted_fault_controls"]["total"], 85)
        self.assertEqual(verdict["planted_fault_controls"]["caught"], 85)


if __name__ == "__main__":
    unittest.main()
