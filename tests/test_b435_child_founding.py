"""Locks for B435 -- the Child Program founding facts."""
import os, sys
HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B435_child_founding")
sys.path.insert(0, HERE)
import founding as F


def test_kac_count_and_free_rotation():
    sols = F.kac_solutions(5)
    assert len(sols) == 75
    n_orb, n_fix = F.orbits_mod_rotation(sols)
    assert n_fix == 0                    # 3 does not divide 5: no rotation-fixed solutions
    assert n_orb == 25 == 5**2           # the abelian E6 vacua of the child

def test_s3_refinement():
    assert F.orbits_mod_S3(F.kac_solutions(5)) == 17

def test_control_sibling_counts_differ():
    # the UNFORCED sibling 4_1(7,1) has H1 = Z/7: its abelian vacuum count differs
    sols7 = F.kac_solutions(7)
    n7, f7 = F.orbits_mod_rotation(sols7)
    assert (len(sols7), n7) != (75, 25)  # control leg: the child's count is slope-specific
