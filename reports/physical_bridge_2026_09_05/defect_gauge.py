"""R29: an added finite-width source model and its bare transverse gauge limit.

No physical chiral-domain transfer, anomaly cancellation or TOE is asserted.
All scientific functions are pure/read-only; main prints its complete receipt.
"""
from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
import itertools
import json
import math
import time

import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigh
from scipy.optimize import brentq
import sympy as sp


def clean(x):
    return sp.factor(sp.trigsimp(sp.simplify(sp.expand(x))))


def zero(x):
    return clean(x) == 0


@lru_cache(maxsize=1)
def character():
    C = 2 * sp.eye(6)
    for i, j in ((0, 2), (2, 3), (3, 4), (4, 5), (1, 3)):
        C[i, j] = C[j, i] = -1
    Ci = C.inv()
    t = 3 * Ci[0, :]
    allowed = {q: all(v.is_Integer for v in sp.Rational(q, 4) * t)
               for q in range(1, 13)}
    zeta = (-1 + sp.I * sp.sqrt(3)) / 2
    return dict(C=C, t=t, gcd=sp.igcd(*list(t)), allowed=allowed,
                phase4=sp.simplify(sp.expand_complex(zeta**4)),
                phase12=sp.simplify(sp.expand_complex(zeta**12)))


@lru_cache(maxsize=1)
def local_action():
    C, kap, q, sig, lam, v, g = sp.symbols(
        'C kappa q sigma lambda v g7', positive=True)
    d, c, f, x, y, ux, uy, A = sp.symbols(
        'div_h curl_h curvature x y dx dy A', real=True)
    n = x*x + y*y
    cov = sp.Matrix([ux + q*A*y, uy - q*A*x])
    D = d - kap*q*sig*n
    radial = n - v*v/2
    residuals = sp.Matrix([c, D, f, cov[0], cov[1], radial])
    W = sp.diag(C, C, 1/(2*g*g), sig, sig, sig*lam)
    density = (residuals.T * W * residuals)[0]
    variables = sp.Matrix([d, c, f, x, y, ux, uy, A])
    point = {d: kap*q*sig*v*v/2, c: 0, f: 0, x: v/sp.sqrt(2),
             y: 0, ux: 0, uy: 0, A: 0}
    gradient = sp.Matrix([sp.diff(density, z) for z in variables])
    J0 = residuals.jacobian(variables).subs(point)
    hess0 = sp.hessian(density, variables).subs(point)
    expected_qx = (-4*C*kap*q*sig*x*D + 4*sig*lam*x*radial
                   - 2*sig*q*A*cov[1])
    current = 2*sig*q*(x*cov[1] - y*cov[0])
    wrong = dict(point)
    wrong[d] = 0
    return dict(C=C, kap=kap, q=q, sig=sig, lam=lam, v=v, g=g,
                d=d, c=c, f=f, x=x, y=y, ux=ux, uy=uy, A=A,
                cov=cov, D=D, radial=radial, variables=variables,
                density=sp.expand(density), gradient=gradient, point=point,
                stationary=gradient.subs(point).applyfunc(clean),
                hessian_residual=(hess0-2*J0.T*W*J0).applyfunc(clean),
                q_equation_residual=clean(sp.diff(density, x)-expected_qx),
                current_residual=clean(sp.diff(density, A)+current),
                source_response=clean(sp.diff(D, x)),
                missing_source_cost=clean(density.subs(wrong)),
                wrong_amplitude_force=clean(gradient[3].subs(
                    {**point, x: sp.sqrt(2)*v, d: 2*kap*q*sig*v*v})))


@lru_cache(maxsize=1)
def covariance():
    theta, omega, q, A, x, y, ux, uy = sp.symbols(
        'theta omega q A x y ux uy', real=True)
    J = sp.Matrix([[0, -1], [1, 0]])
    R = sp.Matrix([[sp.cos(theta), -sp.sin(theta)],
                   [sp.sin(theta), sp.cos(theta)]])
    Q, dQ = sp.Matrix([x, y]), sp.Matrix([ux, uy])
    DQ = dQ-q*A*J*Q
    transformed_derivative = R*dQ+q*omega*J*R*Q
    transformed = transformed_derivative-q*(A+omega)*J*R*Q
    omitted = R*dQ-q*(A+omega)*J*R*Q
    mutant = (omitted-R*DQ).applyfunc(clean)
    return dict(q=q, omega=omega, x=x, y=y,
                residual=(transformed-R*DQ).applyfunc(clean),
                norm_residual=clean((transformed.T*transformed)[0]-(DQ.T*DQ)[0]),
                mutant_norm=clean((mutant.T*mutant)[0]))


@lru_cache(maxsize=1)
def core_and_cutoff():
    r, eps, R, L, kap, q, v, g = sp.symbols(
        'r epsilon R L kappa q v g7', positive=True)
    w = sp.sinh(r)*sp.cosh(r)
    sig = 1/(sp.pi*sp.sinh(eps)**2)
    beta = kap*q*v*v/(4*sp.pi)
    rho = kap*q*sig*v*v/2
    h_in = beta*sp.tanh(r)/sp.sinh(eps)**2
    h_out = beta/w
    div_in = clean(sp.diff(w*h_in, r)/w)
    ell = sp.log(sp.tanh(R))-sp.log(sp.tanh(eps))
    cut = (sp.log(sp.tanh(r))-sp.log(sp.tanh(eps)))/ell
    dc = sp.diff(cut, r)
    energy_primitive = 2*sp.pi*L*sp.log(sp.tanh(r))/ell**2
    volume = sp.pi*L*sp.sinh(eps)**2
    bulk_mass_integral = g*g*q*q*v*v*sig*volume
    return dict(r=r, eps=eps, R=R, L=L, kap=kap, q=q, v=v, g=g,
                w=w, sig=sig, beta=beta, rho=rho, h_in=h_in, h_out=h_out,
                normalization=clean(sp.pi*sp.sinh(eps)**2*sig),
                divergence=div_in,
                divergence_residual=clean(div_in-rho),
                exterior_divergence=clean(sp.diff(w*h_out, r)/w),
                matching=clean((h_in-h_out).subs(r, eps)),
                axis_slope=sp.limit(h_in/r, r, 0, dir='+'),
                side_flux=clean(2*sp.pi*L*(w*h_in).subs(r, eps)),
                integrated_source=clean(volume*rho),
                ell=ell, cutoff=cut,
                endpoints=[clean(cut.subs(r, eps)), clean(cut.subs(r, R))],
                harmonic_residual=clean(sp.diff(w*dc, r)),
                wrong_euclidean_residual=clean(sp.diff(r*dc, r)),
                energy=2*sp.pi*L/ell,
                primitive_residual=clean(sp.diff(energy_primitive, r)
                                         - 2*sp.pi*L*w*dc*dc),
                bulk_mass_integral=clean(bulk_mass_integral),
                beta_v_derivative=sp.diff(beta, v))


@lru_cache(maxsize=1)
def vector_quadratic():
    t, v, rho, drho, dtheta, a, q, sig, g = sp.symbols(
        't v rho drho dtheta a q sigma g7', real=True)
    density = sig*(t*t*drho*drho +
                   (v+t*rho)**2*t*t*(dtheta-q*a)**2)/2
    quadratic = sp.expand(density).coeff(t, 2)
    mass = clean(g*g*sp.diff(quadratic, a, 2))
    k0, k1 = sp.symbols('k0 k1', real=True)
    k, e = sp.Matrix([k0, k1]), sp.Matrix([-k1, k0])
    mu, gap, K = sp.symbols('mu delta K', positive=True)
    lower = mu*gap/(2*gap+mu+2*K)
    return dict(v=v, q=q, sig=sig, g=g, a=a, dtheta=dtheta, drho=drho,
                quadratic=quadratic, mass=mass, transverse_dot=(k.T*e)[0],
                mu=mu, gap=gap, K=K, lower=lower,
                lower_identity=clean(1/lower-(2/mu+2*K/(mu*gap)+1/gap)))


@lru_cache(maxsize=1)
def cusp_cutoff():
    s, S, A = sp.symbols('s S A_T', positive=True)
    # The piecewise-linear transition has derivative -1 on [S,S+1].
    energy = sp.integrate(A*sp.exp(-2*s), (s, S, S+1))
    tail = sp.integrate(A*sp.exp(-2*s), (s, S, sp.oo))
    return dict(s=s, S=S, area=A, energy=clean(energy), tail=clean(tail),
                expected= A*(1-sp.exp(-2))*sp.exp(-2*S)/2,
                energy_limit=sp.limit(energy, S, sp.oo),
                tail_limit=sp.limit(tail, S, sp.oo))


def cutoff_quadrature(eps, radius, length=1.0):
    if not 0 < eps < radius or length <= 0:
        raise ValueError('0 < epsilon < radius and positive length required')
    ell = math.log(math.tanh(radius))-math.log(math.tanh(eps))
    val, err = quad(lambda r: 2*math.pi*length /
                    (math.sinh(r)*math.cosh(r)*ell*ell), eps, radius,
                    epsabs=1e-12, epsrel=1e-12)
    exact = 2*math.pi*length/ell
    return dict(epsilon=eps, radius=radius, quadrature=val, formula=exact,
                relative_error=abs(val-exact)/exact, integration_error=err)


def line_sequence(n, length=1.0):
    """Exact radial energy; L2/axial bounds require the proof's fixed axial bump."""
    if not isinstance(n, int) or not 2 <= n <= 26 or length <= 0:
        raise ValueError('integer 2<=n<=26 and positive length required by float range')
    R, eps = math.exp(-n), math.exp(-n*n)
    ell = math.log(math.tanh(R))-math.log(math.tanh(eps))
    return dict(n=n, radius=R, epsilon=eps, radial_energy=2*math.pi*length/ell,
                l2_upper=math.pi*length*math.sinh(R)**2,
                trace_squared_per_unit_axial_norm=1.0)


def modes(N, dim):
    if not isinstance(N, int) or N < 1 or dim not in (1, 2):
        raise ValueError('N>=1 integer and dim 1 or 2 required')
    return list(itertools.product(range(-N, N+1), repeat=dim))


def shell_sums(N):
    grid = modes(N, 2)
    S = sum((Fraction(1, a*a+b*b) for a, b in grid if a or b), Fraction())
    H = sum((Fraction(1, k) for k in range(1, N+1)), Fraction())
    shells = []
    for k in range(1, N+1):
        shell = [(a,b) for a,b in grid if max(abs(a),abs(b)) == k]
        shells.append(dict(k=k, count=len(shell),
                           squared_norm_max=max(a*a+b*b for a,b in shell)))
    return S, H, shells


def fourier_operator(N, eta, dim=2, uniform=False):
    if eta < 0 or not math.isfinite(eta):
        raise ValueError('finite nonnegative coupling required')
    grid = modes(N, dim)
    d = np.array([sum(a*a for a in p) for p in grid], dtype=float)
    return np.diag(d) + eta*(np.eye(len(grid)) if uniform else np.ones((len(grid),len(grid))))


def secular_root(N, eta, dim=2):
    if eta <= 0 or not math.isfinite(eta):
        raise ValueError('finite positive coupling required')
    d = np.array([sum(a*a for a in p) for p in modes(N, dim)
                  if any(p)], dtype=float)
    def equation(lam):
        return lam*(1/eta + np.sum(1/(d-lam)))-1
    return brentq(equation, 0.0, 1-1e-12, xtol=2e-14, rtol=2e-14)


def fourier_witness(N, eta, dim=2):
    matrix = fourier_operator(N, eta, dim)
    values, vectors = eigh(matrix, subset_by_index=(0, 0), driver='evr')
    eig, vec = float(values[0]), vectors[:, 0]
    secular = secular_root(N, eta, dim)
    nonzero = [sum(a*a for a in p) for p in modes(N, dim) if any(p)]
    sum0 = sum(1/d for d in nonzero)
    return dict(N=N, dim=dim, eta=eta, size=len(matrix), eigenvalue=eig,
                secular_root=secular, difference=abs(eig-secular),
                eigenvector_residual=float(np.linalg.norm(matrix@vec-eig*vec)),
                upper_bound=1/(1/eta+sum0), zero_mode_only=eta,
                sum0=sum0)


@lru_cache(maxsize=1)
def renormalization():
    b, r, L, alpha = sp.symbols('lambda_B lambda_R log_ratio alpha', positive=True)
    a = 2*sp.pi*alpha
    forward = b/(1+b*L/a)
    backward = r/(1-r*L/a)
    return dict(b=b, r=r, L=L, alpha=alpha, forward=forward, backward=backward,
                inverse_residual=clean(forward.subs(b, backward)-r),
                bound_difference=clean(a/L-forward),
                positive_bare_limit=sp.limit(forward, L, sp.oo),
                pole=a/r, sign_after_pole=clean(backward.subs(L, 2*a/r)))


@lru_cache(maxsize=1)
def checks():
    a, c, t, v, u, h = (local_action(), covariance(), core_and_cutoff(),
                         vector_quadratic(), renormalization(), character())
    co = cusp_cutoff()
    table = [fourier_witness(N, eta) for eta in (.25, 1.) for N in (1,2,4,8)]
    one = [fourier_witness(N, .25, 1) for N in (1,2,4,8,16,32)]
    lower_one = 1/(4+4/(1-.25))
    shells = [shell_sums(N) for N in range(1,9)]
    return {
        'primitive_q4_character': h['t'] == sp.Matrix([[4,3,5,6,4,2]]) and h['gcd'] == 1,
        'unchanged_global_holonomy_obstruction': h['phase4'] != 1 and h['phase12'] == 1,
        'coupled_stationarity': a['stationary'] == sp.zeros(8,1),
        'hessian_residual_square': a['hessian_residual'] == sp.zeros(8),
        'source_varies_with_scalar': a['q_equation_residual'] == 0 and a['source_response'] != 0,
        'full_gauge_current': a['current_residual'] == 0,
        'missing_source_fails': a['missing_source_cost'] != 0,
        'wrong_scalar_amplitude_fails': a['wrong_amplitude_force'] != 0,
        'finite_gauge_covariance': c['residual'] == sp.zeros(2,1) and c['norm_residual'] == 0,
        'missing_phase_derivative_fails': c['mutant_norm'] != 0,
        'normalized_source_core': t['normalization'] == 1 and t['divergence_residual'] == 0,
        'core_join_and_exterior': t['matching'] == 0 and t['exterior_divergence'] == 0,
        'integrated_source_is_flux': zero(t['side_flux']-t['integrated_source']),
        'transverse_vector_mass': zero(v['mass']-v['g']**2*v['q']**2*v['v']**2*v['sig']),
        'transverse_phase_decouples': v['transverse_dot'] == 0,
        'finite_width_gap_bound': v['lower_identity'] == 0,
        'cutoff_endpoints': t['endpoints'] == [0,1],
        'hyperbolic_harmonic_cutoff': t['harmonic_residual'] == t['primitive_residual'] == 0,
        'wrong_radial_metric_fails': t['wrong_euclidean_residual'] != 0,
        'quadrature_agrees': all(cutoff_quadrature(e,r)['relative_error'] < 2e-10
                                 for e,r in ((.01,.2),(.003,.4))),
        'cusp_exhaustion': zero(co['energy']-co['expected']) and co['energy_limit'] == co['tail_limit'] == 0,
        'square_shell_lower_bound': all(S >= 4*H and all(k['count']==8*k['k']
             and k['squared_norm_max']==2*k['k']**2 for k in sh) for S,H,sh in shells),
        'independent_two_dimensional_spectrum': all(w['difference'] < 3e-10
             and w['eigenvector_residual'] < 3e-10 for w in table),
        'two_dimensional_upper_bound': all(0 < w['eigenvalue'] <= w['upper_bound']+3e-10
             and w['eigenvalue'] < w['zero_mode_only'] for w in table),
        'codimension_one_lower_bound': all(w['difference'] < 3e-10 and
             w['eigenvalue'] >= lower_one-3e-10 for w in one),
        'uniform_mass_control': abs(eigh(fourier_operator(4,.25,uniform=True),
             eigvals_only=True,subset_by_index=(0,0))[0]-.25) < 3e-10,
        'no_higgs_control': abs(eigh(fourier_operator(4,0.),
             eigvals_only=True,subset_by_index=(0,0))[0]) < 3e-10,
        'renormalization_inverse': u['inverse_residual'] == 0,
        'positive_bare_limit_and_inverse_sign': u['positive_bare_limit'] == 0
             and zero(u['sign_after_pole']+u['r']),
    }


def main():
    started = time.monotonic()
    verdicts = {k: bool(v) for k,v in checks().items()}
    report = dict(
        scope='Added H bosonic tube model; bare bulk-L2 vector limit. No chiral-domain transfer, anomaly completion, empirical fit or TOE.',
        sympy_version=sp.__version__,
        checks=verdicts,
        two_dimensional=[fourier_witness(N,eta) for eta in (.25,1.) for N in (1,2,4,8)],
        one_dimensional=[fourier_witness(N,.25,1) for N in (1,2,4,8,16,32)],
        cutoff_quadratures=[cutoff_quadrature(e,r) for e,r in ((.01,.2),(.003,.4))],
        line_sequence=[line_sequence(n) for n in (2,3,4,6,8,12)],
        all_class_proof='DEFECT_GAUGE_PROOF.md; numerical controls do not replace the analytic argument',
        elapsed_seconds=time.monotonic()-started)
    print(json.dumps(report, indent=2, sort_keys=True))
    if not all(verdicts.values()):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
