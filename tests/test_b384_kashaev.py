"""Locks for B384 T1 -- exact Kashaev Galois components."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B384_kashaev_bridge")
R = json.load(open(os.path.join(HERE, "kashaev.json")))


def test_n5_exact_golden_value():
    assert R["5"]["rational_part"] == "46" and R["5"]["sqrt5_part"] == "2"


def test_sqrt5_content_at_every_5N_level():
    for N in ("5", "15", "25", "45", "135"):
        assert R[N]["sqrt5_part"] not in (None, "0")


def test_no_sqrt5_subfield_elsewhere():
    for N in ("7", "9", "27", "81"):
        assert R[N]["sqrt5_part"] is None


def test_scaling_gate_decreasing():
    gs = [R[N]["growth"] for N in ("5", "9", "15", "27", "45", "81", "135")]
    assert all(a > b for a, b in zip(gs, gs[1:]))


T2 = json.load(open(os.path.join(HERE, "t2_level15_singles.json")))
SW = json.load(open(os.path.join(
    HERE, "..", "B372_level45_sweeper", "sweep45.json")))


def test_t2_m1_identity_transport():
    assert set(T2["m1_ord20"]) == {"1", "6", "11", "16"}
    assert all(v[0] == "1/4" and v[1:] == ["0", "0", "0"]
               for v in T2["m1_ord20"].values())
    assert set(SW["singles1"]) == {"1", "16", "31", "46"}
    assert all(v[0] == "1/4" and all(x == "0" for x in v[1:])
               for v in SW["singles1"].values())


def test_t2_m2_level15_values():
    assert T2["m2_ord12"]["0"] == ["1/12", "1/12", "0", "0"]
    assert T2["m2_ord12"]["2"] == ["1/8", "0", "0", "0"]
    assert "6" not in T2["m2_ord12"]


T3 = json.load(open(os.path.join(HERE, "t3_block.json")))


def test_t3_gauss_sum_is_seam_radical():
    assert T3["gauss15"] == ["0", "0", "0", "1"]


def test_t3_triangular_S_on_slot():
    assert T3["F"]["6,14"]["HAvg"] == ["0", "0", "0", "0"]
    assert T3["F"]["14,6"]["HAvg"] != ["0", "0", "0", "0"]
    assert all(v["proportional"] is True for v in T3["F"].values())


def test_t3_diagonal_entries_exact():
    assert T3["F"]["6,6"]["HAvg"] == ["0", "-3/8", "0", "1/8"]
    assert T3["F"]["14,14"]["HAvg"] == ["15/32", "-3/32", "-5/32", "1/32"]
