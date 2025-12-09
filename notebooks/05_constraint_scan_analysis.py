"""
Analysis of the (epsilon, lambda) constraint scan for the 3D toy universe.

Reads data/processed/constraint_scan_eps_lambda.npz and:
- prints a table of hits and <|A|> by (lambda, epsilon),
- plots <|A|> vs epsilon,
- plots constraint_hits vs epsilon,
separately for lambda = 0 and lambda = 1.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def main():
    base = Path("data/processed")
    path = base / "constraint_scan_eps_lambda.npz"
    if not path.exists():
        raise FileNotFoundError(
            f"{path} not found. Run src/run_toy_universe_constraint_scan.py first."
        )

    npz = np.load(path, allow_pickle=True)
    lam_vals = npz["lam_vals"]
    eps_vals = npz["eps_vals"]
    hits = npz["hits"]
    A_mean = npz["A_mean"]
    A_final = npz["A_final"]
    E_mean = npz["E_mean"]
    E_std = npz["E_std"]
    meta = npz["meta"].item()

    lam_list = sorted(set(lam_vals))
    eps_list = sorted(set(eps_vals))

    print("Scan meta:")
    for k, v in meta.items():
        print(f"  {k}: {v}")

    print("\nResults by (lambda, epsilon):")
    for lam in lam_list:
        print(f"\n=== lambda = {lam:.2f} ===")
        for eps in eps_list:
            mask = (lam_vals == lam) & (eps_vals == eps)
            if not np.any(mask):
                continue
            i = np.where(mask)[0][0]
            print(
                f"  eps = {eps:.3f}: "
                f"hits = {hits[i]:4d}, "
                f"<|A|> = {A_mean[i]:.4e}, "
                f"final |A| = {A_final[i]:.4e}, "
                f"<E> = {E_mean[i]:.6e} ± {E_std[i]:.2e}"
            )

    base.mkdir(parents=True, exist_ok=True)

    # For plotting, we build arrays per lambda value
    for lam in lam_list:
        lam_mask = lam_vals == lam
        eps_for_lam = eps_vals[lam_mask]
        A_mean_for_lam = A_mean[lam_mask]
        hits_for_lam = hits[lam_mask]

        # Sort by epsilon
        order = np.argsort(eps_for_lam)
        eps_sorted = eps_for_lam[order]
        A_mean_sorted = A_mean_for_lam[order]
        hits_sorted = hits_for_lam[order]

        # Plot <|A|> vs epsilon
        plt.figure()
        plt.plot(eps_sorted, A_mean_sorted, marker="o")
        plt.xlabel(r"$\epsilon$")
        plt.ylabel(r"$\langle |A(t)| \rangle$")
        plt.title(f"Mean global amplitude vs epsilon (lambda = {lam:.2f})")
        plt.grid(True)
        plt.tight_layout()
        out_A = base / f"constraint_scan_Amean_vs_eps_lambda{lam:.2f}.png"
        plt.savefig(out_A)

        # Plot hits vs epsilon
        plt.figure()
        plt.plot(eps_sorted, hits_sorted, marker="o")
        plt.xlabel(r"$\epsilon$")
        plt.ylabel("constraint hits")
        plt.title(f"Constraint hits vs epsilon (lambda = {lam:.2f})")
        plt.grid(True)
        plt.tight_layout()
        out_H = base / f"constraint_scan_hits_vs_eps_lambda{lam:.2f}.png"
        plt.savefig(out_H)

        print(
            f"\nSaved plots for lambda = {lam:.2f}:"
            f"\n  {out_A}"
            f"\n  {out_H}"
        )


if __name__ == "__main__":
    main()
