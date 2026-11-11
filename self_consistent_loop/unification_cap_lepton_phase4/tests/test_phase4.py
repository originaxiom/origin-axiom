"""Unit test suite for Phase 4: 1-Loop Vacuum Selection, 4D dP_9 Cusp-Cap & Quark-Lepton PMNS Engine."""

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

from phase4_loop.calibration_gate import run_all_phase4_calibrations
from phase4_loop.gate2_dp9_cusp_cap import run_gate2_dp9_cusp_cap
from phase4_loop.gate3_quark_lepton_unification import (
    verify_e8_lepton_branching_and_charge_uniqueness,
)
from phase4_loop.phase4_core import (
    analyze_pi1_mod5_torsion_lines,
    classify_cohomology_and_z5_cocycles,
    extract_epstein_penner_data,
)
from phase4_loop.phase4_engine import verify_all_phase_seals
import referee_phase4


class TestPhase4Suite(unittest.TestCase):
    """Comprehensive verification tests for Phase 4 gates, seals, and zero-import referee."""

    def test_01_preregistration_seals_intact(self) -> None:
        seals = verify_all_phase_seals(PROJECT_ROOT)
        self.assertTrue(seals["all_seals_intact"])
        self.assertIn("phase4", seals["phases"])
        self.assertTrue(seals["phases"]["phase4"]["seal_intact"])

    def test_02_textbook_calibration_gate(self) -> None:
        cal = run_all_phase4_calibrations()
        self.assertTrue(cal["all_calibrations_passed"])
        self.assertLess(cal["quadrature_and_epstein_penner"]["max_deg5_monomial_err"], 1e-14)
        self.assertLess(cal["alexander_reidemeister_torsion"]["max_reidemeister_err"], 1e-13)
        self.assertTrue(cal["pmns_haar_scrambling"]["seesaw_haar_audit"]["passed"])
        self.assertTrue(cal["pmns_haar_scrambling"]["weinberg_haar_audit"]["passed"])

    def test_03_fox_wada_acyclicity_and_z25_torsion(self) -> None:
        # Test both standard Z/5 + Z manifold ([5,1,2,2]+LR) and Z/25 + Z manifold (`b++RLLLRRRL`):
        for spec in ("b++LLLLLRLLRRLR", "b++RLLLRRRL"):
            ep = extract_epstein_penner_data(spec)
            coh = classify_cohomology_and_z5_cocycles(ep)
            self.assertEqual(len(coh["cusp_unramified_torsion_lines"]), 1)
            self.assertEqual(len(coh["cusp_ramified_torsion_lines"]), 4)

            pi1_t = analyze_pi1_mod5_torsion_lines(spec)
            unram = [ln for ln in pi1_t["lines"] if ln["is_torsion_nontrivial"] and ln["is_cusp_unramified"]]
            ram = [ln for ln in pi1_t["lines"] if ln["is_torsion_nontrivial"] and not ln["is_cusp_unramified"]]
            self.assertEqual(len(unram), 1)
            self.assertEqual(len(ram), 4)
            self.assertLess(unram[0]["torsion_q1"], 1e-13)
            for ln in ram:
                self.assertTrue(ln["is_acyclic_q1"])
                self.assertLess(abs(ln["torsion_product_all_4_charges"] - 5.0), 1e-12)

    def test_04_gate2_dp9_cusp_cap_and_bianchi(self) -> None:
        g2 = run_gate2_dp9_cusp_cap()
        self.assertTrue(g2["gate2_passed"])
        self.assertEqual(g2["dp9_lattice_and_e8_mordell_weil"]["e8_norm_minus2_root_count"], 240)
        self.assertEqual(g2["bianchi_tadpole_and_3gen_threshold"]["symmetric_bianchi_k_vis"], 6)
        self.assertFalse(
            g2["peripheral_gluing_and_ramification_audit"]["bulk_integer_c2_alone_forbids_k_zero"]
        )
        self.assertTrue(
            g2["peripheral_gluing_and_ramification_audit"][
                "branched_cusp_fiber_or_3d_acyclicity_forces_k_nonzero"
            ]
        )

    def test_05_e8_lepton_branching_and_saved_ledgers(self) -> None:
        br = verify_e8_lepton_branching_and_charge_uniqueness()
        self.assertTrue(br["passed"])
        self.assertEqual(br["unique_simultaneous_q_Nc"], [0])
        self.assertEqual(br["down_and_charged_lepton_charge_sum_mod5"], 0)
        self.assertEqual(br["weinberg_quartic_charge_sum_mod5"], 0)

        res_path = PROJECT_ROOT / "outputs" / "phase4_results.json"
        self.assertTrue(res_path.exists())
        prod = json.loads(res_path.read_text(encoding="utf-8"))
        self.assertTrue(prod["all_phase4_gates_passed"])
        self.assertEqual(prod["empirical_inputs_used"], "0 of 19")
        self.assertTrue(prod["gate1_vacuum_selection"]["gate1_passed"])
        self.assertTrue(prod["gate2_dp9_cusp_cap"]["gate2_passed"])
        self.assertTrue(prod["gate3_quark_lepton_unification"]["gate3_passed"])

    def test_06_zero_import_referee_full_audit(self) -> None:
        verdict = referee_phase4.run_all_referee_checks(write_verdict=True)
        self.assertTrue(verdict["all_referee_checks_passed"])
        self.assertTrue(verdict["ast_guardrail_scan"]["passed"])
        self.assertGreaterEqual(verdict["ast_guardrail_scan"]["num_scanned_files"], 9)


if __name__ == "__main__":
    unittest.main()
