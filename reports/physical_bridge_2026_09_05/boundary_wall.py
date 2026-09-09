"""R25 free reference wall: actual chirality, eigenline, index and charge.

An added collar ansatz, not a selected physical defect or full determinant.
See BOUNDARY_WALL_DESIGN.md for the order of limits and analytic inputs.
"""
from functools import lru_cache
import importlib.util
import itertools
import json
from pathlib import Path
import time

import sympy as sp

SPEC = importlib.util.spec_from_file_location('r25_bundle', Path(__file__).with_name('mass_inflow_bundle_control.py'))
bundle = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(bundle)
m = bundle.m
S = m.PAULI
I = sp.I
K = bundle.K


def zero(A):
    return A.applyfunc(lambda x: sp.simplify(sp.expand_complex(x))) == sp.zeros(*A.shape)


@lru_cache(maxsize=1)
def chirality_bridge():
    g4 = [sp.kronecker_product(S[0], sp.eye(2)), sp.kronecker_product(S[1], sp.eye(2)),
          sp.kronecker_product(S[2], S[0]), sp.kronecker_product(S[2], S[1])]
    chi4 = -sp.prod(g4)
    g7 = [sp.kronecker_product(g, sp.eye(2)) for g in g4]
    g7 += [sp.kronecker_product(chi4, s) for s in S]
    chi6 = I*sp.prod(g7[:6])
    right = [i for i in range(4) if chi4[i, i] == -1]
    right_internal = [g.extract([2*i+j for i in right for j in range(2)],
                               [2*i+j for i in right for j in range(2)]) for g in g7[4:]]
    r23 = m.clifford_map()
    return dict(clifford=all(zero(a*b+b*a-2*int(i == j)*sp.eye(8))
                             for i, a in enumerate(g7) for j, b in enumerate(g7)),
                chi4=chi4, chi6=chi6, normal=g7[-1],
                boundary_chirality=zero(chi6-g7[-1]),
                right_internal_matches=[zero(g+sp.kronecker_product(sp.eye(2), s))
                                        for g, s in zip(right_internal, S)],
                r23_kinetic_matches=[zero(g+sp.kronecker_product(s, sp.eye(2)))
                                     for g, s in zip(r23['kinetic_map'], S)],
                factorization=zero(chi6-sp.kronecker_product(chi4, S[2])),
                normal_positive_rank=((sp.eye(8)+g7[-1])/2).rank(),
                reversed_boundary_sign_rejected=not zero(chi6+g7[-1]))


def scalar_crossing(left, right):
    if left not in (-1, 1) or right not in (-1, 1):
        raise ValueError('two nonzero asymptotic mass signs required')
    # exp(-gamma * integral mass dr) must decay at BOTH infinities.
    chiralities = [c for c in (-1, 1) if c*left < 0 and c*right > 0]
    return dict(left=left, right=right, normalizable_chiralities=chiralities)


@lru_cache(maxsize=1)
def smooth_normal():
    s = sp.Symbol('s', real=True)
    a, ell = sp.symbols('a ell', positive=True)
    f = sp.cosh(s)**(-a)
    residual = sp.simplify((sp.diff(f, s)+a*sp.tanh(s)*f)/f)
    opposite = sp.simplify((-sp.diff(f, s)+a*sp.tanh(s)*f)/f)
    t = sp.Symbol('t', real=True)
    controls = []
    for n in (1, 2, 3, 4):
        integral = sp.integrate((1-t*t)**(n-1), (t, -1, 1))
        gamma_formula = sp.sqrt(sp.pi)*sp.gamma(n)/sp.gamma(sp.Rational(1, 2)+n)
        controls.append(dict(a=n, integral=integral, gamma_formula=sp.simplify(gamma_formula),
                             difference=sp.simplify(integral-gamma_formula)))
    return dict(profile=f, dimensionless_mass=a*sp.tanh(s), residual=residual,
                opposite_residual=opposite,
                right_log_slope=sp.limit(sp.diff(f, s)/f, s, sp.oo),
                left_log_slope=sp.limit(sp.diff(f, s)/f, s, -sp.oo),
                normal_norm=ell*sp.sqrt(sp.pi)*sp.gamma(a)/sp.gamma(a+sp.Rational(1, 2)),
                beta_integrand=(1-t*t)**(a-1), integer_integrals=controls,
                scalar_trace=1+sp.tanh(s), identity_mass_coefficient=(1+sp.tanh(s))/2,
                trace_inside=sp.limit(1+sp.tanh(s), s, -sp.oo),
                trace_outside=sp.limit(1+sp.tanh(s), s, sp.oo))


@lru_cache(maxsize=1)
def projected_connection():
    theta, phi, h = sp.symbols('theta phi h', real=True)
    n = sp.Matrix([sp.sin(theta)*sp.cos(phi), sp.sin(theta)*sp.sin(phi), sp.cos(theta)])
    P = (sp.eye(2)+sum((n[i]*S[i] for i in range(3)), sp.zeros(2)))/2
    Q = sp.eye(2)-P
    u = sp.Symbol('u', real=True)
    wall = P+u*Q
    v = sp.Matrix([-sp.exp(-I*phi)*sp.sin(theta/2), sp.cos(theta/2)])
    A = -I*h*sp.cos(theta)*S[2]/2
    def curvature(projector):
        dt = projector.diff(theta)
        dp = projector.diff(phi)+A*projector-projector*A
        return sp.simplify(sp.expand_complex(I*sp.trace(projector*A.diff(theta)+projector*(dt*dp-dp*dt))/(2*sp.pi)))
    conn_t = sp.simplify((v.H*v.diff(theta))[0])
    conn_p = sp.simplify(sp.expand_complex((v.H*(v.diff(phi)+A*v))[0]))
    direct = sp.simplify(I*(sp.diff(conn_p, theta)-sp.diff(conn_t, phi))/(2*sp.pi))
    minus, plus = curvature(Q), curvature(P)
    return dict(unit_vector=sp.simplify((v.H*v)[0]), negative_projector=zero(v*v.H-Q),
                actual_wall_trace=sp.simplify(sp.trace(wall)),
                wall_inside=zero(wall.subs(u, -1)-(2*P-sp.eye(2))),
                wall_outside=zero(wall.subs(u, 1)-sp.eye(2)),
                negative_mass_eigenvector=zero((2*P-sp.eye(2))*v+v),
                direct_curvature=direct, projector_curvature=minus,
                independent_residual=sp.simplify(direct-minus),
                complementary_residual=sp.simplify(minus+plus),
                omitted_connection_difference=sp.simplify(direct-direct.subs(h, 0)),
                off_diagonal_derivative_nonzero=not zero(P*Q.diff(theta)*Q),
                flat_sphere_minus_flux=sp.integrate(minus.subs(h, 0), (theta, 0, sp.pi), (phi, 0, 2*sp.pi)))


def surface_index(total_K, genus, reference=1):
    if not isinstance(total_K, int) or not isinstance(genus, int) or genus < 0 or reference not in (-1, 1):
        raise ValueError('integral flux, nonnegative integral genus, signed reference required')
    line_degree = -reference*total_K
    spin_degree = genus-1
    return dict(total_K=total_K, genus=genus, reference=reference,
                six_chirality=reference, eigenline_degree=line_degree,
                spin_degree=spin_degree, holomorphic_degree=line_degree+spin_degree,
                spin_index=line_degree+spin_degree+1-genus,
                four_index=reference*(line_degree+spin_degree+1-genus),
                spin_omission=line_degree+1-genus)


def sphere_sections(degree):
    if not isinstance(degree, int):
        raise ValueError('integral monopole degree required')
    # Cech H0(O(j)) has monomials 0..j; H1 has Laurent powers j+1..-1.
    j = degree-1  # spin bundle O(-1) MUST be included
    h0_basis = list(range(0, j+1)) if j >= 0 else []
    h1_basis = list(range(j+1, 0)) if j <= -2 else []
    return dict(degree=degree, h0_monomials=h0_basis, h1_laurent_powers=h1_basis,
                index=len(h0_basis)-len(h1_basis))


@lru_cache(maxsize=1)
def anomaly_join():
    b = bundle.characteristic_forms()
    forms = b['forms']
    weights = m.ac.data()['spinor']
    ell = [(w.T*m.ac.Z)[0] for w in weights]
    p1, p2 = m.ac.P1, sp.Symbol('p2_T')
    edge = sp.expand(sum((x-K)**4/24-p1*(x-K)**2/48 for x in ell)
                     +len(ell)*(7*p1*p1-4*p2)/5760)
    negative_reference = sp.expand(-edge.subs(K, -K))
    k = sp.Symbol('k', integer=True)
    reduced = k*sp.Poly(edge, K).nth(1)
    reversed_reduced = k*sp.Poly(negative_reference, K).nth(1)
    charged = m.anomaly_forms()
    return dict(edge8=edge, full_cancellation=sp.expand(edge+b['B8']),
                missing_higher_terms=sp.expand(edge-(forms[8]-K*forms[6])),
                reduced4=sp.expand(reduced), reduced_residual=sp.expand(reduced+k*forms[6]),
                reversed_reference_residual=sp.expand(reversed_reduced-reduced),
                three_spinor_residual=sp.expand(reduced.subs(k, 3)+charged['three_I6']),
                three_linear=3*charged['one_linear_trace'], three_cubic=3*charged['one_cubic_trace'],
                constant_bulk=m.boundary_balance([1, 1, 1], [1, 1, 1], 1),
                compact_bulk=m.boundary_balance([1, 1, 1], [1, 1, 1], 0))


@lru_cache(maxsize=1)
def localization_controls():
    x = sp.Symbol('x', real=True)
    M, R, V, g7 = sp.symbols('M R V g7', positive=True)
    # f0*fR, integrated independently in the three sign regions.
    overlap = sum([sp.integrate(M*sp.exp(-M*(R-2*x)), (x, -sp.oo, 0)),
                   sp.integrate(M*sp.exp(-M*R), (x, 0, R)),
                   sp.integrate(M*sp.exp(-M*(2*x-R)), (x, R, sp.oo))])
    norm = sp.integrate(M*sp.exp(2*M*(x-R)), (x, -sp.oo, R))
    norm += sp.integrate(M*sp.exp(-2*M*(x-R)), (x, R, sp.oo))
    # s0=0 by translation; wall at R>0; fixed observation interval [0,A], R>A.
    A = sp.Symbol('A', positive=True)
    raw_half_norm = sp.integrate(M*sp.exp(-2*M*(R-x)), (x, 0, R))
    raw_half_norm += sp.integrate(M*sp.exp(-2*M*(x-R)), (x, R, sp.oo))
    local_probability = sp.integrate(M*sp.exp(-2*M*(R-x)), (x, 0, A))/raw_half_norm
    measure_cancellation = sp.exp(-2*x)*(sp.exp(x))**2
    # A localized gauge profile is a contrasting theory: exp(-M|x|).
    localized_gauge = sp.integrate(M*sp.exp(-2*M*(R-x)+M*x), (x, -sp.oo, 0))
    localized_gauge += sp.integrate(M*sp.exp(-2*M*(R-x)-M*x), (x, 0, R))
    localized_gauge += sp.integrate(M*sp.exp(-2*M*(x-R)-M*x), (x, R, sp.oo))
    return dict(norm=sp.simplify(norm), overlap=sp.simplify(overlap),
                overlap_limit=sp.limit(overlap, R, sp.oo),
                constant_coupling=sp.simplify(g7*norm/sp.sqrt(V)),
                constant_coupling_R_derivative=sp.diff(g7*norm/sp.sqrt(V), R),
                half_norm=sp.simplify(raw_half_norm), cusp_measure_cancellation=sp.simplify(measure_cancellation),
                normalized_half_norm=sp.simplify(raw_half_norm/raw_half_norm),
                local_probability=sp.simplify(local_probability), local_escape=sp.limit(local_probability, R, sp.oo),
                localized_gauge=sp.simplify(localized_gauge), localized_gauge_limit=sp.limit(localized_gauge, R, sp.oo),
                volume_divergence_control=sp.limit(g7/sp.sqrt(V), V, sp.oo))


def run():
    start = time.monotonic()
    result = dict(scope='added free reference wall, compact-surface effective index and conditional gauge coupling; not selected defect or full singular determinant',
                  clifford=chirality_bridge(), normal=smooth_normal(),
                  sign_controls=[scalar_crossing(a, b) for a, b in itertools.product((-1, 1), repeat=2)],
                  connection=projected_connection(),
                  indices=[surface_index(k, g, r) for k in (-3, -1, 0, 1, 3) for g in (0, 1, 4) for r in (-1, 1)],
                  spheres=[sphere_sections(d) for d in range(-4, 5)],
                  anomaly=anomaly_join(), localization=localization_controls())
    result['seconds'] = time.monotonic()-start
    return result


if __name__ == '__main__':
    print(json.dumps(m.serial(run()), indent=2), flush=True)
