"""Lock: Paper II's residue is one-sided and narrowed to five named values."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
R = json.loads((ROOT / "frontier/B8149_paperII_residue_sharpened/results.json").read_text())
B = json.loads((ROOT / "frontier/B8078_rung_spectrum_attained/results.json").read_text())

def test_the_exposure_is_one_sided_and_hits_attainment_not_the_bound():
    d = R["the_direction_argument"]
    assert "CANNOT LOSE" in d["therefore"]
    assert "ATTAINMENT only" in d["what_is_exposed"]
    assert "untouched" in d["what_is_exposed"]

def test_the_five_exposed_values_are_named():
    assert R["the_narrowing"]["exposed"] == [16, 20, 26, 28, 36]

def test_exposed_plus_corroborated_is_the_whole_spectrum():
    corro = [int(k) for k in R["the_narrowing"]["independently_corroborated"]]
    assert sorted(corro + R["the_narrowing"]["exposed"]) == B["spectrum"]

def test_the_residue_is_narrowed_not_closed():
    assert any("narrows it, nothing more" in x for x in R["not_claimed"])

def test_codex_closure_is_not_assumed():
    assert "UNREAD on this bench" in R["status_of_codex_R013"]
