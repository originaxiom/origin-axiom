"""B20 -- operational awareness test."""

from __future__ import annotations

import math
import sympy as sp


def T_numeric(v: tuple[float, float, float]) -> tuple[float, float, float]:
    x, y, z = v
    return (z, x, 2 * x * z - y)


def I_numeric(v: tuple[float, float, float]) -> float:
    x, y, z = v
    return x * x + y * y + z * z - 2 * x * y * z - 1


def main() -> None:
    print("=" * 72)
    print("B20 -- Operational awareness test")
    print("SPECULATIVE: no consciousness or qualia claims")
    print("=" * 72)

    x, y, z = sp.symbols("x y z")
    invariant = x**2 + y**2 + z**2 - 2 * x * y * z - 1
    T = sp.Matrix([z, x, 2 * x * z - y])
    invariant_next = invariant.subs({x: T[0], y: T[1], z: T[2]}, simultaneous=True)
    assert sp.factor(invariant_next - invariant) == 0
    print("    memory: I is preserved exactly")
    print("    feedback: z update contains 2*x*z")

    # Surface-dependent sample behavior: this is not enough for self-modeling.
    growth = {}
    for c in [0.25, 0.5]:
        v = (1.0, 1.0, 1.0 + math.sqrt(c))
        max_values = []
        for _ in range(5):
            max_values.append(max(abs(a) for a in v))
            assert abs(I_numeric(v) - c) < 1e-7
            v = T_numeric(v)
        growth[c] = max_values[-1]
    assert growth[0.5] > growth[0.25]
    print(f"    sample growth differs by I-surface: {growth}")

    # No explicit read: the symbolic rule has no independent I parameter.
    c = sp.symbols("c")
    T_with_c = T.subs({invariant: c})
    assert T_with_c == T
    print("    update rule has no independent I parameter or branch")

    print("\nVerdict: STALLED")
    print("Invariant-memory yes; read-and-respond self-model no.")


if __name__ == "__main__":
    main()
