"""B25 -- Fibonacci spectrum anchor.

This is a controlled replacement for the local exploratory spectrum scripts.
It keeps the useful finite-approximant numerics and rejects overclaims:

* box-counting estimates are finite-approximant slopes, not exact Hausdorff
  dimensions;
* gap labeling is a known Fibonacci-Hamiltonian control, not a discovery;
* lambda=1 is classified explicitly as motivated rather than derived.
"""

from __future__ import annotations

import argparse
from typing import NamedTuple

import numpy as np
from scipy.linalg import eigh_tridiagonal


PHI = (1.0 + np.sqrt(5.0)) / 2.0
SUTO_LOWER_BOUND = np.log(2.0) / (2.0 * np.log(PHI))


class SpectrumStats(NamedTuple):
    word_index: int
    length: int
    bandwidth: float
    median_spacing: float
    max_gap: float
    gap_count: int
    top_gap_matches: int
    top_gap_count: int
    top_gap_max_residual: float
    dimension_mid: float
    dimension_wide: float
    dimension_late: float


def fibonacci_word(word_index: int) -> list[int]:
    """Return the finite Fibonacci word used by the local scripts.

    With this convention `word_index=20` has length 10946. The label is a word
    index, not the standard Fibonacci subscript.
    """

    if word_index <= 0:
        raise ValueError("word_index must be positive")
    if word_index == 1:
        return [1]
    a, b = [0], [1]
    for _ in range(word_index - 1):
        a, b = b, b + a
    return b


def fibonacci_eigenvalues(word_index: int, lam: float) -> np.ndarray:
    word = fibonacci_word(word_index)
    diagonal = np.array([lam if symbol == 1 else 0.0 for symbol in word])
    off_diagonal = np.ones(len(word) - 1)
    return np.sort(eigh_tridiagonal(diagonal, off_diagonal, check_finite=False)[0])


def best_gap_label_residual(idos: float, q_max: int = 50) -> float:
    best = 1.0
    for q in range(-q_max, q_max + 1):
        if q == 0:
            continue
        predicted = (q / PHI) % 1.0
        residual = min(abs(idos - predicted), abs(idos - 1.0 + predicted))
        best = min(best, residual)
    return best


def box_slopes(eigenvalues: np.ndarray) -> tuple[float, float, float]:
    bandwidth = float(eigenvalues[-1] - eigenvalues[0])
    spacings = np.diff(eigenvalues)
    min_spacing = float(np.min(spacings[spacings > 0.0]))

    log_eps: list[float] = []
    log_boxes: list[float] = []
    for k in range(4, 20):
        eps = bandwidth / (2**k)
        if eps < min_spacing * 0.5:
            break
        boxes = len(np.unique(((eigenvalues - eigenvalues[0]) / eps).astype(np.int64)))
        log_eps.append(float(np.log(1.0 / eps)))
        log_boxes.append(float(np.log(boxes)))

    if len(log_eps) < 8:
        raise AssertionError("not enough scales for a controlled slope estimate")

    x = np.array(log_eps)
    y = np.array(log_boxes)

    def slope(start: int, end: int) -> float:
        return float(np.polyfit(x[start:end], y[start:end], 1)[0])

    n = len(x)
    mid = slope(max(1, n // 4), min(n - 1, 3 * n // 4))
    wide = slope(1, n - 2)
    late = slope(max(1, n // 2), n - 1)
    return mid, wide, late


def analyze_approximant(word_index: int, lam: float, top_n_gaps: int) -> SpectrumStats:
    eigenvalues = fibonacci_eigenvalues(word_index, lam)
    spacings = np.diff(eigenvalues)
    median_spacing = float(np.median(spacings))
    gap_mask = spacings > 5.0 * median_spacing
    gap_widths = spacings[gap_mask]
    gap_starts = eigenvalues[:-1][gap_mask]
    order = np.argsort(gap_widths)[::-1]
    top = order[: min(top_n_gaps, len(order))]

    residuals: list[float] = []
    for gap_index in top:
        idos = float(np.sum(eigenvalues < gap_starts[gap_index]) / len(eigenvalues))
        residuals.append(best_gap_label_residual(idos))

    dim_mid, dim_wide, dim_late = box_slopes(eigenvalues)

    return SpectrumStats(
        word_index=word_index,
        length=len(eigenvalues),
        bandwidth=float(eigenvalues[-1] - eigenvalues[0]),
        median_spacing=median_spacing,
        max_gap=float(np.max(gap_widths)),
        gap_count=len(gap_widths),
        top_gap_matches=sum(residual < 5e-4 for residual in residuals),
        top_gap_count=len(residuals),
        top_gap_max_residual=max(residuals) if residuals else float("nan"),
        dimension_mid=dim_mid,
        dimension_wide=dim_wide,
        dimension_late=dim_late,
    )


def lambda_status(lam: float) -> str:
    invariant = lam**2 / 4.0
    if abs(lam - 1.0) < 1e-12 and abs(invariant - 0.25) < 1e-12:
        return "MOTIVATED"
    return "INSERTED"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda-value", type=float, default=1.0)
    parser.add_argument(
        "--word-indices",
        type=int,
        nargs="+",
        default=[14, 16, 18, 20],
        help="Finite Fibonacci word indices. Index 20 has length 10946.",
    )
    parser.add_argument("--top-gaps", type=int, default=20)
    args = parser.parse_args()

    print("=" * 72)
    print("B25 -- Fibonacci spectrum anchor")
    print("SPECULATIVE: finite-approximant numerics only")
    print("=" * 72)

    stats = [analyze_approximant(index, args.lambda_value, args.top_gaps) for index in args.word_indices]

    print("\n[1] finite-approximant convergence")
    print(
        "    idx length bandwidth max_gap gap_count "
        "top_gap_matches max_resid dim_mid dim_wide dim_late"
    )
    for row in stats:
        print(
            f"    {row.word_index:>3} {row.length:>6} "
            f"{row.bandwidth:>9.5f} {row.max_gap:>8.5f} {row.gap_count:>5} "
            f"{row.top_gap_matches:>2}/{row.top_gap_count:<2} "
            f"{row.top_gap_max_residual:>9.6f} "
            f"{row.dimension_mid:>7.4f} {row.dimension_wide:>8.4f} {row.dimension_late:>8.4f}"
        )

    last = stats[-1]
    assert last.top_gap_matches == last.top_gap_count
    assert last.top_gap_max_residual < 5e-4
    assert 0.65 < last.dimension_mid < 0.85
    assert last.dimension_mid > SUTO_LOWER_BOUND

    print("\n[2] lambda=1 bridge status")
    invariant = args.lambda_value**2 / 4.0
    status = lambda_status(args.lambda_value)
    print(f"    I0(lambda)=lambda^2/4 = {invariant:.6f}")
    print(f"    lambda status: {status}")
    assert status == "MOTIVATED"

    print("\nVerdict: STALLED")
    print("Finite spectra give a strong anchor; lambda=1 is motivated, not derived.")


if __name__ == "__main__":
    main()
