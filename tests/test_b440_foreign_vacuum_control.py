"""Locks for B440 (C3 foreign control) -- CORRECTED after adversarial review.
The golden factor is REDUCIBLE (abelian Z/5 chars, universal); 4_1 and 5_2 both have 4
irreducible vacua in the same -283 field. The 'golden inversion' was retracted as an artifact."""
import os, sys
HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B440_foreign_vacuum_control")
sys.path.insert(0, HERE)
import verify as V


def test_irreducible_vacuum_counts():
    counts = {k: V.irreducible_split(k)[0] for k in V.DATA}
    assert counts == {"4_1(5,1)": 4, "5_2(5,1)": 4, "6_1(5,1)": 11, "3_1(5,1)": 5}


def test_child_charvar_cross_validates_b439():
    # closed-manifold character variety == B439 Cooper-Long A-poly quartic (independent methods)
    assert V.child_charvar_matches_b439()


def test_child_and_neighbour_share_irreducible_neg283_field():
    # 4_1 and 5_2: SAME irreducible count (4) AND same -283 field -- commensurability-shared
    assert V.irreducible_split("4_1(5,1)")[0] == V.irreducible_split("5_2(5,1)")[0] == 4
    assert V.neg283_field_shared()


def test_golden_characters_are_reducible_and_universal():
    # the retraction: golden Q(sqrt5) chars are REDUCIBLE abelian Z/5, present for ALL K(5,1)
    assert V.golden_abelian_is_universal()
    assert V.irreducible_split("5_2(5,1)")[1] == 2   # 5_2's golden factor counted as reducible
