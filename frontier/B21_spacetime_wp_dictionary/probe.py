"""B21 -- Weil-Petersson/Goldman dictionary control."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    print("=" * 72)
    print("B21 -- Spacetime / WP dictionary test")
    print("SPECULATIVE: observations only, not claims")
    print("=" * 72)

    x, y, z = sp.symbols("x y z")
    variables = [x, y, z]
    invariant = x**2 + y**2 + z**2 - 2 * x * y * z - 1
    grad_I = sp.Matrix([sp.diff(invariant, v) for v in variables])

    def bracket(f: sp.Expr, g: sp.Expr) -> sp.Expr:
        grad_f = sp.Matrix([sp.diff(f, v) for v in variables])
        grad_g = sp.Matrix([sp.diff(g, v) for v in variables])
        return sp.factor(grad_I.dot(grad_f.cross(grad_g)))

    T = sp.Matrix([z, x, 2 * x * z - y])
    sub = {x: T[0], y: T[1], z: T[2]}
    for f in variables:
        for g in variables:
            lhs = bracket(f.subs(sub, simultaneous=True), g.subs(sub, simultaneous=True))
            rhs = bracket(f, g).subs(sub, simultaneous=True)
            assert sp.factor(lhs + rhs) == 0
    print("    half-step trace map is anti-Poisson")

    T2 = sp.Matrix([component.subs(sub, simultaneous=True) for component in T])
    sub2 = {x: T2[0], y: T2[1], z: T2[2]}
    for f in variables:
        for g in variables:
            lhs = bracket(f.subs(sub2, simultaneous=True), g.subs(sub2, simultaneous=True))
            rhs = bracket(f, g).subs(sub2, simultaneous=True)
            assert sp.factor(lhs - rhs) == 0
    print("    A-level trace map T^2 is Poisson")

    print("\nVerdict: STALLED")
    print("Natural character-variety symplectic structure yes; spacetime dictionary no.")


if __name__ == "__main__":
    main()
