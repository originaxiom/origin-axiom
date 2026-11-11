"""Unit Test & Guardrail Audit Suite — Phase 2 Cusped 3D Loop Engine."""

from __future__ import annotations

import json
import pathlib
import re
import subprocess
import sys
import unittest


ROOT_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR / "src"))

from cusped_loop.phase2_engine import verify_preregistration_seal  # noqa: E402


BANNED_EMPIRICAL_LITERALS = (
    "172.76",
    "125.25",
    "91.1876",
    "80.377",
    "246.22",
    "137.035999",
    "0.23121",
    "0.1179",
    "1.77686",
    "0.51099895",
)


class TestCuspedPhase2Suite(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        out_json = ROOT_DIR / "outputs" / "phase2_results.json"
        if not out_json.exists():
            subprocess.run(
                [sys.executable, "-m", "cusped_loop.phase2_engine"],
                cwd=str(ROOT_DIR),
                env={"PYTHONPATH": str(ROOT_DIR / "src")},
                check=True,
            )
        cls.results = json.loads(out_json.read_text())

    def test_01_preregistration_seal_intact(self) -> None:
        seal = verify_preregistration_seal(ROOT_DIR)
        self.assertTrue(seal["seal_intact"])
        self.assertEqual(
            seal["actual_sha256"],
            self.results["preregistration_seal"]["actual_sha256"],
        )

    def test_02_zero_of_nineteen_empirical_data_firewall(self) -> None:
        py_files = list((ROOT_DIR / "src").rglob("*.py")) + list(
            (ROOT_DIR / "scripts").rglob("*.py")
        )
        self.assertGreaterEqual(len(py_files), 6)
        for fp in py_files:
            txt = fp.read_text()
            for lit in BANNED_EMPIRICAL_LITERALS:
                self.assertIsNone(
                    re.search(re.escape(lit), txt),
                    f"Banned empirical constant {lit} found in {fp}",
                )

    def test_03_textbook_calibration_gate_precision(self) -> None:
        cal = self.results["calibration_gate"]
        self.assertTrue(cal["all_calibrations_passed"])
        hcal = cal["hyperbolic_m004_calibration"]
        self.assertLess(hcal["b_pp_LR_penner_vol_err"], 1e-12)
        self.assertLess(hcal["b_pm_LR_penner_vol_err"], 1e-12)
        self.assertLess(hcal["tet_bloch_wigner_err"], 1e-12)
        self.assertLess(hcal["max_intra_penner_err"], 1e-12)
        self.assertLess(hcal["max_inter_gluing_err"], 1e-12)

        fcal = cal["fem_cover_equivalence_calibration"]
        self.assertLess(fcal["untwisted_zero_mode_abs"], 1e-12)
        self.assertLess(fcal["base_vs_cover_max_eval_err"], 1e-12)

        dcal = cal["overlap_dirac_index_calibration"]
        self.assertLess(dcal["max_ginsparg_wilson_err"], 1e-12)
        self.assertLess(dcal["max_index_err"], 1e-12)
        self.assertLess(dcal["max_haar_scrambling_err"], 1e-12)

    def test_04_gate1_negative_control_and_enantiomer_invariance(self) -> None:
        g1 = self.results["gate1_3d_twisted_throat"]
        self.assertFalse(g1["negative_control_L2RLR"]["extends_golden_v5"])
        self.assertTrue(g1["negative_control_L2RLR"]["rejected_by_bundle_gate"])
        self.assertLess(g1["enantiomer_6_vs_1_6_E0_diff"], 1e-11)
        self.assertEqual(
            g1["bounded_family_A6_3d_summary"]["bundle_extending_count"], 18
        )

    def test_05_gate2_mostow_rigidity_and_enantiomer_pair(self) -> None:
        g2 = self.results["gate2_mostow_rigidity"]
        self.assertLess(
            abs(g2["golden_background"]["b++LR"]["parity_sin_4pi_cs"]), 1e-12
        )
        self.assertLess(
            abs(g2["golden_background"]["b+-LR"]["parity_sin_4pi_cs"]), 1e-12
        )
        a_one = g2["A_one_minimal_volume"]
        self.assertEqual(a_one["winner_count"], 2)
        self.assertTrue(a_one["winners_are_enantiomeric_pair"])
        self.assertLess(
            abs(g2["A_all_partition_aggregation"]["boltzmann_net_parity_sum"]), 1e-12
        )

    def test_06_gate3_topological_chirality_and_haar_guardrail(self) -> None:
        g3 = self.results["gate3_topological_chirality"]
        self.assertEqual(g3["negative_control_zero_flux_torus_index"], 0)

        so10 = g3["so10_su3c_smooth_flux_obstruction"]
        self.assertFalse(so10["fractional_00000111_is_e8_integral"])
        self.assertTrue(so10["minimal_00000222_is_e8_integral"])
        self.assertEqual(so10["overlap_index_lepton_16_1"], 3)
        self.assertEqual(so10["overlap_index_quark_16_3"], -1)
        self.assertFalse(so10["family_universal_16_possible_on_smooth_T2_without_holonomy"])

        su5 = g3["su5_gut_semisimple_trace_and_z5_projection"]
        self.assertEqual(su5["max_unprojected_5perp_index_sum"], 0)
        self.assertGreater(len(su5["minimal_z5_projected_3gen_coroots"]), 0)
        self.assertLess(su5["haar_multiflavor_scrambling_sval_err"], 1e-12)
        self.assertEqual(su5["haar_scrambled_4block_3gen_kernel_diff"], 12)

        aps = g3["aps_chiral_cusp_boundary_test"]
        self.assertEqual(aps["sealed_periodic_index"], 0)
        self.assertEqual(aps["chiral_aps_cusp_index"], 1)
        self.assertLess(aps["aps_haar_scrambling_err"], 1e-12)

        sp = g3["spatial_3d_parity_and_weak_handedness"]
        self.assertLess(sp["parity_even_riemannian_lr_action_diff_on_run6"], 1e-12)
        self.assertLess(abs(sp["cs_coupled_lr_split_on_amphicheiral_LR"]), 1e-12)
        self.assertLess(sp["enantiomer_cs_cancellation_err"], 1e-12)
        self.assertLess(sp["enantiomer_lr_split_reversal_err"], 1e-12)

    def test_07_zero_trust_referee_execution(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(ROOT_DIR / "scripts" / "referee_cusped_phase2.py")],
            cwd=str(ROOT_DIR),
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(
            proc.returncode,
            0,
            f"Referee failed:\nSTDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}",
        )
        verdict = json.loads(
            (ROOT_DIR / "outputs" / "referee_phase2_verdict.json").read_text()
        )
        self.assertTrue(verdict["all_checks_passed"])
        self.assertTrue(verdict["ast_zero_import_audit"]["zero_producer_imports_verified"])


if __name__ == "__main__":
    unittest.main()
