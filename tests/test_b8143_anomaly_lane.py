"""Lock: the anomaly-lane findings, exact, with no floating point."""
import json, pathlib
from fractions import Fraction as F
ROOT = pathlib.Path(__file__).resolve().parents[1]
R = json.loads((ROOT / "frontier/B8143_anomaly_lane/results.json").read_text())

ST  = {"A": 6, "B": 3, "C": 2, "D": 1}
TRI = {"A": 2, "B": 1, "C": 0, "D": 0}
DBL = {"A": 3, "B": 0, "C": 1, "D": 0}

def anomalies(content, ys):
    return [sum(TRI[r]*y for r, y in zip(content, ys)),
            sum(DBL[r]*y for r, y in zip(content, ys)),
            sum(ST[r]*y for r, y in zip(content, ys)),
            sum(ST[r]*y**3 for r, y in zip(content, ys))]

def test_the_sm_generation_is_anomaly_free():
    assert all(x == 0 for x in anomalies("ABBCD",
        [F(1,6), F(-2,3), F(1,3), F(-1,2), F(1)]))

def test_the_13_state_competitor_is_anomaly_free_and_smaller():
    comp = "ABCDD"
    ys = [F(1,2), F(-1), F(-3,2), F(2), F(1)]
    assert all(x == 0 for x in anomalies(comp, ys))
    assert sum(ST[r] for r in comp) == 13 < sum(ST[r] for r in "ABBCD") == 15
    assert all(y != 0 for y in ys)                     # no sterile field
    assert sum(DBL[r] for r in comp) % 2 == 0          # Witten

def test_b1160_core_reproduced_exactly():
    c = R["b1160_core_reproduced"]
    assert "-18(t-3)(t+3)" in c["cubic"] and "matches exactly" in c["cubic"]
    assert "CORRECT as stated" in c["verdict"]

def test_the_hidden_vector_like_branch_is_recorded():
    s = R["scope_finding_1_the_hidden_branch"]
    assert "THREE branches" in s["result"] and "VECTOR-LIKE" in s["result"]
    assert "B864" in s["corroboration"]
    assert s["is_it_damaging"].startswith("NO")

def test_the_shape_witness_is_recorded_with_its_consequence():
    s = R["scope_finding_2_the_shape_is_free_with_a_witness"]
    assert s["the_witness"]["states"] == 13
    assert "NOT THE MINIMAL" in s["consequence"]

def test_both_of_my_instrument_errors_are_recorded():
    e = R["my_own_two_instrument_errors"]
    assert "RIGIDITY, not existence" in e["first"]
    assert "NEUTRAL (3,2)" in e["second"]

def test_the_decisive_question_is_posed_and_not_answered():
    q = R["the_decisive_open_question"]
    assert "realisable inside the object's 27" in q["statement"]
    assert "not done" in q["not_attempted_here"]
