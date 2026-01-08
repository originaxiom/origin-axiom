#!/usr/bin/env python3
"""
Phase 3: measure_v1 – diagnostics of the baseline A0 distribution.

This script probes the Phase 3 baseline mechanism output and constructs a
summary of the A0 distribution, including:

  - basic statistics (min, max, mean, a few quantiles),
  - fractions below illustrative epsilon thresholds,
  - a simple histogram.

Primary data source (preferred):
  - phase3/outputs/tables/mech_baseline_scan.csv

Fallback data source (if the CSV is missing):
  - phase3/outputs/tables/mech_baseline_scan_diagnostics.json

At this rung all quantities are toy-model diagnostics only. They are not
binding corridor constraints and carry no physical interpretation.
"""

import csv
import json
from pathlib import Path
from typing import Any, Dict, List, Tuple

def resolve_paths() -> Dict[str, Path]:
    script_path = Path(__file__).resolve()
    # .../origin-axiom/phase3/src/phase3_mech/measure_v1.py
    repo_root = script_path.parents[3]
    phase3_root = repo_root / "phase3"
    table_dir = phase3_root / "outputs" / "tables"

    baseline_csv = table_dir / "mech_baseline_scan.csv"
    baseline_diag = table_dir / "mech_baseline_scan_diagnostics.json"
    json_stats = table_dir / "phase3_measure_v1_stats.json"
    csv_hist = table_dir / "phase3_measure_v1_hist.csv"

    return {
        "repo_root": repo_root,
        "phase3_root": phase3_root,
        "table_dir": table_dir,
        "baseline_csv": baseline_csv,
        "baseline_diag": baseline_diag,
        "json_stats": json_stats,
        "csv_hist": csv_hist,
    }

# ---------- helpers for numeric extraction ----------

def _flatten_numeric(obj: Any) -> List[float]:
    """Flatten nested lists/tuples/dicts into a list of numeric leaves."""
    out: List[float] = []
    if isinstance(obj, (int, float)):
        out.append(float(obj))
    elif isinstance(obj, (list, tuple)):
        for x in obj:
            out.extend(_flatten_numeric(x))
    elif isinstance(obj, dict):
        for v in obj.values():
            out.extend(_flatten_numeric(v))
    return out

def _collect_A0_from_json(obj: Any) -> List[float]:
    """
    Recursively collect numeric values from JSON where the key name looks
    A0-like (e.g. contains 'A0', 'A_0', or 'amplitude').
    """
    vals: List[float] = []

    def _walk(o: Any, key: str = ""):
        nonlocal vals
        if isinstance(o, dict):
            for k, v in o.items():
                _walk(v, k)
        elif isinstance(o, list):
            for v in o:
                _walk(v, key)
        else:
            # Leaf; decide whether to take it based on key
            k_lower = key.lower() if key is not None else ""
            if (
                "a0" in k_lower
                or "a_0" in k_lower
                or "amplitude" in k_lower
            ):
                try:
                    vals.append(float(o))
                except (TypeError, ValueError):
                    pass

    _walk(obj)
    return vals

def _quantile(sorted_vals: List[float], p: float) -> float:
    """Simple quantile estimator for 0 <= p <= 1."""
    if not sorted_vals:
        raise ValueError("Empty value list for quantile")
    n = len(sorted_vals)
    if p <= 0.0:
        return sorted_vals[0]
    if p >= 1.0:
        return sorted_vals[-1]
    idx = int(round(p * (n - 1)))
    return sorted_vals[idx]

# ---------- main data loading ----------

def load_A0_values(paths: Dict[str, Path]) -> Tuple[List[float], str]:
    """
    Load A0 values from either the baseline CSV (preferred) or the
    diagnostics JSON (fallback). Returns (A0_values, source_description).
    """
    baseline_csv = paths["baseline_csv"]
    baseline_diag = paths["baseline_diag"]

    # 1) Preferred: CSV with an A0-like column
    if baseline_csv.is_file():
        with baseline_csv.open("r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            header = reader.fieldnames or []

            # Candidate column names for A0
            candidates = [
                "A0",
                "A_0",
                "A0_baseline",
                "A0_mech",
                "amplitude_without_floor",
                "A0_raw",
            ]
            col = None
            for c in candidates:
                if c in header:
                    col = c
                    break

            if col is None:
                # As a last resort, pick the first column whose name contains "A0"
                for h in header:
                    if "A0" in (h or ""):
                        col = h
                        break

            if col is None:
                raise RuntimeError(
                    "Could not identify an A0-like column in "
                    f"{baseline_csv} (headers = {header})"
                )

            vals: List[float] = []
            for row in reader:
                raw = row.get(col, None)
                if raw is None or raw == "":
                    continue
                try:
                    vals.append(float(raw))
                except ValueError:
                    continue

        if not vals:
            raise RuntimeError(
                f"Found column '{col}' in {baseline_csv} but could not "
                "parse any numeric A0 values."
            )

        return vals, f"csv:{baseline_csv.name}[col={col}]"

    # 2) Fallback: diagnostics JSON
    if not baseline_diag.is_file():
        raise FileNotFoundError(
            "Neither baseline CSV nor diagnostics JSON found:\n"
            f"  CSV: {baseline_csv}\n"
            f"  JSON: {baseline_diag}"
        )

    with baseline_diag.open("r", encoding="utf-8") as f:
        diag = json.load(f)

    vals = _collect_A0_from_json(diag)
    if not vals:
        raise RuntimeError(
            "Could not find any A0-like entries in baseline diagnostics JSON. "
            f"Searched for keys containing 'A0', 'A_0', or 'amplitude' in\n"
            f"  {baseline_diag}"
        )

    return vals, f"json:{baseline_diag.name}[A0-like-keys]"

# ---------- main ----------

def main() -> None:
    paths = resolve_paths()
    table_dir = paths["table_dir"]
    table_dir.mkdir(parents=True, exist_ok=True)

    A0_vals, source_descr = load_A0_values(paths)
    A0_vals.sort()
    n = len(A0_vals)
    A0_min = A0_vals[0]
    A0_max = A0_vals[-1]
    A0_mean = sum(A0_vals) / n

    # Quantiles
    A0_p01 = _quantile(A0_vals, 0.01)
    A0_p25 = _quantile(A0_vals, 0.25)
    A0_p50 = _quantile(A0_vals, 0.50)
    A0_p75 = _quantile(A0_vals, 0.75)

    # Epsilon thresholds
    eps_list = [0.005, 0.01, 0.02, 0.05]
    eps_info: Dict[str, Dict[str, float]] = {}
    for eps in eps_list:
        # Because A0_vals is sorted, we can stop once v >= eps
        count = 0
        for v in A0_vals:
            if v < eps:
                count += 1
            else:
                break
        frac = count / n
        key = f"{eps:.4g}"
        eps_info[key] = {
            "eps": eps,
            "fraction_below_eps": frac,
        }

    # Histogram over A0: [0, A0_max] uniform binning
    nbins = 40
    lo = 0.0
    hi = A0_max
    if hi <= lo:
        hi = lo + 1.0

    bin_edges: List[float] = [
        lo + (hi - lo) * i / nbins for i in range(nbins + 1)
    ]
    counts = [0] * nbins
    j = 0
    for v in A0_vals:
        while j < nbins - 1 and v >= bin_edges[j + 1]:
            j += 1
        counts[j] += 1

    # Build stats payload including eps_info for downstream scripts
    stats: Dict[str, Any] = {
        "description": (
            "Summary diagnostics for the Phase 3 baseline A0 distribution. "
            "All values are toy-model diagnostics and not binding corridor "
            "constraints."
        ),
        "source": source_descr,
        "n_samples": n,
        "A0_min": A0_min,
        "A0_max": A0_max,
        "A0_mean": A0_mean,
        "A0_p01": A0_p01,
        "A0_p25": A0_p25,
        "A0_p50": A0_p50,
        "A0_p75": A0_p75,
        "eps_info": eps_info,
        "histogram": {
            "bin_edges": bin_edges,
            "counts": counts,
        },
    }

    # Write stats JSON
    with paths["json_stats"].open("w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2, sort_keys=True)

    # Write histogram CSV
    with paths["csv_hist"].open("w", encoding="utf-8") as f:
        f.write("bin_left,bin_right,count\n")
        for i in range(len(counts)):
            f.write(
                "{0:.8g},{1:.8g},{2:d}\n".format(
                    bin_edges[i], bin_edges[i + 1], counts[i]
                )
            )

    # Console summary
    print("[phase3_measure_v1] Repo root:", paths["repo_root"])
    print("[phase3_measure_v1] Phase 3 root:", paths["phase3_root"])
    print("[phase3_measure_v1] Data source:", source_descr)
    print("[phase3_measure_v1] Wrote stats JSON to", paths["json_stats"])
    print("[phase3_measure_v1] Wrote histogram CSV to", paths["csv_hist"])
    print(
        "[phase3_measure_v1] A0_min = {0:.6g}, A0_p01 = {1:.6g}".format(
            A0_min, A0_p01
        )
    )
    for key in sorted(eps_info.keys(), key=lambda k: float(k)):
        info = eps_info[key]
        print(
            f"  eps = {info['eps']:.4g} -> "
            f"fraction_below_eps = {info['fraction_below_eps']:.6f}"
        )

if __name__ == "__main__":
    main()
