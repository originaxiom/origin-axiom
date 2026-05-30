"""B32 -- selector axiom audit.

Classifies which assumptions are needed to get lambda/h=1.
"""

from __future__ import annotations

import sympy as sp


def main() -> None:
    print("=" * 72)
    print("B32 -- selector axiom audit")
    print("SPECULATIVE: observations only, not claims")
    print("=" * 72)

    c, t = sp.symbols("c t")
    i_family = c**2 - 1
    projective_return_family = sp.solve(sp.Eq(i_family, sp.symbols("I")), c**2)

    print("\n[1] assumptions available before selector S1")
    assumptions = [
        "A1-A6 -> A",
        "exchange/half-step -> F=LP and F^2=A",
        "trace functoriality -> Fibonacci trace map T",
        "central-sign quotient -> projective period-3 return",
    ]
    for assumption in assumptions:
        print(f"    {assumption}")

    print("\n[2] projective return without A-sector matching")
    print(f"    I family = {i_family}")
    print(f"    c^2 as a function of I = {projective_return_family}")
    assert projective_return_family == [sp.symbols("I") + 1]

    print("\n[3] adding selector S1")
    half_return_quadratic = t**2 - (4 * c**2 - 2) * t + 1
    a_quadratic = t**2 - 3 * t + 1
    selected_c2 = sp.solve(sp.Eq(4 * c**2 - 2, 3), c**2)[0]
    selected_i = sp.simplify(selected_c2 - 1)
    print(f"    half-return quadratic = {half_return_quadratic}")
    print(f"    A quadratic = {a_quadratic}")
    print(f"    S1 selects c^2={selected_c2}, I={selected_i}")
    assert sp.factor(half_return_quadratic.subs(c**2, selected_c2) - a_quadratic) == 0
    assert selected_i == sp.Rational(1, 4)

    print("\n[4] full-return counter-control")
    full_return_quadratic = t**2 - (16 * c**4 + 2) * t + 1
    full_return_c2 = [root for root in sp.solve(sp.Eq(16 * c**4 + 2, 3), c**2) if root.is_real]
    print(f"    full-return quadratic = {full_return_quadratic}")
    print(f"    full-return A-match c^2 values = {full_return_c2}")
    assert sp.Rational(1, 4) in full_return_c2
    assert sp.Rational(5, 4) not in full_return_c2

    print("\nVerdict: STALLED")
    print("A1-A7 plus exchange get the trace-map setting, but lambda/h=1 needs")
    print("the additional S1 A-sector self-similarity selector.")


if __name__ == "__main__":
    main()
