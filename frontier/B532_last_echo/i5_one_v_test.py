"""
B532-I5A: The one-V test.

Question: does measuring ONE band old-weight determine all the others?

Method: scan over a 1-parameter family of potentials V = λ·(0,1,2,3) and
a 2-parameter family V = (0, α, β, α+β). For each, compute the four band
old-weights. If the 1-param family traces a CURVE in (w1,w2,w3,w4) space,
then one measurement determines the rest. If the 2-param family traces a
SURFACE, then two measurements are needed.

Also: check whether the functional relationship w_i(λ) is UNIVERSAL
(independent of the potential shape) or V-specific.
"""

import numpy as np
from collections import Counter

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}


def grow(letter, depth):
    word = letter
    for _ in range(depth):
        word = ''.join(SUB[c] for c in word)
    return word


def band_weights(word, V_values):
    N = len(word)
    is_old = np.array([c in 'ab' for c in word], dtype=bool)

    V = np.array([V_values[c] for c in word])
    H = np.diag(V)
    for i in range(N - 1):
        H[i, i + 1] = 1.0
        H[i + 1, i] = 1.0
    H[0, N - 1] = 1.0
    H[N - 1, 0] = 1.0

    evals, evecs = np.linalg.eigh(H)
    idx = np.argsort(evals)
    evals = evals[idx]
    evecs = evecs[:, idx]

    diffs = np.diff(evals)
    top3 = sorted(np.argsort(diffs)[-3:])
    gap_ids = [(g + 1) / N for g in top3]

    # Check gaps are at letter frequencies
    expected = [0.272, 0.440, 0.786]
    at_freqs = all(abs(gi - ex) < 0.015 for gi, ex in zip(gap_ids, expected))
    if not at_freqs:
        return None  # gaps not at letter frequencies for this V

    boundaries = [0] + [g + 1 for g in top3] + [N]
    weights = []
    for i in range(4):
        s, e = boundaries[i], boundaries[i + 1]
        if e > s:
            w = np.mean([np.sum(np.abs(evecs[:, k][is_old]) ** 2) for k in range(s, e)])
        else:
            w = float('nan')
        weights.append(w)
    return weights


def main():
    DEPTH = 6
    word = grow('a', DEPTH)
    N = len(word)
    print(f"Word length: {N}")

    # ================================================================
    # PART 1: 1-parameter scan V = λ·(0,1,2,3)
    # ================================================================
    print("\n" + "=" * 70)
    print("PART 1: V = λ·(0,1,2,3) — one-parameter family")
    print("=" * 70)

    lambdas = np.linspace(0.3, 5.0, 50)
    results_1p = []

    for lam in lambdas:
        V = {'a': 0.0, 'b': lam, 'A': 2 * lam, 'B': 3 * lam}
        w = band_weights(word, V)
        if w is not None:
            results_1p.append((lam, w))

    print(f"Valid points: {len(results_1p)}/{len(lambdas)}")
    print(f"\n{'λ':>6} {'w1(old)':>8} {'w2(old)':>8} {'w3(old)':>8} {'w4(old)':>8}")
    print("-" * 45)
    for lam, w in results_1p[::5]:
        print(f"{lam:6.2f} {w[0]:8.4f} {w[1]:8.4f} {w[2]:8.4f} {w[3]:8.4f}")

    # Check: is w2 a function of w1?
    w1 = np.array([r[1][0] for r in results_1p])
    w2 = np.array([r[1][1] for r in results_1p])
    w3 = np.array([r[1][2] for r in results_1p])
    w4 = np.array([r[1][3] for r in results_1p])

    # Fit w2 = f(w1) — polynomial
    coeffs_21 = np.polyfit(w1, w2, 4)
    w2_pred = np.polyval(coeffs_21, w1)
    resid_21 = np.max(np.abs(w2 - w2_pred))
    print(f"\nw2 = poly4(w1): max residual = {resid_21:.6f}")

    coeffs_31 = np.polyfit(w1, w3, 4)
    w3_pred = np.polyval(coeffs_31, w1)
    resid_31 = np.max(np.abs(w3 - w3_pred))
    print(f"w3 = poly4(w1): max residual = {resid_31:.6f}")

    coeffs_41 = np.polyfit(w1, w4, 4)
    w4_pred = np.polyval(coeffs_41, w1)
    resid_41 = np.max(np.abs(w4 - w4_pred))
    print(f"w4 = poly4(w1): max residual = {resid_41:.6f}")

    # ================================================================
    # PART 2: 2-parameter scan — different potential SHAPES
    # ================================================================
    print("\n" + "=" * 70)
    print("PART 2: Multiple potential shapes — is the curve universal?")
    print("=" * 70)

    shapes = {
        '(0,1,2,3)': lambda l: {'a': 0, 'b': l, 'A': 2*l, 'B': 3*l},
        '(0,1,3,4)': lambda l: {'a': 0, 'b': l, 'A': 3*l, 'B': 4*l},
        '(0,2,3,5)': lambda l: {'a': 0, 'b': 2*l, 'A': 3*l, 'B': 5*l},
        '(-1,0,1,2)': lambda l: {'a': -l, 'b': 0, 'A': l, 'B': 2*l},
        '(-2,-1,1,2)': lambda l: {'a': -2*l, 'b': -l, 'A': l, 'B': 2*l},
        '(0,0.5,1.5,2)': lambda l: {'a': 0, 'b': 0.5*l, 'A': 1.5*l, 'B': 2*l},
        '(0,1,1,2)': lambda l: {'a': 0, 'b': l, 'A': l, 'B': 2*l},
    }

    all_w1 = []
    all_w2 = []
    all_w3 = []
    all_w4 = []
    all_labels = []

    for name, vfunc in shapes.items():
        lams = np.linspace(0.3, 4.0, 30)
        shape_w1, shape_w2, shape_w3, shape_w4 = [], [], [], []
        for lam in lams:
            V = vfunc(lam)
            w = band_weights(word, V)
            if w is not None:
                shape_w1.append(w[0])
                shape_w2.append(w[1])
                shape_w3.append(w[2])
                shape_w4.append(w[3])
                all_labels.append(name)

        all_w1.extend(shape_w1)
        all_w2.extend(shape_w2)
        all_w3.extend(shape_w3)
        all_w4.extend(shape_w4)

        if shape_w1:
            print(f"\n  {name}: {len(shape_w1)} valid pts, "
                  f"w1=[{min(shape_w1):.3f},{max(shape_w1):.3f}], "
                  f"w2=[{min(shape_w2):.3f},{max(shape_w2):.3f}]")

    # Now check: across ALL shapes, is w2 still a function of w1?
    all_w1 = np.array(all_w1)
    all_w2 = np.array(all_w2)
    all_w3 = np.array(all_w3)
    all_w4 = np.array(all_w4)

    print(f"\nTotal data points across all shapes: {len(all_w1)}")

    # Fit w2 = f(w1) across all shapes
    coeffs_21_all = np.polyfit(all_w1, all_w2, 6)
    w2_pred_all = np.polyval(coeffs_21_all, all_w1)
    resid_21_all = np.max(np.abs(all_w2 - w2_pred_all))
    rmse_21_all = np.sqrt(np.mean((all_w2 - w2_pred_all) ** 2))
    print(f"\nw2 = poly6(w1) across ALL shapes:")
    print(f"  max residual = {resid_21_all:.6f}")
    print(f"  RMSE = {rmse_21_all:.6f}")

    coeffs_31_all = np.polyfit(all_w1, all_w3, 6)
    w3_pred_all = np.polyval(coeffs_31_all, all_w1)
    resid_31_all = np.max(np.abs(all_w3 - w3_pred_all))
    rmse_31_all = np.sqrt(np.mean((all_w3 - w3_pred_all) ** 2))
    print(f"\nw3 = poly6(w1) across ALL shapes:")
    print(f"  max residual = {resid_31_all:.6f}")
    print(f"  RMSE = {rmse_31_all:.6f}")

    coeffs_41_all = np.polyfit(all_w1, all_w4, 6)
    w4_pred_all = np.polyval(coeffs_41_all, all_w1)
    resid_41_all = np.max(np.abs(all_w4 - w4_pred_all))
    rmse_41_all = np.sqrt(np.mean((all_w4 - w4_pred_all) ** 2))
    print(f"\nw4 = poly6(w1) across ALL shapes:")
    print(f"  max residual = {resid_41_all:.6f}")
    print(f"  RMSE = {rmse_41_all:.6f}")

    # Check if the different shapes trace DIFFERENT curves
    # by computing the spread of w2 values at similar w1 values
    print("\n" + "=" * 70)
    print("UNIVERSALITY TEST: spread of w2 at fixed w1")
    print("=" * 70)

    bins = np.linspace(0.65, 0.98, 12)
    for i in range(len(bins) - 1):
        lo, hi = bins[i], bins[i + 1]
        mask = (all_w1 >= lo) & (all_w1 < hi)
        if mask.sum() >= 3:
            w2_in_bin = all_w2[mask]
            spread = w2_in_bin.max() - w2_in_bin.min()
            print(f"  w1 in [{lo:.2f},{hi:.2f}): {mask.sum()} pts, "
                  f"w2 in [{w2_in_bin.min():.4f},{w2_in_bin.max():.4f}], "
                  f"spread = {spread:.4f}")

    # ================================================================
    # PART 3: Complementarity constraint w1+w2+w3+w4 vs completeness
    # ================================================================
    print("\n" + "=" * 70)
    print("PART 3: Sum constraint and completeness")
    print("=" * 70)

    # The old-weights across bands must satisfy:
    # sum over bands of (n_band * w_old_band) = total_old_count
    # That is: count(a)*w1 + count(b)*w2 + count(A)*w3 + count(B)*w4 = count(a)+count(b)
    # (each eigenstate's |psi|^2 sums to 1; the total old probability = old fraction)

    counts = Counter(word)
    f_a = counts['a'] / N
    f_b = counts['b'] / N
    f_A = counts['A'] / N
    f_B = counts['B'] / N
    f_old = f_a + f_b

    print(f"Frequencies: f_a={f_a:.4f}, f_b={f_b:.4f}, f_A={f_A:.4f}, f_B={f_B:.4f}")
    print(f"Sum constraint: f_a*w1 + f_b*w2 + f_A*w3 + f_B*w4 = f_old = {f_old:.4f}")

    constraint_violations = f_a * all_w1 + f_b * all_w2 + f_A * all_w3 + f_B * all_w4
    print(f"Constraint value across all {len(all_w1)} points:")
    print(f"  min = {constraint_violations.min():.6f}")
    print(f"  max = {constraint_violations.max():.6f}")
    print(f"  This MUST equal f_old = {f_old:.4f}")

    # So the constraint is: f_a*w1 + f_b*w2 + f_A*w3 + f_B*w4 = f_old
    # This means given w1, w2, w3, w4 lives on a 3-dimensional hyperplane.
    # If the data also lives on a curve (1D), then 2 additional constraints
    # beyond the sum rule are needed — meaning the substitution structure
    # imposes 2 more functional relationships.

    # Test: with the sum constraint, can we predict w4 from w1, w2, w3?
    w4_from_sum = (f_old - f_a * all_w1 - f_b * all_w2 - f_A * all_w3) / f_B
    resid_sum = np.max(np.abs(all_w4 - w4_from_sum))
    print(f"\nw4 from sum constraint: max residual = {resid_sum:.8f}")

    # So 3 weights determine the 4th via the sum rule.
    # But does the data live on a CURVE (1D) or a SURFACE (2D)?
    # If curve: w1 alone determines w2, w3, w4.
    # If surface: w1 alone is not enough; need (w1, w2) to determine (w3, w4).

    # Dimensionality test: PCA on (w1, w2, w3, w4)
    W = np.column_stack([all_w1, all_w2, all_w3, all_w4])
    W_centered = W - W.mean(axis=0)
    cov = np.cov(W_centered.T)
    eigvals = np.sort(np.linalg.eigvalsh(cov))[::-1]
    print(f"\nPCA eigenvalues of (w1,w2,w3,w4): {eigvals}")
    print(f"Explained variance: {eigvals / eigvals.sum()}")
    print(f"First component explains: {eigvals[0]/eigvals.sum()*100:.1f}%")
    print(f"First two components explain: {(eigvals[0]+eigvals[1])/eigvals.sum()*100:.1f}%")

    dim_estimate = np.sum(eigvals / eigvals.sum() > 0.01)
    print(f"Estimated dimensionality (>1% variance): {dim_estimate}")


if __name__ == '__main__':
    main()
