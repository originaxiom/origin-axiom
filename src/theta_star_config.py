"""
theta_star_config.py

Helper to load the theta★ configuration that was inferred in the
`origin-axiom-theta-star` phenomenology repo.

This keeps the scalar-universe / cancellation-system scripts decoupled
from the fitting details, while allowing them to consume a fiducial
theta★ value and an uncertainty band.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Tuple
import json

# Project layout assumption:
#   origin-axiom/
#     config/theta_star_config.json
#     src/theta_star_config.py  (this file)
#
# If the layout changes, only this path logic needs updating.
_CONFIG_PATH = (Path(__file__).resolve().parent.parent
                / "config"
                / "theta_star_config.json")


@dataclass(frozen=True)
class ThetaStarConfig:
    theta_star_fid_rad: float
    theta_star_band_rad: Tuple[float, float]
    raw: Dict[str, Any]


def load_theta_star_config(path: Path | None = None) -> ThetaStarConfig:
    """
    Load the theta★ configuration from JSON.

    Parameters
    ----------
    path : Path, optional
        Override path to the JSON config. If None, use the project default.

    Returns
    -------
    ThetaStarConfig
        - theta_star_fid_rad: fiducial theta★ (radians)
        - theta_star_band_rad: (lo, hi) band (radians)
        - raw: full JSON dict for any extra metadata
    """
    cfg_path = path or _CONFIG_PATH
    if not cfg_path.is_file():
        raise FileNotFoundError(f"theta★ config not found at {cfg_path}")

    with cfg_path.open("r", encoding="utf-8") as f:
        data: Dict[str, Any] = json.load(f)

    band = data.get("theta_star_band_rad", {})
    lo = float(band.get("lo"))
    hi = float(band.get("hi"))

    return ThetaStarConfig(
        theta_star_fid_rad=float(data["theta_star_fid_rad"]),
        theta_star_band_rad=(lo, hi),
        raw=data,
    )