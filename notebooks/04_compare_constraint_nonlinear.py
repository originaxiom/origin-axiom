"""
Compare |A(t)| and E(t) for the nonlinear (lambda != 0) 3D toy universe,
with and without the Origin Axiom constraint.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def load_run(filename: str):
    base = Path("data/processed")
    path = base / filename
    if not path.exists():
        raise FileNotFoundError(
            f"{path} not found. Run src/run_toy_universe_compare_constraint_nonlinear.py first."
        )
    npz = np.load(path, allow_pickle=True)
    t = npz["t"]
    A = npz["A"]
    E = npz["E"]
    params = npz["params"].item()
    return t, A, E, params


def main():
    t0, A0, E0, p0 = load_run("toy_v0_1_nonlinear_no_constraint_epsilon005_meanzero.npz")
    t1, A1, E1, p1 = load_run("toy_v0_1_nonlinear_with_constraint_epsilon005_meanzero.npz")

    print("No-constraint params:")
    for k, v in p0.items():
        print(f"  {k}: {v}")

    print("\nWith-constraint params:")
    for k, v in p1.items():
        print(f"  {k}: {v}")

    base = Path("data/processed")
    base.mkdir(parents=True, exist_ok=True)

    # |A(t)| comparison
    plt.figure()
    plt.plot(t0, np.abs(A0), label="no constraint")
    plt.plot(t1, np.abs(A1), label="with Origin Axiom constraint")
    plt.xlabel("t")
    plt.ylabel("|A(t)|")
    plt.title("Global amplitude vs time (nonlinear, ε=0.05)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    out_A = base / "toy_v0_1_nonlinear_compare_Amod_epsilon005_meanzero.png"
    plt.savefig(out_A)

    # E(t) comparison
    plt.figure()
    plt.plot(t0, E0, label="no constraint")
    plt.plot(t1, E1, label="with Origin Axiom constraint")
    plt.xlabel("t")
    plt.ylabel("E(t)")
    plt.title("Energy vs time (nonlinear, ε=0.05)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    out_E = base / "toy_v0_1_nonlinear_compare_energy_epsilon005_meanzero.png"
    plt.savefig(out_E)

    print("Saved nonlinear comparison plots:")
    print(f"  {out_A}")
    print(f"  {out_E}")


if __name__ == "__main__":
    main()
