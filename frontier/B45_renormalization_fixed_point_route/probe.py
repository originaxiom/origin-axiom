"""B45 -- renormalization fixed-point route."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    print("=" * 72)
    print("B45 -- renormalization fixed-point route")
    print("SPECULATIVE: observations only, not claims")
    print("=" * 72)

    f = sp.Matrix([[1, 1], [1, 0]])
    values = []
    print("\n[1] Lucas hierarchy")
    for n in range(2, 16, 2):
        lucas = sp.trace(f**n)
        g2 = lucas - 2
        values.append((n, lucas, g2))
        print(f"    n={n}: L_n={lucas}, (lambda/h)^2={g2}")
    assert [item[2] for item in values[:5]] == [1, 5, 16, 45, 121]

    print("\n[2] primitive original-sector selector")
    primitive = values[0]
    print(f"    first even hyperbolic member = n={primitive[0]}, (lambda/h)^2={primitive[2]}")
    assert primitive == (2, 3, 1)

    print("\n[3] hierarchy control")
    ratios = [sp.Rational(values[i + 1][2], values[i][2]) for i in range(3)]
    print(f"    first ratios = {ratios}")
    assert values[1][2] != values[0][2]

    print("\nVerdict: CONDITIONAL")
    print("lambda/h=1 is the primitive hierarchy member if higher Lucas values")
    print("are classified as excited sectors; that classification is an assumption.")


if __name__ == "__main__":
    main()
