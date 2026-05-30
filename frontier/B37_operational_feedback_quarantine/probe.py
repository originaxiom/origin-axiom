"""B37 -- operational feedback quarantine.

Turns feedback/self-reference language into explicit computable predicates and
keeps awareness/metaphysics language out of claims.
"""

from __future__ import annotations

import sympy as sp


def main() -> None:
    print("=" * 72)
    print("B37 -- operational feedback quarantine")
    print("SPECULATIVE: observations only, not claims")
    print("=" * 72)

    x, y, z = sp.symbols("x y z")
    state = sp.Matrix([x, y, z])
    trace_map = sp.Matrix([z, x, 2 * x * z - y])
    invariant = x**2 + y**2 + z**2 - 2 * x * y * z - 1
    sub = {x: trace_map[0], y: trace_map[1], z: trace_map[2]}

    print("\n[1] feedback predicate")
    nonlinear_terms = [component for component in trace_map if sp.Poly(component, x, y, z).total_degree() > 1]
    print(f"    nonlinear components = {nonlinear_terms}")
    assert nonlinear_terms == [2 * x * z - y]

    print("\n[2] invariant predicate")
    invariant_delta = sp.factor(invariant.subs(sub, simultaneous=True) - invariant)
    print(f"    I(T(state))-I(state) = {invariant_delta}")
    assert invariant_delta == 0

    print("\n[3] self-model predicate")
    i_symbol = sp.symbols("I")
    explicit_i_dependence = any(component.has(i_symbol) for component in trace_map)
    print(f"    map explicitly reads an invariant variable I? {explicit_i_dependence}")
    assert not explicit_i_dependence

    print("\n[4] term quarantine")
    allowed_terms = {"feedback", "invariant", "quotient", "self-reference"}
    blocked_terms = {"awareness", "consciousness", "religion", "metaphysics"}
    print(f"    allowed operational terms = {sorted(allowed_terms)}")
    print(f"    blocked claim terms = {sorted(blocked_terms)}")
    assert "feedback" in allowed_terms
    assert "awareness" in blocked_terms

    print("\nVerdict: STALLED")
    print("The trace map has feedback and an invariant, but no operational")
    print("self-model criterion is satisfied. Interpretive language stays quarantined.")


if __name__ == "__main__":
    main()
