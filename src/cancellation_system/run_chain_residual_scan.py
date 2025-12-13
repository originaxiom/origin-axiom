"""
run_chain_residual_scan.py

Scan how well 1D integer-structured chains can cancel a complex sum
S = Σ e^{i θ_j} under a θ-agnostic phase rule

    θ_j = q_j * theta + noise_j,

with integer charges q_j ∈ [-max_charge, +max_charge] and optional global
constraint Σ q_j = 0.

For each (theta, N), we draw 'n_samples' independent chains and record:

  - mean |S|
  - rms |S|
  - mean (|S| / sqrt(N))
  - rms (|S| / sqrt(N))

NEW (Act II reproducibility fixes):
  - run-id based outputs (no clobber)
  - optional resume (skip completed (theta,N))
  - theta grid generator (theta-min/theta-max/n-theta)
  - run meta JSON written next to outputs
  - theta-scan plots (at maxN + min-over-N) saved per run

Default outputs (tracked summaries + figures):
  - CSV:  docs/results/cancellation_system/runs/<run_id>/chain_residual_scan.csv
  - PNGs: figures/cancellation_system/runs/<run_id>/*.png

Optional convenience copies (latest):
  - docs/results/cancellation_system/chain_residual_scan_latest.csv
  - figures/cancellation_system/chain_residual_scan.png
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import platform
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np

try:
    import matplotlib.pyplot as plt
    HAVE_MPL = True
except Exception:
    HAVE_MPL = False

from .model_1d_chain import ChainConfig, summarize_many


def _parse_int_list(s: str) -> List[int]:
    return [int(x.strip()) for x in s.split(",") if x.strip()]


def _parse_float_list(s: str) -> List[float]:
    out: List[float] = []
    for chunk in s.split(","):
        chunk = chunk.strip()
        if not chunk:
            continue
        out.append(float(chunk))
    return out


def _default_run_id() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def _git_head() -> Optional[str]:
    try:
        r = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            check=True,
        )
        return r.stdout.strip()
    except Exception:
        return None


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Scan 1D cancellation chains over N and theta.")

    p.add_argument("--Ns", type=str, default="8,16,32,64,128",
                   help="Comma-separated list of N values. Default: 8,16,32,64,128")

    # Theta specification (priority: --thetas > --theta-min/max/n-theta > --theta)
    p.add_argument("--theta", type=float, default=2.0,
                   help="Single theta value (if no list/grid provided). Default: 2.0")
    p.add_argument("--thetas", type=str, default=None,
                   help="Comma-separated list of theta values, e.g. '1.5,2.0,2.5'.")
    p.add_argument("--theta-min", type=float, default=None,
                   help="Grid min theta (inclusive). Used with --theta-max and --n-theta.")
    p.add_argument("--theta-max", type=float, default=None,
                   help="Grid max theta (inclusive). Used with --theta-min and --n-theta.")
    p.add_argument("--n-theta", type=int, default=None,
                   help="Number of theta points for linspace grid. Used with --theta-min/max.")

    p.add_argument("--max-charge", type=int, default=5, help="Max |q_j| allowed. Default: 5")
    p.add_argument("--noise-sigma", type=float, default=0.0,
                   help="Std dev of Gaussian phase noise. Default: 0.0")
    p.add_argument("--n-samples", type=int, default=500,
                   help="Independent chains per (theta,N). Default: 500")
    p.add_argument("--seed", type=int, default=1234,
                   help="Base RNG seed. Default: 1234")
    p.add_argument("--no-zero-sum", action="store_true",
                   help="Disable sum(q_j)=0 constraint if set.")

    # Repro/output controls
    p.add_argument("--run-id", type=str, default=None,
                   help="Run identifier. Default: timestamp YYYYMMDD_HHMMSS")
    p.add_argument("--resume", action="store_true",
                   help="If set, resume from an existing CSV in the run folder (skip completed points).")
    p.add_argument("--force-resume", action="store_true",
                   help="Allow resume even if metadata differs (dangerous).")
    p.add_argument("--results-root", type=str, default="docs/results/cancellation_system/runs",
                   help="Root folder for run CSV outputs. Default: docs/results/cancellation_system/runs")
    p.add_argument("--figures-root", type=str, default="figures/cancellation_system/runs",
                   help="Root folder for run figure outputs. Default: figures/cancellation_system/runs")
    p.add_argument("--write-latest", action="store_true",
                   help="Also write convenience 'latest' copies (overwriting) outside run folder.")
    p.add_argument("--dry-run", action="store_true",
                   help="Print resolved theta list + outputs, then exit.")
    return p.parse_args()


def _resolve_thetas(args: argparse.Namespace) -> List[float]:
    if args.thetas is not None:
        return _parse_float_list(args.thetas)

    if (args.theta_min is not None) or (args.theta_max is not None) or (args.n_theta is not None):
        if args.theta_min is None or args.theta_max is None or args.n_theta is None:
            raise SystemExit("If using theta grid, you must provide --theta-min, --theta-max, and --n-theta.")
        return list(np.linspace(args.theta_min, args.theta_max, int(args.n_theta)))

    return [float(args.theta)]


def _theta_key(theta: float) -> str:
    return f"{theta:.15g}"


def _load_existing(csv_path: Path) -> Tuple[Optional[Dict[str, str]], set]:
    """
    Returns (meta_dict, completed_pairs_set) where completed_pairs_set contains (theta_key, N).
    meta_dict is extracted from first row for consistency checks.
    """
    if not csv_path.exists():
        return None, set()

    completed = set()
    meta = None
    with csv_path.open("r", newline="") as f:
        reader = csv.DictReader(f)
        for row_i, row in enumerate(reader):
            if row_i == 0:
                meta = {k: row.get(k, "") for k in [
                    "max_charge", "noise_sigma", "enforce_zero_sum", "n_samples", "seed", "run_id"
                ]}
            try:
                tk = _theta_key(float(row["theta"]))
                N = int(float(row["N"]))
                completed.add((tk, N))
            except Exception:
                continue
    return meta, completed


def _meta_matches(existing: Optional[Dict[str, str]], current: Dict[str, str]) -> bool:
    if existing is None:
        return True
    for k, v in current.items():
        if k not in existing:
            continue
        if str(existing[k]) != str(v):
            return False
    return True


def _write_meta_json(meta_path: Path, meta: Dict[str, object]) -> None:
    meta_path.write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n")


def main() -> None:
    args = parse_args()

    run_id = args.run_id or _default_run_id()
    Ns = _parse_int_list(args.Ns)
    thetas = _resolve_thetas(args)
    enforce_zero_sum = not args.no_zero_sum

    results_dir = Path(args.results_root) / run_id
    figures_dir = Path(args.figures_root) / run_id
    results_dir.mkdir(parents=True, exist_ok=True)
    figures_dir.mkdir(parents=True, exist_ok=True)

    out_csv = results_dir / "chain_residual_scan.csv"
    meta_json = results_dir / "run_meta.json"

    current_meta = {
        "run_id": run_id,
        "max_charge": str(args.max_charge),
        "noise_sigma": str(args.noise_sigma),
        "enforce_zero_sum": str(enforce_zero_sum),
        "n_samples": str(args.n_samples),
        "seed": str(args.seed),
    }

    if args.dry_run:
        print("=== DRY RUN ===")
        print("run_id:", run_id)
        print("Ns:", Ns)
        print("thetas:", f"{thetas[0]} ... {thetas[-1]} (n={len(thetas)})" if len(thetas) > 2 else thetas)
        print("CSV:", out_csv)
        print("FIG DIR:", figures_dir)
        return

    existing_meta, completed = (None, set())
    if args.resume:
        existing_meta, completed = _load_existing(out_csv)
        if not args.force_resume and not _meta_matches(existing_meta, current_meta):
            raise SystemExit(
                f"Refusing to resume: existing CSV metadata differs.\n"
                f"Existing: {existing_meta}\nCurrent:  {current_meta}\n"
                f"Use --force-resume to override (not recommended)."
            )

    print("=== 1D cancellation chain residual scan ===")
    print(f"run_id  : {run_id}")
    print(f"Ns      : {Ns}")
    print(f"thetas  : {thetas}")
    print(f"max_q   : {args.max_charge}")
    print(f"noise   : {args.noise_sigma}")
    print(f"n_samples per point: {args.n_samples}")
    print(f"seed (base): {args.seed}")
    print(f"enforce_zero_sum   : {enforce_zero_sum}")
    if args.resume:
        print(f"resume  : True (completed pairs loaded: {len(completed)})")
    print("----------------------------------------------------")

    rows: List[dict] = []

    # If resuming, start by loading existing rows so we can rewrite deterministically at end
    if args.resume and out_csv.exists():
        import pandas as pd  # local import to avoid hard dependency
        df0 = pd.read_csv(out_csv)
        rows = df0.to_dict(orient="records")

    # Streaming checkpoint CSV so interruptions preserve progress.
    # We still do a final deterministic rewrite (sorted) at the end.
    stream_fieldnames = [
        "run_id", "N", "theta", "max_charge", "noise_sigma", "enforce_zero_sum", "n_samples", "seed",
        "mean_S_abs", "rms_S_abs", "mean_S_abs_over_sqrtN", "rms_S_abs_over_sqrtN",
    ]

    # Ensure CSV exists with a header before we append.
    if (not out_csv.exists()) or out_csv.stat().st_size == 0:
        with out_csv.open("w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=stream_fieldnames)
            w.writeheader()

    stream_fh = out_csv.open("a", newline="")
    stream_writer = csv.DictWriter(stream_fh, fieldnames=stream_fieldnames)

    # Compute missing points
    new_count = 0
    try:
        for theta in thetas:
            print(f"\n--- theta = {theta:.6f} ---")
            for N in Ns:
                key = (_theta_key(theta), int(N))
                if args.resume and key in completed:
                    continue

                cfg = ChainConfig(
                    N=int(N),
                    theta=float(theta),
                    max_charge=int(args.max_charge),
                    noise_sigma=float(args.noise_sigma),
                    enforce_zero_sum=bool(enforce_zero_sum),
                    seed=int(args.seed),
                )

                stats = summarize_many(cfg, n_samples=int(args.n_samples))

                # Ensure stable keys exist (resume + sorting + streaming)
                stats["N"] = int(N)
                stats["theta"] = float(theta)
                stats["max_charge"] = int(args.max_charge)
                stats["noise_sigma"] = float(args.noise_sigma)
                stats["enforce_zero_sum"] = bool(enforce_zero_sum)
                stats["n_samples"] = int(args.n_samples)
                stats["run_id"] = run_id
                stats["seed"] = int(args.seed)

                rows.append(stats)
                new_count += 1

                # Checkpoint immediately so --resume works after interruptions.
                stream_writer.writerow({k: stats.get(k) for k in stream_fieldnames})
                stream_fh.flush()
                try:
                    os.fsync(stream_fh.fileno())
                except Exception:
                    pass
                completed.add((_theta_key(theta), int(N)))

                print(
                    f"N={int(N):4d}: "
                    f"mean|S|={stats['mean_S_abs']:.3f}, "
                    f"rms|S|={stats['rms_S_abs']:.3f}, "
                    f"mean|S|/sqrtN={stats['mean_S_abs_over_sqrtN']:.3f}"
                )
    finally:
        stream_fh.close()

    # Write meta JSON (always)
    meta = {
        "run_id": run_id,
        "timestamp_local": datetime.now().isoformat(timespec="seconds"),
        "git_head": _git_head(),
        "platform": {
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
            "python": platform.python_version(),
        },
        "argv": " ".join(__import__("sys").argv),
        "params": {
            "Ns": Ns,
            "thetas": thetas,
            "max_charge": args.max_charge,
            "noise_sigma": args.noise_sigma,
            "n_samples": args.n_samples,
            "seed": args.seed,
            "enforce_zero_sum": enforce_zero_sum,
            "resume": args.resume,
            "force_resume": args.force_resume,
        },
        "outputs": {
            "csv": str(out_csv),
            "figures_dir": str(figures_dir),
        },
        "rows_total": len(rows),
        "rows_new": new_count,
    }
    _write_meta_json(meta_json, meta)

    # Write CSV deterministically (sorted)
    if rows:
        rows_sorted = sorted(rows, key=lambda r: (float(r["theta"]), int(r["N"])))

        head = ["run_id", "N", "theta", "max_charge", "noise_sigma", "enforce_zero_sum", "n_samples", "seed",
                "mean_S_abs", "rms_S_abs", "mean_S_abs_over_sqrtN", "rms_S_abs_over_sqrtN"]
        all_keys = list(rows_sorted[0].keys())
        tail = [k for k in all_keys if k not in head]
        fieldnames = head + sorted(tail)

        tmp_csv = out_csv.with_suffix(".csv.tmp")
        with tmp_csv.open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows_sorted)
        tmp_csv.replace(out_csv)

        print(f"\nSaved scan summary to: {out_csv}")
        print(f"Saved run meta to:     {meta_json}")
    else:
        print("No rows produced; nothing to write.")
        return

    # Optional plots
    if not HAVE_MPL:
        print("matplotlib not available; skipping plots.")
    else:
        import pandas as pd
        df = pd.DataFrame(rows_sorted)

        # Plot 1: N-scaling per theta (legacy plot, per run)
        unique_thetas = list(dict.fromkeys([float(x) for x in df["theta"].tolist()]))
        plt.figure()
        for theta in unique_thetas:
            dft = df[df["theta"].astype(float) == float(theta)].sort_values("N")
            plt.plot(
                dft["N"].astype(int).tolist(),
                dft["mean_S_abs_over_sqrtN"].astype(float).tolist(),
                marker="o",
                label=f"theta={theta:g}",
            )
        plt.xscale("log")
        plt.xlabel("N (chain length)")
        plt.ylabel("mean |S| / sqrt(N)")
        plt.title("1D cancellation chain residuals (per θ)")
        plt.legend()
        plt.grid(True, which="both", linestyle="--", alpha=0.4)
        p1 = figures_dir / "chain_residual_scan.png"
        plt.tight_layout()
        plt.savefig(p1, dpi=150)
        plt.close()
        print(f"Saved figure to: {p1}")

        # Plot 2: theta scan at max N
        maxN = int(df["N"].astype(int).max())
        dfN = df[df["N"].astype(int) == maxN].sort_values("theta")
        if dfN.shape[0] >= 3:
            plt.figure()
            plt.plot(dfN["theta"].astype(float), dfN["mean_S_abs_over_sqrtN"].astype(float))
            plt.xlabel("theta")
            plt.ylabel(f"mean(|S|)/sqrt(N) at N={maxN}")
            plt.title(f"Chain residual θ scan (N={maxN})\n{run_id}")
            p2 = figures_dir / f"theta_scan_N{maxN}.png"
            plt.tight_layout()
            plt.savefig(p2, dpi=180)
            plt.close()
            print(f"Saved figure to: {p2}")

        # Plot 3: min over N of mean(|S|)/sqrt(N)
        piv = df.pivot_table(index="theta", columns="N", values="mean_S_abs_over_sqrtN", aggfunc="first")
        dmin = piv.min(axis=1).reset_index()
        if dmin.shape[0] >= 3:
            plt.figure()
            plt.plot(dmin["theta"].astype(float), dmin[0].astype(float))
            plt.xlabel("theta")
            plt.ylabel("min_N mean(|S|)/sqrt(N)")
            plt.title(f"Min over N of mean(|S|)/sqrt(N)\n{run_id}")
            p3 = figures_dir / "theta_scan_min_over_N.png"
            plt.tight_layout()
            plt.savefig(p3, dpi=180)
            plt.close()
            print(f"Saved figure to: {p3}")

    # Optional "latest" copies (overwrite on purpose, but outside run folder)
    if args.write_latest:
        latest_csv = Path("docs/results/cancellation_system/chain_residual_scan_latest.csv")
        latest_png = Path("figures/cancellation_system/chain_residual_scan.png")
        latest_csv.parent.mkdir(parents=True, exist_ok=True)
        latest_png.parent.mkdir(parents=True, exist_ok=True)

        latest_csv.write_text(out_csv.read_text())
        if HAVE_MPL:
            run_png = figures_dir / "chain_residual_scan.png"
            if run_png.exists():
                latest_png.write_bytes(run_png.read_bytes())

        print(f"Wrote latest CSV to: {latest_csv}")
        print(f"Wrote latest PNG to: {latest_png}")


if __name__ == "__main__":
    main()