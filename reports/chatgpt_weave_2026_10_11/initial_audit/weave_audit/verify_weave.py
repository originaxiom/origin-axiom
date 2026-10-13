#!/usr/bin/env python3
"""Independent audit of A Weave of Two Records (October 2026).

No Origin Axiom repository code is imported. Exact checks use SymPy; numerical
checks use independent theta series in tau and the Dedekind eta product.
Numerical checks are not interval certificates. See mathematical_notes.md for proofs.
Run: python verify_weave.py --dps 100 --points 120 --output results.json
"""
from __future__ import annotations
import argparse
from collections import deque
import json
import math
from pathlib import Path
import platform
import time

import mpmath as mp
import numpy as np
import sympy as sp
from sympy.polys.matrices import DomainMatrix

U = sp.symbols('u2 u3 u4')


def theta(tau):
    """Theta constants from their tau-series; no principal-nome-root ambiguity."""
    tau = mp.mpc(tau)
    if tau.imag <= 0:
        raise ValueError('tau must be in the upper half-plane')
    nmax = int(mp.ceil(mp.sqrt((mp.mp.dps + 20) * mp.log(10) / (mp.pi * tau.imag)))) + 2
    even_terms = [mp.exp(mp.pi * 1j * tau * n*n) for n in range(1, nmax + 1)]
    t2 = 2 * mp.fsum(mp.exp(mp.pi * 1j * tau * (mp.mpf(n) + mp.mpf('.5'))**2)
                     for n in range(nmax + 1))
    t3 = 1 + 2 * mp.fsum(even_terms)
    t4 = 1 + 2 * mp.fsum((-1)**n * v for n, v in enumerate(even_terms, 1))
    return [t2, t3, t4]


def eta(tau):
    q = mp.exp(2 * mp.pi * 1j * tau)
    return mp.exp(mp.pi * 1j * tau / 12) * mp.qp(q, q)


def f_spectrum(tau):
    th = theta(tau)
    et = eta(tau)
    f = sum(abs(t)**4 for t in th) / abs(et)**4
    # Unitary diagonal congruence makes the zero-diagonal symmetric matrix real
    # with these off-diagonals, preserving all its singular values.
    a, b, c = abs(th[2])**2, abs(th[1])**2, abs(th[0])**2
    y = mp.matrix([[0, a, b], [a, 0, c], [b, c, 0]])
    sv = sorted([abs(v) for v in mp.eigsy(y, eigvals_only=True)], reverse=True)
    return f, [v / sv[0] for v in sv]


def monomial_product(g, h):
    """M[i,p[i]]=zeta8**e[i], exact exponent/permutation representation."""
    p, e = g
    q, f = h
    return tuple(q[p[i]] for i in range(3)), tuple((e[i] + f[p[i]]) % 8 for i in range(3))


def reduce_cyclotomic(coeff):
    # zeta8**4 = -1; 1,zeta8,zeta8**2,zeta8**3 are Q-linearly independent.
    return [coeff[j] - coeff[j+4] for j in range(4)]


def exact_group():
    identity = ((0, 1, 2), (0, 0, 0))
    generators = [((2, 1, 0), (1, 1, 1)), ((0, 2, 1), (1, 7, 7))]
    found = {identity}
    queue = deque([identity])
    while queue:
        g = queue.popleft()
        for h in generators:
            gh = monomial_product(g, h)
            if gh not in found:
                found.add(gh)
                queue.append(gh)
        if len(found) > 10000:
            raise RuntimeError('Unexpected group growth')
    norm, self_square = [0]*8, [0]*8
    for p, e in found:
        diagonal = [e[i] for i in range(3) if p[i] == i]
        for a in diagonal:
            for b in diagonal:
                norm[(a-b) % 8] += 1
                self_square[(a+b) % 8] += 1
    norm, self_square = reduce_cyclotomic(norm), reduce_cyclotomic(self_square)
    assert len(found) == 96 and norm == [96, 0, 0, 0] and self_square == [0]*4
    central = sorted(e[0] for p, e in found if p == (0, 1, 2) and len(set(e)) == 1)
    return {'order': len(found), 'character_norm': '1 exactly',
            'character_inner_product_with_conjugate': '0 exactly',
            'scalar_zeta8_exponents': central, 'T_eigenvalue_turns': ['1/8', '3/8', '7/8']}


def forms_ops(k):
    """Degree-k polynomials modulo u3^2=u2^2+u4^2.

    Theta-squared transformations: u(-1/tau)=tau*(-i)*swap13*u(tau),
    u(tau+1)=(i*u2,u4,u3). Columns hold images of basis monomials.
    """
    mons = [(a, b, k-a-b) for b in (0, 1) for a in range(k-b+1)]
    index = {m: j for j, m in enumerate(mons)}
    s, t = sp.zeros(len(mons)), sp.zeros(len(mons))
    for j, (a, b, c) in enumerate(mons):
        s[index[(c, b, a)], j] = (-sp.I)**k
        for h in range(c//2 + 1):
            m = (a+2*h, c % 2, b+2*(c//2-h))
            t[index[m], j] += sp.I**a * math.comb(c//2, h)
    return s, t, mons


def coupling_ops(kind):
    if kind == 'diag':
        pairs = [(i, i) for i in range(3)]
    elif kind in ('off', 'anti'):
        pairs = [(i, j) for i in range(3) for j in range(i+1, 3)]
    elif kind == 'sym':
        pairs = [(i, j) for i in range(3) for j in range(i, 3)]
    elif kind == 'full':
        pairs = [(i, j) for i in range(3) for j in range(3)]
    else:
        raise ValueError(kind)

    def op(p, exponents):
        c = sp.zeros(len(pairs))
        for row, (i, j) in enumerate(pairs):
            a, b, sign = p[i], p[j], 1
            if kind != 'full' and a > b:
                a, b = b, a
                if kind == 'anti':
                    sign = -1
            phase = sp.I**((-(exponents[i]+exponents[j])//2) % 4)
            c[row, pairs.index((a, b))] = sign * phase
        return c
    return op((2, 1, 0), (1, 1, 1)), op((0, 2, 1), (1, 7, 7)), pairs


def constraint_matrix(k, kind):
    fs, ft, mons = forms_ops(k)
    cs, ct, pairs = coupling_ops(kind)
    n, m = len(mons), len(pairs)
    mat = (sp.kronecker_product(sp.eye(m), fs)-sp.kronecker_product(cs, sp.eye(n))).col_join(
           sp.kronecker_product(sp.eye(m), ft)-sp.kronecker_product(ct, sp.eye(n)))
    return mat, mons, pairs


def coupling_dimensions():
    rows = []
    for k in [1, 3, 5, 7, 9, 11]:
        dims = {}
        for kind in ['diag', 'off', 'anti']:
            mat, _, _ = constraint_matrix(k, kind)
            dims[kind] = mat.cols - DomainMatrix.from_Matrix(mat).to_field().rank()
        rows.append({'weight': k, **dims, 'symmetric': dims['diag']+dims['off'],
                     'full': sum(dims.values())})
    assert [r['symmetric'] for r in rows] == [1, 1, 3, 3, 5, 5]
    assert [r['full'] for r in rows] == [1, 2, 4, 5, 7, 8]
    return rows


def coupling_basis(k, kind):
    mat, mons, pairs = constraint_matrix(k, kind)
    polynomials = [sp.prod(U[j]**m[j] for j in range(3)) for m in mons]
    result = []
    for vec in mat.nullspace():
        y = sp.zeros(3)
        for row, (a, b) in enumerate(pairs):
            val = sp.factor(sum(vec[row*len(mons)+h]*polynomials[h] for h in range(len(mons))))
            y[a, b] = val
            if kind in ('sym', 'off'):
                y[b, a] = val
            elif kind == 'anti':
                y[b, a] = -val
        result.append(y)
    return result


def vector_weight_three():
    fs, ft, mons = forms_ops(3)
    a_s = -sp.I*sp.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    a_t = sp.Matrix([[sp.I, 0, 0], [0, 0, 1], [0, 1, 0]])
    n = len(mons)
    mat = (sp.kronecker_product(sp.eye(3), fs)-sp.kronecker_product(a_s, sp.eye(n))).col_join(
           sp.kronecker_product(sp.eye(3), ft)-sp.kronecker_product(a_t, sp.eye(n)))
    basis = mat.nullspace()
    assert len(basis) == 1
    pol = [sp.prod(U[j]**m[j] for j in range(3)) for m in mons]
    v = sp.Matrix([sp.factor(sum(basis[0][r*n+h]*pol[h] for h in range(n))) for r in range(3)])
    at_cusp = v.subs(dict(zip(U, [0, 1, 1])))
    assert at_cusp != sp.zeros(3, 1)
    return {'dimension_M3_A': 1, 'basis': str(v), 'cusp_value': str(at_cusp),
            'consequence': 'No cusp-vanishing weight-3 A-valued form; hence M_(3/2)(rho)=0 under the stated eta^3 correspondence.'}


def exact_counterexample(s3, a3):
    root3 = sp.sqrt(3)
    # Values of u/u4 at omega=(-1+i*sqrt(3))/2 in the standard theta branches.
    special = dict(zip(U, [(1-sp.I*root3)/2, (root3-sp.I)/2, 1]))
    y = (s3+2*a3).subs(special).applyfunc(sp.simplify)
    gram = (y.conjugate().T*y).applyfunc(sp.simplify)
    variable = sp.Symbol('lambda')
    cp = sp.factor(gram.charpoly(variable).as_expr())
    assert sp.expand(cp-(variable-27)*(variable-12)*(variable-3)) == 0
    return {'symmetric_basis': str(s3), 'antisymmetric_basis': str(a3),
            'Y_divided_by_u4_cubed': str(y), 'YdaggerY_characteristic_polynomial': str(cp),
            'singular_value_ratio': '3:2:1',
            'scope': 'Full T tensor T, weight 3; does not refute a symmetric-only degeneracy statement.'}


def elementary_checks():
    l = sp.Matrix([[1, 1], [0, 1]])
    r = sp.Matrix([[1, 0], [1, 1]])
    p = sp.Matrix([[0, 1], [1, 0]])
    s = r*l.inv()*r
    assert (l*p)**2 == l*r
    assert s**2 == -sp.eye(2)
    x, y, z = sp.symbols('x y z')
    fixed = sp.solve([z-y, x*z-y-z, z-x, y*z-x-z], [x, y, z])
    assert set(fixed) == {(0, 0, 0), (2, 2, 2)}
    return {'LP': str(l*p), 'LR': str(l*r), 'RL_inverse_R': str(s),
            'square': str(s**2), 'common_Frcke_fixed_points': [list(map(str, pt)) for pt in fixed]}


def numerical_checks(points):
    phi = (1+mp.sqrt(5))/2
    gold = [mp.mpf(1), 1/phi, 1/phi**2]
    max_f, max_ratio, max_modular, max_transform = [mp.mpf(0)]*4
    for j in range(points):
        angle = mp.mpf('.08') + (mp.pi-mp.mpf('.16'))*j/(points-1)
        tau = mp.mpf('.5')+mp.sqrt(5)/2*mp.exp(1j*angle)
        f, spectrum = f_spectrum(tau)
        max_f = max(max_f, abs(f-8))
        max_ratio = max(max_ratio, max(abs(a-b) for a, b in zip(spectrum, gold)))
        if j % max(1, points//12) == 0:
            z, h = tau/(1-2*tau), 1-2*tau
            u = [t*t for t in theta(tau)]
            uz, u5 = [t*t for t in theta(z)], [t*t for t in theta(5*z)]
            lhs = uz[1]*u5[1]-uz[0]*u5[0]-uz[2]*u5[2]
            rhs = 8*eta(z)**2*eta(5*z)**2
            max_modular = max(max_modular, abs(lhs-rhs)/max(1, abs(rhs)))
            expected = [h*u[0], h*u[1], -h*u[2]]
            max_transform = max(max_transform,
                max(abs(a-b)/max(1, abs(b)) for a, b in zip(uz, expected)),
                abs(eta(z)**2-h*mp.exp(mp.pi*1j/3)*eta(tau)**2)/max(1, abs(eta(z)**2)))
    # Test the holomorphic identity away from the axis as well.
    for z in [mp.mpc('.12', '.71'), mp.mpc('-.91', '.32'), mp.mpc('1.31', '.86')]:
        uz, u5 = [t*t for t in theta(z)], [t*t for t in theta(5*z)]
        lhs = uz[1]*u5[1]-uz[0]*u5[0]-uz[2]*u5[2]
        rhs = 8*eta(z)**2*eta(5*z)**2
        max_modular = max(max_modular, abs(lhs-rhs)/max(1, abs(rhs)))
    threshold = mp.mpf(10)**(-mp.mp.dps+15)
    assert max(max_f, max_ratio, max_modular, max_transform) < threshold
    controls = []
    for tau in [mp.mpc(0, 2), mp.mpc(0, mp.mpf('.6')),
                mp.mpc(-mp.mpf('.5'), mp.sqrt(3)/2)]:
        f, masses = f_spectrum(tau)
        controls.append({'tau': str(tau), 'F': mp.nstr(f, 24),
                         'normalized_masses': [mp.nstr(v, 24) for v in masses]})
    return {'decimal_precision': mp.mp.dps, 'axis_points': points,
            'max_abs_F_minus_8': mp.nstr(max_f, 12),
            'max_normalized_singular_value_error': mp.nstr(max_ratio, 12),
            'degree_five_identity_max_scaled_residual': mp.nstr(max_modular, 12),
            'axis_transformation_max_scaled_residual': mp.nstr(max_transform, 12),
            'off_axis_controls': controls,
            'warning': 'High-precision numerical checks, not interval-certified proofs.'}


def quark_local_rank(s3, a3):
    f_s, f_a = sp.lambdify(U, s3, 'numpy'), sp.lambdify(U, a3, 'numpy')
    def observations(p):
        u = [complex(v*v) for v in theta(complex(p[0], p[1]))]
        ys, ya = f_s(*u), f_a(*u)
        yu, yd = ys+complex(p[2], p[3])*ya, ys+complex(p[4], p[5])*ya
        eu, uu = np.linalg.eigh(yu.conj().T@yu)
        ed, ud = np.linalg.eigh(yd.conj().T@yd)
        mu, md = np.sqrt(np.maximum(eu, 0)), np.sqrt(np.maximum(ed, 0))
        v = uu.conj().T@ud
        return np.array([mu[0]/mu[2], mu[1]/mu[2], md[0]/md[2], md[1]/md[2],
                         abs(v[0, 1])**2, abs(v[0, 2])**2, abs(v[1, 2])**2,
                         (v[0, 0]*v[1, 1]*np.conj(v[0, 1])*np.conj(v[1, 0])).imag])
    p = np.array([.23, 1.17, .4, .7, -.6, .3])
    step = 1e-5
    jac = np.column_stack([(observations(p+step*np.eye(6)[j])-
                            observations(p-step*np.eye(6)[j]))/(2*step) for j in range(6)])
    singular = np.linalg.svd(jac, compute_uv=False)
    assert singular[-1] > .01
    return {'point_ReTau_ImTau_ReZu_ImZu_ReZd_ImZd': p.tolist(),
            'jacobian_singular_values': singular.tolist(), 'numerical_local_rank': 6,
            'warning': 'Local numerical check, not a fit to quark data or a global prediction theorem.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dps', type=int, default=100)
    parser.add_argument('--points', type=int, default=120)
    parser.add_argument('--output', type=Path, default=Path('results.json'))
    args = parser.parse_args()
    if args.dps < 40 or args.points < 3:
        parser.error('Use --dps >= 40 and --points >= 3')
    mp.mp.dps = args.dps
    start = time.time()
    s3, a3 = coupling_basis(3, 'sym')[0], coupling_basis(3, 'anti')[0]
    results = {
        'scope': 'Independent selected-claim audit, not a rerun of the full project repository.',
        'versions': {'python': platform.python_version(), 'sympy': sp.__version__,
                     'mpmath': mp.__version__, 'numpy': np.__version__},
        'elementary_exact': elementary_checks(),
        'theta_representation_exact': exact_group(),
        'coupling_dimensions_exact': coupling_dimensions(),
        'weight_three_vector_forms_exact': vector_weight_three(),
        'omega_counterexample_exact': exact_counterexample(s3, a3),
        'theta_numerical_checks': numerical_checks(args.points),
        'quark_shape_local_rank': quark_local_rank(s3, a3),
        'historical_JUNO_comparison': {
            'source': 'JUNO arXiv:2609.37895v1, September 2026',
            'sin2theta12': .3036, 'reported_error': .0064, 'illustrative_sin2theta13': .022,
            'TM1': 1-2/(3*(1-.022)), 'TM2': 1/(3*(1-.022)),
            'TM1_simple_pull': (1-2/(3*(1-.022))-.3036)/.0064,
            'TM2_simple_pull': (1/(3*(1-.022))-.3036)/.0064,
            'warning': 'Illustrative one-dimensional Gaussian pulls, not global-fit significances.'},
        'elapsed_seconds': time.time()-start,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(results, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()
