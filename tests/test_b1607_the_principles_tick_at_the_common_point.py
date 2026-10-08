"""B1607 -- THE PRINCIPLE'S TICK AT THE COMMON POINT: the rule's matrix, lift and parity action as recorded; the two hands;
the sealed instrument unchanged; the post-seal letter; GENESIS v1.29 carries the ruling."""
import hashlib, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1607_the_principles_tick_at_the_common_point"
V = ARC / "verification"


def test_the_sealed_instrument_is_unchanged():
    sealed = open(ARC / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert sealed.startswith("# sealed at 805e2d488: ")
    sha = sealed.split()[4]
    assert hashlib.sha256(open(V / "principle_tick.py", "rb").read()).hexdigest() == sha


def test_c1_the_rule_is_the_golden_matrix_and_the_gieseking():
    d = json.load(open(V / "principle_tick.json"))["C1"]
    assert [[int(x) for x in r] for r in d["sigma_matrix"]] == [[1, 1], [1, 0]] and d["det"] == -1   # sympy ints are stored as strings
    assert d["sigma_squared_matrix_equals_LR_matrix"] and d["sigma_squared_vs_LR_conjugator"] is not None
    assert d["mirror_rule_is_iota_sigma_iota"]
    assert d["sigma_equals_P_after_R_exactly"] is False          # the sealed letter was wrong; see post_seal_lp.json
    p = json.load(open(V / "post_seal_lp.json"))
    assert p["sigma_equals_L_after_P"] and p["mirror_equals_P_after_R"] and p["which_compositions_equal_sigma"] == ["L∘P"]
    b = d["bundles"]
    for name in ("b-+L", "b--L", "b-+R", "b--R"):
        assert b[name]["orientable"] is False and b[name]["is_m000"] is True
    assert b["b++LR"]["is_m004"] is True and d["m004_volume_is_twice_m000"] and d["m000_orientable_double_cover_is_m004"] is True


def test_c2_the_lift_at_the_quaternion_point():
    d = json.load(open(V / "principle_tick.json"))["C2"]
    assert d["2T_elements"] == 24 and d["2O_elements"] == 48 and d["order6_in_2T"] == 8 and d["order6_2T_classes"] == [4, 4]
    rule = d["lifts"]["rule"]
    assert sorted(x["order"] for x in rule) == [3, 6] and all(x["in_2T"] for x in rule)
    assert any(x["coords"] == ["1/2", "-1/2", "-1/2", "-1/2"] for x in rule)
    assert all(x["axis_action"] == {"i": "+k", "j": "+i", "k": "+j"} for x in rule)
    assert d["order6_class_of"]["rule"] == d["order6_class_of"]["mirror_rule"] != d["order6_class_of"]["inverse_rule"]
    assert d["k_conjugate_of_rule_lift"] in [x["coords"] for x in d["lifts"]["mirror_rule"]]
    assert d["L_lift_conjugates_rule_lift_to_class"] != d["rule_lift_class"] and d["R_lift_conjugates_rule_lift_to_class"] != d["rule_lift_class"]
    assert all(x["order"] == 8 and not x["in_2T"] for nm in ("L", "R") for x in d["lifts"][nm])


def test_c3_the_parities_and_the_sense():
    d = json.load(open(V / "principle_tick.json"))["C3"]
    m = d["moves"]
    assert all(m[k]["type"] == "transposition" for k in ("L", "R", "P"))
    assert m["sigma"]["type"] == "3-cycle" and m["sigma_squared"]["sense"] == m["LR"]["sense"] == m["sigma_inverse"]["sense"] != m["sigma"]["sense"]
    assert m["mirror_rule"]["sense"] == m["sigma"]["sense"]
    assert d["odd_trace_words_to_8"] == 30 and d["every_odd_trace_word_a_3_cycle"] and d["every_odd_trace_word_even_length"]
    assert d["sense_constant_on_even_rotations"] and d["sense_inverted_on_odd_rotations"] and d["sense_a_thread_invariant"] is False
    assert d["mirror_keeps_sense"] and d["reverse_inverts_sense"]
    assert d["lift_test_orientations_of_the_parity_triangle"] == [-1, 1] and d["oriented_fibre_orients_the_parity_triangle"] is False


def test_genesis_carries_the_two_hands():
    g = open(ROOT / "GENESIS.md", encoding="utf-8").read()
    assert int(g.split("**Version 1.")[1].split()[0]) >= 29 and "THE PRINCIPLE'S TICK AT THE COMMON POINT (main, B1607" in g   # the version only moves forward; never pin the header
    assert "neither hand is derived on the weave" in g
