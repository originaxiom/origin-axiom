"""Unrun P-210 verification controls; do not import/collect before admission.

Exact finite reconstructions only. No producer or stored result is loaded.
The design was committed before this implementation. No claim of global
Fredholm certification, physical exterior selection or blind prediction.
"""
from itertools import product
import unittest
import sympy as s


I2 = s.eye(2)
I3 = s.eye(3)
I6 = s.eye(6)
QI = s.diag(s.I, -s.I)
QJ = s.Matrix([[0, 1], [-1, 0]])
QK = QI * QJ
EPS = QJ
SX = s.Matrix([[0, 1], [1, 0]])
SY = s.Matrix([[0, -s.I], [s.I, 0]])
SZ = s.diag(1, -1)
GREEN = s.BlockMatrix([[s.zeros(6), I6], [I6, s.zeros(6)]]).as_explicit()
GAMMA = s.diag(I6, -I6)


def zero(matrix):
    return all(s.simplify(x) == 0 for x in matrix)


def h2(matrix):
    gram = matrix * matrix.H
    return gram - s.trace(gram) * I2 / 2


def graph(h):
    return I6.col_join(s.I * h)


def contraction(left, right):
    axes = (QJ, QI, QK)
    return s.Matrix(3, 3, lambda a, b: sum(
        (axes[a].T * EPS * left * axes[b])[m, n] * right[m, n]
        for m in range(2) for n in range(2)))


class SymmetricResponseChecks(unittest.TestCase):
    def assertZero(self, matrix):
        self.assertTrue(zero(matrix), str(matrix))

    def test_actual_symmetric_coupling_keeps_transpose_and_wrong_input(self):
        actual = contraction(I2, EPS.inv())
        self.assertEqual(actual, -2 * I3)
        for a, ca in enumerate((QJ, QI, QK)):
            for b, cb in enumerate((QJ, QI, QK)):
                self.assertEqual(actual[a, b], s.trace(ca * cb))
        self.assertNotEqual(contraction(I2, I2), actual)
        self.assertNotEqual(contraction(I2, EPS), actual)

    def test_full_q8_commutant_and_nonscalar_family_freedom(self):
        variables = s.symbols("x0:36")
        unknown = s.Matrix(6, 6, variables)
        generators = (s.kronecker_product(I3, QI), s.kronecker_product(I3, QJ))
        equations = [x for g in generators for x in unknown * g - g * unknown]
        matrix, _ = s.linear_eq_to_matrix(equations, variables)
        self.assertEqual(36 - matrix.rank(), 9)
        basis = []
        for a, b in product(range(3), repeat=2):
            family = s.zeros(3)
            family[a, b] = 1
            candidate = s.kronecker_product(family, I2)
            for g in generators:
                self.assertZero(candidate * g - g * candidate)
            basis.append(s.Matrix(list(candidate)))
        self.assertEqual(s.Matrix.hstack(*basis).rank(), 9)
        nonscalar = s.kronecker_product(s.diag(1, 2, 3), I2)
        self.assertNotEqual(nonscalar, nonscalar[0, 0] * I6)

    def test_four_cayley_planes_and_nonnull_wrong_graph(self):
        families = (s.zeros(3), I3, s.diag(1, -1, 2),
                    s.Matrix([[1, s.I, 0], [-s.I, 0, 1], [0, 1, -2]]))
        for family in families:
            h = s.kronecker_product(family, I2)
            self.assertZero(h - h.H)
            unitary = (I6 - s.I * h) * (I6 + s.I * h).inv()
            self.assertZero(unitary.H * unitary - I6)
            plane = graph(h)
            self.assertEqual(plane.rank(), 6)
            self.assertZero(plane.H * GREEN * plane)
            a = (I6 + s.I * h) / s.sqrt(2)
            b = (I6 - s.I * h) / s.sqrt(2)
            self.assertZero(b - unitary * a)
        wrong = I6.col_join(I6)
        self.assertEqual(wrong.H * GREEN * wrong, 2 * I6)

    def test_all_eight_graded_family_involutions_and_conditional_indices(self):
        counts = {}
        for signs in product((-1, 1), repeat=3):
            unitary = s.kronecker_product(s.diag(*signs), I2)
            plus = (I6 + unitary) / 2
            minus = I6 - plus
            plane = s.BlockMatrix([[plus, s.zeros(6)],
                                   [s.zeros(6), minus]]).as_explicit()
            rank = 2 * signs.count(1)
            self.assertEqual(plus.rank(), rank)
            self.assertEqual(plane.rank(), 6)
            self.assertZero(plane.H * GREEN * plane)
            self.assertZero(GAMMA * plane - plane * GAMMA)
            self.assertZero(unitary * unitary - I6)
            counts[rank - 3] = counts.get(rank - 3, 0) + 1
        self.assertEqual(counts, {-3: 1, -1: 3, 1: 3, 3: 1})

    def test_null_graph_does_not_automatically_preserve_gamma(self):
        for h, expected_joined_rank in ((s.zeros(6), 6), (I6, 12)):
            plane = graph(h)
            self.assertZero(plane.H * GREEN * plane)
            self.assertEqual(plane.row_join(GAMMA * plane).rank(), expected_joined_rank)

    def test_48_state_covariances_and_frozen_state_rejection(self):
        states = (s.diag(2, 1), s.Matrix([[1, s.I], [0, 1]]), I2)
        lifts = (QI, QJ, (I2 + QI) / s.sqrt(2), (I2 - QJ) / s.sqrt(2))
        permutations = (I3, s.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]]))
        count = 0
        for state, g, phase, perm in product(states, lifts, (1, s.I), permutations):
            transformed = phase * g * state * g.H
            self.assertZero(h2(transformed) - g * h2(state) * g.H)
            big = s.kronecker_product(perm, g)
            self.assertZero(s.kronecker_product(I3, h2(transformed))
                            - big * s.kronecker_product(I3, h2(state)) * big.H)
            count += 1
        self.assertEqual(count, 48)
        frozen = s.diag(1, 0)
        self.assertNotEqual(QJ * frozen * QJ.H, frozen)
        self.assertZero(h2(I2))

    def test_18_projector_paths_keep_opposite_limits_and_endpoint(self):
        count = 0
        for direction, step in product((SX, -SX, SY, -SY, SZ, -SZ),
                                       (s.Rational(1, 2), s.Rational(1, 4), s.Rational(1, 8))):
            plus = (I2 + direction) / 2
            minus = I2 - plus
            root = s.sqrt(1 + step) * plus + s.sqrt(1 - step) * minus
            self.assertZero(root * root.H - I2 - step * direction)
            self.assertZero(h2(root) - step * direction)
            self.assertZero(plus * minus)
            self.assertEqual(s.kronecker_product(I3, plus).rank(), 3)
            self.assertEqual((plus - minus) ** 2, I2)
            count += 1
        self.assertEqual(count, 18)

    def test_tail_clifford_green_grading_and_wrong_commuting_symbol(self):
        momentum = s.symbols("p", real=True)
        mass = s.kronecker_product(I3, s.diag(1, -2))
        derivative = -s.I * s.kronecker_product(SX, I6)
        zeroth = -s.kronecker_product(SY, mass)
        symbol = s.I * momentum * derivative + zeroth
        self.assertZero(derivative.H + derivative)
        self.assertEqual(s.I * derivative, GREEN)
        self.assertZero(zeroth.H - zeroth)
        self.assertZero(GAMMA * symbol + symbol * GAMMA)
        self.assertZero(symbol ** 2 - s.kronecker_product(I2, momentum ** 2 * I6 + mass ** 2))
        wrong = s.kronecker_product(SX, momentum * I6 - mass)
        self.assertFalse(zero(wrong ** 2 - symbol ** 2))

    def test_both_decaying_slots_scalar_controls_and_zero_threshold(self):
        radial = s.symbols("t", nonnegative=True)
        scale = s.symbols("s", positive=True)
        mass = scale * s.kronecker_product(I3, SZ)
        for index in range(6):
            vector = I6[:, index] * s.exp(-scale * radial)
            if index % 2 == 0:
                self.assertZero(vector.diff(radial) + mass * vector)
            else:
                self.assertZero(-vector.diff(radial) + mass * vector)
        self.assertEqual(s.integrate(s.exp(-2 * scale * radial), (radial, 0, s.oo)), 1 / (2 * scale))
        for family, positive in ((I3, 6), (-I3, 0), (s.diag(-2, 1, 3), 4)):
            matrix = s.kronecker_product(family, I2)
            self.assertEqual(sum(n for value, n in matrix.eigenvals().items() if value > 0), positive)
        self.assertEqual(len(s.zeros(6).nullspace()), 6)
        self.assertEqual(s.limit(1 / (2 * scale), scale, 0, dir="+"), s.oo)

    def test_actual_cusp_conjugation_and_retained_bump_normalization(self):
        radial = s.symbols("t", real=True)
        weight = s.exp(-radial)
        profile = s.Function("f")(radial)
        correct = s.sqrt(weight) * (s.diff(profile / s.sqrt(weight), radial)
                  + s.diff(weight, radial) * profile / (2 * weight * s.sqrt(weight)))
        self.assertEqual(s.simplify(correct), profile.diff(radial))
        wrong = weight * (s.diff(profile / weight, radial)
                + s.diff(weight, radial) * profile / (2 * weight ** 2))
        self.assertNotEqual(s.simplify(wrong), profile.diff(radial))
        coordinate = s.symbols("x", real=True)
        bump = coordinate ** 2 * (1 - coordinate) ** 2
        norm = s.integrate(bump ** 2, (coordinate, 0, 1))
        derivative_norm = s.integrate(s.diff(bump, coordinate) ** 2, (coordinate, 0, 1))
        self.assertEqual(norm, s.Rational(1, 630))
        self.assertEqual(derivative_norm / norm, 12)
        for endpoint, order in product((0, 1), (0, 1)):
            self.assertEqual(s.diff(bump, coordinate, order).subs(coordinate, endpoint), 0)
