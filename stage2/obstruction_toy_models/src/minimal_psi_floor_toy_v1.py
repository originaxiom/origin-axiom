from __future__ import annotations

from pathlib import Path
from typing import Tuple

import numpy as np
import pandas as pd


def get_repo_root() -> Path:
    here = Path(__file__).resolve()
    # This file lives under stage2/obstruction_toy_models/src/
    # so repo_root is three levels up.
    return here.parents[3]


def evolve_trajectory(
    psi0: complex,
    gamma: float,
    eps: float,
    h: float,
    n_steps: int,
) -> Tuple[bool, float, float, float]:
    psi = psi0
    floor_hits = 0
    r_min = abs(psi)
    r_max = abs(psi)

    for _ in range(n_steps):
        # Unconstrained step
        psi_half = psi - h * gamma * psi

        r_half = abs(psi_half)
        if r_half < eps:
            if r_half == 0.0:
                # Avoid division by zero: pick an arbitrary direction on the unit circle
                psi = eps * complex(1.0, 0.0)
            else:
                psi = eps * psi_half / r_half
            floor_hits += 1
        else:
            psi = psi_half

        r = abs(psi)
        if r < r_min:
            r_min = r
        if r > r_max:
            r_max = r

    ever_on_floor = floor_hits > 0
    floor_active_fraction = floor_hits / float(n_steps)
    r_final = abs(psi)

    return ever_on_floor, floor_active_fraction, r_min, r_max, r_final


def main() -> int:
    repo_root = get_repo_root()
    base_path = repo_root / "stage2/obstruction_toy_models/outputs/tables"
    base_path.mkdir(parents=True, exist_ok=True)

    # Parameters for the toy
    gamma = 1.0
    eps = 0.05
    h = 0.01
    n_steps = 2000
    n_ics = 256

    rng = np.random.default_rng(seed=20260121)

    rows = []
    for i in range(n_ics):
        # Sample initial radius in a moderate range and random phase
        r0 = rng.uniform(0.2, 2.0)
        phi0 = rng.uniform(0.0, 2.0 * np.pi)
        psi0 = r0 * np.exp(1j * phi0)

        ever_on_floor, frac_floor, r_min, r_max, r_final = evolve_trajectory(
            psi0=psi0,
            gamma=gamma,
            eps=eps,
            h=h,
            n_steps=n_steps,
        )

        rows.append(
            {
                "ic_index": i,
                "psi0_real": float(psi0.real),
                "psi0_imag": float(psi0.imag),
                "r0": float(abs(psi0)),
                "ever_on_floor": bool(ever_on_floor),
                "floor_active_fraction": float(frac_floor),
                "r_min": float(r_min),
                "r_max": float(r_max),
                "r_final": float(r_final),
                "gamma": float(gamma),
                "eps": float(eps),
                "h": float(h),
                "n_steps": int(n_steps),
            }
        )

    df = pd.DataFrame(rows)
    out_path = base_path / "stage2_minimal_psi_floor_toy_trajectories_v1.csv"
    df.to_csv(out_path, index=False)

    print("[minimal_psi_floor_toy_v1]")
    print(f"  repo_root: {repo_root}")
    print(f"  wrote trajectories table: {out_path}")
    print(f"  n_ics={n_ics}, n_steps={n_steps}, gamma={gamma}, eps={eps}, h={h}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
