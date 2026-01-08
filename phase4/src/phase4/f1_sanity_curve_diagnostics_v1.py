#!/usr/bin/env python3
import json
import os
from datetime import datetime

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # script_dir = .../phase4/src/phase4
    phase4_src = os.path.dirname(script_dir)          # .../phase4/src
    phase4_root = os.path.dirname(phase4_src)         # .../phase4
    repo_root = os.path.dirname(phase4_root)          # .../origin-axiom

    print("[F1_sanity_diag] Repo root:", repo_root)
    print("[F1_sanity_diag] Phase 4 root:", phase4_root)

    rel_csv = "phase4/outputs/tables/phase4_F1_sanity_curve.csv"
    rel_json = "phase4/outputs/tables/phase4_F1_sanity_curve_diagnostics.json"

    csv_path = os.path.join(repo_root, rel_csv)
    json_path = os.path.join(repo_root, rel_json)

    os.makedirs(os.path.dirname(json_path), exist_ok=True)

    csv_exists = os.path.exists(csv_path)
    csv_size = os.path.getsize(csv_path) if csv_exists else None

    diag = {
        "interface_version": 1,
        "mapping_family": "F1",
        "mapping_name": "F1_baseline_v1",
        "paths": {
            "curve_csv_rel": rel_csv,
            "curve_csv_abs": csv_path,
            "diagnostics_json_rel": rel_json,
            "diagnostics_json_abs": json_path,
        },
        "csv_status": {
            "exists": csv_exists,
            "size_bytes": csv_size,
        },
        "notes": (
            "Stub diagnostics for the F1 sanity curve. "
            "Content is intentionally minimal; the primary artifact "
            "is the CSV curve itself."
        ),
        "timestamp_utc": datetime.utcnow().isoformat() + "Z",
    }

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(diag, f, indent=2, sort_keys=True)

    print(f"[F1_sanity_diag] Wrote diagnostics JSON to {json_path}")
    if not csv_exists:
        print("[F1_sanity_diag] WARNING: CSV does not exist; run run_f1_sanity.py first.")

if __name__ == "__main__":
    main()
