import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def main():
    data_path = Path("data/processed/toy_v0_1_theta_pi_constraint.npz")
    if not data_path.exists():
        raise FileNotFoundError(f"Data file not found: {data_path}")

    npz = np.load(data_path, allow_pickle=True)
    times = npz["times"]
    A_mod = npz["A_mod"]
    energies = npz["energies"]
    params = npz["params"].item()

    print("Loaded data with params:")
    for k, v in params.items():
        print(f"  {k}: {v}")

    # Plot |A(t)|
    plt.figure()
    plt.plot(times, A_mod)
    plt.xlabel("t")
    plt.ylabel("|A(t)|")
    plt.title("Global amplitude magnitude vs time (with Origin Axiom constraint)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("data/processed/toy_v0_1_theta_pi_Amod.png")

    # Plot E(t)
    plt.figure()
    plt.plot(times, energies)
    plt.xlabel("t")
    plt.ylabel("E(t)")
    plt.title("Energy vs time (with Origin Axiom constraint)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("data/processed/toy_v0_1_theta_pi_energy.png")

    print("Saved plots to:")
    print("  data/processed/toy_v0_1_theta_pi_Amod.png")
    print("  data/processed/toy_v0_1_theta_pi_energy.png")

if __name__ == "__main__":
    main()
