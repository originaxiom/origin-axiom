#!/usr/bin/env python3
"""Exact local certificate for the B530 trace-zero mapping-torus character.

The calculation is performed in a diagonal-T gauge.  It proves:

1. An explicit irreducible representation over Q(sqrt(-3)) satisfies
       T rho(g) T^{-1} = rho(sigma(g))
   for g = a,b,A,B.

2. Its exact generator traces are all zero and its six commutator traces are
       (-2,-2,2,-2,-2,-2).

3. The complex Jacobian has rank 15 in 17 variables.  Its two tangent
   directions are:
       - residual diagonal conjugation;
       - one genuine character tangent.

4. On the transverse gauge slice rho(a)[0,1] = 1, the tangent dimension is one,
   but the physical tangent has a nonzero exact second-order obstruction.

Therefore the set-theoretic character is isolated, while its local scheme is
nonreduced.  On the gauge slice the completed local algebra is C[[e]]/(e^2).
"""

from __future__ import annotations

import sympy as s

I = s.I
r = s.sqrt(3)

SUB = {"a": "abAAB", "b": "aAB", "A": "abAB", "B": "aA"}
GENS = ["a", "b", "A", "B"]

tau = s.Rational(1, 2) + I * r / 2
T = s.diag(tau, 1 / tau)
Ti = s.diag(1 / tau, tau)

rho = {
    "a": s.Matrix([
        [I / r, 1],
        [-s.Rational(2, 3), -I / r],
    ]),
    "b": s.Matrix([
        [-I / r, s.Rational(1, 2) - I * r / 2],
        [-s.Rational(1, 3) - I / r, I / r],
    ]),
    "A": s.Matrix([
        [-I / r, s.Rational(1, 2) + I * r / 2],
        [-s.Rational(1, 3) + I / r, I / r],
    ]),
    "B": s.Matrix([
        [I / r, 1],
        [-s.Rational(2, 3), -I / r],
    ]),
}


def word_matrix(word: str, matrices: dict[str, s.Matrix]) -> s.Matrix:
    result = s.eye(2)
    for letter in word:
        result *= matrices[letter]
    return s.simplify(result)


def commutator_trace(left: s.Matrix, right: s.Matrix):
    commutator = left * right * left.inv() * right.inv()
    return s.simplify(s.trace(commutator))


def exact_point_checks() -> dict:
    fixed = {}
    for generator in GENS:
        difference = s.simplify(
            T * rho[generator] * Ti - word_matrix(SUB[generator], rho)
        )
        fixed[generator] = all(
            s.simplify(entry) == 0 for entry in difference
        )
    determinants = {g: s.simplify(rho[g].det()) for g in GENS}
    traces = {g: s.simplify(s.trace(rho[g])) for g in GENS}

    kappas = {}
    for index, left in enumerate(GENS):
        for right in GENS[index + 1:]:
            kappas[left + right] = commutator_trace(rho[left], rho[right])

    assert all(fixed.values())
    assert all(value == 1 for value in determinants.values())
    assert all(value == 0 for value in traces.values())
    assert kappas == {
        "ab": -2,
        "aA": -2,
        "aB": 2,
        "bA": -2,
        "bB": -2,
        "AB": -2,
    }
    assert s.simplify(tau**6) == 1

    return {
        "fixed_equations": fixed,
        "determinants": determinants,
        "traces": traces,
        "kappas": kappas,
        "tau": tau,
    }


def direct_jacobian() -> s.Matrix:
    """Construct the exact 20x17 complex Jacobian by matrix calculus.

    Variables:
      0       tau
      1..4    entries of rho(a), row-major
      5..8    entries of rho(b)
      9..12   entries of rho(A)
      13..16  entries of rho(B)

    Equations:
      16 matrix entries from the four fixed equations,
      followed by four determinant equations.
    """
    dT = s.diag(1, -1 / tau**2)
    dTi = s.diag(-1 / tau**2, 1)

    elementary = []
    for entry in range(4):
        matrix = s.zeros(2)
        matrix[entry // 2, entry % 2] = 1
        elementary.append(matrix)

    def word_derivative(word: str, target: str, direction: s.Matrix):
        total = s.zeros(2)
        for position, letter in enumerate(word):
            if letter != target:
                continue
            product = s.eye(2)
            for cursor, current in enumerate(word):
                product *= direction if cursor == position else rho[current]
            total += product
        return s.simplify(total)

    jacobian = s.zeros(20, 17)

    for generator_index, generator in enumerate(GENS):
        derivative = s.simplify(
            dT * rho[generator] * Ti
            + T * rho[generator] * dTi
        )
        for entry, value in enumerate(list(derivative)):
            jacobian[4 * generator_index + entry, 0] = value

    for matrix_index, target in enumerate(GENS):
        for entry_index, direction in enumerate(elementary):
            column = 1 + 4 * matrix_index + entry_index
            for equation_index, generator in enumerate(GENS):
                derivative = (
                    T * direction * Ti if target == generator else s.zeros(2)
                ) - word_derivative(SUB[generator], target, direction)
                for entry, value in enumerate(list(derivative)):
                    jacobian[4 * equation_index + entry, column] = s.simplify(value)

            matrix = rho[target]
            determinant_derivatives = [
                matrix[1, 1],
                -matrix[1, 0],
                -matrix[0, 1],
                matrix[0, 0],
            ]
            jacobian[16 + matrix_index, column] = determinant_derivatives[entry_index]

    return jacobian


GAUGE_VECTOR = s.Matrix([
    0,
    0, 2, s.Rational(4, 3), 0,
    0, 1 - r * I, s.Rational(2, 3) + 2 * r * I / 3, 0,
    0, 1 + r * I, s.Rational(2, 3) - 2 * r * I / 3, 0,
    0, 2, s.Rational(4, 3), 0,
])

RAW_PHYSICAL_VECTOR = s.Matrix([
    -s.Rational(3, 16) - 3 * r * I / 16,
    -s.Rational(1, 4) - 3 * r * I / 4,
    s.Rational(9, 8) - 5 * r * I / 8,
    s.Rational(3, 4) - r * I / 4,
    s.Rational(1, 4) - 3 * r * I / 4,
    -s.Rational(5, 4) - 3 * r * I / 4,
    s.Rational(3, 8) - r * I / 8,
    s.Rational(5, 4) - r * I / 4,
    s.Rational(5, 4) - 3 * r * I / 4,
    -s.Rational(1, 2),
    s.Rational(3, 4) + r * I / 4,
    -s.Rational(1, 2) - r * I / 2,
    s.Rational(1, 2),
    -1,
    -r * I,
    0,
    1,
])

GAUGE_COEFFICIENT = s.simplify(
    RAW_PHYSICAL_VECTOR[2] / GAUGE_VECTOR[2]
)
PHYSICAL_VECTOR = s.simplify(
    RAW_PHYSICAL_VECTOR - GAUGE_COEFFICIENT * GAUGE_VECTOR
)

# Gauge slice: fix rho(a)[0,1] = 1, which is variable column 2.
SLICE_MINOR_ROWS = [1, 13, 9, 2, 3, 0, 5, 14, 8, 4, 10, 7, 12, 11, 15]
SLICE_MINOR_COLUMNS = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
EXPECTED_MINOR_DETERMINANT = 88 * I * (2 * r - 3 * I) / 3

LEFT_OBSTRUCTION_WITNESS = s.Matrix([
    s.Rational(2, 3),
    -I * (5 * r + 3 * I) / 9,
    -I * (r - 9 * I) / 6,
    -I * (r + I) / 3,
    -I * (r - 5 * I) / 3,
    -2 * I * (2 * r + 3 * I) / 9,
    I * (r + 9 * I) / 6,
    I * (3 * r + I) / 3,
    -I * (r - 3 * I) / 3,
    2 * r * I / 3,
    I * (r - 3 * I) / 2,
    2 * r * I / 3,
    0,
    I * (r + I) / 3,
    1,
    0, 0, 0, 0, 0,
])

EXPECTED_OBSTRUCTION = -9 * r / (r + I)


def quadratic_coefficient(vector: s.Matrix) -> s.Matrix:
    epsilon = s.symbols("epsilon")
    base = [tau]
    for generator in GENS:
        base.extend(list(rho[generator]))
    line = [base[index] + epsilon * vector[index] for index in range(17)]

    moving_tau = line[0]
    moving_T = s.diag(moving_tau, 1 / moving_tau)
    moving_Ti = s.diag(1 / moving_tau, moving_tau)
    moving_rho = {
        generator: s.Matrix(2, 2, line[1 + 4 * index:5 + 4 * index])
        for index, generator in enumerate(GENS)
    }

    residuals = []
    for generator in GENS:
        residuals.extend(list(
            moving_T * moving_rho[generator] * moving_Ti
            - word_matrix(SUB[generator], moving_rho)
        ))
    for generator in GENS:
        residuals.append(moving_rho[generator].det() - 1)

    return s.Matrix([
        s.factor(
            s.diff(residual, epsilon, 2).subs(epsilon, 0) / 2
        )
        for residual in residuals
    ])


def local_certificate() -> dict:
    jacobian = direct_jacobian()

    assert all(
        s.simplify(entry) == 0
        for entry in jacobian * GAUGE_VECTOR
    )
    assert all(
        s.simplify(entry) == 0
        for entry in jacobian * RAW_PHYSICAL_VECTOR
    )
    assert PHYSICAL_VECTOR[2] == 0
    assert PHYSICAL_VECTOR[16] == 1

    minor = jacobian.extract(
        SLICE_MINOR_ROWS,
        SLICE_MINOR_COLUMNS,
    )
    determinant = s.factor(minor.det(method="domain-ge"))
    assert s.simplify(determinant - EXPECTED_MINOR_DETERMINANT) == 0
    assert determinant != 0

    assert all(
        s.simplify(entry) == 0
        for entry in LEFT_OBSTRUCTION_WITNESS.T * jacobian
    )

    quadratic = quadratic_coefficient(PHYSICAL_VECTOR)
    obstruction = s.factor(
        (LEFT_OBSTRUCTION_WITNESS.T * quadratic)[0]
    )
    assert s.simplify(obstruction - EXPECTED_OBSTRUCTION) == 0
    assert obstruction != 0

    return {
        "complex_jacobian_shape": list(jacobian.shape),
        "complex_rank": 15,
        "complex_kernel_dimension": 2,
        "gauge_dimension_in_diagonal_T_gauge": 1,
        "character_tangent_dimension": 1,
        "slice_minor_rows": SLICE_MINOR_ROWS,
        "slice_minor_columns": SLICE_MINOR_COLUMNS,
        "slice_minor_determinant": determinant,
        "gauge_coefficient": GAUGE_COEFFICIENT,
        "physical_tangent": list(PHYSICAL_VECTOR),
        "quadratic_obstruction": obstruction,
        "local_set_status": "isolated",
        "local_scheme_status": "nonreduced",
        "completed_local_algebra_on_slice": "C[[epsilon]]/(epsilon^2)",
    }


def run_all() -> dict:
    point = exact_point_checks()
    local = local_certificate()
    return {"point": point, "local": local}


if __name__ == "__main__":
    result = run_all()
    print("exact fixed point: PASS")
    print("traces:", result["point"]["traces"])
    print("kappas:", result["point"]["kappas"])
    print("complex rank:", result["local"]["complex_rank"])
    print("character tangent dimension:", result["local"]["character_tangent_dimension"])
    print("quadratic obstruction:", result["local"]["quadratic_obstruction"])
    print("local scheme:", result["local"]["completed_local_algebra_on_slice"])
