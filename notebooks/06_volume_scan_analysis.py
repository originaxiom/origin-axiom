#!/usr/bin/env python3
"""
06_volume_scan_analysis.py

Analyse the output of run_toy_universe_volume_scan.py.

- Loads all volume_scan_*.npz files from data/processed/
- Prints a table of (N, lambda, epsilon, delta_rho)
- Plots delta_rho vs N for each lambda
"""

from pathlib import Path
import json

import numpy as np
import matplotlib.pyplot as plt


def load_volume_scan_files():
    base = Path("data/processed")
    files = sorted(base.glob("volume_scan_N*_lam*_eps*.npz"))
    records = []

    for fpath in files:
        data = np.load(fpath, allow_pickle=True)
        meta = json.loads(str(data["meta_json"]))
        records.append({
            "path": fpath,
            "N": meta["N"],
            "lam": meta["lam"],
            "epsilon": meta["epsilon"],
            "rho_no_mean": meta["rho_no_mean"],
            "rho_with_mean": meta["rho_with_mean"],
            "delta_rho": meta["delta_rho"],
        })

    return records


def print_table(records):
    if not records:
        print("No volume_scan_*.npz files found in data/processed/")
        return

    print("Volume scan results (time-averaged energy density):")
    print(f"{'N':>4}  {'lambda':>7}  {'eps':>7}  {'rho_no':>12}  "
          f"{'rho_with':>12}  {'delta_rho':>12}")
    for r in sorted(records, key=lambda x: (x["lam"], x["N"])):
        print(
            f"{r['N']:4d}  "
            f"{r['lam']:7.2f}  "
            f"{r['epsilon']:7.3f}  "
            f"{r['rho_no_mean']:12.6e}  "
            f"{r['rho_with_mean']:12.6e}  "
            f"{r['delta_rho']:12.6e}"
        )
    print()


def plot_delta_rho_vs_N(records):
    if not records:
        return

    base = Path("data/processed")

    # Group by lambda
    lam_values = sorted({r["lam"] for r in records})

    for lam in lam_values:
        sub = [r for r in records if abs(r["lam"] - lam) < 1e-12]
        if not sub:
            continue

        Ns = np.array([r["N"] for r in sub])
        delta_rhos = np.array([r["delta_rho"] for r in sub])

        # Sort by N for plotting
        idx = np.argsort(Ns)
        Ns = Ns[idx]
        delta_rhos = delta_rhos[idx]

        plt.figure()
        plt.plot(Ns, delta_rhos, marker="o")
        plt.xlabel("Lattice size N")
        plt.ylabel(r"$\Delta \bar{\rho}_\epsilon$ (with - without)")
        plt.title(f"Volume scaling of non-cancelling shift (lambda = {lam:.2f})")
        plt.grid(True)
        out = base / f"volume_scan_delta_rho_vs_N_lambda{lam:.2f}.png"
        plt.tight_layout()
        plt.savefig(out)
        print(f"Saved plot: {out}")


def main():
    records = load_volume_scan_files()
    print_table(records)
    plot_delta_rho_vs_N(records)
    print("Analysis complete.")


if __name__ == "__main__":
    main()