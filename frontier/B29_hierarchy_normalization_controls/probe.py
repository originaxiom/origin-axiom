"""B29 -- hierarchy and normalization controls.

Separates the B26 projective Lucas hierarchy from literal full-return controls
and from the absolute normalization of the Fibonacci Hamiltonian coupling.
"""

from __future__ import annotations

from typing import NamedTuple

import numpy as np
import sympy as sp
from scipy.linalg import eigh_tridiagonal


PHI = (1.0 + np.sqrt(5.0)) / 2.0


class SpectralControl(NamedTuple):
    coupling: float
    length: int
    bandwidth: float
    gap_count: int
    top_gap_max_residual: float
    top_gap_matches: int


def fibonacci_word(word_index: int) -> list[int]:
    if word_index <= 0:
        raise ValueError("word_index must be positive")
    if word_index == 1:
        return [1]
    a, b = [0], [1]
    for _ in range(word_index - 1):
        a, b = b, b + a
    return b


def fibonacci_eigenvalues(word_index: int, coupling: float) -> np.ndarray:
    word = fibonacci_word(word_index)
    diagonal = np.array([coupling if symbol == 1 else 0.0 for symbol in word])
    off_diagonal = np.ones(len(word) - 1)
    return np.sort(eigh_tridiagonal(diagonal, off_diagonal, check_finite=False)[0])


def best_gap_label_residual(idos: float, q_max: int = 80) -> float:
    best = 1.0
    for q in range(-q_max, q_max + 1):
        if q == 0:
            continue
        predicted = (q / PHI) % 1.0
        residual = min(abs(idos - predicted), abs(idos - 1.0 + predicted))
        best = min(best, residual)
    return best


def analyze_spectrum(word_index: int, coupling: float, top_n_gaps: int = 10) -> SpectralControl:
    eigenvalues = fibonacci_eigenvalues(word_index, coupling)
    spacings = np.diff(eigenvalues)
    median_spacing = float(np.median(spacings))
    gap_mask = spacings > 5.0 * median_spacing
    gap_widths = spacings[gap_mask]
    gap_starts = eigenvalues[:-1][gap_mask]
    order = np.argsort(gap_widths)[::-1]
    residuals: list[float] = []
    for gap_index in order[:top_n_gaps]:
        idos = float(np.sum(eigenvalues < gap_starts[gap_index]) / len(eigenvalues))
        residuals.append(best_gap_label_residual(idos))

    return SpectralControl(
        coupling=coupling,
        length=len(eigenvalues),
        bandwidth=float(eigenvalues[-1] - eigenvalues[0]),
        gap_count=len(gap_widths),
        top_gap_max_residual=max(residuals),
        top_gap_matches=sum(residual < 5e-3 for residual in residuals),
    )


def main() -> None:
    print("=" * 72)
    print("B29 -- hierarchy and normalization controls")
    print("SPECULATIVE: observations only, not claims")
    print("=" * 72)

    t = sp.symbols("t")
    energy, coupling, hopping = sp.symbols("E g h", positive=True)
    x = (energy - coupling) / (2 * hopping)
    y = energy / (2 * hopping)
    z = sp.Integer(1)
    invariant = sp.simplify(x**2 + y**2 + z**2 - 2 * x * y * z - 1)
    print("\n[1] Fibonacci Hamiltonian normalization")
    print(f"    I(E,g,h) = {invariant}")
    assert invariant == coupling**2 / (4 * hopping**2)

    print("\n[2] projective half-return Lucas hierarchy")
    F = sp.Matrix([[1, 1], [1, 0]])
    projective_values: list[sp.Expr] = []
    for n in range(2, 14, 2):
        lucas = sp.trace(F**n)
        hierarchy_i = sp.simplify((lucas - 2) / 4)
        hierarchy_g2 = sp.simplify(4 * hierarchy_i)
        hierarchy_c2 = sp.simplify(hierarchy_i + 1)
        projective_values.append(hierarchy_g2)
        half_return_quadratic = t**2 - (4 * hierarchy_c2 - 2) * t + 1
        target = (F**n).charpoly(t).as_expr()
        print(f"    n={n}: L_n={lucas}, I={hierarchy_i}, (lambda/h)^2={hierarchy_g2}")
        assert sp.factor(half_return_quadratic - target) == 0
    assert projective_values[:6] == [1, 5, 16, 45, 121, 320]

    print("\n[3] literal full-return control hierarchy")
    full_return_values: list[sp.Expr] = []
    expected_full_return = [
        sp.Integer(-3),
        sp.sqrt(5) - 4,
        sp.Integer(0),
        3 * sp.sqrt(5) - 4,
        sp.Integer(7),
        8 * sp.sqrt(5) - 4,
    ]
    for n in range(2, 14, 2):
        lucas = sp.trace(F**n)
        full_c2 = sp.sqrt(lucas - 2) / 4
        full_g2 = sp.simplify(4 * (full_c2 - 1))
        full_return_values.append(full_g2)
        full_return_quadratic = t**2 - (16 * full_c2**2 + 2) * t + 1
        target = (F**n).charpoly(t).as_expr()
        print(f"    n={n}: c^2={full_c2}, (lambda/h)^2={full_g2}")
        assert sp.factor(full_return_quadratic - target) == 0
    assert [sp.simplify(v - e) for v, e in zip(full_return_values, expected_full_return)] == [0] * 6

    print("\n[4] finite spectral controls at first projective hierarchy values")
    for selected in [1.0, float(np.sqrt(5.0)), 4.0]:
        control = analyze_spectrum(word_index=16, coupling=selected)
        print(
            f"    lambda/h={control.coupling:.6f}: N={control.length}, "
            f"bandwidth={control.bandwidth:.6f}, gaps={control.gap_count}, "
            f"top10={control.top_gap_matches}/10, max_resid={control.top_gap_max_residual:.6f}"
        )
        assert control.top_gap_matches == 10
        assert control.top_gap_max_residual < 5e-3

    print("\nVerdict: STALLED")
    print("The Lucas hierarchy selects dimensionless lambda/h values under the")
    print("projective criterion; the criterion itself remains unproved.")


if __name__ == "__main__":
    main()
