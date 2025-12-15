#!/usr/bin/env python3
"""
Quick inspection / plotting helper for the 1D two-field localized bump run.

It expects the NPZ produced by:
    PYTHONPATH=src python3 src/run_two_field_bump_1d.py ...

and currently knows how to handle the layout:

  t_snap                       (101,)
  loc_free, loc_constrained    (101,)
  profile_times_free           (4,)
  profiles_phi_free            (4, 512)
  profiles_chi_free            (4, 512)
  profile_times_constrained    (4,)
  profiles_phi_constrained     (4, 512)
  profiles_chi_constrained     (4, 512)
  params                       ()

It will:
  - print the available keys and shapes
  - plot the localized diagnostic vs time (free vs constrained)
  - plot final-time φ and χ profiles (free vs constrained)

Figures are written to:
  data/processed/figures/two_field_bump_1d_loc_amp.png
  data/processed/figures/two_field_bump_1d_phi_final.png
  data/processed/figures/two_field_bump_1d_chi_final.png
"""

from __future__ import annotations

import pathlib
import numpy as np
import matplotlib.pyplot as plt


DATA_PATH = pathlib.Path("data/processed/two_field_bump_1d.npz")
FIG_DIR = pathlib.Path("data/processed/figures")


def main() -> None:
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Could not find {DATA_PATH}")

    d = np.load(DATA_PATH, allow_pickle=True)

    print(f"Loaded {DATA_PATH}")
    print("Available arrays:")
    for k in sorted(d.files):
        arr = d[k]
        print(f"  {k:<26} shape={arr.shape}, dtype={arr.dtype}")

    FIG_DIR.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------
    # 1) Localized diagnostic vs time
    # ------------------------------------------------------------------
    if {"t_snap", "loc_free", "loc_constrained"}.issubset(d.files):
        t = d["t_snap"]
        loc_free = d["loc_free"]
        loc_con = d["loc_constrained"]

        plt.figure(figsize=(8, 5))
        plt.plot(t, loc_free, label="free", alpha=0.8)
        plt.plot(t, loc_con, label="constrained", alpha=0.8)
        plt.xlabel("t")
        plt.ylabel("localized amplitude")
        plt.title("Two-field bump: localized diagnostic vs time")
        plt.legend()
        out = FIG_DIR / "two_field_bump_1d_loc_amp.png"
        plt.tight_layout()
        plt.savefig(out, dpi=150)
        plt.close()
        print(f"Wrote {out}")
    else:
        print("Skipping time-series plot: missing one of "
              "{t_snap, loc_free, loc_constrained}")

    # ------------------------------------------------------------------
    # 2) Final φ profile: free vs constrained
    # ------------------------------------------------------------------
    if {
        "profiles_phi_free",
        "profiles_phi_constrained",
        "profile_times_free",
        "profile_times_constrained",
    }.issubset(d.files):
        phi_free = d["profiles_phi_free"]
        phi_con = d["profiles_phi_constrained"]
        t_free = d["profile_times_free"]
        t_con = d["profile_times_constrained"]

        x = np.arange(phi_free.shape[1])

        # last snapshot index
        i_f = -1

        plt.figure(figsize=(8, 5))
        plt.plot(x, phi_free[i_f], label=f"φ free (t={t_free[i_f]:.2f})", alpha=0.8)
        plt.plot(x, phi_con[i_f], label=f"φ constrained (t={t_con[i_f]:.2f})", alpha=0.8)
        plt.xlabel("lattice site")
        plt.ylabel("φ")
        plt.title("Two-field bump: φ profile at final snapshot")
        plt.legend()
        out = FIG_DIR / "two_field_bump_1d_phi_final.png"
        plt.tight_layout()
        plt.savefig(out, dpi=150)
        plt.close()
        print(f"Wrote {out}")
    else:
        print("Skipping φ-profile plot: missing φ snapshot arrays")

    # ------------------------------------------------------------------
    # 3) Final χ profile: free vs constrained
    # ------------------------------------------------------------------
    if {
        "profiles_chi_free",
        "profiles_chi_constrained",
        "profile_times_free",
        "profile_times_constrained",
    }.issubset(d.files):
        chi_free = d["profiles_chi_free"]
        chi_con = d["profiles_chi_constrained"]
        t_free = d["profile_times_free"]
        t_con = d["profile_times_constrained"]

        x = np.arange(chi_free.shape[1])
        i_f = -1

        plt.figure(figsize=(8, 5))
        plt.plot(x, chi_free[i_f], label=f"χ free (t={t_free[i_f]:.2f})", alpha=0.8)
        plt.plot(x, chi_con[i_f], label=f"χ constrained (t={t_con[i_f]:.2f})", alpha=0.8)
        plt.xlabel("lattice site")
        plt.ylabel("χ")
        plt.title("Two-field bump: χ profile at final snapshot")
        plt.legend()
        out = FIG_DIR / "two_field_bump_1d_chi_final.png"
        plt.tight_layout()
        plt.savefig(out, dpi=150)
        plt.close()
        print(f"Wrote {out}")
    else:
        print("Skipping χ-profile plot: missing χ snapshot arrays")


if __name__ == "__main__":
    main()