"""R36 charged mode overlaps: exact local identities and declared controls.

Not a global m202 eigenproblem, a selected scalar profile, or a quantum gap.
All scientific execution must follow the YUKAWA_OVERLAP_DESIGN seal.
"""
from functools import lru_cache
import json

import sympy as sp

x = sp.Symbol('x', real=True)
t = sp.Symbol('t', positive=True)
q = sp.Symbol('q', real=True)


def residual(left, right=0):
    """Validate operands before subtraction; no float cancellation escape."""
    left, right = sp.sympify(left), sp.sympify(right)
    if left.has(sp.Float) or right.has(sp.Float):
        raise ValueError('exact operands required')
    return sp.simplify(sp.cancel(sp.expand(left-right)))


def cov(f, charge, A):
    return sp.diff(f, x)+sp.I*charge*A*f


def lap(f, charge, A, J):
    return cov(J*cov(f, charge, A), charge, A)/J


def first(f, charge, A, F):
    return cov(f, charge, A)+q*sp.diff(F, x)*f


def scalar_h(f, charge, A, F, J):
    potential = q*q*sp.diff(F, x)**2-q*sp.diff(J*sp.diff(F, x), x)/J
    return -lap(f, charge, A, J)+potential*f


def coefficient_operator(b, charge, A, F, J):
    return lap(b, charge, A, J)/2-q*sp.diff(F, x)*cov(b, charge, A)


@lru_cache(maxsize=None)
def local_identity(charges=(1, 1)):
    """Arbitrary radial volume J: bilinear or dual-charge Hermitian precursor."""
    a, c = charges
    u, v, b, A, F, J = [sp.Function(k)(x) for k in ('u', 'v', 'b', 'A', 'F', 'J')]
    w = u*v
    flux = cov(w, a+c, A)/2+q*sp.diff(F, x)*w
    kinetic = first(u, a, A, F)*first(v, c, A, F)
    hterm = (u*scalar_h(v, c, A, F, J)+v*scalar_h(u, a, A, F, J))/2
    product = residual(kinetic, cov(J*flux, a+c, A)/J+hterm)
    drift = coefficient_operator(b, -a-c, A, F, J)
    endpoint_flux = J*(b*flux-w*cov(b, -a-c, A)/2)
    green = residual(b*(kinetic-hterm)-w*drift, sp.diff(endpoint_flux, x)/J)
    # Removing this term must fail for generic b,F,u,v, not just a test label.
    wrong_drift = lap(b, -a-c, A, J)/2
    missing_drift = residual(b*(kinetic-hterm)-w*wrong_drift,
                             sp.diff(endpoint_flux, x)/J)
    return dict(product=product, green=green, missing_drift=missing_drift)


@lru_cache(maxsize=1)
def gauge_controls():
    u, b, A, F, eta, J = [sp.Function(k)(x) for k in ('u', 'b', 'A', 'F', 'eta', 'J')]
    z = sp.exp(sp.I*eta)
    shifted = A-sp.diff(eta, x)
    q_cov = residual(first(z*u, 1, shifted, F), z*first(u, 1, A, F))
    h_cov = residual(scalar_h(z*u, 1, shifted, F, J), z*scalar_h(u, 1, A, F, J))
    b_cov = residual(coefficient_operator(b/z**2, -2, shifted, F, J),
                     coefficient_operator(b, -2, A, F, J)/z**2)
    # The actual R33 charges, not a fundamental E6/Z3 27.
    mirror_charge = 2-1-1
    ordinary_charge = -2+1+1
    wrong_unconjugated_charge = 2+1+1
    return dict(first=q_cov, scalar=h_cov, coefficient=b_cov,
                mirror_charge=mirror_charge, ordinary_charge=ordinary_charge,
                wrong_unconjugated_charge=wrong_unconjugated_charge)


@lru_cache(maxsize=1)
def interval_control():
    """One positive absolute pair; prescribed, not stationary, scalar profile."""
    u = sp.sqrt(2/sp.pi)*sp.cos(x)
    v = -sp.sqrt(2/sp.pi)*sp.sin(x)
    N = sp.sqrt(2*t/(1-sp.exp(-2*sp.pi*t)))
    s = N*sp.exp(-t*x)
    integrate = lambda f: sp.integrate(f, (x, 0, sp.pi))
    M = integrate(s*u*u)
    P = integrate(s*v*v)
    factor = 2*N*(1-sp.exp(-sp.pi*t))/(sp.pi*t*(t*t+4))
    expected_M, expected_P = factor*(t*t+2), 2*factor
    volume = integrate(u*u*sp.diff(s, x, 2)/2)
    boundary = -(sp.diff(s, x)*u*u).subs(x, sp.pi)/2+(sp.diff(s, x)*u*u).subs(x, 0)/2
    return dict(
        u_norm=residual(integrate(u*u), 1),
        v_norm=residual(integrate(v*v), 1),
        s_norm=residual(integrate(s*s), 1),
        eigen=residual(-sp.diff(u, x, 2), u),
        partner=residual(sp.diff(u, x), v),
        endpoints=[sp.diff(u, x).subs(x, end) for end in (0, sp.pi)],
        M=residual(M), P=residual(P),
        M_formula=residual(M, expected_M), P_formula=residual(P, expected_P),
        identity=residual(P-M, volume+boundary),
        omitted_boundary_at_two=residual((P-M-volume).subs(t, 2)),
        boundary_at_two=residual(boundary.subs(t, 2)),
        ratio=residual(M/P),
        gradient=residual(integrate(sp.diff(s, x)**2), t*t),
        M_limit=sp.limit(sp.sqrt(t)*expected_M, t, sp.oo),
        P_limit=sp.limit(t**sp.Rational(5, 2)*expected_P, t, sp.oo),
        M_zero_limit=sp.limit(expected_M, t, 0, dir='+'),
        P_zero_limit=sp.limit(expected_P, t, 0, dir='+'))


@lru_cache(maxsize=1)
def robin_control():
    """Nonzero Witten field, actual Robin condition, both integral corrections."""
    a = sp.Integer(2)
    u = sp.sqrt(2/(sp.pi*(1+a*a)))*(sp.cos(x)-a*sp.sin(x))
    v = -sp.sqrt(2/sp.pi)*sp.sin(x)
    lam = 1+a*a
    b = x*x  # Deliberately a test coefficient, not a normalized scalar mode.
    integrate = lambda f: sp.integrate(sp.expand_trig(f), (x, 0, sp.pi))
    M, P = integrate(b*u*u), integrate(b*v*v)
    volume = integrate(u*u*(sp.diff(b, x, 2)/2-a*sp.diff(b, x)))
    boundary = -(sp.diff(b, x)*u*u).subs(x, sp.pi)/2+(sp.diff(b, x)*u*u).subs(x, 0)/2
    return dict(
        eigen=residual(-sp.diff(u, x, 2)+a*a*u, lam*u),
        partner=residual((sp.diff(u, x)+a*u)/sp.sqrt(lam), v),
        u_norm=residual(integrate(u*u), 1), v_norm=residual(integrate(v*v), 1),
        robin=[residual((sp.diff(u, x)+a*u).subs(x, end)) for end in (0, sp.pi)],
        undeformed_neumann=[residual(sp.diff(u, x).subs(x, end)) for end in (0, sp.pi)],
        identity=residual(lam*(P-M), volume+boundary),
        boundary=residual(boundary), volume=residual(volume),
        wrong_no_drift=residual(lam*(P-M), integrate(u*u*sp.diff(b, x, 2)/2)+boundary))


def fourier_pair(n, alpha=sp.Rational(1, 3)):
    n, alpha = sp.sympify(n), sp.sympify(alpha)
    if n.is_integer is not True or n.is_number is not True or alpha.has(sp.Float):
        raise ValueError('exact integral mode and exact holonomy required')
    k = n+alpha
    if k.is_real is not True or k.is_zero is not False:
        raise ValueError('nonzero real momentum required for normalized partner')
    u = sp.exp(sp.I*n*x)/sp.sqrt(2*sp.pi)
    return u, sp.I*sp.sign(k)*u, k*k


@lru_cache(maxsize=1)
def circle_control():
    modes = (-1, 0, 1)
    alpha = sp.Rational(1, 3)
    c = {-2: sp.Integer(1), -1: sp.I, 0: sp.Integer(2), 1: 1+sp.I, 2: sp.Integer(0)}
    norm2 = sum(sp.conjugate(z)*z for z in c.values())
    coeff = {n: z/sp.sqrt(norm2) for n, z in c.items()}
    s = sum(z*sp.exp(sp.I*n*x)/sp.sqrt(2*sp.pi) for n, z in coeff.items())
    pairs = [fourier_pair(n, alpha) for n in modes]
    integrate = lambda f: residual(sp.integrate(sp.expand(f), (x, 0, 2*sp.pi)))
    M = sp.Matrix(3, 3, lambda i, j: integrate(s*sp.conjugate(pairs[i][0])*sp.conjugate(pairs[j][0])))
    P = sp.Matrix(3, 3, lambda i, j: integrate(sp.conjugate(s)*pairs[i][1]*pairs[j][1]))
    D = sp.diag(*(sp.sign(n+alpha) for n in modes))
    congruence = (P+D*M.conjugate()*D).applyfunc(residual)
    z = sp.Symbol('z')
    spectral = residual((P.H*P).charpoly(z).as_expr(), (M.H*M).charpoly(z).as_expr())
    target_M = sp.Matrix(3, 3, lambda i, j: coeff[modes[i]+modes[j]]/sp.sqrt(2*sp.pi))
    # Arbitrary local phase requires a nonparallel scalar here; order-three squared is nontrivial.
    omega = (-1+sp.sqrt(3)*sp.I)/2
    U = sp.diag(1, sp.I, -1)
    rebased = U.T*P*U
    basis_spectrum = residual((rebased.H*rebased).charpoly(z).as_expr(), (P.H*P).charpoly(z).as_expr())
    return dict(
        scalar_norm=residual(integrate(s*sp.conjugate(s)), 1),
        fermion_norms=[residual(integrate(u*sp.conjugate(u)), 1) for u, _, _ in pairs],
        partner_residuals=[residual(sp.diff(u, x)+sp.I*alpha*u, sp.sqrt(lam)*v) for u, v, lam in pairs],
        eigenvalues=[lam for _, _, lam in pairs],
        coefficient_residual=(M-target_M).applyfunc(residual),
        congruence=congruence, same_singular_polynomial=spectral, basis_spectrum=basis_spectrum,
        M_scaled=(sp.sqrt(2*sp.pi)*M).applyfunc(residual),
        P_scaled=(sp.sqrt(2*sp.pi)*P).applyfunc(residual),
        squared_holonomy=residual(omega**2),
        squared_holonomy_nontrivial=residual(omega**2-1) != 0)


def tensor_type_control():
    z = sp.Matrix([1, sp.I, 0])/sp.sqrt(2)
    return dict(bilinear=(z.T*z)[0], hermitian=(z.H*z)[0])


def all_results():
    charged, dual = local_identity(), local_identity((1, -1))
    gauge, interval, robin, circle = gauge_controls(), interval_control(), robin_control(), circle_control()
    typed = tensor_type_control()
    checks = dict(
        charged_product_green=charged['product'] == charged['green'] == 0,
        dual_product_green=dual['product'] == dual['green'] == 0,
        drift_mutants_fail=charged['missing_drift'] != 0 and dual['missing_drift'] != 0,
        gauge_covariance=all(gauge[k] == 0 for k in ('first', 'scalar', 'coefficient', 'mirror_charge', 'ordinary_charge')) and gauge['wrong_unconjugated_charge'] != 0,
        interval_normalized=all(interval[k] == 0 for k in ('u_norm', 'v_norm', 's_norm', 'eigen', 'partner', 'M_formula', 'P_formula', 'identity', 'gradient')) and interval['endpoints'] == [0, 0],
        boundary_required=interval['omitted_boundary_at_two'] == interval['boundary_at_two'] != 0,
        ratio_and_absolute_scale=residual(interval['ratio'], (t*t+2)/2) == 0 and interval['M_limit'] == 2*sp.sqrt(2)/sp.pi and interval['P_limit'] == 4*sp.sqrt(2)/sp.pi,
        constant_profile_current=interval['M_zero_limit'] == interval['P_zero_limit'] == 1/sp.sqrt(sp.pi),
        robin_and_drift=all(robin[k] == 0 for k in ('eigen', 'partner', 'u_norm', 'v_norm', 'identity')) and robin['robin'] == [0, 0] and all(z != 0 for z in robin['undeformed_neumann']) and robin['wrong_no_drift'] != 0,
        circle_no_selectivity=circle['scalar_norm'] == circle['same_singular_polynomial'] == circle['basis_spectrum'] == 0 and circle['congruence'] == circle['coefficient_residual'] == sp.zeros(3) and all(z == 0 for z in circle['fermion_norms']+circle['partner_residuals']) and circle['squared_holonomy_nontrivial'],
        bilinear_not_density=typed == dict(bilinear=0, hermitian=1))
    return dict(checks=checks, all_checks_pass=all(checks.values()),
                charged=charged, dual=dual, gauge=gauge, interval=interval,
                robin=robin, circle=circle, tensor_type=typed,
                scope='Exact identities and explicit comparators in the ADDED coupling model; no actual sourced eigenfunctions, selected scalar, or quantum mirror gap.')


if __name__ == '__main__':
    result = all_results()
    print(json.dumps(result, default=str, indent=2))
    raise SystemExit(0 if result['all_checks_pass'] else 1)
