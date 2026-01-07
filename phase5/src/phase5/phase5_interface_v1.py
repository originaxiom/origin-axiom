#!/usr/bin/env python3
"""
Phase 5 interface v1: connectivity diagnostics.

This script does NOT introduce new physics. It simply:
  - Reads phase5/config/phase5_inputs_v1.json
  - Resolves all listed paths relative to the repo root
  - Checks whether each file exists and, if so, records its size in bytes
  - Writes a summary JSON to phase5/outputs/tables/phase5_interface_v1_summary.json
"""

import json
import os
from pathlib import Path
from datetime import datetime


def get_paths():
    here = Path(__file__).resolve()
    # .../phase5/src/phase5/phase5_interface_v1.py
    repo_root = here.parents[3]
    phase5_root = repo_root / "phase5"
    config_path = phase5_root / "config" / "phase5_inputs_v1.json"
    out_dir = phase5_root / "outputs" / "tables"
    out_json = out_dir / "phase5_interface_v1_summary.json"
    return {
        "repo_root": repo_root,
        "phase5_root": phase5_root,
        "config_path": config_path,
        "out_dir": out_dir,
        "out_json": out_json,
    }


def load_interface_spec(config_path: Path):
    if not config_path.is_file():
        raise FileNotFoundError(
            f"Phase 5 interface config not found at {config_path}. "
            "Expected phase5/config/phase5_inputs_v1.json."
        )
    with config_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def check_path(repo_root: Path, rel_path: str):
    """
    Return a small diagnostics dict for a single relative path.
    If rel_path is empty or clearly not a path (e.g. notes), we return a stub.
    """
    if not rel_path or not isinstance(rel_path, str):
        return {
            "is_path": False,
            "exists": False,
            "abspath": None,
            "size_bytes": None,
        }

    abspath = (repo_root / rel_path).resolve()
    if abspath.is_file():
        size_bytes = abspath.stat().st_size
        exists = True
    else:
        size_bytes = None
        exists = False

    return {
        "is_path": True,
        "exists": exists,
        "abspath": str(abspath),
        "size_bytes": size_bytes,
    }


def build_summary(spec: dict, paths: dict):
    repo_root = paths["repo_root"]
    summary = {
        "interface_version": spec.get("version", None),
        "timestamp_utc": datetime.utcnow().isoformat() + "Z",
        "repo_root": str(repo_root),
        "diagnostics": {},
    }

    for section_name in ("phase3", "phase4", "external"):
        section = spec.get(section_name, {})
        section_diag = {}
        for key, value in section.items():
            # Treat non-string entries (e.g. notes) as non-path metadata
            if not isinstance(value, str) or key.lower() == "notes":
                section_diag[key] = {
                    "is_path": False,
                    "exists": False,
                    "abspath": None,
                    "size_bytes": None,
                    "raw_value": value,
                }
            else:
                section_diag[key] = check_path(repo_root, value)
                section_diag[key]["relpath"] = value
        summary["diagnostics"][section_name] = section_diag

    return summary


def main():
    paths = get_paths()
    repo_root = paths["repo_root"]

    print("[phase5_interface_v1] Repo root:", repo_root)
    print("[phase5_interface_v1] Phase 5 root:", paths["phase5_root"])
    print("[phase5_interface_v1] Config:", paths["config_path"])

    spec = load_interface_spec(paths["config_path"])

    # Ensure output directory exists
    paths["out_dir"].mkdir(parents=True, exist_ok=True)

    summary = build_summary(spec, paths)

    with paths["out_json"].open("w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, sort_keys=True)

    print("[phase5_interface_v1] Wrote summary JSON to", paths["out_json"])

    # Simple console diagnostics
    for section_name, section_diag in summary["diagnostics"].items():
        print(f"[phase5_interface_v1] Section: {section_name}")
        for key, info in section_diag.items():
            if not info.get("is_path", False):
                print(f"  - {key}: (non-path entry)")
                continue
            status = "OK" if info.get("exists", False) else "MISSING"
            rel = info.get("relpath", "")
            size = info.get("size_bytes", None)
            if size is not None:
                print(f"  - {key}: {status}, {rel} ({size} bytes)")
            else:
                print(f"  - {key}: {status}, {rel}")

    print("[phase5_interface_v1] Done.")


if __name__ == "__main__":
    main()
