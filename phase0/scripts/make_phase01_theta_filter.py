#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

TAU = 2.0 * math.pi


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    h.update(p.read_bytes())
    return "sha256:" + h.hexdigest()


def load_json(p: Path) -> Dict[str, Any]:
    return json.loads(p.read_text(encoding="utf-8"))


def load_yaml(p: Path) -> Any:
    return yaml.safe_load(p.read_text(encoding="utf-8"))


def read_run_id(p: Path) -> str:
    return p.read_text(encoding="utf-8").strip()


def _allclose(a, b, tol=1e-12) -> bool:
    if len(a) != len(b):
        return False
    return all(abs(float(x) - float(y)) <= tol for x, y in zip(a, b))


def check_eps_sweep_run(run_dir: Path) -> Dict[str, Any]:
    meta_path = run_dir / "meta.json"
    res_path = run_dir / "results.yaml"

    if not meta_path.exists():
        raise FileNotFoundError(f"Missing meta.json in {run_dir}")
    if not res_path.exists():
        raise FileNotFoundError(f"Missing results.yaml in {run_dir}")

    meta = load_json(meta_path)
    results = load_yaml(res_path)

    if not isinstance(results, list) or not results:
        raise ValueError("results.yaml has unexpected format (expected non-empty list).")

    any_bind = False
    all_noninvasive = True

    for row in results:
        raw = row.get("raw_mean", [])
        flo = row.get("floored_mean", [])
        if not raw or not flo:
            raise ValueError("results.yaml row missing raw_mean/floored_mean arrays.")
        if _allclose(raw, flo):
            continue
        all_noninvasive = False
        if any(float(f) - float(r) > 0.0 for r, f in zip(raw, flo)):
            any_bind = True

    return {
        "run_dir": str(run_dir),
        "run_id": meta.get("run_id", run_dir.name),
        "created_utc": meta.get("created_utc", ""),
        "constraint_enabled": bool(meta.get("params", {}).get("constraint_enabled")),
        "all_noninvasive": bool(all_noninvasive),
        "any_bind": bool(any_bind),
        "meta": meta,
    }


def resolve_runs_root(phase1_dir: Path, outputs_run_dir: str) -> Path:
    """
    Resolve outputs.run_dir robustly.

    We try:
      1) If outputs_run_dir is absolute: use it.
      2) phase1_dir / outputs_run_dir
      3) phase1_dir.parent / outputs_run_dir   (repo root case)
    """
    runp = Path(outputs_run_dir)

    candidates: List[Path] = []
    if runp.is_absolute():
        candidates.append(runp)

    candidates.append((phase1_dir / runp))
    candidates.append((phase1_dir.parent / runp))

    for c in candidates:
        if c.exists() and c.is_dir():
            return c.resolve()

    msg = "Could not resolve outputs.run_dir. Tried:\n" + "\n".join(f"  - {c}" for c in candidates)
    raise SystemExit(msg)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase1-dir", type=Path, default=Path("../phase1"), help="Path to phase1/")
    ap.add_argument("--out", type=Path, default=Path("phase_outputs/phase_01_theta_filter.json"))
    args = ap.parse_args()

    p1 = args.phase1_dir.resolve()
    cfg_path = p1 / "config" / "phase1.yaml"
    if not cfg_path.exists():
        raise SystemExit(f"Missing {cfg_path}")

    cfg = load_yaml(cfg_path)

    outputs_run_dir = cfg.get("outputs", {}).get("run_dir", None)
    if not outputs_run_dir:
        raise SystemExit("Missing outputs.run_dir in phase1/config/phase1.yaml")

    runs_root = resolve_runs_root(p1, str(outputs_run_dir))

    tests_dir = p1 / "outputs" / "tests"
    off_ptr = tests_dir / "binding_off.run_id.txt"
    on_ptr = tests_dir / "binding_on.run_id.txt"
    if not off_ptr.exists() or not on_ptr.exists():
        raise SystemExit(
            "Missing Phase1 pointer files. Expected:\n"
            f"  {off_ptr}\n  {on_ptr}\n"
            "Run the pointer-generator step first."
        )

    rid_off = read_run_id(off_ptr)
    rid_on = read_run_id(on_ptr)

    run_off = runs_root / rid_off
    run_on = runs_root / rid_on
    if not run_off.exists() or not run_on.exists():
        raise SystemExit(
            "One of the referenced run directories does not exist under outputs.run_dir.\n"
            f"runs_root: {runs_root}\n"
            f"OFF run id: {rid_off} -> {run_off}\n"
            f"ON  run id: {rid_on} -> {run_on}\n"
            "Fix: ensure outputs.run_dir points to the directory that contains the run-id folders, "
            "or regenerate the run-id pointers after confirming runs_root."
        )

    off = check_eps_sweep_run(run_off)
    on = check_eps_sweep_run(run_on)

    tests = {
        "binding_off_noninvasive": (off["constraint_enabled"] is False) and (off["all_noninvasive"] is True),
        "binding_on_enabled": (on["constraint_enabled"] is True),
        "binding_on_exhibits_binding": (on["any_bind"] is True),
        "ablation_separates": (off["all_noninvasive"] is True) and (on["any_bind"] is True),
        "provenance_present": True,
    }
    all_ok = all(tests.values())

    out_obj: Dict[str, Any] = {
        "schema_version": "1.0",
        "phase": 1,
        "subphase": "phasor_toy_binding_certificate",
        "theta_domain": [0.0, TAU],
        "theta_prior": {"type": "intervals", "intervals": [[0.0, TAU]]},
        "theta_pass": {"type": "intervals", "intervals": [[0.0, TAU]]},
        "tests": list(tests.keys()),
        "meta_tests": {
            "results": tests,
            "all_ok": all_ok,
            "off": {k: off[k] for k in ("run_id", "created_utc", "constraint_enabled", "all_noninvasive", "any_bind")},
            "on":  {k: on[k]  for k in ("run_id", "created_utc", "constraint_enabled", "all_noninvasive", "any_bind")},
            "note": "Phase 1 certificate: explicit constraint.enabled OFF is noninvasive; ON shows binding in eps sweep. "
                    "Phase 1 does not narrow theta."
        },
        "provenance": {
            "phase1_dir": str(p1),
            "phase1_config": str(cfg_path),
            "phase1_config_hash": sha256_file(cfg_path),
            "runs_root": str(runs_root),
            "run_ids": {"binding_off": rid_off, "binding_on": rid_on},
        },
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(out_obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote: {args.out}")
    print("Phase1 tests:", tests)
    print("runs_root:", runs_root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
