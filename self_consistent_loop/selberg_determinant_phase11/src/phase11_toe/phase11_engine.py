"""Phase 11 Clean-Room Composite Engine & Phases 1-11 Cryptographic Seal Verifier (Track A, `0 of 19`)."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Dict

import mpmath as mp

from .p11_1_h3_huygens_propagator_exactness import run_gate_p11_1_h3_huygens_propagator_exactness
from .p11_2_porti_adjoint_torsion import run_gate_p11_2_porti_adjoint_torsion
from .p11_3_one_loop_overtone_partition import run_gate_p11_3_one_loop_overtone_partition
from .p11_4_joint_consistency import run_gate_p11_4_joint_consistency
from .track_b_phase11_scorecard import run_gate_p11_5_track_b_scorecard

mp.mp.dps = 50
PROJECT_ROOT = Path(__file__).resolve().parents[2]

PHASE_DIRS = (
    ("phase1", "self_consistent_loop_phi"),
    ("phase2", "cusped_3d_loop_phase2"),
    ("phase3", "relational_yukawa_phase3"),
    ("phase4", "unification_cap_lepton_phase4"),
    ("phase5", "m004_cl10_a4_phase5"),
    ("phase6", "weave_toe_phase6"),
    ("phase7", "inflation_lepton_phase7"),
    ("phase8", "fourfold_majorana_phase8"),
    ("phase9", "zero_input_precision_phase9"),
    ("phase10", "precision_falsifiability_phase10"),
    ("phase11", "selberg_determinant_phase11"),
)


def _verify_single_seal(phase_dir: Path) -> Dict[str, Any]:
    seal_path = phase_dir / "SEAL_SHA256.txt"
    if not seal_path.exists():
        return {"directory": phase_dir.name, "present": False, "seal_intact": False}
    parts = seal_path.read_text(encoding="utf-8").strip().splitlines()[0].split()
    expected_sha, target_name = parts[0].strip(), parts[1].strip()
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


def verify_all_phase11_seals(project_root: Path = PROJECT_ROOT) -> Dict[str, Any]:
    """Verify Phase 1-11 SEAL_SHA256.txt digests plus Phase 5's immutable Track-A v1 blind lock."""
    mp.mp.dps = 50
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
        elif key in ("phase5", "phase6", "phase7", "phase8", "phase9", "phase10", "phase11"):
            all_intact = False

    p5_dir = parent / "m004_cl10_a4_phase5"
    v1_json = p5_dir / "outputs" / "preregistered_blind_predictions_v1.json"
    v1_lock = p5_dir / "outputs" / "preregistered_blind_lock_sha256.json"
    v1_intact = False
    v1_actual = ""
    v1_expected = ""
    if v1_json.exists() and v1_lock.exists():
        v1_expected = json.loads(v1_lock.read_text(encoding="utf-8"))["preregistered_manifest_sha256"]
        v1_actual = hashlib.sha256(v1_json.read_bytes()).hexdigest()
        v1_intact = bool(v1_actual == v1_expected)
    all_intact = bool(all_intact and v1_intact)

    return {
        "phases": records,
        "track_a_v1_predictions_sha256": {
            "expected": v1_expected,
            "actual": v1_actual,
            "v1_lock_intact": v1_intact,
        },
        "all_seals_intact": all_intact,
    }


def run_phase11_engine(project_root: Path = PROJECT_ROOT, write_outputs: bool = True) -> Dict[str, Any]:
    """Execute all five Phase-11 gates after cryptographic seal verification across Phases 1-11."""
    mp.mp.dps = 50
    seals = verify_all_phase11_seals(project_root)
    assert seals["all_seals_intact"], f"Seal integrity failure: {seals}"

    g1_raw = run_gate_p11_1_h3_huygens_propagator_exactness()
    g2_raw = run_gate_p11_2_porti_adjoint_torsion(g1_raw)
    g3_raw = run_gate_p11_3_one_loop_overtone_partition(g1_raw, g2_raw)
    g4 = run_gate_p11_4_joint_consistency(g1_raw, g3_raw)
    g5 = run_gate_p11_5_track_b_scorecard(g1_raw, g2_raw, g3_raw, g4)

    g1_pub = {k: v for k, v in g1_raw.items() if not k.startswith("_")}
    g2_pub = {k: v for k, v in g2_raw.items() if not k.startswith("_")}
    g3_pub = {k: v for k, v in g3_raw.items() if not k.startswith("_")}

    all_passed = bool(
        seals["all_seals_intact"]
        and g1_pub["gate_p11_1_passed"]
        and g2_pub["gate_p11_2_passed"]
        and g3_pub["gate_p11_3_passed"]
        and g4["gate_p11_4_passed"]
        and g5["gate_p11_5_passed"]
    )
    assert all_passed

    result = {
        "phase": "Phase 11 — Exact 1-Loop Hyperbolic H^3 Propagator Theorem, 60-Digit Porti Adjoint Torsion, & M^(5) Partition Shootout",
        "track_a_empirical_inputs_used": "0 of 19",
        "track_b_continuous_fitted_or_calibrated_parameters": 0,
        "preregistration_seals": seals,
        "gate_p11_1_h3_huygens_propagator_exactness": g1_pub,
        "gate_p11_2_porti_adjoint_torsion": g2_pub,
        "gate_p11_3_one_loop_overtone_partition": g3_pub,
        "gate_p11_4_joint_consistency": g4,
        "gate_p11_5_track_b_scorecard": g5,
        "all_phase11_gates_passed": all_passed,
    }
    if write_outputs:
        out_dir = project_root / "outputs"
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "phase11_results.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    return result


if __name__ == "__main__":
    res = run_phase11_engine(write_outputs=True)
    print("Phase 11 Engine PASSED! All gates:", res["all_phase11_gates_passed"])
