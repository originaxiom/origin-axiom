"""B31 -- primitive projective return selector.

Separates projective return from the extra A-sector matching rule.
"""

from __future__ import annotations

import sympy as sp


def trace_map(state: sp.Matrix) -> sp.Matrix:
    x, y, z = state
    return sp.Matrix([z, x, 2 * x * z - y])


def iterate(state: sp.Matrix, n: int) -> sp.Matrix:
    out = sp.Matrix(state)
    for _ in range(n):
        out = trace_map(out)
    return sp.simplify(out)


def main() -> None:
    print("=" * 72)
    print("B31 -- primitive projective return selector")
    print("SPECULATIVE: observations only, not claims")
    print("=" * 72)

    x, y, z, c, t = sp.symbols("x y z c t")
    state = sp.Matrix([x, y, z])
    point = sp.Matrix([0, 0, c])

    print("\n[1] primitive projective return")
    images = [iterate(point, n) for n in range(1, 4)]
    for n, image in enumerate(images, start=1):
        print(f"    T^{n}(0,0,c) = {tuple(image)}")
    assert images[2] == sp.Matrix([0, 0, -c])
    assert images[2] != point
    assert sp.Matrix([images[2][0], images[2][1], images[2][2] ** 2]) == sp.Matrix([0, 0, c**2])

    print("\n[2] projective return leaves I free")
    invariant_family = c**2 - 1
    print(f"    I = {invariant_family}")
    assert sp.diff(invariant_family, c) == 2 * c

    print("\n[3] A-sector matching selects I=1/4")
    jac_t3 = iterate(state, 3).jacobian(state).subs({x: 0, y: 0, z: c})
    char_t3 = sp.factor(jac_t3.charpoly(t).as_expr())
    expected = sp.factor((t + 1) * (t**2 - (4 * c**2 - 2) * t + 1))
    print(f"    char(DT^3) = {char_t3}")
    assert sp.expand(char_t3 - expected) == 0

    selected_c2 = sp.solve(sp.Eq(4 * c**2 - 2, 3), c**2)[0]
    selected_i = sp.simplify(selected_c2 - 1)
    selected_g2 = sp.simplify(4 * selected_i)
    print(f"    A-sector match: c^2={selected_c2}, I={selected_i}, (lambda/h)^2={selected_g2}")
    assert selected_c2 == sp.Rational(5, 4)
    assert selected_i == sp.Rational(1, 4)
    assert selected_g2 == 1

    print("\n[4] higher A-like matches are a hierarchy, not uniqueness")
    F = sp.Matrix([[1, 1], [1, 0]])
    matches = []
    for n in range(2, 10, 2):
        lucas = sp.trace(F**n)
        c2 = sp.simplify((lucas + 2) / 4)
        i_value = sp.simplify(c2 - 1)
        matches.append(i_value)
        print(f"    match F^{n}: L_n={lucas}, I={i_value}")
    assert matches == [sp.Rational(1, 4), sp.Rational(5, 4), sp.Integer(4), sp.Rational(45, 4)]

    print("\nVerdict: STALLED")
    print("Projective return is primitive for every c; I=1/4 requires the extra")
    print("rule that the return linearization reproduce the original A sector.")


if __name__ == "__main__":
    main()
