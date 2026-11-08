"""Seven UNRUN controls designed at 09f478c79; no direct execution entry.

Scientific import/collection/execution requires a separate admitted
source-complete specification. Finite surrogates are NOT core PDE data.
"""

from fractions import Fraction as F
from math import factorial
import unittest

import dynamic_core_exact as candidate


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), F(0))


def mv(a, b):
    return [dot(row, b) for row in a]


def mm(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def difference(a, b):
    return [[x - y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def power_integral(exponent, cut, weight=0, coefficient=F(1)):
    denominator = F(exponent) + weight + 1
    if denominator >= 0:
        raise ValueError('Nonintegrable actual power')
    return -F(coefficient) * F(cut) ** (weight + 1) / denominator


def independent_bessel_coefficients(l):
    # Closed factorial formula, independent of candidate's recurrence.
    return tuple(F(factorial(l + j),
                   factorial(j) * factorial(l - j) * 2 ** j)
                 for j in range(l + 1))


def inverse2(a):
    determinant = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    if not determinant:
        raise ValueError('Singular independent 2x2 comparator')
    return [[a[1][1] / determinant, -a[0][1] / determinant],
            [-a[1][0] / determinant, a[0][0] / determinant]]


class DynamicCoreControls(unittest.TestCase):
    def test_01_half_integer_angular_tail(self):
        for l in (0, 1, 2, 3):
            coefficients = independent_bessel_coefficients(l)
            self.assertEqual(candidate.bessel_polynomial(l), coefficients)
            for z in (F(1, 3), F(1), F(7, 2), F(11)):
                p = sum((c / z ** j for j, c in enumerate(coefficients)), F(0))
                dp = sum((-j * c / z ** (j + 1)
                          for j, c in enumerate(coefficients)), F(0))
                ddp = sum((j * (j + 1) * c / z ** (j + 2)
                           for j, c in enumerate(coefficients)), F(0))
                # u=e^-z P; the common exponential cancels in its ODE.
                self.assertEqual(ddp - 2 * dp - l * (l + 1) * p / z ** 2, 0)
                vector, scalar = candidate.angular_tail_scaled(l, z)
                lower = independent_bessel_coefficients(max(l - 1, 0))
                lower_p = sum((c / z ** j for j, c in enumerate(lower)), F(0))
                self.assertEqual(vector, z * lower_p / p + l)
                self.assertGreater(vector, 0)
                self.assertGreaterEqual(scalar, 0)
                self.assertEqual(vector * scalar, l * (l + 1))
                # Both false modifications have an explicit discriminator.
                self.assertNotEqual(-vector, z * lower_p / p + l)
                if l:
                    wrong_modified_sign = z * (1 + dp / p)
                    self.assertNotEqual(wrong_modified_sign, vector)
        with self.assertRaises(ValueError):
            candidate.angular_tail_scaled(1, 0)

    def test_02_zero_limits_and_norm(self):
        ell2, cut = F(5, 2), F(7, 3)
        rb0, dv0 = candidate.mean_tail(1, ell2, cut)
        self.assertEqual(rb0, cut / ell2)
        self.assertEqual(dv0, 0)
        self.assertGreater(rb0, 0)
        for nu in (F(1), F(3, 2), F(3)):
            rb, dv = candidate.mean_tail(nu, ell2, cut)
            self.assertEqual(rb * dv, (nu * nu - 1) / (4 * ell2))
        for k in (F(-5), F(-2, 3), F(2, 3), F(5)):
            magnitude, sign = abs(k), F(1 if k > 0 else -1)
            # ax=e^-|k|t; ay=i sign(k)e^-|k|t. Check curl and divergence.
            self.assertEqual(-k * sign + magnitude, 0)
            self.assertEqual(k - magnitude * sign, 0)
            exponential_integral = F(1) / (2 * magnitude)
            norm = (1 + sign * sign) * exponential_integral
            self.assertEqual(norm, F(1) / magnitude)
            self.assertNotEqual(exponential_integral, norm)
            # d(s/L)/ds at zero is 1/L(0); L(0)=|k|, regardless of L'(0).
            self.assertEqual(F(1) / magnitude, norm)
            dy_scaled, rb_scaled = candidate.angular_tail_scaled(0, magnitude * cut)
            self.assertEqual(dy_scaled / cut, magnitude)
            self.assertEqual(rb_scaled, 0)
            self.assertNotEqual(rb0, 0)

    def test_03_core_spectral_constant_norm_and_modes(self):
        area, circulation = F(3), (F(1), F(0))
        rows = ((F(2), (F(1), F(1))),
                (F(5), (F(0), F(2))))
        static, derivative0 = candidate.spectral_core_surrogate(0, area, circulation, rows)
        self.assertEqual(static, [[F(1, 3), F(0)], [F(0), F(0)]])
        self.assertNotEqual(static, [[F(1, 3), F(0)], [F(0), F(1, 3)]])
        for s in (F(0), F(1, 3), F(2)):
            response, derivative = candidate.spectral_core_surrogate(s, area, circulation, rows)
            for b in ((F(1), F(0)), (F(2), F(-3))):
                # Independently reconstruct the weighted gradient coefficients.
                norm = sum((lam * (dot(covector, b) / (lam + s)) ** 2
                            for lam, covector in rows), F(0))
                self.assertEqual(dot(b, mv(derivative, b)), norm)
                self.assertGreaterEqual(norm, 0)
            for t in (F(4, 3), F(7)):
                if s == t:
                    continue
                other, _ = candidate.spectral_core_surrogate(t, area, circulation, rows)
                for i in range(2):
                    for j in range(2):
                        expected = sum((lam * cov[i] * cov[j] / ((lam + s) * (lam + t))
                                        for lam, cov in rows), F(0))
                        self.assertEqual((response[i][j] - other[i][j]) / (s - t), expected)
            if s:
                self.assertNotEqual(response[0][1], 0)
        symmetric_rows = ((F(2), (F(1), F(1))),
                          (F(2), (F(1), F(-1))))
        symmetric, _ = candidate.spectral_core_surrogate(2, area, circulation, symmetric_rows)
        self.assertEqual(symmetric[0][1], 0)
        # These supplied Gram data test retention, NOT a computed topology rank.
        gram = [[F(2), F(1)], [F(1), F(3)]]
        self.assertEqual(candidate.relative_harmonic_core_block(3, gram),
                         [[F(6), F(3)], [F(3), F(9)]])
        self.assertEqual(candidate.relative_harmonic_core_block(0, gram),
                         [[F(0), F(0)], [F(0), F(0)]])
        self.assertGreater(derivative0[0][0], 0)
        with self.assertRaises(ValueError):
            candidate.spectral_core_surrogate(1, area, circulation, ((0, (1, 0)),))

    def test_04_gauge_kernel_and_ordered_dual(self):
        p, angular_k = (F(2), F(-1), F(3)), F(5, 3)
        s = dot(p, p)
        d, r = F(7, 2), F(11, 3)
        matrix = candidate.boundary_gauge_matrix(d, r, angular_k, p)
        gauge = (angular_k,) + p
        self.assertEqual(mv(matrix, gauge), [F(0)] * 4)
        for source in ((F(1), F(2), F(3), F(-1)), gauge):
            b, v = source[0], source[1:]
            pv = dot(p, v)
            transverse = tuple(v[i] - p[i] * pv / s for i in range(3))
            expected = d * dot(transverse, transverse) + r * (b - angular_k * pv / s) ** 2
            self.assertEqual(dot(source, mv(matrix, source)), expected)
        no_cross = [row[:] for row in matrix]
        for j in range(1, 4):
            no_cross[0][j] = no_cross[j][0] = F(0)
        self.assertNotEqual(mv(no_cross, gauge), [F(0)] * 4)
        a, b = [[F(2), F(1)], [F(1), F(3)]], [[F(1), F(0)], [F(0), F(2)]]
        for parameter in (F(1, 3), F(2), F(5)):
            dtn = [[a[i][j] + parameter * b[i][j] for j in range(2)] for i in range(2)]
            response, prime = candidate.dual_response_and_derivative(parameter, dtn, b)
            inv = inverse2(dtn)
            expected_prime = mm(mm(inv, a), inv)
            self.assertEqual(prime, expected_prime)
            self.assertEqual(mm(response, dtn), [[parameter, F(0)], [F(0), parameter]])
            wrong_prime = difference(inv, [[parameter * x for x in row] for row in mm(mm(b, inv), inv)])
            self.assertNotEqual(wrong_prime, prime)
            self.assertGreater(prime[0][0], 0)
            self.assertGreater(prime[0][0] * prime[1][1] - prime[0][1] * prime[1][0], 0)
        with self.assertRaises(ValueError):
            candidate.boundary_gauge_matrix(d, r, angular_k, (0, 0))
        with self.assertRaises(ValueError):
            candidate.dual_response_and_derivative(1, [[1, 1], [1, 1]], b)

    def test_05_longitudinal_cubic_ward(self):
        cut, ell2 = F(7, 3), F(2)
        for np in (F(1), F(3, 2), F(3)):
            for nq in (F(1), F(2), F(3)):
                for nk in (F(1), F(3, 2), F(3)):
                    it, il = candidate.vbb_overlaps(np, nq, nk, cut)
                    bp, bq, vk = -(1 + np) / 2, -(1 + nq) / 2, (1 - nk) / 2
                    self.assertEqual(il, power_integral(bp + bq, cut))
                    self.assertEqual(it, power_integral(bp + bq + vk, cut))
                    sp, sq = (np * np - 1) / (4 * ell2), (nq * nq - 1) / (4 * ell2)
                    rbp, _ = candidate.mean_tail(np, ell2, cut)
                    rbq, _ = candidate.mean_tail(nq, ell2, cut)
                    self.assertEqual(il * (sp - sq), rbp - rbq)
                    if np == nq:
                        self.assertEqual(il, cut / np)
                    if nk != 1:
                        k2 = (nk * nk - 1) / (4 * ell2)
                        quotient = (il - it) / k2
                        self.assertEqual(quotient,
                                         candidate.vbb_projector_coefficient(np, nq, nk, ell2, cut))
                    else:
                        # Differentiate the integrated transverse power:
                        # d nu_k/d(k^2)=2 ell^2 at nu_k=1.
                        independent_limit = 4 * ell2 * cut / (np + nq) ** 2
                        self.assertEqual(candidate.vbb_projector_coefficient(np, nq, 1, ell2, cut),
                                         independent_limit)
        # All incoming: p=0, q=(1,0), k=(-1,0), ell^2=2.
        it, il = candidate.vbb_overlaps(1, 3, 3, cut)
        self.assertEqual(il, cut / 2)
        self.assertEqual(it, cut / 3)
        p, q, k = (F(0), F(0)), (F(1), F(0)), (F(-1), F(0))
        w = tuple(x - y for x, y in zip(p, q))
        k2 = dot(k, k)
        longitudinal = tuple(ki * dot(k, w) / k2 for ki in k)
        transverse = tuple(wi - li for wi, li in zip(w, longitudinal))
        vertex = tuple(it * ti + il * li for ti, li in zip(transverse, longitudinal))
        rbp, _ = candidate.mean_tail(1, ell2, cut)
        rbq, _ = candidate.mean_tail(3, ell2, cut)
        self.assertEqual(dot(k, vertex), -(rbp - rbq))
        self.assertNotEqual(it * dot(k, w), -(rbp - rbq))
        # No k=0 projector was divided by: the coefficient quotient has
        # a separately finite limit 4 ell^2 Y/(nu_p+nu_q)^2.
        limit = candidate.vbb_projector_coefficient(1, 3, 1, ell2, cut)
        self.assertEqual(limit, ell2 * cut / 4)
        self.assertGreater(limit, 0)

    def test_06_quartic_relaxation(self):
        examples = (((F(2), F(3, 2), F(5, 3)), (F(3), F(-1, 2), F(7, 4))),
                    ((F(2), F(1)), (F(1), F(-2))),
                    ((F(2), F(3)), (F(4), F(4))))
        for areas, source in examples:
            correction, mean, energy = candidate.top_form_projection_surrogate(areas, source)
            area, total = sum(areas, F(0)), dot(areas, source)
            residual = tuple(f + d for f, d in zip(source, correction))
            self.assertEqual(dot(areas, correction), 0)
            self.assertEqual(set(residual), {total / area})
            self.assertEqual(energy, total * total / area)
            # Tangent variations preserve integral; the energy difference
            # is their positive weighted norm, an independent KKT check.
            for step in (F(-2), F(0), F(1, 3)):
                drift = [F(0)] * len(source)
                drift[0], drift[1] = step * areas[1], -step * areas[0]
                varied = tuple(r + d for r, d in zip(residual, drift))
                self.assertEqual(dot(areas, drift), 0)
                cost = sum((w * v * v for w, v in zip(areas, varied)), F(0))
                expected_cost = energy + sum((w * d * d for w, d in zip(areas, drift)), F(0))
                self.assertEqual(cost, expected_cost)
                self.assertGreaterEqual(cost, energy)
            bare = sum((w * f * f for w, f in zip(areas, source)), F(0))
            if len(set(source)) > 1:
                self.assertGreater(bare, energy)
            else:
                self.assertEqual(correction, tuple(F(0) for _ in source))
            self.assertEqual(mean, total / area)
        with self.assertRaises(ValueError):
            candidate.top_form_projection_surrogate((1, 0), (2, 3))

    def test_07_handle_scope_compact_trace(self):
        a = candidate.left_quaternion((0, 1, 0, 0))
        b = candidate.left_quaternion((0, 0, 1, 0))
        self.assertNotEqual(mm(a, b), mm(b, a))
        obstruction, squared = candidate.period_obstruction_compact_skew(((a, b),))
        explicit = difference(mm(a, b), mm(b, a))
        self.assertEqual(obstruction, explicit)
        self.assertEqual(squared, sum((x * x for row in explicit for x in row), F(0)))
        self.assertEqual(squared, 16)
        zero_matrix = [[F(0)] * 4 for _ in range(4)]
        self.assertEqual(candidate.period_obstruction_compact_skew(((a, a),)), (zero_matrix, F(0)))
        self.assertEqual(candidate.period_obstruction_compact_skew(((a, b), (b, a))),
                         (zero_matrix, F(0)))
        # Exact group-level opposite control, not only tangent cancellation.
        g = candidate.left_quaternion((F(3, 5), F(4, 5), 0, 0))
        h = candidate.left_quaternion((F(5, 13), 0, F(12, 13), 0))
        gt, ht = [list(r) for r in zip(*g)], [list(r) for r in zip(*h)]
        ident = [[F(i == j) for j in range(4)] for i in range(4)]
        self.assertEqual(mm(g, gt), ident)
        self.assertEqual(mm(h, ht), ident)
        self.assertNotEqual(mm(g, h), mm(h, g))
        cgh, chg = mm(mm(mm(g, h), gt), ht), mm(mm(mm(h, g), ht), gt)
        self.assertNotEqual(cgh, ident)
        self.assertEqual(mm(cgh, chg), ident)
        with self.assertRaises(ValueError):
            candidate.period_obstruction_compact_skew(((ident, b),))
