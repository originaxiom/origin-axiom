"""UNRUN radial-flow controls. Do not import or collect before admission.

Design committed at 706280a20 before this implementation. These exact
finite controls do not certify global PDEs, a physical parent or SM3.
No scientific producer, saved output or observed parameter is loaded.
"""
import unittest
import sympy as s


def comm(a, b):
    return a * b - b * a


def zero(value):
    entries = list(value) if isinstance(value, s.MatrixBase) else [value]
    return all(s.simplify(s.expand(x)) == 0 for x in entries)


def complex_traceless(prefix):
    a, b, c, d, e, f = s.symbols(prefix + "0:6", real=True)
    return s.Matrix([[a + s.I*b, c + s.I*d],
                     [e + s.I*f, -a - s.I*b]])


def hermitian_traceless(prefix):
    a, b, c = s.symbols(prefix + "0:3", real=True)
    return s.Matrix([[a, b + s.I*c], [b - s.I*c, -a]])


def profiles(prefix, y, hermitian=False):
    n = 3 if hermitian else 6
    z = [s.Function(prefix + str(i), real=True)(y) for i in range(n)]
    if hermitian:
        return s.Matrix([[z[0], z[1] + s.I*z[2]],
                         [z[1] - s.I*z[2], -z[0]]])
    return s.Matrix([[z[0] + s.I*z[1], z[2] + s.I*z[3]],
                     [z[4] + s.I*z[5], -z[0] - s.I*z[1]]])


def flow(h, e, g):
    return (h - comm(e, e.H) - comm(g, g.H),
            e/2 - comm(h, e)/4, g/2 - comm(h, g)/4)


def potential(h, e, g, matter_weight=2):
    return (s.trace(h*h)/2 - s.trace(h*(comm(e, e.H) + comm(g, g.H)))
            + matter_weight*s.trace(e.H*e + g.H*g))


def triple(dimension):
    h = s.diag(*[2*n - (dimension-1) for n in range(dimension)])
    e = s.zeros(dimension)
    for n in range(dimension-1):
        e[n+1, n] = s.sqrt((n+1)*(dimension-1-n))
    return h, e


def rotating_control(t):
    rotation = s.Matrix([[1-t*t, -2*t], [2*t, 1-t*t]])/(1+t*t)
    omega = 2/(1+t*t)
    generator = s.Matrix([[0, -omega], [omega, 0]])
    mass = rotation*s.Matrix([[1, -omega], [-omega, -1]])*rotation.T
    projector = rotation*s.diag(1, 0)*rotation.T
    return rotation, generator, mass, projector


class RadialFlowChecks(unittest.TestCase):
    def assertZero(self, value):
        self.assertTrue(zero(value), str(value))

    def test_coordinate_residuals_and_opposite_orientation_control(self):
        y = s.symbols("y", positive=True)
        h, e, g = profiles("h", y, True), profiles("e", y), profiles("g", y)
        ax, q, r = -h/(4*y), e/(2*s.sqrt(y)), g/(2*s.sqrt(y))
        for field, profile in ((q, e), (r, g)):
            actual = s.I*field.diff(y) - s.I*comm(ax, field)
            expected = s.I*(4*y*profile.diff(y)-2*profile+comm(h, profile))/(8*y**s.Rational(3, 2))
            self.assertZero(actual-expected)
        curvature = -ax.diff(y)
        self.assertZero(curvature-(y*h.diff(y)-h)/(4*y*y))
        self.assertFalse(zero(ax.diff(y)-curvature))
        moment = curvature + (comm(q, q.H)+comm(r, r.H))/y
        self.assertZero(4*y*y*moment - (y*h.diff(y)-h+comm(e, e.H)+comm(g, g.H)))

    def test_flow_preserves_commuting_constraint_reality_and_parities(self):
        h, e, g = hermitian_traceless("h"), complex_traceless("e"), complex_traceless("g")
        hd, ed, gd = flow(h, e, g)
        actual = comm(ed, g)+comm(e, gd)
        expected = comm(e, g)-comm(h, comm(e, g))/4
        self.assertZero(actual-expected)
        wrong_ed = e/2-comm(h, e)/2
        self.assertFalse(zero(comm(wrong_ed, g)+comm(e, gd)-expected))
        self.assertZero(hd-hd.H)
        for field in (hd, ed, gd):
            self.assertZero(s.trace(field))
        a, b, c, d, f = s.symbols("a b c d f", real=True)
        hp = s.diag(a, -a)
        ep = s.Matrix([[0, b+s.I*c], [d+s.I*f, 0]])
        gp = s.Matrix([[0, 1+s.I], [2-s.I, 0]])
        p = s.diag(1, -1)
        hdp, edp, gdp = flow(hp, ep, gp)
        self.assertZero(p*hdp*p-hdp)
        self.assertZero(p*edp*p+edp)
        self.assertZero(p*gdp*p+gdp)

    def test_trace_monotone_by_directional_differentiation_and_wrong_weight(self):
        h, e, g = hermitian_traceless("h"), complex_traceless("e"), complex_traceless("g")
        hd, ed, gd = flow(h, e, g)
        step = s.symbols("step", real=True)
        actual = s.diff(potential(h+step*hd, e+step*ed, g+step*gd), step).subs(step, 0)
        expected = s.trace(hd.H*hd)+8*s.trace(ed.H*ed+gd.H*gd)
        self.assertZero(actual-expected)
        hz, ez, gz = s.zeros(2), s.Matrix([[0, 1], [0, 0]]), s.zeros(2)
        dh, de, dg = flow(hz, ez, gz)
        wrong = s.diff(potential(hz+step*dh, ez+step*de, gz+step*dg, 1), step).subs(step, 0)
        norm = s.trace(dh.H*dh)+8*s.trace(de.H*de+dg.H*dg)
        self.assertFalse(zero(wrong-norm))

    def test_old_triples_and_two_field_fixed_points(self):
        for n in (2, 5):
            h, e = triple(n)
            self.assertZero(comm(h, e)-2*e)
            self.assertZero(comm(e, e.H)-h)
            for residual in flow(h, e, s.zeros(n)):
                self.assertZero(residual)
            self.assertFalse(zero(flow(h, e/2, s.zeros(n))[0]))
        h = s.diag(s.Rational(2, 3), s.Rational(2, 3), -s.Rational(4, 3))
        e, g = s.zeros(3), s.zeros(3)
        e[0, 2], g[1, 2] = s.sqrt(s.Rational(2, 3)), s.sqrt(s.Rational(2, 3))
        self.assertZero(comm(e, g))
        for residual in flow(h, e, g):
            self.assertZero(residual)
        self.assertEqual(s.Matrix.hstack(s.Matrix(list(e)), s.Matrix(list(g))).rank(), 2)
        self.assertFalse(zero(comm(e, g.H)))
        for residual in flow(s.zeros(2), s.zeros(2), s.zeros(2)):
            self.assertZero(residual)

    def test_scalar_reduction_and_linearized_stable_unstable_directions(self):
        h, f = s.symbols("h f", real=True)
        for n in (2, 5):
            h0, e0 = triple(n)
            hd, ed, gd = flow(h*h0, f*e0, s.zeros(n))
            self.assertZero(hd-(h-f*f)*h0)
            self.assertZero(ed-(1-h)*f*e0/2)
            self.assertZero(gd)
        vector = s.Matrix([h-f*f, (1-h)*f/2])
        jacobian = vector.jacobian((h, f)).subs({h: 1, f: 1})
        self.assertEqual(jacobian, s.Matrix([[1, -2], [-s.Rational(1, 2), 0]]))
        lam = s.symbols("lam")
        self.assertZero(jacobian.charpoly(lam).as_expr()-(lam*lam-lam-1))
        stable, unstable = (1-s.sqrt(5))/2, (1+s.sqrt(5))/2
        self.assertTrue((-stable).is_positive)
        self.assertTrue(unstable.is_positive)
        for eigenvalue in (stable, unstable):
            self.assertZero((jacobian-eigenvalue*s.eye(2)).det())
        eta, xi = s.symbols("eta xi", real=True)
        self.assertZero(vector.subs({h: 1+eta, f: 1+xi})-jacobian*s.Matrix([eta, xi])
                        -s.Matrix([-xi*xi, -eta*xi/2]))

    def test_kinetic_rescalings_and_nonconstant_complex_identity(self):
        y = s.symbols("y", positive=True)
        m = s.symbols("m", real=True)
        hy, uy = s.Function("hy")(y), s.Function("uy")(y)
        gauge = s.sqrt(y)*(s.diff(s.sqrt(y)*uy, y)+hy*m*s.sqrt(y)*uy/(2*y))
        spin = y*(s.diff(uy, y)+hy*(m+1)*uy/(2*y))
        self.assertZero(gauge-y*uy.diff(y)-(s.Rational(1, 2)+hy*m/2)*uy)
        self.assertZero(spin-y*uy.diff(y)-hy*(m+1)*uy/2)
        t = s.symbols("t", real=True)
        h, f, u = s.Function("h")(t), s.Function("f")(t), s.Function("u")(t)
        k0 = s.symbols("k0", real=True)
        a, b, k = s.Rational(1, 2)+h*m/2, h*(m+1)/2, f*k0
        first, second = u.diff(t)+a*u, -k*u
        composite = k*first+second.diff(t)+b*second
        equation = {f.diff(t): (1-h)*f/2}
        self.assertZero(composite.subs(equation))
        wrong = (k*first+second.diff(t)+a*second).subs(equation)
        self.assertFalse(zero(wrong))
        self.assertZero((k.diff(t)-(a-b)*k).subs(equation))

    def test_operator_square_keeps_derivative_and_trace(self):
        t = s.symbols("t", real=True)
        a, b, k = [s.Function(name, real=True)(t) for name in ("a", "b", "k")]
        mass, j = s.Matrix([[a, k], [k, -b]]), s.diag(1, -1)
        u = s.Matrix([s.Function("u0")(t), s.Function("u1")(t)])
        apply_b = lambda v: j*(v.diff(t)+mass*v)
        apply_bd = lambda v: -(j*v).diff(t)+mass*j*v
        self.assertZero(apply_bd(apply_b(u))-(-u.diff(t, 2)+(mass*mass-mass.diff(t))*u))
        self.assertZero(apply_b(apply_bd(u))-(-u.diff(t, 2)+j*(mass*mass+mass.diff(t))*j*u))
        h, f, m, k0 = s.symbols("h f m k0", real=True)
        physical = s.Matrix([[s.Rational(1, 2)+h*m/2, f*k0], [f*k0, -h*(m+1)/2]])
        self.assertZero(s.trace(physical)-(1-h)/2)
        comparator = s.diag(1+t, -2)
        control = s.Matrix([1, 1])
        correct = (comparator*comparator-comparator.diff(t))*control
        omitted = comparator*comparator*control
        self.assertFalse(zero(correct-omitted))
        self.assertFalse(zero(physical*physical-s.trace(physical*physical)*s.eye(2)/2))

    def test_both_scalar_extremes_and_constant_recovery(self):
        paired, upper, lower = 0, 0, 0
        for j in range(5):
            channels = 0
            for m in range(-j-1, j+1):
                if m % 2:
                    continue
                has_a, has_q = -j <= m <= j, -j <= m+1 <= j
                if not (has_a or has_q):
                    continue
                d = s.Rational(m+1, 2)
                if has_a and has_q:
                    k = s.sqrt(s.Rational((j-m)*(j+m+1), 2))
                    mass = s.Matrix([[d, k], [k, -d]])
                    self.assertZero(mass*mass-(d*d+k*k)*s.eye(2))
                    channels += 2
                    paired += 1
                elif has_a:
                    self.assertEqual(m, j)
                    self.assertEqual(d, s.Rational(j+1, 2))
                    channels += 1
                    upper += 1
                else:
                    self.assertEqual(m, -j-1)
                    k_lower = s.Rational(j, 2)
                    self.assertEqual(k_lower, -d)
                    self.assertEqual(k_lower*k_lower, d*d)
                    channels += 1
                    lower += 1
            self.assertEqual(channels, 2*j+1)
        self.assertGreater(paired, 0)
        self.assertGreater(upper, 0)
        self.assertGreater(lower, 0)

    def test_rotating_tail_transported_projector_not_instantaneous_sign(self):
        t = s.symbols("t", nonnegative=True)
        rotation, generator, mass, projector = rotating_control(t)
        identity = s.eye(2)
        self.assertZero(rotation.T*rotation-identity)
        self.assertZero(rotation.diff(t)-rotation*generator)
        self.assertZero(projector*projector-projector)
        self.assertZero(projector.diff(t)+(identity-projector)*mass*projector
                        +projector*mass*(identity-projector))
        for actual, expected in ((projector, s.diag(1, 0)), (mass, s.diag(1, -1))):
            limit = actual.applyfunc(lambda x: s.limit(x, t, s.oo))
            self.assertZero(limit-expected)
        self.assertFalse(zero((projector*mass-mass*projector).subs(t, 0)))
        omega = 2/(1+t*t)
        instantaneous = (identity+mass/s.sqrt(1+omega*omega))/2
        self.assertFalse(zero((projector-instantaneous).subs(t, 0)))
        wrong = instantaneous.diff(t)+(identity-instantaneous)*mass*instantaneous \
            +instantaneous*mass*(identity-instantaneous)
        self.assertFalse(zero(wrong.subs(t, 0)))

    def test_rotating_tail_both_slots_green_and_integrated_norm(self):
        t = s.symbols("t", nonnegative=True)
        rotation, _generator, mass, _projector = rotating_control(t)
        x, v = s.exp(-t)*rotation[:, 0], s.exp(-t)*rotation[:, 1]
        self.assertZero(x.diff(t)+mass*x)
        self.assertZero(v.diff(t)-mass*v)
        self.assertZero((x.H*v)[0])
        plane = s.zeros(4, 2)
        plane[:2, 0], plane[2:, 1] = x.subs(t, 0), v.subs(t, 0)
        green = s.BlockMatrix([[s.zeros(2), s.eye(2)], [s.eye(2), s.zeros(2)]]).as_explicit()
        self.assertEqual(plane.rank(), 2)
        self.assertZero(plane.H*green*plane)
        for profile in (x, v):
            squared_norm = s.simplify((profile.H*profile)[0])
            self.assertZero(squared_norm-s.exp(-2*t))
            self.assertEqual(s.integrate(squared_norm, (t, 0, s.oo)), s.Rational(1, 2))
        self.assertZero(mass.subs(t, 0)**2-5*s.eye(2))
        self.assertNotEqual(s.Rational(1, 2), 1/(2*s.sqrt(5)))
