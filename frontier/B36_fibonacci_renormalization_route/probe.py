"""B36 -- Fibonacci renormalization route.

Checks whether finite spectral/gap-label controls independently select
lambda/h=1, or whether they reuse the B26 invariant-surface selector.
"""

from __future__ import annotations

from typing import NamedTuple

import numpy as np
import sympy as sp
from scipy.linalg import eigh_tridiagonal


PHI = (1.0 + np.sqrt(5.0)) / 2.0


class GapControl(NamedTuple):
    coupling: float
    matches: int
    count: int
    max_residual: float


def fibonacci_word(word_index: int) -> list[int]:
    if word_index == 1:
        return [1]
    a, b = [0], [1]
    for _ in range(word_index - 1):
        a, b = b, b + a
    return b


def eigenvalues(word_index: int, coupling: float) -> np.ndarray:
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


def gap_control(coupling: float, word_index: int = 16, top_n: int = 10) -> GapControl:
    values = eigenvalues(word_index, coupling)
    spacings = np.diff(values)
    gap_mask = spacings > 5.0 * float(np.median(spacings))
    gap_widths = spacings[gap_mask]
    gap_starts = values[:-1][gap_mask]
    order = np.argsort(gap_widths)[::-1][:top_n]
    residuals = []
    for gap_index in order:
        idos = float(np.sum(values < gap_starts[gap_index]) / len(values))
        residuals.append(best_gap_label_residual(idos))
    return GapControl(coupling, sum(r < 5e-3 for r in residuals), len(residuals), max(residuals))


def main() -> None:
    print("=" * 72)
    print("B36 -- Fibonacci renormalization route")
    print("SPECULATIVE: observations only, not claims")
    print("=" * 72)

    energy, coupling, hopping = sp.symbols("E g h", positive=True)
    x = (energy - coupling) / (2 * hopping)
    y = energy / (2 * hopping)
    z = sp.Integer(1)
    invariant = sp.simplify(x**2 + y**2 + z**2 - 2 * x * y * z - 1)
    print("\n[1] invariant line")
    print(f"    I = {invariant}")
    assert invariant == coupling**2 / (4 * hopping**2)

    print("\n[2] B26 selected surface")
    selected_ratio_squared = sp.solve(sp.Eq((coupling / hopping) ** 2 / 4, sp.Rational(1, 4)), (coupling / hopping) ** 2)[0]
    print(f"    I=1/4 gives (lambda/h)^2 = {selected_ratio_squared}")
    assert selected_ratio_squared == 1

    print("\n[3] gap-label controls do not uniquely select coupling")
    for value in [0.5, 1.0, float(np.sqrt(5.0)), 4.0]:
        control = gap_control(value)
        print(
            f"    lambda/h={value:.6f}: top gaps {control.matches}/{control.count}, "
            f"max_resid={control.max_residual:.6f}"
        )
        assert control.matches == control.count
        assert control.max_residual < 5e-3

    print("\nVerdict: STALLED")
    print("Fibonacci spectral controls are compatible with lambda/h=1 but do not")
    print("select it independently of the B26 A-sector criterion.")


if __name__ == "__main__":
    main()
