"""B23 -- BKL/gravity controls."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    print("=" * 72)
    print("B23 -- BKL/gravity controls")
    print("SPECULATIVE: observations only, not claims")
    print("=" * 72)

    u, v, w = sp.symbols("u v w")
    x, y, z = 1 + u, 1 + v, 1 + w
    T = sp.Matrix([z, x, 2 * x * z - y])
    perturbation = sp.Matrix([sp.expand(component - 1) for component in T])
    expected = sp.Matrix([w, u, 2 * u - v + 2 * w + 2 * u * w])
    assert perturbation == expected
    linear = sp.Matrix([w, u, 2 * u - v + 2 * w])
    nonlinear = perturbation - linear
    assert nonlinear == sp.Matrix([0, 0, 2 * u * w])
    print(f"    perturbation map = {tuple(perturbation)}")
    print("    only nonlinear term = 2*u*w")

    print("\nVerdict: STALLED")
    print("Nonlinear bounce-like term isolated; no BKL variable dictionary derived.")


if __name__ == "__main__":
    main()
