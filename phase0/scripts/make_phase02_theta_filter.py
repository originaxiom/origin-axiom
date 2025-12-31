#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any, Dict, Tuple

TAU = 2.0 * math.pi


def load_json(p: Path) -> Dict[str, Any]:
    return json.loads(p.read_text(encoding="utf-8"))


def read_run_id(p: Path) -> str:
    return p.read_text(encoding="utf-8").strip()


def check_mode_sum_summary(summary: Dict[str, Any]) -> Tuple[bool, Dict[str, Any]]:
    # Mode-sum summary schema (phase2.modes.mode_model.to_summary_dict)
    applied = bool(summary["constraint"]["applied"])
    eps = float(summary["constraint"]["epsilon"])
    r_raw = float(summary["residual"]["raw"])
    r_con = float(summary["residual"]["constrained"])
    return True, {
        "constraint_applied": applied,
        "epsilon": eps,
        "residual_raw": r_raw,
        "residual_constrained": r_con,
        "delta": (r_con - r_raw),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase2-dir", type=Path, default=Path("../phase2"), help="Path to phase2/")
    ap.add_argument("--out", type=Path, default=Path("phase_outputs/phase_02_theta_filter.json"))
    args = ap.parse_args()

    p2 = args.phase2_dir.resolve()
    tests_dir = p2 / "outputs" / "tests"
    runs_dir = p2 / "outputs" / "runs"

    off_ptr = tests_dir / "binding_off.run_id.txt"
    on_ptr  = tests_dir / "binding_on.run_id.txt"

    if not off_ptr.exists() or not on_ptr.exists():
        raise SystemExit(
            "Missing binding regime pointers. Expected:\n"
            f"  {off_ptr}\n  {on_ptr}\n"
            "Run the Phase2 OFF/ON tests first (see instructions)."
        )

    run_off = read_run_id(off_ptr)
    run_on  = read_run_id(on_ptr)

    sum_off_path = runs_dir / run_off / "summary.json"
    sum_on_path  = runs_dir / run_on / "summary.json"

    if not sum_off_path.exists() or not sum_on_path.exists():
        raise SystemExit("Missing summary.json in one of the binding runs.")

    sum_off = load_json(sum_off_path)
    sum_on  = load_json(sum_on_path)

    _, off = check_mode_sum_summary(sum_off)
    _, on  = check_mode_sum_summary(sum_on)

    # Tests
    tol = 1e-12
    test_ok = {}

    # OFF: noninvasive
    test_ok["binding_off_noninvasive"] = (off["constraint_applied"] is False) and (abs(off["delta"]) <= tol)

    # ON: binds + enforces epsilon approximately
    test_ok["binding_on_applies"] = (on["constraint_applied"] is True)
    test_ok["binding_on_sets_floor"] = abs(on["residual_constrained"] - on["epsilon"]) <= 1e-9

    # Separation (ablation)
    test_ok["ablation_separates"] = (on["residual_constrained"] - on["residual_raw"]) > 0.0

    # If any test fails, we should NOT claim Phase 2 is lockable yet.
    all_ok = all(test_ok.values())

    out_obj: Dict[str, Any] = {
        "schema_version": "1.0",
        "phase": 2,
        "subphase": "binding_regime_certificate",
        "theta_domain": [0.0, TAU],

        # Phase 2 does not narrow theta by itself (no theta sweep in canonical Phase2 workflow)
        "theta_prior": {"type": "intervals", "intervals": [[0.0, TAU]]},
        "theta_pass": {"type": "intervals", "intervals": [[0.0, TAU]]},

        "tests": list(test_ok.keys()),
        "meta_tests": {
            "results": test_ok,
            "all_ok": all_ok,
            "off_run": off,
            "on_run": on,
            "note": "Phase 2 filter certifies that OA floor is noninvasive when inactive and binds when forced. "
                    "It does not (yet) narrow theta; that requires a theta sweep phase."
        },
        "provenance": {
            "phase2_dir": str(p2),
            "run_ids": {"binding_off": run_off, "binding_on": run_on},
        },
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(out_obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote: {args.out}")
    print("Phase2 tests:", test_ok)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())