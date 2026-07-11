"""
T2 — Control substitution: Arnoux-Rauzy on 4 letters.

σ_AR: a→ab, b→ac, c→ad, d→a
Perron root β_AR ≈ 1.928, Pisot, primitive (M^4 > 0).
Second real eigenvalue ≈ −0.775 (negative, like ours).

Binary potential: V = 0 for {a,b}, V = ε for {c,d}.
"""
import numpy as np
from scipy.linalg import eigh_tridiagonal

SUB_CTRL = {'a': 'ab', 'b': 'ac', 'c': 'ad', 'd': 'a'}
ALPH_CTRL = 'abcd'
M_CTRL = np.array([[1, 1, 1, 1], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]], float)
HIGH_LETTERS = 'cd'


def _word_ctrl(depth):
    u = 'a'
    for _ in range(depth):
        u = ''.join(SUB_CTRL[c] for c in u)
    return u


def verify_pisot_primitive():
    """Verify Pisot and primitivity properties."""
    evals = np.linalg.eigvals(M_CTRL)
    perron = max(abs(evals))
    conjugates = [abs(e) for e in evals if abs(e) < perron - 0.01]
    pisot = all(c < 1 for c in conjugates)

    Mk = np.linalg.matrix_power(M_CTRL, 4)
    primitive = np.all(Mk > 0)

    print("=" * 70)
    print("CONTROL VERIFICATION: Arnoux-Rauzy 4-letter")
    print("=" * 70)
    print(f"  Substitution: a→ab, b→ac, c→ad, d→a")
    print(f"  Eigenvalues: {np.sort(evals.real)[::-1]}")
    print(f"  Perron root: {perron:.6f}")
    print(f"  Conjugate moduli: {conjugates}")
    print(f"  Pisot: {pisot}")
    print(f"  Primitive (M^4 > 0): {primitive}")
    print(f"  Second real eigenvalue: {sorted(evals.real)[-2]:.6f}")

    perron_vec = np.linalg.eig(M_CTRL)[1][:, np.argmax(abs(evals))]
    perron_vec = abs(perron_vec) / abs(perron_vec).sum()
    print(f"  Perron frequencies: {perron_vec}")

    return pisot, primitive, perron, perron_vec


def gap_labels_ctrl():
    """Compute topological gap labels (cumulative Perron frequencies)."""
    evals, V = np.linalg.eig(M_CTRL)
    i_perr = np.argmax(abs(evals))
    perron_vec = abs(V[:, i_perr])
    perron_vec = perron_vec / perron_vec.sum()

    freqs = perron_vec
    cum = np.cumsum(freqs)
    gaps_ids = sorted(cum[:-1])

    return freqs, gaps_ids


def gap_widths_ctrl(word, eps, target_ids, window=30):
    """Compute gap widths at target IDS positions."""
    N = len(word)
    diag = np.array([eps if c in HIGH_LETTERS else 0.0 for c in word])
    off = np.ones(N - 1)
    widths = []
    for t in target_ids:
        center = int(round(t * N))
        lo = max(0, center - window)
        hi = min(N - 1, center + window)
        eigs = eigh_tridiagonal(diag, off, eigvals_only=True,
                                select='i', select_range=(lo, hi))
        spacings = np.diff(eigs)
        widths.append(float(spacings.max()))
    return widths


def slope_convergence_ctrl(depths=None, eps_values=None):
    """Compute gap-opening slopes for the control substitution."""
    freqs, gap_ids = gap_labels_ctrl()

    if depths is None:
        depths = list(range(8, 20))
    if eps_values is None:
        eps_values = np.array([0.01, 0.02, 0.03, 0.04, 0.05])

    print("\n" + "=" * 70)
    print("T2 — CONTROL SLOPE CONVERGENCE (Arnoux-Rauzy 4-letter)")
    print("=" * 70)
    print(f"  Gap IDS positions: {[f'{g:.6f}' for g in gap_ids]}")
    print(f"  Perron frequencies: {[f'{f:.6f}' for f in freqs]}")
    n_gaps = len(gap_ids)
    header = f"{'Depth':>5} {'N':>9}"
    for g in range(n_gaps):
        header += f" {'s'+str(g+1):>8}"
    if n_gaps >= 2:
        header += f" {'s1/s2':>8}"
    print(header)

    results = {}
    for depth in depths:
        word = _word_ctrl(depth)
        N = len(word)
        if N > 5_000_000:
            break

        widths_per_gap = [[] for _ in range(n_gaps)]
        for eps in eps_values:
            ws = gap_widths_ctrl(word, eps, gap_ids)
            for g in range(n_gaps):
                widths_per_gap[g].append(ws[g])

        slopes = []
        for g in range(n_gaps):
            w_arr = np.array(widths_per_gap[g])
            slopes.append(np.sum(eps_values * w_arr) / np.sum(eps_values ** 2))

        ratio = slopes[0] / slopes[1] if len(slopes) >= 2 and slopes[1] > 0 else float('inf')
        line = f"{depth:>5} {N:>9}"
        for s in slopes:
            line += f" {s:>8.4f}"
        if n_gaps >= 2:
            line += f" {ratio:>8.4f}"
        print(line)
        results[depth] = {'slopes': slopes, 'ratio': ratio, 'N': N}

    return results


def even_odd_analysis_ctrl(results):
    """Check if the control also shows even/odd alternation."""
    print("\n" + "=" * 70)
    print("CONTROL EVEN/ODD ANALYSIS")
    print("=" * 70)

    n_gaps = len(next(iter(results.values()))['slopes'])
    for g in range(n_gaps):
        even = [results[d]['slopes'][g] for d in sorted(results) if d % 2 == 0 and d >= 12]
        odd = [results[d]['slopes'][g] for d in sorted(results) if d % 2 == 1 and d >= 13]
        if even and odd:
            e_mean, o_mean = np.mean(even), np.mean(odd)
            amplitude = abs(e_mean - o_mean)
            avg = (e_mean + o_mean) / 2
            print(f"  Gap {g+1}: even={e_mean:.4f}  odd={o_mean:.4f}  "
                  f"amplitude={amplitude:.4f}  relative={amplitude/avg*100:.1f}%")


if __name__ == "__main__":
    verify_pisot_primitive()
    results = slope_convergence_ctrl()
    even_odd_analysis_ctrl(results)
