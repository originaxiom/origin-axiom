"""B28 -- projective quotient legitimacy.

Controls whether the B26 projective half-return is compatible with the central
sign ambiguity of SL(2) lifts.
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


def sign_action(state: sp.Matrix, sa: int, sb: int) -> sp.Matrix:
    x, y, z = state
    return sp.Matrix([sa * x, sb * y, sa * sb * z])


def invariant(state: sp.Matrix) -> sp.Expr:
    x, y, z = state
    return sp.expand(x**2 + y**2 + z**2 - 2 * x * y * z - 1)


def main() -> None:
    print("=" * 72)
    print("B28 -- projective quotient legitimacy")
    print("SPECULATIVE: observations only, not claims")
    print("=" * 72)

    x, y, z, c = sp.symbols("x y z c")
    state = sp.Matrix([x, y, z])

    print("\n[1] central sign equivariance")
    for sa in (-1, 1):
        for sb in (-1, 1):
            lhs = trace_map(sign_action(state, sa, sb))
            rhs = sign_action(trace_map(state), sa * sb, sa)
            residual = sp.simplify(lhs - rhs)
            print(f"    signs ({sa:+d},{sb:+d}) residual = {tuple(residual)}")
            assert residual == sp.zeros(3, 1)

    print("\n[2] invariant under central signs")
    base_i = invariant(state)
    for sa in (-1, 1):
        for sb in (-1, 1):
            shifted_i = invariant(sign_action(state, sa, sb))
            residual = sp.simplify(shifted_i - base_i)
            print(f"    signs ({sa:+d},{sb:+d}) delta I = {residual}")
            assert residual == 0

    print("\n[3] B26 half-return sign control")
    point = sp.Matrix([0, 0, c])
    half_return = iterate(point, 3)
    central_flip = sign_action(point, 1, -1)
    print(f"    T^3(0,0,c) = {tuple(half_return)}")
    print(f"    S(+1,-1)(0,0,c) = {tuple(central_flip)}")
    assert half_return == sp.Matrix([0, 0, -c])
    assert half_return == central_flip

    print("\n[4] global antipodal control")
    antipodal = -state
    central_images = [sign_action(state, sa, sb) for sa in (-1, 1) for sb in (-1, 1)]
    generic_point = {x: 2, y: 3, z: 5}
    is_central = any(image.subs(generic_point) == antipodal.subs(generic_point) for image in central_images)
    delta_antipodal_i = sp.expand(invariant(antipodal) - invariant(state))
    print(f"    generic antipodal is central sign action? {is_central}")
    print(f"    I(-x,-y,-z)-I(x,y,z) = {delta_antipodal_i}")
    assert not is_central
    assert delta_antipodal_i == 4 * x * y * z

    print("\nVerdict: STALLED")
    print("The B26 projective sign quotient is legitimate in central-sign/PSL data,")
    print("but using it as the selector remains an added bridge criterion.")


if __name__ == "__main__":
    main()
