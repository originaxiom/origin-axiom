from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


def load_case(use_constraint: bool):
    """
    Load the most recent two-field run (with or without constraint).
    """
    base = Path("data/processed")
    pattern = (
        "two_field_compare_with_constraint_eps*.npz"
        if use_constraint
        else "two_field_compare_no_constraint_eps*.npz"
    )
    matches = sorted(base.glob(pattern))
    if not matches:
        raise FileNotFoundError(f"No files matching {pattern} in {base}")

    path = matches[-1]
    data = np.load(path, allow_pickle=True)

    print(f"Loaded: {path}")
    return data, path


def main() -> None:
    base = Path("data/processed")
    base.mkdir(parents=True, exist_ok=True)

    data_no, path_no = load_case(use_constraint=False)
    data_yes, path_yes = load_case(use_constraint=True)

    t0 = data_no["t"]
    t1 = data_yes["t"]

    A_psi_0 = data_no["A_psi"]
    A_psi_1 = data_yes["A_psi"]

    E0 = data_no["E"]
    E1 = data_yes["E"]

    eps = float(data_yes["epsilon"])
    lam_phi = float(data_yes["lam_phi"])
    lam_chi = float(data_yes["lam_chi"])
    g = float(data_yes["g"])

    hits_psi = int(data_yes["constraint_hits_psi"])

    # --- |A_psi(t)| comparison ---
    plt.figure()
    plt.plot(t0, np.abs(A_psi_0), label="no constraint")
    plt.plot(t1, np.abs(A_psi_1), label="with Origin Axiom constraint")
    plt.axhline(eps, linestyle="--")
    plt.xlabel("t")
    plt.ylabel(r"$|A_\psi(t)|$")
    plt.title(
        rf"Two-field toy: $\lambda_\phi={lam_phi}$, "
        rf"$\lambda_\chi={lam_chi}$, $g={g}$, \epsilon={eps}"
    )
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    out_A = base / "two_field_compare_Apsi.png"
    plt.savefig(out_A)

    # --- Energy comparison ---
    plt.figure()
    plt.plot(t0, E0, label="no constraint")
    plt.plot(t1, E1, label="with Origin Axiom constraint")
    plt.xlabel("t")
    plt.ylabel("E(t)")
    plt.title("Two-field toy: total energy vs time")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    out_E = base / "two_field_compare_energy.png"
    plt.savefig(out_E)

    print("Saved figures:")
    print(f"  {out_A}")
    print(f"  {out_E}")
    print(f"Constraint hits on psi in constrained run: {hits_psi}")


if __name__ == "__main__":
    main()
