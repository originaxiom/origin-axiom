"""UNRUN successor for independent review R1/R2. Admission still required.

The predecessor and its unfavorable coverage verdict are preserved.
This module must not be imported/collected before genuine admission.
It exposes one ten-method subclass, not the predecessor TestCase alias.
"""
from hashlib import sha256
import importlib.util
from pathlib import Path


_BASE_PATH = Path(__file__).resolve().parent.parent / "verification_radial_flow" / "checks.py"
_BASE_SHA256 = "ad60f47e14c9671277e8888202451a2db7b414b58d48ed347cf735b2eff9d7d5"
if sha256(_BASE_PATH.read_bytes()).hexdigest() != _BASE_SHA256:
    raise ValueError("Preserved radial source changed; refuse scientific import")
_spec = importlib.util.spec_from_file_location("radial_preserved_unrun_controls", _BASE_PATH)
if _spec is None or _spec.loader is None:
    raise ValueError("Cannot locate the preserved radial source")
_base = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_base)
s = _base.s


def polynomial_module(n):
    """Reconstruct operators by differentiating monomials, not old outputs."""
    x, y = s.symbols("polynomial_x polynomial_y")
    basis = [x**(n-k)*y**k for k in range(n+1)]
    raising = [x*s.diff(v, y) for v in basis]
    lowering = [y*s.diff(v, x) for v in basis]
    grading = [x*s.diff(v, x)-y*s.diff(v, y) for v in basis]
    matrices = [s.Matrix(n+1, n+1, lambda i, k:
                         s.Poly(images[k], x, y).coeff_monomial(basis[i]))
                for images in (raising, lowering, grading)]
    gram = s.diag(*[s.Rational(1, int(s.binomial(n, k))) for k in range(n+1)])
    bilinear = s.zeros(n+1)
    for k in range(n+1):
        bilinear[k, n-k] = (-1)**k*gram[k, k]
    return (*matrices, gram, bilinear)


class RadialFlowV2Checks(_base.RadialFlowChecks):
    def test_kinetic_rescalings_and_nonconstant_complex_identity(self):
        super().test_kinetic_rescalings_and_nonconstant_complex_identity()
        y = s.symbols("y", positive=True)
        f_coordinate = s.symbols("f_coordinate", real=True)
        q_bg = f_coordinate/(2*s.sqrt(y))
        gauge_coefficient = s.sqrt(2)*q_bg*s.sqrt(y)
        hessian_coefficient = y*q_bg*s.sqrt(2/y)
        self.assertZero(gauge_coefficient-f_coordinate/s.sqrt(2))
        self.assertZero(hessian_coefficient-f_coordinate/s.sqrt(2))
        omitted_normalization = q_bg*s.sqrt(y)
        self.assertFalse(_base.zero((omitted_normalization-gauge_coefficient).subs(f_coordinate, 1)))
        paired_count, identity_gram_rejected = 0, False
        t = s.symbols("t", real=True)
        h, f = s.Function("h", real=True)(t), s.Function("f", real=True)(t)
        u = s.Function("r_profile")(t)
        for j in range(1, 5):
            e, lower, grading, gram, bilinear = polynomial_module(2*j)
            self.assertZero(gram.inv()*e.T*gram-lower)
            self.assertZero(_base.comm(e, lower)-grading)
            self.assertZero(_base.comm(grading, e)-2*e)
            for operator in (e, lower, grading):
                self.assertZero(bilinear*operator+operator.T*bilinear)
            self.assertZero(bilinear.T*gram.inv()*bilinear-gram)
            normalizer = s.diag(*[s.sqrt(gram[k, k]) for k in range(2*j+1)])
            normalized_e = normalizer*e*normalizer.inv()
            for m in range(-j, j):
                if m % 2:
                    continue
                paired_count += 1
                index = j-m
                q_index = index-1
                r_index = 2*j-q_index
                amplitude = s.simplify(normalized_e[index-1, index])
                weighted_square = e[index-1, index]**2*gram[index-1, index-1]/gram[index, index]
                self.assertZero(amplitude**2-weighted_square)
                self.assertEqual(weighted_square, (j-m)*(j+m+1))
                identity_gram_rejected |= weighted_square != e[index-1, index]**2
                k_gauge = gauge_coefficient*amplitude
                k_hessian = hessian_coefficient*amplitude
                self.assertZero(k_gauge-k_hessian)
                self.assertZero(k_gauge**2-f_coordinate**2*(j-m)*(j+m+1)/2)

                self.assertNotEqual(bilinear[q_index, r_index], 0)
                self.assertEqual(grading[q_index, q_index]/2, m+1)
                r_weight = grading[r_index, r_index]/2
                self.assertEqual(r_weight, -m-1)
                self.assertEqual(bilinear[q_index, q_index], 0)
                r_raising_square = e[r_index-1, r_index]**2*gram[r_index-1, r_index-1]/gram[r_index, r_index]
                self.assertEqual(r_raising_square, weighted_square)
                quartic_radial = 2*y*q_bg**2*r_raising_square
                self.assertZero(quartic_radial-k_gauge**2)

                hy, uy = s.Function("hy", real=True)(y), s.Function("uy")(y)
                r_coordinate = y*(uy.diff(y)+hy*r_weight*uy/(2*y))
                self.assertZero(r_coordinate-y*uy.diff(y)+hy*(m+1)*uy/2)
                same_weight_coordinate = y*(uy.diff(y)+hy*(m+1)*uy/(2*y))
                self.assertFalse(_base.zero((same_weight_coordinate-r_coordinate).subs(hy, 1)))

                a, b, k = s.Rational(1, 2)+h*m/2, h*(m+1)/2, f*amplitude/s.sqrt(2)
                r_derivative = u.diff(t)-b*u
                r_square = -r_derivative.diff(t)-b*r_derivative+k*k*u
                expected = -u.diff(t, 2)+(b*b+b.diff(t)+k*k)*u
                self.assertZero(r_square-expected)
                mass, sign = s.Matrix([[a, k], [k, -b]]), s.diag(1, -1)
                vector = s.Matrix([0, u])
                applied = sign*(vector.diff(t)+mass*vector)
                full_square = -(sign*applied).diff(t)+mass*sign*applied
                self.assertZero(full_square[1]-r_square)
                self.assertZero(full_square[0].subs(f.diff(t), (1-h)*f/2))
                wrong_dual_derivative = u.diff(t)+b*u
                self.assertFalse(_base.zero((wrong_dual_derivative-r_derivative).subs(h, 1)))
        self.assertEqual(paired_count, 10)
        self.assertTrue(identity_gram_rejected)

    def test_both_scalar_extremes_and_constant_recovery(self):
        super().test_both_scalar_extremes_and_constant_recovery()
        y = s.symbols("y", positive=True)
        t = s.symbols("t", real=True)
        hy, uy = s.Function("hy", real=True)(y), s.Function("uy")(y)
        h = s.Function("h", real=True)(t)
        u = s.Function("u")(t)
        pair = s.Matrix([s.Function("x")(t), s.Function("v")(t)])
        sx, sy = s.Matrix([[0, 1], [1, 0]]), s.Matrix([[0, -s.I], [s.I, 0]])
        orientations = {}
        derivative_controls = 0
        for j in range(5):
            if j % 2 == 0:
                coordinate = s.sqrt(y)*(s.diff(s.sqrt(y)*uy, y)+hy*j*s.sqrt(y)*uy/(2*y))
                coefficient_y = s.simplify((coordinate-y*uy.diff(y))/uy)
                self.assertZero(coefficient_y-(s.Rational(1, 2)+hy*j/2))
                epsilon = 1
                expected_k = s.Rational(1, 2)+h*j/2
                constant = s.Rational(j+1, 2)
            else:
                coordinate = y*(uy.diff(y)-hy*j*uy/(2*y))
                coefficient_y = s.simplify((coordinate-y*uy.diff(y))/uy)
                self.assertZero(coefficient_y+hy*j/2)
                epsilon = -1  # Actual spin derivative's formal adjoint in dt.
                expected_k = h*j/2
                constant = s.Rational(j, 2)
            orientations[j] = epsilon
            c = coefficient_y.subs(hy, h)
            k = epsilon*c
            self.assertZero(k-expected_k)

            apply_b = lambda value: epsilon*value.diff(t)+c*value
            apply_bd = lambda value: -epsilon*value.diff(t)+c*value
            actual_left, actual_right = apply_bd(apply_b(u)), apply_b(apply_bd(u))
            self.assertZero(actual_left-(-u.diff(t, 2)+(k*k-k.diff(t))*u))
            self.assertZero(actual_right-(-u.diff(t, 2)+(k*k+k.diff(t))*u))
            flipped = -epsilon*u.diff(t)+c*u
            self.assertFalse(_base.zero(flipped-apply_b(u)))

            def doubled(value):
                return s.Matrix([apply_bd(value[1]), apply_b(value[0])])

            unitary = s.diag(1, s.I*epsilon)
            declared = -s.I*sx*pair.diff(t)-sy*k*pair
            self.assertZero(unitary.H*doubled(unitary*pair)-declared)
            wrong_unitary = s.diag(1, epsilon)
            self.assertFalse(_base.zero(wrong_unitary.H*doubled(wrong_unitary*pair)-declared))
            self.assertZero(k.subs(h, 1)-constant)
            self.assertZero(k.subs(h, 1)**2-constant**2)
            omitted_derivative = -u.diff(t, 2)+k*k*u
            if j:
                self.assertFalse(_base.zero(actual_left-omitted_derivative))
                derivative_controls += 1
            else:
                self.assertZero(actual_left-omitted_derivative)
        self.assertEqual(orientations, {0: 1, 1: -1, 2: 1, 3: -1, 4: 1})
        self.assertEqual(derivative_controls, 4)
