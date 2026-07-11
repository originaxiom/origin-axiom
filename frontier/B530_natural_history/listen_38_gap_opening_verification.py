"""
Movement XXXIII — gap-opening curve verification.

The handoff claims:
  - Gap 1 (IDS=0.272): opens linearly, slope ≈ 0.184·ε
  - Gap 2 (IDS=0.440): opens linearly, slope ≈ 0.153·ε
  - Gap 3 (IDS=0.786): opens quadratically (slope ≈ 0)
  - Ratio slope₁/slope₂ ≈ 1.204 ≈ √(1/φ²+1)
  - Saturation: gap1→1.10, gap2→2.82, gap3→0.71 at ε=5

RESULTS:
  - Gap 1 slope ≈ 0.193 (handoff 0.184, ~5% off — plausible finite-size shift)
  - Gap 2 slope ≈ 0.155 (handoff 0.153, matches)
  - Gap 3 slope ≈ 0.155 — opens LINEARLY, NOT quadratically (handoff WRONG)
  - slope2 ≈ slope3 (ratio 1.0006): gaps 2 and 3 open at identical rates
  - Ratio slope1/slope2 ≈ 1.25 (handoff 1.204 off; √(1/φ²+1)=1.176 = numerology)
  - Saturation values at ε=5: all correct
"""
import numpy as np
from scipy.linalg import eigh_tridiagonal

PHI = (1 + np.sqrt(5)) / 2
SQ = np.sqrt(PHI)
SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
M = np.array([[1, 1, 1, 1], [1, 0, 1, 0], [2, 1, 1, 1], [1, 1, 1, 0]])

S = PHI + 1 + PHI * SQ + SQ
FREQ = np.array([PHI / S, 1 / S, PHI * SQ / S, SQ / S])
TARGET_IDS = [FREQ[0], FREQ[0] + FREQ[1], FREQ[0] + FREQ[1] + FREQ[2]]


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


def gap_width_windowed(eigs, target_ids, window=30):
    N = len(eigs)
    center = int(round(target_ids * N))
    lo = max(0, center - window)
    hi = min(N - 1, center + window)
    spacings = np.diff(eigs[lo:hi + 1])
    return float(spacings.max()) if len(spacings) > 0 else 0.0


def verify_gap_opening():
    """Verify gap-opening slopes and saturation values."""
    print("=" * 70)
    print("GAP-OPENING CURVE VERIFICATION")
    print("=" * 70)
    print(f"Target IDS: {TARGET_IDS[0]:.4f}, {TARGET_IDS[1]:.4f}, {TARGET_IDS[2]:.4f}")

    word7 = _word(7)
    N = len(word7)
    print(f"Depth 7: N = {N}, mean spacing ~ {4 / N:.5f}")

    # Perturbative regime (0.01 < ε < 0.05) for slope extraction
    eps_fit = np.array([0.01, 0.02, 0.03, 0.04, 0.05])
    slopes = []
    print(f"\n{'eps':>8} {'gap1/eps':>10} {'gap2/eps':>10} {'gap3/eps':>10}")
    for eps in eps_fit:
        eigs = tight_binding_spectrum(word7, eps)
        widths = [gap_width_windowed(eigs, t) for t in TARGET_IDS]
        print(f"{eps:8.3f} {widths[0] / eps:10.4f} {widths[1] / eps:10.4f} {widths[2] / eps:10.4f}")

    # Linear fit through origin
    print("\n--- Linear slopes (fit 0.01-0.05, depth 7) ---")
    for g in range(3):
        w = np.array([gap_width_windowed(tight_binding_spectrum(word7, e), TARGET_IDS[g])
                       for e in eps_fit])
        slope = np.sum(eps_fit * w) / np.sum(eps_fit ** 2)
        slopes.append(slope)
        claimed = [0.184, 0.153, 0.0][g]
        print(f"  Gap {g + 1}: slope = {slope:.4f}  (handoff: {claimed})")

    ratio12 = slopes[0] / slopes[1]
    ratio23 = slopes[1] / slopes[2]
    print(f"\n  Ratio slope1/slope2 = {ratio12:.4f}  (handoff: 1.204)")
    print(f"  Ratio slope2/slope3 = {ratio23:.4f}  (gaps 2 and 3 open at same rate)")
    print(f"  √(1/φ²+1) = {np.sqrt(1 / PHI ** 2 + 1):.4f}  (handoff's identification)")

    # Full curve for saturation check
    print("\n--- Full gap-opening curve (depth 7) ---")
    eps_full = [0.1, 0.2, 0.5, 1.0, 2.0, 3.0, 5.0]
    print(f"{'eps':>8} {'gap1':>10} {'gap2':>10} {'gap3':>10}")
    for eps in eps_full:
        eigs = tight_binding_spectrum(word7, eps)
        widths = [gap_width_windowed(eigs, t) for t in TARGET_IDS]
        print(f"{eps:8.2f} {widths[0]:10.4f} {widths[1]:10.4f} {widths[2]:10.4f}")

    # Saturation comparison
    eigs5 = tight_binding_spectrum(word7, 5.0)
    sat = [gap_width_windowed(eigs5, t) for t in TARGET_IDS]
    claimed_sat = [1.10, 2.82, 0.71]
    print("\n--- Saturation at ε=5 ---")
    for g in range(3):
        match = abs(sat[g] - claimed_sat[g]) < 0.02
        print(f"  Gap {g + 1}: {sat[g]:.4f}  (handoff: {claimed_sat[g]})  {'✓' if match else '✗'}")

    # Convergence across depths
    print("\n--- Convergence (ε=1.0) ---")
    for depth in [5, 6, 7]:
        w = _word(depth)
        eigs = tight_binding_spectrum(w, 1.0)
        widths = [gap_width_windowed(eigs, t) for t in TARGET_IDS]
        print(f"  Depth {depth} (N={len(w)}): {widths[0]:.4f} / {widths[1]:.4f} / {widths[2]:.4f}")

    return dict(slopes=slopes, ratio12=ratio12, ratio23=ratio23, saturation=sat)


def verify_corrections():
    """Summarize corrections to the handoff."""
    print("\n" + "=" * 70)
    print("CORRECTIONS")
    print("=" * 70)
    print("""
  1. Gap 1 slope: 0.193, NOT 0.184 (5% error, may shift with larger N).
  2. Gap 3: opens LINEARLY with slope ≈ 0.155, NOT quadratically.
     The handoff's "opens more slowly / nearly zero at ε<0.3" was an artifact
     of insufficient system size or wrong gap identification.
  3. Slope ratio: ≈ 1.25, NOT 1.204. The identification √(1/φ²+1) = 1.176
     does not match either value — this is numerology.
  4. slope2 ≈ slope3 (ratio 1.0006): a NEW structural fact not in the handoff.
     Gaps 2 and 3 open at essentially identical rates.
  5. Saturation values (ε=5): CORRECT — gap1=1.10, gap2=2.82, gap3=0.71.
  6. Gap 3 convergence: 15-20% fluctuation between approximant levels,
     as the handoff noted. The other two gaps converge tightly.
""")


if __name__ == "__main__":
    r = verify_gap_opening()
    verify_corrections()
