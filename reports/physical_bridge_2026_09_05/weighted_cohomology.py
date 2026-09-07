"""R18: controls of the declared weighted-complex comparison proof.

These finite/symbolic controls do not replace its analytic domain proof.
No physical source selection, PDE eigenfunction mesh, or TOE certificate.
"""
from __future__ import annotations

from functools import lru_cache
import importlib.util
import json
import math
from pathlib import Path
import time

import mpmath as mp
import numpy as np
import sympy as sp


def load_local(name, filename):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


cd = load_local('r18_frozen_exterior', 'charged_domain.py')
ct = load_local('r18_frozen_cusp', 'cusp_tail.py')
gs = load_local('r18_frozen_global', 'global_singular.py')
r, x, y = cd.COORDS


def strong_class(q, beta, cusp_totals):
    values = (q, *beta, *cusp_totals)
    if not beta or not cusp_totals or not all(math.isfinite(float(v)) for v in values):
        raise ValueError('finite, nonempty source and cusp data required')
    if q == 0 or any(b <= 0 or abs(q)*b < 1 for b in beta) or any(Q <= 0 for Q in cusp_totals):
        raise ValueError('outside the declared strong same-sign source class')
    return 'relative_T' if q > 0 else 'relative_E'


@lru_cache(maxsize=1)
def norm_and_conjugacy():
    H = r*r+x*y+r*x
    dH = cd.exterior({(): H})
    weight_rows, conjugacy, wrong = [], [], []
    a, s, h = sp.symbols('a s h', real=True)
    for j in cd.BASIS:
        form = {j: 1+r+x+y}
        residual = cd.add(cd.exterior(cd.scale(form, sp.exp(H))),
                          cd.scale(cd.HYP.dq(form, dH), -sp.exp(H)))
        conjugacy.append(residual == {})
        mutant = cd.add(cd.exterior(cd.scale(form, sp.exp(-H))),
                       cd.scale(cd.HYP.dq(form, dH), -sp.exp(-H)))
        wrong.append(mutant != {})
        epsilon, eps_t = int(1 in j), int(2 in j)
        p = 1-2*a-2*epsilon
        exact = sp.tanh(r)**(-2*a)*cd.HYP.volume/cd.HYP.basis_length(j)**2
        ratio = (sp.tanh(r)/r)**(-2*a)*(sp.sinh(r)/r)**(1-2*epsilon)*sp.cosh(r)**(1-2*eps_t)
        # Positive r makes the real-power splitting legitimate.
        ratio_error = sp.powsimp(sp.expand_power_base(exact/r**p/ratio, force=True), force=True)-1
        cusp_degree = len([i for i in j if i != 0])
        cusp_metric = cd.MetricForms((1, sp.exp(-s), sp.exp(-s)))
        cusp_weight = sp.simplify(sp.exp(-2*h)*cusp_metric.volume/cusp_metric.basis_length(j)**2)
        cusp_target = sp.exp((2*cusp_degree-2)*s-2*h)
        weight_rows.append(dict(basis=list(j), power=str(p), ratio_error=str(sp.simplify(ratio_error)),
                               ratio_limits=[str(sp.limit(ratio.subs(a, v), r, 0))
                                             for v in (-2, -1, 1, 2)],
                               cusp_degree=cusp_degree, cusp_error=str(sp.simplify(cusp_weight-cusp_target))))
    # Under the changed Hilbert norm the scalar factors cancel identically.
    unitary = sp.simplify(sp.exp(-2*H)*sp.exp(H)**2-1)
    return dict(rows=weight_rows, conjugacy=conjugacy, wrong_sign_nonzero=wrong,
                unitary_error=str(unitary), original_unweighted_multiplier_unbounded=True)


def hardy_bounds():
    u, R, t, z = sp.symbols('u R t z', positive=True)
    # Forward: p=1-u; integrate first in the inner variable.
    forward_inner = sp.integrate(z**(u-1), (z, 0, t))
    forward = sp.integrate(t**(1-u)*forward_inner, (t, 0, R))
    # Backward: p=u-1; reverse the double-integral order first.
    backward_inner = sp.integrate(t**(u-1), (t, 0, z))
    backward = sp.integrate(z**(1-u)*backward_inner, (z, 0, R))
    target = R**2/(2*u)
    return dict(forward=str(sp.simplify(forward-target)), backward=str(sp.simplify(backward-target)),
                forward_expression=str(forward), backward_expression=str(backward))


def constant_trace_rows():
    out = []
    for a in (sp.Rational(-2), sp.Rational(-1), sp.Rational(0), sp.Rational(1, 2), sp.Rational(1), sp.Rational(2)):
        for angular in (0, 1):
            p = 1-2*a-2*angular
            out.append(dict(a=str(a), angular=angular, p=str(p), constant_L2=bool(p > -1),
                            forward_bounded=bool(p < 1), backward_bounded=bool(p > -1)))
    return out


def hardy_profiles():
    rows = []
    with mp.workdps(40):
        for a in (-2, -1.5, -1, 1, 1.5, 2):
            for angular in (0, 1):
                p = mp.mpf(1)-2*mp.mpf(a)-2*angular
                b = (1-p)/2 if a > 0 else -p/2
                kappa = mp.mpf('0.7')
                for radius in ('1', '0.3'):
                    R = mp.mpf(radius)
                    def primitive(z, power):
                        return mp.log(z) if power == -1 else z**(power+1)/(power+1)
                    def K(z):
                        zvalue = primitive(z, b)+1j*kappa*primitive(z, b+1)
                        if a > 0:
                            return zvalue  # b>0, so the zero endpoint contributes zero.
                        return zvalue-primitive(R, b)-1j*kappa*primitive(R, b+1)
                    input_norm = R**(p+2*b+1)/(p+2*b+1)+kappa**2*R**(p+2*b+3)/(p+2*b+3)
                    output_norm = mp.quad(lambda z: z**p*abs(K(z))**2, [0, R/4, R])
                    bound = R**2/(2*(1-p if a > 0 else p+1))
                    rows.append(dict(a=a, angular=angular, p=float(p), radius=float(R),
                                     log_primitive=bool(b == -1 or b+1 == -1),
                                     squared_ratio=float(output_norm/input_norm), squared_bound=float(bound),
                                     normalized_ratio=float(output_norm/input_norm/bound)))
    return rows


def cusp_slope_controls():
    out = []
    for row in ct.radial_controls():
        for j in range(3):
            hp = row['hprime']
            hp0, _ = ct.radial(row['start'], row['q'], row['b'], row['c'])
            alpha = abs(float(hp0))-1
            phi_prime = j-1-hp
            margin = (-phi_prime if row['q'] > 0 else phi_prime)-alpha
            out.append(dict(q=row['q'], beta=list(row['beta']), c=row['c'], s=row['s'], j=j,
                            alpha=alpha, margin=margin, derivative_error=row['derivative_error']))
    return out


def volterra_controls():
    out = []
    b = math.pi*3/(math.sqrt(3)/2)
    for q in (-2., 2.):
        for c in (-20., 0., 20.):
            S = ct.sufficient_height(q, b, c)
            hp, _ = ct.radial(S, q, b, c)
            alpha = abs(float(hp))-1
            for j in range(3):
                norms, bare = [], []
                for n in (64, 128):
                    z = (np.arange(n)+.5)*6/n
                    delta = z/alpha
                    # Stable even when S+delta would round back to S.
                    hchange = q*math.exp(2*S)*((b*S+c)*np.expm1(2*delta)+b*delta*np.exp(2*delta))
                    phi = (j-1)*delta-hchange
                    diff = phi[:, None]-phi[None, :]
                    direction = z[:, None] > z[None, :] if q > 0 else z[:, None] < z[None, :]
                    kernel = np.zeros_like(diff)
                    kernel[direction] = np.exp(diff[direction])
                    # Norm here is alpha times the physical operator norm.
                    norms.append(float(np.linalg.norm(kernel*(6/n), 2)))
                    bare.append(float(np.linalg.norm(direction.astype(float)*(6/n), 2)))
                out.append(dict(q=q, c=c, j=j, start=S, alpha=alpha,
                                scaled_norms=norms, unweighted_scaled_norms=bare,
                                refinement_change=abs(norms[1]-norms[0])))
    return out


def radial_homotopy(form, endpoint):
    z = sp.Symbol('integration_z', real=True)
    return cd.clean({j[1:]: sp.integrate(c.subs(r, z), (z, endpoint, r))
                     for j, c in form.items() if j and j[0] == 0})


def averaged(form, homotopy=False):
    z = sp.Symbol('slice_z', real=True)
    eta = 6*(z-1)*(2-z)
    source = radial_homotopy(form, z) if homotopy else {j: c.subs(r, z) for j, c in form.items() if 0 not in j}
    return cd.clean({j: sp.integrate(eta*c, (z, 1, 2)) for j, c in source.items()})


@lru_cache(maxsize=1)
def homotopy_controls():
    u = {j: (i+1)*(1+r+r*r*x+y*x) for i, j in enumerate(cd.BASIS)}
    K = lambda f: averaged(f, True)
    P = lambda f: averaged(f, False)
    diff = lambda f: cd.exterior(f)
    relative = cd.scale(u, r**4)
    K0 = lambda f: radial_homotopy(f, 0)
    chi = 3*r*r-2*r**3
    def A(f, omit=False):
        out = cd.add(cd.scale(f, 1-chi), cd.scale(P(f), chi))
        return out if omit else cd.add(out, cd.scale(cd.wedge(diff({(): chi}), K(f)), -1))
    correct = cd.add(diff(K(u)), K(diff(u)), P(u), cd.scale(u, -1))
    relative_error = cd.add(diff(K0(relative)), K0(diff(relative)), cd.scale(relative, -1))
    cutoff_error = cd.add(diff(A(u)), cd.scale(A(diff(u)), -1))
    missing_term = cd.add(diff(A(u, True)), cd.scale(A(diff(u), True), -1))
    # Relative cap is y=0. Only components containing dy may survive there.
    cap_input = {j: c if 2 in j else y*c for j, c in u.items()}
    cap_K = radial_homotopy(cap_input, 1)
    cap_trace = cd.clean({j: c.subs(y, 0) for j, c in cap_K.items() if 2 not in j})
    eps, t = sp.symbols('epsilon t', positive=True)
    bump_norm = 2*sp.integrate((1-t/eps)**2/eps, (t, 0, eps))
    bump_integral = 2*sp.integrate((1-t/eps)/sp.sqrt(eps), (t, 0, eps))
    return dict(averaged_identity=correct == {}, relative_identity=relative_error == {},
                cutoff_commutes=cutoff_error == {}, omitted_cutoff_term_fails=missing_term != {},
                projection_nonzero=P(u) != {}, omitted_projection_fails=cd.add(diff(K(u)), K(diff(u)), cd.scale(u, -1)) != {},
                cap_preserved=cap_trace == {}, bump_norm=str(bump_norm),
                bump_point_square=str(1/eps), bump_integral=str(bump_integral),
                bump_point_limit=str(sp.limit(1/eps, eps, 0, dir='+')))


def parametrix_algebra():
    dC = sp.zeros(4)
    dC[2, 0] = 1
    KC = dC.T
    PiC = sp.eye(4)-dC*KC-KC*dC
    dG = sp.zeros(6)
    dG[3, 0], dG[5, 2] = 1, 2
    J = sp.zeros(6)
    J[2, 5] = sp.Rational(1, 2)
    i = sp.zeros(6, 4)
    for a, b in ((0, 0), (1, 1), (3, 2), (4, 3)):
        i[a, b] = 1
    p = i.T
    B = sp.diag(sp.Matrix([[1, 2, 0], [0, 1, 1], [0, 0, 1]]), sp.Matrix([[2, 1, 0], [0, 1, 2], [0, 0, 1]]))
    dG, J, i, p = B*dG*B.inv(), B*J*B.inv(), B*i, p*B.inv()
    Q, Pi = J+i*KC*p, i*PiC*p
    return dict(chain_nilpotent=dG*dG == sp.zeros(6),
                chain_i=dG*i == i*dC, chain_p=p*dG == dC*p,
                original_homotopy=dG*J+J*dG == sp.eye(6)-i*p,
                composed_parametrix=dG*Q+Q*dG == sp.eye(6)-Pi,
                projection_kills_exact=Pi*dG == sp.zeros(6),
                projection_closed=dG*Pi == sp.zeros(6), projection_rank=int(Pi.rank()),
                omitted_core_homotopy_fails=dG*J+J*dG != sp.eye(6)-Pi,
                projection_is_not_orthogonal=Pi != Pi.T)


def topology_controls():
    return [gs.cellular_pair(k) for k in range(4)]+[gs.cellular_pair(3, 8, 2)]


def run():
    start = time.monotonic()
    result = dict(norms=norm_and_conjugacy(), hardy_exact=hardy_bounds(), traces=constant_trace_rows(),
                  hardy_profiles=hardy_profiles(), slopes=cusp_slope_controls(), volterra=volterra_controls(),
                  homotopies=homotopy_controls(), parametrix=parametrix_algebra(), topology=topology_controls())
    result['runtime_seconds'] = time.monotonic()-start
    result['scope'] = 'controls plus separate analytic proof; maximal strong-source complex, not physical domain selection'
    return result


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True, default=str), flush=True)
