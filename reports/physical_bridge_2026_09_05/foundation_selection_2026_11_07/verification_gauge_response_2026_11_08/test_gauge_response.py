"""Six exact scientific controls, implemented UNRUN; imports require admission."""
from fractions import Fraction as F
from itertools import product
import unittest

from gauge_response_exact import (
    cubic_factors, mode, normalized_power_integral, response_derivatives, static_shell,
)


def mm(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))


def mt(a):
    return tuple(zip(*a))


def ms(a, b):
    return tuple(tuple(x-y for x, y in zip(row, other)) for row, other in zip(a, b))


def ma(a, b):
    return tuple(tuple(x+y for x, y in zip(row, other)) for row, other in zip(a, b))


def scale(c, a):
    return tuple(tuple(c*x for x in row) for row in a)


def tr(a):
    return sum(a[i][i] for i in range(len(a)))


def comm(a, b):
    return ms(mm(a, b), mm(b, a))


def integral_at_one(power):
    """Independent elementary antiderivative on t>=1, with divergence guard."""
    power = F(power)
    if power >= -1:
        raise ValueError("Diverges at infinity")
    return -1/(power+1)


class GaugeResponseControls(unittest.TestCase):
    def test_01_weights_outward_flux_and_retained_moment_source(self):
        item = mode(3, ell2=F(5, 2), cut=F(7, 3))
        # Vary the original radial derivative quadratic at its lower endpoint.
        lower_flux_b = -(item.cut**2/item.ell2)*item.b_power/item.cut
        lower_flux_v = -item.v_power/item.cut
        self.assertEqual(lower_flux_b, item.response_b)
        self.assertEqual(lower_flux_v, item.response_v)
        self.assertNotEqual(-lower_flux_b, item.response_b)
        self.assertNotEqual(lower_flux_v, item.response_b)  # wrong common weight

        omega, z, f, step = F(3, 2), F(2, 3), F(1, 5), F(1, 7)
        h = ((1, 0), (0, -1))
        q = ((0, z), (0, 0))
        source = comm(q, mt(q))
        self.assertEqual(source, scale(z*z, h))

        def energy(curvature):
            mu = tuple(tuple(curvature*h[i][j]+omega*source[i][j]
                             for j in range(2)) for i in range(2))
            return tr(mm(mu, mu))/(2*omega**2)

        derivative = (energy(f+step)-energy(f-step))/(2*step)
        actual_mu = scale(f+omega*z*z, h)
        self.assertEqual(derivative, tr(mm(actual_mu, h))/omega**2)
        self.assertNotEqual(derivative, tr(mm(scale(f, h), h))/omega**2)

    def test_02_poisson_equations_and_both_norm_branches(self):
        for nu, ell2, cut in product((F(1), F(3, 2), F(3), F(5)),
                                     (F(1), F(5, 3)), (F(1), F(7, 2))):
            item = mode(nu, ell2, cut)
            rb, rv = item.b_power, item.v_power
            self.assertEqual(-rb*(rb+1)/ell2+item.s, 0)
            self.assertEqual(-rv*(rv-1)+ell2*item.s, 0)
            self.assertLess(2*rb, -1)        # scalar coefficient measure dy
            self.assertLess(2*rv-2, -1)      # vector coefficient measure ell^2 dy/y^2
            self.assertGreaterEqual(2*item.b_other, -1)
            self.assertGreaterEqual(2*item.v_other-2, -1)
        zero = mode(1)
        self.assertEqual(zero.v_power, 0)
        self.assertEqual(zero.b_other, 0)
        self.assertEqual(normalized_power_integral(0, 1, -2, 1), 1)
        with self.assertRaises(ValueError):
            normalized_power_integral(0, 1)  # constant connection shift
        with self.assertRaises(ValueError):
            normalized_power_integral(2*zero.v_power, 1)  # wrong flat vector norm
        for args in ((0, 1, 1), (1, 0, 1), (1, 1, 0)):
            with self.assertRaises(ValueError):
                mode(*args)

    def test_03_green_divided_differences_and_response_norms(self):
        ell2, cut = F(5, 2), F(7, 3)
        for nu in (F(1), F(3, 2), F(2), F(5)):
            item = mode(nu, ell2, cut)
            nb = cut*integral_at_one(2*item.b_power)
            nv = ell2/cut*integral_at_one(2*item.v_power-2)
            self.assertEqual(response_derivatives(item), (nb, nv))
            self.assertEqual(normalized_power_integral(2*item.b_power, cut), nb)
            self.assertEqual(normalized_power_integral(2*item.v_power, cut, -2, ell2), nv)
            # Independently integrate gradient plus momentum energy.
            scalar_energy = item.s*nb+item.b_power**2/cut/ell2 * cut**2*integral_at_one(2*item.b_power)
            vector_energy = item.v_power**2/cut*integral_at_one(2*item.v_power-2)+item.s*nv
            self.assertEqual(scalar_energy, item.response_b)
            self.assertEqual(vector_energy, item.response_v)
        for n1, n2 in ((F(1), F(2)), (F(3, 2), F(5)), (F(2), F(3))):
            a, b = mode(n1, ell2, cut), mode(n2, ell2, cut)
            cross_b = cut*integral_at_one(a.b_power+b.b_power)
            cross_v = ell2/cut*integral_at_one(a.v_power+b.v_power-2)
            self.assertEqual((a.response_b-b.response_b)/(a.s-b.s), cross_b)
            self.assertEqual((a.response_v-b.response_v)/(a.s-b.s), cross_v)
            self.assertNotEqual(cross_b, cut/(n1+n2))  # wrong denominator
        zero = mode(1, ell2, cut)
        self.assertEqual(zero.response_v, 0)
        self.assertGreater(response_derivatives(zero)[1], 0)

    def test_04_static_shell_schur_and_both_riccati_laws(self):
        for ell2, a, b in ((F(1), F(1), F(3)),
                          (F(3, 2), F(2, 3), F(7, 2))):
            shell = static_shell(ell2, a, b)
            for left, right in ((F(1), F(0)), (F(2), F(-3)), (F(3), F(3))):
                d = (left-right)/(1/a-1/b)
                direct_energy = d*d/ell2*(1/a-1/b)
                form = left*(shell[0][0]*left+shell[0][1]*right)+right*(shell[1][0]*left+shell[1][1]*right)
                self.assertEqual(form, direct_energy)
            tail = mode(1, ell2, b).response_b
            schur = shell[0][0]-shell[0][1]*shell[1][0]/(shell[1][1]+tail)
            self.assertEqual(schur, mode(1, ell2, a).response_b)
            without_tail = shell[0][0]-shell[0][1]*shell[1][0]/shell[1][1]
            self.assertEqual(without_tail, 0)
            self.assertNotEqual(without_tail, schur)
            self.assertNotEqual(-schur, mode(1, ell2, a).response_b)
        for nu in (F(1), F(3, 2), F(3), F(7)):
            item = mode(nu, ell2=F(3, 2), cut=F(7, 2))
            self.assertEqual(item.response_b/item.cut,
                             item.ell2*item.response_b**2/item.cut**2-item.s)
            self.assertEqual(-item.response_v/item.cut,
                             item.response_v**2-item.ell2*item.s/item.cut**2)

    def test_05_cubic_power_overlap_and_nonabelian_colour_vertex(self):
        ell2, cut = F(5, 2), F(7, 3)
        for values in product((F(1), F(3, 2), F(3)), repeat=3):
            a, b, c = (mode(n, ell2, cut) for n in values)
            mixed = cut*integral_at_one(a.b_power+b.b_power+c.v_power)
            vectors = ell2/cut*integral_at_one(a.v_power+b.v_power+c.v_power-2)
            self.assertEqual(cubic_factors(a, b, c), (mixed, vectors))
        zero = mode(1, ell2, cut)
        mixed, vectors = cubic_factors(zero, zero, zero)
        self.assertEqual((mixed, vectors), response_derivatives(zero))
        self.assertEqual((mixed, vectors), (cut, ell2/cut))
        with self.assertRaises(ValueError):
            normalized_power_integral(0, cut)  # unweighted vector cubic would diverge
        with self.assertRaises(ValueError):
            cubic_factors(zero, zero, mode(1, ell2, cut+1))
        t1 = ((0, 0, 0), (0, 0, -1), (0, 1, 0))
        t2 = ((0, 0, 1), (0, 0, 0), (-1, 0, 0))
        t3 = ((0, -1, 0), (1, 0, 0), (0, 0, 0))
        self.assertEqual(comm(t3, t2), scale(-1, t1))
        # Hermitian H_j=i*T_j: -i Tr(H1[H3,H2])=-Tr(T1[T3,T2]).
        actual_vertex = -tr(mm(t1, comm(t3, t2)))
        self.assertEqual(actual_vertex, -2)
        self.assertGreater(-tr(mm(t1, t1)), 0)
        self.assertNotEqual(actual_vertex, 0)  # falsely Abelianized interaction

    def test_06_curvature_finite_norm_and_remote_sector_control(self):
        ell2, cut, amplitude, y = F(5, 2), F(7, 3), F(2, 5), F(11, 3)
        b = amplitude*cut/y
        b_prime = -amplitude*cut/y**2
        curvature = -b_prime
        self.assertEqual(curvature, amplitude*cut/y**2)
        norm = amplitude**2*cut*integral_at_one(-2)
        energy = amplitude**2*cut/ell2*integral_at_one(-2)
        self.assertEqual(norm, amplitude**2*cut)
        self.assertEqual(energy, amplitude**2*mode(1, ell2, cut).response_b)
        self.assertNotEqual(b, 0)
        # b=amplitude*cut*t in t=1/y, so the remote perturbation is zero.
        self.assertEqual(amplitude*cut*F(0), 0)
        with self.assertRaises(ValueError):
            integral_at_one(0)  # flat constant shift is not a finite connection mode

        # One commuting gauge channel H=i*J. Solve the parallel-transport
        # ODE and its y derivative by coefficient recursion, then form the
        # inverse and W^-1 W_y independently. No exponentiation oracle.
        j = ((0, -1), (1, 0))
        background = F(3, 7)  # retain its nonzero 1/y connection coefficient
        full_curvature = (background+amplitude*cut)/y**2
        self.assertEqual(full_curvature-background/y**2, curvature)
        self.assertNotEqual(full_curvature, curvature)
        a = F(2, 7)+(background+amplitude*cut)/y
        generator = scale(-a, j)
        generator_derivative = scale(full_curvature, j)
        identity, zero = ((1, 0), (0, 1)), ((0, 0), (0, 0))
        transport, derivative = [identity], [zero]
        for n in range(3):
            derivative.append(scale(F(1, n+1), ma(mm(generator_derivative, transport[n]),
                                                 mm(generator, derivative[n]))))
            transport.append(scale(F(1, n+1), mm(generator, transport[n])))
        inverse = [identity]
        for n in range(1, 4):
            total = zero
            for k in range(1, n+1):
                total = ma(total, mm(transport[k], inverse[n-k]))
            inverse.append(scale(-1, total))
        current = []
        for n in range(4):
            total = zero
            for k in range(n+1):
                total = ma(total, mm(inverse[k], derivative[n-k]))
            current.append(total)
        self.assertEqual(current, [zero, scale(full_curvature, j), zero, zero])
        self.assertNotEqual(current[1], scale(-full_curvature, j))
        self.assertNotEqual(derivative[2], zero)
        self.assertNotEqual(current[2], derivative[2])  # omitting W^-1 fails


if __name__ == "__main__":
    unittest.main(verbosity=2)
