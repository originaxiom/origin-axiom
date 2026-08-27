"""Lock: L173's precision column is closed as a negative, with its scope intact."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
R = json.loads((ROOT / "frontier/B8146_l173_precision/results.json").read_text())
B = json.loads((ROOT / "frontier/B8094_L173_anchors/results.json").read_text())

def test_the_anchor_reports_no_precision_at_all():
    e = R["extracted_from_1403_7124"]
    assert e["error_bars"].startswith("NONE")
    assert e["mode_counting"].startswith("NOT DONE")

def test_the_concrete_numbers_were_extracted():
    e = R["extracted_from_1403_7124"]
    assert "13-28 waveguides" in e["array_sizes"]
    assert "THIRTEEN" in e["phason_sampling"]

def test_the_prediction_is_a_count_so_the_prereg_needs_an_observable():
    f = R["the_finding"]
    assert "COUNT" in f["and_the_deeper_point"]
    assert "OBSERVABLE" in f["what_the_prereg_must_say_instead"]
    assert "KNOB" in f["what_the_prereg_must_say_instead"] and "READOUT" in f["what_the_prereg_must_say_instead"]

def test_b8094s_open_field_is_now_closed():
    assert B["precision_figures_extracted"] is not False
    assert "COMPLETED BY B8146" in str(B["precision_figures_extracted"])

def test_scope_limits_the_claim_to_what_was_read():
    assert "ONE anchor read in full" in R["scope"]
    assert "NOT a claim about every paper" in R["scope"]
    assert any("no experiment anywhere" in x for x in R["not_claimed"])
