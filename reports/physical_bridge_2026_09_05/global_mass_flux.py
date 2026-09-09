"""R24: exact spin/angular identities and controls for the total boundary flux.

The general smooth-boundary theorem and exhaustion proof are stated in the
design/report, not inferred from the finite product-model cell controls.
No pointwise mesh solution, isolated-critical-point census or end QFT.
"""
from __future__ import annotations

from functools import lru_cache
import itertools
import json
import time

import sympy as sp

from pathlib import Path
import importlib.util


def local(name, filename):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


mass = local('r24_mass', 'mass_inflow.py')
source = local('r24_source', 'global_singular.py')
SIGMA = mass.PAULI


def clean(x):
    return sp.cancel(sp.expand(x))


def clean_matrix(A):
    return A.applyfunc(clean)


def hat(v):
    return sp.Matrix([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])


def pauli(v):
    return sum((v[i]*SIGMA[i] for i in range(3)), sp.zeros(2))


@lru_cache(maxsize=1)
def spin_connection_bridge():
    a = sp.symbols('a0:3', real=True)
    creation, annihilation, _, _ = mass.form_matrices()
    natural = sp.zeros(4)
    for k, i, j in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
        generator = creation[i]*annihilation[j]-creation[j]*annihilation[i]
        natural -= a[k]*generator.extract(mass.EVEN, mass.EVEN)
    U = mass.clifford_map()['U']
    spin = -sp.I*pauli(a)/2
    expected = sp.kronecker_product(spin, sp.eye(2))+sp.kronecker_product(sp.eye(2), spin)
    mapped = clean_matrix(U.H*natural*U)
    m = sp.symbols('m0:3', real=True)
    texture = sum((m[i]*mass.clifford_map()['T'][i] for i in range(3)), sp.zeros(4))
    return dict(connection_matches=mapped == expected,
                missing_second_factor_rejected=mapped != sp.kronecker_product(spin, sp.eye(2)),
                wrong_spin_sign_rejected=mapped != -expected,
                mass_on_second_factor=clean_matrix(U.H*texture*U) == sp.kronecker_product(sp.eye(2), pauli(m)),
                antihermitian=natural.H == -natural, mapped_connection=mapped)


def chern_coefficient(n, n_u, n_v, a, b, c):
    """Actual projector curvature, coefficient of du wedge dv.

    a,b are spin-connection vectors in the u,v directions; c is the
    derivative jet partial_u b-partial_v a, NOT the full curvature.
    """
    n, n_u, n_v, a, b, c = map(sp.Matrix, (n, n_u, n_v, a, b, c))
    P = (sp.eye(2)+pauli(n))/2
    ga, gb = -sp.I*pauli(a)/2, -sp.I*pauli(b)/2
    dp_u = pauli(n_u)/2+ga*P-P*ga
    dp_v = pauli(n_v)/2+gb*P-P*gb
    curvature = -sp.I*pauli(c)/2+ga*gb-gb*ga
    curved = clean(sp.I*sp.trace(P*curvature)/(2*sp.pi))
    projected = clean(sp.I*sp.trace(P*(dp_u*dp_v-dp_v*dp_u))/(2*sp.pi))
    return dict(K=clean(curved+projected), curvature_part=curved,
                projector_part=projected, curvature=clean_matrix(curvature),
                DP_u=clean_matrix(dp_u), DP_v=clean_matrix(dp_v))


@lru_cache(maxsize=1)
def angular_identity():
    u, v = sp.symbols('u v', real=True)
    d = 1+u*u+v*v
    n = sp.Matrix([2*u/d, 2*v/d, (1-u*u-v*v)/d])
    a, b, c = [sp.Matrix(sp.symbols(prefix+'0:3', real=True)) for prefix in ('a', 'b', 'c')]
    row = chern_coefficient(n, n.diff(u), n.diff(v), a, b, c)
    f = c+a.cross(b)
    du, dv = n.diff(u)+a.cross(n), n.diff(v)+b.cross(n)
    expected = clean((n.dot(f)-n.dot(du.cross(dv)))/(4*sp.pi))
    tangent_curvature = hat(c)+hat(a)*hat(b)-hat(b)*hat(a)
    paper_curvature = -tangent_curvature  # Nie (2.2)-(2.3): ROW rather than COLUMN.
    phi0, phi1 = 0, 0
    for p in itertools.permutations(range(3)):
        i, j, k = p
        eps = mass.permutation_sign(p)
        phi0 += eps*n[i]*(du[j]*dv[k]-dv[j]*du[k])
        phi1 += eps*n[i]*paper_curvature[j, k]
    phi = clean((phi0-phi1)/(8*sp.pi))
    flat = clean(row['K'].subs({x: 0 for x in list(a)+list(b)+list(c)}))
    reversed_row = chern_coefficient(-n, -n.diff(u), -n.diff(v), a, b, c)
    P = (sp.eye(2)+pauli(n))/2
    return dict(unit_identity=clean(n.dot(n)-1),
                projector_identity=clean_matrix(P*P-P) == sp.zeros(2),
                spin_curvature_identity=clean_matrix(row['curvature']+sp.I*pauli(f)/2) == sp.zeros(2),
                tangent_curvature_identity=clean_matrix(tangent_curvature-hat(f)) == sp.zeros(3),
                pauli_to_vector_residual=clean(row['K']-expected),
                K_plus_Phi=clean(row['K']+phi), K=row['K'], Phi=phi,
                reversed_sum=clean(reversed_row['K']+row['K']),
                wrong_angular_sign_rejected=clean(row['K']-phi) != 0,
                omitted_curvature_rejected=clean(row['projector_part']-expected) != 0,
                flat_stereographic=flat,
                flat_residual=clean(flat+1/(sp.pi*d*d)))


@lru_cache(maxsize=1)
def sphere_control():
    r = sp.Symbol('r', nonnegative=True)
    integral = sp.integrate(-2*r/(1+r*r)**2, (r, 0, sp.oo))
    old = mass.angular_form()
    return dict(stereographic_flux=integral, spherical_flux=old['sphere_flux'],
                reverse_flux=-integral, constant_mass_flux=0)


@lru_cache(maxsize=1)
def hyperbolic_control():
    x, y, z = sp.symbols('x y z', real=True, positive=True)
    coords = (x, y, z)
    e = [{(i,): 1/z} for i in range(3)]
    # ds^2=(dx^2+dy^2+dz^2)/z^2: a=(dy/z,-dx/z,0).
    avec = [e[1], mass.cd.scale(e[0], -1), {}]
    torsion = []
    for i in range(3):
        row = mass.exterior(e[i], coords)
        for j in range(3):
            Aij = mass.cd.add(*(mass.cd.scale(avec[k], -sp.LeviCivita(i, j, k)) for k in range(3)))
            row = mass.cd.add(row, mass.cd.wedge(Aij, e[j]))
        torsion.append(row)
    zero = sp.zeros(3, 1)
    vertical = sp.Matrix([0, 0, 1])
    row = chern_coefficient(vertical, zero, zero,
                            sp.Matrix([0, -1/z, 0]), sp.Matrix([1/z, 0, 0]), zero)
    return dict(torsion=torsion, K=row['K'], curvature_part=row['curvature_part'],
                projector_part=row['projector_part'],
                omitted_curvature=row['projector_part'], omitted_covariant_DP=row['curvature_part'])


@lru_cache(maxsize=1)
def corner_control():
    a, b, delta = sp.symbols('a b delta', positive=True)
    c, t = sp.symbols('c t', real=True)
    curve = sp.Matrix([delta*(1-sp.cos(t)), delta*(1-sp.sin(t)), 0])
    normal = sp.Matrix([-sp.cos(t), -sp.sin(t), 0])
    tangent = sp.Matrix([sp.sin(t), -sp.cos(t), 0])
    V = sp.Matrix([a, -b, c])
    nv, tv = normal.dot(V), tangent.dot(V)
    root = {sp.cos(t): b/sp.sqrt(a*a+b*b), sp.sin(t): a/sp.sqrt(a*a+b*b)}
    at_crossing = sp.simplify(tv.subs(root))
    return dict(normal_pairing=nv, tangent_pairing=tv,
                curve_orientation=sp.simplify(curve.diff(t)-delta*tangent) == sp.zeros(3, 1),
                normal_endpoints=[nv.subs(t, 0), nv.subs(t, sp.pi/2)],
                positive_normal_derivative=sp.simplify(sp.diff(nv, t)-tv) == 0,
                normal_at_crossing=sp.simplify(nv.subs(root)),
                q_positive_outward_tangent=at_crossing,
                q_negative_outward_tangent=sp.simplify((-tangent).dot(-V).subs(root)),
                wrong_negative_region_sign=sp.simplify(tangent.dot(-V).subs(root)),
                nonzero_normal_plane_norm=a*a+b*b,
                positive_cone_homotopy_required=True)


def topological_prediction(k, sign=1):
    if not isinstance(k, int) or isinstance(k, bool) or k < 0 or sign not in (-1, 1):
        raise ValueError('a nonnegative integer arc count and a nonzero charge sign required')
    chi_Q, chi_N, chi_T = 0, k, 0
    chi_C = chi_Q-chi_N+chi_T
    chi_E = -2*k
    incoming = chi_T if sign == 1 else chi_E
    index = chi_C-incoming
    return dict(k=k, sign=sign, chi_Q=chi_Q, chi_N=chi_N, chi_T=chi_T,
                chi_C=chi_C, chi_E=chi_E, incoming_chi=incoming,
                vector_index=index, mass_flux=-index,
                unexcised_core_mutant_flux=-(chi_Q-incoming))


@lru_cache(maxsize=None)
def cellular_control(k, n=6, height=1):
    row = source.cellular_pair(k, n, height)
    chi = {key: row[key]['chi'] for key in ('Q', 'C', 'T', 'E', 'boundary_C', 'relative_T', 'relative_E')}
    ranks = {key: row[key]['betti'] for key in ('C', 'T', 'E', 'relative_T', 'relative_E')}
    return dict(k=k, n=n, height=height, chi=chi, betti=ranks,
                q_positive_flux=chi['T']-chi['C'], q_negative_flux=chi['E']-chi['C'],
                cochain_positive_flux=-chi['relative_T'], cochain_negative_flux=-chi['relative_E'],
                interpretation='product-model cochains, not the actual manifold triangulation')


def ball_controls():
    flux = sphere_control()['stereographic_flux']
    # For the constant field on B3, the incoming hemisphere is a disc.
    # Radial outward/inward fields have empty/full incoming S2.
    return [dict(field='constant', chi_core=1, chi_incoming=1, actual_flux=0),
            dict(field='radial_outward', chi_core=1, chi_incoming=0, actual_flux=flux),
            dict(field='radial_inward', chi_core=1, chi_incoming=2, actual_flux=-flux)]


@lru_cache(maxsize=1)
def cutoff_controls():
    s = sp.Symbol('s', real=True)
    b, beta = sp.symbols('b beta', positive=True)
    C, D, B, t = sp.symbols('C D B t', nonnegative=True)
    c = sp.Symbol('c', real=True)
    lead = sp.exp(2*s)*(b*s+c)
    scaled_derivative = sp.simplify(sp.exp(-2*s)*sp.diff(lead, s))
    # For s>=0 and |dv/ds|<=D the scaled error is >=-D;
    # |c|<=C and s>=(2C+D)/(2b) give the following strict lower bound.
    floor = (2*C+D)/(2*b)
    margin = sp.expand((2*b*s+b-2*C-D).subs(s, floor+t))
    radius = beta/(B+1)
    tube_margin = sp.simplify(beta/radius-B)
    # A fixed radius cannot dominate every bound B(S) as S grows.
    fixed_radius_margins = [1-sp.Integer(S)**2 for S in (1, 2, 4)]
    return dict(scaled_leading_derivative=scaled_derivative,
                cap_height_floor=floor, cap_scaled_lower_bound=margin,
                tube_radius_upper_bound=radius, tube_derivative_lower_bound=tube_margin,
                zero_b_negative_c=scaled_derivative.subs({b: 0, c: -1}),
                fixed_radius_counter_margins=fixed_radius_margins,
                cutoff_order='cap first, then sufficiently small tubes, then corner collars',
                bounds_are_existence_parameters_not_computed_corrector_values=True)


@lru_cache(maxsize=1)
def actual_anomaly_join():
    flux = cellular_control(3)['q_positive_flux']
    forms = mass.anomaly_forms()
    spinor = mass.ac.data()['spinor']
    return dict(boundary_flux=flux, one_I6=forms['one_I6'], boundary_I6=sp.expand(flux*forms['one_I6']),
                previous_three_I6=forms['three_I6'],
                linear_trace=flux*sum(w[0] for w in spinor),
                cubic_trace=flux*sum(w[0]**3 for w in spinor),
                constant_parameter_balance=mass.boundary_balance([int(flux)], [1], 1),
                no_isolated_zero_census=True, no_boundary_quantum_completion=True)


def run():
    started = time.monotonic()
    out = dict(spin_connection=spin_connection_bridge(), angular=angular_identity(),
               sphere=sphere_control(), hyperbolic=hyperbolic_control(), corner=corner_control(),
               topology=[topological_prediction(k, q) for k in (0, 1, 2, 3, 5) for q in (-1, 1)],
               cells=[cellular_control(k) for k in range(4)]+[cellular_control(3, 8, 2)],
               ball=ball_controls(), cutoffs=cutoff_controls(), anomaly=actual_anomaly_join())
    out['runtime_seconds'] = time.monotonic()-started
    out['scope'] = 'exact local identities and finite controls of an analytic total-flux theorem; not a complete quantum boundary theory'
    return out


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True, default=str), flush=True)
