"""Phase 7 Clean-Room Composite Engine & Phases 1-7 Cryptographic Seal Verifier (Track A, `0 of 19`)."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Dict

from .p7_1_inflation_baryogenesis import run_gate_p7_1_inflation_baryogenesis
from .p7_2_schwinger_adams_cusp import run_gate_p7_2_schwinger_adams_cusp
from .p7_3_lepton_pin_minus import run_gate_p7_3_lepton_pin_minus
from .p7_4_nogo_and_bp_flux import run_gate_p7_4_nogo_and_bp_flux
from .track_b_phase7_scorecard import run_gate_p7_5_track_b_scorecard

PROJECT_ROOT = Path(__file__).resolve().parents[2]

PHASE_DIRS = (
    ("phase1", "self_consistent_loop_phi"),
    ("phase2", "cusped_3d_loop_phase2"),
    ("phase3", "relational_yukawa_phase3"),
    ("phase4", "unification_cap_lepton_phase4"),
    ("phase5", "m004_cl10_a4_phase5"),
    ("phase6", "weave_toe_phase6"),
    ("phase7", "inflation_lepton_phase7"),
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


def verify_all_phase7_seals(project_root: Path = PROJECT_ROOT) -> Dict[str, Any]:
    """Verify Phase 1-7 SEAL_SHA256.txt digests plus Phase 5's immutable Track-A v1 blind lock."""
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
        elif key in ("phase5", "phase6", "phase7"):
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


def run_phase7_engine(project_root: Path = PROJECT_ROOT, write_outputs: bool = True) -> Dict[str, Any]:
    seals = verify_all_phase7_seals(project_root)
    assert seals["all_seals_intact"], f"Seal integrity failure: {seals}"

    g3_raw = run_gate_p7_3_lepton_pin_minus()
    g1 = run_gate_p7_1_inflation_baryogenesis(g3_raw["same_bundle_overtones_M5"])
    g2 = run_gate_p7_2_schwinger_adams_cusp()
    g4 = run_gate_p7_4_nogo_and_bp_flux(g3_raw["_Y_weave"][3])
    g5 = run_gate_p7_5_track_b_scorecard(g1, g3_raw, g4)

    g3_public = {k: v for k, v in g3_raw.items() if not k.startswith("_")}
    all_passed = bool(
        seals["all_seals_intact"]
        and g1["gate_p7_1_passed"]
        and g2["gate_p7_2_passed"]
        and g3_public["gate_p7_3_passed"]
        and g4["gate_p7_4_passed"]
        and g5["gate_p7_5_passed"]
    )
    assert all_passed

    result = {
        "phase": "Phase 7 — 7D Radion Plateau Inflation, Kähler Baryogenesis, Adams Cusp/Schwinger Audit, Pin_- Lepton Closure, & No-Go Theorems",
        "track_a_empirical_inputs_used": "0 of 19",
        "track_b_free_inflation_baryo_yukawa_mixing_spin_parameters": 0,
        "preregistration_seals": seals,
        "gate_p7_1_inflation_baryogenesis": g1,
        "gate_p7_2_schwinger_adams_cusp": g2,
        "gate_p7_3_lepton_pin_minus": g3_public,
        "gate_p7_4_nogo_and_bp_flux": g4,
        "gate_p7_5_track_b_scorecard": g5,
        "all_phase7_gates_passed": all_passed,
    }
    if write_outputs:
        out_dir = project_root / "outputs"
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "phase7_results.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    return result


if __name__ == "__main__":
    res = run_phase7_engine(write_outputs=True)
    print("Phase 7 Engine PASSED! All gates:", res["all_phase7_gates_passed"])
