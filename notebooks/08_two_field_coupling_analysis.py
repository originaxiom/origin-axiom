from __future__ import annotations

from pathlib import Path
from typing import List, Tuple

import numpy as np
import matplotlib.pyplot as plt


DATA_DIR = Path("data/processed")


def load_group(label: str) -> List[Tuple[float, dict]]:
    """
    Load all files matching two_field_coupling_gXX_label.npz and
    return list of (g, data_dict) sorted by g.
    """
    files = sorted(DATA_DIR.glob(f"two_field_coupling_g*_{label}.npz"))
    out: List[Tuple[float, dict]] = []
    for f in files:
        data = dict(np.load(f, allow_pickle=True))
        g = float(data["g"])
        out.append((g, data))
    out.sort(key=lambda x: x[0])
    return out


def plot_Apsi(groups_no, groups_with) -> None:
    plt.figure()
    for g, data in groups_no:
        t = data["t"]
        Apsi = data["Apsi"]
        plt.plot(t, np.abs(Apsi), label=f"g={g:.2f} (no)")
    for g, data in groups_with:
        t = data["t"]
        Apsi = data["Apsi"]
        plt.plot(t, np.abs(Apsi), linestyle="--", label=f"g={g:.2f} (with)")
    plt.xlabel("t")
    plt.ylabel(r"$|A_\psi(t)|$")
    plt.title(r"Two-field coupling: $|A_\psi|$ vs time")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    out = DATA_DIR / "two_field_coupling_Apsi_vs_t.png"
    plt.savefig(out)
    print(f"Saved {out}")


def plot_energy(groups_no, groups_with) -> None:
    plt.figure()
    for g, data in groups_no:
        t = data["t"]
        E = data["E"]
        plt.plot(t, E, label=f"g={g:.2f} (no)")
    for g, data in groups_with:
        t = data["t"]
        E = data["E"]
        plt.plot(t, E, linestyle="--", label=f"g={g:.2f} (with)")
    plt.xlabel("t")
    plt.ylabel("E(t)")
    plt.title("Two-field coupling: energy vs time")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    out = DATA_DIR / "two_field_coupling_energy_vs_t.png"
    plt.savefig(out)
    print(f"Saved {out}")


def print_summary(groups_no, groups_with) -> None:
    print("\n=== Summary over g ===")
    print("label   g      hits   <|A_psi|>       <E>")
    for label, groups in [("no ", groups_no), ("with", groups_with)]:
        for g, data in groups:
            Apsi = data["Apsi"]
            E = data["E"]
            hits = int(data["constraint_hits"])
            print(
                f"{label:4s}  {g:5.2f}  {hits:5d}  "
                f"{np.mean(np.abs(Apsi)):.3e}  {np.mean(E):.6e}"
            )
    print("===")


def main() -> None:
    groups_no = load_group("no_constraint")
    groups_with = load_group("with_constraint")

    if not groups_no or not groups_with:
        print("No coupling scan data found. Run src/run_two_field_coupling_scan.py first.")
        return

    print_summary(groups_no, groups_with)
    plot_Apsi(groups_no, groups_with)
    plot_energy(groups_no, groups_with)
    print("Two-field coupling analysis complete.")


if __name__ == "__main__":
    main()
