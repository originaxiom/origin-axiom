"""Comprehensive Unit & Guardrail Verification Suite for Phi(X*) = X*."""

from __future__ import annotations

import ast
import json
import subprocess
import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RESULTS_JSON = PROJECT_ROOT / "outputs" / "phi_loop_results.json"
REFEREE_SCRIPT = PROJECT_ROOT / "scripts" / "referee_phi_loop.py"


class TestPhiLoopEngineAndGuardrails(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        if not RESULTS_JSON.exists():
            from phi_loop.composite_loop_engine import run_composite_loop

            cls.results = run_composite_loop()
        else:
            cls.results = json.loads(RESULTS_JSON.read_text(encoding="utf-8"))

    def test_01_preregistration_seal_intact(self) -> None:
        seal = self.results["preregistration_seal"]
        self.assertTrue(seal["seal_intact"])
        self.assertEqual(seal["actual_sha256"], seal["expected_sha256"])

    def test_02_data_free_0_of_19_firewall_scan(self) -> None:
        """Guardrail 1 & 0-of-19 firewall: ensure no measured constants or target tau* appear in src/."""
        banned_literals = ["6.0653", "137.035", "0.2312", "0.1179", "172.69", "91.1876", "246.22"]
        for py_file in (PROJECT_ROOT / "src" / "phi_loop").glob("*.py"):
            txt = py_file.read_text(encoding="utf-8")
            for lit in banned_literals:
                self.assertNotIn(lit, txt, f"Banned target/empirical literal {lit} found in {py_file.name}")

    def test_03_guardrail6_referee_zero_imports_and_pass(self) -> None:
        src = REFEREE_SCRIPT.read_text(encoding="utf-8")
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for al in node.names:
                    self.assertNotIn("phi_loop", al.name)
            elif isinstance(node, ast.ImportFrom) and node.module:
                self.assertNotIn("phi_loop", node.module)

        proc = subprocess.run(
            [sys.executable, str(REFEREE_SCRIPT)],
            cwd=str(PROJECT_ROOT),
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, msg=f"Referee failed:\n{proc.stdout}\n{proc.stderr}")

    def test_04_sector1_unique_e8_and_cartan_trap(self) -> None:
        s1 = self.results["sector1_BE1"]
        self.assertTrue(s1["H1_1_unique_E8_closure"])
        self.assertTrue(s1["H1_2_center_and_3branch_orbit"])
        self.assertEqual(s1["catalogue_summary"]["sewed_winners"], ["E_8"])
        traps = {t["algebra"]: t["det_gram"] for t in s1["catalogue_summary"]["cartan_det1_non_self_dual_traps"]}
        self.assertEqual(traps, {"G_2": 3, "F_4": 4})
        self.assertLess(s1["poisson_theta_sewing"]["E8"]["single_channel_S_err"], 1e-12)
        self.assertLess(s1["e8_center_and_weave"]["err_X_minus_h4_eq_zeta_Spin10"], 1e-12)

    def test_05_sector2_calibration_falsifiers_and_siblings(self) -> None:
        s2 = self.results["sector2_BE2"]
        self.assertTrue(s2["instrument_calibration"]["instrument_calibrated"])
        self.assertLess(s2["instrument_calibration"]["harmonic_oscillator_rel_err"], 1e-9)
        fv = s2["falsifier_verdicts"]
        self.assertTrue(fv["T0_loop_read_depends_on_data_on_6_k1"])
        self.assertTrue(fv["T3_non_extending_L2RLR_rejected"])
        self.assertTrue(fv["T3_mirror_21112_rejected_in_S1"])
        self.assertTrue(fv["SURPRISE_run6_single_in_S1_but_mirror_split_in_T"])
        self.assertTrue(fv["m1_uniquely_has_trivial_Kplus_and_cyclic_Kminus"])
        # Check exact geodesic & cosh law residuals < 1e-12:
        h6 = s2["history_catalog_A1_A4"]["(6)"]["k=1"]
        self.assertLess(h6["geodesic_equiv_err"], 1e-12)
        self.assertLess(h6["cosh_law_err"], 1e-12)
        self.assertEqual(h6["S1_A1"]["distinct_circle_peaks_count"], 1)
        self.assertEqual(h6["T_A1"]["distinct_circle_peaks_count"], 2)

    def test_06_sector3_modular_identities_and_1loop_verdict(self) -> None:
        s3 = self.results["sector3_BE3"]
        ids = s3["modular_and_jacobi_identities"]
        self.assertLess(ids["det2d_sl2z_err"], 1e-12)
        self.assertLess(ids["jacobi_2d_parity_product_err"], 1e-12)
        self.assertLess(ids["e3_6d_sl2z_err"], 1e-12)
        self.assertLess(ids["parity_6d_minus_15_16_err"], 1e-12)
        self.assertLess(ids["order5_torsion_modular_err"], 1e-12)
        self.assertTrue(s3["all_sl2z_potentials_stationary_at_i_and_omega"])
        self.assertFalse(s3["any_forced_1loop_stabilizes_interior_tau_off_i_omega"])
        self.assertTrue(s3["trivial_wilson_line_beats_all_N2_to_6"])

    def test_07_sector4_46d_commutant_haar_scrambling_and_chirality(self) -> None:
        s4 = self.results["sector4_BE4"]
        self.assertLess(s4["e8_jacobi_err"], 1e-12)
        self.assertEqual(s4["commutant_u3_c"]["dim"], 46)
        self.assertEqual(s4["commutant_u3_c"]["structured_subspace_dims"]["total_rank"], 46)
        self.assertLess(s4["commutant_u3_c"]["explicit_46_commutator_err"], 1e-12)
        self.assertEqual(s4["su2L_preserving_subspace_dim"], 11)
        ws = s4["weak_splitting_tests"]
        self.assertLess(ws["self_dual_omega16_lr_eigenvalue_diff"], 1e-12)
        self.assertLess(ws["pure_coset_22_max_trace_diff"], 1e-12)
        self.assertGreater(ws["pure_coset_22_min_wL_trace"], 0.1)
        self.assertLess(max(abs(x) for x in ws["normal_octR_wL_eigenvalues"]), 1e-12)
        self.assertGreater(min(ws["normal_octR_wR_eigenvalues"]), 0.1)
        # Guardrail 3 Haar scrambling:
        haar = s4["haar_basis_scrambling_guardrail3"]
        self.assertTrue(haar["passed"])
        self.assertLess(haar["haar_248_weak_mass_eigenvalue_err"], 1e-12)
        self.assertLess(haar["haar_64_independent_LR_dirac_err"], 1e-12)
        # Chiral index no-go:
        self.assertEqual(s4["chiral_index_test"]["max_conjugate_kernel_asymmetry"], 0)
        self.assertLess(s4["chiral_index_test"]["max_conjugate_singular_value_diff"], 1e-12)


if __name__ == "__main__":
    unittest.main()
