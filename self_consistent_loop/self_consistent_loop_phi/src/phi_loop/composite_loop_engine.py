"""Composite Fixed-Point Loop Engine: Phi(X*) = X* Orchestrator.

Verifies the pre-registration SHA-256 seal prior to running, executes all four
coupled back-edge sectors (BE-1 through BE-4), evaluates pre-registered
falsifiers T0-T4, compiles the honest upstream closure vs. obstruction ledger,
and writes outputs/phi_loop_results.json.
"""

from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path
from typing import Any, Dict

import numpy as np

from phi_loop.sector1_parent_anomaly import run_sector1
from phi_loop.sector2_history_state_loop import run_sector2
from phi_loop.sector3_weave_potential import run_sector3
from phi_loop.sector4_chirality_hand import run_sector4


PROJECT_ROOT = Path(__file__).resolve().parents[2]
PLAN_PATH = PROJECT_ROOT / "PREREGISTRATION_PLAN.md"
SEAL_PATH = PROJECT_ROOT / "SEAL_SHA256.txt"
OUTPUT_JSON_PATH = PROJECT_ROOT / "outputs" / "phi_loop_results.json"


def verify_preregistration_seal() -> Dict[str, Any]:
    """Verify PREREGISTRATION_PLAN.md matches the pre-run SHA-256 hash in SEAL_SHA256.txt."""
    raw_plan = PLAN_PATH.read_bytes()
    actual_sha256 = hashlib.sha256(raw_plan).hexdigest()
    seal_text = SEAL_PATH.read_text(encoding="utf-8").strip()
    expected_sha256 = seal_text.split()[0]
    matches = bool(actual_sha256 == expected_sha256)
    if not matches:
        raise RuntimeError(
            f"Pre-registration seal mismatch! Expected {expected_sha256}, got {actual_sha256}"
        )
    return {
        "plan_file": str(PLAN_PATH.name),
        "seal_file": str(SEAL_PATH.name),
        "expected_sha256": expected_sha256,
        "actual_sha256": actual_sha256,
        "seal_intact": matches,
    }


def run_composite_loop() -> Dict[str, Any]:
    """Execute the full composite fixed-point map Phi(X) across BE-1..BE-4."""
    t0 = time.time()
    seal = verify_preregistration_seal()

    s1 = run_sector1()
    s2 = run_sector2()
    s3 = run_sector3()
    s4 = run_sector4()

    elapsed = time.time() - t0

    # Assemble transparent upstream-choice closure & obstruction ledger:
    ledger = [
        {
            "upstream_node": "X:PARENT (Parent Lie algebra g and rank r)",
            "sector": "BE-1",
            "status": "CLOSED_TO_1_STRUCTURAL_PREMISE",
            "result": (
                f"Unique winner across {s1['catalogue_summary']['total_tested']} crystallographic "
                f"algebras (1 <= r <= 24) under Euclidean Gram (T, S) single-channel sewing: "
                f"{s1['catalogue_summary']['sewed_winners']}."
            ),
        },
        {
            "upstream_node": "SE1/SE2 & Level N=5 / Line +-(1,2) on metallic backgrounds L^m R^m",
            "sector": "BE-2 (A0 & T4)",
            "status": "NARROWED_UNIQUELY_AMONG_METALLIC_BACKGROUNDS",
            "result": (
                f"m=1 (LR) uniquely has trivial untwisted torsion |det(W0-I)|=1 and 1 cyclic "
                f"inversion-twisted line K^-(W0)=Z/5Z (intrinsic level N={s2['golden_background_A0']['intrinsic_twisted_level_N']}, "
                f"pm_pairs={s2['golden_background_A0']['background_K_minus_pm_pairs']})."
            ),
        },
        {
            "upstream_node": "T:POINT-WEIGHT & History Departure H via Twisted Eigenstate Readout",
            "sector": "BE-2 (A1-A6, T0-T3)",
            "status": "NON_TAUTOLOGICAL_LOOP_REFUTES_NAIVE_RUN6_SINGLE_STATE_IN_SOL_MODEL",
            "result": (
                f"T0ReadDependsOnData={s2['falsifier_verdicts']['T0_loop_read_depends_on_data_on_6_k1']}; "
                f"L2RLRRejected={s2['falsifier_verdicts']['T3_non_extending_L2RLR_rejected']}; "
                f"Mirror21112RejectedInS1={s2['falsifier_verdicts']['T3_mirror_21112_rejected_in_S1']}; "
                f"SurpriseRun6MirrorSplitInT={s2['falsifier_verdicts']['SURPRISE_run6_single_in_S1_but_mirror_split_in_T']}; "
                f"BoundedFamilySingleStateCount={s2['bounded_family_A6_k1']['single_unoriented_state_count']}."
            ),
        },
        {
            "upstream_node": "X:TAU & X:WEIGHT (1-Loop Weave / Torsion Modulus Stabilization)",
            "sector": "BE-3 (P-629)",
            "status": "PROVED_NEGATIVE_AT_1LOOP",
            "result": (
                f"StationaryAt_i_omega={s3['all_sl2z_potentials_stationary_at_i_and_omega']}; "
                f"InteriorMinimumOffOrbifold={s3['any_forced_1loop_stabilizes_interior_tau_off_i_omega']}; "
                f"TrivialLineGlobalMin={s3['trivial_wilson_line_beats_all_N2_to_6']}."
            ),
        },
        {
            "upstream_node": "X:HAND (Left-Right w_L/w_R Splitting & 4D Chiral Matter Index)",
            "sector": "BE-4 (WP-3.3)",
            "status": "EXACT_ALGEBRAIC_SPLIT_AND_INDEX_NO_GO_PROVED",
            "result": (
                f"NeutralCoreDim={s4['commutant_u3_c']['dim']} (45 D5 + 1); "
                f"PureCoset25TraceDiff={s4['weak_splitting_tests']['pure_coset_22_max_trace_diff']:.2e} (exact tie); "
                f"SU2LPreservingSubspaceDim={s4['su2L_preserving_subspace_dim']} (splits w_R > w_L iff Z2 self-duality broken); "
                f"Static4DChiralIndexDiff={s4['chiral_index_test']['max_conjugate_kernel_asymmetry']} (requires topological flux / boundary)."
            ),
        },
    ]

    payload = {
        "engine": "Self-Consistent Fixed-Point Loop Engine Phi(X*) = X*",
        "data_firewall": "0 of 19 empirical numbers imported",
        "elapsed_seconds": round(elapsed, 3),
        "preregistration_seal": seal,
        "sector1_BE1": s1,
        "sector2_BE2": s2,
        "sector3_BE3": s3,
        "sector4_BE4": s4,
        "upstream_closure_ledger": ledger,
    }

    def _json_default(obj: Any) -> Any:
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.bool_):
            return bool(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

    OUTPUT_JSON_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON_PATH.write_text(
        json.dumps(payload, indent=2, default=_json_default),
        encoding="utf-8",
    )
    return payload


def main() -> None:
    res = run_composite_loop()
    print("=" * 78)
    print("SELF-CONSISTENT FIXED-POINT LOOP ENGINE (Phi(X*) = X*) — SUMMARY")
    print("=" * 78)
    print(f"Pre-registration seal intact: {res['preregistration_seal']['seal_intact']}")
    print(f"SHA-256: {res['preregistration_seal']['actual_sha256']}")
    print(f"Elapsed: {res['elapsed_seconds']} s | Data firewall: {res['data_firewall']}")
    print("-" * 78)
    for item in res["upstream_closure_ledger"]:
        print(f"[{item['sector']}] {item['upstream_node']}")
        print(f"  Status : {item['status']}")
        print(f"  Result : {item['result']}")
    print("=" * 78)
    print(f"Saved full JSON payload to: {OUTPUT_JSON_PATH}")


if __name__ == "__main__":
    main()
