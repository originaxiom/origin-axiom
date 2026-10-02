"""R80 conditional local source admission; not all physical profiles or vacua."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sympy as s


def clean(a):
    return a.applyfunc(s.cancel) if isinstance(a, s.MatrixBase) else s.cancel(a)


def norm(a):
    return s.expand(s.trace(a.H*a))


def element(n, i, j):
    a = s.zeros(n)
    a[i, j] = 1
    return a


def projector(n, k):
    if not 0 < k < n:
        raise ValueError('Proper nonzero rank required')
    return s.diag(*([1]*k+[0]*(n-k)))


def generic(n, m=None):
    m = n if m is None else m
    return s.Matrix(n, m, lambda i, j: s.Symbol(f'r{i}_{j}', real=True)
                    +s.I*s.Symbol(f'i{i}_{j}', real=True))


@lru_cache(None)
def block_controls():
    checks = {}
    for n in range(2, 7):
        z = generic(n)
        mu = clean(z*z.H-z.H*z)
        for k in range(1, n):
            p = projector(n, k); xi = n*p-k*s.eye(n)
            b, c = z[:k, k:], z[k:, :k]
            checks[f'moment_{n}_{k}'] = clean(s.trace(xi*mu)-n*(norm(b)-norm(c))) == 0
            upper = z.copy(); upper[k:, :k] = s.zeros(n-k, k)
            a = (upper-upper.H)/2; psi = (upper+upper.H)/2
            contraction = s.trace(psi*(a*xi-xi*a))
            checks[f'bulk_{n}_{k}'] = clean(contraction+s.Rational(n, 2)*norm(b)) == 0
    z = s.Matrix([[1+s.I, 2-s.I], [3+2*s.I, -1-s.I]])
    p = projector(2, 1); xi = 2*p-s.eye(2)
    u = s.Matrix([[s.Rational(3, 5), 4*s.I/5], [4*s.I/5, s.Rational(3, 5)]])
    zp, pp = clean(u*z*u.H), clean(u*p*u.H)
    checks['unitary_fixture'] = clean(u.H*u) == s.eye(2)
    checks['whole_projector_transport'] = clean(s.trace((2*pp-s.eye(2))*(zp*zp.H-zp.H*zp))
                                                    -s.trace(xi*(z*z.H-z.H*z))) == 0
    checks['untransported_projector_detected'] = clean(s.trace(xi*(zp*zp.H-zp.H*zp))
                                                          -s.trace(xi*(z*z.H-z.H*z))) != 0
    up, down = element(5, 0, 4), element(5, 4, 0)
    current = up*up.H-up.H*up
    checks['lower_full_current_match'] = current+down*down.H-down.H*down == s.zeros(5)
    checks['upper_full_current_fails'] = current+up*up.H-up.H*up != s.zeros(5)
    checks['constant_is_not_parallel'] = up*down-down*up != s.zeros(5)
    xi5 = 5*projector(5, 4)-4*s.eye(5)
    checks['positive_bulk_projection'] = s.trace(xi5*current) == 5
    checks['negative_lower_projection'] = s.trace(xi5*(down*down.H-down.H*down)) == -5
    checks['split_zero_control'] = norm(s.zeros(4, 1)) == 0
    return {'checks': checks, 'symbolic_block_cases': 15}


@lru_cache(None)
def peripheral_controls():
    path = Path(__file__).with_name('cross_branch_positives.py')
    spec = importlib.util.spec_from_file_location('r80_reuse_r75', path)
    old = importlib.util.module_from_spec(spec); spec.loader.exec_module(old)
    q = old.Q; m, n = old.literal()
    lv = old.sym_word('nMNmmNMn', {'m': m, 'n': n})
    d = clean((lv-s.eye(4)).det())
    expected = (q-1)**3*(q**-3-1)
    numerator, denominator = s.fraction(d)
    g = q**6-34*q**3+1
    v = s.Matrix(s.symbols('v0:4'))
    lw = lv.row_join(v).col_join(s.zeros(1, 4).row_join(s.ones(1, 1)))
    z = generic(5)
    comm = clean(lw*z-z*lw)
    checks = {
        'actual_longitude_gap': clean(d-expected) == 0,
        'numerator_coprime_actual_roots': s.gcd(numerator, g) == 1,
        'denominator_coprime_actual_roots': s.gcd(denominator, g) == 1,
        'q_zero_not_root': g.subs(q, 0) != 0,
        'q_one_gap_fails': d.subs(q, 1) == 0,
        'q_one_not_actual_root': g.subs(q, 1) != 0,
        'commutation_forces_lower_block': clean(comm[4, :4]+z[4, :4]*(lv-s.eye(4))) == s.zeros(1, 4),
        'image_with_any_extension_column': lw[4, :4] == s.zeros(1, 4) and lw[4, 4] == 1,
        'bad_polynomial_common_root_detected': s.gcd(g, g) != 1,
    }
    return {'checks': checks, 'gap_determinant': str(s.factor(d)),
            'reused_primitives': ['R75 literal', 'R75 sym_word'],
            'not_recomputed': 'cohomology, triplet census, global metric, physical spectrum'}


@lru_cache(None)
def boundary_controls():
    t = s.Symbol('t', positive=True)
    h = (1-t*t)/(2*(1+t*t)); b = 2*t/(1+t*t)
    c = s.Matrix([[h, b], [0, -h]])
    xi = s.diag(1, -1); psi = (c+c.H)/2
    residual = clean(t*(c+c.H).diff(t)+c*c.H-c.H*c)
    bulk = s.integrate(b*b/t, (t, s.Rational(1, 2), 2))
    flux = clean(s.trace(xi*psi).subs(t, 2)-s.trace(xi*psi).subs(t, s.Rational(1, 2)))
    checks = {
        'full_real_residual_zero': residual == s.zeros(2),
        'one_coordinate_flat': c*c-c*c == s.zeros(2),
        'second_component_curvature_detected': clean(c*xi-xi*c) != s.zeros(2),
        'nonzero_extension': b != 0,
        'bulk_norm_positive': bulk == s.Rational(6, 5),
        'outward_flux_negative': flux == -s.Rational(6, 5),
        'complete_boundary_identity': clean(2*bulk+2*flux) == 0,
        'flux_omission_rejected': 2*bulk != 0,
        'wrong_outward_sign_rejected': 2*bulk-2*flux != 0,
        'finite_background_norm': clean(s.trace(psi.H*psi)-2*h*h-b*b/2) == 0,
    }
    return {'checks': checks, 'bulk_norm': str(bulk), 'outward_flux': str(flux)}


@lru_cache(None)
def relation_controls():
    checks = {}
    cases = 0
    for nt, nh in ((2, 3), (3, 2), (1, 4)):
        b = generic(nh, nt)
        mu_t, mu_h = -b.H*b, b*b.H
        for kt in range(nt+1):
            for kh in range(nh+1):
                pt = s.diag(*([1]*kt+[0]*(nt-kt)))
                ph = s.diag(*([1]*kh+[0]*(nh-kh)))
                projection = s.trace(pt*mu_t)+s.trace(ph*mu_h)
                rhs = norm(ph*b*(s.eye(nt)-pt))-norm((s.eye(nh)-ph)*b*pt)
                checks[f'edge_{nt}_{nh}_{kt}_{kh}'] = clean(projection-rhs) == 0
                cases += 1
        checks[f'total_current_{nt}_{nh}'] = clean(s.trace(mu_t)+s.trace(mu_h)) == 0
        checks[f'deleting_partner_detected_{nt}_{nh}'] = clean(s.trace(mu_t)) != 0
    return {'checks': checks, 'rectangular_projector_cases': cases}


def run():
    groups = []
    for name, fn in [('blocks', block_controls), ('periphery', peripheral_controls),
                     ('boundary', boundary_controls), ('relations', relation_controls)]:
        out = fn(); groups.append(out)
        print(json.dumps({'group': name, **out}, sort_keys=True), flush=True)
    flags = [v for a in groups for v in a['checks'].values()]
    if not all(type(v) is bool for v in flags):
        raise TypeError('Every verdict must be a ground Python boolean')
    result = {'passed': sum(flags), 'total': len(flags), 'all_checks_pass': all(flags),
              'scope': 'conditional local identities; no physical source selection or complete spectrum'}
    print(json.dumps(result, sort_keys=True), flush=True)
    return result


if __name__ == '__main__':
    raise SystemExit(0 if run()['all_checks_pass'] else 1)
