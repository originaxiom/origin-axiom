"""B19 -- exchange/half-step axiom audit."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    print("=" * 72)
    print("B19 -- Exchange/half-step axiom audit")
    print("SPECULATIVE: observations only, not claims")
    print("=" * 72)

    L = sp.Matrix([[1, 1], [0, 1]])
    R = sp.Matrix([[1, 0], [1, 1]])
    A = L * R
    RL = R * L
    P = sp.Matrix([[0, 1], [1, 0]])
    I = sp.eye(2)
    candidates = []
    for a in range(-8, 9):
        for b in range(-8, 9):
            for c in range(-8, 9):
                for d in range(-8, 9):
                    X = sp.Matrix([[a, b], [c, d]])
                    if X.det() in (-1, 1):
                        candidates.append(X)

    exchange = [X for X in candidates if X * L * X.inv() == R]
    exchange_involutions = [X for X in exchange if X**2 == I]
    conjugate_order = [X for X in candidates if X * A * X.inv() == RL]
    conjugate_order_involutions = [X for X in conjugate_order if X**2 == I]
    half_step = [X for X in candidates if (L * X) ** 2 == A]
    def key(X: sp.Matrix) -> tuple[tuple[int, ...], ...]:
        return tuple(tuple(int(value) for value in row) for row in X.tolist())

    expected = {key(-P), key(P)}
    assert {key(X) for X in exchange_involutions} == expected
    assert {key(X) for X in conjugate_order_involutions} == expected
    assert {key(X) for X in half_step} == expected
    print(f"    plain exchange candidates: {len(exchange)}")
    print(f"    plain order-conjugacy candidates: {len(conjugate_order)}")
    print("    adding X^2=I, or using (L X)^2=A, isolates +/-P")

    weak_involutions = [X for X in candidates if X.det() == -1 and X**2 == I]
    time_reversals = [X for X in weak_involutions if X * A * X.inv() == A.inv()]
    assert len(weak_involutions) > 2
    assert len(time_reversals) > 2
    print(f"    det=-1 involution candidates: {len(weak_involutions)}")
    print(f"    time-reversal candidates: {len(time_reversals)}")

    for X in half_step:
        assert X**2 == I
        assert X * L * X.inv() == R
    print("    (L X)^2=A implies the exchange behavior in the bounded solution set")

    print("\nVerdict: STALLED")
    print("P is forced by the half-step condition; the half-step condition is still assumed.")


if __name__ == "__main__":
    main()
