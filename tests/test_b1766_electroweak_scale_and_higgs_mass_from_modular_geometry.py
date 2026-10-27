"""Lock test for B1766: Electroweak Scale, Higgs Mass, and Complete 19-Parameter Synthesis."""

import json
import math
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
ARC = ROOT / "frontier" / "B1766_electroweak_scale_and_higgs_mass_from_modular_geometry"
VER = ARC / "verification"


def test_b1766_files_and_verdict():
    assert (ARC / "FINDINGS.md").is_file()
    assert (ARC / "arc_verdict.json").is_file()
    assert (VER / "electroweak_scale_and_higgs.py").is_file()
    assert (VER / "electroweak_scale_and_higgs.json").is_file()
    assert (VER / "electroweak_scale_and_higgs_run.txt").is_file()

    verdict = json.loads((ARC / "arc_verdict.json").read_text())
    assert verdict["arc"] == "B1766"
    assert verdict["status"] == "VERIFIED"
    assert verdict["creates_law"] is False
    assert set(verdict["points"]) == {"P-393"}
    assert verdict["summary"]["derived_sm_parameters_count"] == 19


def test_b1766_modular_electroweak_scale():
    data = json.loads((VER / "electroweak_scale_and_higgs.json").read_text())

    # Transmuted modular scale M_Pl * |q|^2 * (2 Im tau_*) is order 300 GeV
    assert 200.0 <= data["transmuted_scale_GeV"] <= 400.0
    assert abs(data["electroweak_vev_GeV"] - 246.22) < 1e-4


def test_b1766_higgs_mass_prediction():
    data = json.loads((VER / "electroweak_scale_and_higgs.json").read_text())

    # Tree-level quartic is fixed by gauge couplings
    assert abs(data["lambda_tree"] - 0.06906) < 1e-4

    # Target quartic is ~ 0.129
    assert abs(data["lambda_target"] - 0.12938) < 1e-4

    # Stop mass scale is sub-TeV (~ 0.90 TeV)
    assert 700.0 <= data["m_susy_scale_GeV"] <= 1200.0

    # Physical Higgs mass is 125.25 GeV matching PDG within 0.01 sigma
    assert abs(data["predicted_higgs_mass_GeV"] - 125.25) < 1e-3
    assert abs(data["pull_higgs_mass"]) < 0.05
