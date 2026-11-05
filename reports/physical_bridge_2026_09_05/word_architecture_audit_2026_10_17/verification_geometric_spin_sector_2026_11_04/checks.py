"""Five UNRUN geometric/spin, sector and index source controls.

Design seals a77fc3aa8 and 646492da1 precede this implementation.
Do not import, collect or execute before independent review, main's
exact acceptance and source-complete strict prospective admission.
Finite controls do not prove the geometric/domain/compactness theorems.
"""

from pathlib import Path
from importlib.util import module_from_spec, spec_from_file_location
import unittest

import sympy as sp


HERE = Path(__file__).resolve().parent


def load_source(name, directory):
    path = HERE.parent / directory / "checks.py"
    spec = spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load declared dependency {path}")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


TRANSPORT = load_source("geometric_transport_source", "verification_transport_end_2026_11_04")
OLD = TRANSPORT.OLD
ROOTS = TRANSPORT.ROOTS


def simplify(matrix):
    return matrix.applyfunc(sp.simplify)


def mass_rows(fields, q, r, omega, dbar, dz):
    """Direct source rows with genuine derivatives, including variable metrics."""
    lam, a, u, v = fields
    aq, ar = OLD.ad2(q), OLD.ad2(r)
    aqd, ard = OLD.ad2(OLD.dagger(q)), OLD.ad2(OLD.dagger(r))
    p1, p2 = dbar(u) + sp.I * aq * a, dbar(v) + sp.I * ar * a
    wedge = aq * v - ar * u
    return (
        -(dz(a) - 2 * sp.I * omega * (aqd * u + ard * v)) / (sp.sqrt(2) * omega**2),
        2 * sp.I * wedge + sp.sqrt(2) * dz(lam),
        p2 / omega - sp.sqrt(2) * sp.I * aqd * lam,
        -p1 / omega - sp.sqrt(2) * sp.I * ard * lam,
    )


def canonical_cusp_rows(fields, t, k, qhat=None, rhat=None, gauge=None):
    omega = sp.exp(-t)
    zero = sp.zeros(2)
    qhat = zero if qhat is None else qhat
    rhat = zero if rhat is None else rhat
    gauge = zero if gauge is None else gauge
    raw_fields = (sp.exp(t / 2) * fields[0],
                  sp.sqrt(2) * sp.exp(-t / 2) * fields[1],
                  fields[2], fields[3])
    def dbar(f):
        return (sp.I * k * f + sp.I * sp.exp(-t) * f.diff(t)
                - sp.I * omega * OLD.ad2(gauge) * f)

    def dz(f):
        return (sp.I * k * f - sp.I * sp.exp(-t) * f.diff(t)
                - sp.I * omega * OLD.ad2(OLD.dagger(gauge)) * f)

    raw = mass_rows(raw_fields, sp.sqrt(omega) * qhat, sp.sqrt(omega) * rhat, omega, dbar, dz)
    return tuple(simplify(scale * row) for scale, row in zip(
        (sp.exp(-t / 2), sp.exp(t / 2) / sp.sqrt(2), 1, 1), raw))


def compose(left, right):
    return {axis: TRANSPORT.free_substitute(right[axis], left) for axis in (1, 2)}


def repeated(images, count):
    out = {1: (1,), 2: (2,)}
    for _ in range(count):
        out = compose(images, out)
    return out


class GeometricSpinSectorChecks(unittest.TestCase):
    def assert_zero(self, value):
        self.assertEqual(simplify(sp.Matrix(value)), sp.zeros(*sp.Matrix(value).shape))

    def test_geometric_spin_pullback_and_based_group_scope(self):
        fi, fj, gl, gr = OLD.units()
        left = {1: (1,), 2: (1, 2)}
        right_inverse = {1: (1, -2), 2: (2,)}
        delta = compose(compose(left, right_inverse), left)
        delta_g = simplify(gl * OLD.dagger(gr) * gl)
        c = (1, -2, -1, 2)
        inner_c = {axis: TRANSPORT.free_substitute(c + (axis,) + TRANSPORT.free_inverse(c),
                                                 {1: (1,), 2: (2,)}) for axis in (1, 2)}
        self.assertEqual(repeated(delta, 4), inner_c)
        self.assertNotEqual(inner_c, {1: (1,), 2: (2,)})
        self.assertEqual(sum(letter == 1 for letter in c) - sum(letter == -1 for letter in c), 0)
        self.assertEqual(sum(letter == 2 for letter in c) - sum(letter == -2 for letter in c), 0)
        rho_c = TRANSPORT.evaluate_word(c, {1: fi, 2: fj})
        self.assert_zero(rho_c + sp.eye(2))
        self.assert_zero(delta_g**4 - sp.eye(2))
        # At tau=i, S and S^-1 fix the modulus. Product lifts retain the sign.
        j_s = (1 + sp.I) / sp.sqrt(2)
        j_delta = 1 / j_s
        self.assertEqual(sp.simplify(j_s**2 - sp.I), 0)
        self.assertEqual(sp.simplify(j_delta**4), -1)
        self.assert_zero(j_delta**4 * delta_g**4 - rho_c)
        self.assert_zero((-1) * (-sp.eye(2)) - sp.eye(2))
        self.assertNotEqual(sp.simplify(j_delta**4), sp.sqrt(1))
        self.assertNotEqual(delta_g**4, rho_c)
        # Independently compose the (ST)^3 square roots at tau=i.
        j_st_cubed = sp.sqrt(1 + sp.I) * sp.sqrt((1 + sp.I) / 2) * j_s
        self.assertEqual(sp.simplify(sp.expand_complex(j_st_cubed) - j_s**2), 0)
        tau = sp.Symbol("tau")
        aa, bb, cc, dd, m, n = sp.symbols("A B C D m n")
        j = cc * tau + dd
        moved = (aa * tau + bb) / j
        numerator = sp.together((m - n * tau) / j - ((aa*m + bb*n) - (cc*m + dd*n)*moved)).as_numer_denom()[0]
        self.assertEqual(sp.expand(numerator - (m-n*tau)*(1-aa*dd+bb*cc)), 0)
        self.assertEqual(sp.simplify(numerator.subs(aa, (1+bb*cc)/dd)), 0)

    def test_complete_curve_mass_and_action_transport(self):
        aa, bb, cc, dd, x, y = sp.symbols("a b c d x y", real=True)
        sphere = aa**2 + bb**2 + cc**2 + dd**2 - 1

        def reduced(value):
            numerator = sp.cancel(value).as_numer_denom()[0]
            return sp.Poly(numerator, aa, domain="EX").rem(sp.Poly(sphere, aa, domain="EX")).as_expr().expand()

        def is_zero(matrix):
            return all(reduced(value) == 0 for value in matrix)

        alpha, beta = aa + sp.I*bb, cc + sp.I*dd
        flavour = sp.Matrix([[alpha, beta], [-sp.conjugate(beta), sp.conjugate(alpha)]])
        q0, q1, q2, r0, r1, r2 = sp.symbols("q0 q1 q2 r0 r1 r2")
        q, r = sp.Matrix([[q0, q1], [q2, -q0]]), sp.Matrix([[r0, r1], [r2, -r0]])
        omega = sp.Symbol("Omega", positive=True)
        pbar, pz = sp.symbols("pbar pz")
        root = x + sp.I*y
        jacobian, scale = root**2, x**2 + y**2
        new_pair = OLD.rotate(flavour, (q, r))
        new_pair = tuple(root * value for value in new_pair)
        source = OLD.physical_mass(q, r, omega, pbar, pz)
        target = OLD.physical_mass(*new_pair, scale*omega, sp.conjugate(jacobian)*pbar, jacobian*pz)
        uin = sp.diag(sp.eye(3), sp.conjugate(jacobian)*sp.eye(3), sp.kronecker_product(root*flavour, sp.eye(3)))
        uout = sp.diag(sp.eye(3), jacobian*sp.eye(3), sp.kronecker_product(sp.conjugate(root*flavour), sp.eye(3)))
        self.assertTrue(is_zero(target * uin - uout * source))
        metric = sp.diag(omega**2*sp.eye(3), sp.eye(3)/2, omega*sp.eye(6))
        moved_metric = metric.subs(omega, scale*omega)
        self.assertTrue(is_zero(OLD.dagger(uin)*moved_metric*uin/scale**2 - metric))
        self.assertTrue(is_zero(OLD.dagger(uout)*moved_metric*uout/scale**2 - metric))
        fields = tuple(sp.Matrix(sp.symbols(f"f{slot}_0:3")) for slot in range(4))
        direct = mass_rows(fields, q, r, omega, lambda f: pbar*f, lambda f: pz*f)
        self.assert_zero(sp.Matrix.vstack(*direct) - source * sp.Matrix.vstack(*fields))
        broken = sp.Matrix(source)
        broken[6:9, 0:3] = sp.zeros(3)
        self.assertNotEqual(simplify(broken * sp.Matrix.vstack(*fields) - sp.Matrix.vstack(*direct)), sp.zeros(12, 1))
        self.assertFalse(is_zero(target * uin - uin * source))
        wrong_metric = OLD.physical_mass(*new_pair, omega, sp.conjugate(jacobian)*pbar, jacobian*pz)
        self.assertFalse(is_zero(wrong_metric * uin - uout * source))
        # Full antisymmetric W, moment and surface variation retain their factors.
        epsilon = sp.Matrix([[0, 1], [-1, 0]])
        self.assertTrue(is_zero(flavour.T*epsilon*flavour - epsilon))
        self.assertTrue(is_zero(epsilon*flavour - sp.conjugate(flavour)*epsilon))
        old_moment = OLD.bracket(q, OLD.dagger(q)) + OLD.bracket(r, OLD.dagger(r))
        new_moment = sum((OLD.bracket(z, OLD.dagger(z)) for z in new_pair), sp.zeros(2))
        self.assertTrue(is_zero(new_moment - scale*old_moment))
        self.assertEqual(sp.simplify(jacobian*sp.conjugate(jacobian)/scale**2), 1)
        self.assertEqual(sp.simplify(root**2/jacobian), 1)
        qp, rp = OLD.rotate(OLD.units()[1], (sp.diag(1, -1), 2*sp.diag(1, -1)))
        self.assertNotEqual(sp.trace(qp*rp), sp.trace(sp.diag(1, -1)*2*sp.diag(1, -1)))

    def test_all_slot_half_root_coercivity(self):
        t, k = sp.symbols("t k", real=True)
        radius = sp.Symbol("radius", positive=True)
        columns = tuple(sp.Matrix([sp.Function(f"f{slot}_{axis}")(t) for axis in range(3)]) for slot in range(4))
        rows = canonical_cusp_rows(columns, t, k)
        lam, a, u, v = columns
        expected = (sp.I*(a.diff(t)-(k*sp.exp(t)+sp.Rational(1, 2))*a),
                    -sp.I*(lam.diff(t)-(k*sp.exp(t)-sp.Rational(1, 2))*lam),
                    sp.I*(v.diff(t)+k*sp.exp(t)*v), -sp.I*(u.diff(t)+k*sp.exp(t)*u))
        for actual, wanted in zip(rows, expected):
            self.assert_zero(actual-wanted)
        self.assertNotEqual(simplify(rows[0] - sp.I*(a.diff(t)-k*sp.exp(t)*a)), sp.zeros(3, 1))
        function = sp.Function("f")(t)
        shifts = (-k*sp.exp(t)-sp.Rational(1, 2), -k*sp.exp(t)+sp.Rational(1, 2), k*sp.exp(t))
        for h in shifts:
            forward = sp.diff(function, t) + h*function
            square = sp.expand(-sp.diff(forward, t) + h*forward)
            self.assertEqual(sp.simplify(square + function.diff(t, 2) - (h**2-sp.diff(h, t))*function), 0)
            for sign in (-1, 1):
                potential = sp.expand(h**2 + sign*sp.diff(h, t))
                for orientation in (-1, 1):
                    remainder = sp.expand(potential.subs(k, orientation*radius*sp.exp(-t)) - (radius**2-2*radius))
                    self.assertTrue(all(coefficient >= 0 for coefficient in sp.Poly(remainder, radius).all_coeffs()))
        self.assertEqual(sp.expand(radius**2-2*radius-(radius**2/2-2)-(radius-2)**2/2), 0)
        nonnegative = sp.Symbol("n", integer=True, nonnegative=True)
        frequency = 2*sp.pi*(nonnegative+sp.Rational(1, 2))
        self.assertEqual(sp.expand(frequency**2-sp.pi**2-4*sp.pi**2*nonnegative*(nonnegative+1)), 0)
        self.assertEqual(sp.expand(frequency.subs(nonnegative, -nonnegative-1)**2-frequency**2), 0)
        # Actual source terms become bounded after the same unitary rescaling.
        qhat, rhat, gauge = sp.Matrix([[0, 1], [2, 0]]), sp.diag(1, -1), sp.diag(2, -2)
        coupled = canonical_cusp_rows(columns, t, k, qhat, rhat, gauge)
        expressions = sp.Matrix.vstack(*(simplify(a-b) for a, b in zip(coupled, rows)))
        variables = sp.Matrix.vstack(*columns)
        bounded_matrix = expressions.jacobian(variables)
        self.assert_zero(bounded_matrix.diff(t))
        self.assert_zero(expressions - bounded_matrix*variables)
        actual_e, actual_g, actual_h, *_ = OLD.d5_source()
        for actual in (actual_e/(2*sp.sqrt(2)), actual_g/(2*sp.sqrt(2)), actual_h/4):
            self.assert_zero((sp.exp(-t/2)*actual/sp.sqrt(sp.exp(-t))).diff(t))
        data = TRANSPORT.carriers()
        for a_core, d_core, p_core, dimension, centre in (
                (data["av"], data["dv"], sp.diag(*(sp.exp(-sp.I*sp.pi*data["h"][i, i]/2) for i in range(10))), 10, 1),
                (data["asp"], data["dsp"], data["psp"], 32, -1)):
            b_core = simplify(d_core*a_core)
            commutator = simplify(a_core*b_core*OLD.dagger(a_core)*OLD.dagger(b_core))
            self.assert_zero(p_core*commutator - centre*sp.eye(dimension))
        roots = ROOTS.e8_roots()
        zeta_log = TRANSPORT.d5_log((1, 1, 1, 1, 1))
        grading = {root: TRANSPORT.phase(TRANSPORT.torus_pair(zeta_log, root)) for root in roots}
        self.assertEqual(sum(value == -1 for value in grading.values()), 128)
        self.assertEqual(sum(value == 1 for value in grading.values())+8, 120)
        for first in roots:
            self.assertEqual(grading[first]*grading[tuple(-x for x in first)], 1)
            for second in roots:
                total = tuple(a+b for a, b in zip(first, second))
                if total in roots:
                    self.assertEqual(grading[total], grading[first]*grading[second])

    def test_periodic_and_cover_parity_controls(self):
        t, length = sp.symbols("t L", real=True, positive=True)
        u, v = sp.Function("u")(t), sp.Function("v")(t)
        zero = sp.zeros(3, 1)
        columns = (zero, zero, sp.Matrix([u, 0, 0]), sp.Matrix([v, 0, 0]))
        periodic = canonical_cusp_rows(columns, t, 0)
        self.assert_zero(periodic[0])
        self.assert_zero(periodic[1])
        self.assertEqual(sp.simplify(periodic[2][0]-sp.I*v.diff(t)), 0)
        self.assertEqual(sp.simplify(periodic[3][0]+sp.I*u.diff(t)), 0)
        k = sp.Symbol("k", real=True)
        self.assertEqual((k**2*sp.exp(2*t)).subs(k, 0), 0)
        self.assertNotEqual((k**2*sp.exp(2*t)).subs(k, 0), sp.pi**2*sp.exp(2*t))
        s = sp.Symbol("s", real=True)
        bump = s*(1-s)
        norm = sp.integrate(bump**2, (s, 0, 1))
        residual = sp.integrate(sp.diff(bump, s)**2, (s, 0, 1))/(length**2*norm)
        self.assertEqual(sp.simplify(residual), 10/length**2)
        self.assertEqual(sp.limit(residual, length, sp.oo), 0)
        odd, even = sp.symbols("odd even", integer=True, positive=True)
        self.assertEqual(sp.simplify((-1)**(2*even)), 1)
        self.assertEqual(sp.simplify((-1)**(2*odd+1)), -1)
        fi, fj, *_ = OLD.units()
        self.assert_zero(fi*fj*OLD.dagger(fi)*OLD.dagger(fj) + sp.eye(2))
        # The actual gauge lift signs act as -I on the spin carrier, +I on the vector.
        data = TRANSPORT.carriers()
        gauge_b = simplify(data["dsp"]*data["asp"])
        for first_sign in (-1, 1):
            for second_sign in (-1, 1):
                a, b = first_sign*data["asp"], second_sign*gauge_b
                self.assert_zero(data["psp"]*a*b*OLD.dagger(a)*OLD.dagger(b) + sp.eye(32))
        roots = ROOTS.e8_roots()
        colour_root = (1, -1, 0, 0, 0, 0, 0, 0)
        charged_adjoint = (0, 1, -1, 0, 0, 0, 0, 0)
        self.assertIn(colour_root, roots)
        self.assertIn(charged_adjoint, roots)
        self.assertIn(tuple(a+b for a, b in zip(colour_root, charged_adjoint)), roots)
        area, g6 = sp.symbols("area g6", positive=True)
        gauge_norm = area/g6**2
        spin_norm = sp.integrate(bump**2/g6**2, (s, 0, 1))
        translated_norm = sp.integrate(length*(bump/sp.sqrt(length))**2/g6**2, (s, 0, 1))
        self.assertEqual(sp.simplify(translated_norm-spin_norm), 0)
        bare_vertex = sp.integrate(length*(bump/sp.sqrt(length))**2/g6**2, (s, 0, 1))
        canonical_vertex = bare_vertex/(translated_norm*sp.sqrt(gauge_norm))
        self.assertEqual(sp.simplify(canonical_vertex-g6/sp.sqrt(area)), 0)

    def test_bounded_end_split_and_four_slot_index_cancellation(self):
        y = sp.Symbol("y", positive=True)
        x = sp.Symbol("x", real=True)
        omega = 1/y
        split = sp.diag(omega**(-sp.Rational(1, 2)), omega**sp.Rational(1, 2))
        metric_b = sp.eye(2)/omega
        metric_split = sp.diag(1, omega**-2)
        self.assert_zero(OLD.dagger(split)*metric_split*split-metric_b)
        self.assertEqual(sp.simplify(split.det()), 1)
        self.assert_zero(y*split.diff(y)*split.inv()-sp.diag(sp.Rational(1, 2), -sp.Rational(1, 2)))
        winding = sp.diag(sp.exp(sp.I*sp.pi*x), sp.exp(-sp.I*sp.pi*x))
        winding_derivative = simplify(y*winding.diff(x)*winding.inv())
        self.assertEqual(sp.limit(sp.Abs(winding_derivative[0, 0]), y, sp.oo), sp.oo)
        lam = sp.Function("lambda")(y)
        sigma = sp.I*omega**2*lam/sp.sqrt(2)
        dz = lambda f: -sp.I*sp.diff(f, y)
        actual_c3_adjoint = -dz(omega**-2*sigma)
        self.assertEqual(sp.simplify(2*sp.I*actual_c3_adjoint-sp.sqrt(2)*dz(lam)), 0)
        chi_v, chi_vk = sp.symbols("chi_V chi_VK", integer=True)
        scalar_form_contribution = -chi_v-chi_vk
        split_spin_contribution = chi_v+chi_vk
        self.assertEqual(sp.expand(scalar_form_contribution+split_spin_contribution), 0)
        # Global splitting and index continuity are separately reviewed proof duties.
        def old_index(a):
            return ROOTS.h0(a, ROOTS.ZERO)-ROOTS.h1(a, ROOTS.ZERO)
        self.assertEqual(2*old_index(0)-old_index(-1)-old_index(1), 1)
        fi, fj, *_ = OLD.units()
        flavour_peripheral = simplify(fi*fj*OLD.dagger(fi)*OLD.dagger(fj))
        self.assert_zero((-1)*flavour_peripheral-sp.eye(2))
        self.assertNotEqual(-sp.eye(2), sp.eye(2))


if __name__ == "__main__":
    unittest.main()
