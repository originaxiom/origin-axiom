"""Unrun controls for lift families, infinite histories and graph joining.

Import only through the admitted runner. Finite controls do not certify
the general topological or infinite-history proofs in the companion notes.
"""
from fractions import Fraction
from itertools import product
import unittest

import sympy as s
import controls as c


IDENTITY = {"a": "a", "b": "b"}
LEFT = {"a": "a", "b": "ab"}
RIGHT = {"a": "ab", "b": "b"}
LEFT_BAR = {"a": "a", "b": "ba"}
RIGHT_BAR = {"a": "ba", "b": "b"}


def inner(word):
    return {g: c.reduce_word(word + g + c.inverse_word(word)) for g in "ab"}


def change_frame(mapping, word):
    return c.compose(inner(word), c.compose(mapping, inner(c.inverse_word(word))))


def word_power(mapping, exponent):
    result = IDENTITY
    for _ in range(exponent):
        result = c.compose(mapping, result)
    return result


class LiftFamilyChecks(unittest.TestCase):
    def test_all_four_fixed_pairs_and_their_transported_boundaries(self):
        cases = ((LEFT, RIGHT, "", "aBAb"),
                 (LEFT, RIGHT_BAR, "A", "BAba"),
                 (LEFT_BAR, RIGHT, "b", "baBA"),
                 (LEFT_BAR, RIGHT_BAR, "bA", "AbaB"))
        for left, right, frame, boundary in cases:
            with self.subTest(frame=frame):
                self.assertEqual(change_frame(LEFT, frame), left)
                self.assertEqual(change_frame(RIGHT, frame), right)
                self.assertEqual(c.apply_map(inner(frame), "aBAb"), boundary)
                for step in (left, right):
                    self.assertEqual(c.apply_map(step, boundary), boundary)
        self.assertNotEqual(c.apply_map(LEFT_BAR, "aBAb"), "aBAb")
        self.assertNotEqual(c.apply_map(RIGHT_BAR, "aBAb"), "aBAb")

    def test_independent_lifts_add_inner_moves_and_the_old_loop_survives(self):
        li, ri = {"a": "a", "b": "Ab"}, {"a": "aB", "b": "b"}
        self.assertEqual(c.compose(LEFT_BAR, li), inner("A"))
        self.assertEqual(c.compose(RIGHT_BAR, ri), inner("b"))
        step = c.compose(LEFT, c.compose(ri, LEFT))
        loop = word_power(step, 4)
        self.assertEqual(loop, inner("aBAb"))
        self.assertNotEqual(loop, IDENTITY)
        self.assertEqual(c.homology(loop), s.eye(2))
        self.assertEqual(c.apply_map(loop, "aBAb"), "aBAb")

    def test_relative_register_is_a_crossed_not_ordinary_product(self):
        # Compare the two specified actions on the same two-letter history.
        h_left, h_right = "A", "b"
        crossed = c.reduce_word(h_left + c.apply_map(LEFT, h_right))
        ordinary = c.reduce_word(h_left + h_right)
        actual = c.compose(LEFT_BAR, RIGHT_BAR)
        base = c.compose(LEFT, RIGHT)
        self.assertEqual(crossed, "b")
        self.assertNotEqual(crossed, ordinary)
        self.assertEqual(actual, c.compose(inner(crossed), base))
        self.assertNotEqual(actual, c.compose(inner(ordinary), base))

    def test_changing_frames_retains_both_path_endpoints(self):
        frames = ("a", "b", "ab", "BA")
        steps = (LEFT, RIGHT, LEFT)
        transported = IDENTITY
        original = IDENTITY
        for i, step in enumerate(steps):
            changed = c.compose(inner(frames[i+1]),
                                c.compose(step, inner(c.inverse_word(frames[i]))))
            transported = c.compose(changed, transported)
            original = c.compose(step, original)
        expected = c.compose(inner(frames[-1]),
                             c.compose(original, inner(c.inverse_word(frames[0]))))
        self.assertEqual(transported, expected)
        self.assertNotEqual(transported, original)


def positive_children(matrix):
    a, b, c0, d = matrix
    return ((a, a+b, c0, c0+d), (a+b, b, c0+d, d))


def cone(matrix):
    a, b, c0, d = matrix
    points = (Fraction(a, a+c0), Fraction(b, b+d))
    return min(points), max(points)


class InfiniteHistoryChecks(unittest.TestCase):
    def test_all_positive_prefixes_through_depth_nine_are_nested_cones(self):
        level = [(1, 0, 0, 1)]
        seen = 1
        for depth in range(1, 10):
            children = []
            for parent in level:
                lo, hi = cone(parent)
                for child in positive_children(parent):
                    a, b, c0, d = child
                    lower, upper = cone(child)
                    self.assertEqual(a*d-b*c0, 1)
                    self.assertLessEqual(lo, lower)
                    self.assertLessEqual(upper, hi)
                    self.assertEqual(upper-lower, Fraction(1, (a+c0)*(b+d)))
                    self.assertLessEqual(upper-lower, Fraction(1, depth+1))
                    children.append(child)
            level = children
            seen += len(level)
        self.assertEqual(seen, 1023)

    def test_golden_recovery_and_constant_letter_endpoint_controls(self):
        matrix = (1, 0, 0, 1)
        polynomial = lambda x: x*x+x-1
        for n in range(1, 17):
            matrix = positive_children(positive_children(matrix)[0])[1]
            lo, hi = cone(matrix)
            self.assertLessEqual(polynomial(lo), 0)
            self.assertGreaterEqual(polynomial(hi), 0)
            self.assertEqual(cone((1, n, 0, 1)), (Fraction(n, n+1), Fraction(1)))
            self.assertEqual(cone((1, 0, n, 1)), (Fraction(0), Fraction(1, n+1)))

    def test_chronological_blocks_have_opposite_endpoint_bounds(self):
        x, y, k = s.symbols("x y k", positive=True)
        after_left = (x+k*y)/(x+(k+1)*y)
        after_right = x/((k+1)*x+y)
        self.assertEqual(s.cancel(after_left-k/(k+1)-x/((k+1)*(x+(k+1)*y))), 0)
        self.assertEqual(s.cancel(1/(k+1)-after_right-y/((k+1)*((k+1)*x+y))), 0)
        a, b = 1, 1
        for block in range(1, 21):
            a += block*b
            self.assertGreater(Fraction(a, a+b), Fraction(block, block+1))
            b += block*a
            self.assertLess(Fraction(a, a+b), Fraction(1, block+1))

    def test_symmetric_stationary_laws_do_not_fix_history_correlations(self):
        q = s.symbols("q")
        transition = s.Matrix([[q, 1-q], [1-q, q]])
        swap = s.Matrix([[0, 1], [1, 0]])
        stationary = s.Matrix([[s.Rational(1, 2), s.Rational(1, 2)]])
        self.assertEqual(stationary*transition, stationary)
        self.assertEqual(swap*transition*swap, transition)
        self.assertEqual(transition*s.Matrix([1, -1]), (2*q-1)*s.Matrix([1, -1]))
        for probability in (s.Rational(1, 3), s.Rational(1, 2), s.Rational(2, 3)):
            law = transition.subs(q, probability)
            self.assertEqual(sum(stationary[i]*law[i, i] for i in range(2)), probability)
            self.assertTrue(all(0 < value < 1 for value in law))
        self.assertNotEqual(transition.subs(q, s.Rational(1, 3)),
                            transition.subs(q, s.Rational(2, 3)))


def incidence(vertices, edges):
    if vertices < 1 or any(not (0 <= a < vertices and 0 <= b < vertices) for a, b in edges):
        raise ValueError("Invalid vertex or edge")
    matrix = s.zeros(len(edges), vertices)
    for i, (a, b) in enumerate(edges):
        matrix[i, a] -= 1
        matrix[i, b] += 1
    return matrix


def form_triple(first, second, third, fibre):
    # Small exterior-algebra control, not a cochain model of B1043.
    return sum(v*w*z*s.LeviCivita(i, j, k)*fibre(a, b, c0)
               for (i, a), v in first.items()
               for (j, b), w in second.items()
               for (k, c0), z in third.items())


class GraphJoiningChecks(unittest.TestCase):
    def test_edge_matching_preserves_nontrivial_loop_transport(self):
        left, right = s.Matrix([[1, 1], [0, 1]]), s.Matrix([[1, 0], [1, 1]])
        generator = left*right
        frames = (s.eye(2), left, right)
        reps = [g*generator*g.inv() for g in frames]
        edges = ((0, 1), (1, 2), (2, 0))
        transports = [frames[t]*generator**n*frames[v].inv()
                      for (v, t), n in zip(edges, (0, 0, 1))]
        for (v, t), h in zip(edges, transports):
            self.assertEqual(reps[t], h*reps[v]*h.inv())
        loop = transports[2]*transports[1]*transports[0]
        self.assertEqual(loop, generator)
        self.assertNotEqual(loop, s.eye(2))
        normalized = [frames[t].inv()*h*frames[v]
                      for (v, t), h in zip(edges, transports)]
        self.assertEqual(normalized, [s.eye(2), s.eye(2), generator])
        bad = left*transports[0]
        self.assertNotEqual(reps[1], bad*reps[0]*bad.inv())

    def test_finite_graph_cohomology_consequences_and_disconnected_control(self):
        cases = ((1, (), (1, 1, 0, 0)),
                 (2, ((0, 1),), (1, 1, 1, 1)),
                 (3, ((0, 1), (1, 2), (2, 0)), (1, 2, 4, 3)),
                 (1, ((0, 0),), (1, 2, 2, 1)),
                 (2, ((0, 1), (0, 1)), (1, 2, 3, 2)),
                 (4, ((0, 1), (0, 2), (0, 3)), (1, 1, 3, 3)))
        # This checks MV arithmetic GIVEN H*(M), H*(T) and the restriction
        # maps. Injectivity, asphericity and identification require proof review.
        for vertices, edges, expected in cases:
            d0 = incidence(vertices, edges)
            d1 = s.zeros(2*len(edges), vertices)
            for row in range(len(edges)):
                d1[2*row, :] = d0[row, :]
            r0, r1 = d0.rank(), d1.rank()
            actual = (vertices-r0, len(edges)-r0+vertices-r1,
                      2*len(edges)-r1, len(edges))
            self.assertEqual(actual, expected)
            self.assertEqual(sum((-1)**i*b for i, b in enumerate(actual)), 0)
            self.assertEqual(r0, vertices-1)
        self.assertEqual(incidence(2, ()).rank(), 0)
        self.assertNotEqual(incidence(2, ()).rank(), 2-1)
        with self.assertRaises(ValueError):
            incidence(2, ((0, 2),))

    def test_cubic_sign_depends_on_the_fibre_tensor_not_its_name(self):
        alpha, beta, gamma = ({(i, i): 1} for i in range(3))
        symmetric = lambda a, b, c0: 1
        alternating = lambda a, b, c0: s.LeviCivita(a, b, c0)
        self.assertEqual(form_triple(alpha, beta, gamma, symmetric), 1)
        self.assertEqual(form_triple(beta, alpha, gamma, symmetric), -1)
        self.assertEqual(form_triple(beta, alpha, gamma, alternating), 1)
        combined = {(i, i): 1 for i in range(3)}
        self.assertEqual(form_triple(combined, combined, combined, symmetric), 0)
        self.assertEqual(form_triple(combined, combined, combined, alternating), 6)
        plane = (alpha, beta)
        self.assertTrue(all(form_triple(a, b, c0, symmetric) == 0
                            for a, b, c0 in product(plane, repeat=3)))


if __name__ == "__main__":
    raise SystemExit("Unadmitted entrypoint; use the separately reviewed runner")
