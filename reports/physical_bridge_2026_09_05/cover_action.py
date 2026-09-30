"""R58 exact finite safeguards, not a manifold index or global PDE solver."""
import json
import sympy as s


def equal(a, b):
    d = a - b
    if isinstance(d, s.MatrixBase):
        return all(s.simplify(v) == 0 for v in d)
    return s.simplify(d) == 0


def bracket(a, b):
    return a * b - b * a


def adjoint(a, h):
    return h.inv() * a.conjugate().T * h


def diagonal_part(a, r=2):
    n = a.rows // r
    return s.diag(*(a[i*r:(i+1)*r, i*r:(i+1)*r] for i in range(n)))


def fixtures():
    x = s.Symbol('x', real=True)
    aa = [s.Matrix([[x+i, i+1], [1, -x-i]]) for i in range(3)]
    bb = [s.Matrix([[i+2, x], [x+1, -i-2]]) for i in range(3)]
    hh = [s.diag(i+1, i+2) for i in range(3)]
    return x, aa, bb, hh


def algebra_checks():
    _, aa, bb, _ = fixtures()
    a, b = s.diag(*aa), s.diag(*bb)
    basis = []
    for i in range(6):
        for j in range(6):
            if i // 2 == j // 2:
                e = s.zeros(6); e[i, j] = 1
                basis.append(e.reshape(36, 1))
    e02, e20 = s.zeros(6), s.zeros(6)
    e02[0, 2] = 1; e20[2, 0] = 1
    c = bracket(e02, e20)
    return {
        'product': equal(a*b, s.diag(*(u*v for u, v in zip(aa, bb)))),
        'bracket': equal(bracket(a,b), s.diag(*(bracket(u,v) for u,v in zip(aa,bb)))),
        'cubic_trace': equal(s.trace(a*b*a), sum(s.trace(u*v*u) for u,v in zip(aa,bb))),
        'proper_subalgebra_rank': s.Matrix.hstack(*basis).rank() == 12 < 36,
        'off_diagonal_directions': diagonal_part(e02) == diagonal_part(e20) == s.zeros(6),
        'projection_not_lie': diagonal_part(c) == c and c != s.zeros(6),
    }


def kinetic_checks():
    x, aa, bb, hh = fixtures()
    a, b, h = s.diag(*aa), s.diag(*bb), s.diag(*hh)
    norms = [s.trace(adjoint(u,g)*u) for u,g in zip(aa,hh)]
    total = s.trace(adjoint(a,h)*a)
    da = a.diff(x) + bracket(b,a)
    sheet_da = [u.diff(x)+bracket(v,u) for u,v in zip(aa,bb)]
    eps = s.Symbol('eps', real=True)
    variation = s.diff(s.trace(adjoint(a+eps*b,h)*(a+eps*b)),eps).subs(eps,0)
    parts = sum(s.diff(s.trace(adjoint(u+eps*v,g)*(u+eps*v)),eps).subs(eps,0)
                for u,v,g in zip(aa,bb,hh))
    return {
        'adjoint': equal(adjoint(a,h),s.diag(*(adjoint(u,g) for u,g in zip(aa,hh)))),
        'positive_gram': all(g.det()>0 and g[0,0]>0 for g in hh),
        'positive_nonzero_norm': total.subs(x,0)>0,
        'pointwise_quadratic': equal(total,sum(norms)),
        'integrated_quadratic': equal(s.integrate(total,(x,0,1)),sum(s.integrate(v,(x,0,1)) for v in norms)),
        'first_variation': equal(variation,parts),
        'covariant_derivative': equal(da,s.diag(*sheet_da)),
        'commutator_norm': equal(s.trace(adjoint(bracket(a,b),h)*bracket(a,b)),
            sum(s.trace(adjoint(bracket(u,v),g)*bracket(u,v)) for u,v,g in zip(aa,bb,hh))),
    }


def monodromy_checks():
    j = s.Matrix([[1,1],[0,1]])
    t = s.zeros(6)
    t[2:4,0:2] = s.eye(2); t[4:6,2:4] = s.eye(2); t[0:2,4:6] = j
    a = s.diag(1,2,3,4,5,6)
    h = s.diag(1,2,3,4,5,6)
    moved = t*a*t.inv()
    hnew = t.inv().T*h*t.inv()
    norm = lambda m,g: s.trace(adjoint(m,g)*m)
    nil = t**3 - s.eye(6)
    return {
        'nontrivial_cube': t**3 == s.diag(j,j,j) and nil != s.zeros(6),
        'unipotent_cube': nil**2 == s.zeros(6),
        'block_algebra_preserved': diagonal_part(moved) == moved,
        'transported_metric_norm': equal(norm(moved,hnew), norm(a,h)),
        'fixed_metric_opposite': not equal(norm(moved,h),norm(a,h)),
    }


def quartic_checks():
    _, aa, _, hh = fixtures()
    a, h = s.diag(*aa), s.diag(*hh)
    single = s.trace((adjoint(a,h)*a)**2)
    sheet = sum(s.trace((adjoint(u,g)*u)**2) for u,g in zip(aa,hh))
    x0,x1,x2 = s.symbols('x0 x1 x2', nonnegative=True)
    sqsum = x0*x0+x1*x1+x2*x2
    naive = (x0+x1+x2)**2
    gap = naive-sqsum
    # Exact symbolic certificates for both inequalities, not a random grid.
    upper = 3*sqsum-naive
    return {
        'single_trace_quartic': equal(single,sheet),
        'extra_cross_terms': equal(gap,2*(x0*x1+x0*x2+x1*x2)),
        'nonzero_quartic_opposite': gap.subs({x0:1,x1:4,x2:9}) == 98,
        'upper_bound_certificate': equal(upper,(x0-x1)**2+(x0-x2)**2+(x1-x2)**2),
        'both_bounds_sharp': gap.subs({x0:1,x1:0,x2:0}) == 0 and upper.subs({x0:1,x1:1,x2:1}) == 0,
    }


def boundary_checks():
    z, i = s.zeros(3), s.eye(3)
    green = z.row_join(i).col_join((-i).row_join(z))
    dd = z.col_join(i); nn = i.col_join(z)
    p = s.Matrix([[0,0,1],[1,0,0],[0,1,0]])
    deck = s.diag(p,p)
    return {
        'nondegenerate_green': green.rank() == 6,
        'maximal_isotropic_both': dd.rank() == nn.rank() == 3 and dd.T*green*dd == nn.T*green*nn == z,
        'distinct_domains': dd.row_join(nn).rank() == 6,
        'both_deck_stable': deck*dd == dd*p and deck*nn == nn*p,
    }


def run():
    groups = {f.__name__: f() for f in (algebra_checks, kinetic_checks,
              monodromy_checks, quartic_checks, boundary_checks)}
    groups = {k:{n:bool(v) for n,v in rows.items()} for k,rows in groups.items()}
    values = [v for rows in groups.values() for v in rows.values()]
    return dict(checks=groups,passed=sum(values),total=len(values),
        all_checks_pass=all(values),actual_m6_index_recomputed=False,
        physical_action_selected=False,physical_end_law_derived=False,
        physical_chirality_derived=False,global_analysis_independently_reviewed=False)


if __name__ == '__main__':
    result = run()
    print(json.dumps(result,sort_keys=True))
    raise SystemExit(0 if result['all_checks_pass'] else 1)
