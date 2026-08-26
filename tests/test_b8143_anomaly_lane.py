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

A3 = {"A": +2, "B": -1, "C": 0, "D": 0}     # pure [SU(3)]^3, the condition first omitted

def test_the_13_state_witness_FAILS_the_su3_cubed_anomaly():
    """The withdrawn counterexample. It satisfies the four conditions first imposed and
    FAILS the fifth, which is why the claim built on it is withdrawn."""
    comp = "ABCDD"
    ys = [F(1,2), F(-1), F(-3,2), F(2), F(1)]
    assert all(x == 0 for x in anomalies(comp, ys))      # the four I had
    assert sum(A3[r] for r in comp) == 1                 # the one I had not
    assert sum(A3[r] for r in "ABBCD") == 0              # the SM passes it

def test_su3_cubed_forces_two_antitriplets_per_quark_doublet():
    assert sum(A3[r] for r in "ABBCD") == 0
    assert sum(A3[r] for r in "ABCDD") != 0
    assert sum(A3[r] for r in "ABBBCD"[:5]) != 0

def test_b1160_core_reproduced_exactly():
    c = R["b1160_core_reproduced"]
    assert "-18(t-3)(t+3)" in c["cubic"] and "matches exactly" in c["cubic"]
    assert "CORRECT as stated" in c["verdict"]

def test_the_hidden_vector_like_branch_is_recorded():
    s = R["scope_finding_1_the_hidden_branch"]
    assert "THREE branches" in s["result"] and "VECTOR-LIKE" in s["result"]
    assert "B864" in s["corroboration"]
    assert s["is_it_damaging"].startswith("NO")

def test_the_withdrawal_is_recorded_with_its_severity():
    c = R["CORRECTION_the_13_state_witness_is_DEAD"]
    assert "OMITTED THE PURE [SU(3)]^3" in c["what_I_got_wrong"]
    assert "IS WITHDRAWN" in c["the_consequence"]
    assert "REVERSES" in c["severity"]

def test_the_corrected_result_and_its_honest_robustness():
    c = R["CORRECTED_RESULT"]
    assert "EXACTLY TWO" in c["over_the_SM_visible_alphabet"]["survivors"]
    assert c["over_the_SM_visible_alphabet"]["killed_by_SU3_cubed_alone"] == 222
    assert "UNIQUENESS IS ALPHABET-DEPENDENT" in c["robustness"]["honest_summary"]
    assert "MINIMALITY IS ROBUST" in c["robustness"]["honest_summary"]
    assert "STRENGTHENS B1160" in c["what_this_means_for_B1160"]

def test_all_of_my_instrument_errors_are_recorded():
    e = R["my_own_two_instrument_errors"]
    assert "RIGIDITY, not existence" in e["first"]
    assert "NEUTRAL (3,2)" in e["second"]
    assert "MISSING EQUATION" in e["fourth_and_worst"]

def test_the_decisive_question_is_posed_and_not_answered():
    q = R["the_decisive_open_question"]
    assert "realisable inside the object's 27" in q["statement"]
    assert "not done" in q["not_attempted_here"]


def test_the_forcing_is_generic_not_object_specific():
    g = R["step6_how_much_is_object_specific"]
    assert g["object_tokens_in_executable_code"].startswith("NONE")
    assert "ARENA" in g["conclusion"] and "CONTENT" in g["conclusion"]
    assert "not evidence FOR the object" in g["why_it_matters"]

def test_the_one_prose_hit_is_disclosed_not_swept():
    g = R["step6_how_much_is_object_specific"]
    assert "COMMENT" in g["the_one_prose_hit"]
    assert "my own control fired on it" in g["the_one_prose_hit"]

def test_no_novelty_is_claimed_for_the_uniqueness():
    assert R["step6_how_much_is_object_specific"]["novelty"].startswith("NONE CLAIMED")
