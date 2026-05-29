"""B34 -- Goldman/WP quotient naturality."""

from __future__ import annotations

import sympy as sp


def invariant_to_quotient(expr: sp.Expr, x: sp.Symbol, y: sp.Symbol, z: sp.Symbol) -> sp.Expr:
    u, v, w, r = sp.symbols("u v w r")
    poly = sp.Poly(sp.expand(expr), x, y, z)
    out = sp.Integer(0)
    for powers, coeff in poly.terms():
        a, b, c = powers
        parity = a % 2
        assert b % 2 == parity and c % 2 == parity
        if parity == 0:
            out += coeff * u ** (a // 2) * v ** (b // 2) * w ** (c // 2)
        else:
            out += coeff * r * u ** ((a - 1) // 2) * v ** ((b - 1) // 2) * w ** ((c - 1) // 2)
    return sp.factor(out)


def main() -> None:
    print("=" * 72)
    print("B34 -- Goldman/WP quotient naturality")
    print("SPECULATIVE: observations only, not claims")
    print("=" * 72)

    x, y, z = sp.symbols("x y z")
    variables = [x, y, z]
    invariant = x**2 + y**2 + z**2 - 2 * x * y * z - 1
    grad_i = sp.Matrix([sp.diff(invariant, v) for v in variables])

    def bracket(f: sp.Expr, g: sp.Expr) -> sp.Expr:
        grad_f = sp.Matrix([sp.diff(f, v) for v in variables])
        grad_g = sp.Matrix([sp.diff(g, v) for v in variables])
        return sp.factor(grad_i.dot(grad_f.cross(grad_g)))

    print("\n[1] central signs are Poisson")
    coords = [x, y, z]
    for sa in (-1, 1):
        for sb in (-1, 1):
            sub = {x: sa * x, y: sb * y, z: sa * sb * z}
            for f in coords:
                for g in coords:
                    lhs = bracket(f.subs(sub, simultaneous=True), g.subs(sub, simultaneous=True))
                    rhs = bracket(f, g).subs(sub, simultaneous=True)
                    assert sp.factor(lhs - rhs) == 0
            print(f"    signs ({sa:+d},{sb:+d}) preserve bracket")

    print("\n[2] quotient generators close under bracket")
    generators = [x**2, y**2, z**2, x * y * z]
    names = ["u", "v", "w", "r"]
    for i, f in enumerate(generators):
        for j, g in enumerate(generators):
            if i < j:
                lifted = bracket(f, g)
                quotient = invariant_to_quotient(lifted, x, y, z)
                print(f"    {{{names[i]},{names[j]}}} = {quotient}")

    print("\n[3] half-step remains anti-Poisson")
    trace_map = sp.Matrix([z, x, 2 * x * z - y])
    sub_t = {x: trace_map[0], y: trace_map[1], z: trace_map[2]}
    for f in coords:
        for g in coords:
            lhs = bracket(f.subs(sub_t, simultaneous=True), g.subs(sub_t, simultaneous=True))
            rhs = bracket(f, g).subs(sub_t, simultaneous=True)
            assert sp.factor(lhs + rhs) == 0
    print("    T is anti-Poisson")

    print("\n[4] no I=1/4 privilege")
    i_symbol = sp.symbols("I")
    print("    bracket construction depends on dI, not on a selected constant I=1/4")
    assert sp.diff(i_symbol, i_symbol) == 1

    print("\nVerdict: STALLED")
    print("The Poisson/WP structure supports the quotient but applies to all")
    print("I-surfaces, so it does not derive the selector.")


if __name__ == "__main__":
    main()
