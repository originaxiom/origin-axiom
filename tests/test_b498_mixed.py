"""B498 locks — mixed words in the monoid (C1, Q1, C2 depth-2)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "frontier", "B498_mixed_monoid_dynamics"))
import verify_mixed as V


def test_c1_classification():
    na, nc, fach = V.c1_classification()
    assert (na, nc) == (15, 24) and fach == ['MFM']


def test_c1_lemma_and_control():
    assert V.c1_lemma_MS() and V.c1_mirror_closure()


def test_q1a_minus_two():
    assert V.q1a_per_factor()


def test_q1b_reduction():
    assert V.q1b_reduction_identity()


def test_c2_depth2_monopoly():
    ok, levels = V.c2_depth2()
    assert ok
    # the correction: the (1+-3sqrt5)/8 levels are present (DD) - Q(sqrt5) but not Z[phi]
    import sympy as sp
    from sympy import sqrt, Rational
    assert sp.nsimplify(Rational(1,8) + 3*sqrt(5)/8, [sqrt(5)]) in levels


def test_c2_D_line():
    assert V.c2_D_line()


def test_q1b_hand_proof():
    assert V.q1b_hand_proof_steps()
