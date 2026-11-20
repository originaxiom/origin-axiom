"""Unit and pytest verification suite for Phase 5:
`m004 x Cl(10) x A_4` Flavour, `Spin(11)` Hosotani/Collar, `7D` Radion, & `2`-Loop RGE Closure (`45 / 45` Controls)."""

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

from phase5_loop.clifford_hosotani_collar import run_gate_p5_2_clifford_hosotani_collar
from phase5_loop.geometry_and_selection import run_gate_p5_1_geometry
from phase5_loop.gravity_radion_and_warping import run_gate_p5_3_gravity_radion
from phase5_loop.rge_and_phase5_engine import (
    run_gate_p5_4_rge_benchmarks_and_clauses,
    verify_all_phase5_seals,
)
import referee_phase5


class TestPhase5Suite(unittest.TestCase):
    """Comprehensive verification tests for Phase 5 gates, seals, Track-A 0-of-19 firewall, and 45/45 referee."""

    def test_01_preregistration_seals_1_to_5_and_v1_lock(self) -> None:
        seals = verify_all_phase5_seals(PROJECT_ROOT)
        self.assertTrue(seals["all_seals_intact"])
        self.assertIn("phase5", seals["phases"])
        self.assertTrue(seals["phases"]["phase5"]["seal_intact"])
        self.assertTrue(seals["track_a_v1_predictions_sha256"]["v1_lock_intact"])

    def test_02_gate_p5_1_m004_and_m5_covering_geometry(self) -> None:
        g1 = run_gate_p5_1_geometry()
        self.assertTrue(g1["gate_p5_1_passed"])
        self.assertEqual(g1["m5_closed_geodesics_at_ell1"], 0)
        self.assertEqual(g1["m5_closed_systoles_at_ell2"], 4)
        self.assertLess(g1["z_apex_Ab"], 1.0)
        self.assertLess(g1["z_apex_AAb_fourth_minus_3_err"], 1e-48)
        self.assertEqual(g1["majorana_2torsion_offdiag_allowed"], 0)
        self.assertEqual(g1["majorana_2torsion_diag_allowed"], 3)

    def test_03_gate_p5_2_spin11_kawamura_ghu_and_uv_ir_duality(self) -> None:
        g1 = run_gate_p5_1_geometry()
        g2 = run_gate_p5_2_clifford_hosotani_collar(g1["eps_1"])
        self.assertTrue(g2["gate_p5_2_passed"])
        self.assertEqual(g2["kawamura_triplet_norm"], 0.0)
        self.assertEqual(g2["n_massless_gauge_bosons"], 9)
        self.assertAlmostEqual(g2["tree_sin2_thetaW"], 0.375, places=13)
        self.assertEqual(g2["gluon_H_vev_comm_norm"], 0.0)
        self.assertAlmostEqual(g2["su2_fhL_down"], 0.75, places=13)
        self.assertAlmostEqual(g2["su2_ff_down"], 0.0, places=13)
        self.assertLess(g2["uv_ir_mirror_duality_50d_err"], 1e-48)

    def test_04_gate_p5_3_7d_gravity_radion_and_warped_einstein(self) -> None:
        g1 = run_gate_p5_1_geometry()
        g3 = run_gate_p5_3_gravity_radion(g1["vol_m5_cover"])
        self.assertTrue(g3["gate_p5_3_passed"])
        self.assertEqual(g3["weyl_exponents"], [-3, -5, -6, -9, -10])
        self.assertLess(g3["pure_casimir_hilltop_d2V"], 0.0)
        self.assertGreater(g3["minkowski_nf1_d2V"], 0.0)
        self.assertTrue(g3["clause_N8_ads7_locks_yt_yb_to_hierarchy"])

    def test_05_gate_p5_4_rge_benchmarks_and_clauses_n6_n12(self) -> None:
        g1 = run_gate_p5_1_geometry()
        g4 = run_gate_p5_4_rge_benchmarks_and_clauses(g1["eps_1"])
        self.assertTrue(g4["gate_p5_4_passed"])
        self.assertLess(g4["pendleton_ross_err"], 1e-13)
        self.assertLess(g4["machacek_vaughn_2loop_err"], 1e-13)
        self.assertLess(g4["adklr_weinberg_err"], 1e-13)
        self.assertEqual(g4["spin11_dynkin_T_int"], [0.8, 6.0, 5.0])
        self.assertEqual(g4["spin11_dynkin_T_half"], [8.2, 3.0, 4.0])
        self.assertLess(g4["clause_N12_amphicheiral_det_commutator_50d"], 1e-48)

    def test_06_saved_phase5_ledger_and_zero_import_referee_45_controls(self) -> None:
        res_path = PROJECT_ROOT / "outputs" / "phase5_results.json"
        self.assertTrue(res_path.exists())
        prod = json.loads(res_path.read_text(encoding="utf-8"))
        self.assertTrue(prod["all_phase5_gates_passed"])
        self.assertEqual(prod["track_a_empirical_inputs_used"], "0 of 19")
        self.assertEqual(prod["track_b_free_yukawa_mixing_higgs_seesaw_parameters"], 0)

        sc = prod["gate_p5_5_track_b_v1_vs_v7_scorecard"]
        self.assertEqual(sc["v1_tier_summary"]["Tier_1_Precision_Hit"], 8)
        self.assertEqual(sc["v1_tier_summary"]["Tier_2_Structural_O1_Hit"], 8)
        self.assertEqual(sc["v7_tier_summary"]["Tier_1_Precision_Hit"], 12)
        self.assertEqual(sc["v7_tier_summary"]["Tier_2_Structural_O1_Hit"], 10)
        self.assertLess(sc["v7_haar_10trial_SU3x5_max_err"], 1e-11)

        verdict = referee_phase5.run_all_referee_checks(PROJECT_ROOT, write_verdict=True)
        self.assertTrue(verdict["all_referee_checks_passed"])
        self.assertTrue(verdict["ast_guardrail_scan"]["passed"])
        self.assertEqual(verdict["planted_fault_controls"]["total"], 45)
        self.assertEqual(verdict["planted_fault_controls"]["caught"], 45)


if __name__ == "__main__":
    unittest.main()
