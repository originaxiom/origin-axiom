"""Frontier probe B15 -- trace-map invariant controls.

This probe checks the extra Part C2 trace-map scripts while separating exact
algebra from interpretive labels.
"""

from __future__ import annotations

import sympy as sp


def assert_zero(expr: sp.Expr, label: str) -> None:
    simplified = sp.factor(sp.simplify(expr))
    if simplified != 0:
        raise AssertionError(f"{label}: expected 0, got {simplified}")


def main() -> None:
    print("=" * 72)
    print("B15 -- Trace-map invariant controls")
    print("SPECULATIVE: observations only, not claims (GOVERNANCE.md section 5)")
    print("=" * 72)

    x, y, z, c, mu, p, r, E, coupling = sp.symbols("x y z c mu p r E coupling")
    trace_map = sp.Matrix([z, x, 2 * x * z - y])
    invariant = x**2 + y**2 + z**2 - 2 * x * y * z - 1

    print("\n[1] Discrete invariant preservation")
    x1, y1, z1 = trace_map
    invariant_next = x1**2 + y1**2 + z1**2 - 2 * x1 * y1 * z1 - 1
    assert_zero(invariant_next - invariant, "Fricke-Vogt invariant preservation")
    print("    I(T(x,y,z)) - I(x,y,z) = 0")

    print("\n[2] Diagonal linearization of V=T-id")
    vector_field_proxy = trace_map - sp.Matrix([x, y, z])
    JV = vector_field_proxy.jacobian([x, y, z]).subs({x: c, y: c, z: c})
    char = sp.factor(JV.charpoly(mu).as_expr())
    expected_char = (mu + 2) * (mu**2 + (1 - 2 * c) * mu + (1 - 2 * c))
    assert_zero(char - expected_char, "diagonal proxy characteristic polynomial")
    discriminant = sp.factor((1 - 2 * c) ** 2 - 4 * (1 - 2 * c))
    assert discriminant == (2 * c - 1) * (2 * c + 3)
    print(f"    char(J_V(c)) = {char}")
    print(f"    quadratic discriminant = {discriminant}")
    for cv, label in [(0, "Eisenstein"), (sp.Rational(1, 2), "nilpotent"), (1, "golden")]:
        print(f"    c={cv}: {sp.factor(char.subs(c, cv))} ({label})")

    print("\n[3] Fixed-point control")
    fixed_points = sp.solve(
        [
            sp.Eq(trace_map[0], x),
            sp.Eq(trace_map[1], y),
            sp.Eq(trace_map[2], z),
        ],
        (x, y, z),
        dict=True,
    )
    assert fixed_points == [{x: 0, y: 0, z: 0}, {x: 1, y: 1, z: 1}]
    print(f"    fixed points of T = {fixed_points}")
    print("    c=1/2 is not a trace-map fixed point")

    print("\n[4] Naive continuum proxy fails invariant preservation")
    dI_dt = sum(
        sp.diff(invariant, variable) * component
        for variable, component in zip((x, y, z), vector_field_proxy)
    )
    test_point = {x: sp.Rational(3, 2), y: 1, z: sp.Rational(3, 2)}
    assert invariant.subs(test_point) == 0
    value = sp.simplify(dI_dt.subs(test_point))
    assert value == sp.Rational(-5, 4)
    print("    test point (3/2,1,3/2) lies on I=0")
    print(f"    dI/dt along V=T-id = {value}")
    print("    this rejects the naive proxy, not all possible continuum flows")

    print("\n[5] Master polynomial identity")
    roots = sp.solve(r**2 + p * r + p, r)
    product_identity = sp.simplify((1 + roots[0]) * (1 + roots[1]))
    assert product_identity == 1
    print("    for r^2+p r+p=0, (1+r1)(1+r2)=1")
    print("    identity is algebraic/tautological for this polynomial family")

    print("\n[6] Fibonacci coupling normalization control")
    initial_x = (E - coupling) / 2
    initial_y = E / 2
    initial_z = sp.Integer(1)
    initial_invariant = sp.factor(
        invariant.subs({x: initial_x, y: initial_y, z: initial_z})
    )
    assert initial_invariant == coupling**2 / 4
    point_invariant = invariant.subs({x: 1, y: 1, z: sp.Rational(3, 2)})
    assert point_invariant == sp.Rational(1, 4)
    inferred_couplings = sp.solve(sp.Eq(coupling**2 / 4, point_invariant), coupling)
    assert inferred_couplings == [-1, 1]
    print(f"    Fibonacci initial-line invariant = {initial_invariant}")
    print("    I(1,1,3/2)=1/4 -> coupling = +/-1 under this normalization")
    print("    sqrt(5) requires a shifted convention, not accepted here")

    print("\n[7] I-surface separation")
    values = {
        "origin": invariant.subs({x: 0, y: 0, z: 0}),
        "Cayley singular": invariant.subs({x: 1, y: 1, z: 1}),
        "complete-point proxy": point_invariant,
    }
    assert values == {
        "origin": -1,
        "Cayley singular": 0,
        "complete-point proxy": sp.Rational(1, 4),
    }
    print(f"    I-values = {values}")
    print("    discrete trace-map orbits cannot cross I-surfaces")
    print("    semantic labels for these surfaces are not derived")

    print("\nVerdict: STALLED")
    print("Endpoint algebra and invariant controls survive; awareness/physics dictionary does not.")


if __name__ == "__main__":
    main()
