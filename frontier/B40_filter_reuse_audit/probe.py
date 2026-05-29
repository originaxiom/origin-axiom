"""B40 -- filter reuse audit.

Classifies which parts of the S1 derivation are inherited and which require a
new tangent-filter assumption.
"""

from __future__ import annotations

import sympy as sp


def main() -> None:
    print("=" * 72)
    print("B40 -- filter reuse audit")
    print("SPECULATIVE: observations only, not claims")
    print("=" * 72)

    c, t = sp.symbols("c t")
    mu = 4 * c**2 - 2
    a_quadratic = t**2 - 3 * t + 1
    tangent_quadratic = t**2 - mu * t + 1

    derived_inputs = [
        "A1-A6 -> A",
        "exchange/half-step -> F=LP",
        "trace functoriality -> T",
        "central-sign quotient -> projective return",
    ]
    extra_filter = "T1: tangent return inherits integer/minimal/torsion filters"

    print("\n[1] derived before T1")
    for item in derived_inputs:
        print(f"    {item}")
    print(f"    free tangent quadratic = {tangent_quadratic}")
    assert sp.diff(mu, c) == 8 * c

    print("\n[2] extra filter")
    print(f"    {extra_filter}")
    selected_c2 = sp.solve(sp.Eq(mu, 3), c**2)[0]
    selected_i = selected_c2 - 1
    selected_quadratic = tangent_quadratic.subs(c**2, selected_c2)
    print(f"    T1 minimal trace gives c^2={selected_c2}, I={selected_i}")
    assert selected_i == sp.Rational(1, 4)
    assert sp.factor(selected_quadratic - a_quadratic) == 0

    print("\n[3] status classification")
    statuses = {
        "projective quotient": "derived conditional on PSL state data",
        "S1": "conditional on T1",
        "lambda/h=1": "conditional on T1",
    }
    for key, value in statuses.items():
        print(f"    {key}: {value}")
    assert statuses["S1"] == "conditional on T1"

    print("\nVerdict: CONDITIONAL")
    print("The clean statement is T1 -> S1 -> lambda/h=1. T1 is not yet")
    print("derived from A1-A7 plus exchange.")


if __name__ == "__main__":
    main()
