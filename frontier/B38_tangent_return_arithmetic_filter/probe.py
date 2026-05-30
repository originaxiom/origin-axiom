"""B38 -- tangent return arithmetic filter.

Tests whether reusing the original integer/minimal-hyperbolic/torsion filters
on the projective return's tangent quadratic forces S1.
"""

from __future__ import annotations

import sympy as sp


def main() -> None:
    print("=" * 72)
    print("B38 -- tangent return arithmetic filter")
    print("SPECULATIVE: observations only, not claims")
    print("=" * 72)

    c, i_symbol, mu, t = sp.symbols("c I mu t")
    tangent_mu = 4 * c**2 - 2
    invariant = c**2 - 1

    print("\n[1] tangent trace in terms of c and I")
    print(f"    mu(c) = {tangent_mu}")
    print(f"    I(c) = {invariant}")
    assert sp.expand(tangent_mu - (4 * invariant + 2)) == 0

    print("\n[2] minimal integer hyperbolic trace")
    integer_hyperbolic_traces = [m for m in range(-8, 9) if abs(m) > 2]
    positive_branch = [m for m in integer_hyperbolic_traces if m > 2]
    selected_mu = min(positive_branch)
    selected_c2 = sp.solve(sp.Eq(tangent_mu, selected_mu), c**2)[0]
    selected_i = sp.simplify(selected_c2 - 1)
    selected_g2 = sp.simplify(4 * selected_i)
    print(f"    positive integer hyperbolic traces = {positive_branch[:5]}...")
    print(f"    minimal positive trace = {selected_mu}")
    print(f"    c^2={selected_c2}, I={selected_i}, (lambda/h)^2={selected_g2}")
    assert selected_mu == 3
    assert selected_i == sp.Rational(1, 4)
    assert selected_g2 == 1

    print("\n[3] torsion-one tangent closure")
    torsion_order = sp.Abs(mu - 2)
    positive_torsion_solution = [root for root in sp.solve(sp.Eq((mu - 2) ** 2, 1), mu) if root > 2][0]
    print(f"    |det(M-I)| = {torsion_order}")
    print(f"    positive hyperbolic torsion-one trace = {positive_torsion_solution}")
    assert positive_torsion_solution == 3

    print("\n[4] selected quadratic")
    selected_quadratic = t**2 - selected_mu * t + 1
    a_quadratic = t**2 - 3 * t + 1
    print(f"    selected quadratic = {selected_quadratic}")
    assert sp.factor(selected_quadratic - a_quadratic) == 0

    print("\nVerdict: CONDITIONAL")
    print("S1 follows if the tangent return inherits the original arithmetic")
    print("or torsion-one filters; that inheritance is the remaining assumption.")


if __name__ == "__main__":
    main()
