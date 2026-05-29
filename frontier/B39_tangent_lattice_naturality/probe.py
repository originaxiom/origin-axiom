"""B39 -- tangent lattice naturality.

Checks whether the projective return itself supplies a canonical integer
tangent lattice, or whether integrality is an added filter.
"""

from __future__ import annotations

import sympy as sp


def main() -> None:
    print("=" * 72)
    print("B39 -- tangent lattice naturality")
    print("SPECULATIVE: observations only, not claims")
    print("=" * 72)

    c, m, mu = sp.symbols("c m mu")
    companion = sp.Matrix([[0, -1], [1, mu]])
    print("\n[1] companion matrix for tangent quadratic")
    print(f"    M_mu = {companion.tolist()}")
    assert companion.det() == 1
    assert companion.trace() == mu

    print("\n[2] integrality condition")
    tangent_mu = 4 * c**2 - 2
    c2_family = sp.solve(sp.Eq(tangent_mu, m), c**2)[0]
    print(f"    mu(c) = {tangent_mu}")
    print(f"    integer trace m gives c^2 = {c2_family}")
    assert c2_family == (m + 2) / 4

    print("\n[3] integer hyperbolic family")
    family = []
    for trace in range(3, 9):
        c2 = sp.Rational(trace + 2, 4)
        i_value = c2 - 1
        family.append((trace, c2, i_value))
        print(f"    mu={trace}: c^2={c2}, I={i_value}")
    assert family[0] == (3, sp.Rational(5, 4), sp.Rational(1, 4))
    assert len(family) > 1

    print("\nVerdict: STALLED")
    print("Integrality gives a discrete family; the quotient alone does not")
    print("choose the minimal trace-3 lattice.")


if __name__ == "__main__":
    main()
