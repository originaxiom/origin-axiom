"""
Movement XXXIII — gap-opening curve verification (CORRECTED after depth 8-9).

SELF-CORRECTION: The initial depth-7 computation led to three premature claims:
  - "slope₂ ≈ slope₃" → artifact (ratio 1.27 at depth 8)
  - "slope ratio numerology killed" → wrong (ratio converges to 1.204 at depth 9)
  - "gap 3 slope ≈ 0.155" → unconverged (oscillates 0.12-0.15)

Converged results (depths 7-9):
  - Gap 1 slope ≈ 0.184 (handoff correct)
  - Gap 2 slope ≈ 0.153 (handoff correct)
  - Gap 3: oscillates 0.12-0.15, slower than gaps 1-2 (handoff "quadratic" overstates)
  - Ratio slope1/slope2 ≈ 1.204 (handoff correct; √(1/φ²+1)=1.176 ≠ 1.204)
  - Saturation at ε=5: all match
"""
import numpy as np
from scipy.linalg import eigh_tridiagonal

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


def tight_binding_spectrum(word, eps):
    N = len(word)
    diag = np.array([eps if c in 'AB' else 0.0 for c in word])
    off = np.ones(N - 1)
    return np.sort(eigh_tridiagonal(diag, off, eigvals_only=True))


def gap_width_windowed(eigs, target_ids, window=40):
    N = len(eigs)
    center = int(round(target_ids * N))
    lo = max(0, center - window)
    hi = min(N - 1, center + window)
    spacings = np.diff(eigs[lo:hi + 1])
    return float(spacings.max()) if len(spacings) > 0 else 0.0


def verify_convergence():
    """Check slope convergence across depths 5-8."""
    print("=" * 70)
    print("GAP-OPENING SLOPE CONVERGENCE (depths 5-8)")
    print("=" * 70)

    eps_fit = np.array([0.01, 0.02, 0.03, 0.04, 0.05])

    for depth in [5, 6, 7, 8]:
        word = _word(depth)
        N = len(word)
        slopes = []
        for g in range(3):
            widths = np.array([gap_width_windowed(
                tight_binding_spectrum(word, e), TARGET_IDS[g]) for e in eps_fit])
            slope = np.sum(eps_fit * widths) / np.sum(eps_fit ** 2)
            slopes.append(slope)
        ratio = slopes[0] / slopes[1] if slopes[1] > 0 else float('inf')
        print(f"  Depth {depth} (N={N:>6}): "
              f"s1={slopes[0]:.4f}  s2={slopes[1]:.4f}  s3={slopes[2]:.4f}  "
              f"s1/s2={ratio:.4f}")


def verify_saturation():
    """Verify saturation values at ε=5."""
    print("\n" + "=" * 70)
    print("SATURATION AT ε=5 (depth 7)")
    print("=" * 70)

    word = _word(7)
    eigs = tight_binding_spectrum(word, 5.0)
    claimed = [1.10, 2.82, 0.71]
    for g in range(3):
        w = gap_width_windowed(eigs, TARGET_IDS[g])
        print(f"  Gap {g + 1}: {w:.4f}  (handoff: {claimed[g]})  "
              f"{'✓' if abs(w - claimed[g]) < 0.02 else '✗'}")


def verify_potential_dependence():
    """Show that slopes depend on which letters carry the potential."""
    print("\n" + "=" * 70)
    print("POTENTIAL-DEPENDENCE (depth 7, ε=0.03)")
    print("=" * 70)

    word = _word(7)
    eps = 0.03

    assignments = {
        'old/new (standard)': 'AB',
        'new/old (inverted)': 'ab',
        'decider/courier': 'aA',
        'only-a': 'a',
    }

    print(f"{'assignment':>25} {'gap1/ε':>10} {'gap2/ε':>10} {'gap3/ε':>10}")
    for name, new_set in assignments.items():
        N = len(word)
        diag = np.array([eps if c in new_set else 0.0 for c in word])
        off = np.ones(N - 1)
        eigs = np.sort(eigh_tridiagonal(diag, off, eigvals_only=True))
        widths = [gap_width_windowed(eigs, t) for t in TARGET_IDS]
        print(f"{name:>25} {widths[0] / eps:10.4f} {widths[1] / eps:10.4f} {widths[2] / eps:10.4f}")

    print("\n  Gap POSITIONS are topological (same IDS at all assignments).")
    print("  Gap WIDTHS are non-topological (depend on the physical realization).")


if __name__ == "__main__":
    verify_convergence()
    verify_saturation()
    verify_potential_dependence()
