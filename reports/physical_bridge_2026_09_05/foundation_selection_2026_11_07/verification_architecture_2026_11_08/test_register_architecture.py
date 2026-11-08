"""Seven exact controls, implemented for source review only: UNRUN.

Do not import/collect this file before separate execution admission.
The finite tests do not certify the all-word/cofinality proofs.
"""

from __future__ import annotations

import unittest
from itertools import product

from register_exact import (
    L, R, ONE, PERM_ID, QuaternionCover, apply_word_map, commutator,
    homogeneous, inner_coefficient, inner_joint_inverse, inner_joint_multiply,
    inverse_word, magnus, permutation_word, qinverse, qmul, rational_rank,
    reduce_word, rho, series_add, series_multiply, tensor_product,
)


def matrix_multiply(a: tuple, b: tuple) -> tuple:
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)) for i in range(3))


def heisenberg_matrix(x: int, y: int, inverse: bool = False) -> tuple:
    if inverse:
        return ((1, -x, x * y), (0, 1, -y), (0, 0, 1))
    return ((1, x, 0), (0, 1, y), (0, 0, 1))


class RegisterArchitectureControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cover = QuaternionCover()
        cls.alpha = (1,) * 4
        cls.beta = (2,) * 4
        cls.comparison = commutator(cls.alpha, cls.beta)

    def nword(self, word: tuple[int, ...]) -> tuple[int, ...]:
        endpoint, result = self.cover.rewrite(word)
        self.assertEqual(endpoint, ONE)
        return result

    def test_01_cover_basis_and_oriented_flow(self) -> None:
        cover = self.cover
        self.assertEqual((len(cover.vertices), len(cover.edges), len(cover.tree_edges)), (8, 16, 7))
        self.assertEqual(len(cover.basis), 9)
        for index, word in cover.basis.items():
            self.assertEqual(rho(word), ONE)
            self.assertEqual(cover.rewrite(word), (ONE, (index,)))
            self.assertEqual(cover.expand((index,)), word)
        corpus = list(cover.basis.values()) + [self.alpha, self.beta, self.comparison]
        corpus += [reduce_word(u + v) for u in corpus[:4] for v in corpus[:4]]
        for word in corpus:
            rewritten = self.nword(word)
            self.assertEqual(cover.expand(rewritten), reduce_word(word))
            endpoint, flow = cover.edge_flow(word)
            self.assertEqual(endpoint, ONE)
            reconstructed: dict = {}
            for letter in rewritten:
                _, basis_flow = cover.edge_flow(cover.basis[abs(letter)])
                for edge, value in basis_flow.items():
                    reconstructed[edge] = reconstructed.get(edge, 0) + (1 if letter > 0 else -1) * value
            reconstructed = {edge: value for edge, value in reconstructed.items() if value}
            self.assertEqual(flow, reconstructed)
        _, forward = cover.edge_flow(self.alpha)
        _, backward = cover.edge_flow(inverse_word(self.alpha))
        self.assertTrue(forward)
        self.assertEqual(backward, {edge: -value for edge, value in forward.items()})
        self.assertNotEqual(backward, forward)  # wrong inverse orientation cannot pass

    def test_02_lost_order_and_independent_heisenberg_replay(self) -> None:
        ab, ba = self.alpha + self.beta, self.beta + self.alpha
        self.assertEqual(self.cover.edge_flow(ab), self.cover.edge_flow(ba))
        a, b = self.nword(self.alpha), self.nword(self.beta)
        first_a = homogeneous(magnus(a, 2), 1)
        first_b = homogeneous(magnus(b, 2), 1)
        expected = series_add(tensor_product(first_a, first_b), tensor_product(first_b, first_a), -1)
        self.assertTrue(expected)
        actual = homogeneous(magnus(self.nword(self.comparison), 2), 2)
        self.assertEqual(actual, expected)
        self.assertEqual(magnus(self.nword(self.comparison), 1), {(): 1})
        self.assertNotEqual(magnus(self.nword(ab), 2), magnus(self.nword(ba), 2))
        # Independent 3x3 integer matrices use the graph's two edge functionals.
        images = {}
        for index, word in self.cover.basis.items():
            _, flow = self.cover.edge_flow(word)
            images[index] = (flow.get((ONE, 1), 0), flow.get((ONE, 2), 0))
        matrix = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
        for letter in self.nword(self.comparison):
            x, y = images[abs(letter)]
            matrix = matrix_multiply(matrix, heisenberg_matrix(x, y, inverse=letter < 0))
        self.assertEqual(matrix, ((1, 0, 1), (0, 1, 0), (0, 0, 1)))
        self.assertNotEqual(actual, {})  # deleting the mixed term gives the wrong zero

    def test_03_independent_degree_two_commutators(self) -> None:
        tensor_basis = [(i, j) for i in range(1, 10) for j in range(1, 10)]
        rows = []
        for i in range(1, 10):
            for j in range(i + 1, 10):
                part = homogeneous(magnus(commutator((i,), (j,)), 2), 2)
                self.assertEqual(part, {(i, j): 1, (j, i): -1})
                self.assertNotEqual(part, {(i, j): 1, (j, i): 1})
                rows.append([part.get(monomial, 0) for monomial in tensor_basis])
        self.assertEqual(rational_rank(rows), 36)
        self.assertEqual(rational_rank(rows[:-1] + [rows[0]]), 35)
        self.assertEqual(rational_rank([[0, 0], [0, 0]]), 0)

    def test_04_higher_order_inverse_and_syllable_guards(self) -> None:
        nested = commutator(self.alpha, self.comparison)
        rewritten = self.nword(nested)
        self.assertEqual(magnus(rewritten, 2), {(): 1})
        self.assertTrue(homogeneous(magnus(rewritten, 3), 3))
        actual_inverse = magnus((-1,), 3)
        self.assertEqual(actual_inverse, {(): 1, (1,): -1, (1, 1): 1, (1, 1, 1): -1})
        self.assertEqual(series_multiply(actual_inverse, magnus((1,), 3), 3), {(): 1})
        wrong_inverse = {(): 1, (1,): -1}
        self.assertNotEqual(series_multiply(wrong_inverse, magnus((1,), 3), 3), {(): 1})
        cases = [((1, 2), (2, -3), (1, -1), (3, 2)), ((2, -2), (1, -1), (2, 1)), ((9, -1),)]
        for syllables in cases:
            word = tuple(letter for generator, power in syllables for letter in [generator if power > 0 else -generator] * abs(power))
            monomial = tuple(generator for generator, _ in syllables)
            expected = 1
            for _, power in syllables:
                expected *= power
            self.assertEqual(magnus(word, len(syllables)).get(monomial), expected)

    def test_05_native_transport_in_both_composition_orders(self) -> None:
        induced_l = self.cover.induced_map(L)
        induced_r = self.cover.induced_map(R)
        corpus = list(self.cover.basis.values()) + [self.alpha, self.beta, self.comparison]
        for mapping, induced in [(L, induced_l), (R, induced_r)]:
            for word in corpus:
                native = self.nword(apply_word_map(mapping, word))
                coordinate = apply_word_map(induced, self.nword(word))
                self.assertEqual(native, coordinate)
                self.assertEqual(self.cover.expand(coordinate), apply_word_map(mapping, word))
        for outer, inner, outer_n, inner_n in [(L, R, induced_l, induced_r), (R, L, induced_r, induced_l)]:
            for word in corpus:
                native = self.nword(apply_word_map(outer, apply_word_map(inner, word)))
                coordinate = apply_word_map(outer_n, apply_word_map(inner_n, self.nword(word)))
                self.assertEqual(native, coordinate)
        lr = self.nword(apply_word_map(L, apply_word_map(R, self.alpha)))
        rl = self.nword(apply_word_map(R, apply_word_map(L, self.alpha)))
        self.assertNotEqual(magnus(lr, 1), magnus(rl, 1))

    def test_06_finite_a5_register_is_not_the_relative_truncation(self) -> None:
        self.assertEqual(magnus(self.nword(self.comparison), 1), {(): 1})
        image = permutation_word(self.comparison)
        self.assertNotEqual(image, PERM_ID)
        self.assertEqual(image[0], 4)
        nested = commutator(self.alpha, self.comparison)
        self.assertEqual(magnus(self.nword(nested), 2), {(): 1})
        nested_image = permutation_word(nested)
        self.assertNotEqual(nested_image, PERM_ID)
        self.assertEqual(nested_image[0], 2)

    def test_07_finite_inner_lifted_joint_scope_control(self) -> None:
        # Restricted inner-quaternion example only, not the full E or 2O image.
        quaternions = self.cover.vertices
        pairs = list(product(quaternions, repeat=2))
        identity = (ONE, ONE)
        self.assertEqual(len(pairs), 64)
        for left in pairs:
            inverse = inner_joint_inverse(left)
            self.assertEqual(inner_joint_multiply(left, inverse), identity)
            self.assertEqual(inner_joint_multiply(inverse, left), identity)
            for right in pairs:
                multiplied = inner_joint_multiply(left, right)
                self.assertIn(multiplied, pairs)
                self.assertEqual(inner_coefficient(multiplied), qmul(inner_coefficient(left), inner_coefficient(right)))
        generators = [(quaternions[1], ONE), (quaternions[2], ONE), (ONE, quaternions[1]), (ONE, quaternions[2])]
        for first in generators:
            for second in pairs:
                for third in pairs:
                    self.assertEqual(
                        inner_joint_multiply(inner_joint_multiply(first, second), third),
                        inner_joint_multiply(first, inner_joint_multiply(second, third)),
                    )
        central = (ONE, (-1, 0, 0, 0))
        self.assertNotEqual(central, identity)
        self.assertNotEqual(inner_coefficient(central), ONE)
        hidden = ((-1, 0, 0, 0), (-1, 0, 0, 0))
        self.assertNotEqual(hidden, identity)
        self.assertEqual(inner_coefficient(hidden), ONE)
        self.assertEqual(sum(inner_coefficient(pair) == ONE for pair in pairs), 8)


if __name__ == "__main__":
    unittest.main()
