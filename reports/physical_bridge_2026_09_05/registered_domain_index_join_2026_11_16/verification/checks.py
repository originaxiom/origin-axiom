"""Unrun exact author controls for the bounded P-C3 statements.

No producer modules, measured data or saved scientific outputs are loaded.
Import and collection belong to the separately reviewed execution scope.
"""

from itertools import product
import unittest

import sympy as sp


I = sp.I
Q = sp.Rational


def commutator(left, right):
    return left * right - right * left


def reduced(matrix):
    return matrix.applyfunc(sp.simplify)


def matrix_unit(size, row, column):
    result = sp.zeros(size)
    result[row, column] = 1
    return result


def quaternion_data():
    qi = sp.diag(I, -I)
    qj = sp.Matrix([[0, 1], [-1, 0]])
    qk = qi * qj
    return qi, qj, qk, (qj, qi, qk)


def axis_action(gauge_matrix, basis):
    """Columns are actual conjugates expressed in the trace-orthogonal basis."""
    inverse = gauge_matrix.inv()
    return reduced(sp.Matrix(3, 3, lambda a, b:
        -sp.trace(basis[a] * gauge_matrix * basis[b] * inverse) / 2))


def contraction(state, pairing, basis):
    epsilon = sp.Matrix([[0, 1], [-1, 0]])
    result = sp.zeros(3)
    for a, b in product(range(3), repeat=2):
        coefficient = basis[a].T * epsilon * state * basis[b]
        result[a, b] = sum(coefficient[m, n] * pairing[m, n]
                           for m, n in product(range(2), repeat=2))
    return reduced(result)


class ExactMatrixChecks(unittest.TestCase):
    def assert_matrix_equal(self, left, right):
        self.assertEqual(reduced(left - right), sp.zeros(*left.shape))

    def assert_matrix_differs(self, left, right):
        self.assertNotEqual(reduced(left - right), sp.zeros(*left.shape))


class RegisteredVertexChecks(ExactMatrixChecks):
    def test_quaternion_relations_and_conjugation_generators(self):
        qi, qj, qk, basis = quaternion_data()
        identity = sp.eye(2)
        for generator in (qi, qj, qk):
            self.assertEqual(generator ** 2, -identity)
        self.assertEqual(qi * qj, qk)
        self.assertEqual(qj * qi, -qk)
        self.assertNotEqual(qj * qi, qk)  # Planted commutation/sign error.

        quarter_turn = (identity + qi) / sp.sqrt(2)
        generators = (qi, qj, quarter_turn)
        for left, right in product(generators, repeat=2):
            ol = axis_action(left, basis)
            oright = axis_action(right, basis)
            self.assert_matrix_equal(axis_action(left * right, basis), ol * oright)
            self.assert_matrix_equal(ol.T * ol, sp.eye(3))
            self.assertEqual(ol.det(), 1)
            # Absolute values define a representation only on this monomial family.
            self.assert_matrix_equal(axis_action(left * right, basis).applyfunc(abs),
                                     ol.applyfunc(abs) * oright.applyfunc(abs))
        rotation = axis_action(quarter_turn, basis)
        self.assertEqual(rotation.applyfunc(abs).det(), -1)
        x, y = sp.Matrix([1, 0, 0]), sp.Matrix([0, 1, 0])
        unsigned = rotation.applyfunc(abs)
        self.assert_matrix_equal((rotation * x).cross(rotation * y), rotation * x.cross(y))
        self.assert_matrix_differs((unsigned * x).cross(unsigned * y), unsigned * x.cross(y))

    def test_coupling_span_full_and_traceless(self):
        _, _, _, basis = quaternion_data()
        units = [matrix_unit(2, m, n) for m, n in product(range(2), repeat=2)]
        traceless = [sp.diag(1, -1), units[1], units[2]]
        for states in (units, traceless):
            columns = [sp.Matrix(list(contraction(state, pairing, basis)))
                       for state, pairing in product(states, units)]
            self.assertEqual(sp.Matrix.hstack(*columns).rank(), 9)
        self.assertTrue(all(pairing.rank() == 1 for pairing in units))
        single = contraction(traceless[0], units[1], basis)
        self.assertLess(single.rank(), 3)

    def test_coupling_covariance_and_unsigned_counterexample(self):
        qi, qj, _, basis = quaternion_data()
        units = [matrix_unit(2, m, n) for m, n in product(range(2), repeat=2)]
        # The unipotent control also tests the stated SL2(C) covariance.
        generators = (qi, qj, (sp.eye(2) + qi) / sp.sqrt(2),
                      sp.Matrix([[1, 1], [0, 1]]))
        for gauge, state, pairing in product(generators, units, units):
            axes = axis_action(gauge, basis)
            changed = contraction(gauge * state * gauge.inv(),
                                  gauge * pairing * gauge.T, basis)
            original = contraction(state, pairing, basis)
            self.assert_matrix_equal(changed, axes * original * axes.T)
            self.assert_matrix_equal(axes.T * changed * axes, original)

        state = sp.diag(1, -1)
        pairing = sp.Matrix([[0, -1], [0, 0]])
        original = contraction(state, pairing, basis)
        expected = sp.Matrix([[-1, 0, -I], [0, 1, 0], [I, 0, -1]])
        self.assert_matrix_equal(original, expected)
        changed = contraction(qj * state * qj.inv(), qj * pairing * qj.T, basis)
        axes = axis_action(qj, basis)
        unsigned = axes.applyfunc(abs)
        self.assert_matrix_differs(unsigned.T * changed * unsigned, original)
        self.assert_matrix_equal(axes.T * changed * axes, original)

    def test_inner_residual_and_vertical_spin_sheet(self):
        qi, qj, qk, basis = quaternion_data()
        identity = sp.eye(2)
        elements = (identity, -identity, qi, -qi, qj, -qj, qk, -qk)
        for h in elements:
            deck = sp.kronecker_product(sp.eye(3), h)
            axes = axis_action(h, basis)
            signed_lift = sp.kronecker_product(axes, h)
            residual = signed_lift * deck.inv()
            self.assert_matrix_equal(residual, sp.kronecker_product(axes, identity))
            self.assert_matrix_equal(deck * deck.inv(), sp.eye(6))
        for h, k in product(elements, repeat=2):
            self.assert_matrix_equal(axis_action(h * k, basis),
                                     axis_action(h, basis) * axis_action(k, basis))
            # Evaluate the argument on the finite regular cover directly.
            # Equivariant sections have Psi(k)=R_k seed for each seed vector.
            lift_h = sp.kronecker_product(axis_action(h, basis), h)
            section_at_inverse_argument = sp.kronecker_product(sp.eye(3), h.inv() * k)
            observed = lift_h * section_at_inverse_argument
            expected = sp.kronecker_product(axis_action(h, basis), k)
            self.assert_matrix_equal(observed, expected)
        lift_i = sp.kronecker_product(axis_action(qi, basis), qi)
        right_side_argument = sp.kronecker_product(sp.eye(3), qj * qi.inv())
        left_side_argument = sp.kronecker_product(sp.eye(3), qi.inv() * qj)
        self.assert_matrix_differs(lift_i * right_side_argument, lift_i * left_side_argument)
        deck = sp.kronecker_product(sp.eye(3), qi)
        lift = sp.kronecker_product(axis_action(qi, basis), qi)
        self.assert_matrix_differs(lift, lift * deck.inv())  # Missing argument/deck factor.
        self.assert_matrix_differs(axis_action(qi, basis), sp.eye(3))
        self.assertEqual(axis_action(-identity, basis), sp.eye(3))

        k_epsilon, j_epsilon = -1, -1
        unspun = sp.eye(3) / k_epsilon
        spun = j_epsilon * unspun
        self.assertEqual(unspun, -sp.eye(3))
        self.assertEqual(spun, sp.eye(3))
        self.assertNotEqual(unspun, spun)  # Omitting the declared vertical spin changes the sheet.
        self.assertEqual(unspun * axis_action(-identity, basis), -sp.eye(3))

    def test_full_and_slot_family_constant_stabilizers(self):
        full = [matrix_unit(3, a, b) for a, b in product(range(3), repeat=2)]
        slots = [matrix_unit(3, a, b) for a, b in ((0, 2), (1, 2), (2, 0), (2, 1), (2, 2))]
        variables = sp.symbols("l0:9 b0:9")
        left, inverse_right = sp.Matrix(3, 3, variables[:9]), sp.Matrix(3, 3, variables[9:])
        identity_pair = sp.Matrix(list(sp.eye(3)) + list(sp.eye(3)))
        for family in (full, slots):
            equations = [entry for coefficient in family
                         for entry in left.T * coefficient - coefficient * inverse_right]
            system, constants = sp.linear_eq_to_matrix(equations, variables)
            self.assertEqual(constants, sp.zeros(len(equations), 1))
            self.assertEqual(system.rank(), 17)
            self.assertEqual(len(system.nullspace()), 1)
            self.assertEqual(system * identity_pair, sp.zeros(len(equations), 1))
        nonscalar = sp.diag(1, 2, 3)
        self.assertTrue(any(nonscalar.T * y - y * nonscalar != sp.zeros(3) for y in slots))
        # A single coupling can leave more freedom than the whole family.
        equations = list(left.T * slots[-1] - slots[-1] * inverse_right)
        system, _ = sp.linear_eq_to_matrix(equations, variables)
        self.assertLess(system.rank(), 17)


def root_data():
    generator = sp.diag(-2, -2, -2, 3, 3)
    positive = matrix_unit(5, 3, 0)
    negative = matrix_unit(5, 0, 3)
    return generator, positive, negative


def source_cubic(connection, u, v):
    return -I * sp.trace(u * commutator(connection, v)
                         - v * commutator(connection, u)) / 2


def polarized_vertex(first, second, third):
    total = 0
    for a, b, c in ((first, second, third), (second, third, first), (third, first, second)):
        total += sp.trace(a[0] * (commutator(b[1], c[2]) + commutator(c[1], b[2])))
    return I * total


def normalized_squared(q, root_pairing, h_norm, action_scale, area_form, area_metric,
                       mixed_integral, c_plus, c_minus, connection_weight=Q(1, 2)):
    za = connection_weight * h_norm * area_form / action_scale
    zu = root_pairing * c_plus * mixed_integral / action_scale
    zv = root_pairing * c_minus * mixed_integral / action_scale
    zh = h_norm * area_metric / action_scale
    raw_squared = q ** 2 * root_pairing ** 2 * area_form ** 2 / action_scale ** 2
    return sp.cancel(raw_squared / (za * zu * zv)), sp.cancel(q ** 2 / zh)


class PhysicalVertexChecks(ExactMatrixChecks):
    def test_source_cubic_and_polarization(self):
        h, positive, negative = root_data()
        fields = ((h, positive, negative), (2 * h, 3 * positive, 5 * negative),
                  (7 * h, 11 * positive, 13 * negative))
        parameters = sp.symbols("t1 t2 t3")
        slots = [sum((parameters[n] * fields[n][slot] for n in range(3)), sp.zeros(5))
                 for slot in range(3)]
        source = sp.expand(source_cubic(*slots))
        actual = source.coeff(parameters[0]).coeff(parameters[1]).coeff(parameters[2])
        expected = polarized_vertex(*fields)
        self.assertEqual(actual, expected)
        self.assertNotEqual(actual, 0)
        self.assertNotEqual(actual, -expected)
        self.assertNotEqual(actual, expected / 2)
        self.assertEqual(source_cubic(h, positive, negative),
                         I * sp.trace(h * commutator(positive, negative)))
        self.assertEqual(source_cubic(h, h, h), 0)

    def test_root_vertex_and_physical_mass_derivative(self):
        h, positive, negative = root_data()
        charge = 5
        self.assertEqual(commutator(h, positive), charge * positive)
        self.assertEqual(commutator(h, negative), -charge * negative)
        self.assertEqual(sp.trace(h * h), 30)
        self.assertEqual(sp.trace(positive * negative), 1)
        omega = Q(3, 2)
        # Constant local jets compute the coefficient of the connection variation.
        t = sp.Symbol("t", real=True)
        p1 = -I * commutator(t * h, positive)
        row_derivative = (-p1 / omega).diff(t)
        projected = omega * sp.trace(negative * row_derivative)
        cubic = source_cubic(h, positive, negative)
        self.assertEqual(projected, cubic)
        self.assertEqual(projected, 5 * I)
        self.assertNotEqual(sp.trace(negative * row_derivative), cubic)
        self.assertNotEqual(-projected, cubic)

    def test_normalized_vertex_current_and_rescalings(self):
        q, k, h, g, a, b, integral, c = sp.symbols("q k h g a b integral c", positive=True)
        y2, e2 = normalized_squared(q, k, h, g, a, b, integral, c, 1 / c)
        expected = 2 * a * b / integral ** 2
        self.assertEqual(sp.cancel(y2 / e2 - expected), 0)
        wrong_y2, _ = normalized_squared(q, k, h, g, a, b, integral, c, 1 / c,
                                         connection_weight=1)
        self.assertNotEqual(sp.cancel(wrong_y2 / e2 - expected), 0)

        base = (5, 1, 30, Q(7, 3), 1, Q(9, 2), 2, 4, Q(1, 4))
        reference_y2, reference_e2 = normalized_squared(*base)
        trace_scale = 7
        trace_and_action = (5, trace_scale, 30 * trace_scale, Q(7, 3) * trace_scale,
                            1, Q(9, 2), 2, 4, Q(1, 4))
        self.assertEqual(normalized_squared(*trace_and_action), (reference_y2, reference_e2))
        scale = 3
        rescaled_metric = (5, 1, 30, Q(7, 3), 1, Q(9, 2) * scale ** 2,
                           2 * scale, 4, Q(1, 4))
        ys, es = normalized_squared(*rescaled_metric)
        self.assertEqual(sp.cancel(ys / es), sp.cancel(reference_y2 / reference_e2))

        # Direct frame changes act on the raw cubic and all three Grams together.
        lam, p = 3 + 4 * I, 1 + I
        factors = (sp.conjugate(lam), p, lam / p)
        cubic_factor = sp.prod(factors)
        gram_factor = sp.prod(sp.conjugate(x) * x for x in factors)
        self.assertEqual(sp.simplify(cubic_factor * sp.conjugate(cubic_factor) / gram_factor), 1)
        self.assertNotEqual(sp.simplify(1 / gram_factor), 1)  # Frozen cubic with moved mode frames.
        # Changing omega changes A_omega by |lambda|^2 and I_omega by |lambda|.
        yf, ef = normalized_squared(5, 1, 30, Q(7, 3), 25, Q(9, 2), 10,
                                    4 * Q(2, 5), Q(1, 4) * Q(5, 2))
        self.assertEqual((yf, ef), (reference_y2, reference_e2))

    def test_shape_inequality_exact_metric_controls(self):
        x = sp.Symbol("x", real=True)
        for omega in (sp.Integer(2), 2 + sp.cos(2 * sp.pi * x)):
            area = sp.integrate(omega ** 2, (x, 0, 1))
            mixed = sp.integrate(omega, (x, 0, 1))
            gap = sp.simplify(area - mixed ** 2)
            y2, e2 = normalized_squared(5, 1, 30, Q(7, 3), 1, area, mixed, 1, 1)
            self.assertEqual(sp.cancel(y2 / e2 - 2 * area / mixed ** 2), 0)
            self.assertGreaterEqual(gap, 0)
            if omega.is_Integer:
                self.assertEqual(gap, 0)
                self.assertEqual(sp.cancel(y2 / e2), 2)
            else:
                self.assertGreater(gap, 0)
                self.assertEqual(sp.cancel(y2 / e2), Q(9, 4))

    def test_slot_rank_and_illicit_form_entry(self):
        x1, x2, y1, y2, z = sp.symbols("x1 x2 y1 y2 z")
        coefficient = sp.Matrix([[0, 0, x1], [0, 0, x2], [y1, y2, z]])
        self.assertEqual(coefficient.det(), 0)
        self.assertEqual(coefficient.rank(), 2)
        leading = matrix_unit(3, 0, 2) + matrix_unit(3, 2, 0)
        self.assertEqual(leading.rank(), 2)
        self.assertEqual((leading + matrix_unit(3, 1, 1)).rank(), 3)
        self.assertEqual(leading * sp.Matrix([0, 1, 0]), sp.zeros(3, 1))

    def test_full_complement_response_and_backreaction(self):
        t = sp.Symbol("t", real=True)
        leading = matrix_unit(3, 0, 2) + matrix_unit(3, 2, 0)
        second = 4 * matrix_unit(3, 1, 1)
        b = sp.Matrix([0, 2, 0])
        c = sp.Matrix([[0, 5, 0]])
        d = 3 + 7 * t
        full = (t * leading + t ** 2 * second).row_join(t * b)
        full = full.col_join((t * c).row_join(sp.Matrix([[d]])))
        z1, z2, z3 = sp.symbols("z1 z2 z3")
        retained = sp.Matrix([z1, z2, z3])
        heavy = -(t * c * retained)[0] / d
        reconstructed = retained.col_join(sp.Matrix([heavy]))
        actual_equations = reduced(full * reconstructed)
        self.assertEqual(actual_equations[-1], 0)
        reduced_map = t * leading + t ** 2 * second - t ** 2 * b * c / d
        self.assert_matrix_equal(actual_equations[:3, :], reduced_map * retained)
        coefficient2 = reduced(reduced_map.diff(t, 2).subs(t, 0) / 2)
        self.assert_matrix_equal(coefficient2, second - b * c / 3)
        null = sp.Matrix([0, 1, 0])
        m2 = (null.T * coefficient2 * null)[0]
        self.assertEqual(m2, Q(2, 3))
        self.assertNotEqual(m2, (null.T * second * null)[0])
        self.assertNotEqual(m2, (-null.T * b * c * null / 3)[0])

        # Independent physical squared-mass equation for the coupled 2x2 block.
        mass_block = full.extract([1, 3], [1, 3])
        squared = mass_block.T * mass_block
        lam = sp.Symbol("lam")
        characteristic = squared.charpoly(lam).as_expr()
        leading_light = sp.expand(characteristic.subs(lam, m2 ** 2 * t ** 4)).coeff(t, 4)
        self.assertEqual(leading_light, 0)
        wrong_light = sp.expand(characteristic.subs(lam, 16 * t ** 4)).coeff(t, 4)
        self.assertNotEqual(wrong_light, 0)

        right_reconstruction = sp.eye(3).col_join(-t * c / d)
        left_reconstruction = sp.eye(3).col_join(-t * b.T / d)
        right_norm = reduced(right_reconstruction.T * right_reconstruction)
        left_norm = reduced(left_reconstruction.T * left_reconstruction)
        self.assert_matrix_equal(right_norm, sp.eye(3) + t ** 2 * c.T * c / d ** 2)
        self.assert_matrix_equal(left_norm, sp.eye(3) + t ** 2 * b * b.T / d ** 2)
        self.assertGreater((right_norm[1, 1] - 1).subs(t, Q(1, 10)), 0)
        self.assertGreater((left_norm[1, 1] - 1).subs(t, Q(1, 10)), 0)

    def test_complex_bilinear_gram_and_current_transport(self):
        sl = sp.Matrix([[2, I], [-I, 2]])
        sr = sp.Matrix([[3, 1 + I], [1 - I, 3]])
        for square_root in (sl, sr):
            self.assertEqual(square_root.H, square_root)
            self.assertGreater(square_root[0, 0], 0)
            self.assertGreater(square_root.det(), 0)
        gl, gr = sl ** 2, sr ** 2
        y = sp.Matrix([[1, I], [2, 3 - I]])
        canonical = sl.inv().T * y * sr.inv() / 3
        self.assert_matrix_equal(sl.T * canonical * sr * 3, y)
        self.assert_matrix_differs(sl.inv().H * y * sr.inv() / 3, canonical)
        z = sp.Matrix([1 + I, 2 - I])
        raw = sl.inv() * z
        self.assertEqual(sp.simplify((raw.H * gl * raw)[0]), (z.H * z)[0])
        zr = sp.Matrix([2 + I, 1 - 2 * I])
        raw_right = sr.inv() * zr
        self.assertEqual(sp.simplify((raw_right.H * gr * raw_right)[0]), (zr.H * zr)[0])
        self.assertEqual(sp.simplify((z.T * canonical * zr)[0]
                                     - (raw.T * y * raw_right)[0] / 3), 0)

        charge = sp.diag(2, -1)
        representation = sl.inv() * charge * sl
        current = gl * representation
        self.assert_matrix_equal(current, current.H)
        self.assert_matrix_equal(sl.inv() * current * sl.inv(), charge)
        self.assert_matrix_differs(current, representation)
        frame = sp.Matrix([[1, 1 + I], [0, 2]])
        moved_gram = frame.H * gl * frame
        moved_representation = frame.inv() * representation * frame
        self.assert_matrix_equal(moved_gram * moved_representation, frame.H * current * frame)
        self.assert_matrix_differs(gl * moved_representation, frame.H * current * frame)

        b, u, ubar, du, dubar = sp.symbols("b u ubar du dubar")
        norm, q = Q(11, 7), 5
        kinetic = sp.expand(norm * (dubar + I * q * b * ubar) * (du - I * q * b * u))
        current_coefficient = kinetic.coeff(b, 1)
        self.assertEqual(sp.expand(current_coefficient - I * q * norm * (ubar * du - dubar * u)), 0)
        self.assertNotEqual(sp.expand(current_coefficient - I * q * (ubar * du - dubar * u)), 0)
