"""Lock test for B1764: Dynamical Modular Ground State and tau_* Selection."""

import json
import math
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
ARC = ROOT / "frontier" / "B1764_dynamical_modular_ground_state_and_tau_selection"
VER = ARC / "verification"


def test_b1764_files_and_verdict():
    assert (ARC / "FINDINGS.md").is_file()
    assert (ARC / "arc_verdict.json").is_file()
    assert (VER / "tau_ground_state.py").is_file()
    assert (VER / "tau_ground_state.json").is_file()
    assert (VER / "tau_ground_state_run.txt").is_file()

    verdict = json.loads((ARC / "arc_verdict.json").read_text())
    assert verdict["arc"] == "B1764"
    assert verdict["status"] == "VERIFIED"
    assert verdict["creates_law"] is False
    assert set(verdict["points"]) == {"P-373", "P-380", "P-391"}
    assert "sm:W154" in verdict["cites_seat"]


def test_b1764_sl2z_matrix_and_geodesic_geometry():
    data = json.loads((VER / "tau_ground_state.json").read_text())
    a, b, c, d = data["matrix_A"]

    # SL(2, Z) determinant
    assert a * d - b * c == 1
    assert data["trace_A"] == 110

    # Invariant geodesic circle geometry
    c0 = (a - d) / (2.0 * c)
    assert abs(c0 % 1.0 - 1.0 / 3.0) < 1e-12

    disc = (a + d) ** 2 - 4
    assert disc == 12096
    assert 4 * c**2 == 1296
    # 12096 / 1296 == 84 / 9
    assert disc * 9 == 84 * (4 * c**2)

    expected_R = math.sqrt(84.0) / 3.0
    assert abs(data["geodesic_radius"] - expected_R) < 1e-12
    assert abs(data["tau_star"][0] - 1.0 / 3.0) < 1e-12
    assert abs(data["tau_star"][1] - expected_R) < 1e-12


def test_b1764_modular_potential_stability():
    data = json.loads((VER / "tau_ground_state.json").read_text())
    t_star = data["t_star"]
    w_min, w_max = data["w154_window"]

    # Critical ratio t_* lies inside W154's stability window
    assert w_min <= t_star <= w_max
    assert data["is_inside_window"] is True

    # Radial curvature d^2V/dy^2 is strictly positive (stable minimum)
    assert data["modulus_mass_squared"] > 0.0
    assert abs(data["modulus_mass_squared"] - 17.113) < 0.1
