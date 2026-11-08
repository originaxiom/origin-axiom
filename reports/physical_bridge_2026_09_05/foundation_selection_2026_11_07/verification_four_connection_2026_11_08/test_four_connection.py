"""Four UNRUN methods, designed before implementation at e38c42a60.

No direct run entry: source-complete review, acceptance and admission
are required before import, collection or scientific execution.
"""
from fractions import Fraction as F
import unittest

import four_connection_exact as candidate


def mm(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def comm(a, b):
    ab, ba = mm(a, b), mm(b, a)
    return [[x - y for x, y in zip(ar, br)] for ar, br in zip(ab, ba)]


def norm2(a):
    return sum((x * x for row in a for x in row), F(0))


def tail_power_integral(exponent):
    exponent = F(exponent)
    if exponent >= -1:
        raise ValueError('Divergent dimensionless tail power')
    return -1 / (exponent + 1)


def triangle_integral(a, b, nu):
    # First integrate u^(rplus-A) on [1,v], then v^(rminus-B).
    rm, rp = (1 - F(nu)) / 2, (1 + F(nu)) / 2
    inner_exponent_plus_one = rp - a + 1
    if inner_exponent_plus_one:
        return (tail_power_integral(rm - b + inner_exponent_plus_one)
                - tail_power_integral(rm - b)) / inner_exponent_plus_one
    # At exponent -1 the inner primitive is log(v). Differentiate
    # integral v^t dv=-1/(t+1) to integrate v^t log(v).
    return 1 / (rm - b + 1) ** 2


class FourConnectionControls(unittest.TestCase):
    def test_01_green_kernel_and_actual_endpoint_norm(self):
        ell2, cut = F(5, 2), F(7, 3)
        for nu in (F(1), F(3, 2), F(3), F(5)):
            rm, rp, s = candidate.powers(nu, ell2)
            self.assertEqual(rm * (rm - 1), ell2 * s)
            self.assertEqual(rp * (rp - 1), ell2 * s)
            self.assertEqual(rp + rm, 1)
            self.assertEqual(rp - rm, nu)
            # u_left=y^rp-Y^nu y^rm; u_right=y^rm.
            # Their Wronskian u_left' u_right-u_left u_right'=nu.
            self.assertEqual((rp - rm) / nu, 1)
            # The y-derivative jump is -1 after dividing by nu.
            self.assertEqual((rm - rp) / nu, -1)
            self.assertNotEqual((rp - rm) / nu, -1)
            self.assertLess(2 * rm - 2, -1)
            self.assertGreaterEqual(2 * rp - 2, -1)
        for nu in (1, 3, 5):
            for y, z in ((cut, cut), (cut, F(5)), (F(4), F(6))):
                g = candidate.green_at_integer_powers(nu, ell2, cut, y, z)
                self.assertEqual(g, candidate.green_at_integer_powers(nu, ell2, cut, z, y))
                if y == cut or z == cut:
                    self.assertEqual(g, 0)
                else:
                    self.assertGreater(g, 0)
                if nu == 1:
                    self.assertEqual(g, min(y, z) - cut)
        # Explicit sourced profile v=Y^2/2*(1-Y/y) for J=(y/Y)^-3.
        amplitude = cut * cut / 2
        self.assertEqual(amplitude * (1 - cut / cut), 0)
        for y in (cut, 2 * cut, 5 * cut):
            minus_second_derivative = 2 * amplitude * cut / y ** 3
            self.assertEqual(minus_second_derivative, (y / cut) ** -3)
        # Integrate all three terms of its ACTUAL Omega^2 dy norm.
        weighted_norm = ell2 * amplitude ** 2 / cut * (
            tail_power_integral(-2) - 2 * tail_power_integral(-3)
            + tail_power_integral(-4))
        self.assertEqual(weighted_norm, ell2 * amplitude ** 2 / (3 * cut))
        self.assertGreater(amplitude, 0)  # Nonzero constant remote limit.
        with self.assertRaises(ValueError):
            tail_power_integral(0)
        with self.assertRaises(ValueError):
            candidate.green_at_integer_powers(F(3, 2), ell2, cut, cut, 5)

    def test_02_conserved_current_gauss_and_gaussian_coefficient(self):
        ell2 = F(2)
        for np, nq in ((F(1), F(3)), (F(3), F(1)), (F(3), F(3)), (F(1), F(1))):
            row = candidate.pair_current_parameters(np, nq, ell2)
            external_divergence = (row['q2'] - row['p2']) / 2
            radial_derivative = row['radial_coefficient'] * row['radial_power']
            self.assertEqual(external_divergence + radial_derivative, 0)
            self.assertEqual(row['mu_coefficient'], F(1, 2))
            # Independently antisymmetrize f_p f_q' - f_q f_p'.
            bp, bq = -(1 + np) / 2, -(1 + nq) / 2
            self.assertEqual(row['radial_coefficient'], -(bq - bp) / (2 * ell2))
            if np != nq:
                self.assertNotEqual(external_divergence - radial_derivative, 0)
                self.assertNotEqual(2 * row['mu_coefficient'], F(1, 2))
                # Missing y^2 makes the derivative power two lower.
                self.assertNotEqual(row['radial_power'] - 2 - 1, -row['a'])
                self.assertEqual(row['radial_power'] - 1, -row['a'])
            else:
                self.assertEqual(row['radial_coefficient'], 0)
        # Physically consistent 1D p=0,q=1 has k^2=1 and nu=(1,3).
        self.assertEqual(candidate.pair_current_parameters(1, 3, ell2)['q2'], 1)
        for s, jy in ((F(1), F(3, 5)), (F(2), F(-7, 3))):
            c = candidate.gauss_response(s, jy)
            self.assertEqual(s * c + jy, 0)
            self.assertNotEqual(jy, 0)  # c=0 fails this actual equation.
            self.assertEqual(s * c * c / 2 + c * jy, -jy * jy / (2 * s))
        for k, j in (([[F(2), F(1)], [F(1), F(3)]], [F(2), F(-3)]),
                     ([[F(3), F(0)], [F(0), F(2)]], [F(0), F(0)])):
            v, energy = candidate.gaussian_minimum2(k, j)
            residual = [sum((k[i][h] * v[h] for h in range(2)), F(0)) + j[i] for i in range(2)]
            self.assertEqual(residual, [F(0), F(0)])
            self.assertEqual(energy, sum((v[i] * j[i] for i in range(2)), F(0)) / 2)
            self.assertLessEqual(energy, 0)
            # Displace in each basis vector: cross terms cancel and the
            # energy difference is exactly +1/2 delta.K.delta.
            for d in ([F(1), F(0)], [F(0), F(2)]):
                vd = [v[i] + d[i] for i in range(2)]
                varied = sum((vd[i] * k[i][h] * vd[h] for i in range(2) for h in range(2)), F(0)) / 2
                varied += sum((vd[i] * j[i] for i in range(2)), F(0))
                delta = sum((d[i] * k[i][h] * d[h] for i in range(2) for h in range(2)), F(0)) / 2
                self.assertEqual(varied - energy, delta)
                self.assertGreater(delta, 0)
        with self.assertRaises(ValueError):
            candidate.gauss_response(0, 0)

    def test_03_double_overlap_and_logarithmic_cases(self):
        cut = F(7, 3)
        for nu in (F(1), F(3, 2), F(3), F(5)):
            rm, rp, _ = candidate.powers(nu, 1)
            for a, b in ((F(2), F(2)), (F(3), F(4)), (rp + 1, rp + 1), (rp + 1, F(5))):
                if min(a, b) < 2:
                    continue
                t1, t2 = triangle_integral(a, b, nu), triangle_integral(b, a, nu)
                subtraction = tail_power_integral(rm - a) * tail_power_integral(rm - b)
                independent = cut ** 3 * (t1 + t2 - subtraction) / nu
                result = candidate.green_overlap(nu, a, b, cut)
                self.assertEqual(result, independent)
                self.assertEqual(result, candidate.green_overlap(nu, b, a, cut))
                self.assertGreater(result, 0)
                self.assertNotEqual(result, cut ** 3 * (t1 + t2) / nu)
                self.assertNotEqual(result, cut ** 3 * (t1 - subtraction) / nu)
                self.assertEqual(candidate.green_overlap(nu, a, b, 2 * cut), 8 * result)
        for np, nq, nr, nt, nk in ((1, 3, 1, 3, 3), (3, 3, 3, 3, 1), (1, 1, 1, 1, 1)):
            a, b = 1 + F(np + nq, 2), 1 + F(nr + nt, 2)
            self.assertEqual(candidate.four_nu_overlap(np, nq, nr, nt, nk, cut),
                             candidate.green_overlap(nk, a, b, cut))
            self.assertEqual(cut ** 3 * tail_power_integral(2 - a - b), cut ** 3 / (a + b - 3))
        # These are radial algebra controls; the labels (1,1,1,1,1)
        # have no nonzero external momentum assigned to them.

    def test_04_zero_exchange_and_nonabelian_conjugate_pair(self):
        cut = F(7, 3)
        for a, b in ((F(2), F(2)), (F(3), F(4)), (F(7, 2), F(5, 2))):
            # F_A(y)=Y/(A-1) u^(1-A); independently integrate F_A F_B.
            single = cut ** 3 * tail_power_integral(2 - a - b) / ((a - 1) * (b - 1))
            double = cut ** 3 * (triangle_integral(a, b, 1) + triangle_integral(b, a, 1)
                                 - tail_power_integral(-a) * tail_power_integral(-b))
            self.assertEqual(single, double)
            self.assertEqual(single, candidate.longitudinal_zero_overlap(a, b, cut))
            self.assertEqual(double, candidate.green_overlap(1, a, b, cut))
            # For j_y=i k F_A the divergence coefficient is k*(1-1).
            for k in (F(1, 3), F(1, 7)):
                self.assertEqual(k + k * (1 - a) / (a - 1), 0)
                self.assertEqual(k * k * single / (k * k), double)
        self.assertEqual(candidate.pair_current_parameters(3, 3, 2)['radial_coefficient'], 0)
        x = candidate.left_quaternion((0, 1, 0, 0))
        y = candidate.left_quaternion((0, 0, 1, 0))
        bracket = comm(x, y)
        self.assertGreater(norm2(bracket), 0)
        # Hermitian X=i*x,Y=i*y: C=-i[X,Y]=i[x,y].
        # Positive Tr(C^2)=-Tr([x,y]^2) equals real Frobenius norm.
        bracket_squared = mm(bracket, bracket)
        self.assertEqual(-sum((bracket_squared[i][i] for i in range(4)), F(0)), norm2(bracket))
        self.assertEqual(norm2(comm(x, x)), 0)
        # B=X cos(z)+Y sin(z) retains conjugate Fourier partners.
        # Its current is C*(cos^2+sin^2); use an exact circle point.
        co, si = F(3, 5), F(4, 5)
        self.assertEqual(co * co + si * si, 1)
        b = [[co * x[i][j] + si * y[i][j] for j in range(4)] for i in range(4)]
        db = [[-si * x[i][j] + co * y[i][j] for j in range(4)] for i in range(4)]
        self.assertEqual(comm(b, db), bracket)
        self.assertEqual(norm2(comm(b, db)), norm2(bracket))
        # p^2=1,ell^2=2 gives nu=3 and pair power A=4; exchange k=0.
        coefficient = candidate.green_overlap(1, 4, 4, cut)
        self.assertEqual(coefficient, cut ** 3 / 45)
        self.assertLess(-norm2(bracket) * coefficient / 2, 0)
