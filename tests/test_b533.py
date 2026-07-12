"""Locks for B533 — Coupling Invariance.

Gate 1: the object has 5 stable observation types with universal
eigenvalue spectrum but observation-dependent Perron eigenvectors.
"""

import sys
import os
import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier',
                                'B530_natural_history'))
from listen_39_induction_engine import (
    grow, factor_position_map, standard_return_words_from_positions,
    canonical_induced_system, original_matrix, canonical_codes,
)

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
SIGMA_CODES = ((0, 1, 2, 2, 3), (0, 2, 3), (0, 1, 2, 3), (0, 2))
SIGMA_CANONICAL = canonical_codes(SIGMA_CODES)

PHI = (1 + np.sqrt(5)) / 2
SQ_PHI = np.sqrt(PHI)
S = PHI + 1 + PHI * SQ_PHI + SQ_PHI
FREQ = {'a': PHI/S, 'b': 1/S, 'A': PHI*SQ_PHI/S, 'B': SQ_PHI/S}
BETA = 3.676205


@pytest.fixture(scope='module')
def host():
    return grow(10)


def _analyze(factor, host):
    fpm = factor_position_map(host, len(factor))
    if factor not in fpm:
        return None
    positions = fpm[factor]
    if len(positions) < 6:
        return None
    rws = standard_return_words_from_positions(host, positions)
    ind = canonical_induced_system(rws, max_power=2)
    if ind is None:
        return None
    M = np.array(ind['matrix'].tolist(), dtype=float)
    eigs, vecs = np.linalg.eig(M)
    idx = np.argmax(np.abs(eigs.real))
    v = vecs[:, idx].real
    if np.any(v < 0):
        v = -v
    v = v / v.sum()
    return {
        'rws': rws, 'rc': len(rws), 'induced': ind,
        'eigs': np.sort(eigs.real)[::-1],
        'perron_vec': v, 'beta': eigs[idx].real,
        'is_self': ind['canonical_codes'] == SIGMA_CANONICAL,
    }


def _type_key(v, prec=4):
    return tuple(np.round(np.sort(v)[::-1], prec))


# ── S1: Eigenvalue universality ──

def test_eigenvalue_universality(host):
    """All rc=4 observation points share eigenvalues {beta, lambda2, lambda3, lambda4}."""
    M_orig = np.array(original_matrix().tolist(), dtype=float)
    expected = np.sort(np.linalg.eigvals(M_orig).real)[::-1]

    for factor in ['a', 'b', 'A', 'B', 'AB', 'Ba', 'Aa', 'bA', 'abA']:
        r = _analyze(factor, host)
        if r is None or r['rc'] != 4:
            continue
        assert np.allclose(r['eigs'][:4], expected, rtol=1e-3), \
            f"factor '{factor}': eigenvalues {r['eigs']} != {expected}"


def test_perron_eigenvalue_universal(host):
    """beta_u = beta for all observation points."""
    for factor in ['a', 'b', 'A', 'B', 'AB', 'Ba', 'aA', 'bAA', 'Bab']:
        r = _analyze(factor, host)
        if r is None:
            continue
        assert abs(r['beta'] - BETA) < 0.001, \
            f"factor '{factor}': beta={r['beta']} != {BETA}"


# ── S2: Five stable types ──

def test_five_types(host):
    """Length 1-3 factors produce exactly 5 distinct Perron-vector types."""
    types = set()
    for length in range(1, 4):
        fpm = factor_position_map(host, length)
        for factor in fpm:
            r = _analyze(factor, host)
            if r is None:
                continue
            types.add(_type_key(r['perron_vec']))
    assert len(types) == 5


def test_type_counts(host):
    """Type counts match: 9/7/2/2/1 for length 1-3."""
    from collections import Counter
    type_counter = Counter()
    for length in range(1, 4):
        fpm = factor_position_map(host, length)
        for factor in fpm:
            r = _analyze(factor, host)
            if r is None:
                continue
            type_counter[_type_key(r['perron_vec'])] += 1
    counts = sorted(type_counter.values(), reverse=True)
    assert counts == [9, 7, 2, 2, 1]


# ── S3: Type 1 = sigma ──

def test_type1_is_sigma(host):
    """Factor 'a' gives return words = sigma images, with self-recovery."""
    r = _analyze('a', host)
    assert r is not None
    assert r['is_self'], "factor 'a' should recover sigma's canonical codes"
    assert r['rc'] == 4
    rw_set = set(r['rws'])
    image_set = {SUB[g] for g in 'abAB'}
    assert rw_set == image_set, f"return words {rw_set} != sigma images {image_set}"


def test_type1_perron_is_letter_freq(host):
    """Type 1 sorted Perron vector equals the sorted global letter frequencies."""
    r = _analyze('a', host)
    v_sorted = np.sort(r['perron_vec'])[::-1]
    f_sorted = np.sort([FREQ[g] for g in 'abAB'])[::-1]
    assert np.allclose(v_sorted, f_sorted, atol=1e-4), \
        f"sorted Perron {v_sorted} != sorted freqs {f_sorted}"


# ── S4: Type 2 Z-mixing ──

def test_type2_z_mixing(host):
    """Type 2 Perron components are Z-combinations of letter frequencies."""
    r = _analyze('B', host)
    assert r is not None
    v = np.sort(r['perron_vec'])[::-1]
    f_a, f_b, f_A, f_B = FREQ['a'], FREQ['b'], FREQ['A'], FREQ['B']
    assert abs(v[0] - (f_a + f_b)) < 1e-3, f"v[0]={v[0]} != f_a+f_b={f_a+f_b}"
    assert abs(v[1] - f_a) < 1e-3, f"v[1]={v[1]} != f_a={f_a}"
    assert abs(v[2] - f_B) < 1e-3, f"v[2]={v[2]} != f_B={f_B}"
    assert abs(v[3] - (f_A - f_a)) < 1e-3, f"v[3]={v[3]} != f_A-f_a={f_A-f_a}"


# ── S5: Self-recovery pattern ──

def test_self_recovery_count(host):
    """Exactly 7 self-recovery points among length 1-4 factors."""
    self_count = 0
    for length in range(1, 5):
        fpm = factor_position_map(host, length)
        for factor in fpm:
            r = _analyze(factor, host)
            if r is not None and r['is_self']:
                self_count += 1
    assert self_count == 7


# ── S6: Q-conjugacy (same charpoly) ──

def test_same_charpoly(host):
    """All rc=4 induced matrices have the same charpoly."""
    import sympy as sp
    x = sp.Symbol('x')
    target = sp.factor(sp.Matrix(original_matrix()).charpoly(x).as_expr())

    for factor in ['a', 'B', 'A', 'Bab']:
        r = _analyze(factor, host)
        if r is None or r['rc'] != 4:
            continue
        cp = sp.factor(r['induced']['matrix'].charpoly(x).as_expr())
        assert cp == target, f"factor '{factor}': charpoly {cp} != {target}"


# ── S7: Type stability across depths ──

def test_type_stability_depth_8_vs_10():
    """Same 5 types at depth 8 as at depth 10."""
    types_8 = set()
    types_10 = set()
    for depth, type_set in [(8, types_8), (10, types_10)]:
        h = grow(depth)
        for length in range(1, 4):
            fpm = factor_position_map(h, length)
            for factor in fpm:
                r = _analyze(factor, h)
                if r is None:
                    continue
                type_set.add(_type_key(r['perron_vec']))
    assert types_8 == types_10


# ── S8: Pair-sum preservation ──

def test_pair_sum_t1_t2(host):
    """Type 1 → Type 2 preserves the pair sum f_A + f_b."""
    r1 = _analyze('a', host)
    r2 = _analyze('B', host)
    v1 = np.sort(r1['perron_vec'])[::-1]
    v2 = np.sort(r2['perron_vec'])[::-1]
    sum1 = v1[0] + v1[3]  # f_A + f_b
    sum2 = v2[0] + v2[3]
    assert abs(sum1 - sum2) < 1e-3, f"pair sum not preserved: {sum1} vs {sum2}"


def test_pair_sum_t1_t3(host):
    """Type 1 → Type 3 preserves the pair sum f_A + f_a = 1/phi."""
    r1 = _analyze('a', host)
    r3 = _analyze('A', host)
    v1 = np.sort(r1['perron_vec'])[::-1]
    v3 = np.sort(r3['perron_vec'])[::-1]
    sum1 = v1[0] + v1[1]  # f_A + f_a
    sum3 = v3[0] + v3[1]
    assert abs(sum1 - sum3) < 1e-3, f"pair sum not preserved: {sum1} vs {sum3}"
    assert abs(sum1 - 1/PHI) < 1e-3, f"pair sum {sum1} != 1/phi"
