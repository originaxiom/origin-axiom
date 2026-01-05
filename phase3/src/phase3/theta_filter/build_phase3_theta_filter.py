#!/usr/bin/env python3
"""
Build Phase 0 ledger-compatible theta-filter artifact for Phase 3.

We treat Phase 3 as an *empirical calibration step* for the optional "single θ links CKM+PMNS" hypothesis.
Accordingly, the filter is a declared, reproducible mapping from the fit outputs to an admissible θ corridor,
NOT a claim of first-principles derivation.
"""
from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Tuple

import pandas as pd
import hashlib


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_best_interval(summary_csv):
    """
    Return (theta_best_rad, theta_lo_rad, theta_hi_rad) from the Phase 3 fit summary.

    Supported schemas:
      - current: theta_best_rad, theta_68_lo_rad, theta_68_hi_rad
      - fallback: theta_best (assumed rad), theta_68_lo (rad), theta_68_hi (rad)
      - deg-only: theta_best_deg plus theta_68_*_deg (converted to rad) if ever used
    """
    import csv
    import math

    with open(summary_csv, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        row = next(reader, None)
        if row is None:
            raise ValueError(f"Empty CSV: {summary_csv}")

    keys = set(row.keys())

    def ffloat(k):
        v = row.get(k, None)
        if v is None:
            raise KeyError(f"Missing required column '{k}' in {summary_csv}. Found: {sorted(keys)}")
        try:
            return float(v)
        except Exception as e:
            raise ValueError(f"Could not parse float from column '{k}' value '{v}' in {summary_csv}") from e

    # Prefer rad schema (current)
    if {"theta_best_rad", "theta_68_lo_rad", "theta_68_hi_rad"}.issubset(keys):
        theta_best = ffloat("theta_best_rad")
        theta_lo   = ffloat("theta_68_lo_rad")
        theta_hi   = ffloat("theta_68_hi_rad")
        return theta_best, theta_lo, theta_hi

    # Fallback: older rad names
    if {"theta_best", "theta_68_lo_rad", "theta_68_hi_rad"}.issubset(keys):
        theta_best = ffloat("theta_best")
        theta_lo   = ffloat("theta_68_lo_rad")
        theta_hi   = ffloat("theta_68_hi_rad")
        return theta_best, theta_lo, theta_hi

    if {"theta_best", "theta_68_lo", "theta_68_hi"}.issubset(keys):
        theta_best = ffloat("theta_best")
        theta_lo   = ffloat("theta_68_lo")
        theta_hi   = ffloat("theta_68_hi")
        return theta_best, theta_lo, theta_hi

    # Last resort: deg schema (convert)
    if {"theta_best_deg", "theta_68_lo_deg", "theta_68_hi_deg"}.issubset(keys):
        theta_best = math.radians(ffloat("theta_best_deg"))
        theta_lo   = math.radians(ffloat("theta_68_lo_deg"))
        theta_hi   = math.radians(ffloat("theta_68_hi_deg"))
        return theta_best, theta_lo, theta_hi

    # Mixed schema fallback: best_deg + interval_rad (convert best only)
    if {"theta_best_deg", "theta_68_lo_rad", "theta_68_hi_rad"}.issubset(keys):
        theta_best = math.radians(ffloat("theta_best_deg"))
        theta_lo   = ffloat("theta_68_lo_rad")
        theta_hi   = ffloat("theta_68_hi_rad")
        return theta_best, theta_lo, theta_hi

    raise KeyError(
        f"Could not find a supported theta interval schema in {summary_csv}. "
        f"Found columns: {sorted(keys)}"
    )
def normalize_0_2pi(theta: float) -> float:
    t = theta % (2.0 * math.pi)
    if t < 0:
        t += 2.0 * math.pi
    return t


def interval_to_wrapaware(a: float, b: float) -> List[List[float]]:
    """
    Represent an interval on [0,2π) possibly wrapping across 0.
    Returns list of intervals [[a,b], ...] with 0<=a<=b<=2π.
    """
    a = normalize_0_2pi(a)
    b = normalize_0_2pi(b)

    if a <= b:
        return [[a, b]]
    # wrap-around
    return [[0.0, b], [a, 2.0 * math.pi]]


def build_theta_grid(step: float = 0.01) -> List[float]:
    n = int((2.0 * math.pi) / step) + 1
    return [i * step for i in range(n)]


def in_any_interval(t: float, intervals: List[List[float]]) -> bool:
    for a, b in intervals:
        if a <= t <= b:
            return True
    return False


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--in_summary_csv", required=True, type=Path)
    ap.add_argument("--in_summary_meta", required=False, type=Path)
    ap.add_argument("--in_targets_yaml", required=False, type=Path)
    ap.add_argument("--in_ansatz_py", required=False, type=Path)
    ap.add_argument("--out_json", required=True, type=Path)
    ap.add_argument("--grid_step", type=float, default=0.01)  # radians
    ap.add_argument("--test_name", type=str, default="fit_compat_interval")
    args = ap.parse_args()

    theta_best, theta_lo, theta_hi = load_best_interval(args.in_summary_csv)

    # Interval may cross 0; represent wrap-aware.
    theta_pass_intervals = interval_to_wrapaware(theta_lo, theta_hi)

    theta_grid = build_theta_grid(step=args.grid_step)
    pass_arr = [in_any_interval(t, theta_pass_intervals) for t in theta_grid]

    # provenance: prefer meta.json if present, else fallback
    prov: Dict[str, Any] = {}
    if args.in_summary_meta and args.in_summary_meta.exists():
        prov["summary_meta_sha256"] = sha256_file(args.in_summary_meta)
        try:
            meta = json.loads(args.in_summary_meta.read_text(encoding="utf-8"))
            # carry through common keys if present
            for k in ["git_commit", "config_hash", "environment", "run_id", "generated_utc"]:
                if k in meta:
                    prov[k] = meta[k]
        except Exception as e:
            prov["summary_meta_parse_error"] = str(e)

    if args.in_targets_yaml and args.in_targets_yaml.exists():
        prov["targets_yaml"] = str(args.in_targets_yaml)
        prov["targets_yaml_sha256"] = sha256_file(args.in_targets_yaml)

    if args.in_ansatz_py and args.in_ansatz_py.exists():
        prov["ansatz_file"] = str(args.in_ansatz_py)
        prov["ansatz_sha256"] = sha256_file(args.in_ansatz_py)

    out = {
        "schema_version": "1.0",
        "phase": 3,
        "subphase": "ckm_pmns_fit_calibration",
        "theta_domain": [0.0, 2.0 * math.pi],
        "theta_prior": {"type": "intervals", "intervals": [[0.0, 2.0 * math.pi]]},
        # Provide both: interval representation + a grid + pass array for determinism.
        "theta_pass": {"type": "intervals", "intervals": theta_pass_intervals},
        "theta_grid": theta_grid,
        "tests": [args.test_name],
        "pass": pass_arr,
        "fail_reasons": [[] if ok else [f"{args.test_name}=false"] for ok in pass_arr],
        "notes": (
            "Phase 3 emits a corridor based on a declared fit interval for the optional 'single θ links CKM+PMNS' hypothesis. "
            "This is an empirical calibration filter, not a first-principles derivation."
        ),
        "provenance": prov,
    }

    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(out, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
