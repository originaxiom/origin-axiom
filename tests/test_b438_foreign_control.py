"""Locks for B438 -- the foreign control: nothing about the child is figure-eight-unique."""
import os, sys
HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B438_foreign_control")
sys.path.insert(0, HERE)
import foreign_control as FC


def test_5_2_shares_the_child_field():
    assert FC.shares_child_field(-0.24812606280262192, -1.0339820609759678)   # 5_2(5,1) = x^4-x-1
    assert FC.shares_child_field(-0.24812606280262192, 1.0339820609759678)    # child itself


def test_generic_knots_differ():
    assert not FC.shares_child_field(-1.1835049885455573, 1.3443083489183951)  # 6_1(5,1)
    assert not FC.shares_child_field(-1.710222649301387, 0.2177674839366718)   # m007(5,1)


def test_torsion_value_shared_by_5_2_not_trefoil():
    import sympy as sp
    t = sp.Symbol('t')
    assert FC.total_torsion(2*t**2-3*t+2) == FC.total_torsion(t**2-3*t+1) == 121  # 5_2 == child
    assert FC.total_torsion(t**2-t+1) == 1                                        # trefoil differs
