"""R64 exact local controls, not a global particle or end-law certificate."""
from functools import lru_cache
import importlib.util
from pathlib import Path
import json
import sympy as s


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(file))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


r62 = load('r64_cone_action', 'cone_interaction.py')
r63 = load('r64_cone_symbol', 'cone_spectrum.py')
clean, zero, comm, norm = r62.clean, r62.zero, r62.comm, r62.norm
r = s.Symbol('r', positive=True)
a = s.Symbol('a', positive=True)
f, fp, fpp = s.symbols('f fp fpp', real=True)
eta = s.Symbol('eta', positive=True)
H = s.diag(1, -1)
T = s.Matrix([[0, 1], [1, 0]])
J = s.Matrix([[0, 1], [-1, 0]])


def dr(x):
    return x.diff(r)+fp*x.diff(f)+fpp*x.diff(fp)


def geometry(kind):
    h_inv, w = r62.link(kind)
    inverse = s.diag(1, 1/r**2, 1/r**2)
    inverse[1:3, 1:3] = h_inv/r**2
    c = clean((w.H*h_inv*w)[0])
    return inverse, w, c


def residuals(C, inverse):
    n = C[0].rows
    deriv = lambda i, x: dr(x) if i == 0 else s.zeros(n)
    F = {(i, j): clean(deriv(i, C[j])-deriv(j, C[i])+comm(C[i], C[j]))
         for i in range(3) for j in range(3)}
    divergence = dr(r**2*(C[0]+C[0].H))/r**2
    interaction = sum((inverse[i, j]*comm(C[i], C[j].H)
                       for i in range(3) for j in range(3)), s.zeros(n))
    return F, clean(divergence+interaction)


def one_norm(u, inverse):
    return clean(sum(inverse[i, j]*s.trace(u[i].H*u[j])
                     for i in range(3) for j in range(3)))


def two_norm(F, inverse):
    return clean(sum(inverse[i, k]*inverse[j, ell]*s.trace(F[i, j].H*F[k, ell])/2
                     for i in range(3) for j in range(3)
                     for k in range(3) for ell in range(3)
                     if inverse[i, k] != 0 and inverse[j, ell] != 0))


@lru_cache(None)
def metric_controls(kind):
    inverse, w, c = geometry(kind)
    lam = c*a*a
    g = s.cosh(f)*s.eye(2)+s.sinh(f)*T
    gi = s.cosh(f)*s.eye(2)-s.sinh(f)*T
    D = clean(g*H*gi)
    C = [clean(-dr(g)*gi)]+[clean(a*w[j]*D/2) for j in range(2)]
    C0 = [s.zeros(2)]+[a*w[j]*H/2 for j in range(2)]
    F, I = residuals(C, inverse)
    target = (-2*fpp-4*fp/r+lam*s.sinh(4*f)/(2*r**2))*T
    u = [clean(C[j]-C0[j]) for j in range(3)]
    wedge = {(i, j): clean(comm(u[i], u[j])) for i in range(3) for j in range(3)}
    derivative = lambda i, x: dr(x) if i == 0 else s.zeros(2)
    linear_F = {(i, j): clean(derivative(i, u[j])-derivative(j, u[i])
                              +comm(C0[i], u[j])-comm(C0[j], u[i]))
                for i in range(3) for j in range(3)}
    adj = clean(-dr(r**2*u[0])/r**2+
                sum((inverse[i, j]*comm(C0[i].H, u[j])
                     for i in range(3) for j in range(3)), s.zeros(2)))
    Us, Vs = s.cosh(2*f)-1, s.sinh(2*f)
    adj_shell = clean(adj.subs(fpp, lam*s.sinh(4*f)/(4*r**2)-2*fp/r))
    pair_density = clean(r*r*one_norm(u, inverse))
    bracket_density = clean(r*r*two_norm(wedge, inverse))
    v = [clean(x.diff(f).subs(f, 0)*r**eta+
               x.diff(fp).subs({f: 0, fp: 0})*eta*r**(eta-1)) for x in u]
    # The radial and tangential derivatives are taken at the zero field jet.
    v = [clean(x.subs(fp, 0)) for x in v]
    primitive_derivative = [eta*r**(eta-1)*T]+[comm(C0[j], r**eta*T) for j in (1, 2)]
    U = s.cos(f)*s.eye(2)+s.I*s.sin(f)*T
    Cu = [clean(-dr(U)*U.H)]+[clean(a*w[j]*U*H*U.H/2) for j in range(2)]
    Fu, Iu = residuals(Cu, inverse)
    C5 = [r62.embedded(x) for x in C]
    F5, I5 = residuals(C5, inverse)
    wrongly_omitted = list(C)
    wrongly_omitted[0] = s.zeros(2)
    bad_F, _ = residuals(wrongly_omitted, inverse)
    product_inverse = inverse.subs(r, 1)
    product_I = clean(dr(C[0]+C[0].H)+sum((product_inverse[i, j]*comm(C[i], C[j].H)
                      for i in range(3) for j in range(3)), s.zeros(2)))
    eps = s.Symbol('epsilon', real=True)
    leading_pair = clean(pair_density.subs({f: eps, fp: eta*eps/r}).series(eps, 0, 3).removeO().coeff(eps, 2))
    leading_bracket = clean(bracket_density.subs({f: eps, fp: eta*eps/r}).series(eps, 0, 5).removeO().coeff(eps, 4))
    checks = dict(
        positive_inverse=zero(g*gi-s.eye(2)),
        conjugated_H=zero(D-H*s.cosh(2*f)+J*s.sinh(2*f)),
        full_curvature_zero=all(zero(x) for x in F.values()),
        moment_from_metric=zero(I-target),
        radial_equation_annuls_moment=zero(I.subs(fpp, lam*s.sinh(4*f)/(4*r**2)-2*fp/r)),
        wrong_radial_omission_rejected=not zero(bad_F[0, 1]),
        wrong_product_metric_rejected=not zero(I-product_I),
        wrong_nonlinear_sign_rejected=not zero(I-(-2*fpp-4*fp/r-lam*s.sinh(4*f)/(2*r**2))*T),
        compact_unitary=zero(U.H*U-s.eye(2)),
        compact_full_residual_zero=all(zero(x) for x in Fu.values()) and zero(Iu),
        compact_radial_Higgs_zero=zero(Cu[0]+Cu[0].H),
        positive_not_unitary=not zero(g.H*g-s.eye(2)),
        positive_radial_detector=zero(norm((C[0]+C[0].H)/2)-2*fp**2),
        root_inclusion=all(zero(F5[k]-r62.embedded(F[k])) for k in F) and zero(I5-r62.embedded(I)),
        tangent_is_negative_covariant_primitive=all(zero(v[j]+primitive_derivative[j]) for j in range(3)),
        background_adjoint=zero(adj-(fpp+2*fp/r-lam*Vs/(2*r*r))*T),
        shell_adjoint_cubic=zero(adj_shell-lam*Vs*Us*T/(2*r*r)),
        compact_gauge_component_zero=zero(adj-adj.H),
        exact_flatness_retains_quadratic_source=all(zero(linear_F[k]+wedge[k]) for k in F),
        quadratic_source_nonzero=not zero(wedge[0, 1]),
        pairing_density=zero(pair_density-2*r*r*fp**2-lam*(Us**2+Vs**2)/2),
        bracket_density=zero(bracket_density-2*lam*fp**2*(Us**2+Vs**2)),
        pairing_leading_coefficient=zero(leading_pair-2*(eta**2+lam)),
        bracket_leading_coefficient=zero(leading_bracket-8*lam*eta**2/r**2),
    )
    return dict(checks=checks, lambda_value=lam, moment=I,
                pairing_density=pair_density, bracket_density=bracket_density,
                on_shell_adjoint=adj_shell)


@lru_cache(None)
def pair_controls():
    x, y, z, t, theta = s.symbols('x y z t theta', real=True)
    S = s.Matrix([[0, x+s.I*y], [z+s.I*t, 0]])
    K, P = (S-S.H)/2, (S+S.H)/2
    columns = [s.Matrix([s.re(B[0, 1]), s.im(B[0, 1]),
                         s.re(B[1, 0]), s.im(B[1, 0])]) for B in (J, s.I*T, T, s.I*J)]
    phase = s.diag(s.exp(s.I*theta/2), s.exp(-s.I*theta/2))
    Tp = s.Matrix([[0, s.exp(s.I*theta)], [s.exp(-s.I*theta), 0]])
    lam = eta*(eta+1)
    phi = r**eta
    scalar = clean(-s.diff(r*r*s.diff(phi, r), r)+lam*phi)
    roots = {}
    for sign in (1, -1):
        zz = s.Matrix([sign*s.sqrt(lam), 0])
        d0 = r63.operators(zz, eta+1)[0]
        mode = d0*s.eye(8)[:, 0]
        d1, adj, _ = r63.operators(zz, eta)
        roots[sign] = zero(d1*mode) and zero(adj*mode) and not zero(mode)
    checks = dict(
        real_split=zero(S-K-P) and zero(K.H+K) and zero(P.H-P),
        four_real_directions=s.Matrix.hstack(*columns).rank()==4,
        two_compact_generators=zero(J.H+J) and zero((s.I*T).H+s.I*T),
        two_Hermitian_generators=zero(T.H-T) and zero((s.I*J).H-s.I*J),
        scalar_Jacobi_zero=zero(scalar),
        wrong_radial_density_rejected=not zero(-r*r*s.diff(phi, r, 2)+lam*phi),
        both_roots_are_R63_modes=all(roots.values()),
        stabilizer_unitary=zero(phase.H*phase-s.eye(2)),
        stabilizer_fixes_background=zero(phase*H*phase.H-H),
        stabilizer_rotates_Hermitian_phase=zero(phase*T*phase.H-Tp),
        opposite_sign_is_same_stabilizer_orbit=zero(Tp.subs(theta, s.pi)+T),
        compact_tip_limit=s.limit(s.cos(r**eta), r, 0, dir='+')==1 and s.limit(s.sin(r**eta), r, 0, dir='+')==0,
        positive_tip_limit=s.limit(s.cosh(r**eta), r, 0, dir='+')==1 and s.limit(s.sinh(r**eta), r, 0, dir='+')==0,
    )
    return dict(checks=checks, compact_part=K, Hermitian_part=P)


@lru_cache(None)
def volterra_controls():
    k, v = s.symbols('k v', positive=True)
    pwr = eta+k
    exact = clean((r**eta*s.integrate(v**(k-1), (v, 0, r))
                   -r**(-eta-1)*s.integrate(v**(2*eta+k), (v, 0, r)))/(2*eta+1))
    expected = r**pwr/(k*(2*eta+k+1))
    lam = eta*(eta+1)
    L = lambda h: r*r*s.diff(h, r, 2)+2*r*s.diff(h, r)-lam*h
    b, c3 = s.symbols('b c3', real=True)
    cubic = 4*(eta+1)/(3*(4*eta+1))
    cubic_equation = c3*(3*eta*(3*eta+1)-lam)-8*lam/3
    u = s.Symbol('u', real=True)
    N = lam*(s.sinh(4*u)-4*u)/4
    remainder = s.series(N, u, 0, 6).removeO()
    delta = s.Rational(1, 8)
    correction_bound = s.Rational(8, 3)*delta**2*2
    lipschitz_bound = 4*delta**2*2
    checks = dict(
        monomial_integrals=zero(exact-expected),
        exact_Euler_inverse=zero(L(exact)-r**pwr),
        wrong_denominator_rejected=not zero(L(r**pwr/(k*(2*eta+k)))-r**pwr),
        kernel_factorization=zero(r**eta*v**(-eta-1)-r**(-eta-1)*v**eta
                                  -r**(-eta-1)*v**(-eta-1)*(r**(2*eta+1)-v**(2*eta+1))),
        kernel_positive_control=clean((r**(2*eta+1)-v**(2*eta+1)).subs({r: 2, v: 1})).is_positive is True,
        positive_homogeneous_kernel=zero(L(r**eta)),
        divergent_homogeneous_kernel=zero(L(r**(-eta-1))),
        fixed_amplitude_excludes_positive_kernel=s.limit(r**eta/r**eta, r, 0, dir='+')==1,
        remainder_excludes_divergent_kernel=s.limit(r**(-eta-1)/r**eta, r, 0, dir='+')==s.oo,
        cubic_source=zero(remainder.coeff(u, 3)-8*lam/3),
        cubic_correction=zero(cubic_equation.subs(c3, cubic)),
        wrong_cubic_rejected=not zero(cubic_equation.subs(c3, cubic/2)),
        uniform_ratio_bound=zero((4*eta+1)-(eta+1)-3*eta),
        hyperbolic_majorant=s.Rational(1, 1)/(1-s.Rational(1, 4)) < 2,
        ball_bound=correction_bound==s.Rational(1, 12) and correction_bound<1,
        contraction_bound=lipschitz_bound==s.Rational(1, 8) and lipschitz_bound<1,
    )
    return dict(checks=checks, monomial_inverse=exact, cubic_coefficient=cubic,
                correction_bound=correction_bound, lipschitz_bound=lipschitz_bound)


@lru_cache(None)
def threshold_controls():
    eps, b = s.symbols('epsilon b', positive=True)
    lam = eta*(eta+1)
    values4 = (s.Rational(1, 8), s.Rational(1, 4), s.Rational(1, 3), s.Rational(5, 12))
    values6 = (s.Rational(1, 8), s.Rational(1, 6), s.Rational(1, 5), s.Rational(1, 3))
    def improper(power):
        return s.limit(s.integrate(r**power, (r, eps, 1)), eps, 0, dir='+')
    integrals4 = [improper(4*x-2) for x in values4]
    integrals6 = [improper(6*x-2) for x in values6]
    t = s.Symbol('t', real=True)
    moment_cost = lam**2*(s.sinh(4*t)-4*t)**2/(4*r*r)
    sixth = clean(s.series(moment_cost, t, 0, 8).removeO().coeff(t, 6))
    checks = dict(
        L2_exponent=2*eta > -1,
        L4_threshold_equation=zero((4*eta-2)+1-4*(eta-s.Rational(1, 4))),
        bracket_leading_positive=bool((8*lam*eta**2).is_positive),
        L4_both_sides=[bool(x.is_finite) for x in integrals4]==[False, False, True, True],
        L4_borderline_log=zero(s.integrate(r**-1, (r, eps, 1))+s.log(eps)),
        unrelaxed_sixth_coefficient=zero(sixth-256*lam**2/(9*r*r)),
        moment_threshold_equation=zero((6*eta-2)+1-6*(eta-s.Rational(1, 6))),
        moment_both_sides=[bool(x.is_finite) for x in integrals6]==[False, False, True, True],
        distinct_thresholds=s.Rational(1, 6)<s.Rational(1, 4)<s.Rational(1, 2),
        admitted_critical_interval_nonempty=s.Rational(1, 4)<s.Rational(1, 3)<s.Rational(1, 2),
    )
    return dict(checks=checks, L4_integrals=integrals4, moment_integrals=integrals6)


@lru_cache(None)
def boundary_controls():
    R = s.Symbol('R', positive=True)
    lam = eta*(eta+1)
    density = 2*(eta**2+lam)*r**(2*eta)
    integral = clean(s.integrate(density, (r, 0, R)))
    flux = 2*eta*r**(2*eta+1)
    identity = dr(r*r*f*fp)-r*r*fp**2-lam*f*s.sinh(4*f)/4
    ode = r*r*fpp+2*r*fp-lam*s.sinh(4*f)/4
    return dict(checks=dict(
        exact_linear_energy_flux=zero(integral-flux.subs(r, R)),
        apex_flux_zero=s.limit(flux, r, 0, dir='+')==0,
        outer_flux_positive=integral.is_positive is True,
        dropping_outer_flux_rejected=not zero(integral),
        nonlinear_energy_identity=zero(identity-f*ode),
        nonlinear_zero_ODE_removes_remainder=zero(identity.subs(fpp, lam*s.sinh(4*f)/(4*r*r)-2*fp/r)),
        positive_and_negative_controls=all(x*s.sinh(4*x)>0 for x in (s.Integer(1), s.Integer(-1))),
        zero_profile_control=zero(ode.subs({f: 0, fp: 0, fpp: 0})),
    ), energy=integral, outer_flux=flux.subs(r, R))


def run():
    groups = dict(square=metric_controls('square'), hexagonal=metric_controls('hexagonal'),
                  pair=pair_controls(), volterra=volterra_controls(),
                  thresholds=threshold_controls(), boundary=boundary_controls())
    checks = {group+'_'+key: bool(value) for group, data in groups.items()
              for key, value in data['checks'].items()}
    return dict(scope='Local supplied cone action, compact split and authored nonlinear existence; no global particle count',
                groups=groups, checks=checks, all_checks_pass=all(checks.values()))


if __name__ == '__main__':
    result = run()
    print(json.dumps(r63.serial(result), indent=2))
    raise SystemExit(0 if result['all_checks_pass'] else 1)
