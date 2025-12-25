from __future__ import annotations
import argparse, math
from pathlib import Path
import numpy as np
import yaml
import matplotlib.pyplot as plt

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    cfg = yaml.safe_load(Path(args.config).read_text())
    seed = cfg["phase1"]["seed"]
    np.random.seed(seed)

    n_trials = cfg["phasor_toy"]["n_trials"]
    n_modes_list = cfg["phasor_toy"]["n_modes_list"]
    twist_angles = cfg["phasor_toy"]["twist_angles"]

    # Placeholder: generate a simple curve showing residual vs twist for a fixed N
    N = n_modes_list[-1]
    residuals = []
    for theta in twist_angles:
        # Two-source toy: 1 + e^{i theta}
        residuals.append(abs(1 + np.exp(1j * theta)))

    plt.figure()
    plt.plot(twist_angles, residuals, marker="o")
    plt.xlabel(r"Twist angle $\theta$ (rad)")
    plt.ylabel(r"$|1 + e^{i\theta}|$")
    plt.title("Two-source non-cancellation toy (Phase 1)")
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(args.out, bbox_inches="tight")

if __name__ == "__main__":
    main()
