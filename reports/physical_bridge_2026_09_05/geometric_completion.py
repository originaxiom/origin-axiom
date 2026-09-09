"""R22: compose R21 with the actual source/domain, not an imported EFT.

Analytic domain and unique-continuation inputs are in the sealed design.
Finite matrix/integral controls do not independently prove those inputs.
"""
from __future__ import annotations

from functools import lru_cache
import importlib.util
import itertools
import json
import math
from pathlib import Path
import time

import sympy as sp
from scipy.integrate import quad


def local(name, filename):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ac = local('r22_anomaly_prior', 'anomaly_completion.py')
hs = ac.hs
cd = local('r22_forms_prior', 'charged_domain.py')
ZETA = (-1+sp.I*sp.sqrt(3))/2
PERIPHERAL_WORDS = (('bbAbA', 'bba'), ('bbAb', 'AAbAb'))


@lru_cache(maxsize=None)
def source_pair(q, k=3, source_orientation=1):
    """One chosen CPT representative; reversal changes the source, not q."""
    if not isinstance(q, int) or q == 0:
        raise ValueError('nonzero integral gauge charge required; beta >= 1 is assumed')
    if not isinstance(k, int) or k < 1 or source_orientation not in (-1, 1):
        raise ValueError('positive source count and a declared common source orientation required')
    # Three residue classes suffice for ALL integer charges, not a scan bound.
    x = sp.simplify(sp.expand_complex(ZETA**(q % 3)))
    y = sp.conjugate(x)
    cochains = hs.cochains(x, y, k=k)
    positive = cochains['relative_T']
    negative = cochains['relative_E_dual']
    current = positive if q*source_orientation > 0 else negative
    conjugate = negative if q*source_orientation > 0 else positive
    return dict(q=q, k=k, source_orientation=source_orientation,
                residue=q % 3, polynomial=cochains['polynomial'],
                betti=current, conjugate_betti=conjugate,
                net_H1=current[1]-conjugate[1],
                independent_euler=-sum((-1)**j*n for j, n in enumerate(current)),
                differential_ranks=cochains['differential_ranks'])


def weighted_anomaly(weights, k=3, orientations=None):
    orientations = {} if orientations is None else orientations
    answer = sp.Integer(0)
    for w in weights:
        q = w[0]
        if not q.is_Integer or q == 0:
            raise ValueError('this helper covers nonzero integral charged CPT pairs')
        index = source_pair(int(q), k, orientations.get(int(q), 1))['net_H1']
        answer += ac.anomaly([w], index)
    return sp.expand(answer)


@lru_cache(maxsize=1)
def supply():
    d = ac.data()
    weights = d['spinor']+d['vector']+d['singlet']
    out = weighted_anomaly(weights)
    expected = ac.anomaly(d['spinor']+[-w for w in d['vector']]+d['singlet'], 3)
    linear = sum(source_pair(int(w[0]))['net_H1']*w[0] for w in weights)
    cubic = sum(source_pair(int(w[0]))['net_H1']*w[0]**3 for w in weights)
    labels = lambda w: (d['C']*w)[1:, :]
    mixed = sum((source_pair(int(w[0]))['net_H1']*w[0]*labels(w)*labels(w).T
                 for w in weights), sp.zeros(5))
    vector_quadratic = sum((labels(w)*labels(w).T for w in d['vector']), sp.zeros(5))
    i, j = next((i, j) for i in range(5) for j in range(5) if vector_quadratic[i, j])
    ratio = sp.cancel(mixed[i, j]/vector_quadratic[i, j])
    return dict(charge_rows=[source_pair(q) for q in (-12, -6, -4, -3, -2, -1, 1, 2, 3, 4, 6, 12)],
                component_controls=[source_pair(q, k) for k in (1, 2, 4) for q in (-3, -2, -1, 1, 2, 3)],
                bulk_anomaly=out, expected_weight_polynomial=expected,
                full_polynomial_match=sp.expand(out-expected) == 0,
                original_added_field_polynomial=ac.anomaly(weights, 3),
                mixed_gravity_trace=linear, cubic_u_trace=cubic,
                mixed_spin10_u=ratio, mixed_matrix_match=mixed == ratio*vector_quadratic,
                CPT_representative_invariance=weighted_anomaly([-w for w in weights]) == out,
                reversed_source=-out == weighted_anomaly(weights, orientations={1: -1, -2: -1, 4: -1}),
                independent_vector_source_restores_zero=weighted_anomaly(weights, orientations={-2: -1}) == 0,
                absolute_charge_trace=3*sum(abs(w[0]) for w in weights),
                absolute_cubic_trace=3*sum(abs(w[0])**3 for w in weights))


def exponent_sum(word):
    return tuple(sum((1 if letter.islower() else -1) for letter in word if letter.lower() == g)
                 for g in ('a', 'b'))


def peripheral(q):
    if not isinstance(q, int):
        raise ValueError('integral charge required')
    classes = [[exponent_sum(word) for word in pair] for pair in PERIPHERAL_WORDS]
    phases = [[sp.Rational(q*(a+2*b), 3) % 1 for a, b in pair] for pair in classes]
    # Square flat torus CONTROL: coordinate-wise nearest integer is complete.
    gaps = [sum(min(alpha, 1-alpha)**2 for alpha in pair) for pair in phases]
    enumerated = [min(sum((sp.Integer(n)+alpha)**2 for n, alpha in zip(ns, pair))
                      for ns in itertools.product((-1, 0), repeat=2)) for pair in phases]
    return dict(q=q, relator_exponents=exponent_sum(hs.RELATOR), classes=classes,
                phases=phases, square_torus_gap_over_4pi2=gaps,
                nearest_lattice_control=gaps == enumerated,
                nontrivial_cusps=[any(alpha != 0 for alpha in pair) for pair in phases])


@lru_cache(maxsize=1)
def cusp_identities():
    s = sp.Symbol('s', real=True)
    x, eta, X = sp.symbols('x eta X', positive=True)
    q, b, c = sp.symbols('q b c', real=True)
    a = sp.exp(-eta*sp.exp(2*s))
    h = sp.exp(2*s)*(b*s+c)
    volume = sp.exp(-2*s)
    radial = volume*(sp.diff(a, s)+q*sp.diff(h, s)*a)**2
    change = lambda v: sp.simplify(v.subs(s, sp.log(x)/2)/(2*x))
    d = q*(b+2*c)-2*eta
    expected_radial = sp.exp(-2*eta*x)*(q*b*sp.log(x)+d)**2/2
    J0 = sp.exp(-2*eta*X)/(2*eta)
    J1 = sp.exp(-2*eta*X)*(X/(2*eta)+1/(4*eta**2))
    # Bounds follow from log(x)^2 <= x on x>=1 and (u+v)^2<=2u^2+2v^2.
    bound = q*q*b*b*J1+d*d*J0
    ratio = sp.log(x)**2/x
    return dict(radial_change=sp.simplify(change(radial)-expected_radial) == 0,
                norm_change=sp.simplify(change(volume*a*a)-sp.exp(-2*eta*x)/(2*x*x)) == 0,
                transverse_change=sp.simplify(change(a*a)-sp.exp(-2*eta*x)/(2*x)) == 0,
                no_cusp_volume_factor_transverse=sp.simplify(volume*sp.exp(2*s)) == 1,
                radial_integrand=expected_radial, radial_bound=bound,
                norm_bound=J0/(2*X*X), transverse_bound=J0/(2*X),
                elementary_tail_checks=[sp.simplify(sp.diff(J0, X)+sp.exp(-2*eta*X)) == 0,
                                       sp.simplify(sp.diff(J1, X)+X*sp.exp(-2*eta*X)) == 0],
                logarithm_ratio_derivative=sp.factor(sp.diff(ratio, x)),
                logarithm_ratio_at_max=sp.simplify(ratio.subs(x, sp.exp(2))),
                constant_amplitude_norm=sp.exp(-2*s)/2,
                constant_amplitude_transverse_primitive=s)


def cusp_integral_controls():
    rows = []
    for q, b, c, eta, X in ((4, .7, -.2, .3, 1.), (-4, .7, -.2, .3, 1.),
                          (4, 1., 2., 1., 2.), (-1, 2., -.7, .5, 4.),
                          (0, 1., 1., .4, 1.)):
        d = q*(b+2*c)-2*eta
        integrands = (lambda x: .5*math.exp(-2*eta*x)/x**2,
                      lambda x: .5*math.exp(-2*eta*x)*(q*b*math.log(x)+d)**2,
                      lambda x: .5*math.exp(-2*eta*x)/x)
        values = [quad(f, X, math.inf, epsabs=1e-12, epsrel=1e-12) for f in integrands]
        J0 = math.exp(-2*eta*X)/(2*eta)
        J1 = math.exp(-2*eta*X)*(X/(2*eta)+1/(4*eta**2))
        bounds = (J0/(2*X*X), q*q*b*b*J1+d*d*J0, J0/(2*X))
        rows.append(dict(q=q, b=b, c=c, eta=eta, X=X, integrals=[v for v, err in values],
                         quadrature_error_estimates=[err for v, err in values], bounds=bounds,
                         controls_pass=all(0 < v <= bound+1e-11 for (v, err), bound in zip(values, bounds))))
    return rows


@lru_cache(maxsize=1)
def current_controls():
    s = sp.Symbol('s', real=True)
    A, Ap, App, f, fp, q, k, g, W = sp.symbols('A Ap App f fp q k g W', real=True)
    lagrangian = Ap*Ap/(2*g*g)+sp.exp(-2*s)*fp*fp+(k-q*A)**2*f*f+sp.exp(-2*s)*W*f*f
    equation = sp.diff(lagrangian, A)-sp.diff(lagrangian, Ap, 2)*App
    expected = -App/g**2+2*q*(q*A-k)*f*f
    alpha = sp.Rational(1, 3)
    single = equation.subs({App: 0, q: 4, A: alpha/4, k: 0})
    j0 = (2*q*(q*A-k)*f*f).subs({q: 4, A: alpha/4, k: 0, f: sp.sqrt(2)*f})
    j1 = (2*q*(q*A-k)*f*f).subs({q: 4, A: alpha/4, k: 1})
    x = sp.Symbol('x', real=True)
    wave = sp.sin(x/2)
    # The real antiperiodic wave is a circle control, not a global cusp vacuum.
    wave_current = sp.im(sp.conjugate(wave)*sp.diff(wave, x))
    a, b, da, db = sp.symbols('a b da db', real=True)
    cartesian = (da+q*A*b)**2+(db-q*A*a)**2
    return dict(cusp_lagrangian=lagrangian, maxwell_equation=equation,
                equation_match=sp.expand(equation-expected) == 0,
                flat_order_three_current=single, single_current_nonzero=single != 0,
                local_current=sp.diff(cartesian, A).subs(A, 0),
                real_wave_current=wave_current,
                real_wave_antiperiodic=sp.simplify(wave.subs(x, x+2*sp.pi)+wave) == 0,
                real_wave_nonparallel=sp.diff(wave, x) != 0,
                real_wave_elliptic_equation=sp.simplify(-sp.diff(wave, x, 2)-wave/4) == 0,
                two_field_opposite_currents=[j0, j1], two_field_current_cancels=sp.simplify(j0+j1) == 0,
                neutral_current=sp.diff(lagrangian, A).subs(q, 0),
                compatible_phase_current=sp.diff(lagrangian, A).subs(k, q*A),
                nonreal_order_three_holonomy=sp.im(ZETA) != 0)


@lru_cache(maxsize=1)
def curved_differential():
    r, x, y = cd.COORDS
    q = sp.Symbol('q', real=True)
    A = {(1,): r}
    dF = cd.exterior({(): r*r+x*y})
    eta = cd.add(cd.scale(A, -sp.I*q), cd.scale(dF, q))
    def D(v):
        return cd.add(cd.exterior(v), cd.wedge(eta, v))
    curvature = cd.exterior(A)
    rows = []
    for indices in cd.BASIS:
        v = {indices: 1+r+x+y}
        square = D(D(v))
        target = cd.scale(cd.wedge(curvature, v), -sp.I*q)
        rows.append(dict(indices=indices, square=square,
                         curvature_identity=cd.add(square, cd.scale(target, -1)) == {}))
    flat_eta = cd.add({(1,): -sp.I*q}, cd.scale(dF, q))
    def Dflat(v):
        return cd.add(cd.exterior(v), cd.wedge(flat_eta, v))
    return dict(rows=rows, zero_form_square_nonzero=D(D({(): sp.Integer(1)})) != {},
                flat_all_degrees=all(Dflat(Dflat({j: 1+r+x+y})) == {} for j in cd.BASIS))


def run():
    start = time.monotonic()
    result = dict(supply=supply(), peripheral=[peripheral(q) for q in (0, 1, -2, 4, 12)],
                  cusp=cusp_identities(), cusp_integrals=cusp_integral_controls(),
                  current=current_controls(), differential=curved_differential())
    result['runtime_seconds'] = time.monotonic()-start
    return ac.serial(result)


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True))
