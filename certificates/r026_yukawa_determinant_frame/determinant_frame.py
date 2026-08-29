#!/usr/bin/env python3
"""Explicit determinant frame for the height-308 BCDD monad.

This certificate uses only the ordered twelve-ray frame, the integral Euler
matrix and the selected six character lines.  It constructs normalized
Q(zeta_12) Euler eigenvectors by exact Fourier projectors, derives the
determinant character of the quotient bundle, and checks the sparse local
determinant formula for the connecting-sector Yukawa cochain.

It does not construct the H^3(O_Y) trace or any Serre-tail cocycle, and hence
does not assign a value or rank to a Yukawa tensor.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import prod
from pathlib import Path
from random import Random


ORDER = 12
PRIME = 1009
ZETA_MOD = 160
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def rational(value: int | Fraction) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


def solve_rational(matrix: list[list[Fraction]], target: list[Fraction]) -> list[Fraction]:
    size = len(matrix)
    rows = [list(map(rational, row)) + [rational(target[index])] for index, row in enumerate(matrix)]
    for column in range(size):
        pivot = next(row for row in range(column, size) if rows[row][column])
        rows[column], rows[pivot] = rows[pivot], rows[column]
        scale = rows[column][column]
        rows[column] = [value / scale for value in rows[column]]
        for row in range(size):
            if row == column:
                continue
            scale = rows[row][column]
            if scale:
                rows[row] = [left - scale * right for left, right in zip(rows[row], rows[column])]
    return [rows[index][-1] for index in range(size)]


@dataclass(frozen=True)
class K12:
    """Q[z]/(z^4-z^2+1), with z the marked primitive twelfth root."""

    coefficients: tuple[Fraction, Fraction, Fraction, Fraction]

    @staticmethod
    def coerce(value: "K12 | int | Fraction") -> "K12":
        if isinstance(value, K12):
            return value
        return K12((rational(value), Fraction(0), Fraction(0), Fraction(0)))

    def __add__(self, other: "K12 | int | Fraction") -> "K12":
        right = K12.coerce(other)
        return K12(tuple(a + b for a, b in zip(self.coefficients, right.coefficients)))

    __radd__ = __add__

    def __neg__(self) -> "K12":
        return K12(tuple(-value for value in self.coefficients))

    def __sub__(self, other: "K12 | int | Fraction") -> "K12":
        return self + (-K12.coerce(other))

    def __rsub__(self, other: "K12 | int | Fraction") -> "K12":
        return K12.coerce(other) - self

    def __mul__(self, other: "K12 | int | Fraction") -> "K12":
        right = K12.coerce(other)
        product = [Fraction(0)] * 7
        for i, left_value in enumerate(self.coefficients):
            for j, right_value in enumerate(right.coefficients):
                product[i + j] += left_value * right_value
        # z^d = z^(d-2)-z^(d-4), from z^4-z^2+1=0.
        for degree in range(6, 3, -1):
            value = product[degree]
            product[degree] = 0
            product[degree - 2] += value
            product[degree - 4] -= value
        return K12(tuple(product[:4]))

    __rmul__ = __mul__

    def inverse(self) -> "K12":
        assert self != ZERO
        columns = []
        for exponent in range(4):
            columns.append((self * basis_k(exponent)).coefficients)
        multiplication = [[columns[column][row] for column in range(4)] for row in range(4)]
        solution = solve_rational(multiplication, [Fraction(1), Fraction(0), Fraction(0), Fraction(0)])
        inverse = K12(tuple(solution))
        assert self * inverse == ONE
        return inverse

    def __truediv__(self, other: "K12 | int | Fraction") -> "K12":
        return self * K12.coerce(other).inverse()

    def __pow__(self, exponent: int) -> "K12":
        if exponent < 0:
            return (self.inverse()) ** (-exponent)
        answer = ONE
        base = self
        power = exponent
        while power:
            if power & 1:
                answer = answer * base
            base = base * base
            power //= 2
        return answer

    def to_mod(self) -> int:
        result = 0
        for exponent, coefficient in enumerate(self.coefficients):
            numerator = coefficient.numerator % PRIME
            denominator = pow(coefficient.denominator, PRIME - 2, PRIME)
            result = (result + numerator * denominator * pow(ZETA_MOD, exponent, PRIME)) % PRIME
        return result


ZERO = K12((Fraction(0),) * 4)
ONE = K12((Fraction(1), Fraction(0), Fraction(0), Fraction(0)))


def basis_k(exponent: int) -> K12:
    coefficients = [Fraction(0)] * 4
    coefficients[exponent] = Fraction(1)
    return K12(tuple(coefficients))


ZETA = basis_k(1)


Q_PRIME = (
    (1, 0, 0, 1, 0, 0),
    (0, 1, 0, 0, 1, 0),
    (0, 0, 1, 0, 0, 1),
    (1, -1, 1, 0, 0, 0),
)


def block_euler_matrix() -> tuple[tuple[int, ...], ...]:
    q = [[0] * 12 for _ in range(8)]
    for block in range(2):
        for row in range(4):
            for column in range(6):
                q[4 * block + row][6 * block + column] = Q_PRIME[row][column]
    return tuple(tuple(q[column][row] for column in range(8)) for row in range(12))


EULER = block_euler_matrix()
RAY_PERMUTATION = (6, 7, 8, 9, 10, 11, 1, 2, 3, 4, 5, 0)
G_EULER = (
    (0, 0, 0, 0, 0, 0, 1, 1),
    (0, 0, 0, 0, 1, 0, 0, 0),
    (0, 0, 0, 0, 0, 1, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, -1),
    (1, 0, 0, 0, 0, 0, 0, 0),
    (0, 1, 0, 0, 0, 0, 0, 0),
    (0, 0, 1, 0, 0, 0, 0, 0),
    (0, 0, 0, 1, 0, 0, 0, 0),
)
ALL_EULER_CHARACTERS = (0, 2, 3, 4, 6, 8, 9, 10)
W_CHARACTERS = (0, 2, 6, 8, 9, 10)
OMITTED_EULER_CHARACTERS = (3, 4)


def integer_matvec(matrix: tuple[tuple[int, ...], ...], vector: tuple[K12, ...]) -> tuple[K12, ...]:
    return tuple(sum((entry * value for entry, value in zip(row, vector)), ZERO) for row in matrix)


def euler_to_b(vector: tuple[K12, ...]) -> tuple[K12, ...]:
    return tuple(sum((entry * value for entry, value in zip(row, vector)), ZERO) for row in EULER)


def permute_b(vector: tuple[K12, ...]) -> tuple[K12, ...]:
    answer = [ZERO] * 12
    for source, target in enumerate(RAY_PERMUTATION):
        answer[target] = vector[source]
    return tuple(answer)


def canonical_character_vector(label: int) -> tuple[K12, ...]:
    """Fourier-project the earliest Euler anchor and normalize in B coordinates."""

    for anchor in range(8):
        orbit = tuple(ONE if index == anchor else ZERO for index in range(8))
        projected = [ZERO] * 8
        cursor = orbit
        for power in range(ORDER):
            scalar = ZETA ** ((-label * power) % ORDER)
            projected = [left + scalar * right for left, right in zip(projected, cursor)]
            cursor = integer_matvec(G_EULER, cursor)
        projected = [value / ORDER for value in projected]
        b_vector = euler_to_b(tuple(projected))
        if all(value == ZERO for value in b_vector):
            continue
        pivot = next(value for value in b_vector if value != ZERO)
        normalized = tuple(value / pivot for value in b_vector)
        assert next(value for value in normalized if value != ZERO) == ONE
        assert permute_b(normalized) == tuple((ZETA ** label) * value for value in normalized)
        return normalized
    raise AssertionError(f"missing character {label}")


def rank_mod(columns: list[list[int]]) -> int:
    if not columns:
        return 0
    rows = [[columns[column][row] % PRIME for column in range(len(columns))]
            for row in range(len(columns[0]))]
    rank = 0
    for column in range(len(columns)):
        pivot = next((row for row in range(rank, len(rows)) if rows[row][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], PRIME - 2, PRIME)
        rows[rank] = [(value * inverse) % PRIME for value in rows[rank]]
        for row in range(len(rows)):
            if row == rank:
                continue
            scale = rows[row][column]
            if scale:
                rows[row] = [(left - scale * right) % PRIME
                             for left, right in zip(rows[row], rows[rank])]
        rank += 1
    return rank


def det_k(matrix: list[list[K12]]) -> K12:
    size = len(matrix)
    assert size and all(len(row) == size for row in matrix)
    rows = [row[:] for row in matrix]
    determinant = ONE
    for column in range(size):
        pivot = next((row for row in range(column, size) if rows[row][column] != ZERO), None)
        if pivot is None:
            return ZERO
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            determinant = -determinant
        pivot_value = rows[column][column]
        determinant = determinant * pivot_value
        for row in range(column + 1, size):
            if rows[row][column] == ZERO:
                continue
            scale = rows[row][column] / pivot_value
            rows[row] = [left - scale * right for left, right in zip(rows[row], rows[column])]
    return determinant


def nullspace_mod(matrix: list[list[int]]) -> list[list[int]]:
    rows = [[value % PRIME for value in row] for row in matrix]
    row_count = len(rows)
    column_count = len(rows[0])
    pivots: list[int] = []
    rank = 0
    for column in range(column_count):
        pivot = next((row for row in range(rank, row_count) if rows[row][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], PRIME - 2, PRIME)
        rows[rank] = [(value * inverse) % PRIME for value in rows[rank]]
        for row in range(row_count):
            if row == rank:
                continue
            scale = rows[row][column]
            if scale:
                rows[row] = [(left - scale * right) % PRIME
                             for left, right in zip(rows[row], rows[rank])]
        pivots.append(column)
        rank += 1
        if rank == row_count:
            break
    free = [column for column in range(column_count) if column not in pivots]
    basis = []
    for free_column in free:
        vector = [0] * column_count
        vector[free_column] = 1
        for row, pivot in reversed(list(enumerate(pivots))):
            vector[pivot] = -sum(rows[row][column] * vector[column]
                                 for column in free) % PRIME
        basis.append(vector)
    return basis


def det_mod(columns: list[list[int]]) -> int:
    size = len(columns)
    assert size and all(len(column) == size for column in columns)
    rows = [[columns[column][row] % PRIME for column in range(size)] for row in range(size)]
    determinant = 1
    for column in range(size):
        pivot = next((row for row in range(column, size) if rows[row][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            determinant = -determinant
        pivot_value = rows[column][column]
        determinant = determinant * pivot_value % PRIME
        inverse = pow(pivot_value, PRIME - 2, PRIME)
        for row in range(column + 1, size):
            scale = rows[row][column] * inverse % PRIME
            rows[row] = [(left - scale * right) % PRIME
                         for left, right in zip(rows[row], rows[column])]
    return determinant % PRIME


def dot(left: list[int], right: list[int]) -> int:
    return sum(a * b for a, b in zip(left, right)) % PRIME


def add(left: list[int], right: list[int], scale: int = 1) -> list[int]:
    return [(a + scale * b) % PRIME for a, b in zip(left, right)]


def scalar(value: int, vector: list[int]) -> list[int]:
    return [(value * entry) % PRIME for entry in vector]


Exterior = dict[tuple[int, ...], int]


def exterior_vector(index: int, coefficient: int = 1) -> Exterior:
    return {(index,): coefficient}


def exterior_add(left: Exterior, right: Exterior, scale: int = 1) -> Exterior:
    answer = dict(left)
    for indices, value in right.items():
        answer[indices] = answer.get(indices, 0) + scale * value
    return {indices: value for indices, value in answer.items() if value}


def exterior_wedge(left: Exterior, right: Exterior) -> Exterior:
    answer: Exterior = {}
    for left_indices, left_value in left.items():
        for right_indices, right_value in right.items():
            if set(left_indices) & set(right_indices):
                continue
            inversions = sum(i > j for i in left_indices for j in right_indices)
            indices = tuple(sorted(left_indices + right_indices))
            answer[indices] = answer.get(indices, 0) + (-1 if inversions % 2 else 1) * left_value * right_value
    return {indices: value for indices, value in answer.items() if value}


def formal_sparse_identity() -> None:
    sa, sb, sc, sd, k1, k2 = (exterior_vector(index) for index in range(6))
    theta_ab = exterior_add(sb, sa, -1)
    theta_bc = exterior_add(sc, sb, -1)
    theta_cd = exterior_add(sd, sc, -1)
    left = theta_ab
    for factor in (theta_bc, k1, theta_cd, k2, sa):
        left = exterior_wedge(left, factor)
    right = sa
    for factor in (sb, sc, sd, k1, k2):
        right = exterior_wedge(right, factor)
    assert left == right == {(0, 1, 2, 3, 4, 5): 1}


def local_determinant_control(w_columns: list[list[int]]) -> tuple[tuple[int, ...], int, int]:
    # A local quotient functional Phi annihilating W.  Search its six-dimensional
    # annihilator deterministically for one with at least four nonzero components.
    equations = [[column[row] for row in range(12)] for column in w_columns]
    annihilator = nullspace_mod(equations)
    assert len(annihilator) == 6
    phi = None
    for offset in range(1, 20):
        candidate = [0] * 12
        for index, basis in enumerate(annihilator):
            candidate = add(candidate, basis, offset + index)
        if sum(value != 0 for value in candidate) >= 4:
            phi = candidate
            break
    assert phi is not None and all(dot(phi, column) == 0 for column in w_columns)
    indices = tuple(index for index, value in enumerate(phi) if value)[:4]
    for rescale in range(1, PRIME):
        candidate = scalar(rescale, phi)
        values = [candidate[index] for index in indices]
        if all(value != 1 for value in values) and prod(values) % PRIME != 1:
            phi = candidate
            break
    assert all(dot(phi, column) == 0 for column in w_columns)
    a, b, c, d = indices
    standard = [[int(row == column) for row in range(12)] for column in range(12)]
    splittings = {index: scalar(pow(phi[index], PRIME - 2, PRIME), standard[index]) for index in indices}
    assert all(dot(phi, splittings[index]) == 1 for index in indices)

    rng = Random(308026)
    pivot = next(index for index, value in enumerate(phi) if value)

    def random_kernel_vector() -> list[int]:
        vector = [rng.randrange(PRIME) for _ in range(12)]
        correction = dot(phi, vector) * pow(phi[pivot], PRIME - 2, PRIME) % PRIME
        vector[pivot] = (vector[pivot] - correction) % PRIME
        assert dot(phi, vector) == 0
        return vector

    determinant = 0
    for _ in range(100):
        k1 = random_kernel_vector()
        k2 = random_kernel_vector()
        rhs_columns = w_columns + [splittings[a], splittings[b], splittings[c], splittings[d], k1, k2]
        determinant = det_mod(rhs_columns)
        if determinant:
            break
    assert determinant

    theta_ab = add(splittings[b], splittings[a], -1)
    theta_bc = add(splittings[c], splittings[b], -1)
    theta_cd = add(splittings[d], splittings[c], -1)
    lhs = det_mod(w_columns + [theta_ab, theta_bc, k1, theta_cd, k2, splittings[a]])
    assert lhs == determinant

    # epsilon is independent of the last local splitting: two splittings differ
    # by a V-vector, and six V-vectors wedge to zero in the rank-five kernel.
    alternate_splitting = add(splittings[a], random_kernel_vector())
    assert dot(phi, alternate_splitting) == 1
    assert det_mod(w_columns + [theta_ab, theta_bc, k1, theta_cd, k2, alternate_splitting]) == lhs

    numerator = det_mod(w_columns + [standard[a], standard[b], standard[c], standard[d], k1, k2])
    denominator = phi[a] * phi[b] * phi[c] * phi[d] % PRIME
    assert denominator not in (0, 1)
    assert numerator * pow(denominator, PRIME - 2, PRIME) % PRIME == determinant
    wrong_denominator = phi[a] * phi[b] * phi[c] % PRIME
    assert numerator * pow(wrong_denominator, PRIME - 2, PRIME) % PRIME != determinant

    # Quotient-lift controls: adding any Euler-frame vector to either K lift
    # leaves the determinant comparison unchanged.
    lift = [0] * 12
    for coefficient, column in zip(range(1, 7), w_columns):
        lift = add(lift, column, coefficient)
    assert det_mod(w_columns + [splittings[a], splittings[b], splittings[c], splittings[d], add(k1, lift), k2]) == determinant
    assert det_mod(w_columns + [splittings[a], splittings[b], splittings[c], splittings[d], k1, add(k2, lift)]) == determinant
    return indices, determinant, denominator


def main() -> None:
    assert ZETA**4 - ZETA**2 + ONE == ZERO
    assert ZETA**12 == ONE and all(ZETA**power != ONE for power in (1, 2, 3, 4, 6))
    assert pow(ZETA_MOD, 12, PRIME) == 1 and all(pow(ZETA_MOD, power, PRIME) != 1 for power in (1, 2, 3, 4, 6))

    vectors = {label: canonical_character_vector(label) for label in ALL_EULER_CHARACTERS}
    assert len(vectors) == 8
    w_exact = [vectors[label] for label in W_CHARACTERS]
    u = ZETA**2
    imaginary = ZETA**3
    expected_rows = (
        (1, 1, 1, 1, 1, 1),
        (1, -u, 1, -u, -1, u - 1),
        (1, u - 1, 1, u - 1, 1, -u),
        (1, 1, 1, 1, -1, 1),
        (1, -u, 1, -u, 1, u - 1),
        (1, u - 1, 1, u - 1, -1, -u),
        (1, 1 - u, -1, u - 1, imaginary, u),
        (1, -1, -1, 1, -imaginary, -1),
        (1, u, -1, -u, imaginary, 1 - u),
        (1, 1 - u, -1, u - 1, -imaginary, u),
        (1, -1, -1, 1, imaginary, -1),
        (1, u, -1, -u, -imaginary, 1 - u),
    )
    assert all(w_exact[column][row] == K12.coerce(expected_rows[row][column])
               for row in range(12) for column in range(6))
    exact_minor_rows = (0, 1, 2, 3, 6, 7)
    exact_minor = det_k([[w_exact[column][row] for column in range(6)]
                         for row in exact_minor_rows])
    assert exact_minor == -72 * ZETA**2
    w_mod = [[entry.to_mod() for entry in vector] for vector in w_exact]
    assert rank_mod(w_mod) == 6

    # det(B) is the sign of the twelve-cycle; det(W) is the product of the
    # selected character eigenvalues.  Therefore det(G)=det(B)/det(W).
    cursor = 0
    orbit = []
    while cursor not in orbit:
        orbit.append(cursor)
        cursor = RAY_PERMUTATION[cursor]
    assert cursor == 0 and len(orbit) == 12
    inversions = sum(left > right for index, left in enumerate(RAY_PERMUTATION)
                     for right in RAY_PERMUTATION[index + 1:])
    permutation_sign = -1 if inversions % 2 else 1
    b_character = next(label for label in range(ORDER)
                       if ZETA**label == K12.coerce(permutation_sign))
    w_character = sum(W_CHARACTERS) % ORDER
    quotient_character = (b_character - w_character) % ORDER
    assert quotient_character == sum(OMITTED_EULER_CHARACTERS) % ORDER
    determinant_twists = tuple(
        twist for twist in range(ORDER)
        if (5 * twist + sum(OMITTED_EULER_CHARACTERS)) % ORDER == 0
    )
    assert determinant_twists == (1,)
    determinant_twist = determinant_twists[0]
    physical_v_character = (quotient_character + 5 * determinant_twist) % ORDER
    assert (w_character, quotient_character, physical_v_character) == (11, 7, 0)

    formal_sparse_identity()
    local_indices, local_det, local_denominator = local_determinant_control(w_mod)

    # Lock the branch-local source statements this frame is paying down.
    spec = (
        ROOT
        / "documents"
        / "program-question-map"
        / "evidence"
        / "YUKAWA_DOWN_RESIDUE_SPEC_308.md"
    ).read_text(encoding="utf-8")
    for marker in (
        "ordered twelve-ray frame and ordered six-Euler frame",
        "Delta_G : det(G) ~= L",
        "The expression is independent of `alpha`",
        "normalized trace",
    ):
        assert marker in spec, marker

    print(f"exact_euler_characters={ALL_EULER_CHARACTERS}")
    print(f"selected_ordered_W_characters={W_CHARACTERS}; exact_rank=6")
    print("normalization=earliest Euler anchor, then earliest nonzero ordered-ray coefficient = 1")
    print(f"exact_Euler_minor_rows={exact_minor_rows}; determinant=-72*zeta^2")
    print(f"det_characters_mod12=B:{b_character},W:{w_character},G:{quotient_character},V_twisted:{physical_v_character}")
    print("formal_identity=(sb-sa)^(sc-sb)^k1^(sd-sc)^k2^sa = sa^sb^sc^sd^k1^k2; sign=+1")
    print(f"good_prime_local_indices={local_indices}; nonzero_control_det={local_det}; denominator={local_denominator}")
    print("sparse_formula=c*det(E_W,e_a,e_b,e_c,e_d,k1,k2)/(Phi_a Phi_b Phi_c Phi_d)")
    print("quotient_lift_invariance=PASS")
    print("scope=determinant frame and local contraction only; H3 trace, Serre tails, Yukawa entries and physical normalization remain open")
    print("R026 YUKAWA DETERMINANT FRAME: PASS")


if __name__ == "__main__":
    main()
