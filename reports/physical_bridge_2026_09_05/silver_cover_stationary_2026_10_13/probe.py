"""Exact local transformation jets and graded comparators, not a global PDE."""
from functools import lru_cache
import json
import sympy as s

x, e, q = s.symbols('x epsilon q', real=True)
I = s.I
X = s.Matrix([[0, 1], [1, 0]])
Y = s.Matrix([[0, -I], [I, 0]])
Z = s.diag(1, -1)
O = s.zeros(2)


def trim(a):
    return a.applyfunc(lambda z: sum(s.expand(z).coeff(e, k)*e**k for k in range(3)))


def eq(a, b):
    return trim(a-b) == s.zeros(*a.shape)


def mm(a, b):
    return trim(a*b)


def comm(a, b):
    return mm(a, b)-mm(b, a)


def derivative(a, j):
    return a.diff(x) if j == 0 else s.zeros(*a.shape)


def da(a, j, A):
    return trim(derivative(a, j)+I*comm(A[j], a))


def parts(phi):
    return ([trim((p+p.H)/2) for p in phi], [trim((p-p.H)/(2*I)) for p in phi])


def moment(phi):
    A, B = parts(phi)
    return trim(sum((da(B[j], j, A) for j in range(3)), O))


def curvature(phi):
    return [trim(derivative(phi[k], j)-derivative(phi[j], k)+I*comm(phi[j], phi[k]))
            for j in range(3) for k in range(j+1, 3)]


def P(lam, A, B):
    return trim(-sum((da(da(lam, j, A), j, A) for j in range(3)), O)
                +sum((comm(B[j], comm(B[j], lam)) for j in range(3)), O))


def transform(phi, lam, wrong=False):
    g = s.eye(2)-e*lam+e**2*lam*lam/2
    gi = s.eye(2)+e*lam+e**2*lam*lam/2
    return [trim(mm(mm(gi, a), g)+(I if wrong else -I)*mm(gi, derivative(g, j)))
            for j, a in enumerate(phi)], g, gi


def encode(a):
    out = []
    for row in a.tolist():
        vals = []
        for z in row:
            p = s.Poly(s.expand(z), x)
            degree = max(0, int(p.degree())) if not p.is_zero else 0
            vals.append([[str(s.re(p.nth(k))), str(s.im(p.nth(k)))] for k in range(degree+1)])
        out.append(vals)
    return out


@lru_cache(None)
def run():
    checks = {}
    def ck(k, v):
        checks[k] = bool(v)
        assert checks[k], k

    A = [(1+x)*X+x*x*Z, 2*Y+x*Z, (1+x*x)*Z+X]
    B = [(2+x)*Y+x*Z, Z+x*X, 3*X+x*Y]
    phi = [a+I*b for a, b in zip(A, B)]
    lam = (1+x+x*x)*X+(2+x*x)*Y+x*Z
    new, g, gi = transform(phi, lam)
    ck('positive_Hermitian_not_unitary', eq(g, g.H) and not eq(g.H*g, s.eye(2)))
    ck('inverse_series_and_tracefree_determinant', eq(mm(gi, g), s.eye(2)) and s.trace(lam) == 0
       and s.expand(g.det()).coeff(e, 1) == s.expand(g.det()).coeff(e, 2) == 0)
    ck('actual_first_complex_transform_sign', all(eq(a.applyfunc(lambda z: s.expand(z).coeff(e, 1)),
       I*derivative(lam, j)+comm(lam, phi[j])) for j, a in enumerate(new)))
    ck('actual_second_complex_transform_coefficient', all(eq(a.applyfunc(lambda z: s.expand(z).coeff(e, 2)),
       (comm(lam, comm(lam, phi[j]))+I*comm(lam, derivative(lam, j)))/2) for j, a in enumerate(new)))
    hs = curvature(phi)
    ck('curvature_covariance_with_full_derivative_jets', all(eq(a, mm(mm(gi, b), g))
       for a, b in zip(curvature(new), hs)))
    wrong, _, _ = transform(phi, lam, True)
    ck('wrong_derivative_sign_rejected', any(not eq(a, mm(mm(gi, b), g))
       for a, b in zip(curvature(wrong), hs)))
    mu = moment(new)
    ck('full_real_moment_derivative_minus_P', eq(mu.applyfunc(lambda z: s.expand(z).coeff(e, 1)), -P(lam, A, B)))
    ck('generic_residual_not_assumed_harmonic', not eq(moment(phi), O) and any(not eq(h, O) for h in hs))
    ck('moment_jets_Hermitian_and_traceless', eq(mu, mu.H) and s.expand(s.trace(mu)) == 0)
    ck('second_moment_coefficient_retained', not eq(mu.applyfunc(lambda z: s.expand(z).coeff(e, 2)), O))
    frozen = -sum((comm(b, comm(b, lam)) for b in B), O)
    ck('frozen_connection_derivatives_rejected', not eq(P(lam, A, B), -frozen))

    Af = [Z, 2*Z, 3*Z]; Bf = [2*Z, 3*Z, 5*Z]
    flat = [a+I*b for a, b in zip(Af, Bf)]
    lf = x*(1-x)*X+x*x*(1-x)*Y
    tf, gf, _ = transform(flat, lf)
    ck('harmonic_flat_fixture_verified', eq(moment(flat), O) and all(eq(h, O) for h in curvature(flat)))
    ck('complex_transform_keeps_flat_not_moment', all(eq(h, O) for h in curvature(tf)) and not eq(moment(tf), O))
    ck('both_boundary_values_fixed', all(eq(a.subs(x, endpoint), b.subs(x, endpoint))
       for a, b in zip(tf[1:], flat[1:]) for endpoint in (0, 1)))
    ck('normal_derivatives_not_frozen', all(not eq((tf[0]-flat[0]).subs(x, endpoint), O) for endpoint in (0, 1)))
    ck('Dirichlet_positive_frame_identity', all(eq(gf.subs(x, endpoint), s.eye(2)) for endpoint in (0, 1)))
    energy = sum((s.trace(da(lf, j, Af).H*da(lf, j, Af)+comm(Bf[j], lf).H*comm(Bf[j], lf)) for j in range(3)), s.Integer(0))
    en = s.integrate(s.expand(energy), (x, 0, 1))
    pairing = s.integrate(s.expand(s.trace(lf*P(lf, Af, Bf))), (x, 0, 1))
    ck('actual_Dirichlet_form_positive_no_surface', en > 0 and en == pairing)
    ck('unrestricted_parallel_kernel_not_Dirichlet', eq(P(Z, Af, Bf), O) and not eq(Z.subs(x, 0), O))
    wp = -sum((da(da(lf, j, Af), j, Af) for j in range(3)), O)-sum((comm(b, comm(b, lf)) for b in Bf), O)
    ck('wrong_Higgs_sign_rejected', not eq(P(lf, Af, Bf), wp))

    N = s.zeros(5); N[3, 0] = 1; N[0, 4] = 1
    T = s.eye(5)+q*N+q*q*N*N/2; Ti = s.eye(5)-q*N+q*q*N*N/2
    d0 = T[:, 0]; d1 = s.eye(5)[1, :]*Ti
    deck = s.diag(1, 1, 1, -1, -1)
    zero = s.Matrix([-q, 0, 0, 1, 0])
    ck('whole_graded_complex_invertible_change', T*Ti == s.eye(5) and T.det() == 1 and d1*d0 == s.zeros(1, 1))
    ck('whole_three_kernel_not_sector_copy', d0.rank() == d1.rank() == 1 and d1*zero == s.zeros(1, 1) and d0.H*zero == s.zeros(1, 1))
    ck('deck_parity_fails_at_nonzero_parameter', d0.H*deck*zero != s.zeros(1, 1))
    ck('old_adjoint_cannot_be_frozen', s.eye(5)[:, 0].H*zero != s.zeros(1, 1))
    closed = (1-q)*s.eye(5)[:, 0]
    start = [1-d0.subs(q, 0).rank(), 5-d0.subs(q, 0).rank()-d1.subs(q, 0).rank(), 1-d1.subs(q, 0).rank()]
    mixed = [1-d0.subs(q, 1).rank(), 5-d0.subs(q, 1).rank()-d1.subs(q, 1).rank(), 1-d1.subs(q, 1).rank()]
    gap = [1-closed.subs(q, 1).rank(), 5-closed.subs(q, 1).rank()-1, 0]
    ck('index_alone_allows_extra_endpoint_pair', gap == [1, 4, 0] and gap[1]-gap[0]-gap[2] == 3 and start != gap)
    records = {'moment_jets': [encode(mu.applyfunc(lambda z: s.expand(z).coeff(e, k))) for k in range(3)],
               'dirichlet_energy': str(en), 'toy_start': list(map(int, start)), 'toy_mixed': list(map(int, mixed)), 'toy_gap_closed': list(map(int, gap))}
    return {'checks': checks, 'exact_predicates': len(checks), 'records': records,
            'local_jets_epsilon_order': 2, 'global_silver_PDE_computed': False,
            'new_geometric_census': False, 'all_neutrals_integrated': False,
            'authored_analytic_continuation': True, 'outside_acceptance': False,
            'generated_selection': False, 'full_goal_achieved': False}


if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True, indent=2))
