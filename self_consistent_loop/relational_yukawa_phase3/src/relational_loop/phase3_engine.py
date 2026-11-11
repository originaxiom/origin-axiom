"""Phase 3 Composite Engine: Relational Quotient, Spin-Flux Throat, 3D Hyperbolic Yukawa Overlaps & Tadpole Audit.

Executes:
  0. Pre-registration SHA-256 seal integrity check (PREREGISTRATION_PHASE3.md vs SEAL_SHA256.txt),
  1. Step 2 Textbook Calibration Gate (14-point degree-5 FEM, 10-tet 5-fold cover Z/5Z selection rule,
     discrete harmonic 1-form alpha_s = d theta_s, and Haar U(3)^3 CKM/Jarlskog gate),
  2. Gate 1: Relational Weak-Compass Quotient (enantiomer collapse, A-one uniqueness, A-all non-zero CP),
  3. Gate 2: Coupled Spin-Flux Throat & Klein-Four Palindrome Protection Audit,
  4. Gate 3: 3D Hyperbolic Yukawa Overlaps, Mass Ranks, CKM Selection Rules & Jarlskog CP Audit,
  5. Gate 4: Unrigged Topological Tadpole & E_8 Flux Quantization Audit,
and writes the full machine-readable output ledger to `outputs/phase3_results.json`.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Dict

from .calibration_gate import run_calibration_gate
from .gate1_relational_quotient import run_gate1
from .gate2_coupled_spin_flux_throat import run_gate2
from .gate3_3d_yukawa_overlap import run_gate3
from .gate4_topological_tadpole_audit import run_gate4


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def verify_phase3_seal(project_root: Path = PROJECT_ROOT) -> Dict[str, Any]:
    """Verify PREREGISTRATION_PHASE3.md SHA-256 matches SEAL_SHA256.txt."""
    prereg_path = project_root / "PREREGISTRATION_PHASE3.md"
    seal_path = project_root / "SEAL_SHA256.txt"
    actual_sha = hashlib.sha256(prereg_path.read_bytes()).hexdigest()
    sealed_line = seal_path.read_text(encoding="utf-8").strip().splitlines()[0]
    expected_sha = sealed_line.split()[0].strip()
    return {
        "preregistration_file": str(prereg_path.name),
        "expected_sha256": expected_sha,
        "actual_sha256": actual_sha,
        "seal_intact": (actual_sha == expected_sha),
    }


def run_phase3_engine(write_output: bool = True) -> Dict[str, Any]:
    """Run the complete Phase 3 pipeline and persist outputs/phase3_results.json."""
    seal = verify_phase3_seal(PROJECT_ROOT)
    if not seal["seal_intact"]:
        raise RuntimeError(
            f"SEAL VIOLATION: expected {seal['expected_sha256']}, got {seal['actual_sha256']}"
        )

    cal = run_calibration_gate()
    g1 = run_gate1()
    g2 = run_gate2(n_sub=4)
    g3 = run_gate3()
    g4 = run_gate4()

    all_passed = bool(
        seal["seal_intact"]
        and cal["all_calibrations_passed"]
        and g1["gate1_passed"]
        and g2["gate2_passed"]
        and g3["gate3_passed"]
        and g4["gate4_passed"]
    )

    payload = {
        "phase": "Phase 3: Relational Quotient, Spin-Flux Throat, 3D Hyperbolic Yukawa Overlaps & Topological Tadpole Engine",
        "empirical_inputs_used": "0 of 19",
        "all_phase3_gates_passed": all_passed,
        "seal_verification": seal,
        "calibration_gate": cal,
        "gate1_relational_quotient": g1,
        "gate2_coupled_spin_flux_throat": g2,
        "gate3_3d_yukawa_overlap": g3,
        "gate4_topological_tadpole_audit": g4,
    }

    if write_output:
        out_dir = PROJECT_ROOT / "outputs"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "phase3_results.json"
        out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    return payload


if __name__ == "__main__":
    res = run_phase3_engine(write_output=True)
    summary = {
        "all_phase3_gates_passed": res["all_phase3_gates_passed"],
        "seal_intact": res["seal_verification"]["seal_intact"],
        "calibration_passed": res["calibration_gate"]["all_calibrations_passed"],
        "gate1_passed": res["gate1_relational_quotient"]["gate1_passed"],
        "gate2_passed": res["gate2_coupled_spin_flux_throat"]["gate2_passed"],
        "gate3_passed": res["gate3_3d_yukawa_overlap"]["gate3_passed"],
        "gate4_passed": res["gate4_topological_tadpole_audit"]["gate4_passed"],
        "output_written": str(PROJECT_ROOT / "outputs" / "phase3_results.json"),
    }
    print(json.dumps(summary, indent=2))
    if not res["all_phase3_gates_passed"]:
        raise SystemExit(1)
