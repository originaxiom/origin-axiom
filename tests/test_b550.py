"""Locks for B550 — the Promotion-Sign Conjecture refutation."""
import math

TOWER_EXACT = {3: (0, 1), 4: (1, 1)}   # B111 locked: (char(+M^1), char(-M^1)) at height 1


def _closed_h1(n):
    return (math.ceil((n-1)/2), math.floor((n-1)/2))


def _conjecture(n):
    p, m = _closed_h1(n)
    return (p, m-1) if n % 2 else (p-1, m)


def _meridian(n):
    p, m = _closed_h1(n)
    return (p-1, m)


def test_conjecture_refuted_at_n3():
    assert _conjecture(3) != TOWER_EXACT[3]
    assert _conjecture(3) == (1, 0) and TOWER_EXACT[3] == (0, 1)


def test_meridian_rule_reproduces_exact():
    for n in (3, 4):
        assert _meridian(n) == TOWER_EXACT[n]


def test_n6_does_not_discriminate():
    assert _conjecture(6) == _meridian(6) == (2, 2)


def test_n5_discriminating_prediction():
    assert _meridian(5) == (1, 2)
    assert _conjecture(5) == (2, 1)
