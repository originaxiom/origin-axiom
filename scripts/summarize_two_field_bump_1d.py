#!/usr/bin/env python3
"""
Summarise the 1D two-field bump demo.

Reads data/processed/two_field_bump_1d.npz and prints a few simple
diagnostics for the localised bump amplitude with and without
the non-cancelling constraint.
"""

import numpy as np
from pathlib import Path


def main() -> None:
    path = Path("data/processed/two_field_bump_1d.npz")
    if not path.exists():
        raise FileNotFoundError(
            f"{path} not found. Run src/run_two_field_bump_1d.py first."
        )

    d = np.load(path)

    t = d["t_snap"]  # shape (T,)
    loc_free = d["loc_free"]  # shape (T,)
    loc_con = d["loc_constrained"]  # shape (T,)

    print("=== two_field_bump_1d summary ===")
    print(f"file: {path}")
    print(f"  n_snapshots = {t.size}")
    print(f"  t range     = {float(t[0]):.3f} -> {float(t[-1]):.3f}")

    a0_free = float(loc_free[0])
    a0_con = float(loc_con[0])
    aF_free = float(loc_free[-1])
    aF_con = float(loc_con[-1])

    print()
    print("Initial amplitudes:")
    print(f"  loc_free(0)        = {a0_free:.6e}")
    print(f"  loc_constrained(0) = {a0_con:.6e}")
    print("Final amplitudes:")
    print(f"  loc_free(t_final)        = {aF_free:.6e}")
    print(f"  loc_constrained(t_final) = {aF_con:.6e}")

    # Simple lifetime proxy: last time where |loc| >= 0.5 * |loc(0)|
    def half_life_time(t_arr: np.ndarray, x_arr: np.ndarray) -> float:
        threshold = 0.5 * abs(float(x_arr[0]))
        mask = np.abs(x_arr) >= threshold
        if not np.any(mask):
            return float(t_arr[0])
        idx_last = np.where(mask)[0][-1]
        return float(t_arr[idx_last])

    t_half_free = half_life_time(t, loc_free)
    t_half_con = half_life_time(t, loc_con)

    print()
    print("Half-amplitude lifetimes (|loc| >= 0.5 * |loc(0)|):")
    print(f"  free        : t_half ≈ {t_half_free:.3f}")
    print(f"  constrained : t_half ≈ {t_half_con:.3f}")

    if t_half_free > 0.0:
        ratio = t_half_con / t_half_free
        print(f"  ratio t_half(constrained) / t_half(free) ≈ {ratio:.2f}")

    print()
    print("Mean absolute amplitudes:")
    print(f"  <|loc_free|>        = {float(np.mean(np.abs(loc_free))):.6e}")
    print(f"  <|loc_constrained|> = {float(np.mean(np.abs(loc_con))):.6e}")


if __name__ == "__main__":
    main()
