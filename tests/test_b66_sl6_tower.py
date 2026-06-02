"""Tests for B66: the SL(6) numerical fixed-line tower (35-dim).

Fast structural checks: the opposition-involution theta-split sector counts
(9 odd-height + 6 even-height + 5 parity = 35, validated across the tower; the
height-parity binning equals |k|-parity only for odd n), the Dickson
catalog Lucas coefficients, and that SL6_WORDS is a rank-35 coordinate set at a
generic representation. The full numerical spectrum and the |k|=3 multiplicity
result (= 2, refuting max(n-d,1)) live in FINDINGS.md and are reproduced by
probe.py (~30 min, too slow for the suite).
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
PROBE_PATH = ROOT / "frontier" / "B66_sl6_tower" / "probe.py"


def load_probe():
    spec = importlib.util.spec_from_file_location("b66_sl6_tower", PROBE_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_word_set_is_35_inverse_words():
    probe = load_probe()
    assert probe.DIM == 35
    assert len(probe.SL6_WORDS) == 35
    for w in probe.SL6_WORDS:
        assert 1 <= len(w) <= 5
        assert set(w) <= set("ABab")  # words in {A,B,A^-1,B^-1}


def test_theta_split_sector_prediction_is_9_6_5():
    probe = load_probe()
    assert probe.sector_prediction(6) == (9, 6, 5)  # odd-height, even-height quads, parity


def test_theta_split_totals_match_dim_across_tower():
    probe = load_probe()
    for n, dim in [(3, 8), (4, 15), (5, 24), (6, 35)]:  # n^2 - 1
        oq, eq, par = probe.sector_prediction(n)
        assert 2 * (oq + eq) + par == dim


def test_theta_split_height_space_dimensions():
    probe = load_probe()
    # the height-h root space of A_{n-1} has 2(n-h) roots -> (n-h) quadratics
    for n in (5, 6):
        for h in range(1, n):
            dim, _, _ = probe.theta_split(n, h)
            assert dim == 2 * (n - h)


def test_dickson_lucas_coefficients():
    probe = load_probe()
    L = probe._lucas(6)
    assert (L[2], L[3], L[4], L[5]) == (3, 4, 7, 11)  # Fibonacci-Lucas tr(M^k)
    assert L[-1] == -1  # tr(M^-1), M = [[1,1],[1,0]]


def test_sl2_parity_factor_is_t_plus_1():
    """The n=2 row: the SL(2) identity-fixed-point trace-map Jacobian factors as
    (t+1)*char(M^2) for all m -- the parity eigenvalue is det(M) = -1, so the
    factor is (t+1), NOT (t-1). (Coordinates x=trA, y=trB, z=trAB; p_k=tr(A^k B)
    with p_0=y, p_1=z, p_k = x p_{k-1} - p_{k-2}; substitution A->A^m B, B->A.)"""
    import sympy as sp

    x, y, z, t = sp.symbols("x y z t")
    for mval in range(1, 6):
        p = [y, z]
        for k in range(2, mval + 2):
            p.append(sp.expand(x * p[-1] - p[-2]))
        T = [p[mval], x, p[mval + 1]]  # x'=tr(A^m B), y'=tr A, z'=tr(A^{m+1}B)
        J = sp.Matrix([[sp.diff(Ti, v) for v in (x, y, z)] for Ti in T]).subs({x: 2, y: 2, z: 2})
        cp = sp.expand(J.charpoly(t).as_expr())
        expected = sp.expand((t + 1) * (t**2 - (mval**2 + 2) * t + 1))  # (t+1)*char(M^2)
        assert sp.expand(cp - expected) == 0


def test_char_negMk_equals_char_Mminusk_for_odd_k_only():
    """char(-M^k) = char(M^{-k}) iff k is odd (det M = -1); independent confirmation
    of the B64 Dickson parity backbone L_k(-m) = (-1)^k L_k(m), checked through L_8."""
    import sympy as sp

    m, t = sp.symbols("m t")
    M = sp.Matrix([[m, 1], [1, 0]])
    for k in range(1, 9):
        Mk, Mnk = sp.simplify(M**k), sp.simplify(M ** (-k))
        char_negMk = sp.expand(t**2 + sp.trace(Mk) * t + Mk.det())     # char(-M^k)
        char_Mnegk = sp.expand(t**2 - sp.trace(Mnk) * t + Mnk.det())   # char(M^{-k})
        assert (sp.expand(char_negMk - char_Mnegk) == 0) == (k % 2 == 1)
        assert sp.expand(sp.trace((-M) ** k) - (-1) ** k * sp.trace(M**k)) == 0  # Dickson parity


def test_k3_catalog_roots():
    import mpmath as mp

    probe = load_probe()
    # char(M^3) = t^2 - 4t - 1 has roots 2 +- sqrt(5) (= 4.236, -0.236)
    roots = sorted(float(mp.re(x)) for x in probe._q(1, -4, -1))
    assert abs(roots[1] - float(2 + mp.sqrt(5))) < 1e-9
    assert abs(roots[0] - float(2 - mp.sqrt(5))) < 1e-9


def test_word_set_full_rank_35_at_generic_rep():
    """The 35 word-traces are functionally independent at a generic GL(6) point,
    so SL6_WORDS is a valid rank-35 coordinate set (rank drops only on the fixed
    line, which is the whole point of the numerical extrapolation)."""
    probe = load_probe()
    rng = np.random.default_rng(1)

    def rep():
        Z = rng.standard_normal((6, 6)) + 1j * rng.standard_normal((6, 6))
        return np.eye(6) + 0.5 * Z

    A, B = rep(), rep()
    Ai, Bi = np.linalg.inv(A), np.linalg.inv(B)

    def word(s, mm):
        R = np.eye(6, dtype=complex)
        for c in s:
            R = R @ mm[c]
        return R

    basis = []
    for i in range(6):
        for j in range(6):
            if i != j:
                e = np.zeros((6, 6), dtype=complex)
                e[i, j] = 1.0
                basis.append(e)
    for i in range(5):
        e = np.zeros((6, 6), dtype=complex)
        e[i, i], e[i + 1, i + 1] = 1.0, -1.0
        basis.append(e)
    assert len(basis) == 35  # dim sl(6)

    h = 1e-6
    J = np.zeros((35, 70), dtype=complex)
    col = 0
    for G in basis:  # perturb A along sl(6)
        Ap, Am = (np.eye(6) + h * G) @ A, (np.eye(6) - h * G) @ A
        mp_ = {"A": Ap, "B": B, "a": np.linalg.inv(Ap), "b": Bi}
        mm_ = {"A": Am, "B": B, "a": np.linalg.inv(Am), "b": Bi}
        for r, s in enumerate(probe.SL6_WORDS):
            J[r, col] = (np.trace(word(s, mp_)) - np.trace(word(s, mm_))) / (2 * h)
        col += 1
    for G in basis:  # perturb B along sl(6)
        Bp, Bm = (np.eye(6) + h * G) @ B, (np.eye(6) - h * G) @ B
        mp_ = {"A": A, "B": Bp, "a": Ai, "b": np.linalg.inv(Bp)}
        mm_ = {"A": A, "B": Bm, "a": Ai, "b": np.linalg.inv(Bm)}
        for r, s in enumerate(probe.SL6_WORDS):
            J[r, col] = (np.trace(word(s, mp_)) - np.trace(word(s, mm_))) / (2 * h)
        col += 1

    assert np.linalg.matrix_rank(J, tol=1e-2) == 35
