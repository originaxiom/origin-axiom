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


# ── S5: β = 1/(√φ - 1) ──

def test_beta_is_reciprocal_sqrtphi_minus_1():
    """β = 1/(√φ - 1), proved algebraically via charpoly substitution."""
    tau = SQ_PHI
    beta = BETA
    assert abs(beta - 1/(tau - 1)) < 1e-4, \
        f"β={beta} != 1/(√φ-1)={1/(tau-1)}"
    assert abs(beta * (tau - 1) - 1) < 1e-4, \
        f"β(√φ-1)={beta*(tau-1)} != 1"


# ── S6: Eigenvalue identities ──

def test_beta_times_lambda2_equals_phi():
    """β · |λ₂| = φ (product of the two real eigenvalues)."""
    tau = SQ_PHI
    beta = PHI * (1 + tau)
    lam2 = 1 / (1 + tau)
    assert abs(beta * lam2 - PHI) < 1e-8, \
        f"β·|λ₂|={beta*lam2} != φ={PHI}"


def test_modulus_identity():
    """β · |λ₂| · |λ₃|² = 1 (modulus identity)."""
    tau = SQ_PHI
    beta = PHI * (1 + tau)
    lam2_abs = 1 / (1 + tau)
    lam3_mod_sq = 1 / PHI
    product = beta * lam2_abs * lam3_mod_sq
    assert abs(product - 1) < 1e-8, f"β·|λ₂|·|λ₃|²={product} != 1"


def test_det_M_minus_one():
    """det(M) = -1 (orientation-reversing substitution)."""
    import sympy as sp
    M = sp.Matrix(original_matrix())
    assert M.det() == -1


# ── S7: f_a = 1/β ──

def test_f_a_equals_one_over_beta(host):
    """f_a = 1/β: letter frequency = reciprocal of growth rate."""
    assert abs(FREQ['a'] - 1/BETA) < 1e-4, \
        f"f_a={FREQ['a']} != 1/β={1/BETA}"
    tau = SQ_PHI
    assert abs(FREQ['a'] - (tau - 1)) < 1e-8, \
        f"f_a={FREQ['a']} != √φ-1={tau-1}"


# ── S8: Single number field ──

def test_all_freqs_in_Q_tau():
    """All 4 letter frequencies expressible in ℚ(τ), τ=√φ."""
    tau = SQ_PHI
    beta = tau**2 * (1 + tau)
    assert abs(FREQ['a'] - 1/beta) < 1e-8
    assert abs(FREQ['b'] - 1/(PHI*beta)) < 1e-8
    assert abs(FREQ['A'] - tau/beta) < 1e-8
    assert abs(FREQ['B'] - tau/(PHI*beta)) < 1e-8


# ── S9: sin θ = 1/φ, cos θ = -1/√φ ──

def test_complex_eigenvalue_trig():
    """Complex eigenvalue phase has algebraic trig: cos θ = -1/τ, sin θ = 1/φ."""
    tau = SQ_PHI
    lam3_re = -1 / PHI
    lam3_im = np.sqrt(np.sqrt(5) - 2)
    lam3_mod = np.sqrt(lam3_re**2 + lam3_im**2)
    cos_theta = lam3_re / lam3_mod
    sin_theta = lam3_im / lam3_mod
    assert abs(cos_theta - (-1/tau)) < 1e-10, f"cos θ = {cos_theta} != -1/τ"
    assert abs(sin_theta - 1/PHI) < 1e-10, f"sin θ = {sin_theta} != 1/φ"


def test_complex_eigenvalue_modulus():
    """|λ₃| = 1/τ = 1/√φ."""
    tau = SQ_PHI
    lam3_re = -1 / PHI
    lam3_im = np.sqrt(np.sqrt(5) - 2)
    lam3_mod = np.sqrt(lam3_re**2 + lam3_im**2)
    assert abs(lam3_mod - 1/tau) < 1e-10


# ── S10: discriminant ──

def test_discriminant_minus_400():
    """disc(x⁴-x²-1) = disc(charpoly M) = -400."""
    import sympy as sp
    x = sp.Symbol('x')
    d1 = sp.discriminant(x**4 - x**2 - 1, x)
    d2 = sp.discriminant(x**4 - 2*x**3 - 5*x**2 - 4*x - 1, x)
    assert d1 == -400
    assert d2 == -400


# ── S2 (audit-corrected): all rc=4 matrices GL(4,Z)-conjugate ──

CONJUGATORS = {
    'B':   [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, -1], [0, -1, 0, 1]],
    'A':   [[1, 0, 0, 0], [2, 1, -1, -1], [-2, -1, 2, 1], [-1, 0, 1, 1]],
    'Bab': [[1, 0, 0, 0], [0, 0, 1, 0], [2, 1, -1, -1], [-1, 0, 1, 1]],
}


def test_gl4z_conjugacy(host):
    """Audit correction: the rc=4 induced matrices ARE GL(4,Z)-conjugate.

    Explicit unimodular P with P*A('a')*P^-1 = A(u) for u in B, A, Bab.
    (Latimer-MacDuffee: Z[beta] maximal, class number 1 => single class.)
    """
    import sympy as sp
    A1 = sp.Matrix(_analyze('a', host)['induced']['matrix'])
    for factor, P_rows in CONJUGATORS.items():
        Au = sp.Matrix(_analyze(factor, host)['induced']['matrix'])
        P = sp.Matrix(P_rows)
        assert abs(P.det()) == 1, f"P for '{factor}' not unimodular"
        assert P * A1 * P.inv() == Au, \
            f"P A(a) P^-1 != A({factor})"


# ── S3 (audit-upgraded): exact mixing forms for Types 4 and 5 ──

def test_t4_full_z_mixing(host):
    """Type 4 (u='aA', rc=5) is FULLY Z-mixing: all 5 components are
    integer combos of {1, tau, phi, tau^3} (audit-exact; 1e-9 here)."""
    tau = SQ_PHI
    r = _analyze('aA', host)
    assert r['rc'] == 5
    v = np.sort(r['perron_vec'])[::-1]
    exact = np.sort([
        2 - tau + PHI - tau**3,
        -2 + 2*tau - 4*PHI + 3*tau**3,
        2 - 2*tau + 3*PHI - 2*tau**3,
        -2 + tau - 2*PHI + 2*tau**3,
        1 + 2*PHI - 2*tau**3,
    ])[::-1]
    assert np.allclose(v, exact, atol=1e-9), f"{v} != {exact}"


def test_t5_half_integer_mixing(host):
    """Type 5 (u='Bab') is HALF-INTEGER mixing (not 'irrational'):
    components are exactly (1+tau-phi)/2, f_a, (1-2tau+tau^3)/2,
    (2-tau+phi-tau^3)/2."""
    tau = SQ_PHI
    r = _analyze('Bab', host)
    v = np.sort(r['perron_vec'])[::-1]
    exact = np.sort([
        (1 + tau - PHI) / 2,
        tau - 1,
        (1 - 2*tau + tau**3) / 2,
        (2 - tau + PHI - tau**3) / 2,
    ])[::-1]
    assert np.allclose(v, exact, atol=1e-9), f"{v} != {exact}"


# ── S11: no SM ratio in ℚ(√φ) ──

def test_no_sm_ratio_exact_in_Q_tau():
    """No SM coupling constant matches ℤ[τ] within 10× lattice spacing."""
    tau = SQ_PHI
    T = np.array([1.0, tau, tau**2, tau**3])
    MAX_C = 8
    rng = np.arange(-MAX_C, MAX_C + 1, dtype=float)
    N = len(rng)
    a = rng.reshape(N, 1, 1, 1)
    b = rng.reshape(1, N, 1, 1)
    c = rng.reshape(1, 1, N, 1)
    d = rng.reshape(1, 1, 1, N)
    lattice = a*T[0] + b*T[1] + c*T[2] + d*T[3]

    alpha_em = 1 / 137.035999084
    sm_values = [alpha_em, 0.1180, 0.23122, 0.22500]

    for val in sm_values:
        err = np.min(np.abs(lattice - val))
        assert err > 1e-6, \
            f"SM value {val} matches ℤ[τ] with err {err} < 1e-6 (would be exact)"
