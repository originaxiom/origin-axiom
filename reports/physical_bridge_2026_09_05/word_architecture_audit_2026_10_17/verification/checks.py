"""Proposed exact controls. NOT executed or collected before admission.

These are in the research packet, not automatic repository discovery.
The explicit admitted runner is the sole planned execution entrypoint.
"""
from itertools import product
import unittest

import sympy as s
from sympy.matrices.exceptions import NonInvertibleMatrixError
import controls as c


def refined_partition(states, updates, outputs):
    """Second algorithm: deterministic partition refinement, not pair search."""
    blocks = {x: outputs[x] for x in states}
    while True:
        signatures = {x: (outputs[x], tuple((True, blocks[t[x]]) if x in t
                                            else (False,) for t in updates.values()))
                      for x in states}
        labels = {}
        fresh = {x: labels.setdefault(signatures[x], len(labels)) for x in states}
        if all((fresh[x] == fresh[y]) == (blocks[x] == blocks[y])
               for x in states for y in states):
            return fresh
        blocks = fresh


class PartialRecordChecks(unittest.TestCase):
    def test_definedness_is_observable_even_with_constant_output(self):
        self.assertFalse(c.future_equivalent((0, 1), {"u": {0: 0}}, {0: 0, 1: 0}, 0, 1))
        self.assertTrue(c.future_equivalent((0, 1), {"u": {0: 0, 1: 1}}, {0: 0, 1: 0}, 0, 1))

    def test_later_output_and_later_definedness_are_both_checked(self):
        states = (0, 1, 2, 3, 4, 5)
        step = {0: 2, 1: 3, 2: 4, 3: 5, 4: 4, 5: 5}
        outputs = dict.fromkeys(states, 0)
        outputs[5] = 1
        self.assertEqual(outputs[0], outputs[1])
        self.assertFalse(c.future_equivalent(states, {"u": step}, outputs, 0, 1))
        outputs[5] = 0
        self.assertTrue(c.future_equivalent(states, {"u": step}, outputs, 0, 1))
        self.assertFalse(c.future_equivalent(states, {"u": step, "v": {2: 2}}, outputs, 0, 1))

    def test_all_two_state_two_update_binary_output_machines(self):
        count = 0
        for targets in product((None, 0, 1), repeat=4):
            updates = {"u": {i: targets[i] for i in range(2) if targets[i] is not None},
                       "v": {i: targets[i+2] for i in range(2) if targets[i+2] is not None}}
            for values in product((0, 1), repeat=2):
                outputs = dict(enumerate(values))
                blocks = refined_partition((0, 1), updates, outputs)
                for x, y in product((0, 1), repeat=2):
                    self.assertEqual(c.future_equivalent((0, 1), updates, outputs, x, y),
                                     blocks[x] == blocks[y])
                count += 1
        self.assertEqual(count, 324)

    def test_malformed_domains_fail_closed(self):
        with self.assertRaises(ValueError):
            c.future_equivalent((0, 1), {"u": {0: 2}}, {0: 0, 1: 0}, 0, 1)
        with self.assertRaises(ValueError):
            c.future_equivalent((0, 1), {}, {0: 0}, 0, 1)


class WordLiftChecks(unittest.TestCase):
    def test_inverses_and_boundary_fixing_on_actual_word_generators(self):
        identity = {"a": "a", "b": "b"}
        left, right = {"a": "a", "b": "ab"}, {"a": "ab", "b": "b"}
        li, ri = {"a": "a", "b": "Ab"}, {"a": "aB", "b": "b"}
        for forward, backward in ((left, li), (right, ri)):
            self.assertEqual(c.compose(forward, backward), identity)
            self.assertEqual(c.compose(backward, forward), identity)
        for mapping in (left, right, li, ri):
            self.assertEqual(c.apply_map(mapping, "aBAb"), "aBAb")
        self.assertEqual(c.homology(left), s.Matrix([[1, 1], [0, 1]]))
        self.assertEqual(c.homology(right), s.Matrix([[1, 0], [1, 1]]))

    def test_same_homology_sign_different_based_boundary_action(self):
        left, ri = {"a": "a", "b": "ab"}, {"a": "aB", "b": "b"}
        step = c.compose(left, c.compose(ri, left))
        square = c.compose(step, step)
        invert = {"a": "A", "b": "B"}
        self.assertEqual(step, {"a": "aBA", "b": "a"})
        self.assertEqual(square, {"a": "aBAbA", "b": "aBA"})
        self.assertEqual(c.homology(square), -s.eye(2))
        self.assertEqual(c.homology(square), c.homology(invert))
        inner = {x: c.reduce_word("aB" + x + "bA") for x in "ab"}
        self.assertEqual(square, c.compose(inner, invert))
        self.assertEqual(c.apply_map(square, "aBAb"), "aBAb")
        self.assertNotEqual(c.apply_map(invert, "aBAb"), "aBAb")
        for h in ("a", "b"):
            pushed = c.reduce_word(h + "aBAb" + c.inverse_word(h))
            self.assertNotEqual(pushed, "aBAb")


class RelativePlacementChecks(unittest.TestCase):
    def test_polynomial_family_and_commutator_identity(self):
        n = s.symbols("n", integer=True)
        a = s.Matrix([[2, 1], [1, 1]])
        h = s.Matrix([[1, n], [0, 1]])
        b = h * a * h.inv()
        self.assertEqual(b, s.Matrix([[2+n, 1-n-n**2], [1, 1-n]]))
        self.assertEqual(s.expand(s.trace(a*b)), 7-n**2)
        self.assertEqual(s.expand(c.kappa(a, b)), n**4-5*n**2+2)
        self.assertNotEqual(s.trace(a*b).subs(n, 0), s.trace(a*b).subs(n, -1))
        self.assertEqual(b.subs(n, -1), s.Matrix([[1, 1], [1, 2]]))

    def test_double_coset_changes_preserve_product_class(self):
        a, b, h = s.Matrix([[2, 1], [1, 1]]), s.Matrix([[2, 3], [1, 2]]), s.Matrix([[1, 1], [0, 1]])
        h2 = a*h*b.inv()
        joined = a*h*b*h.inv()
        self.assertEqual(a*h2*b*h2.inv(), a*joined*a.inv())
        self.assertNotEqual(a*b, a*h*b*h.inv())
        g = s.Matrix([[1, 0], [2, 1]])
        self.assertEqual((g*a*g.inv())*(g*b*g.inv()), g*(a*b)*g.inv())

    def test_additive_commutator_formula_before_specialization(self):
        a = s.Matrix(2, 2, s.symbols("a:4"))
        b = s.Matrix(2, 2, s.symbols("b:4"))
        comm = a*b-b*a
        self.assertEqual((comm*a-a.adjugate()*comm).applyfunc(s.expand), s.zeros(2))
        self.assertEqual((comm*b-b.adjugate()*comm).applyfunc(s.expand), s.zeros(2))
        scaled_trace = s.trace(a*b*a.adjugate()*b.adjugate())
        self.assertEqual(s.expand(comm.det()-2*a.det()*b.det()+scaled_trace), 0)

    def test_all_three_nondegenerate_integral_branches(self):
        a = s.Matrix([[2, 1], [1, 1]])
        partners = ((s.Matrix([[2, 3], [1, 2]]), -1),
                    (s.Matrix([[5, 2], [2, 1]]), 1),
                    (s.Matrix([[8, 7], [9, 8]]), 59))
        for b, expected in partners:
            with self.subTest(partner=list(b)):
                x, determinant, content, k = c.primitive_reverser(a, b)
                self.assertEqual(determinant, expected)
                self.assertEqual(determinant*content**2, 2-k)
                self.assertEqual(x*a, a.inv()*x)
                self.assertEqual(x*b, b.inv()*x)
                variables = s.symbols("v:4")
                test = s.Matrix(2, 2, variables)
                equations = list(test*a-a.inv()*test) + list(test*b-b.inv()*test)
                linear, _ = s.linear_eq_to_matrix(equations, variables)
                self.assertEqual(4-linear.rank(), 1)

    def test_degenerate_locus_does_not_have_a_universal_sign_or_rank(self):
        a, q = s.symbols("a q", integer=True)
        m = s.Matrix([[2, 3], [1, 2]])
        x = s.Matrix([[a, -3*q], [q, -a]])
        self.assertEqual(x*m, m.inv()*x)
        variables = s.symbols("z:4")
        y = s.Matrix(2, 2, variables)
        equations, _ = s.linear_eq_to_matrix(list(y*m-m.inv()*y), variables)
        self.assertEqual(s.linsolve((equations, s.zeros(4, 1)), variables),
                         s.FiniteSet((-variables[3], -3*variables[2], variables[2], variables[3])))
        self.assertEqual(s.expand(x.det()), 3*q**2-a**2)
        self.assertNotIn(1, {(-u*u) % 3 for u in range(3)})
        self.assertEqual(x.subs({a: 1, q: 0}).det(), -1)
        golden = s.Matrix([[2, 1], [1, 1]])
        for reverser, determinant in ((s.Matrix([[0, 1], [-1, 0]]), 1),
                                       (s.Matrix([[1, 0], [-1, -1]]), -1)):
            self.assertEqual(reverser*golden, golden.inv()*reverser)
            self.assertEqual(reverser.det(), determinant)
        self.assertEqual(y*s.eye(2)-s.eye(2)*y, s.zeros(2))
        with self.assertRaises(ValueError):
            c.primitive_reverser(m, m)
        with self.assertRaises(ValueError):
            c.primitive_reverser(s.eye(2), s.eye(2))

    def test_complex_trace_equivalence_does_not_erase_integral_orientation(self):
        a, b = s.Matrix([[2, 1], [1, 1]]), s.Matrix([[2, 3], [1, 2]])
        x = s.Matrix([[2, -3], [1, -2]])
        self.assertEqual(x.det(), -1)
        self.assertEqual((s.I*x).det(), 1)
        for g in (a, b):
            self.assertEqual((s.I*x)*g*(s.I*x).inv(), g.inv())
        self.assertEqual((s.trace(a), s.trace(b), s.trace(a*b)), (3, 4, 10))
        self.assertEqual(s.trace(a.inv()*b.inv()), s.trace(a*b))

    def test_literal_mirror_gluing_inequality_is_not_a_chirality_certificate(self):
        # For solid tori in (meridian, longitude) marking, both diagonal
        # reflections extend; -I extends orientation-preservingly.
        phi = s.Matrix([[0, 1], [1, 0]])
        h = s.diag(1, -1)
        mirror = h*phi*h.inv()
        self.assertNotEqual(phi, mirror)
        self.assertEqual(mirror, -s.eye(2)*phi)
        h2 = s.diag(-1, 1)
        self.assertEqual(h2*phi, phi*h)
        self.assertEqual(h.det(), -1)
        self.assertEqual(h2.det(), -1)
        self.assertEqual((-s.eye(2)).det(), 1)


class ActualJoinChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.n = c.r85()

    def test_actual_field_and_all_three_retained_joins(self):
        n = self.n
        polynomial = s.Poly(n.C.Q**6-34*n.C.Q**3+1, n.C.Q, domain=s.QQ)
        self.assertTrue(polynomial.is_irreducible)
        self.assertEqual(n.CHARS, ((0, 1), (1, 1), (1, 0)))
        for ab in n.CHARS:
            with self.subTest(character=ab):
                rec = n.case(ab)
                self.assertTrue(rec["checks"])
                self.assertTrue(all(rec["checks"].values()))
                self.assertEqual(c.r85_relators(rec["_whole"], n.DOUBLE_RELS), [True]*6)
                self.assertTrue(c.matching(c.r85_boundary(rec["_left"]),
                                          c.r85_boundary(rec["_right"], True),
                                          n.C.eye(5, n.K), n.C.same, n.C.inv))

    def test_separate_frame_change_needs_its_intertwiner(self):
        n = self.n
        identity = n.C.eye(5, n.K)
        frame = identity+c.r85_unit(0, 4)
        for ab in n.CHARS:
            with self.subTest(character=ab):
                rec = n.case(ab)
                left, right = rec["_left"], rec["_right"]
                changed = c.r85_conjugate(right, frame)
                self.assertEqual(c.r85_relators(changed, n.LEFT_RELS), [True]*2)
                self.assertFalse(c.matching(c.r85_boundary(left), c.r85_boundary(changed, True),
                                           identity, n.C.same, n.C.inv))
                self.assertFalse(all(c.r85_relators(c.r85_whole(left, changed), n.DOUBLE_RELS)))
                self.assertTrue(c.matching(c.r85_boundary(left), c.r85_boundary(changed, True),
                                          n.C.inv(frame), n.C.same, n.C.inv))
                left_frame = identity+c.r85_unit(1, 0)
                changed_left = c.r85_conjugate(left, left_frame)
                self.assertTrue(c.matching(c.r85_boundary(changed_left), c.r85_boundary(changed, True),
                                          left_frame*n.C.inv(frame), n.C.same, n.C.inv))

    def test_compatible_bend_is_not_automatically_a_common_frame_change(self):
        n = self.n
        for ab in n.CHARS:
            with self.subTest(character=ab):
                rec = n.case(ab)
                left, right = rec["_left"], rec["_right"]
                values = []
                for t in (1, 2, 3):
                    frame = c.r85_scale(t)
                    self.assertEqual(n.determinant(frame), n.K.one)
                    for seam in c.r85_boundary(left).values():
                        self.assertTrue(n.C.same(frame*seam, seam*frame))
                    bent = c.r85_conjugate(right, frame)
                    self.assertEqual(c.r85_relators(c.r85_whole(left, bent), n.DOUBLE_RELS), [True]*6)
                    values.append(c.r85_trace(left["x"]*bent["x"]))
                rows_left, rows_right = left["x"].to_list(), right["x"].to_list()
                coefficient = sum((rows_left[i][4]*rows_right[4][i] for i in range(4)), n.K.zero)
                self.assertNotEqual(coefficient, n.K.zero)
                for t, value in zip((1, 2, 3), values):
                    self.assertEqual(value, values[0]-coefficient+coefficient/n.K.convert(t)**5)
                self.assertNotEqual(values[0], values[1])
                self.assertNotEqual(values[1], values[2])

    def test_interface_roster_and_singular_frame_are_rejected(self):
        with self.assertRaises(ValueError):
            c.matching({}, {}, s.eye(2), lambda a, b: a == b, lambda a: a.inv())
        with self.assertRaises(ValueError):
            c.matching({"u": s.eye(2)}, {"v": s.eye(2)}, s.eye(2), lambda a, b: a == b, lambda a: a.inv())
        with self.assertRaises(ValueError):
            c.r85_scale(0)
        with self.assertRaises(NonInvertibleMatrixError):
            c.matching({"u": s.eye(2)}, {"u": s.eye(2)}, s.zeros(2),
                       lambda a, b: a == b, lambda a: a.inv())


if __name__ == "__main__":
    raise SystemExit("Not admitted through this entrypoint; use the separately reviewed runner")
