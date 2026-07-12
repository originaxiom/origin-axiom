"""Locks for B558 — the three-level negative verification."""
import numpy as np

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
phi = (1 + np.sqrt(5)) / 2


def _word(n=40000):
    w = 'a'
    while len(w) < n:
        w = ''.join(SUB[c] for c in w)
    return w[:n]


def test_p5_is_17_affine_complexity():
    w = _word()
    p = [len(set(w[i:i+n] for i in range(len(w)-n))) for n in range(1, 8)]
    assert p[4] == 17                       # p(5) = 17
    for n in range(5, 8):                   # affine p(n) = 3n+2 for n>=5
        assert p[n-1] == 3*n + 2


def test_gap_label_is_1_over_phi_cubed_not_squared():
    """The 0.23607 near-miss is 1/phi^3 (= 2/phi mod 1), NOT 1/phi^2."""
    assert abs(1/phi**3 - 0.23607) < 1e-4
    assert abs(1/phi**2 - 0.38197) < 1e-4
    assert abs((2/phi) % 1 - 1/phi**3) < 1e-9


def test_weinberg_near_miss_is_2pct_not_significant():
    """1/phi^3 vs sin2W is 2.1% — a real but non-significant golden near-miss."""
    sin2w = 0.23122
    rel = abs(1/phi**3 - sin2w) / sin2w
    assert 0.015 < rel < 0.025            # ~2.1%, far from a match


def test_rational_vertex_frequencies():
    for img, denom in [('abAAB', 5), ('aAB', 3), ('abAB', 4), ('aA', 2)]:
        assert img.count('a') == 1 and len(img) == denom
