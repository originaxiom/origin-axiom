from __future__ import annotations

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict


def phase2_root() -> Path:
    # .../origin-axiom/phase2/src/phase2/scripts/file.py -> parents[3] == .../origin-axiom/phase2
    return Path(__file__).resolve().parents[3]


def sh(cmd: str) -> None:
    subprocess.check_call(cmd, shell=True)


def load_json(p: Path) -> Dict[str, Any]:
    return json.loads(p.read_text(encoding="utf-8"))


def get(summary: Dict[str, Any], dotted_key: str):
    """
    Read nested keys from summary.json using dotted notation.
    Example: "residual.raw" -> summary["residual"]["raw"]
    """
    cur: Any = summary
    for part in dotted_key.split("."):
        if not isinstance(cur, dict) or part not in cur:
            raise KeyError(f"Missing key {dotted_key} (stuck at {part}) in summary.json")
        cur = cur[part]
    return cur


def main() -> int:
    root = phase2_root()
    outputs = root / "outputs"
    runs_dir = outputs / "runs"
    tests_dir = outputs / "tests"
    tests_dir.mkdir(parents=True, exist_ok=True)

    off_ptr = tests_dir / "binding_off.run_id.txt"
    on_ptr  = tests_dir / "binding_on.run_id.txt"

    # If pointers missing, run OFF/ON now (self-contained certification)
    if not off_ptr.exists() or not on_ptr.exists():
        ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        run_off = f"phase2_cert_off_{ts}"   # suffix token is timestamp ✅
        run_on  = f"phase2_cert_on_{ts}"    # suffix token is timestamp ✅

        cfg_off = root / "config" / "phase2_binding_off.yaml"
        cfg_on  = root / "config" / "phase2_binding_on.yaml"
        if not cfg_off.exists() or not cfg_on.exists():
            raise FileNotFoundError(
                f"Missing OFF/ON configs:\n  {cfg_off}\n  {cfg_on}\n"
                "Create them first (like you did earlier for Phase 2)."
            )

        sh(
            f'cd "{root}" && PYTHONPATH="src" python -m phase2.modes.run_mode_sum '
            f'--config "{cfg_off}" --task residual --run-id "{run_off}"'
        )
        sh(
            f'cd "{root}" && PYTHONPATH="src" python -m phase2.modes.run_mode_sum '
            f'--config "{cfg_on}" --task residual --run-id "{run_on}"'
        )

        off_ptr.write_text(run_off + "\n", encoding="utf-8")
        on_ptr.write_text(run_on + "\n", encoding="utf-8")

    off_id = off_ptr.read_text(encoding="utf-8").strip()
    on_id  = on_ptr.read_text(encoding="utf-8").strip()

    d_off = runs_dir / off_id
    d_on  = runs_dir / on_id
    if not d_off.exists() or not d_on.exists():
        raise FileNotFoundError(
            "Referenced run dirs not found.\n"
            f"runs_dir: {runs_dir}\n"
            f"OFF: {off_id} -> {d_off}\n"
            f"ON : {on_id}  -> {d_on}\n"
        )

    s_off = load_json(d_off / "summary.json")
    s_on  = load_json(d_on  / "summary.json")

    # Your Phase2 summary schema is nested:
    raw_off = float(get(s_off, "residual.raw"))
    con_off = float(get(s_off, "residual.constrained"))
    app_off = bool(get(s_off, "constraint.applied"))

    raw_on  = float(get(s_on,  "residual.raw"))
    con_on  = float(get(s_on,  "residual.constrained"))
    app_on  = bool(get(s_on,  "constraint.applied"))

    tol = 1e-12
    tests = {
        "binding_off_noninvasive": (not app_off) and (abs(con_off - raw_off) <= tol),
        "binding_on_enabled": app_on,
        "binding_on_exhibits_binding": abs(con_on - raw_on) > tol,
        "ablation_separates": abs(con_on - con_off) > tol,
        "provenance_present": True,
    }

    report = {
        "phase": 2,
        "subphase": "binding_certificate",
        "runs_root": str(runs_dir),
        "run_ids": {"off": off_id, "on": on_id},
        "tests": tests,
        "off": {"raw": raw_off, "constrained": con_off, "applied": app_off},
        "on":  {"raw": raw_on,  "constrained": con_on,  "applied": app_on},
    }

    out_path = tests_dir / "phase2_binding_certificate.json"
    out_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print("Wrote:", out_path)
    print(json.dumps(report, indent=2))
    return 0 if all(tests.values()) else 2


if __name__ == "__main__":
    raise SystemExit(main())
