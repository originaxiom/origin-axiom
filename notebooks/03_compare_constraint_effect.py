import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def load_npz(path):
    npz = np.load(path, allow_pickle=True)
    return npz["times"], npz["A_mod"], npz["energies"], npz["params"].item()

def main():
    base = Path("data/processed")
    no_c_path = base / "toy_v0_1_no_constraint_epsilon005_meanzero.npz"
    with_c_path = base / "toy_v0_1_with_constraint_epsilon005_meanzero.npz"

    if not no_c_path.exists() or not with_c_path.exists():
        raise FileNotFoundError("Expected NPZ files not found. Run run_toy_universe_compare_constraint.py first.")

    t0, A0, E0, p0 = load_npz(no_c_path)
    t1, A1, E1, p1 = load_npz(with_c_path)

    print("No-constraint params:")
    for k, v in p0.items():
        print(f"  {k}: {v}")
    print("\nWith-constraint params:")
    for k, v in p1.items():
        print(f"  {k}: {v}")

    # |A(t)| comparison
    plt.figure()
    plt.plot(t0, A0, label="no constraint")
    plt.plot(t1, A1, label="with Origin Axiom constraint")
    plt.xlabel("t")
    plt.ylabel("|A(t)|")
    plt.title("Global amplitude vs time (Toy Universe v0.1, mean-subtracted, ε=0.05)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    out_A = base / "toy_v0_1_compare_Amod_epsilon005_meanzero.png"
    plt.savefig(out_A)

    # E(t) comparison
    plt.figure()
    plt.plot(t0, E0, label="no constraint")
    plt.plot(t1, E1, label="with Origin Axiom constraint")
    plt.xlabel("t")
    plt.ylabel("E(t)")
    plt.title("Energy vs time (Toy Universe v0.1, mean-subtracted, ε=0.05)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    out_E = base / "toy_v0_1_compare_energy_epsilon005_meanzero.png"
    plt.savefig(out_E)

    print("Saved comparison plots:")
    print(f"  {out_A}")
    print(f"  {out_E}")

if __name__ == "__main__":
    main()
