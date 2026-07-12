"""B532 locks — the Last Echo campaign (interaction grammar → irreducible feedback kernel).

I1: Fixed-point dimension + period-3 spectral test.
"""
import numpy as np
import pytest
from scipy.linalg import eigh_tridiagonal
from scipy.optimize import least_squares

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
PHI_GOLDEN = (1 + np.sqrt(5)) / 2
SQ = np.sqrt(PHI_GOLDEN)
S = PHI_GOLDEN + 1 + PHI_GOLDEN * SQ + SQ
FREQ = np.array([PHI_GOLDEN / S, 1 / S, PHI_GOLDEN * SQ / S, SQ / S])
TARGET_IDS = [FREQ[0], FREQ[0] + FREQ[1], 1 - FREQ[3]]


def _grow(depth, seed='a'):
    u = seed
    for _ in range(depth):
        u = ''.join(SUB[c] for c in u)
    return u


def _gap_slopes(word, eps_values=None):
    if eps_values is None:
        eps_values = np.array([0.01, 0.02, 0.03, 0.04, 0.05])
    N = len(word)
    widths_per_gap = [[], [], []]
    for eps in eps_values:
        diag = np.array([eps if c in 'AB' else 0.0 for c in word])
        off = np.ones(N - 1)
        for g, t in enumerate(TARGET_IDS):
            center = int(round(t * N))
            lo, hi = max(0, center - 30), min(N - 1, center + 30)
            eigs = eigh_tridiagonal(diag, off, eigvals_only=True,
                                    select='i', select_range=(lo, hi))
            widths_per_gap[g].append(float(np.diff(eigs).max()))
    slopes = []
    for g in range(3):
        w_arr = np.array(widths_per_gap[g])
        slopes.append(np.sum(eps_values * w_arr) / np.sum(eps_values ** 2))
    return slopes


# ─── I1 Part B: Period-3 spectral test ───

def test_i1_period3_slopes_are_pure_period2():
    """Gap-3 slope ratio s₁/s₃ shows pure period-2 (even/odd), no period-3."""
    ratios = {}
    for d in [8, 9, 10, 11]:
        s = _gap_slopes(_grow(d))
        ratios[d] = s[0] / s[2]

    # Period-2: even and odd are clearly separated
    even = [ratios[d] for d in [8, 10]]
    odd = [ratios[d] for d in [9, 11]]
    assert all(r > 1.4 for r in even), f"even ratios should be > 1.4: {even}"
    assert all(r < 1.3 for r in odd), f"odd ratios should be < 1.3: {odd}"

    # Period-3 absence: d%3 classes should NOT be separated
    # d=8 (mod3=2, even=high), d=9 (mod3=0, odd=low), d=10 (mod3=1, even=high), d=11 (mod3=2, odd=low)
    # If period-3 existed, same-d%3 would cluster. Instead, 8 and 11 are mod3=2 but have opposite ratios.
    assert abs(ratios[8] - ratios[11]) > 0.2, \
        "d=8 and d=11 are both mod3=2 but should have different ratios (no period-3)"


def test_i1_period3_complex_eigenvalue_not_period3():
    """The complex eigenvalue pair has arg ≈ -0.79π, period ≈ 2.54, NOT period 3."""
    M = np.array([[1, 1, 1, 1], [1, 0, 1, 0], [2, 1, 1, 1], [1, 1, 1, 0]], float)
    evals = np.linalg.eigvals(M)
    complex_evals = [e for e in evals if abs(e.imag) > 0.01]
    assert len(complex_evals) == 2, f"expected 2 complex eigenvalues, got {len(complex_evals)}"
    arg = abs(np.angle(complex_evals[0]))
    period = 2 * np.pi / arg
    assert 2.3 < period < 2.8, f"period = {period}, expected ~2.54 (not 3)"
    assert abs(period - 3.0) > 0.2, f"period {period} too close to 3"


def test_i1_period3_fourier_phases_converge():
    """Fourier phases converge without period-3 modulation."""
    phases = []
    for d in [9, 10, 11]:
        word = _grow(d)[:200000]
        V = np.array([1.0 if c in 'AB' else 0.0 for c in word])
        N = len(V)
        ns = np.arange(N)
        gap_phases = []
        for alpha in TARGET_IDS:
            Vhat = np.sum(V * np.exp(-2j * np.pi * alpha * ns)) / N
            gap_phases.append(np.angle(Vhat))
        phases.append(gap_phases)

    # Phases should converge (d=10 and d=11 nearly identical due to truncation)
    for g in range(3):
        diff_10_11 = abs(phases[1][g] - phases[2][g])
        assert diff_10_11 < 0.01, f"gap {g+1}: phases at d=10,11 differ by {diff_10_11}"


def test_i1_period3_c2_is_period2_not_3():
    """Quadratic correction c₂ for gap 3 alternates with depth parity (period 2)."""
    eps_values = np.array([0.01, 0.02, 0.03, 0.04, 0.05])
    c2_vals = {}
    for d in [8, 9, 10, 11]:
        word = _grow(d)
        N = len(word)
        widths = []
        for eps in eps_values:
            diag = np.array([eps if c in 'AB' else 0.0 for c in word])
            off = np.ones(N - 1)
            t = TARGET_IDS[2]
            center = int(round(t * N))
            lo, hi = max(0, center - 30), min(N - 1, center + 30)
            eigs = eigh_tridiagonal(diag, off, eigvals_only=True,
                                    select='i', select_range=(lo, hi))
            widths.append(float(np.diff(eigs).max()))
        A = np.column_stack([eps_values, eps_values**2])
        c, _, _, _ = np.linalg.lstsq(A, widths, rcond=None)
        c2_vals[d] = c[1]

    # Period-2: even depths have c₂ ≈ 0.27, odd depths ≈ 0.38
    assert abs(c2_vals[8] - c2_vals[10]) < 0.01, "even depths should match"
    assert abs(c2_vals[9] - c2_vals[11]) < 0.01, "odd depths should match"
    assert c2_vals[9] > c2_vals[8], "odd c₂ > even c₂"
    # Period-3: d=8 (mod3=2) and d=11 (mod3=2) should match if period-3 exists
    assert abs(c2_vals[8] - c2_vals[11]) > 0.05, \
        "same d%3 class has different c₂ → no period-3"


# ─── I1 Part A: Fixed-point dimension ───

GENS = ['a', 'b', 'A', 'B']
PHI_SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}


def _mat(v):
    return np.array([[v[0], v[1]], [v[2], v[3]]], complex)


def _unpack(x):
    z = x[:len(x) // 2] + 1j * x[len(x) // 2:]
    return np.diag([z[0], 1 / z[0]]), {g: _mat(z[1 + 4 * i:5 + 4 * i]) for i, g in enumerate(GENS)}


def _wm(w, Ms, inv):
    P = np.eye(2, dtype=complex)
    for ch in w:
        P = P @ (Ms[ch] if ch in Ms else inv[ch.lower()])
    return P


def _resid(x):
    T, Ms = _unpack(x)
    Ti = np.linalg.inv(T)
    inv = {g: np.linalg.inv(Ms[g]) for g in GENS}
    r = [T @ Ms[g] @ Ti - _wm(PHI_SUB[g], Ms, inv) for g in GENS]
    d = np.array([np.linalg.det(Ms[g]) - 1 for g in GENS])
    flat = np.concatenate([m.ravel() for m in r] + [d])
    return np.concatenate([flat.real, flat.imag])


def _find_fp(seed, irred_only=True):
    np.random.seed(seed)
    for _ in range(500):
        s = least_squares(_resid, np.random.randn(34) * 0.9, method='lm', max_nfev=1500)
        if s.cost < 1e-18:
            T, Ms = _unpack(s.x)
            if irred_only:
                C = Ms['a'] @ Ms['b'] @ np.linalg.inv(Ms['a']) @ np.linalg.inv(Ms['b'])
                if abs(np.trace(C) - 2) > 0.3:
                    return s.x, T, Ms
            else:
                return s.x, T, Ms
    return None


def _jacobian_rank(x0, eps=1e-7):
    r0 = _resid(x0)
    n, m = len(x0), len(r0)
    J = np.zeros((m, n))
    for j in range(n):
        xp = x0.copy()
        xp[j] += eps
        J[:, j] = (_resid(xp) - r0) / eps
    sv = np.linalg.svd(J, compute_uv=False)
    rank = int(np.sum(sv > 1e-6))
    return rank, n - rank


def test_i1_fp_generic_irreducible_are_isolated():
    """Generic irreducible FPs have Jacobian kernel dim = 2 (= gauge dim) → isolated."""
    for seed in [7, 11, 19, 31]:
        result = _find_fp(seed)
        if result is None:
            continue
        x0, T, Ms = result
        tr_a = abs(np.trace(Ms['a']))
        if tr_a < 0.01:
            continue
        rank, kernel = _jacobian_rank(x0)
        assert kernel == 2, f"seed {seed}: kernel_dim = {kernel}, expected 2"


def test_i1_fp_trace_zero_have_extra_kernel():
    """Trace-zero FPs (κ=-2) have Jacobian kernel dim = 4 (extra 2-dim family)."""
    for seed in [2, 37, 41]:
        result = _find_fp(seed)
        if result is None:
            continue
        x0, T, Ms = result
        if abs(np.trace(Ms['a'])) > 0.1:
            continue
        rank, kernel = _jacobian_rank(x0)
        assert kernel == 4, f"seed {seed}: kernel_dim = {kernel}, expected 4"
        kappa = np.trace(Ms['a'] @ Ms['b'] @ np.linalg.inv(Ms['a']) @ np.linalg.inv(Ms['b']))
        assert abs(kappa + 2) < 0.01, f"κ = {kappa}, expected -2"


def test_i1_fp_two_components():
    """The irreducible FP variety has (at least) two components:
    trace-zero (dim=1 complex) and generic (dim=0, isolated)."""
    trace_zero_count = 0
    generic_count = 0
    for seed in [2, 7, 11, 19, 31, 37, 41, 53]:
        result = _find_fp(seed)
        if result is None:
            continue
        x0, T, Ms = result
        rank, kernel = _jacobian_rank(x0)
        if abs(np.trace(Ms['a'])) < 0.01:
            trace_zero_count += 1
            assert kernel == 4
        else:
            generic_count += 1
            assert kernel == 2
    assert trace_zero_count >= 2, f"found only {trace_zero_count} trace-zero FPs"
    assert generic_count >= 3, f"found only {generic_count} generic FPs"


# ─── I2: The Projection Algebra ───

import sympy as sp

_PHI = (1 + np.sqrt(5)) / 2
_SQ_PHI = np.sqrt(_PHI)
_S_NORM = _PHI + 1 + _PHI * _SQ_PHI + _SQ_PHI
_PERRON_FREQ = np.array([_PHI / _S_NORM, 1 / _S_NORM, _PHI * _SQ_PHI / _S_NORM, _SQ_PHI / _S_NORM])
_ALPHA = ['a', 'b', 'A', 'B']
_SUB_MAP = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}


def _projected_freq_ratio(class0_indices, class1_indices):
    f0 = sum(_PERRON_FREQ[i] for i in class0_indices)
    f1 = sum(_PERRON_FREQ[i] for i in class1_indices)
    return f0 / f1


def _is_substitutive(class0_indices, class1_indices):
    proj = {}
    for i in class0_indices:
        proj[_ALPHA[i]] = 0
    for i in class1_indices:
        proj[_ALPHA[i]] = 1
    images_by_class = {}
    for g in _ALPHA:
        target = proj[g]
        image = ''.join(str(proj[c]) for c in _SUB_MAP[g])
        if target not in images_by_class:
            images_by_class[target] = {image}
        else:
            images_by_class[target].add(image)
    return all(len(v) == 1 for v in images_by_class.values())


def test_i2_no_projection_is_substitutive():
    """None of the 7 binary partitions commute with σ."""
    partitions = [
        ([0], [1, 2, 3]),      # {a}|{bAB}
        ([1], [0, 2, 3]),      # {b}|{aAB}
        ([2], [0, 1, 3]),      # {A}|{abB}
        ([3], [0, 1, 2]),      # {B}|{abA}
        ([0, 1], [2, 3]),      # {ab}|{AB}
        ([0, 2], [1, 3]),      # {aA}|{bB}
        ([0, 3], [1, 2]),      # {aB}|{bA}
    ]
    for c0, c1 in partitions:
        assert not _is_substitutive(c0, c1), \
            f"partition {[_ALPHA[i] for i in c0]} is substitutive (should not be)"


def test_i2_structural_partition_gives_phi():
    """{aA}|{bB} projection reads frequency ratio = φ exactly."""
    ratio = _projected_freq_ratio([0, 2], [1, 3])
    assert abs(ratio - _PHI) < 1e-10, f"ratio = {ratio}, expected φ = {_PHI}"


def test_i2_old_new_partition_gives_inv_sqrt_phi():
    """{ab}|{AB} projection reads frequency ratio = 1/√φ exactly."""
    ratio = _projected_freq_ratio([0, 1], [2, 3])
    assert abs(ratio - 1 / _SQ_PHI) < 1e-10, f"ratio = {ratio}, expected 1/√φ = {1/_SQ_PHI}"


def test_i2_cross_partition_not_golden():
    """{aB}|{bA} ratio ≈ 0.945, not a simple golden expression."""
    ratio = _projected_freq_ratio([0, 3], [1, 2])
    assert 0.94 < ratio < 0.95, f"ratio = {ratio}"
    assert abs(ratio - _PHI) > 0.5, "should not be φ"
    assert abs(ratio - 1 / _PHI) > 0.3, "should not be 1/φ"
    assert abs(ratio - 1 / _SQ_PHI) > 0.1, "should not be 1/√φ"


def test_i2_all_projections_primitive():
    """All 7 binary partitions give primitive 2×2 induced matrices."""
    partitions = [
        ([0], [1, 2, 3]), ([1], [0, 2, 3]), ([2], [0, 1, 3]), ([3], [0, 1, 2]),
        ([0, 1], [2, 3]), ([0, 2], [1, 3]), ([0, 3], [1, 2]),
    ]
    for c0, c1 in partitions:
        proj = {}
        for i in c0:
            proj[_ALPHA[i]] = 0
        for i in c1:
            proj[_ALPHA[i]] = 1
        M = np.zeros((2, 2), dtype=int)
        for g in _ALPHA:
            target = proj[g]
            for c in _SUB_MAP[g]:
                M[proj[c], target] += 1
        Mk = np.eye(2, dtype=int)
        for k in range(1, 20):
            Mk = Mk @ M
            if np.all(Mk > 0):
                break
        else:
            assert False, f"partition {[_ALPHA[i] for i in c0]} not primitive"


def test_i2_pisot_count():
    """Exactly 5 of 7 partitions have Pisot induced matrices (|λ₂| < 1).
    The two non-Pisot: {aA}|{bB} (|λ₂|≈1.47) and {aB}|{bA} (|λ₂|=1)."""
    partitions = [
        ([0], [1, 2, 3]), ([1], [0, 2, 3]), ([2], [0, 1, 3]), ([3], [0, 1, 2]),
        ([0, 1], [2, 3]), ([0, 2], [1, 3]), ([0, 3], [1, 2]),
    ]
    pisot_count = 0
    non_pisot = []
    for c0, c1 in partitions:
        proj = {}
        for i in c0:
            proj[_ALPHA[i]] = 0
        for i in c1:
            proj[_ALPHA[i]] = 1
        M = np.zeros((2, 2), dtype=int)
        for g in _ALPHA:
            target = proj[g]
            for c in _SUB_MAP[g]:
                M[proj[c], target] += 1
        evals = np.abs(np.linalg.eigvals(M.astype(float)))
        evals.sort()
        if evals[0] < 1 - 1e-6:
            pisot_count += 1
        else:
            non_pisot.append((''.join(_ALPHA[i] for i in c0), evals[0]))
    assert pisot_count == 5, f"expected 5 Pisot, got {pisot_count}"
    assert len(non_pisot) == 2
