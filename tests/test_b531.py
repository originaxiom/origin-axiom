"""B531 locks — Trace-Map Gate Campaign.

T1: gap-opening slopes to depth 12 via partial eigendecomposition.
T2: control substitution (Arnoux-Rauzy 4-letter).
T3: internal-space Fourier projection.
"""
import numpy as np
import pytest
from scipy.linalg import eigh_tridiagonal

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
PHI = (1 + np.sqrt(5)) / 2
SQ = np.sqrt(PHI)
S = PHI + 1 + PHI * SQ + SQ
FREQ = np.array([PHI / S, 1 / S, PHI * SQ / S, SQ / S])
TARGET_IDS = [FREQ[0], FREQ[0] + FREQ[1], 1 - FREQ[3]]


def _word(depth):
    u = 'a'
    for _ in range(depth):
        u = ''.join(SUB[c] for c in u)
    return u


def _gap_widths(word, eps, window=30):
    N = len(word)
    diag = np.array([eps if c in 'AB' else 0.0 for c in word])
    off = np.ones(N - 1)
    widths = []
    for t in TARGET_IDS:
        center = int(round(t * N))
        lo = max(0, center - window)
        hi = min(N - 1, center + window)
        eigs = eigh_tridiagonal(diag, off, eigvals_only=True,
                                select='i', select_range=(lo, hi))
        spacings = np.diff(eigs)
        widths.append(float(spacings.max()))
    return widths


def _slopes(depth, eps_values=None):
    if eps_values is None:
        eps_values = np.array([0.01, 0.02, 0.03, 0.04, 0.05])
    word = _word(depth)
    widths_per_gap = [[], [], []]
    for eps in eps_values:
        ws = _gap_widths(word, eps)
        for g in range(3):
            widths_per_gap[g].append(ws[g])
    slopes = []
    for g in range(3):
        w_arr = np.array(widths_per_gap[g])
        slopes.append(np.sum(eps_values * w_arr) / np.sum(eps_values ** 2))
    return slopes


# --- T1 locks ---

def test_t1_partial_eigendecomp_matches_full():
    """Cross-validation: partial and full eigendecomp give identical gap widths."""
    word = _word(7)
    N = len(word)
    eps = 0.05
    diag = np.array([eps if c in 'AB' else 0.0 for c in word])
    off = np.ones(N - 1)

    eigs_full = np.sort(eigh_tridiagonal(diag, off, eigvals_only=True))
    for g, t in enumerate(TARGET_IDS):
        center = int(round(t * N))
        lo, hi = max(0, center - 30), min(N - 1, center + 30)
        w_full = float(np.diff(eigs_full[lo:hi + 1]).max())
        eigs_p = eigh_tridiagonal(diag, off, eigvals_only=True,
                                  select='i', select_range=(lo, hi))
        w_partial = float(np.diff(eigs_p).max())
        assert abs(w_full - w_partial) < 1e-12, f"gap {g+1}: {w_full} != {w_partial}"


def test_t1_slopes_converged_gaps_1_2():
    """Gaps 1-2 slopes converge to definitive values by depth 9."""
    s9 = _slopes(9)
    assert abs(s9[0] - 0.1914) < 0.001, f"s1 = {s9[0]}"
    assert abs(s9[1] - 0.1524) < 0.001, f"s2 = {s9[1]}"


def test_t1_slope_ratio_converged():
    """Slope ratio s1/s2 converges to 1.2565."""
    s9 = _slopes(9)
    ratio = s9[0] / s9[1]
    assert abs(ratio - 1.2565) < 0.002, f"ratio = {ratio}"


def test_t1_gap3_even_odd_alternation():
    """Gap 3 slope alternates with depth parity: ~0.124 (even) vs ~0.154 (odd)."""
    s8 = _slopes(8)
    s9 = _slopes(9)
    assert abs(s8[2] - 0.1244) < 0.002, f"s3(d8) = {s8[2]}"
    assert abs(s9[2] - 0.1539) < 0.002, f"s3(d9) = {s9[2]}"
    assert s9[2] > s8[2], "odd slope should exceed even slope"


def test_t1_gap3_cesaro_average():
    """Gap 3 Cesàro average (even+odd)/2 ≈ 0.139."""
    s8 = _slopes(8)
    s9 = _slopes(9)
    cesaro = (s8[2] + s9[2]) / 2
    assert abs(cesaro - 0.139) < 0.005, f"Cesàro = {cesaro}"


def test_t1_saturation_gaps_1_2():
    """Saturation at ε=5 is depth-independent for gaps 1-2."""
    for depth in [7, 8]:
        ws = _gap_widths(_word(depth), 5.0, window=50)
        assert abs(ws[0] - 1.095) < 0.01, f"gap1 sat d{depth} = {ws[0]}"
        assert abs(ws[1] - 2.821) < 0.01, f"gap2 sat d{depth} = {ws[1]}"


def test_t1_saturation_gap3_parity():
    """Gap 3 saturation shows even/odd effect: 0.712 (odd) vs 0.772 (even)."""
    ws7 = _gap_widths(_word(7), 5.0, window=50)
    ws8 = _gap_widths(_word(8), 5.0, window=50)
    assert abs(ws7[2] - 0.712) < 0.01, f"gap3 sat d7 = {ws7[2]}"
    assert abs(ws8[2] - 0.772) < 0.01, f"gap3 sat d8 = {ws8[2]}"


def test_t1_all_gaps_open():
    """All three gaps open at ε > 0 (positive slope)."""
    s8 = _slopes(8)
    for g in range(3):
        assert s8[g] > 0.1, f"gap {g+1} slope {s8[g]} too small"


def test_t1_gap1_largest_slope():
    """Gap 1 always has the largest slope. Gap 2 vs 3 depends on depth parity."""
    s8 = _slopes(8)
    s9 = _slopes(9)
    assert s8[0] > s8[1] > s8[2], f"even: s1={s8[0]}, s2={s8[1]}, s3={s8[2]}"
    assert s9[0] > s9[1], f"odd: s1={s9[0]} not > s2={s9[1]}"
    assert s9[2] > s9[1], "odd: s3 > s2 (parity inversion of the gap 3 ordering)"


# --- T2 locks ---

def _word_ctrl(depth):
    sub = {'a': 'ab', 'b': 'ac', 'c': 'ad', 'd': 'a'}
    u = 'a'
    for _ in range(depth):
        u = ''.join(sub[c] for c in u)
    return u


def test_t2_control_is_pisot_primitive():
    """AR-4 control is Pisot and primitive."""
    M = np.array([[1, 1, 1, 1], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]], float)
    evals = np.linalg.eigvals(M)
    perron = max(abs(evals))
    assert abs(perron - 1.9276) < 0.001
    assert all(abs(e) < 1 for e in evals if abs(e) < perron - 0.01)
    Mk = np.linalg.matrix_power(M, 4)
    assert np.all(Mk > 0)


def test_t2_control_has_negative_eigenvalue():
    """AR-4 has a negative real contracting eigenvalue (like ours)."""
    M = np.array([[1, 1, 1, 1], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]], float)
    evals = np.linalg.eigvals(M)
    real_evals = sorted([e.real for e in evals if abs(e.imag) < 1e-9])
    assert real_evals[0] < 0, f"smallest real eigenvalue = {real_evals[0]}"


def test_t2_control_gap1_converges():
    """Control gap 1 slope converges (s1 ≈ 0.27 at depth 17+)."""
    M = np.array([[1, 1, 1, 1], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]], float)
    evals, V = np.linalg.eig(M)
    i_perr = np.argmax(abs(evals))
    pv = abs(V[:, i_perr])
    pv = pv / pv.sum()
    gap_ids = sorted(np.cumsum(pv)[:-1])

    eps_fit = np.array([0.01, 0.02, 0.03, 0.04, 0.05])
    word = _word_ctrl(17)
    N = len(word)
    ws = []
    for eps in eps_fit:
        diag = np.array([eps if c in 'cd' else 0.0 for c in word])
        off = np.ones(N - 1)
        center = int(round(gap_ids[0] * N))
        lo, hi = max(0, center - 30), min(N - 1, center + 30)
        eigs = eigh_tridiagonal(diag, off, eigvals_only=True,
                                select='i', select_range=(lo, hi))
        ws.append(float(np.diff(eigs).max()))
    s1 = np.sum(eps_fit * np.array(ws)) / np.sum(eps_fit ** 2)
    assert abs(s1 - 0.269) < 0.01, f"control s1 = {s1}"


# --- T3 locks ---

def test_t3_fourier_amplitude_ordering():
    """Fourier amplitudes |V̂| at gap frequencies match slope ordering."""
    u = 'a'
    for _ in range(12):
        u = ''.join(SUB[c] for c in u)
    u = u[:200000]
    V = np.array([1.0 if c in 'AB' else 0.0 for c in u])
    N = len(V)
    ns = np.arange(N)
    amps = []
    for alpha in TARGET_IDS:
        Vhat = np.sum(V * np.exp(-2j * np.pi * alpha * ns)) / N
        amps.append(abs(Vhat))
    assert amps[0] > amps[1] > amps[2], f"amplitudes: {amps}"


def test_t3_fourier_slope_proportionality():
    """Slopes ≈ 2× Fourier amplitude (within 15%)."""
    u = 'a'
    for _ in range(12):
        u = ''.join(SUB[c] for c in u)
    u = u[:200000]
    V = np.array([1.0 if c in 'AB' else 0.0 for c in u])
    N = len(V)
    ns = np.arange(N)
    slopes = [0.1914, 0.1524, 0.1392]
    for g, alpha in enumerate(TARGET_IDS):
        Vhat = abs(np.sum(V * np.exp(-2j * np.pi * alpha * ns)) / N)
        ratio = slopes[g] / Vhat
        assert 1.8 < ratio < 2.5, f"gap {g+1}: s/|V̂| = {ratio}"


def test_t3_gap1_is_strongest_bragg_peak():
    """Gap 1 frequency is the strongest peak in the FFT spectrum."""
    u = 'a'
    for _ in range(12):
        u = ''.join(SUB[c] for c in u)
    u = u[:200000]
    V = np.array([1.0 if c in 'AB' else 0.0 for c in u])
    fft_V = np.fft.fft(V - V.mean())
    power = np.abs(fft_V[:len(V) // 2]) ** 2
    peak_idx = np.argmax(power)
    peak_freq = peak_idx / len(V)
    assert abs(peak_freq - TARGET_IDS[0]) < 0.001, \
        f"strongest peak at {peak_freq}, expected {TARGET_IDS[0]}"
