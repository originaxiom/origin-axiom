"""Locks for B385 T1 -- the double kill."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier",
                    "B385_bright_dark_discriminator")
GH = json.load(open(os.path.join(HERE, "group_hunt.json")))
CC = json.load(open(os.path.join(HERE, "class_counts.json")))


def test_kill1_no_group_separator():
    assert GH["separators"] == []


def test_kill1_riddle_profiles_identical():
    a, b = GH["table"]["2,3"], GH["table"]["1,3"]
    for n in ("15", "3", "5"):
        assert a[n]["order"] == b[n]["order"]
        assert a[n]["det_classes"] == b[n]["det_classes"]


def test_kill2_word_map_fails_on_riddle():
    assert CC["separates"] is False
    assert CC["res"]["3,4"]["counts"] == CC["res"]["1,3"]["counts"] == {
        "1": 63, "3": 21, "5": 27, "15": 9}


def test_b382_profile_is_shared_by_two_pairs():
    assert CC["res"]["1,2"]["counts"] == CC["res"]["2,4"]["counts"] == {
        "1": 142, "3": 26, "5": 68, "15": 4}


VW = json.load(open(os.path.join(HERE, "vword.json")))


def test_vword_riddle_pair_separates():
    assert VW["3,4"]["nsupport"] == 12 and VW["1,3"]["nsupport"] == 18
    assert VW["3,4"]["support"] != VW["1,3"]["support"]


def test_vword_support_sets_disjoint_bright_dark():
    b = {tuple(map(tuple, VW[k]["support"])) for k in VW
         if VW[k]["status"] == "bright"}
    d = {tuple(map(tuple, VW[k]["support"])) for k in VW
         if VW[k]["status"] == "dark"}
    assert not (b & d)


AC = json.load(open(os.path.join(HERE, "anti_correlation.json")))


def test_dark_cells_are_not_anti_free():
    assert AC["nb"] == 44 and AC["nd"] == 44


def test_bright_exclusive_labels():
    assert sorted(map(str, AC["missed"])) == sorted(map(str, [
        [1, [0, 2]], [1, [2, 1]], [1, [2, 3]], [1, [4, 2]]]))
