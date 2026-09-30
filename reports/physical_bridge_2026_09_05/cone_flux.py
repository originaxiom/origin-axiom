"""R67 exact boundary and radial controls, not a physical-domain certificate."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

import sympy as s


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(file))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


prior = load('r67_nilpotent_source', 'nilpotent_cone.py')
metric_source = load('r67_metric_source', 'source_action.py')
r, h, hp, hpp, alpha, beta, k = prior.r, prior.h, prior.hp, prior.hpp, prior.alpha, prior.beta, prior.k
H, N, P, D = prior.H, prior.N, prior.P, prior.D
clean, zero, comm = prior.clean, prior.zero, prior.comm
u, v, tau, c = prior.u, prior.v, prior.tau, prior.c
f, fp, fpp = s.symbols('f fp fpp', real=True)


def dr(x):
    return prior.dr(x)+fp*x.diff(f)+fpp*x.diff(fp)


def norm(x):
    return clean(s.trace(x.H*x))


@lru_cache(None)
def geometry():
    x, y = s.symbols('x y', real=True)
    g = s.diag(1, r*r/alpha, alpha*r*r)
    return metric_source.metric_data(g, (r, x, y))


@lru_cache(None)
def flux_controls():
    inv, gamma, ric = geometry()
    C = prior.fields()
    A = [clean((a-a.H)/2) for a in C]
    psi = [clean((a+a.H)/2) for a in C]
    derivative = lambda i, a: dr(a) if i == 0 else s.zeros(4)
    nabla = {(i, j): clean(derivative(i, psi[j])+comm(A[i], psi[j])
                           -sum((gamma[t][i][j]*psi[t] for t in range(3)), s.zeros(4)))
             for i in range(3) for j in range(3)}
    Fa = {(i, j): clean(derivative(i, A[j])-derivative(j, A[i])+comm(A[i], A[j]))
          for i in range(3) for j in range(3)}
    wedge = {(i, j): comm(psi[i], psi[j]) for i in range(3) for j in range(3)}
    exterior = {(i, j): clean(nabla[i, j]-nabla[j, i])
                for i in range(3) for j in range(3)}
    div = clean(sum((inv[i, i]*nabla[i, i] for i in range(3)), s.zeros(4)))
    rough = clean(sum(inv[i, i]*inv[j, j]*norm(nabla[i, j]) for i in range(3) for j in range(3)))
    ric_pair = clean(sum(inv[i, i]*inv[j, j]*ric[i, j]*s.trace(psi[i]*psi[j])
                         for i in range(3) for j in range(3)))
    current = clean(s.trace(psi[0]*div-sum(
        (inv[j, j]*psi[j]*nabla[j, 0] for j in range(3)), s.zeros(4))))
    B = clean(r*r*current)
    F, I = prior.residuals(C, inv)
    residual = clean(r*r*(prior.two_norm(F, inv)+norm(I)/4))
    expanded = clean(r*r*(prior.two_norm(Fa, inv)+prior.two_norm(wedge, inv)+rough+ric_pair))
    cross = clean(sum(inv[i, i]*inv[j, j]*s.trace(Fa[i, j].H*wedge[i, j])/2
                      for i in range(3) for j in range(3)))
    B0 = alpha*s.exp(-2*h)+beta*beta*s.exp(-4*h)/alpha
    target = 4*r*hp*hp+2*hp*B0+(alpha*s.exp(-2*h)+12*k*k/alpha+beta*beta*s.exp(-4*h)/(2*alpha))/r
    shell = {hpp: -2*hp/r-B0/(2*r*r)}
    checks = dict(
        inverse_metric=zero(inv-prior.metric()),
        volume_density=zero(inv.det()-r**-4),
        metric_Ricci=ric == s.diag(0, -1/alpha, -alpha),
        radial_Christoffel=gamma[0][1][1] == -r/alpha and gamma[0][2][2] == -alpha*r,
        unitary_connection=all(zero(a+a.H) for a in A),
        Hermitian_Higgs=all(zero(a-a.H) for a in psi),
        curvature_decomposition=all(zero(F[j]-Fa[j]-wedge[j]-exterior[j]) for j in F),
        moment_is_twice_divergence=zero(I-2*div),
        covariant_Bochner=zero(prior.two_norm(exterior, inv)+norm(div)-rough-ric_pair+2*cross-dr(B)/(r*r)),
        full_off_shell_boundary_identity=zero(residual-expanded-dr(B)),
        actual_boundary_current=zero(B-target),
        wrong_boundary_sign_fails=not zero(residual-expanded+dr(B)),
        omitted_Ricci_fails=not zero(residual-expanded+r*r*ric_pair-dr(B)),
        nonabelian_cross_not_zero=not zero(cross),
        omitted_nonabelian_energy_fails=not zero(prior.two_norm(Fa, inv)+prior.two_norm(wedge, inv)),
        exact_on_shell_zero=zero(residual.subs(shell)),
        on_shell_expanded_is_boundary=zero((expanded+dr(B)).subs(shell)),
    )
    return dict(checks=checks, boundary=B, residual_density=residual,
                expanded_density=expanded, rough_density=clean(r*r*rough),
                Ricci_density=clean(r*r*ric_pair), on_shell=shell)


@lru_cache(None)
def limit_controls():
    flux = flux_controls()
    B = flux['boundary']
    poly = clean((r*B).subs({hp: -v/r, h: -s.log(u)/2}, simultaneous=True))
    reference = 12*k*k/(alpha*r)
    leading = {u: 1/(alpha*tau), v: 1/(2*tau)}
    expected = 4*v*v-2*v*(alpha*u+beta*beta*u*u/alpha)+alpha*u+12*k*k/alpha+beta*beta*u*u/(2*alpha)
    hh = s.log(alpha*(tau+c))/2
    vv = hh.diff(tau)
    exact_B = clean(B.subs({h: hh, hp: -vv/r}, simultaneous=True).subs(beta**2, alpha**3))
    derivative = lambda a: clean(a.diff(r)-a.diff(tau)/r)
    exact_E = clean(flux['expanded_density'].subs({h: hh, hp: -vv/r,
                    hpp: (vv.diff(tau)+vv)/r**2}, simultaneous=True).subs(beta**2, alpha**3))
    # A separately assembled commuting reference, not the nilpotent formula with missing terms.
    inv, gamma, ric = geometry()
    psi = [s.zeros(4), s.zeros(4), k*D]
    nabla = {(i, j): -sum((gamma[t][i][j]*psi[t] for t in range(3)), s.zeros(4))
             for i in range(3) for j in range(3)}
    ref_rough = clean(r*r*sum(inv[i, i]*inv[j, j]*norm(nabla[i, j]) for i in range(3) for j in range(3)))
    ref_Ricci = clean(r*r*sum(inv[i, i]*inv[j, j]*ric[i, j]*s.trace(psi[i]*psi[j])
                             for i in range(3) for j in range(3)))
    ref_B = clean(-r*r*sum(inv[j, j]*s.trace(psi[j]*nabla[j, 0]) for j in range(3)))
    checks = dict(
        logarithmic_flux_polynomial=zero(poly-expected),
        reference_flux_derived=zero(ref_B-reference),
        reference_rough=zero(ref_rough-24*k*k/(alpha*r*r)),
        reference_Ricci=zero(ref_Ricci+12*k*k/(alpha*r*r)),
        reference_boundary_identity=zero(ref_rough+ref_Ricci+reference.diff(r)),
        full_leading_constant=s.limit(poly.subs(leading), tau, s.oo) == 12*k*k/alpha,
        reference_subtraction_leaves_log=s.limit(tau*(poly-12*k*k/alpha).subs(leading), tau, s.oo) == 1,
        remaining_flux_diverges=s.limit(s.exp(tau)/tau, tau, s.oo) == s.oo,
        exact_comparator_boundary=zero(exact_E+derivative(exact_B)),
        comparator_reference_not_enough=not zero(exact_B-reference),
        outward_sign_retained=zero(derivative(exact_B-reference)+exact_E-12*k*k/(alpha*r*r)),
    )
    return dict(checks=checks, flux_polynomial=poly, exact_boundary=exact_B,
                exact_expanded_density=exact_E, reference_boundary=ref_B)


@lru_cache(None)
def jacobi_controls():
    C = prior.fields()
    inv, _, _ = geometry()
    a = [fp*H, -f*s.exp(-h)*N, -2*beta*f*s.exp(-2*h)*P]
    derivative = lambda i, x: dr(x) if i == 0 else s.zeros(4)
    dCa = {(i, j): clean(derivative(i, a[j])-derivative(j, a[i])+comm(C[i], a[j])-comm(C[j], a[i]))
           for i in range(3) for j in range(3)}
    adj = clean(-dr(r*r*a[0])/r**2+sum(
        (inv[i, i]*comm(C[i].H, a[i]) for i in range(3)), s.zeros(4)))
    Ah = alpha*s.exp(-2*h)+2*beta*beta*s.exp(-4*h)/alpha
    pair = clean(r*r*prior.one_norm(a, inv))
    jacobi = r*r*fpp+2*r*fp-Ah*f
    us = -2*u*v
    vs = v-(alpha*u+beta*beta*u*u/alpha)/2
    vss = clean(vs.diff(u)*us+vs.diff(v)*vs)
    gamma = (beta*beta-alpha**3)/(2*alpha)
    converted = clean(jacobi.subs({h: -s.log(u)/2, f: v, fp: -vs/r,
                                  fpp: (vss+vs)/r**2}, simultaneous=True))
    leading = {h: s.log(alpha*tau)/2, f: 1/(2*tau), fp: 1/(2*r*tau**2)}
    kinetic = clean(pair.subs(leading, simultaneous=True))
    Xi = s.Matrix(4, 4, lambda i,j: s.Symbol('xi'+str(i)+str(j)))
    checks = dict(
        exact_covariant_primitive=all(zero(a[i]-([fp*H, comm(C[1], f*H), comm(C[2], f*H)][i])) for i in range(3)),
        tangent_flatness=all(zero(x) for x in dCa.values()),
        tangent_formal_adjoint=zero(adj+jacobi*H/r**2),
        positive_Jacobi_coefficient=zero(Ah-alpha*s.exp(-2*h)-2*beta*beta*s.exp(-4*h)/alpha),
        wrong_Jacobi_sign_fails=not zero(adj+(r*r*fpp+2*r*fp+Ah*f)*H/r**2),
        kinetic_metric=zero(pair-2*r*r*fp*fp-2*Ah*f*f),
        autonomous_translation_solves=zero(converted),
        derivative_asymptotic=zero(vs.subs(v, alpha*u/2+gamma*u*u)+alpha*alpha*u*u/2),
        kinetic_leading=s.limit(tau**3*kinetic, tau, s.oo) == s.Rational(1, 2),
        quartic_leading=s.limit(tau**6*kinetic**2, tau, s.oo) == s.Rational(1, 4),
        L2_comparison=s.integrate(s.exp(-tau), (tau, 1, s.oo)) == s.exp(-1),
        L4_divergence=s.limit(s.exp(tau)/tau**6, tau, s.oo) == s.oo,
        radial_energy_identity=zero(dr(2*r*r*f*fp)-pair-2*f*jacobi),
        apex_flux_vanishes=s.limit(s.exp(-tau)/(4*tau**3), tau, s.oo) == 0,
        compact_projection_zero=zero(s.trace(H*comm(Xi, hp*H))),
        actual_radial_projection=s.trace(H*a[0]) == 2*fp,
    )
    return dict(checks=checks, formal_adjoint=adj, kinetic_density=pair,
                translation_equation=converted, radial_derivative=vs)


@lru_cache(None)
def boundary_controls():
    C = prior.fields()
    inv, _, _ = geometry()
    dh, db, dk = s.symbols('delta_h delta_beta delta_k', real=True)
    variation = [dh*x.diff(h)+db*x.diff(beta)+dk*x.diff(k) for x in C]
    theta = clean(-s.trace(C[1]*variation[2]-C[2]*variation[1]))
    a = [s.zeros(4), s.zeros(4), s.exp(h)*N.H]
    bad_theta = clean(-s.trace(C[1]*a[2]-C[2]*a[1]))
    derivative = lambda i, x: dr(x) if i == 0 else s.zeros(4)
    dCa = {(i, j): clean(derivative(i, a[j])-derivative(j, a[i])+comm(C[i], a[j])-comm(C[j], a[i]))
           for i in range(3) for j in range(3)}
    pair = clean(r*r*prior.one_norm(a, inv))
    graph = clean(r*r*prior.two_norm(dCa, inv))
    checks = dict(
        triangular_family_boundary_zero=zero(theta),
        lower_control_boundary_nonzero=bad_theta == -2,
        lower_control_kinetic=zero(pair-2*s.exp(2*h)/alpha),
        lower_control_L2=s.integrate(2*tau*s.exp(-tau), (tau, 1, s.oo)) == 4/s.E,
        lower_control_radial_flat=zero(dCa[0, 2]),
        lower_control_angular_not_flat=zero(dCa[1, 2]-H),
        lower_control_graph=zero(graph-2/r**2),
        lower_control_graph_diverges=s.limit(2/r, r, 0, dir='+') == s.oo,
    )
    return dict(checks=checks, triangular_boundary=theta, lower_boundary=bad_theta,
                lower_kinetic_density=pair, lower_graph_density=graph)


def run():
    groups = {name: func() for name, func in (
        ('flux', flux_controls), ('limits', limit_controls),
        ('jacobi', jacobi_controls), ('boundary', boundary_controls))}
    checks = {name+'/'+key: bool(value) for name, group in groups.items() for key, value in group['checks'].items()}
    return dict(checks=checks, all_checks_pass=all(checks.values()),
                groups={name: {key:str(value) for key,value in group.items() if key!='checks'}
                        for name,group in groups.items()},
                scope='Exact local boundary and profile identities; no full fermion domain, global mode or physical completion')


if __name__ == '__main__':
    answer = run()
    print(json.dumps(answer, sort_keys=True))
    raise SystemExit(0 if answer['all_checks_pass'] else 1)
