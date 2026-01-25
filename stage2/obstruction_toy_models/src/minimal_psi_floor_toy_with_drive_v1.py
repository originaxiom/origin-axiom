from __future__ import annotations

from pathlib import Path
import numpy as np
import pandas as pd


def find_repo_root(start: Path | None = None) -> Path:
    here = start or Path(__file__).resolve()
    for parent in [here] + list(here.parents):
        if (parent / ".git").is_dir():
            return parent
    raise RuntimeError("Could not find repo root (no .git found)")


def evolve_trajectory(
    psi0: complex,
    gamma: float,
    omega: float,
    drive: float,
    eps: float,
    h: float,
    n_steps: int,
) -> dict:
    psi = psi0
    r0 = abs(psi0)

    r_min = r0
    r_max = r0
    on_floor_steps = 0

    for _ in range(n_steps):
        # Project onto the floor if cancellation would overshoot it
        r = abs(psi)
        if r < eps:
            if r == 0.0:
                psi = eps + 0j
            else:
                psi = eps * psi / r
            on_floor_steps += 1

        # Friction + rotation + simple constant drive
        #   dψ/dτ = -γ ψ + i ω ψ + drive
        dpsi = (-gamma * psi) + (1j * omega * psi) + drive
        psi = psi + h * dpsi

        r = abs(psi)
        if r < r_min:
            r_min = r
        if r > r_max:
            r_max = r

    r_final = abs(psi)
    floor_active_fraction = on_floor_steps / float(n_steps)

    return {
        "psi0_real": float(psi0.real),
        "psi0_imag": float(psi0.imag),
        "r0": float(r0),
        "r_min": float(r_min),
        "r_max": float(r_max),
        "r_final": float(r_final),
        "ever_on_floor": bool(r_min <= eps + 1e-12),
        "floor_active_fraction": float(floor_active_fraction),
    }


def main() -> int:
    repo_root = find_repo_root()
    out_path = (
        repo_root
        / "stage2/obstruction_toy_models/outputs/tables"
        / "stage2_minimal_psi_floor_toy_with_drive_trajectories_v1.csv"
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)

    rng = np.random.default_rng(42)

    n_ics = 256
    gamma = 1.0
    omega = 1.0
    drive = 0.15
    eps = 0.05
    h = 0.01
    n_steps = 2000

    rows = []
    for ic_index in range(n_ics):
        r0 = rng.uniform(0.2, 2.0)
        phi0 = rng.uniform(0.0, 2.0 * np.pi)
        psi0 = r0 * np.exp(1j * phi0)

        stats = evolve_trajectory(
            psi0=psi0,
            gamma=gamma,
            omega=omega,
            drive=drive,
            eps=eps,
            h=h,
            n_steps=n_steps,
        )
        stats.update(
            {
                "ic_index": ic_index,
                "gamma": gamma,
                "omega": omega,
                "drive": drive,
                "eps": eps,
                "h": h,
                "n_steps": n_steps,
            }
        )
        rows.append(stats)

    df = pd.DataFrame(rows)
    df = df[
        [
            "ic_index",
            "psi0_real",
            "psi0_imag",
            "r0",
            "ever_on_floor",
            "floor_active_fraction",
            "r_min",
            "r_max",
            "r_final",
            "gamma",
            "omega",
            "drive",
            "eps",
            "h",
            "n_steps",
        ]
    ]
    df.to_csv(out_path, index=False)

    print("[minimal_psi_floor_toy_with_drive_v1]")
    print(f"  repo_root: {repo_root}")
    print(f"  wrote trajectories table: {out_path}")
    print(f"  n_ics={n_ics}, n_steps={n_steps}, gamma={gamma}, omega={omega}, drive={drive}, eps={eps}, h={h}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
