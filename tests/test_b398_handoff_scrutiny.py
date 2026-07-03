"""Locks for B398 S1-S4 -- the handoff scrutiny verdicts."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B398_handoff_scrutiny")
R = json.load(open(os.path.join(HERE, "s1_s2.json")))


def test_s1_doublet_and_f4_gram():
    assert R["S1_blocks"]["doublet_sigma"] == "1/24"
    assert R["S1_F4"]["ratio"] == "23/75"
    assert R["S1_F4"]["int480"] == {"norm": "98", "inner": "-52"}


def test_s1_fork_pinned():
    assert R["S1_fork"] == {"full_rational_ratio": "23/25",
                            "F4_restricted_ratio": "23/75"}


def test_s2_z3_exact_but_degenerate():
    assert R["S2_23"]["norms"] == ["1/6912"]
    assert R["S2_23"]["inners"] == ["-1/13824"]
    assert R["S2_23"]["eig_ratio_claim"] == "div0"


def test_s2_34_seven_five_from_full_gram():
    G = json.load(open(os.path.join(HERE, "s2_fullgram.json")))
    assert G["g34_ratio"] == "7/5" and G["g23_ratio"] == "1"


def test_s2_ranks():
    assert R["S2_ranks"] == {"1,2": 4, "2,3": 2, "2,4": 1, "3,4": 2,
                             "1,3": 0, "1,4": 0}


def test_s3_fibers_and_rectangles():
    S3 = json.load(open(os.path.join(HERE, "s3_tensor.json")))
    assert S3["fibers"] == {"0,0": 1, "1,1": 2, "1,3": 2, "2,2": 1,
                            "3,1": 2, "3,3": 2}
    assert S3["rect"] == [168, 265]


def test_s5_gate_verdict():
    S5 = json.load(open(os.path.join(HERE, "s5_statistics.json")))
    e = S5["_ensemble"]
    assert e["space_size"] == 5964
    assert S5["pmns_s12"]["hits_1sigma"] == 139
    assert e["p_combined_family_corrected"] > 0.01   # the binding rule: ensemble killed
