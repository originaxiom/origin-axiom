#!/usr/bin/env python3
"""B532 I1 Part B — Period-3 spectral test.

The F₂⁴ phase map has period 6 = 2×3. B531 found the period-2 spectral shadow
(gap-3 slope alternation from λ₂ < 0). Does the period-3 have a spectral shadow?

Tests:
1. Fourier PHASES arg(V̂(α)) at gap frequencies vs depth d — period-3 modulation?
2. Quadratic correction c₂(d) — period-3 in |c₂|?
3. Gap-width ratios W₁/W₃, W₂/W₃ vs depth — period-6 modulation?
4. Internal-space projection phases — period-3 in the Rauzy fractal component?
"""

import numpy as np
from scipy.linalg import eigh_tridiagonal

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
PHI = (1 + np.sqrt(5)) / 2
SQ = np.sqrt(PHI)
S = PHI + 1 + PHI * SQ + SQ
FREQ = np.array([PHI / S, 1 / S, PHI * SQ / S, SQ / S])
TARGET_IDS = [FREQ[0], FREQ[0] + FREQ[1], 1 - FREQ[3]]


def grow(depth, seed='a'):
    u = seed
    for _ in range(depth):
        u = ''.join(SUB[c] for c in u)
    return u


def gap_slopes(word, eps_values=None):
    if eps_values is None:
        eps_values = np.array([0.01, 0.02, 0.03, 0.04, 0.05])
    N = len(word)
    widths_per_gap = [[], [], []]
    for eps in eps_values:
        diag = np.array([eps if c in 'AB' else 0.0 for c in word])
        off = np.ones(N - 1)
        for g, t in enumerate(TARGET_IDS):
            center = int(round(t * N))
            lo = max(0, center - 30)
            hi = min(N - 1, center + 30)
            eigs = eigh_tridiagonal(diag, off, eigvals_only=True,
                                    select='i', select_range=(lo, hi))
            widths_per_gap[g].append(float(np.diff(eigs).max()))
    slopes = []
    for g in range(3):
        w_arr = np.array(widths_per_gap[g])
        s = np.sum(eps_values * w_arr) / np.sum(eps_values ** 2)
        slopes.append(s)
    return slopes


def quadratic_fit(word, eps_values=None):
    """Fit W_g(eps) = c1*eps + c2*eps^2 for each gap."""
    if eps_values is None:
        eps_values = np.array([0.01, 0.02, 0.03, 0.04, 0.05])
    N = len(word)
    coeffs = []
    for g, t in enumerate(TARGET_IDS):
        widths = []
        for eps in eps_values:
            diag = np.array([eps if c in 'AB' else 0.0 for c in word])
            off = np.ones(N - 1)
            center = int(round(t * N))
            lo = max(0, center - 30)
            hi = min(N - 1, center + 30)
            eigs = eigh_tridiagonal(diag, off, eigvals_only=True,
                                    select='i', select_range=(lo, hi))
            widths.append(float(np.diff(eigs).max()))
        A = np.column_stack([eps_values, eps_values**2])
        c, _, _, _ = np.linalg.lstsq(A, widths, rcond=None)
        coeffs.append({'c1': c[0], 'c2': c[1]})
    return coeffs


def fourier_phases(word, truncate=None):
    """Compute Fourier amplitudes and phases at gap frequencies."""
    if truncate:
        word = word[:truncate]
    V = np.array([1.0 if c in 'AB' else 0.0 for c in word])
    N = len(V)
    ns = np.arange(N)
    results = []
    for alpha in TARGET_IDS:
        Vhat = np.sum(V * np.exp(-2j * np.pi * alpha * ns)) / N
        results.append({
            'amplitude': abs(Vhat),
            'phase': np.angle(Vhat),
        })
    return results


def main():
    print("=" * 70)
    print("B532 I1 Part B — Period-3 spectral test")
    print("=" * 70)

    # Test 1: Fourier phases vs depth
    print("\n--- Test 1: Fourier phases at gap frequencies ---")
    print(f"{'depth':>5} {'|V̂₁|':>10} {'arg(V̂₁)':>10} {'|V̂₂|':>10} {'arg(V̂₂)':>10} {'|V̂₃|':>10} {'arg(V̂₃)':>10}")
    phase_data = {}
    for d in range(5, 13):
        word = grow(d)
        fp = fourier_phases(word, truncate=200000 if len(word) > 200000 else None)
        phase_data[d] = fp
        print(f"{d:5d} {fp[0]['amplitude']:10.6f} {fp[0]['phase']:10.4f} "
              f"{fp[1]['amplitude']:10.6f} {fp[1]['phase']:10.4f} "
              f"{fp[2]['amplitude']:10.6f} {fp[2]['phase']:10.4f}")

    # Check for period-3 modulation in phases
    print("\n  Phase differences (d) - (d-3):")
    for d in range(8, 13):
        if d in phase_data and d - 3 in phase_data:
            for g in range(3):
                diff = phase_data[d][g]['phase'] - phase_data[d-3][g]['phase']
                diff = (diff + np.pi) % (2 * np.pi) - np.pi
                print(f"    d={d}, gap {g+1}: Δarg = {diff:.6f}")

    # Test 2: Quadratic correction c₂(d) — period-3?
    print("\n--- Test 2: Quadratic correction c₂(d) ---")
    print(f"{'depth':>5} {'c₂(gap1)':>12} {'c₂(gap2)':>12} {'c₂(gap3)':>12}")
    c2_data = {}
    for d in range(6, 12):
        word = grow(d)
        coeffs = quadratic_fit(word)
        c2_data[d] = [c['c2'] for c in coeffs]
        print(f"{d:5d} {coeffs[0]['c2']:12.4f} {coeffs[1]['c2']:12.4f} {coeffs[2]['c2']:12.4f}")

    # Check period-3 in c₂
    print("\n  c₂ residuals mod 3:")
    for d in range(6, 12):
        phase = d % 3
        print(f"    d={d} (mod 3 = {phase}): c₂ = [{c2_data[d][0]:.4f}, {c2_data[d][1]:.4f}, {c2_data[d][2]:.4f}]")

    # Test 3: Gap-slope ratios vs depth — period-6?
    print("\n--- Test 3: Gap-slope ratios vs depth ---")
    print(f"{'depth':>5} {'s₁':>10} {'s₂':>10} {'s₃':>10} {'s₁/s₃':>10} {'s₂/s₃':>10} {'s₁/s₂':>10} {'d%6':>5}")
    ratio_data = {}
    for d in range(6, 12):
        word = grow(d)
        s = gap_slopes(word)
        r13 = s[0] / s[2] if s[2] > 0.01 else float('nan')
        r23 = s[1] / s[2] if s[2] > 0.01 else float('nan')
        r12 = s[0] / s[1] if s[1] > 0.01 else float('nan')
        ratio_data[d] = {'s': s, 'r13': r13, 'r23': r23, 'r12': r12}
        print(f"{d:5d} {s[0]:10.6f} {s[1]:10.6f} {s[2]:10.6f} {r13:10.4f} {r23:10.4f} {r12:10.4f} {d%6:5d}")

    # Test 4: Internal-space Fourier projection — period-3 components
    print("\n--- Test 4: Internal-space projection at depths 7-12 ---")

    M = np.array([[1, 1, 1, 1], [1, 0, 1, 0], [2, 1, 1, 1], [1, 1, 1, 0]], float)
    evals, V = np.linalg.eig(M)
    idx = np.argsort(-np.abs(evals))
    evals = evals[idx]
    V = V[:, idx]
    print(f"  Eigenvalues: {evals}")
    print(f"  |λ₁| = {abs(evals[0]):.6f} (Perron)")
    print(f"  |λ₂| = {abs(evals[1]):.6f} (real negative)")
    print(f"  |λ₃| = {abs(evals[2]):.6f}, |λ₄| = {abs(evals[3]):.6f} (complex pair)")

    # The complex pair λ₃,λ₄ has |λ|~0.440 and arg ≈ ±2π/3 would give period-3
    for i in [2, 3]:
        if np.abs(evals[i].imag) > 0.01:
            arg = np.angle(evals[i])
            print(f"  λ_{i+1}: arg = {arg:.6f} = {arg/np.pi:.4f}π")
            period = 2 * np.pi / abs(arg)
            print(f"         implied period = {period:.4f}")

    # Project the potential V onto the complex eigenvector direction
    print(f"\n  Projection of V onto complex eigenvector at each depth:")
    for d in range(7, 13):
        word = grow(d)[:200000]
        V_pot = np.array([1.0 if c in 'AB' else 0.0 for c in word])
        N = len(V_pot)
        # Build Parikh running sums (approximate internal-space coordinate)
        parikh_stream = np.zeros((N, 4))
        for i, c in enumerate(word[:N]):
            idx_c = 'abAB'.index(c)
            parikh_stream[i, idx_c] = 1
        cum = np.cumsum(parikh_stream, axis=0)

        Vinv = np.linalg.inv(V)
        internal = cum @ Vinv.T
        # The complex eigenvector component ~ e^{i·arg(λ)·n}
        if abs(evals[2].imag) > 0.01:
            z = internal[:, 2]
            amp = np.mean(np.abs(z[-N//2:]))
            ang = np.angle(z[-1])
            print(f"    d={d}, N={N}: |z_complex| mean = {amp:.4f}, arg(z_end) = {ang:.4f}")

    # Verdict
    print("\n" + "=" * 70)
    print("VERDICT SUMMARY")
    print("=" * 70)

    # Period-2 in slopes (from B531, for comparison)
    s_even = [ratio_data[d]['s'][2] for d in [6, 8, 10] if d in ratio_data]
    s_odd = [ratio_data[d]['s'][2] for d in [7, 9, 11] if d in ratio_data]
    if s_even and s_odd:
        p2_effect = abs(np.mean(s_odd) - np.mean(s_even))
        print(f"  Period-2 (gap 3 slope): effect = {p2_effect:.6f} (KNOWN from B531)")

    # Period-3 in c₂
    c2_by_mod3 = {r: [] for r in range(3)}
    for d in range(6, 12):
        c2_by_mod3[d % 3].append(c2_data[d][2])
    c2_means = {r: np.mean(v) for r, v in c2_by_mod3.items() if v}
    if len(c2_means) == 3:
        c2_spread = max(c2_means.values()) - min(c2_means.values())
        c2_overall = np.std(list(c2_means.values()))
        print(f"  Period-3 (c₂ gap 3 by d mod 3): means = {c2_means}, spread = {c2_spread:.4f}")

    # Period-3 in ratios
    r13_by_mod3 = {r: [] for r in range(3)}
    for d in range(6, 12):
        r13_by_mod3[d % 3].append(ratio_data[d]['r13'])
    r13_means = {r: np.mean(v) for r, v in r13_by_mod3.items() if v}
    if len(r13_means) == 3:
        r13_spread = max(r13_means.values()) - min(r13_means.values())
        print(f"  Period-3 (s₁/s₃ by d mod 3): means = {r13_means}, spread = {r13_spread:.4f}")

    # Period-6 in ratios
    r13_by_mod6 = {r: [] for r in range(6)}
    for d in range(6, 12):
        r13_by_mod6[d % 6].append(ratio_data[d]['r13'])
    r13_6_means = {r: np.mean(v) for r, v in r13_by_mod6.items() if v}
    print(f"  Period-6 (s₁/s₃ by d mod 6): {r13_6_means}")


if __name__ == '__main__':
    main()
