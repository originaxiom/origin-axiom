"""Phase 4 Composite Engine: 1-Loop Vacuum Selection, 4D dP_9 Cusp-Cap Gluing & Quark-Lepton PMNS Unification.

Executes:
  0. Pre-registration SHA-256 seal integrity checks across Phases 1, 2, 3, and 4,
  1. Step 2 Textbook Calibration Gate (14-point degree-5 simplex quadrature on degree-3 Yukawa
     and degree-4 Weinberg monomials, Fox-Wada Alexander/Reidemeister torsion on m004 and m003,
     and 20-trial Haar U(3)^3 scrambling invariance of Seesaw & Weinberg PMNS observables),
  2. Gate 1: Unrestricted Necklace Census (|W| <= 12), 1-Loop Fox-Wada Reidemeister Acyclicity &
     Casimir/CW Buckling Audit (Test 1A), and Deduplicated Relational A-all Ensemble (Test 1B),
  3. Gate 2: 4D Rational Elliptic Surface (dP_9) Cusp-Cap Lattice I_{1,9}, Mordell-Weil E_8(-1),
     Symmetric Bianchi 3-Generation Threshold Match, and Peripheral Mod-5 Ramification Audit,
  4. Gate 3: E_8 -> su(5)_GUT x su(5)_perp Lepton Branching (Y_e = Y_d^T, q(N^c) = 0),
     3D Hyperbolic KK Seesaw & Weinberg Operator Overlaps, and Quark-vs.-Lepton Acid Test,
and writes the full machine-readable output ledger to `outputs/phase4_results.json`.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Dict

from .calibration_gate import run_all_phase4_calibrations
from .gate1_vacuum_selection import run_gate1_vacuum_selection
from .gate2_dp9_cusp_cap import run_gate2_dp9_cusp_cap
from .gate3_quark_lepton_unification import run_gate3_quark_lepton_unification


PROJECT_ROOT = Path(__file__).resolve().parents[2]

PHASE_DIRS = (
    ("phase1", "self_consistent_loop_phi"),
    ("phase2", "cusped_3d_loop_phase2"),
    ("phase3", "relational_yukawa_phase3"),
    ("phase4", "unification_cap_lepton_phase4"),
)


def _verify_single_seal(phase_dir: Path) -> Dict[str, Any]:
    """Verify SEAL_SHA256.txt against its target pre-registration markdown file in `phase_dir`."""
    seal_path = phase_dir / "SEAL_SHA256.txt"
    if not seal_path.exists():
        return {
            "directory": phase_dir.name,
            "present": False,
            "seal_intact": False,
        }
    first_line = seal_path.read_text(encoding="utf-8").strip().splitlines()[0]
    parts = first_line.split()
    expected_sha = parts[0].strip()
    target_name = parts[1].strip()
    target_path = phase_dir / Path(target_name).name
    actual_sha = hashlib.sha256(target_path.read_bytes()).hexdigest()
    return {
        "directory": phase_dir.name,
        "preregistration_file": target_path.name,
        "present": True,
        "expected_sha256": expected_sha,
        "actual_sha256": actual_sha,
        "seal_intact": bool(actual_sha == expected_sha),
    }


def verify_all_phase_seals(project_root: Path = PROJECT_ROOT) -> Dict[str, Any]:
    """Verify Phase 4 seal strictly and sibling Phase 1-3 seals if present in parent directory."""
    parent = project_root.parent
    records: Dict[str, Any] = {}
    all_intact = True
    for key, dirname in PHASE_DIRS:
        pdir = project_root if dirname == project_root.name else (parent / dirname)
        if pdir.exists():
            rec = _verify_single_seal(pdir)
            records[key] = rec
            if not rec["seal_intact"]:
                all_intact = False
        elif key == "phase4":
            rec = _verify_single_seal(project_root)
            records[key] = rec
            if not rec["seal_intact"]:
                all_intact = False
    if "phase4" not in records or not records["phase4"]["seal_intact"]:
        all_intact = False
    return {
        "phases": records,
        "all_seals_intact": all_intact,
    }


def build_nondimensional_ledger_and_verdicts(
    g1: Dict[str, Any], g2: Dict[str, Any], g3: Dict[str, Any]
) -> Dict[str, Any]:
    """Construct strict non-dimensionalized input ledger and unvarnished physics verdicts."""
    t1a = g1["test_1a_one_loop_buckling"]
    t1b = g1["test_1b_relational_a_all_ensemble"]
    gluing = g2["peripheral_gluing_and_ramification_audit"]
    bianchi = g2["bianchi_tadpole_and_3gen_threshold"]
    acid = g3["chiral_irreversible_acid_test_summary"]

    dep5122 = acid["departure_irreversible_5122"]
    dep_flags = dep5122["acid_test_flags_nsub4"]

    # Determine physics claim statuses directly from computed quantities (never hardcoded booleans):
    reidemeister_selects_k_nonzero = bool(t1a["k_nonzero_selected_over_k_zero_by_reidemeister_acyclicity"])
    one_loop_overturns_classical_vol = bool(
        t1a["unrestricted_comparison"]["one_loop_overturns_classical_volume_without_tuning"]
    )
    unbroken_4line_sum_cancels = bool(abs(t1b["unbroken_4line_sum_relational_jarlskog_sym"]) < 1e-14)
    spontaneous_branch_nonzero_cp = bool(t1b["spontaneous_branch_relational_jarlskog_sym_boltzmann"] > 0.0)
    bianchi_3gen_closed = bool(
        bianchi["triangular_formula_verified"] and bianchi["exact_3gen_threshold_match"]
    )
    bulk_c2_alone_forces_k_nonzero = bool(gluing["bulk_integer_c2_alone_forbids_k_zero"])
    branched_fiber_forces_k_nonzero = bool(gluing["branched_cusp_fiber_or_3d_acyclicity_forces_k_nonzero"])

    solar_reactor_enhanced_on_5122 = bool(
        dep_flags["weinberg_theta12_gt_ckm"]
        and dep_flags["weinberg_theta13_gt_ckm"]
        and dep_flags["kk_dirichlet_theta12_gt_ckm"]
    )
    atmospheric_enhanced_on_5122 = bool(
        dep_flags["weinberg_theta23_gt_ckm"] and dep_flags["kk_dirichlet_theta23_gt_ckm"]
    )

    return {
        "input_ledger": {
            "empirical_sm_inputs_used": 0,
            "total_sm_free_parameters": 19,
            "dimensionful_anchors_imported": 0,
            "all_reported_observables_dimensionless": True,
            "selection_bits_for_post_inspection_choices": "N/A (exhaustive census & all 4 torsion lines audited)",
        },
        "physics_hypothesis_verdicts": {
            "H1A_reidemeister_acyclicity_selects_cusp_ramified_k_nonzero": (
                "CLOSED" if reidemeister_selects_k_nonzero else "FALSIFIED"
            ),
            "H1A_unrigged_1loop_casimir_cw_overturns_classical_volume_for_A_one": (
                "CLOSED" if one_loop_overturns_classical_vol else "FALSIFIED"
            ),
            "H1B_unbroken_4line_sum_in_A_all_yields_net_jarlskog_without_branch_choice": (
                "FALSIFIED" if unbroken_4line_sum_cancels else "CLOSED"
            ),
            "H1B_spontaneous_hyperelliptic_branch_in_A_all_yields_nonzero_relational_cp": (
                "OPEN_SUPPRESSED" if spontaneous_branch_nonzero_cp else "FALSIFIED"
            ),
            "H2A_symmetric_dp9_bianchi_tadpole_matches_3gen_threshold_k6": (
                "CLOSED" if bianchi_3gen_closed else "FALSIFIED"
            ),
            "H2B_bulk_integer_c2_eq_6_alone_forbids_unramified_k0_on_smooth_boundary": (
                "CLOSED" if bulk_c2_alone_forces_k_nonzero else "FALSIFIED"
            ),
            "H2B_branched_cusp_fiber_or_3d_reidemeister_acyclicity_forces_k_nonzero": (
                "CLOSED" if branched_fiber_forces_k_nonzero else "FALSIFIED"
            ),
            "H3_lopsided_su5_transpose_enhances_solar_and_reactor_pmns_over_ckm_on_5122": (
                "CLOSED" if solar_reactor_enhanced_on_5122 else "FALSIFIED"
            ),
            "H3_scalar_throat_higgs_simultaneously_yields_large_atmospheric_theta23_gt_ckm": (
                "CLOSED" if atmospheric_enhanced_on_5122 else "FALSIFIED"
            ),
        },
    }


def run_phase4_engine(write_output: bool = True) -> Dict[str, Any]:
    """Run the complete Phase 4 pipeline and persist `outputs/phase4_results.json`."""
    seals = verify_all_phase_seals(PROJECT_ROOT)
    if not seals["all_seals_intact"]:
        raise RuntimeError(f"Pre-registration SHA-256 seal check failed: {seals}")

    cal = run_all_phase4_calibrations()
    g1 = run_gate1_vacuum_selection()
    g2 = run_gate2_dp9_cusp_cap()
    g3 = run_gate3_quark_lepton_unification()
    verdicts = build_nondimensional_ledger_and_verdicts(g1, g2, g3)

    all_passed = bool(
        seals["all_seals_intact"]
        and cal["all_calibrations_passed"]
        and g1["gate1_passed"]
        and g2["gate2_passed"]
        and g3["gate3_passed"]
    )

    payload = {
        "phase": "Phase 4: 1-Loop Vacuum Selection, 4D dP_9 Cusp-Cap Gluing & Quark-Lepton PMNS Unification Engine",
        "empirical_inputs_used": "0 of 19",
        "all_phase4_gates_passed": all_passed,
        "seal_verification": seals,
        "ledger_and_verdicts": verdicts,
        "calibration_gate": cal,
        "gate1_vacuum_selection": g1,
        "gate2_dp9_cusp_cap": g2,
        "gate3_quark_lepton_unification": g3,
    }

    if write_output:
        out_dir = PROJECT_ROOT / "outputs"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "phase4_results.json"
        out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    return payload


if __name__ == "__main__":
    result = run_phase4_engine(write_output=True)
    print("Phase 4 Engine all_phase4_gates_passed:", result["all_phase4_gates_passed"])
    print("Physics Hypothesis Verdicts:")
    for k, v in result["ledger_and_verdicts"]["physics_hypothesis_verdicts"].items():
        print(f"  {k}: {v}")
    if not result["all_phase4_gates_passed"]:
        sys.exit(1)
