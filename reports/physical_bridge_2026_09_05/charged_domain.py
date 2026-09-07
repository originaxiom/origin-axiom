"""R16: exact local charged forms, normal domains, and extreme-degree L2 tests.

No complete H1 kernel, physical defect choice or global Fredholm certificate.
The differential-form operator is derived from the metric, not a root table.
"""
from __future__ import annotations

from functools import lru_cache
from itertools import combinations
import json
import math
import time

import sympy as sp
from scipy.integrate import quad

r = sp.Symbol('r', positive=True)
theta, t, a, lam, m = sp.symbols('theta t a lambda m', real=True)
COORDS = (r, theta, t)
BASIS = tuple(j for k in range(4) for j in combinations(range(3), k))
NORMAL = ((), (0,), (1,), (0, 1))


def simplify(x):
    return sp.factor(sp.trigsimp(sp.powsimp(sp.expand(x), force=True)))


def clean(form):
    out = {j: simplify(c) for j, c in form.items()}
    return {j: c for j, c in out.items() if c != 0}


def add(*forms):
    out = {}
    for form in forms:
        for j, c in form.items():
            out[j] = out.get(j, 0) + c
    return clean(out)


def scale(form, c):
    return clean({j: c*v for j, v in form.items()})


def wedge(left, right):
    out = {}
    for j, c in left.items():
        for k, d in right.items():
            if set(j) & set(k):
                continue
            sign = (-1)**sum(x > y for x in j for y in k)
            key = tuple(sorted(j+k))
            out[key] = out.get(key, 0)+sign*c*d
    return clean(out)


def exterior(form):
    return add(*(wedge({(i,): sp.diff(c, x)}, {j: 1})
                 for j, c in form.items() for i, x in enumerate(COORDS)))


class MetricForms:
    def __init__(self, lengths):
        self.lengths = tuple(map(sp.sympify, lengths))
        self.volume = sp.prod(self.lengths)

    def basis_length(self, j):
        return sp.prod(self.lengths[i] for i in j)

    def star(self, form):
        out = {}
        for j, c in form.items():
            k = tuple(i for i in range(3) if i not in j)
            sign = (-1)**sum(x > y for x in j for y in k)
            out[k] = sign*c*self.volume/self.basis_length(j)**2
        return clean(out)

    def delta(self, form):
        # In dimension three delta|Omega^k = (-1)^k * d *.
        return add(*(scale(self.star(exterior(self.star({j: c}))), (-1)**len(j))
                     for j, c in form.items()))

    def contract_gradient(self, form, dH):
        out = {}
        for j, c in form.items():
            for pos, i in enumerate(j):
                k = j[:pos]+j[pos+1:]
                out[k] = out.get(k, 0)+(-1)**pos*c*dH.get((i,), 0)/self.lengths[i]**2
        return clean(out)

    def dq(self, form, dH):
        return add(exterior(form), wedge(dH, form))

    def deltaq(self, form, dH):
        return add(self.delta(form), self.contract_gradient(form, dH))

    def D(self, form, dH):
        return add(self.dq(form, dH), self.deltaq(form, dH))


HYP = MetricForms((1, sp.sinh(r), sp.cosh(r)))
FLAT = MetricForms((1, r, 1))


@lru_cache(maxsize=1)
def line_modes():
    ep = sp.tanh(r)**a
    dH = {(0,): a/HYP.volume}
    rows = []
    for j in BASIS:
        c = ep*HYP.basis_length(j)**2/HYP.volume if 0 in j else 1/ep
        orth = c/HYP.basis_length(j)
        exponent = sp.limit(simplify(r*sp.diff(orth, r)/orth), r, 0)
        rows.append(dict(basis=j, coefficient=c, exponent=exponent,
                         d=HYP.dq({j: c}, dH), delta=HYP.deltaq({j: c}, dH)))
    return rows


def integrable(exponent, measure_power=1):
    """A strict test of integral r^(2*exponent+measure_power) dr at zero."""
    return bool(2*sp.sympify(exponent)+measure_power > -1)


def integrable_components(charge):
    return [row['basis'] for row in line_modes()
            if integrable(row['exponent'].subs(a, charge))]


@lru_cache(maxsize=1)
def angular_matrix():
    phase = r**lam*sp.exp(sp.I*m*theta)
    dH = {(0,): a/r}
    matrix = sp.zeros(8)
    ordered = NORMAL + tuple(j+(2,) for j in NORMAL)
    for col, j in enumerate(ordered):
        out = FLAT.D({j: phase*FLAT.basis_length(j)}, dH)
        for row, k in enumerate(ordered):
            matrix[row, col] = simplify(out.get(k, 0)*r/(phase*FLAT.basis_length(k)))
    return matrix


@lru_cache(maxsize=1)
def hyperbolic_indicial_matrix():
    momentum = sp.Symbol('k', real=True)
    phase = r**lam*sp.exp(sp.I*(m*theta+momentum*t))
    ordered = NORMAL + tuple(j+(2,) for j in NORMAL)
    matrix = sp.zeros(8)
    for col, j in enumerate(ordered):
        out = HYP.D({j: phase*HYP.basis_length(j)}, {(0,): a/HYP.volume})
        for row, k in enumerate(ordered):
            coefficient = simplify(out.get(k, 0)*r/(phase*HYP.basis_length(k)))
            matrix[row, col] = sp.limit(coefficient, r, 0)
    return matrix


def normalized_tangential():
    I = angular_matrix()[:4, :4]
    J = I.diff(lam)
    K = I.subs(lam, 0)
    return J, sp.simplify(-J*K-sp.eye(4)/2)


def critical_eigenvalues(charge, angular):
    nu = sp.sqrt(sp.sympify(charge)**2+sp.sympify(angular)**2)
    eigen = [s*nu+h for s in (-1, 1) for h in (-sp.Rational(1, 2), sp.Rational(1, 2))]
    return [v for v in eigen if bool(-sp.Rational(1, 2) < v < sp.Rational(1, 2))]


def power_integral(power, epsilon, outer):
    """Integral epsilon..outer r^power dr, including the logarithmic boundary."""
    if not 0 < epsilon < outer:
        raise ValueError('requires 0 < epsilon < outer')
    p = float(power)+1.0
    if p == 0:
        return math.log(outer/epsilon)
    return epsilon**p*math.expm1(p*math.log(outer/epsilon))/p


def capacity(exponent, epsilon, outer):
    return 1/power_integral(-2*float(exponent)-1, epsilon, outer)


@lru_cache(maxsize=1)
def boundary_identities():
    rows = {row['basis']: row for row in line_modes()}
    scalar, radial = rows[()]['coefficient'], rows[(0,)]['coefficient']
    chi = sp.Function('chi')(r)
    dH = {(0,): a/HYP.volume}
    L, eps, R = sp.symbols('L epsilon R', positive=True)
    # Capacity follows by minimizing int w * chi'^2 with int chi'=1.
    weight = r**(2*L+1)
    inverse_weight_integral = (eps**(-2*L)-R**(-2*L))/(2*L)
    minimizing_derivative = 1/(weight*inverse_weight_integral)
    energy = sp.integrate(weight*minimizing_derivative**2, (r, eps, R))
    normalization = sp.integrate(minimizing_derivative, (r, eps, R))
    return dict(green_pair=simplify(HYP.volume*scalar*radial),
                radial_d_cutoff=HYP.dq({(0,): chi*radial}, dH),
                scalar_delta_cutoff=HYP.deltaq({(): chi*scalar}, dH),
                scalar_d_cutoff=HYP.dq({(): chi*scalar}, dH),
                radial_delta_cutoff=HYP.deltaq({(0,): chi*radial}, dH),
                capacity_inverse=1/inverse_weight_integral,
                capacity_energy_identity=simplify(energy-1/inverse_weight_integral),
                cutoff_normalization=simplify(normalization))


@lru_cache(maxsize=1)
def numerical_norm_controls():
    rows = []
    outer = 0.01
    for charge in (-2, -1, -0.5, 0, 0.5, 1, 2):
        for mode in line_modes():
            j = mode['basis']
            exponent = float(mode['exponent'].subs(a, charge))
            for eps in (1e-4, 1e-6, 1e-8):
                exact = power_integral(2*exponent+1, eps, outer)
                flat_quad = quad(lambda s: math.exp((2*exponent+2)*s),
                                 math.log(eps), math.log(outer), epsabs=1e-13, epsrel=1e-12)[0]
                def hyperbolic(s):
                    radius = math.exp(s)
                    log_A, log_B = math.log(math.sinh(radius)), math.log(math.cosh(radius))
                    log_T = math.log(math.tanh(radius))
                    if 0 in j:
                        log_density = (2*charge*log_T + 2*(1 in j)*log_A
                                       + 2*(2 in j)*log_B-log_A-log_B)
                    else:
                        log_density = (-2*charge*log_T + log_A+log_B
                                       - 2*(1 in j)*log_A-2*(2 in j)*log_B)
                    return math.exp(log_density+s)
                hyper = quad(hyperbolic, math.log(eps), math.log(outer),
                             epsabs=1e-13, epsrel=1e-12)[0]
                rows.append(dict(a=charge, basis=j, epsilon=eps, outer=outer,
                                 exponent=exponent, integrable=integrable(exponent),
                                 flat_exact=exact, flat_quad=flat_quad, hyperbolic_quad=hyper,
                                 quadrature_relative_error=abs(flat_quad/exact-1),
                                 hyperbolic_relative_correction=abs(hyper/exact-1)))
    return rows


def extreme_l2(q, cusp_densities):
    """Complete formal 0/3-form L2 test on R15's positive-source background.

    Assumes every prescribed line has cusp ends, the declared end asymptotics,
    a connected core and trivial gauge bundle. Does not select a closed domain.
    """
    q = sp.sympify(q)
    cusps = tuple(tuple(map(sp.sympify, c)) for c in cusp_densities)
    if not cusps or any(not c or any(b <= 0 for b in c) for c in cusps):
        raise ValueError('requires nonempty cusps with strictly positive source densities')
    def scalar(charge):
        if charge == 0:
            return True
        height = all(charge*sum(c) > 0 for c in cusps)
        transverse = all(charge*b < 1 for c in cusps for b in c)
        return bool(height and transverse)
    return dict(scalar=scalar(q), top=scalar(-q))


@lru_cache(maxsize=1)
def cusp_identities():
    # The symbols r,theta,t serve here simply as three independent coordinates.
    F = sp.Function('F')(*COORDS)
    q = sp.Symbol('q', real=True)
    dH = exterior({(): q*F})
    general = HYP
    scalar = {(): sp.exp(-q*F)}
    top = {(0, 1, 2): general.volume*sp.exp(q*F)}
    z, C, c, U = sp.symbols('z C c U', positive=True)
    potential = U+C*z**2*sp.log(z)+c*z**2
    density = sp.exp(-2*q*potential)*z**(-3)
    separation = sp.exp(-2*q*U)*sp.exp(-2*q*(C*z**2*sp.log(z)+c*z**2))*z**(-3)
    return dict(scalar_equation=general.D(scalar, dH), top_equation=general.D(top, dH),
                separated_norm_identity=sp.simplify(density-separation),
                leading_log_density=sp.limit(sp.log(density)/(z**2*sp.log(z)), z, sp.oo))


def jsonable(value):
    if isinstance(value, sp.MatrixBase):
        return [[jsonable(x) for x in row] for row in value.tolist()]
    if isinstance(value, dict):
        return {str(k): jsonable(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [jsonable(v) for v in value]
    if isinstance(value, sp.Basic):
        return str(value)
    return value


def run():
    started = time.monotonic()
    I = angular_matrix()[:4, :4]
    J, A = normalized_tangential()
    x = sp.Symbol('x')
    charges = (-2, -1, -sp.Rational(1, 2), 0, sp.Rational(1, 2), 1, 2)
    norms = numerical_norm_controls()
    out = dict(modes=line_modes(), angular_matrix=angular_matrix(),
               hyperbolic_indicial_matrix=hyperbolic_indicial_matrix(),
               normal_characteristic=sp.factor(I.det()), J=J, tangential=A,
               tangential_characteristic=sp.factor(A.charpoly(x).as_expr()),
               angular_controls=[dict(a=b, m=k, critical=critical_eigenvalues(b, k))
                                 for b in charges for k in range(-3, 4)],
               line_integrability=[dict(a=b, components=integrable_components(b)) for b in charges],
               boundary=boundary_identities(), norm_controls=norms,
               worst_flat_quadrature_error=max(row['quadrature_relative_error'] for row in norms),
               worst_hyperbolic_correction=max(row['hyperbolic_relative_correction'] for row in norms),
               cusp=cusp_identities(),
               extreme_degrees=[dict(q=b, **extreme_l2(b, ((1, 1, 1), (1, 1, 1)))) for b in charges],
               capacities=[dict(exponent=L, epsilon=e, value=capacity(L, e, 0.01))
                           for L in (-0.75, -0.5, -0.25, 0, 0.5) for e in (1e-4, 1e-6, 1e-8)],
               scope='local normal domains and complete formal degrees 0/3; not a complete H1 index')
    out['runtime_seconds'] = time.monotonic()-started
    return jsonable(out)


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True), flush=True)
