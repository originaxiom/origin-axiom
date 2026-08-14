"""Locks B886 -- the matter pencil and the two laws as theorems."""
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B886_matter_pencil"
S1 = json.loads((_D / "results_stage1.json").read_text(encoding="utf-8"))
S2 = json.loads((_D / "results_stage2.json").read_text(encoding="utf-8"))
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split()).lower().replace("*", "")


def test_the_factorization():
    fs = S1["factor_structure"]
    assert sorted((f["mult"], f["deg_x"]) for f in fs) == [(1, 3), (8, 3)]


def test_the_collision_structure_at_roots():
    assert sorted(map(tuple, S1["spec_structure"])) == [(1, 1), (10, 1), (16, 1)]


def test_the_equivariant_design():
    lones = [c["lone_w"] for c in S2["collisions"]]
    assert lones == [[2], [1], [0]]
    hits = [c["w_u_hits"] for c in S2["collisions"]]
    assert hits[0] == [[0], [0], []]
    assert hits[1] == [[1], [], [1]]
    assert hits[2] == [[], [2], [2]]


def test_law1_and_law2_are_theorems():
    assert S2["law1_all"] is True
    assert len(S2["law1"]) == 6
    assert S2["law2_all"] is True


def test_the_two_cubic_fields():
    assert S2["fields_match_K"] == [False, True]
    assert "a second cubic field" in _F
    assert "brand-new arithmetic invariant" in _F


def test_scope():
    assert "everything here is exact" in _F
    assert "no physics reading" in _F
