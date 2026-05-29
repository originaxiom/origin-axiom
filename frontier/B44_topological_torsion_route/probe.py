"""B44 -- topological torsion route."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    print("=" * 72)
    print("B44 -- topological torsion route")
    print("SPECULATIVE: observations only, not claims")
    print("=" * 72)

    mu, c = sp.symbols("mu c")
    companion = sp.Matrix([[0, -1], [1, mu]])
    torsion_det = sp.factor((companion - sp.eye(2)).det())

    print("\n[1] determinant-one tangent return")
    print(f"    M = {companion.tolist()}")
    print(f"    det(M-I) = {torsion_det}")
    assert companion.det() == 1
    assert companion.trace() == mu
    assert torsion_det == 2 - mu

    print("\n[2] torsion-one positive hyperbolic branch")
    solutions = sp.solve(sp.Eq((2 - mu) ** 2, 1), mu)
    positive_hyperbolic = [solution for solution in solutions if solution > 2][0]
    selected_c2 = sp.solve(sp.Eq(4 * c**2 - 2, positive_hyperbolic), c**2)[0]
    selected_i = selected_c2 - 1
    print(f"    |det(M-I)|=1 solutions = {solutions}")
    print(f"    positive hyperbolic solution = {positive_hyperbolic}")
    print(f"    c^2={selected_c2}, I={selected_i}")
    assert positive_hyperbolic == 3
    assert selected_i == sp.Rational(1, 4)

    print("\nVerdict: CONDITIONAL")
    print("Torsion-one selects S1 if the tangent return has a legitimate")
    print("mapping-torus torsion interpretation.")


if __name__ == "__main__":
    main()
