"""B8116 -- locks the proven/conjectured split, the scope fence, and the B8115 correction."""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = json.load(open(os.path.join(ROOT, "frontier", "B8116_c2_pathA_tower", "results.json")))


def test_reading_depth_is_declared_as_summary_level():
    """B8102's lesson inverted: no theorem-level precision claimed from summaries."""
    d = R["reading_depth"]
    assert "SUMMARY-LEVEL" in d and "NOT read verbatim" in d
    assert "cuts BOTH ways" in d


def test_andersen_hansen_proven_and_unproven_are_kept_apart():
    ah = R["andersen_hansen"]
    assert len(ah["proved"]) == 3 and len(ah["not_proved"]) == 2
    assert any("Chern-Simons" in p for p in ah["proved"])
    assert any("PROPOSED, not proved" in p for p in ah["not_proved"])
    assert any("AGREED WITH, not established" in p for p in ah["not_proved"])


def test_gz_is_recorded_as_partially_open():
    s = R["garoufalidis_zagier"]["status_for_4_1"]
    assert "PARTIALLY OPEN" in s and "SOME ARE NOW PROVED" in s


def test_the_surgery_versus_complement_fence_is_present():
    f = R["scope_fence"]
    assert "CLOSED manifolds" in f and "CUSPED COMPLEMENT" in f
    assert "Adjacent, not identical" in f


def test_b8115s_successor_set_is_corrected_not_replaced():
    c = R["corrects_b8115"]
    assert "TOO NARROW" in c
    assert "at least TWO candidate doors" in c
    # the correction widens; it must not retract the boundary itself
    assert "ARCHIMEDEAN PLACE" in c


def test_the_cs_zero_question_is_registered_as_not_answered():
    q = R["sharp_question_for_our_object"]
    assert "NOT asked here" in q and "needs the full text" in q
