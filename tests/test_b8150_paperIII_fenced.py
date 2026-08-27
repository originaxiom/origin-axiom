"""Lock: Paper III's continuation fence is present and the duplicate is gone."""
import json, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[1]
R = json.loads((ROOT / "frontier/B8150_paperIII_fenced/results.json").read_text())
TEX = (ROOT / "papers/series/paper3_one_loop/main.tex").read_text()

def test_the_paper_states_where_the_identity_was_verified():
    assert r"\mathrm{Re}(s)>2+m" in TEX
    assert "continues\nmeromorphically" in TEX or "continues meromorphically" in TEX

def test_the_paper_names_the_continuation_as_the_licence():
    assert "identity theorem" in TEX and "licenses the" in TEX

def test_the_duplicated_lead_in_is_gone():
    assert TEX.count("The gap can nevertheless be located exactly") == 1

def test_the_defect_is_recorded_as_fencing_not_falsehood():
    d = R["defect_1_the_missing_fence"]
    assert d["is_the_statement_false"].startswith("NO")
    assert "FENCING defect" in d["is_the_statement_false"]

def test_the_whole_codex_set_is_accounted_for():
    c = R["codex_set_now_complete"]
    assert set(c) == {"R010", "R011", "R013", "R014"}
