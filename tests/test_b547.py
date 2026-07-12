"""Locks for B547 — the ghost scanner."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier',
                                'B547_ghost_scanner'))
from scanner import classify, slot_realizable, all_hyperbolic


def test_markov_triples_realize():
    for tri in [(3, 3, 3), (3, 3, 6), (3, 6, 15)]:
        assert classify(*tri)[0] == 'REALIZED'


def test_4_4_16_is_proved_all_hyperbolic_ghost():
    v, t = classify(4, 4, 16)
    assert v == 'GHOST(proved)'
    assert all_hyperbolic(4, 4, 16)          # every coord hyperbolic
    assert not slot_realizable(4, 4, 16)     # the inert-prime slot fails
    assert not slot_realizable(4, 16, 4)


def test_inert_prime_obstruction():
    """u^2 - 3v^2 = 7 has no solution (7 inert in Q(sqrt3))."""
    assert not any(u*u - 3*v*v == 7
                   for u in range(-300, 301) for v in range(-300, 301))


def test_small_ghosts_confirmed():
    assert classify(1, 0, 0)[0] == 'GHOST(proved)'      # c=1
    assert classify(1, 1, 5)[0] == 'GHOST(proved)'      # c=22
    assert classify(4, 16, 60)[0] == 'GHOST(proved)'    # c=32, all-hyperbolic
