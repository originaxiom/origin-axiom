"""Locks for B411 -- the boundary/generic field-dictionary split."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B411_field_dictionary")
D = json.load(open(os.path.join(HERE, "dictionary.json")))


def test_boundary_determined_generic_not():
    # boundary classes (a nonzero chi is 0 => det shares a factor) are single-valued
    assert len(D["(0, -1, 5)".replace("(0, -1, 5)", "(0, -1, 3)")]) == 1  # gcd-3 boundary
    assert len(D["(0, 0, 15)"]) == 1                                       # gcd-15 boundary
    # generic class-1 (both chars nonzero) is multi-valued
    assert len(D["(-1, -1, 1)"]) > 1 and len(D["(1, 1, 1)"]) > 1
