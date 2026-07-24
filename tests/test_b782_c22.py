"""B782 -- C22: the choice-incomputability wall (free torsor has no equivariant section)."""
import itertools
import json
import pathlib

ARC = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B782_choice_incomputability"


def test_closing_action_is_free_no_equivariant_section():
    G = list(itertools.product([0, 1], repeat=3))       # (Z/2)^3 = (c, theta, gamma5)
    torsor = list(itertools.product([0, 1], repeat=3))    # the 8 closings
    act = lambda g, x: tuple(a ^ b for a, b in zip(g, x))
    # free: no non-identity element fixes any closing
    assert all(act(g, x) != x for g in G if g != (0, 0, 0) for x in torsor)
    # transitive: a torsor
    assert all(any(act(g, x) == y for g in G) for x in torsor for y in torsor)
    # no G-fixed closing == no equivariant section
    assert [x for x in torsor if all(act(g, x) == x for g in G)] == []


def test_c22_banked():
    d = json.loads((ARC / "results.json").read_text())
    assert d["chain_link"] == "C22" and d["verdict"] == "RESOLVED-A"
    assert d["action_free"] and d["no_equivariant_section"]
