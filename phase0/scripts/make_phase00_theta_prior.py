#!/usr/bin/env python3
"""
make_phase00_theta_prior.py

Reads origin-axiom/config/theta_star_config.json and emits:
  phase_outputs/phase_00_theta_filter.json

This encodes the θ* prior band as a formal ledger filter (Phase 00).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Dict

TAU = 2.0 * math.pi


def sha256_bytes(b: bytes) -> str:
    h = hashlib.sha256()
    h.update(b)
    return "sha256:" + h.hexdigest()


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--theta-config",
        type=Path,
        required=True,
        help="Path to origin-axiom/config/theta_star_config.json",
    )
    ap.add_argument(
        "--out",
        type=Path,
        default=Path("phase_outputs/phase_00_theta_filter.json"),
        help="Output path (default: phase_outputs/phase_00_theta_filter.json)",
    )
    args = ap.parse_args()

    raw = args.theta_config.read_bytes()
    cfg = json.loads(raw.decode("utf-8"))

    lo = float(cfg["theta_star_band_rad"]["lo"])
    hi = float(cfg["theta_star_band_rad"]["hi"])
    fid = float(cfg.get("theta_star_fid_rad", float("nan")))
    source = cfg.get("source", {})

    out_obj: Dict[str, Any] = {
        "schema_version": "1.0",
        "phase": 0,
        "subphase": "theta_star_prior_from_theta_star_repo",
        "theta_domain": [0.0, TAU],
        "theta_prior": {"type": "intervals", "intervals": [[0.0, TAU]]},
        "theta_pass": {"type": "intervals", "intervals": [[lo, hi]]},
        "tests": ["prior_band_from_theta_star_summary"],
        "meta_prior": {
            "theta_star_fid_rad": fid,
            "theta_star_band_rad": {"lo": lo, "hi": hi},
            "note": "Phase 00 encodes the external theta-star prior as a corridor filter; it is not a derived constant claim."
        },
        "provenance": {
            "config_path": str(args.theta_config),
            "config_hash": sha256_bytes(raw),
            "source": source
        }
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(out_obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote: {args.out}")
    print(f"θ band: [{lo}, {hi}]   (fiducial θ* = {fid})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())