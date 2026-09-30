"""R62 actual cone residual controls; no global or universal chirality verdict."""
import json
import sympy as s


def clean(x):
    if isinstance(x, s.MatrixBase):
        return x.applyfunc(lambda y: s.simplify(s.expand_complex(y)))
    return s.simplify(s.expand_complex(x))


def zero(x):
    return clean(x) == (s.zeros(*x.shape) if isinstance(x, s.MatrixBase) else 0)


def comm(a, b):
    return a*b-b*a


def norm(a):
    return clean(s.trace(a.H*a))


def residuals(B, X, c):
    if B.shape != X.shape or B.rows != B.cols:
        raise ValueError('equal square coefficient matrices required')
    M = clean(B+B.H+comm(B, B.H)+c*comm(X, X.H))
    F = clean(comm(B, X))
    K = clean(2*c*norm(F)+norm(M)/2)
    return F, M, K


def link(kind):
    if kind == 'square':
        return s.eye(2), s.Matrix([s.I, 1])
    if kind == 'hexagonal':
        return s.Matrix([[2, -1], [-1, 2]])/s.sqrt(3), s.Matrix([(1+s.sqrt(3)*s.I)/2, 1])
    raise ValueError('square or hexagonal link required')


def metric_residuals(B, X, kind):
    H, w = link(kind)
    r = s.Symbol('r', positive=True)
    x, y = s.symbols('x y', real=True)
    coords = (r, x, y)
    ginv = s.diag(1, 1/r**2, 1/r**2)
    ginv[1:3, 1:3] = H/r**2
    volume = r**2  # det(h)=1 and coordinate area=1 in these controls
    C = [B/r, w[0]*X, w[1]*X]
    n = B.rows
    F = {(i, j): clean(C[j].diff(coords[i])-C[i].diff(coords[j])+comm(C[i], C[j]))
         for i in range(3) for j in range(3)}
    divergence = sum((s.diff(volume*ginv[i, j]*(C[j]+C[j].H), coords[i])
                      for i in range(3) for j in range(3)), s.zeros(n))/volume
    interaction = sum((ginv[i, j]*comm(C[i], C[j].H)
                       for i in range(3) for j in range(3)), s.zeros(n))
    moment = clean(divergence+interaction)
    Fnorm = s.Integer(0)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for ell in range(3):
                    if ginv[i, k] != 0 and ginv[j, ell] != 0:
                        Fnorm += ginv[i, k]*ginv[j, ell]*s.trace(F[i, j].H*F[k, ell])/2
    density = clean(volume*(2*Fnorm+norm(moment)/2))
    pairing = clean(volume*sum((ginv[i, j]*s.trace(C[i].H*C[j])
                               for i in range(3) for j in range(3))))
    c = clean((w.H*H*w)[0])
    expected_F, expected_M, K = residuals(B, X, c)
    checks = dict(moment_from_metric=zero(moment-expected_M/r**2),
                  mixed_curvature_from_derivatives=all(zero(F[0, a+1]-w[a]*expected_F/r) for a in range(2)),
                  tangential_curvature_zero=zero(F[1, 2]),
                  full_density_from_metric=zero(density-K/r**2),
                  quadratic_pairing_finite_density=zero(pairing-(norm(B)+c*norm(X))))
    return dict(checks=checks, c=c, F=expected_F, M=expected_M, K=K,
                density=density, pairing=pairing)


def symbolic_trace():
    coeff = s.symbols('b0:8 x0:8', real=True)
    B = s.Matrix(2, 2, [coeff[j]+s.I*coeff[j+4] for j in range(4)])
    X = s.Matrix(2, 2, [coeff[j+8]+s.I*coeff[j+12] for j in range(4)])
    c = s.Symbol('c', positive=True)
    M = B+B.H+comm(B, B.H)+c*comm(X, X.H)
    herm = (B+B.H)/2
    identity = clean(s.re(s.trace(B*M))-2*norm(herm)-c*s.re(s.trace(comm(B, X)*X.H)))
    wrong = clean(s.re(s.trace(B*M))-norm(herm)-c*s.re(s.trace(comm(B, X)*X.H)))
    return dict(identity=identity, wrong_factor_nonzero=wrong != 0,
                radial_cyclic_trace=zero(s.trace(B*comm(B, B.H))))


def embedded(a):
    out = s.zeros(5)
    out[0:2, 0:2] = a
    return out


def fixtures(kind):
    H, w = link(kind)
    c = clean((w.H*H*w)[0])
    e = s.Matrix([[0, 1], [0, 0]])
    h = s.diag(1, -1)
    Xnormal = (1+s.I)*h
    pairs = dict(nilpotent_no_radial=(s.zeros(2), e),
                 moment_only_cancel=(-c*h/2, e),
                 nonnormal_radial=(e, e),
                 normal_positive=(s.I*h, Xnormal))
    rows = {name: metric_residuals(B, X, kind) for name, (B, X) in pairs.items()}
    checks = {}
    for name, data in rows.items():
        checks.update({name+'_'+key: value for key, value in data['checks'].items()})
    checks.update(
        nilpotent_flat_but_not_moment=zero(rows['nilpotent_no_radial']['F']) and not zero(rows['nilpotent_no_radial']['M']),
        radial_moment_cancel_keeps_curvature=zero(rows['moment_only_cancel']['M']) and not zero(rows['moment_only_cancel']['F']),
        both_partial_cancellations_cost=rows['nilpotent_no_radial']['K'] > 0 and rows['moment_only_cancel']['K'] > 0,
        nonnormal_radial_term_needed=not zero(comm(e, e.H)) and not zero(rows['nonnormal_radial']['M']-(e+e.H+c*comm(e, e.H))),
        nonzero_normal_pair_has_zero_action=zero(rows['normal_positive']['K']) and rows['normal_positive']['pairing'] > 0,
    )
    U = s.Matrix([[1, s.I], [s.I, 1]])/s.sqrt(2)
    checks['unitary_comparator'] = zero(U.H*U-s.eye(2))
    checks['unitary_residual_covariance'] = True
    checks['actual_su5_root_inclusion'] = True
    for name, (B, X) in pairs.items():
        F, M, K = residuals(B, X, c)
        Fu, Mu, Ku = residuals(U*B*U.H, U*X*U.H, c)
        checks['unitary_residual_covariance'] &= zero(Fu-U*F*U.H) and zero(Mu-U*M*U.H) and zero(Ku-K)
        F5, M5, K5 = residuals(embedded(B), embedded(X), c)
        checks['actual_su5_root_inclusion'] &= zero(F5-embedded(F)) and zero(M5-embedded(M)) and zero(K5-K)
    r = s.Symbol('r', positive=True)
    cone_div = s.diff(r**2*(h/r), r)/r**2
    flat_div = s.diff(h/r, r)
    checks['wrong_metric_sign_rejected'] = not zero(cone_div-flat_div)
    return dict(checks={k: bool(v) for k, v in checks.items()}, rows=rows)


def convergence():
    r, eps, R = s.symbols('r epsilon R', positive=True)
    pole = s.integrate(r**-2, (r, eps, R))
    tests = []
    for delta in (s.Rational(1, 4), s.Rational(1, 2), s.Rational(3, 4), s.Integer(1)):
        integral = s.integrate(delta**2*r**(2*delta-2), (r, eps, 1))
        limit = s.limit(integral, eps, 0, dir='+')
        tests.append(dict(delta=delta, integral=integral, limit=limit,
                          finite=bool(limit.is_finite)))
    return dict(checks=dict(pole_integral=zero(pole-(1/eps-1/R)),
                           norm_integral=zero(s.integrate(1, (r, eps, R))-(R-eps)),
                           threshold_controls=[x['finite'] for x in tests] == [False, False, True, True],
                           borderline_log=zero(tests[1]['integral']+s.log(eps)/4)),
                controls=tests)


def normality():
    h = s.diag(1, -1)
    t = s.Matrix([[0, 1], [1, 0]])
    z = s.Symbol('z', real=True)
    e = s.Matrix([[0, 1], [0, 0]])
    normal_ray = comm(z*e, (z*e).H)
    return dict(checks=dict(two_normal_controls=zero(comm(h, h.H)) and zero(comm(t, t.H)),
                           complex_sum_not_normal=not zero(comm(h+s.I*t, (h+s.I*t).H)),
                           origin_first_derivative_zero=zero(normal_ray.diff(z).subs(z, 0)),
                           nonnormal_ray_second_derivative_nonzero=not zero(normal_ray.diff(z, 2)),
                           cartan_complex_line_survives=zero(comm((1+s.I)*h, ((1+s.I)*h).H))),
                nonnormal_ray=normal_ray)


def serial(value):
    if isinstance(value, s.MatrixBase):
        return [[str(x) for x in row] for row in value.tolist()]
    if isinstance(value, s.Basic):
        return str(value)
    if isinstance(value, dict):
        return {k: serial(v) for k, v in value.items()}
    if isinstance(value, list):
        return [serial(v) for v in value]
    return value


def run():
    trace = symbolic_trace()
    checks = dict(trace_identity=zero(trace['identity']), trace_wrong_factor=trace['wrong_factor_nonzero'],
                  trace_radial_cyclicity=trace['radial_cyclic_trace'])
    links = {kind: fixtures(kind) for kind in ('square', 'hexagonal')}
    radial, normal = convergence(), normality()
    for name, data in dict(links, radial=radial, normal=normal).items():
        checks.update({name+'_'+k: bool(v) for k, v in data['checks'].items()})
    return serial(dict(scope='Fixed cone and constant helicity trace with radial simple pole; not all completions or chirality',
                       checks=checks, all_checks_pass=all(checks.values()), links=links,
                       trace=trace, convergence=radial, normality=normal))


if __name__ == '__main__':
    data = run()
    print(json.dumps(data, indent=2))
    raise SystemExit(0 if data['all_checks_pass'] else 1)
