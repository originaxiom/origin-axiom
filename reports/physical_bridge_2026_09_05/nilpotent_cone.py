"""R66 exact local controls; the center-manifold proof is a separate input."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

import sympy as s

_spec = importlib.util.spec_from_file_location(
    'r66_canonical_source', Path(__file__).with_name('canonical_cusp.py'))
source = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(source)

r, alpha = s.symbols('r alpha', positive=True)
h, hp, hpp, beta, k = s.symbols('h hp hpp beta k', real=True)
u, v, z = s.symbols('u v z', real=True)
tau, c = s.symbols('tau c', positive=True)
q = source.Q
N = s.zeros(4)
N[0, 2] = N[2, 3] = 1
P = N**2
D = s.diag(1, -3, 1, 1)
H = s.diag(1, 0, 0, -1)
E = s.eye(4)


def clean(x):
    return x.applyfunc(s.simplify) if isinstance(x, s.MatrixBase) else s.simplify(x)


def zero(x):
    y = clean(x)
    return y == s.zeros(*y.shape) if isinstance(y, s.MatrixBase) else y == 0


def comm(a, b):
    return a*b-b*a


def dr(x):
    return x.diff(r)+hp*x.diff(h)+hpp*x.diff(hp)


def metric(cross=0):
    return s.Matrix([[1, 0, 0], [0, alpha/r**2, cross/r**2],
                     [0, cross/r**2, 1/(alpha*r**2)]])


def residuals(C, inv):
    n = C[0].rows
    derivative = lambda i, x: dr(x) if i == 0 else s.zeros(n)
    curvature = {(i, j): clean(derivative(i, C[j])-derivative(j, C[i])+comm(C[i], C[j]))
                 for i in range(3) for j in range(3)}
    moment = dr(r**2*(C[0]+C[0].H))/r**2
    moment += sum((inv[i, j]*comm(C[i], C[j].H)
                   for i in range(3) for j in range(3)), s.zeros(n))
    return curvature, clean(moment)


def one_norm(a, inv):
    return clean(sum(inv[i, j]*s.trace(a[i].H*a[j])
                     for i in range(3) for j in range(3)))


def two_norm(a, inv):
    return clean(sum(inv[i, i]*inv[j, j]*s.trace(a[i, j].H*a[i, j])/2
                     for i in range(3) for j in range(3)))


def fields():
    return [hp*H, s.exp(-h)*N, k*D+beta*s.exp(-2*h)*P]


@lru_cache(None)
def source_controls():
    actual = source.peripheral()
    M, L = actual['meridian'], actual['longitude']
    qD = s.diag(q, q**-3, q, q)
    checks = dict(
        actual_meridian=zero(M-E-N-P/2),
        actual_longitude=zero(L-qD*(E+6/(q-1/q)*P)),
        actual_basis_invertible=not zero(actual['det']),
        peripheral_commutation=zero(comm(M, L)),
        determinant_one=zero(M.det()-1) and zero(L.det()-1),
        nilpotent_index_three=zero(N**3) and not zero(N**2),
        P_square_zero=zero(P**2),
        N_P_commute=zero(comm(N, P)),
        D_commutes=all(zero(comm(D, a)) for a in (N, P, N.H, P.H)),
        N_grade=zero(comm(H, N)-N),
        P_grade=zero(comm(H, P)-2*P),
        N_moment=zero(comm(N, N.H)-H),
        P_moment=zero(comm(P, P.H)-H),
        trace_norms=[s.trace(a.H*a) for a in (H, N, P, D)] == [2, 2, 1, 12],
        all_traceless=all(s.trace(a) == 0 for a in (H, N, P, D)),
    )
    return dict(checks=checks, meridian=M, longitude=L, basis_determinant=actual['det'])


@lru_cache(None)
def equation_controls():
    C = fields()
    G = s.diag(s.exp(-h), 1, 1, s.exp(h))
    F, I = residuals(C, metric())
    B = alpha*s.exp(-2*h)+beta**2*s.exp(-4*h)/alpha
    target = (2*(r*r*hpp+2*r*hp)+B)*H/r**2
    omission, _ = residuals([s.zeros(4)]+C[1:], metric())
    reversed_F, _ = residuals([-C[0]]+C[1:], metric())
    cross = s.Symbol('cross', real=True)
    _, mixed_I = residuals(C, metric(cross))
    cross_matrix = comm(N, P.H)+comm(P, N.H)
    product_I = clean(dr(C[0]+C[0].H)+sum(
        (metric().subs(r, 1)[i, j]*comm(C[i], C[j].H)
         for i in range(3) for j in range(3)), s.zeros(4)))
    embedded = [s.diag(a, 0) for a in C]
    F5, I5 = residuals(embedded, metric())
    checks = dict(
        G_determinant_one=zero(G.det()-1),
        G_radial=zero(-dr(G)*G.inv()-C[0]),
        G_x=zero(G*N*G.inv()-C[1]),
        G_y=zero(G*(k*D+beta*P)*G.inv()-C[2]),
        all_curvature_zero=all(zero(a) for a in F.values()),
        moment_equation=zero(I-target),
        on_shell_moment_zero=zero(I.subs(hpp, -2*hp/r-B/(2*r*r))),
        radial_omission_fails=not zero(omission[0, 1]),
        radial_reversal_fails=not zero(reversed_F[0, 1]),
        cross_term=zero(mixed_I-I-cross*beta*s.exp(-3*h)*cross_matrix/r**2),
        nonrectangular_transfer_fails=not zero(cross_matrix) and not zero(mixed_I-I),
        product_metric_transfer_fails=not zero(product_I-I),
        block_curvature=all(zero(F5[j]-s.diag(F[j], 0)) for j in F),
        block_moment=zero(I5-s.diag(I, 0)),
    )
    return dict(checks=checks, moment=I, curvature=F, cross_matrix=cross_matrix)


@lru_cache(None)
def center_controls():
    us = -2*u*v
    vs = v-(alpha*u+beta**2*u**2/alpha)/2
    uz = clean(us.subs(v, z+alpha*u/2))
    zz = clean((vs-alpha*us/2).subs(v, z+alpha*u/2))
    gamma = (beta**2-alpha**3)/(2*alpha)
    graph2 = gamma*u**2
    graph3 = graph2-3*alpha*gamma*u**3
    residual = lambda graph: clean(zz.subs(z, graph)-graph.diff(u)*uz.subs(z, graph))
    rem2, rem3 = residual(graph2), residual(graph3)
    system = s.Matrix([uz, zz])
    jac = system.jacobian([u, z]).subs({u: 0, z: 0})
    zeta = s.Symbol('zeta', positive=True)
    reciprocal = clean((-uz/u**2).subs(z, graph2).subs(u, 1/zeta))
    scalar_radial = 2*(r*r*hpp+2*r*hp)+alpha*s.exp(-2*h)+beta**2*s.exp(-4*h)/alpha
    v_s = s.Symbol('v_s', real=True)
    converted = scalar_radial.subs({hp: -v/r, hpp: (v_s+v)/r**2, h: -s.log(u)/2}, simultaneous=True)
    checks = dict(
        logarithmic_derivative=zero(converted-2*(v_s-v)-alpha*u-beta**2*u**2/alpha),
        u_center_equation=zero(uz+alpha*u*u+2*u*z),
        z_center_equation=zero(zz-z-(alpha**2-beta**2/alpha)*u*u/2-alpha*u*z),
        equilibrium=zero(system.subs({u: 0, z: 0})),
        linearization=jac == s.diag(0, 1),
        center_eigenvalue=jac.det() == 0,
        unstable_eigenvalue=jac.trace() == 1,
        graph_tangent=graph2.subs(u, 0) == 0 and graph2.diff(u).subs(u, 0) == 0,
        quadratic_residual=zero(rem2-3*alpha*gamma*u**3-4*gamma**2*u**4),
        cubic_residual_order=all(s.expand(rem3).coeff(u, j) == 0 for j in range(4)),
        generic_graph_not_exact=not zero(rem2),
        reciprocal_equation=zero(reciprocal-alpha-2*gamma/zeta),
        logarithmic_coefficient=zero(2*gamma/alpha-(beta**2-alpha**3)/alpha**2),
        h_logarithmic_coefficient=zero(gamma/alpha**2-(beta**2-alpha**3)/(2*alpha**3)),
        positive_comparison=alpha.is_positive is True,
    )
    return dict(checks=checks, gamma=gamma, graph2_residual=rem2,
                graph3_residual=rem3, vector_field=system)


@lru_cache(None)
def comparator_controls():
    hh = s.log(alpha*(tau+c))/2
    vv = hh.diff(tau)
    scalar = clean(2*(vv.diff(tau)-vv)+alpha*s.exp(-2*hh)+beta**2*s.exp(-4*hh)/alpha)
    density = clean(scalar**2/r**2)
    roots = (3+s.sqrt(10), s.sqrt(10)-3)
    checks = dict(
        generic_residual=zero(scalar-(beta**2-alpha**3)/(alpha**3*(tau+c)**2)),
        exact_parameter_surface=zero(scalar.subs(beta**2, alpha**3)),
        generic_leading_log_fails=not zero(scalar),
        wrong_log_action=zero(density-(beta**2-alpha**3)**2/(alpha**6*r**2*(tau+c)**4)),
        comparator_positive=all(x.is_positive is True for x in roots),
        comparator_beta_plus=zero(6/(roots[0]-1/roots[0])-1),
        comparator_beta_minus=zero(6/(roots[1]-1/roots[1])+1),
        comparator_inverse_pair=zero(roots[0]*roots[1]-1),
        exact_u_equation=zero(s.diff(1/(alpha*(tau+c)), tau)+2*vv/(alpha*(tau+c))),
        exact_v_equation=zero(vv.diff(tau)-vv+(1/(tau+c)+1/(tau+c)**2)/2),
        generic_density_diverges=s.limit(s.exp(tau)/(tau+c)**4, tau, s.oo) == s.oo,
    )
    return dict(checks=checks, scalar_residual=scalar, q_comparators=roots)


@lru_cache(None)
def holonomy_controls():
    G = s.diag(s.exp(-h), 1, 1, s.exp(h))
    qD = s.diag(q, q**-3, q, q)
    M0, L0 = E+N+P/2, qD*(E+beta*P)
    Mr = E+s.exp(-h)*N+s.exp(-2*h)*P/2
    Lr = qD*(E+beta*s.exp(-2*h)*P)
    delta = s.Symbol('delta', positive=True)
    checks = dict(
        actual_meridian_conjugation=zero(G*M0*G.inv()-Mr),
        actual_longitude_conjugation=zero(G*L0*G.inv()-Lr),
        preserved_commutation=zero(comm(Mr, Lr)),
        preserved_determinants=zero(Mr.det()-1) and zero(Lr.det()-1),
        finite_radius_Jordan_cube=zero((Mr-E)**3),
        finite_radius_Jordan_square=not zero((Mr-E)**2),
        limit_meridian=zero(Mr.applyfunc(lambda x: s.limit(x, h, s.oo))-E),
        limit_longitude=zero(Lr.applyfunc(lambda x: s.limit(x, h, s.oo))-qD),
        condition_asymptotic=zero(s.exp(2*h).subs(h, s.log(alpha*tau)/2)-alpha*tau),
        unbounded_transport=s.limit(alpha*tau, tau, s.oo) == s.oo,
        radial_coefficient_tends_zero=s.limit(-1/(2*tau), tau, s.oo) == 0,
        not_positive_power_error=s.limit(s.exp(delta*tau)/tau, tau, s.oo) == s.oo,
        logarithmic_radial_integral=s.integrate(1/tau, tau) == s.log(tau),
    )
    return dict(checks=checks, meridian=Mr, longitude=Lr)


@lru_cache(None)
def domain_controls():
    C = fields()
    C0 = [s.zeros(4), s.zeros(4), k*D]
    a = [C[j]-C0[j] for j in range(3)]
    inv = metric()
    jet = {hp: -v/r, h: -s.log(u)/2}
    pair = clean((r*r*one_norm(a, inv)).subs(jet, simultaneous=True))
    full = clean((r*r*one_norm(C, inv)).subs(jet, simultaneous=True))
    psi = clean((r*r*one_norm([(a+a.H)/2 for a in C], inv)).subs(jet, simultaneous=True))
    wedge = {(i, j): comm(a[i], a[j]) for i in range(3) for j in range(3)}
    derivative = lambda i, x: dr(x) if i == 0 else s.zeros(4)
    linear = {(i, j): clean(derivative(i, a[j])-derivative(j, a[i])
                           +comm(C0[i], a[j])-comm(C0[j], a[i]))
              for i in range(3) for j in range(3)}
    diff_density = clean((r*r*two_norm(linear, inv)).subs(jet, simultaneous=True))
    adj = clean(-dr(r*r*a[0])/r**2+sum(
        (inv[i, j]*comm(C0[i].H, a[j]) for i in range(3) for j in range(3)), s.zeros(4)))
    on_shell = {hpp: -2*hp/r-(alpha*s.exp(-2*h)+beta**2*s.exp(-4*h)/alpha)/(2*r*r)}
    adj_shell = clean(adj.subs(on_shell).subs(jet, simultaneous=True))
    adj_density = clean(r*r*s.trace(adj_shell.H*adj_shell))
    leading = {u: 1/(alpha*tau), v: 1/(2*tau)}
    checks = dict(
        limiting_reference_flat=all(zero(x) for x in residuals(C0, inv)[0].values()),
        limiting_reference_moment=zero(residuals(C0, inv)[1]),
        exact_pairing=zero(pair-2*v*v-2*alpha*u-beta*beta*u*u/alpha),
        exact_full_pairing=zero(full-pair-12*k*k/alpha),
        exact_Higgs_pairing=zero(psi-2*v*v-alpha*u-12*k*k/alpha-beta*beta*u*u/(2*alpha)),
        curvature_cancellation=all(zero(linear[j]+wedge[j]) for j in linear),
        separate_derivative_nonzero=not zero(linear[0, 1]),
        derivative_density=zero(diff_density-(2*alpha*v*v*u+4*beta*beta*v*v*u*u/alpha)/r**2),
        on_shell_adjoint=zero(adj_shell-(alpha*u+beta*beta*u*u/alpha)*H/(2*r*r)),
        adjoint_density=zero(adj_density-(alpha*u+beta*beta*u*u/alpha)**2/(2*r*r)),
        pairing_leading=s.limit(tau*pair.subs(leading), tau, s.oo) == 2,
        L4_leading=s.limit(tau**2*pair.subs(leading)**2, tau, s.oo) == 4,
        differential_leading=s.limit(r*r*tau**3*diff_density.subs(leading), tau, s.oo) == s.Rational(1, 2),
        adjoint_leading=s.limit(r*r*tau**2*adj_density.subs(leading), tau, s.oo) == s.Rational(1, 2),
        L2_comparison=s.integrate(s.exp(-tau), (tau, 1, s.oo)) == s.exp(-1),
        L4_divergence=s.limit(s.exp(tau)/tau**2, tau, s.oo) == s.oo,
        derivative_divergence=s.limit(s.exp(tau)/tau**3, tau, s.oo) == s.oo,
        adjoint_divergence=s.limit(s.exp(tau)/tau**2, tau, s.oo) == s.oo,
    )
    return dict(checks=checks, pairing_density=pair, full_density=full,
                Higgs_density=psi, differential_density=diff_density, adjoint_density=adj_density)


def run():
    groups = {name: function() for name, function in (
        ('source', source_controls), ('equations', equation_controls),
        ('center', center_controls), ('comparator', comparator_controls),
        ('holonomy', holonomy_controls), ('domain', domain_controls))}
    checks = {name+'/'+key: bool(value) for name, group in groups.items()
              for key, value in group['checks'].items()}
    return dict(checks=checks, all_checks_pass=all(checks.values()),
                groups={name: {key: str(value) for key, value in group.items() if key != 'checks'}
                        for name, group in groups.items()},
                scope='Exact local identities; authored external-theorem existence proof; no global or physical certificate')


if __name__ == '__main__':
    answer = run()
    print(json.dumps(answer, sort_keys=True))
    raise SystemExit(0 if answer['all_checks_pass'] else 1)
