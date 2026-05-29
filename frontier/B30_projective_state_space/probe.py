"""B30 -- projective state-space control.

Checks whether the B26 central-sign quotient is a natural trace-character
quotient and whether that quotient alone selects I=1/4.
"""

from __future__ import annotations

import sympy as sp


def trace_map(state: sp.Matrix) -> sp.Matrix:
    x, y, z = state
    return sp.Matrix([z, x, 2 * x * z - y])


def sign_action(state: sp.Matrix, sa: int, sb: int) -> sp.Matrix:
    x, y, z = state
    return sp.Matrix([sa * x, sb * y, sa * sb * z])


def quotient_coordinates(state: sp.Matrix) -> sp.Matrix:
    x, y, z = state
    return sp.Matrix([x**2, y**2, z**2, x * y * z])


def quotient_map(qstate: sp.Matrix) -> sp.Matrix:
    u, v, w, r = qstate
    return sp.Matrix([w, u, 4 * u * w - 4 * r + v, 2 * u * w - r])


def iterate_quotient(qstate: sp.Matrix, n: int) -> sp.Matrix:
    out = sp.Matrix(qstate)
    for _ in range(n):
        out = quotient_map(out)
    return sp.simplify(out)


def main() -> None:
    print("=" * 72)
    print("B30 -- projective state space")
    print("SPECULATIVE: observations only, not claims")
    print("=" * 72)

    x, y, z, c = sp.symbols("x y z c")
    state = sp.Matrix([x, y, z])

    print("\n[1] quotient coordinates are central-sign invariant")
    base_q = quotient_coordinates(state)
    for sa in (-1, 1):
        for sb in (-1, 1):
            shifted_q = quotient_coordinates(sign_action(state, sa, sb))
            residual = sp.simplify(shifted_q - base_q)
            print(f"    signs ({sa:+d},{sb:+d}) residual = {tuple(residual)}")
            assert residual == sp.zeros(4, 1)

    print("\n[2] relation and Fricke invariant descend")
    u, v, w, r = base_q
    relation = sp.expand(r**2 - u * v * w)
    invariant = sp.expand(x**2 + y**2 + z**2 - 2 * x * y * z - 1)
    quotient_invariant = sp.expand(u + v + w - 2 * r - 1)
    print(f"    r^2-uvw = {relation}")
    print(f"    I = {quotient_invariant}")
    assert relation == 0
    assert invariant == quotient_invariant

    print("\n[3] trace map descends polynomially")
    lifted_after = quotient_coordinates(trace_map(state))
    quotient_after = quotient_map(base_q)
    residual = sp.simplify(lifted_after - quotient_after)
    print(f"    residual = {tuple(residual)}")
    assert residual == sp.zeros(4, 1)

    print("\n[4] B26 half-return is literal in the quotient")
    qpoint = sp.Matrix([0, 0, c**2, 0])
    for n in range(1, 4):
        image = iterate_quotient(qpoint, n)
        print(f"    Q^{n}(0,0,c^2,0) = {tuple(image)}")
    assert iterate_quotient(qpoint, 3) == qpoint

    print("\n[5] no I-selection from quotient return alone")
    q_invariant = sp.expand(qpoint[0] + qpoint[1] + qpoint[2] - 2 * qpoint[3] - 1)
    print(f"    I on the projective 3-cycle = {q_invariant}")
    assert q_invariant == c**2 - 1

    print("\nVerdict: STALLED")
    print("The PSL/central-sign quotient is canonical if lift-independent data are")
    print("chosen, but the quotient alone leaves I=c^2-1 free.")


if __name__ == "__main__":
    main()
