"""Comprehensive Unit & Guardrail Verification Suite for Phase 3."""

from __future__ import annotations

import ast
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import unittest


PHASE3_ROOT = Path(__file__).resolve().parents[1]
SCRATCH_ROOT = PHASE3_ROOT.parent
PHASE1_ROOT = SCRATCH_ROOT / "self_consistent_loop_phi"
PHASE2_ROOT = SCRATCH_ROOT / "cusped_3d_loop_phase2"

if str(PHASE3_ROOT / "src") not in sys.path:
    sys.path.insert(0, str(PHASE3_ROOT / "src"))

from relational_loop.phase3_engine import verify_phase3_seal  # noqa: E402


class TestRelationalYukawaPhase3(unittest.TestCase):
    """End-to-end mathematical-physics & guardrail test suite for Phase 3."""

    @classmethod
    def setUpClass(cls) -> None:
        results_path = PHASE3_ROOT / "outputs" / "phase3_results.json"
        if not results_path.exists():
            raise RuntimeError("Run `PYTHONPATH=src python3 -m relational_loop.phase3_engine` before tests.")
        cls.results = json.loads(results_path.read_text(encoding="utf-8"))

    def test_01_all_three_phase_seals_intact(self) -> None:
        """Verify Phase 1, Phase 2, and Phase 3 SHA-256 seals are all intact."""
        s3 = verify_phase3_seal(PHASE3_ROOT)
        self.assertTrue(s3["seal_intact"])
        self.assertEqual(
            s3["actual_sha256"],
            "64039873eb88506cefb788a2ca0ba8a2e9578e0a45f91476aa7a94b1536cd48a",
        )

        p2_sha = hashlib.sha256((PHASE2_ROOT / "PREREGISTRATION_PHASE2.md").read_bytes()).hexdigest()
        p2_exp = (PHASE2_ROOT / "SEAL_SHA256.txt").read_text(encoding="utf-8").split()[0].strip()
        self.assertEqual(p2_sha, p2_exp)

        p1_sha = hashlib.sha256((PHASE1_ROOT / "PREREGISTRATION_PLAN.md").read_bytes()).hexdigest()
        p1_exp = (PHASE1_ROOT / "SEAL_SHA256.txt").read_text(encoding="utf-8").split()[0].strip()
        self.assertEqual(p1_sha, p1_exp)

    def test_02_ast_zero_import_referee_and_empirical_firewall(self) -> None:
        """Verify referee has 0 producer imports and src/ has 0 empirical PDG constants."""
        ref_path = PHASE3_ROOT / "scripts" / "referee_relational_phase3.py"
        tree = ast.parse(ref_path.read_text(encoding="utf-8"))
        forbidden = ("relational_loop", "cusped_loop", "phi_loop", "src")
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    self.assertFalse(alias.name.startswith(forbidden), f"Illegal import: {alias.name}")
            elif isinstance(node, ast.ImportFrom):
                mod = node.module or ""
                self.assertEqual(node.level, 0, "Relative import forbidden in referee")
                self.assertFalse(mod.startswith(forbidden), f"Illegal from-import: {mod}")

        banned_pdg = tuple(
            float(s)
            for s in ("125.25", "172.69", "91.1876", "80.377", "246.22", "0.23121", "0.1179", "0.22500", "3.08e-5")
        )
        for pyf in (PHASE3_ROOT / "src").rglob("*.py"):
            stree = ast.parse(pyf.read_text(encoding="utf-8"))
            for node in ast.walk(stree):
                if isinstance(node, ast.Constant) and isinstance(node.value, float):
                    for b in banned_pdg:
                        self.assertGreater(
                            abs(node.value - b),
                            1e-9,
                            f"Empirical constant {node.value} found in {pyf.name}",
                        )

    def test_03_textbook_calibration_gate(self) -> None:
        """Verify all Step 2 calibration benchmarks pass to < 1e-12."""
        cal = self.results["calibration_gate"]
        self.assertTrue(cal["all_calibrations_passed"])
        q14 = cal["quad14_and_m004_volume_calibration"]
        self.assertGreater(q14["min_quad14_weight"], 0.0)
        self.assertLess(q14["max_degree5_monomial_err"], 1e-15)
        self.assertLess(q14["b_pp_LR_penner_vol_err"], 1e-12)

        cov = cal["z5_trilinear_selection_and_cover_calibration"]
        self.assertLess(cov["max_forbidden_charge_triple_10tet_cover"], 1e-13)
        self.assertLess(cov["allowed_triple_10tet_cover_vs_5x_base_sv_err"], 1e-12)

        h1 = cal["discrete_harmonic_1form_calibration"]
        self.assertLess(h1["b_pp_LR_coclosure_err"], 1e-12)
        self.assertLess(h1["b_pp_LR_loop_holonomy_err"], 1e-12)

        haar = cal["haar_yukawa_jarlskog_calibration"]
        self.assertTrue(haar["cp_benchmark_haar"]["haar_invariance_verified"])
        self.assertLess(abs(haar["real_neg_ctrl_jarlskog"]), 1e-15)

    def test_04_gate1_relational_quotient_and_controls(self) -> None:
        """Verify Gate 1 collapses enantiomer pairs, yields 1 A-one winner, and zeros amphicheiral controls."""
        g1 = self.results["gate1_relational_quotient"]
        self.assertTrue(g1["gate1_passed"])
        ec = g1["enantiomer_relational_collapse"]
        self.assertLess(ec["max_tau_cusp_rel_diff"], 1e-12)
        self.assertLess(ec["max_tau_tube_rel_diff"], 1e-12)
        self.assertLess(ec["max_delta_m2_weak_rel_diff"], 1e-12)
        self.assertLess(ec["max_haar_u16_scrambling_err"], 1e-12)

        a1 = g1["a_one_quotient_selection"]
        self.assertEqual(a1["quotient_volume_winner_count"], 1)
        self.assertEqual(a1["quotient_throat_winner_count"], 1)

        a_all = g1["a_all_partition_aggregation"]
        self.assertLess(abs(a_all["unquotiented_boltz_tau_cusp"][0]), 1e-14)
        self.assertGreater(abs(a_all["relational_quotient_boltz_tau_cusp"][0]), 0.1)

        ctrl = g1["amphicheiral_negative_controls"]
        self.assertEqual(ctrl["b_pm_LR"]["sigma_P"], 0.0)
        self.assertEqual(ctrl["b_pm_LLLLLRRRRRLR_5_5"]["sigma_P"], 0.0)

    def test_05_gate2_coupled_spin_flux_palindrome_vs_irreversible(self) -> None:
        """Verify Klein-four palindrome protection on (6) and symmetry breaking on irreversible [5,1,2,2]."""
        g2 = self.results["gate2_coupled_spin_flux_throat"]
        self.assertTrue(g2["gate2_passed"])
        kp = g2["klein_four_palindrome_protection_on_run6"]
        self.assertLess(kp["palindrome_err_q2_cs_flux"], 1e-12)
        self.assertLess(kp["palindrome_err_q1_cs_flux"], 1e-12)
        self.assertLess(kp["palindrome_err_q2_irrational_flux"], 1e-12)
        self.assertLess(g2["max_haar_su2_spin_scrambling_err"], 1e-12)

        ir = g2["irreversible_chiral_pair_5_1_2_2"]
        self.assertFalse(ir["5_1_2_2_symmetry"]["is_time_reversible_3d"])
        self.assertGreater(ir["lowest_sector_single_peak_gap"], 1e-2)

    def test_06_gate3_3d_yukawa_hierarchy_and_jarlskog_cp(self) -> None:
        """Verify 3-tier Jarlskog CP theorem, (6) 2+1 CKM block zeros, and [5,1,2,2] CP breakthrough."""
        g3 = self.results["gate3_3d_yukawa_overlap"]
        self.assertTrue(g3["gate3_passed"])
        self.assertLess(g3["global_invariance_audits"]["max_haar_u3_scrambling_err"], 1e-12)
        self.assertLess(g3["global_invariance_audits"]["max_eigensolver_u1_phase_err"], 1e-12)

        thm = g3["hyperelliptic_and_palindromic_cp_theorem"]
        self.assertLess(thm["max_unramified_jarlskog_across_all_9_manifolds"], 1e-15)
        self.assertLess(thm["max_klein4_reversible_ramified_jarlskog"], 1e-15)
        self.assertEqual(thm["run6_n4_unramified_ranks"], [3, 3])
        self.assertEqual(thm["run6_n4_unramified_exact_zero_ckm_entries"], 4)

        cp = g3["irreversible_chiral_cp_breakthrough_5_1_2_2"]
        self.assertGreater(cp["max_abs_jarlskog_nsub4"], 1e-5)
        self.assertGreater(cp["max_abs_jarlskog_nsub5"], 1e-5)
        self.assertGreater(cp["ram0_nsub4_min_ckm_entry"], 1e-2)
        self.assertLess(cp["enantiomer_jarlskog_reversal_err_nsub5"], 1e-14)
        self.assertLess(cp["relational_jarlskog_collapse_err_nsub5"], 1e-14)

    def test_07_gate4_unrigged_tadpole_and_bianchi(self) -> None:
        """Verify triangular E_8 instanton thresholds k_min(N) = 1, 3, 6, 10 and Rules T1/T2/T3."""
        g4 = self.results["gate4_topological_tadpole_audit"]
        self.assertTrue(g4["gate4_passed"])
        th = g4["e8_instanton_quantization_theorem"]["minimal_instanton_thresholds_by_ngen"]
        self.assertEqual(th["1"]["minimal_k_inst"], 1)
        self.assertEqual(th["2"]["minimal_k_inst"], 3)
        self.assertEqual(th["3"]["minimal_k_inst"], 6)
        self.assertEqual(th["4"]["minimal_k_inst"], 10)

        self.assertFalse(g4["rule_t1_2d_fiber_audit"]["reaches_3_generations_unrigged"])
        self.assertFalse(g4["rule_t2_3d_dedekind_audit"]["run6_reaches_3_generations"])
        self.assertFalse(g4["rule_t2_3d_dedekind_audit"]["irrev_5_1_2_2_reaches_3_generations"])
        self.assertTrue(g4["rule_t3_4d_dp9_cusp_cap_audit"]["exact_match_to_3gen_threshold"])

    def test_08_zero_import_referee_subprocess(self) -> None:
        """Execute independent referee in a clean subprocess without PYTHONPATH and assert exit 0."""
        clean_env = {k: v for k, v in os.environ.items() if k != "PYTHONPATH"}
        proc = subprocess.run(
            [sys.executable, str(PHASE3_ROOT / "scripts" / "referee_relational_phase3.py")],
            cwd=str(PHASE3_ROOT),
            env=clean_env,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, msg=f"Referee failed:\n{proc.stdout}\n{proc.stderr}")
        verdict = json.loads(proc.stdout)
        self.assertTrue(verdict["all_referee_checks_passed"])


if __name__ == "__main__":
    unittest.main()
