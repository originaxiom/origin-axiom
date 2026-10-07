"""B1600 -- THE WEAVE VERIFIED: W1, the parity lemma, W2 and W3 as main's instrument recorded them."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1600_the_weave_verified" / "verification"


def test_w1_w2_w3_as_recorded():
    d = json.load(open(HERE / "weave_verify.json"))
    assert d["W1"]["L"] == [[1, 0]] and d["W1"]["R"] == [[0, 1]] and d["W1"]["P"] == [[1, 1]] and len(d["W1"]["minus_I"]) == 3 and d["W1"]["any_two_cycle_all_three"]
    assert d["parity_lemma"]["holds"] and d["parity_lemma"]["words"] == 988 and d["parity_lemma"]["odd"] == 448
    assert d["W2"]["parabolic_common_fixed_points"] == [{"x": "0", "y": "0", "z": "0"}] and len(d["W2"]["all_levels"]) == 2
    assert d["W3"]["odd_words"] == 54 and d["W3"]["odd_all_2T"] and d["W3"]["even_images"] == [8] and d["W3"]["even_without_tau_in_2T"] == 36


def test_every_arc_from_b1491_carries_the_weave_or_thread_label():
    import glob
    for a in ("B1491", "B1492", "B1493", "B1494", "B1495", "B1496", "B1497", "B1498", "B1499", "B1600"):
        f = glob.glob(str(HERE.parents[1] / f"{a}_*" / "arc_verdict.json"))[0]; v = json.load(open(f)); assert v.get("weave_or_thread")
    assert json.load(open(HERE.parent / "arc_verdict.json"))["weave_or_thread"] == "weave"
