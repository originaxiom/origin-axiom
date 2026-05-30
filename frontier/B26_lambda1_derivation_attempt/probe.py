"""B26 -- lambda/h=1 derivation attempt.

Tests whether the proposed period-3 trace-map argument derives the Fibonacci
Hamiltonian dimensionless coupling lambda/h=1.
"""

from __future__ import annotations

import sympy as sp


def trace_map(state: sp.Matrix) -> sp.Matrix:
    x, y, z = state
    return sp.Matrix([z, x, 2 * x * z - y])


def iterate(state: sp.Matrix, n: int) -> sp.Matrix:
    out = sp.Matrix(state)
    for _ in range(n):
        out = trace_map(out)
    return sp.simplify(out)


def main() -> None:
    print("=" * 72)
    print("B26 -- lambda/h=1 derivation attempt")
    print("SPECULATIVE: observations only, not claims")
    print("=" * 72)

    x, y, z, c, t = sp.symbols("x y z c t")
    state = sp.Matrix([x, y, z])
    point = {x: 0, y: 0, z: c}

    print("\n[1] orbit check")
    for n in range(1, 7):
        image = iterate(state, n).subs(point)
        print(f"    T^{n}(0,0,c) = {tuple(image)}")
    assert iterate(state, 3).subs(point) == sp.Matrix([0, 0, -c])
    assert iterate(state, 6).subs(point) == sp.Matrix([0, 0, c])

    print("\n[2] projective half-return linearization")
    jac_t3 = iterate(state, 3).jacobian(state).subs(point)
    char_t3 = sp.factor(jac_t3.charpoly(t).as_expr())
    expected_t3 = sp.factor((t + 1) * (t**2 - (4 * c**2 - 2) * t + 1))
    print(f"    char(DT^3) = {char_t3}")
    assert sp.expand(char_t3 - expected_t3) == 0

    a_quadratic = t**2 - 3 * t + 1
    selected_c2 = sp.solve(sp.Eq(4 * c**2 - 2, 3), c**2)[0]
    selected_i = sp.simplify(selected_c2 - 1)
    print(f"    A-sector match forces c^2 = {selected_c2}")
    print(f"    I = c^2 - 1 = {selected_i}")
    assert selected_c2 == sp.Rational(5, 4)
    assert selected_i == sp.Rational(1, 4)
    assert sp.factor((t**2 - (4 * selected_c2 - 2) * t + 1) - a_quadratic) == 0

    print("\n[3] literal return control")
    jac_t6 = iterate(state, 6).jacobian(state).subs(point)
    char_t6 = sp.factor(jac_t6.charpoly(t).as_expr())
    expected_t6 = sp.factor((t - 1) * (t**2 - (16 * c**4 + 2) * t + 1))
    print(f"    char(DT^6) = {char_t6}")
    assert sp.expand(char_t6 - expected_t6) == 0
    literal_at_selected = sp.factor(char_t6.subs(c**2, selected_c2))
    print(f"    at c^2=5/4, char(DT^6) = {literal_at_selected}")
    assert sp.factor(literal_at_selected - (t - 1) * (t**2 - 27 * t + 1)) == 0

    u = sp.symbols("u")
    full_return_match = sp.solve(sp.Eq(16 * u**2 + 2, 3), u)
    print(f"    full-return A-sector match solves c^2 = {full_return_match}")
    assert sp.Rational(1, 4) in full_return_match
    assert sp.simplify(sp.Rational(1, 4) - 1) == sp.Rational(-3, 4)

    print("\n[4] coupling consequence")
    lam = sp.symbols("lambda", positive=True)
    selected_lambda = sp.solve(sp.Eq(lam**2 / 4, selected_i), lam)[0]
    print(f"    (lambda/h)^2/4=1/4 with lambda/h>0 gives lambda/h = {selected_lambda}")
    assert selected_lambda == 1

    print("\n[5] Lucas hierarchy under the projective criterion")
    F = sp.Matrix([[1, 1], [1, 0]])
    lambda_sq_values = []
    for n in range(2, 14, 2):
        trace = sp.trace(F**n)
        hierarchy_i = sp.simplify((trace - 2) / 4)
        hierarchy_lambda_sq = sp.simplify(4 * hierarchy_i)
        hierarchy_c_sq = sp.simplify(hierarchy_i + 1)
        lambda_sq_values.append(hierarchy_lambda_sq)
        print(
            f"    n={n}: L_n={trace}, I={hierarchy_i}, "
            f"(lambda/h)^2={hierarchy_lambda_sq}, c^2={hierarchy_c_sq}"
        )
        half_return_quadratic = t**2 - (4 * hierarchy_c_sq - 2) * t + 1
        assert sp.factor(half_return_quadratic - (F**n).charpoly(t).as_expr()) == 0
    assert lambda_sq_values[:5] == [1, 5, 16, 45, 121]

    print("\nVerdict: STALLED")
    print("lambda/h=1 is the first member of an exact Lucas hierarchy selected by")
    print("projective half-return self-similarity; the projective criterion remains")
    print("an added selection rule.")


if __name__ == "__main__":
    main()
