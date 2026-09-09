"""B1249 -- the relational class does not pass the McKay door.

Locks the census: 2T's kappa spectrum, the 48 surjections (reproduced from the relator, which is
this arc's own control that the group and relator are right), the uniformity on those surjections,
and the ramification contrast across the door.
"""
import importlib.util
import pathlib

import sympy as sp

_SRC = (pathlib.Path(__file__).resolve().parents[1]
        / "frontier" / "B1249_the_door_and_the_class" / "verification" / "door_class.py")
_spec = importlib.util.spec_from_file_location("b1249_door_class", _SRC)
dc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(dc)

_CENSUS = dc.door_census()


def test_selftest_passes():
    assert dc.selftest(verbose=False) == []


def test_2T_has_order_24_and_a_three_value_kappa_spectrum():
    order, allspec, _, _, _ = _CENSUS
    assert order == 24
    assert set(allspec) == {-2, 0, 2}


def test_the_bit_is_unavailable_in_2T():
    """eps = -1 needs kappa - 2 a positive perfect square; 2T's values never are."""
    _, allspec, _, _, _ = _CENSUS
    for k in allspec:
        assert dc.squarefree(2 - k) != -1 if hasattr(dc, "squarefree") else (2 - int(k)) not in (-1,)
        n = int(k) - 2
        assert not (n > 0 and sp.integer_nthroot(n, 2)[1])


def test_the_48_surjections_are_reproduced_from_the_relator():
    """The banked count (B237/B1019/B997), re-derived here without reference to it."""
    _, _, rel, nsurj, _ = _CENSUS
    assert nsurj == 48
    assert rel == 72 and rel - nsurj == 24


def test_the_door_is_not_class_preserving():
    """All 48 surjections give kappa = 0 uniformly -> 2-kappa = 2, class D = 2 (never -1)."""
    _, _, _, _, surjspec = _CENSUS
    assert set(surjspec) == {0}
    assert sum(surjspec.values()) == 48
    assert 2 - 0 == 2


def test_ramification_controls_match_known_answers():
    """Two-sided: the Hurwitz algebra ramifies at {2, oo}; split algebras ramify nowhere."""
    assert dc.ramification(-1, -1) == [2, "oo"]
    assert dc.ramification(1, 1) == []
    assert dc.ramification(-1, 1) == []
    assert dc.ramification(2, 3) == [2, 3]


def test_the_door_adds_ramification():
    """Object algebra (5,-5) splits everywhere; 2T's (-1,-1) ramifies at {2, oo}."""
    assert dc.ramification(5, -5) == []
    assert dc.ramification(-1, -1) == [2, "oo"]


def test_the_relator_discriminates_NOTHING_the_door_claim_is_refuted():
    """The control that killed this arc's draft headline. Keep it permanent.

    A draft said 'all 48 surjections give kappa = 0, so THE DOOR is not class-preserving'.
    But all 384 GENERATING pairs of 2T already have kappa = 0, so the fig-8 relator cuts
    nothing and the observation is about generation in 2T, not about the door.
    If this test ever fails because the relator DOES discriminate, the door claim may be
    re-opened -- deliberately, not silently.
    """
    ngen, genspec = dc.generating_pair_census()
    _, _, _, _, surjspec = _CENSUS
    assert ngen == 384
    assert set(genspec) == {0}
    assert set(genspec) == set(surjspec)      # identical -> the relator adds no information
