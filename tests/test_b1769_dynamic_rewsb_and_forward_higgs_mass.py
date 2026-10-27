"""Lock test for B1769: Dynamic REWSB and Forward Higgs Mass Prediction."""

import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
ARC = ROOT / "frontier" / "B1769_dynamic_rewsb_and_forward_higgs_mass"
VER = ARC / "verification"


def test_b1769_files_and_verdict():
    assert (ARC / "FINDINGS.md").is_file()
    assert (ARC / "arc_verdict.json").is_file()
    assert (VER / "dynamic_rewsb.py").is_file()
    assert (VER / "dynamic_rewsb.json").is_file()
    assert (VER / "dynamic_rewsb_run.txt").is_file()

    verdict = json.loads((ARC / "arc_verdict.json").read_text())
    assert verdict["arc"] == "B1769"
    assert verdict["status"] == "VERIFIED"
    assert verdict["creates_law"] is False
    assert set(verdict["points"]) == {"P-396"}


def test_b1769_dynamic_rewsb_triggered():
    data = json.loads((VER / "dynamic_rewsb.json").read_text())

    # REWSB triggered: mHu2 < 0 and mHd2 > 0
    assert data["is_rewsb_triggered"] is True
    assert data["mHu2_MZ"] < 0
    assert abs(data["mHu_scale_MZ"] - 238.83) < 1.0
    assert data["mHd_scale_MZ"] > 400.0


def test_b1769_forward_higgs_prediction():
    data = json.loads((VER / "dynamic_rewsb.json").read_text())

    # Effective stop scale around 550 GeV
    assert abs(data["M_susy_GeV"] - 549.26) < 2.0
    # Stop mixing ratio around -1.135
    assert abs(data["Xt_over_Msusy"] - (-1.1347)) < 0.05

    # Total quartic around 0.1298
    assert abs(data["lambda_tot"] - 0.1298) < 0.005

    # Forward predicted Higgs mass within 1.5 sigma of LHC PDG target (125.25 +/- 0.17 GeV)
    assert abs(data["predicted_Higgs_mass_GeV"] - 125.46) < 0.25
    assert abs(data["pull_Higgs_mass_sigma"]) <= 1.50
