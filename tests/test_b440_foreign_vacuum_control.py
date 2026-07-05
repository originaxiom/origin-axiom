"""Locks for B440 (C3 foreign control) -- the SL(2,C) vacuum spectra of K(5,1)."""
import os, sys
HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B440_foreign_vacuum_control")
sys.path.insert(0, HERE)
import verify as V


def test_vacuum_counts():
    assert {k: V.DATA[k]["total_vacua"] for k in V.DATA} == \
        {"4_1(5,1)": 4, "5_2(5,1)": 6, "6_1(5,1)": 11, "3_1(5,1)": 5}


def test_child_charvar_cross_validates_b439():
    # closed-manifold character variety == B439 Cooper-Long A-poly quartic (independent methods)
    assert V.child_charvar_matches_b439()


def test_neg283_field_is_commensurability_shared():
    assert V.neg283_field_shared()


def test_golden_vacua_only_in_foreign_neighbour():
    # the golden Q(sqrt5) vacua are in 5_2's child, NOT in the golden parent's own child
    assert V.golden_vacua_only_in_5_2()
