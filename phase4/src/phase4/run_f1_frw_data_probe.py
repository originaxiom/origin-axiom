#!/usr/bin/env python3
"""
Phase 4: FRW data-facing probe on top of F1 FRW viability.

This script:

- reads the Phase 4 FRW viability mask
  (phase4/outputs/tables/phase4_F1_frw_viability_mask.csv);
- optionally reads an external binned distance-redshift dataset from
  phase4/data/external/frw_distance_binned.csv with columns:
  z, mu, sigma_mu;
- for each FRW-viable theta, computes model distance moduli and a
  chi^2 statistic against the data; and
- writes:
  - a diagnostics JSON:
    phase4/outputs/tables/phase4_F1_frw_data_probe.json
  - a per-theta mask CSV:
    phase4/outputs/tables/phase4_F1_frw_data_probe_mask.csv

If the external data file is missing or empty, the script records
data_available = false in the diagnostics and writes a mask with
chi2_data/chi2_per_dof = NaN and data_ok = 0 for all rows.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np

# ----------------------------------------------------------------------
# Paths and constants
# ----------------------------------------------------------------------

THIS_FILE = Path(__file__).resolve()
PHASE4_ROOT = THIS_FILE.parents[2]  # .../origin-axiom/phase4
TABLES_DIR = PHASE4_ROOT / "outputs" / "tables"
EXTERNAL_DATA_PATH = PHASE4_ROOT / "data" / "external" / "frw_distance_binned.csv"

C_KM_S = 2.99792458e5  # speed of light in km/s

# FRW background parameters (consistent with viability layer)
OMEGA_M = 0.3
OMEGA_R = 0.0
H0_KM_S_MPC = 70.0

# Data-level chi^2 threshold (per degree of freedom)
CHI2_PER_DOF_MAX = 5.0


# ----------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------

def load_viability_mask(path: Path) -> List[Dict[str, object]]:
    if not path.exists():
        raise FileNotFoundError(f"[F1_FRW_DATA_PROBE] Missing viability mask: {path}")

    rows: List[Dict[str, object]] = []
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        expected = {
            "theta",
            "E_vac",
            "omega_lambda",
            "age_Gyr",
            "has_matter_era",
            "has_late_accel",
            "smooth_H2",
            "frw_viable",
        }
        missing = expected.difference(reader.fieldnames or [])
        if missing:
            raise RuntimeError(
                f"[F1_FRW_DATA_PROBE] Viability mask {path} is missing expected "
                f"columns: {sorted(missing)}; found {reader.fieldnames}"
            )

        for row in reader:
            try:
                theta = float(row["theta"])
                evac = float(row["E_vac"])
                omega_lambda = float(row["omega_lambda"])
                age_Gyr = float(row["age_Gyr"])
                has_matter_era = bool(int(row["has_matter_era"]))
                has_late_accel = bool(int(row["has_late_accel"]))
                smooth_H2 = bool(int(row["smooth_H2"]))
                frw_viable = bool(int(row["frw_viable"]))
            except Exception as exc:  # noqa: BLE001
                raise RuntimeError(
                    f"[F1_FRW_DATA_PROBE] Failed to parse row in {path}: {row}"
                ) from exc

            rows.append(
                {
                    "theta": theta,
                    "E_vac": evac,
                    "omega_lambda": omega_lambda,
                    "age_Gyr": age_Gyr,
                    "has_matter_era": has_matter_era,
                    "has_late_accel": has_late_accel,
                    "smooth_H2": smooth_H2,
                    "frw_viable": frw_viable,
                }
            )
    return rows


def load_external_data(path: Path) -> List[Tuple[float, float, float]]:
    """
    Load external distance-redshift data.

    Expected CSV columns: z, mu, sigma_mu.
    Returns a list of (z, mu, sigma_mu) for sigma_mu > 0.
    If file is missing or empty/invalid, returns an empty list.
    """
    if not path.exists():
        print(f"[F1_FRW_DATA_PROBE] No external data file found at {path}")
        return []

    data: List[Tuple[float, float, float]] = []
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            print(f"[F1_FRW_DATA_PROBE] External data file {path} has no header")
            return []

        required = {"z", "mu", "sigma_mu"}
        missing = required.difference(reader.fieldnames)
        if missing:
            print(
                f"[F1_FRW_DATA_PROBE] External data file {path} is missing "
                f"required columns: {sorted(missing)}; found {reader.fieldnames}"
            )
            return []

        for row in reader:
            try:
                z = float(row["z"])
                mu = float(row["mu"])
                sigma = float(row["sigma_mu"])
            except Exception:
                continue
            if sigma <= 0.0:
                continue
            if z < 0.0:
                continue
            data.append((z, mu, sigma))

    print(f"[F1_FRW_DATA_PROBE] Loaded {len(data)} data points from {path}")
    return data


def E_of_z(
    z: np.ndarray,
    omega_m: float,
    omega_r: float,
    omega_lambda: float,
) -> np.ndarray:
    """Dimensionless H(z)/H0 for flat FRW with given Omegas."""
    zp1 = 1.0 + z
    return np.sqrt(omega_r * zp1**4 + omega_m * zp1**3 + omega_lambda)


def comoving_distance_Mpc(
    z: float,
    omega_m: float,
    omega_r: float,
    omega_lambda: float,
    H0_km_s_Mpc: float,
    n_grid: int = 512,
) -> float:
    """Comoving distance in Mpc for a single redshift."""
    if z <= 0.0:
        return 0.0

    z_grid = np.linspace(0.0, z, n_grid)
    integrand = 1.0 / E_of_z(z_grid, omega_m, omega_r, omega_lambda)
    integral = float(np.trapezoid(integrand, z_grid))
    return (C_KM_S / H0_km_s_Mpc) * integral


def distance_modulus_from_omega_lambda(
    z: float,
    omega_lambda: float,
    omega_m: float,
    omega_r: float,
    H0_km_s_Mpc: float,
) -> float:
    """Distance modulus mu(z) from a flat FRW model with given Omegas."""
    dL_Mpc = (1.0 + z) * comoving_distance_Mpc(
        z=z,
        omega_m=omega_m,
        omega_r=omega_r,
        omega_lambda=omega_lambda,
        H0_km_s_Mpc=H0_km_s_Mpc,
    )
    if dL_Mpc <= 0.0:
        return float("nan")
    return 5.0 * np.log10(dL_Mpc) + 25.0


def chi2_for_theta(
    omega_lambda: float,
    data: List[Tuple[float, float, float]],
    omega_m: float,
    omega_r: float,
    H0_km_s_Mpc: float,
) -> Tuple[float, float]:
    """
    Compute chi^2 and chi^2/dof for a given omega_lambda and data set.

    Returns (chi2, chi2_per_dof). If the model breaks (NaNs), returns
    (inf, inf).
    """
    if not data:
        return float("nan"), float("nan")

    chi2 = 0.0
    n_eff = 0
    for z, mu_obs, sigma_mu in data:
        mu_model = distance_modulus_from_omega_lambda(
            z=z,
            omega_lambda=omega_lambda,
            omega_m=omega_m,
            omega_r=omega_r,
            H0_km_s_Mpc=H0_km_s_Mpc,
        )
        if not np.isfinite(mu_model):
            return float("inf"), float("inf")
        r = (mu_model - mu_obs) / sigma_mu
        chi2 += float(r * r)
        n_eff += 1

    if n_eff <= 0:
        return float("nan"), float("nan")

    chi2_per_dof = chi2 / float(n_eff)
    return chi2, chi2_per_dof


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------

def main() -> None:
    TABLES_DIR.mkdir(parents=True, exist_ok=True)

    viability_path = TABLES_DIR / "phase4_F1_frw_viability_mask.csv"
    diag_path = TABLES_DIR / "phase4_F1_frw_data_probe.json"
    mask_path = TABLES_DIR / "phase4_F1_frw_data_probe_mask.csv"

    rows = load_viability_mask(viability_path)
    data = load_external_data(EXTERNAL_DATA_PATH)

    data_available = len(data) > 0
    n_grid = len(rows)
    n_frw_viable = sum(1 for r in rows if r["frw_viable"])

    chi2_list: List[float] = []
    chi2_per_dof_list: List[float] = []
    data_ok_flags: List[bool] = []

    if not data_available:
        print(
            "[F1_FRW_DATA_PROBE] No usable external data; writing mask with "
            "data_ok = 0 for all rows."
        )
        for r in rows:
            chi2_list.append(float("nan"))
            chi2_per_dof_list.append(float("nan"))
            data_ok_flags.append(False)
        n_data = 0
        n_data_ok = 0
    else:
        n_data = len(data)
        n_data_ok = 0
        for r in rows:
            frw_viable = bool(r["frw_viable"])
            omega_lambda = float(r["omega_lambda"])
            if not frw_viable:
                chi2 = float("nan")
                chi2_per_dof = float("nan")
                ok = False
            else:
                chi2, chi2_per_dof = chi2_for_theta(
                    omega_lambda=omega_lambda,
                    data=data,
                    omega_m=OMEGA_M,
                    omega_r=OMEGA_R,
                    H0_km_s_Mpc=H0_KM_S_MPC,
                )
                ok = (
                    np.isfinite(chi2_per_dof)
                    and chi2_per_dof <= CHI2_PER_DOF_MAX
                )
            chi2_list.append(chi2)
            chi2_per_dof_list.append(chi2_per_dof)
            data_ok_flags.append(ok)
            if ok:
                n_data_ok += 1

    frac_data_ok = (
        float(n_data_ok) / float(n_frw_viable) if n_frw_viable > 0 else 0.0
    )

    diagnostics = {
        "mapping_family": "F1",
        "source_mask": str(viability_path),
        "external_data_path": str(EXTERNAL_DATA_PATH),
        "data_available": data_available,
        "n_grid": n_grid,
        "n_frw_viable": n_frw_viable,
        "n_data_points": n_data,
        "chi2_per_dof_max": CHI2_PER_DOF_MAX,
        "n_data_ok": n_data_ok,
        "frac_data_ok_within_frw_viable": frac_data_ok,
    }

    with diag_path.open("w", encoding="utf-8") as f:
        json.dump(diagnostics, f, indent=2, sort_keys=True)

    fieldnames = [
        "theta",
        "E_vac",
        "omega_lambda",
        "age_Gyr",
        "has_matter_era",
        "has_late_accel",
        "smooth_H2",
        "frw_viable",
        "chi2_data",
        "chi2_per_dof",
        "data_ok",
    ]

    with mask_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(fieldnames)
        for r, chi2, chi2pdof, ok in zip(
            rows, chi2_list, chi2_per_dof_list, data_ok_flags
        ):
            writer.writerow(
                [
                    float(r["theta"]),
                    float(r["E_vac"]),
                    float(r["omega_lambda"]),
                    float(r["age_Gyr"]),
                    int(bool(r["has_matter_era"])),
                    int(bool(r["has_late_accel"])),
                    int(bool(r["smooth_H2"])),
                    int(bool(r["frw_viable"])),
                    float(chi2),
                    float(chi2pdof),
                    int(bool(ok)),
                ]
            )

    print("[F1_FRW_DATA_PROBE] Wrote diagnostics to", diag_path)
    print("[F1_FRW_DATA_PROBE] Wrote mask CSV to", mask_path)
    print("[F1_FRW_DATA_PROBE] Summary:")
    for k, v in diagnostics.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
