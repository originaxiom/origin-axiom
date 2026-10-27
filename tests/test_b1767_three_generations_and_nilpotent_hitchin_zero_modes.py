"""Lock test for B1767: Three Generations and Nilpotent Hitchin Zero-Modes on Genus-3 Cover."""

import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
ARC = ROOT / "frontier" / "B1767_three_generations_and_nilpotent_hitchin_zero_modes"
VER = ARC / "verification"


def test_b1767_files_and_verdict():
    assert (ARC / "FINDINGS.md").is_file()
    assert (ARC / "arc_verdict.json").is_file()
    assert (VER / "hitchin_zero_modes.py").is_file()
    assert (VER / "hitchin_zero_modes.json").is_file()
    assert (VER / "hitchin_zero_modes_run.txt").is_file()

    verdict = json.loads((ARC / "arc_verdict.json").read_text())
    assert verdict["arc"] == "B1767"
    assert verdict["status"] == "VERIFIED"
    assert verdict["creates_law"] is False
    assert set(verdict["points"]) == {"P-394"}


def test_b1767_three_generations_and_differentials():
    data = json.loads((VER / "hitchin_zero_modes.json").read_text())
    assert data["genus"] == 3
    assert data["chiral_generations"] == 3

    diffs = data["differentials"]
    assert len(diffs) == 3

    # omega_1 is singlet with parity +1
    assert diffs[0]["name"] == "omega_1"
    assert "singlet" in diffs[0]["rep"]
    assert diffs[0]["z_parity"] == +1

    # omega_2 and omega_3 form doublet with parity -1
    assert diffs[1]["name"] == "omega_2"
    assert "doublet" in diffs[1]["rep"]
    assert diffs[1]["z_parity"] == -1

    assert diffs[2]["name"] == "omega_3"
    assert "doublet" in diffs[2]["rep"]
    assert diffs[2]["z_parity"] == -1


def test_b1767_gram_block_diagonality():
    data = json.loads((VER / "hitchin_zero_modes.json").read_text())
    assert data["gram_is_1_plus_2_block_diagonal"] is True
    assert set(data["gram_zero_entries"]) == {"G_12", "G_13", "G_21", "G_31"}


def test_b1767_nilpotent_hitchin_orbit():
    data = json.loads((VER / "hitchin_zero_modes.json").read_text())
    hitchin = data["hitchin_selection"]
    assert hitchin["dim_S6"] == 0
    assert hitchin["casimir_Q2"] == 0.0
    assert hitchin["is_strictly_nilpotent"] is True
