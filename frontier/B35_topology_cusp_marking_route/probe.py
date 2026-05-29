"""B35 -- topology / cusp marking route.

Models central lift signs as H^1(F_2; Z/2) data and checks the half-step action.
"""

from __future__ import annotations

import itertools

import sympy as sp


def mod2_matrix_power(matrix: sp.Matrix, n: int) -> sp.Matrix:
    out = sp.eye(matrix.rows)
    for _ in range(n):
        out = (out * matrix).applyfunc(lambda value: value % 2)
    return out


def main() -> None:
    print("=" * 72)
    print("B35 -- topology / cusp marking route")
    print("SPECULATIVE: observations only, not claims")
    print("=" * 72)

    print("\n[1] half-step action on sign characters")
    # Fibonacci substitution a->ab, b->a acts on Z_2 sign exponents by
    # (alpha,beta) -> (alpha+beta, alpha).
    f_mod2 = sp.Matrix([[1, 1], [1, 0]])
    print(f"    F mod 2 = {f_mod2.tolist()}")
    assert mod2_matrix_power(f_mod2, 3) == sp.eye(2)
    assert mod2_matrix_power(f_mod2, 1) != sp.eye(2)

    print("\n[2] nonzero sign characters form a 3-cycle")
    nonzero = [sp.Matrix(v) for v in itertools.product([0, 1], repeat=2) if v != (0, 0)]
    orbit = []
    current = nonzero[0]
    for _ in range(3):
        orbit.append(tuple(current))
        current = (f_mod2 * current).applyfunc(lambda value: value % 2)
    print(f"    orbit = {orbit}")
    assert set(orbit) == {(1, 0), (0, 1), (1, 1)}

    print("\n[3] no selector parameter in sign topology")
    c = sp.symbols("c")
    invariant_family = c**2 - 1
    print(f"    I family remains {invariant_family}")
    assert sp.diff(invariant_family, c) == 2 * c

    print("\nVerdict: STALLED")
    print("Sign topology explains the projective order-3 behavior but carries no")
    print("I-parameter, so it does not select lambda/h=1.")


if __name__ == "__main__":
    main()
