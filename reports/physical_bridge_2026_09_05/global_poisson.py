"""R31 controls for the separately proved compact normalized Poisson estimate.

No m202 mesh, certified intervals, complete-end spectrum or empirical masses.
The infinite tube and half-space computations are explicitly comparators.
"""
from __future__ import annotations

from functools import lru_cache
import json
import math
import time

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad
import sympy as sp


def clean(expr):
    return sp.factor(sp.cancel(sp.expand_trig(expr.rewrite(sp.exp))))


@lru_cache(maxsize=None)
def exact_controls():
    r, e, d, beta, height = sp.symbols('r e d beta height', positive=True)
    theta, z, s, phi, t = sp.symbols('theta z s phi t', real=True)
    embedding = sp.Matrix([sp.cosh(r)*sp.cosh(z), sp.cosh(r)*sp.sinh(z),
                           sp.sinh(r)*sp.cos(theta), sp.sinh(r)*sp.sin(theta)])
    jac = embedding.jacobian([r, theta, z])
    metric = jac.T*sp.diag(-1, 1, 1, 1)*jac
    metric_target = sp.diag(1, sp.sinh(r)**2, sp.cosh(r)**2)
    metric_residual = (metric-metric_target).applyfunc(lambda v: sp.trigsimp(v))
    point = embedding.subs({theta: 0, z: 0})
    other = embedding.subs({r: s, theta: phi})
    cosh_distance = (point.T*sp.diag(1, -1, -1, -1)*other)[0]
    distance_target = sp.cosh(r)*sp.cosh(s)*sp.cosh(z)-sp.sinh(r)*sp.sinh(s)*sp.cos(phi)
    kernel = (sp.coth(d)-1)/(4*sp.pi)
    euclidean = 1/(4*sp.pi*d)
    radial = lambda f: sp.diff(f, d, 2)+2*sp.coth(d)*sp.diff(f, d)
    w = sp.sinh(r)*sp.cosh(r)
    inside = beta*(sp.log(sp.tanh(e))+(sp.log(sp.cosh(r))-sp.log(sp.cosh(e)))/sp.sinh(e)**2)
    outside = beta*sp.log(sp.tanh(r))
    div = lambda f: sp.diff(w*sp.diff(f, r), r)/w
    mass = 2*sp.pi*beta
    normal_disc_ratio = 2/(1+sp.cosh(e))
    ball = sp.pi*(sp.sinh(2*e)-2*e)
    two_cap_mass = 4*beta*ball/sp.sinh(e)**2
    c = sp.symbols('c', positive=True)
    stable_identity = sp.expand((1+c-sp.sqrt(c*(c+2)))*(1+c+sp.sqrt(c*(c+2)))-1)
    C = sp.symbols('C', positive=True)
    primitive = (sp.asinh(C*sp.sinh(t))-t)/(4*sp.pi)
    primitive_derivative = (C*sp.cosh(t)/sp.sqrt(1+C**2*sp.sinh(t)**2)-1)/(4*sp.pi)
    radicand = sp.sinh(r)**2+sp.cosh(r)**2*sp.sinh(t)**2-(sp.cosh(r)**2*sp.cosh(t)**2-1)
    fixed_height_center = height*(sp.sinh(e)**2*sp.log(sp.tanh(e))-sp.log(sp.cosh(e)))/2
    zeros = {
        'fermi_metric': list(map(str, metric_residual)),
        'fermi_distance': str(sp.simplify(cosh_distance-distance_target)),
        'kernel_radial_equation': str(clean(radial(kernel))),
        'kernel_flux_minus_one': str(clean(-4*sp.pi*sp.sinh(d)**2*sp.diff(kernel, d)-1)),
        'kernel_stable_identity': str(stable_identity),
        'inside_poisson': str(clean(div(inside)-2*beta/sp.sinh(e)**2)),
        'outside_poisson': str(clean(div(outside))),
        'value_join': str(sp.simplify((inside-outside).subs(r, e))),
        'derivative_join': str(clean((sp.diff(inside, r)-sp.diff(outside, r)).subs(r, e))),
        'axis_derivative': str(sp.limit(sp.diff(inside, r), r, 0, dir='+')),
        'linear_source_mass': str(clean(2*beta/sp.sinh(e)**2*2*sp.pi*sp.integrate(w, (r, 0, e))-mass)),
        'ball_volume_derivative': str(clean(sp.diff(ball, e)-4*sp.pi*sp.sinh(e)**2)),
        'two_cap_mass_limit': str(sp.limit(two_cap_mass, e, 0, dir='+')),
        'line_primitive_derivative': str(sp.simplify(sp.diff(primitive, t)-primitive_derivative)),
        'line_distance_radicand': str(clean(radicand)),
        'fixed_height_center_limit': str(sp.limit(fixed_height_center, e, 0, dir='+')),
        'sign_reversal': str(sp.simplify(inside.subs(beta, -beta)+inside)),
    }
    return {
        'zero_residuals': zeros,
        'point_kernel_singular_coefficient': str(sp.limit(d*kernel, d, 0, dir='+')),
        'correct_linear_mass': str(mass),
        'normal_disc_wrong_ratio': str(normal_disc_ratio),
        'normal_disc_wrong_ratio_at_one': float(normal_disc_ratio.subs(e, 1)),
        'euclidean_wrong_h3_residual_at_one': float(radial(euclidean).subs(d, 1)),
        'endpoint_two_ball_mass_slope': str(sp.limit(two_cap_mass/e, e, 0, dir='+')),
    }


def positive_finite(value, name):
    value = float(value)
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f'{name} must be positive and finite')
    return value


def green_from_cosh_minus_one(c):
    """Stable positive H3 kernel; c=cosh(distance)-1, not distance itself."""
    c = np.asarray(c, dtype=float)
    if np.any(~np.isfinite(c)) or np.any(c <= 0):
        raise ValueError('kernel requires positive finite cosh(distance)-1')
    root = np.sqrt(c*(c+2))
    return 1/(4*math.pi*root*(1+c+root))


def distance_c(r, s, theta, z):
    # Avoid subtracting nearly equal cosh products when epsilon is small.
    return (2*np.sinh((r-s)/2)**2
            + 2*np.cosh(r)*np.cosh(s)*np.sinh(z/2)**2
            + 2*np.sinh(r)*np.sinh(s)*np.sin(theta/2)**2)


def axial_tail_bound(beta, cutoff):
    cutoff = positive_finite(cutoff, 'cutoff')
    beta = float(beta)
    if not math.isfinite(beta) or beta < 0:
        raise ValueError('tail bound requires finite nonnegative beta')
    return -beta*math.log1p(-math.exp(-2*cutoff))


def radial_field(r, epsilon, beta=1.0):
    epsilon = positive_finite(epsilon, 'epsilon')
    r, beta = float(r), float(beta)
    if not math.isfinite(r) or r < 0 or not math.isfinite(beta):
        raise ValueError('radius must be finite nonnegative and beta finite')
    if r >= epsilon:
        return beta*math.log(math.tanh(r))
    # log(cosh r) evaluated accurately down to a very small radius.
    log_cosh = lambda x: math.log1p(2*math.sinh(x/2)**2)
    return beta*(math.log(math.tanh(epsilon))
                 +(log_cosh(r)-log_cosh(epsilon))/math.sinh(epsilon)**2)


def tube_green_integral(r, epsilon, beta=1.7, radial_order=24,
                        angular_order=48, cutoff=14.0):
    r, epsilon = positive_finite(r, 'r'), positive_finite(epsilon, 'epsilon')
    cutoff = positive_finite(cutoff, 'cutoff')
    beta = float(beta)
    if r < 2*epsilon or not math.isfinite(beta) or beta < 0:
        raise ValueError('positive convolution control requires r>=2epsilon and beta>=0')
    if (not isinstance(radial_order, int) or radial_order < 2
            or not isinstance(angular_order, int) or angular_order < 4):
        raise ValueError('quadrature orders too small or not integers')
    nodes, weights = leggauss(radial_order)
    radii = np.arcsinh(math.sinh(epsilon)*np.sqrt((nodes+1)/2))[:, None]
    weights = weights/2
    angles = (2*math.pi*np.arange(angular_order)/angular_order)[None, :]

    def axial_integrand(z):
        kernels = green_from_cosh_minus_one(distance_c(r, radii, angles, z))
        return float(weights @ np.mean(kernels, axis=1))

    val, err = quad(axial_integrand, 0, cutoff, epsabs=2e-11, epsrel=2e-11, limit=300)
    factor = 4*math.pi*beta  # both z tails and the full angular period
    return dict(value=factor*val, estimated_quadrature_error=factor*err,
                positive_axial_tail_bound=axial_tail_bound(beta, cutoff),
                transverse_grid=[radial_order, angular_order], cutoff=cutoff,
                interval_certified=False)


def line_primitive(r, t):
    r = positive_finite(r, 'r')
    return (math.asinh(math.sinh(t)/math.tanh(r))-t)/(4*math.pi)


def halfspace_line_field(r, z, length=1.3, beta=1.0):
    r, length = positive_finite(r, 'r'), positive_finite(length, 'length')
    if z < 0:
        raise ValueError('observation must lie in z>=0 half-space')
    return -2*math.pi*beta*(2*line_primitive(r, z)-line_primitive(r, z-length)
                           -line_primitive(r, z+length))


@lru_cache(maxsize=None)
def numerical_controls():
    lines = []
    for r in (.001, .03, .4, 1.2):
        v, err = quad(lambda z: float(green_from_cosh_minus_one(distance_c(r, 0, 0, z))),
                      0, 14, epsabs=2e-11, epsrel=2e-11, limit=300)
        expected = -math.log(math.tanh(r))/(2*math.pi)
        tail = axial_tail_bound(1, 14)/(2*math.pi)
        lines.append(dict(r=r, integral=2*v, expected=expected, error=2*v-expected,
                          estimated_quadrature_error=2*err, positive_tail_bound=tail))
    tubes = []
    for epsilon in (.2, .04, .005):
        for factor in (2, 4):
            r = factor*epsilon
            low = tube_green_integral(r, epsilon, radial_order=12, angular_order=24)
            high = tube_green_integral(r, epsilon, radial_order=24, angular_order=48)
            expected = -radial_field(r, epsilon, 1.7)
            tubes.append(dict(epsilon=epsilon, r=r, beta=1.7, low=low, high=high,
                              expected=expected, high_error=high['value']-expected,
                              resolution_difference=high['value']-low['value']))
    halfspace = []
    for r in (.1, .01, .001):
        z = .4
        fun = lambda s: float(green_from_cosh_minus_one(distance_c(r, 0, 0, z-s))
                              -green_from_cosh_minus_one(distance_c(r, 0, 0, z+s)))
        val, err = quad(fun, 0, 1.3, points=[z], epsabs=2e-11, epsrel=2e-11, limit=300)
        expected = halfspace_line_field(r, z)
        halfspace.append(dict(r=r, z=z, length=1.3, integral=-2*math.pi*val,
                              expected=expected, error=-2*math.pi*val-expected,
                              estimated_quadrature_error=2*math.pi*err,
                              boundary_value=halfspace_line_field(r, 0),
                              boundary_log_discrepancy=abs(math.log(r))))
    slope = ((halfspace_line_field(.001, .4)-halfspace_line_field(.0001, .4))
             /math.log(10))
    heights = []
    for e in (.1, .01, .001, .0001):
        beta = math.sinh(e)**2/2
        heights.append(dict(epsilon=e, density=1.0, beta=beta,
                            central_field=radial_field(0, e, beta)))
    return dict(line_integrals=lines, tube_convolutions=tubes, reflected_line=halfspace,
                interior_log_slope=slope, fixed_height=heights)


def control_checks(exact, numeric):
    zeros = exact['zero_residuals']
    scalar_zeros = {k: v for k, v in zeros.items() if k != 'fermi_metric'}
    tol = lambda row: 5e-8*max(1, abs(row['expected']))
    h = numeric['fixed_height']
    return {
        'exact_fermi_metric': zeros['fermi_metric'] == ['0']*9,
        'exact_scalar_identities': all(v == '0' for v in scalar_zeros.values()),
        'point_source_coefficient': exact['point_kernel_singular_coefficient'] == '1/(4*pi)',
        'euclidean_kernel_rejected': exact['euclidean_wrong_h3_residual_at_one'] < -.01,
        'normal_disc_measure_rejected': abs(exact['normal_disc_wrong_ratio_at_one']-1) > .1,
        'independent_axis_integrals': all(abs(r['error']) < 8e-10+r['positive_tail_bound']
                                         for r in numeric['line_integrals']),
        'low_resolution_tube_integrals': all(abs(r['low']['value']-r['expected']) < tol(r)
                                            for r in numeric['tube_convolutions']),
        'high_resolution_tube_integrals': all(abs(r['high_error']) < tol(r)
                                             for r in numeric['tube_convolutions']),
        'transverse_refinement': all(abs(r['resolution_difference']) < tol(r)
                                     for r in numeric['tube_convolutions']),
        'reflected_dirichlet_line': all(abs(r['error']) < 8e-10 and abs(r['boundary_value']) < 1e-13
                                        for r in numeric['reflected_line']),
        'interior_log_coefficient': abs(numeric['interior_log_slope']-1) < 2e-5,
        'fixed_height_is_different': (all(abs(a['central_field']) > abs(b['central_field'])
                                           for a, b in zip(h, h[1:]))
                                     and abs(h[-1]['central_field']) < 1e-6
                                     and abs(h[0]['central_field']) > 100*abs(h[-1]['central_field'])),
    }


def run():
    started = time.monotonic()
    exact, numeric = exact_controls(), numerical_controls()
    checks = control_checks(exact, numeric)
    return dict(exact=exact, numeric=numeric, checks=checks, all_checks_pass=all(checks.values()),
                runtime_seconds=time.monotonic()-started,
                scope='Identity and comparator controls for the separate compact proof; not a global mesh solve, interval certificate, independent proof review or complete physical spectrum.')


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, indent=2, sort_keys=True), flush=True)
    raise SystemExit(0 if result['all_checks_pass'] else 1)
