#!/usr/bin/env python
"""
Rung F1.D1 – External FRW distance diagnostics.

This script inspects the external FRW distance–redshift dataset
defined at:

    phase4/data/external/frw_distance_binned.csv

and writes a small JSON diagnostics file at:

    phase4/outputs/tables/phase4_F1_frw_external_diagnostics.json

The goal is to provide a model-independent summary of the dataset
presence and basic properties (row count, redshift range, simple
checks), without introducing any cosmological modeling or likelihood.
"""

from __future__ import annotations

import csv
import json
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional


@dataclass
class ExternalFRWDiagnostics:
    repo_root: str
    phase4_root: str
    csv_relpath: str
    out_relpath: str

    file_exists: bool
    has_required_columns: Optional[bool] = None
    fieldnames: Optional[List[str]] = None

    n_rows: Optional[int] = None
    n_parsed_rows: Optional[int] = None
    parse_errors: int = 0

    z_min: Optional[float] = None
    z_max: Optional[float] = None
    mu_min: Optional[float] = None
    mu_max: Optional[float] = None
    sigma_mu_min: Optional[float] = None
    sigma_mu_max: Optional[float] = None

    monotonic_z_non_decreasing: Optional[bool] = None

    status: str = "unknown"
    notes: List[str] = field(default_factory=list)


def _get_roots() -> Dict[str, Path]:
    here = Path(__file__).resolve()
    # .../phase4/src/phase4/f1_frw_external_diagnostics_v1.py
    phase4_root = here.parents[2]  # .../phase4
    repo_root = here.parents[3]    # repo root
    return {"repo_root": repo_root, "phase4_root": phase4_root}


def compute_diagnostics(csv_path: Path, repo_root: Path, phase4_root: Path) -> ExternalFRWDiagnostics:
    rel_csv = csv_path.relative_to(repo_root)
    out_path = phase4_root / "outputs" / "tables" / "phase4_F1_frw_external_diagnostics.json"
    rel_out = out_path.relative_to(repo_root)

    diag = ExternalFRWDiagnostics(
        repo_root=str(repo_root),
        phase4_root=str(phase4_root),
        csv_relpath=str(rel_csv),
        out_relpath=str(rel_out),
        file_exists=csv_path.exists(),
    )

    if not csv_path.exists():
        diag.status = "missing_file"
        diag.notes.append("CSV file does not exist at expected path.")
        return diag

    # Prepare to read, skipping comment lines that start with '#'.
    def _non_comment_lines(path: Path):
        with path.open("r", encoding="utf-8") as f:
            for line in f:
                if line.lstrip().startswith("#"):
                    continue
                if not line.strip():
                    continue
                yield line

    try:
        reader = csv.DictReader(_non_comment_lines(csv_path))
    except Exception as exc:  # pragma: no cover
        diag.status = "read_error"
        diag.notes.append(f"Failed to construct DictReader: {exc!r}")
        return diag

    fieldnames = list(reader.fieldnames or [])
    diag.fieldnames = fieldnames

    required = ["z", "mu", "sigma_mu"]
    has_required = all(col in fieldnames for col in required)
    diag.has_required_columns = has_required

    if not has_required:
        diag.status = "schema_mismatch"
        diag.notes.append(
            "Required columns missing; expected at least "
            f"{required}, got {fieldnames!r}"
        )
        return diag

    zs: List[float] = []
    mus: List[float] = []
    sigmas: List[float] = []
    parse_errors = 0
    total_rows = 0

    for row in reader:
        total_rows += 1
        try:
            z_str = (row.get("z") or "").strip()
            mu_str = (row.get("mu") or "").strip()
            sigma_str = (row.get("sigma_mu") or "").strip()

            if not z_str and not mu_str and not sigma_str:
                # Skip fully empty logical rows.
                continue

            z_val = float(z_str)
            mu_val = float(mu_str)
            sigma_val = float(sigma_str)
        except Exception:
            parse_errors += 1
            continue

        zs.append(z_val)
        mus.append(mu_val)
        sigmas.append(sigma_val)

    diag.n_rows = total_rows
    diag.n_parsed_rows = len(zs)
    diag.parse_errors = parse_errors

    if len(zs) == 0:
        # Header-only or effectively empty dataset is valid at this rung.
        diag.status = "ok_zero_rows"
        diag.notes.append(
            "CSV has no successfully parsed data rows; "
            "this is valid at Rung F1.D1."
        )
        return diag

    # Basic ranges.
    diag.z_min = min(zs)
    diag.z_max = max(zs)
    diag.mu_min = min(mus)
    diag.mu_max = max(mus)
    diag.sigma_mu_min = min(sigmas)
    diag.sigma_mu_max = max(sigmas)

    # Check non-decreasing z.
    diag.monotonic_z_non_decreasing = all(
        z2 >= z1 for z1, z2 in zip(zs[:-1], zs[1:])
    )

    if not diag.monotonic_z_non_decreasing:
        diag.notes.append("z sequence is not non-decreasing.")

    if parse_errors > 0:
        diag.notes.append(f"Encountered {parse_errors} parse error(s).")

    diag.status = "ok"
    return diag


def main(argv: Optional[List[str]] = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    roots = _get_roots()
    repo_root: Path = roots["repo_root"]
    phase4_root: Path = roots["phase4_root"]

    csv_path = phase4_root / "data" / "external" / "frw_distance_binned.csv"
    out_path = phase4_root / "outputs" / "tables" / "phase4_F1_frw_external_diagnostics.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    diag = compute_diagnostics(csv_path=csv_path, repo_root=repo_root, phase4_root=phase4_root)

    with out_path.open("w", encoding="utf-8") as f:
        json.dump(asdict(diag), f, indent=2, sort_keys=True)

    print(f"[f1_frw_external_diagnostics_v1] Repo root: {repo_root}")
    print(f"[f1_frw_external_diagnostics_v1] CSV: {csv_path}")
    print(f"[f1_frw_external_diagnostics_v1] Output JSON: {out_path}")
    print(f"[f1_frw_external_diagnostics_v1] Status: {diag.status}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
