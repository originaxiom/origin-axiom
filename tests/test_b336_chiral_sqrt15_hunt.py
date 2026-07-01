"""B336 -- the chiral sqrt(-15) hunt (Chat-1 insight, probed). sympy-only + recorded SnapPy values."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B336_chiral_sqrt15_hunt'))
from chiral_sqrt15_hunt import (jones_at_zeta15_is_real, monodromy_discs, minus15_reachable_by_monodromy,
                                chiral_fillings_are_chiral, commensurables_share_sqrt_minus3)


def test_A1_jones_at_zeta15_is_real():
    assert jones_at_zeta15_is_real()          # amphichiral object -> zero sqrt(-15) component


def test_A2_monodromy_never_reaches_minus15():
    assert not minus15_reachable_by_monodromy()          # {t^2-4} never = -15
    assert -15 not in monodromy_discs(30)
    assert 5 in monodromy_discs() and 117 in monodromy_discs()   # but the metallic discs 5,117 are there


def test_A2_commensurables_and_fillings():
    assert commensurables_share_sqrt_minus3()   # class = Q(sqrt-3) != Q(sqrt-15); route closed
    assert chiral_fillings_are_chiral()          # fillings do break amphichirality (CS != 0)...
    # ...but generically non-arithmetic -> not Q(sqrt-15) (Sage-checkable exception; generic no)
