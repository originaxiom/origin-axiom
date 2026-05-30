"""B43 -- Markov/Fricke arithmetic route."""

from __future__ import annotations

import math

import sympy as sp


def main() -> None:
    print("=" * 72)
    print("B43 -- Markov/Fricke arithmetic route")
    print("SPECULATIVE: observations only, not claims")
    print("=" * 72)

    i, mu = sp.symbols("I mu")
    discriminant_i = sp.expand((4 * i + 2) ** 2 - 4)
    discriminant_mu = mu**2 - 4
    print("\n[1] tangent discriminant")
    print(f"    Delta(I) = {discriminant_i}")
    assert sp.expand(discriminant_i - 16 * i * (i + 1)) == 0

    print("\n[2] integer hyperbolic discriminants")
    values = []
    for trace in range(3, 12):
        delta = trace**2 - 4
        if int(math.isqrt(delta)) ** 2 != delta:
            values.append((trace, delta))
    print(f"    first nonsquare values = {values[:5]}")
    assert values[0] == (3, 5)

    selected_i = sp.solve(sp.Eq(discriminant_i, 5), i)
    positive_selected = [root for root in selected_i if root > 0][0]
    print(f"    Delta=5 selects I={positive_selected}")
    assert positive_selected == sp.Rational(1, 4)
    assert discriminant_mu.subs(mu, 3) == 5

    print("\n[3] continuity control")
    epsilon = sp.symbols("epsilon", positive=True)
    continuous_delta = discriminant_i.subs(i, epsilon)
    print(f"    Delta(epsilon) = {continuous_delta}")
    assert sp.limit(continuous_delta, epsilon, 0, dir="+") == 0

    print("\nVerdict: CONDITIONAL")
    print("Delta=5 is minimal only after integer hyperbolic tangent trace is")
    print("assumed; otherwise the discriminant is continuous.")


if __name__ == "__main__":
    main()
