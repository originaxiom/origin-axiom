"""Unit and pytest verification suite for Phase 10 (`145 / 145` Controls)."""
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

from phase10_toe.p10_1_pati_salam_projection import run_gate_p10_1_pati_salam_projection
from phase10_toe.p10_2_m5_axion_baryon_closure import run_gate_p10_2_m5_axion_baryon_closure
from phase10_toe.p10_3_falsifiability_observables import run_gate_p10_3_falsifiability_observables
from phase10_toe.p10_4_joint_consistency import run_gate_p10_4_joint_consistency
from phase10_toe.phase10_engine import verify_all_phase10_seals
import referee_phase10


class TestPhase10Suite(unittest.TestCase):
    """Comprehensive verification tests for Phase 10 gates, seals, Track-A 0-of-19 firewall, and 145/145 referee."""

    def test_01_preregistration_seals_1_to_10_and_v1_lock(self) -> None:
        seals = verify_all_phase10_seals(PROJECT_ROOT)
        self.assertTrue(seals["all_seals_intact"])
        self.assertIn("phase10", seals["phases"])
        self.assertTrue(seals["phases"]["phase10"]["seal_intact"])
        self.assertTrue(seals["track_a_v1_predictions_sha256"]["v1_lock_intact"])

    def test_02_gates_p10_1_to_p10_4_track_a(self) -> None:
        g1 = run_gate_p10_1_pati_salam_projection()
        self.assertTrue(g1["gate_p10_1_passed"])
        self.assertLess(g1["v12_zero_input_fixed_point_track_a"]["haar_10trial_SU3x5_max_err"], 1e-11)

        g2 = run_gate_p10_2_m5_axion_baryon_closure(g1)
        self.assertTrue(g2["gate_p10_2_passed"])

        g3 = run_gate_p10_3_falsifiability_observables(g1, g2)
        self.assertTrue(g3["gate_p10_3_passed"])
        self.assertLess(g3["benchmarks"]["takagi_50d_abs_err"], 1e-45)
        self.assertLess(g3["benchmarks"]["haar_10trial_falsifiability_max_err"], 1e-11)

        g4 = run_gate_p10_4_joint_consistency(g1, g2)
        self.assertTrue(g4["gate_p10_4_passed"])
        self.assertTrue(g4["strict_scale_ordering_satisfied"])

    def test_03_saved_phase10_ledger_26_tier1_and_falsifiability(self) -> None:
        res_path = PROJECT_ROOT / "outputs" / "phase10_results.json"
        self.assertTrue(res_path.exists())
        prod = json.loads(res_path.read_text(encoding="utf-8"))
        self.assertTrue(prod["all_phase10_gates_passed"])
        self.assertEqual(prod["track_a_empirical_inputs_used"], "0 of 19")
        self.assertEqual(prod["track_b_continuous_fitted_or_calibrated_parameters"], 0)

        g5 = prod["gate_p10_5_track_b_scorecard"]
        self.assertEqual(g5["v12_sm24_tier_summary"]["Tier_1_Precision_Hit"], 18)
        self.assertEqual(g5["unified_36_observable_summary"]["total_tier1_precision_hits_of_36"], 26)
        self.assertEqual(g5["unified_36_observable_summary"]["total_passing_of_36"], 36)
        self.assertGreater(g5["experimental_falsifiability_ledger"]["tau_p_to_e_pi0_yr"], 2.4e34)

    def test_04_zero_import_referee_145_cumulative_controls(self) -> None:
        verdict = referee_phase10.run_all_referee_checks(PROJECT_ROOT, write_verdict=False)
        self.assertTrue(verdict["all_referee_checks_passed"])
        self.assertTrue(verdict["ast_guardrail_scan"]["passed"])
        self.assertEqual(verdict["phase10_new_controls"]["caught"], 20)
        self.assertEqual(verdict["planted_fault_controls"]["total"], 145)
        self.assertEqual(verdict["planted_fault_controls"]["caught"], 145)


if __name__ == "__main__":
    unittest.main()
