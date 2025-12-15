#!/usr/bin/env python3
"""
show_theta_star_config.py

Small helper script to verify that the Act II theta★ configuration
is wired correctly into the origin-axiom repo.

It does NOT run any simulations; it just prints the fiducial value
and the working band so other scripts (Einstein-limit, 1D twisted
vacuum, etc.) can copy/paste the pattern.
"""

from __future__ import annotations

from theta_star_config import load_theta_star_config


def main() -> None:
    cfg = load_theta_star_config()
    theta_fid = cfg.theta_star_fid_rad
    theta_lo, theta_hi = cfg.theta_star_band_rad

    print("=== Act II theta★ configuration ===")
    print(f"  fiducial theta★ (rad): {theta_fid:.6f}")
    print(f"  band theta★ (rad):     [{theta_lo:.6f}, {theta_hi:.6f}]")
    print()
    print("Provenance:")
    src = cfg.raw.get("source", {})
    print(f"  repo:   {src.get('repo', 'n/a')}")
    print(f"  runs:   {src.get('runs', 'n/a')}")
    print(f"  chi2_max: {src.get('chi2_max', 'n/a')}")
    print()
    print("Usage example in other scripts:")
    print("  from theta_star_config import load_theta_star_config")
    print("  cfg = load_theta_star_config()")
    print("  theta_fid = cfg.theta_star_fid_rad")
    print("  theta_lo, theta_hi = cfg.theta_star_band_rad")


if __name__ == "__main__":
    main()