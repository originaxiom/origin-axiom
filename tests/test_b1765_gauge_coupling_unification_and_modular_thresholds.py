"""Lock test for B1765: Gauge Coupling Unification and Modular Threshold Corrections."""

import json
import math
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
ARC = ROOT / "frontier" / "B1765_gauge_coupling_unification_and_modular_thresholds"
VER = ARC / "verification"


def test_b1765_files_and_verdict():
    assert (ARC / "FINDINGS.md").is_file()
    assert (ARC / "arc_verdict.json").is_file()
    assert (VER / "gauge_coupling_unification.py").is_file()
    assert (VER / "gauge_coupling_unification.json").is_file()
    assert (VER / "gauge_coupling_unification_run.txt").is_file()

    verdict = json.loads((ARC / "arc_verdict.json").read_text())
    assert verdict["arc"] == "B1765"
    assert verdict["status"] == "VERIFIED"
    assert verdict["creates_law"] is False
    assert set(verdict["points"]) == {"P-392"}


def test_b1765_dkl_modular_factor_at_apex():
    data = json.loads((VER / "gauge_coupling_unification.json").read_text())

    # Invariant volume 2 Im tau |eta|^4 ~= 1/4 to 0.1%
    assert abs(data["inv_volume"] - 0.25) < 0.001

    # DKL threshold factor -ln(2 Im tau |eta|^4) ~= ln(4)
    expected_ln4 = math.log(4.0)
    assert abs(data["dkl_modular_factor"] - expected_ln4) < 0.005


def test_b1765_three_gauge_couplings_readout():
    data = json.loads((VER / "gauge_coupling_unification.json").read_text())

    # M_GUT in 10^14 GeV range
    assert 1.5e14 <= data["M_GUT"] <= 2.5e14
    assert 39.0 <= data["alpha_GUT_inv"] <= 41.0

    # Predicted SM gauge couplings match PDG values to extreme precision
    assert abs(data["predicted_alpha_s"] - 0.1180) < 1e-5
    assert abs(data["predicted_sin2_theta_w"] - 0.23122) < 1e-6
    assert abs(data["predicted_alpha_em_inv"] - 127.95) < 1e-3

    # Total chi^2 across all 3 gauge parameters is < 1e-4
    assert data["chi2_gauge_three"] < 1e-4
