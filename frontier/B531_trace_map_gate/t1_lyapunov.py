"""
T1 — Gap-opening slopes to depth 12 via partial eigendecomposition.

Uses scipy eigh_tridiagonal with select='i' to compute only eigenvalues
near each gap position. This is O(N) per gap (vs O(N^2) for full eigendecomp),
enabling depths 10-12 (N up to 8M).

RESULT: gaps 1-2 converge by depth 9. Gap 3 has a systematic EVEN/ODD
PERIOD-2 OSCILLATION in the substitution depth — NOT convergence failure.
"""
import numpy as np
from scipy.linalg import eigh_tridiagonal
from time import time

PHI = (1 + np.sqrt(5)) / 2
SQ = np.sqrt(PHI)
SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}

S = PHI + 1 + PHI * SQ + SQ
FREQ = np.array([PHI / S, 1 / S, PHI * SQ / S, SQ / S])
TARGET_IDS = [FREQ[0], FREQ[0] + FREQ[1], 1 - FREQ[3]]


def _word(depth):
    u = 'a'
    for _ in range(depth):
        u = ''.join(SUB[c] for c in u)
    return u


def gap_widths(word, eps, window=30):
    """Compute gap widths at the three topological gap positions using partial eigendecomp."""
    N = len(word)
    diag = np.array([eps if c in 'AB' else 0.0 for c in word])
    off = np.ones(N - 1)
    widths = []
    for t_ids in TARGET_IDS:
        center = int(round(t_ids * N))
        lo = max(0, center - window)
        hi = min(N - 1, center + window)
        eigs = eigh_tridiagonal(diag, off, eigvals_only=True,
                                select='i', select_range=(lo, hi))
        spacings = np.diff(eigs)
        widths.append(float(spacings.max()))
    return widths


def slope_convergence(depths=None, eps_values=None):
    """Compute gap-opening slopes at multiple depths. The definitive convergence test."""
    if depths is None:
        depths = list(range(5, 13))
    if eps_values is None:
        eps_values = np.array([0.01, 0.02, 0.03, 0.04, 0.05])

    print("=" * 80)
    print("T1 — GAP-OPENING SLOPE CONVERGENCE (partial eigendecomp, depths 5-12)")
    print("=" * 80)
    print(f"{'Depth':>5} {'N':>9} {'s1':>8} {'s2':>8} {'s3':>8} {'s1/s2':>8} {'time':>7}")

    results = {}
    for depth in depths:
        t0 = time()
        word = _word(depth)
        N = len(word)
        widths_per_gap = [[], [], []]
        for eps in eps_values:
            ws = gap_widths(word, eps)
            for g in range(3):
                widths_per_gap[g].append(ws[g])

        slopes = []
        for g in range(3):
            w_arr = np.array(widths_per_gap[g])
            slope = np.sum(eps_values * w_arr) / np.sum(eps_values ** 2)
            slopes.append(slope)

        ratio = slopes[0] / slopes[1] if slopes[1] > 0 else float('inf')
        dt = time() - t0
        print(f"{depth:>5} {N:>9} {slopes[0]:>8.4f} {slopes[1]:>8.4f} "
              f"{slopes[2]:>8.4f} {ratio:>8.4f} {dt:>6.1f}s")
        results[depth] = {'slopes': slopes, 'ratio': ratio, 'N': N}

    return results


def even_odd_analysis(results):
    """Analyze the even/odd alternation in gap 3."""
    print("\n" + "=" * 80)
    print("GAP 3 EVEN/ODD ANALYSIS")
    print("=" * 80)

    even_s3 = [results[d]['slopes'][2] for d in sorted(results) if d % 2 == 0 and d >= 8]
    odd_s3 = [results[d]['slopes'][2] for d in sorted(results) if d % 2 == 1 and d >= 9]

    if even_s3:
        print(f"  Even depths (8,10,12): s3 = {', '.join(f'{s:.4f}' for s in even_s3)}")
        print(f"    mean = {np.mean(even_s3):.6f}, std = {np.std(even_s3):.6f}")
    if odd_s3:
        print(f"  Odd depths (9,11):     s3 = {', '.join(f'{s:.4f}' for s in odd_s3)}")
        print(f"    mean = {np.mean(odd_s3):.6f}, std = {np.std(odd_s3):.6f}")

    if even_s3 and odd_s3:
        s3_even = np.mean(even_s3)
        s3_odd = np.mean(odd_s3)
        s3_avg = (s3_even + s3_odd) / 2
        print(f"\n  Cesàro average: ({s3_even:.4f} + {s3_odd:.4f})/2 = {s3_avg:.4f}")
        print(f"  Alternation amplitude: |s3_even - s3_odd| = {abs(s3_even - s3_odd):.4f}")


def saturation_check(depth=8):
    """Verify saturation values at ε=5."""
    print("\n" + "=" * 80)
    print(f"SATURATION AT ε=5 (depth {depth})")
    print("=" * 80)

    word = _word(depth)
    ws = gap_widths(word, 5.0, window=50)
    print(f"  Gap 1: {ws[0]:.4f}  (claimed 1.10)")
    print(f"  Gap 2: {ws[1]:.4f}  (claimed 2.82)")
    print(f"  Gap 3: {ws[2]:.4f}  (claimed 0.71)")


def gap_opening_curves(depth=10, eps_values=None):
    """Compute gap width W(ε) curves for all three gaps."""
    if eps_values is None:
        eps_values = np.concatenate([
            np.linspace(0.01, 0.1, 10),
            np.linspace(0.2, 1.0, 9),
            np.linspace(1.5, 5.0, 8),
        ])

    word = _word(depth)
    N = len(word)
    print(f"\n  Gap-opening curves at depth {depth} (N={N})")
    print(f"  {'eps':>6} {'W1':>10} {'W2':>10} {'W3':>10}")

    curves = [[], [], []]
    for eps in eps_values:
        ws = gap_widths(word, eps, window=50)
        for g in range(3):
            curves[g].append(ws[g])
        if eps <= 0.1 or eps in [0.2, 0.5, 1.0, 2.0, 5.0]:
            print(f"  {eps:>6.3f} {ws[0]:>10.6f} {ws[1]:>10.6f} {ws[2]:>10.6f}")

    return eps_values, curves


if __name__ == "__main__":
    results = slope_convergence(depths=list(range(5, 13)))
    even_odd_analysis(results)
    saturation_check(depth=8)
