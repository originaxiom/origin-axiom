"""Separate exact Gaussian-Fraction polynomial convolution; no symbolic engine."""
from fractions import Fraction as F
from functools import lru_cache
import json


def c(z):
    return z if isinstance(z, tuple) else (F(z), F(0))


def ca(a, b):
    a, b = c(a), c(b)
    return (a[0]+b[0], a[1]+b[1])


def cm(a, b):
    a, b = c(a), c(b)
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def clean(p):
    return {k: v for k, v in p.items() if v != (0, 0)}


def const(z):
    return clean({(0, 0): c(z)})


def pa(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = ca(out.get(k, c(0)), v)
    return clean(out)


def pm(a, b):
    out = {}
    for (j, k), v in a.items():
        for (l, m), w in b.items():
            if k+m <= 2:
                key = (j+l, k+m)
                out[key] = ca(out.get(key, c(0)), cm(v, w))
    return clean(out)


def ps(a, z):
    return clean({k: cm(v, z) for k, v in a.items()})


def pd(a):
    return clean({(j-1, k): cm(v, j) for (j, k), v in a.items() if j})


def pc(a):
    return {k: (v[0], -v[1]) for k, v in a.items()}


def pe(a, endpoint):
    out = {}
    for (j, k), v in a.items():
        key = (0, k)
        out[key] = ca(out.get(key, c(0)), cm(v, F(endpoint)**j))
    return clean(out)


def mat(a):
    return [[const(z) for z in row] for row in a]


def ident(n):
    return mat([[int(i == j) for j in range(n)] for i in range(n)])


def ma(*arrays):
    return [[pa(*(a[i][j] for a in arrays)) for j in range(len(arrays[0][0]))] for i in range(len(arrays[0]))]


def ms(a, z):
    return [[ps(v, z) for v in row] for row in a]


def mp(a, p):
    return [[pm(v, p) for v in row] for row in a]


def mm(a, b):
    return [[pa(*(pm(a[i][k], b[k][j]) for k in range(len(b)))) for j in range(len(b[0]))] for i in range(len(a))]


def mh(a):
    return [[pc(a[j][i]) for j in range(len(a))] for i in range(len(a[0]))]


def md(a, j):
    return [[pd(v) if j == 0 else {} for v in row] for row in a]


def me(a, endpoint):
    return [[pe(v, endpoint) for v in row] for row in a]


def zero(a):
    return all(not v for row in a for v in row)


def equal(a, b):
    return zero(ma(a, ms(b, -1)))


def comm(a, b):
    return ma(mm(a, b), ms(mm(b, a), -1))


def trace(a):
    return pa(*(a[j][j] for j in range(len(a))))


def coeff(a, epsilon_degree):
    return [[clean({(j, 0): v for (j, k), v in p.items() if k == epsilon_degree}) for p in row] for row in a]


def encode(a):
    return [[[[str(p.get((j, 0), c(0))[0]), str(p.get((j, 0), c(0))[1])]
              for j in range(max((k[0] for k in p), default=0)+1)] for p in row] for row in a]


II = (F(0), F(1))
px = {(1, 0): c(1)}
epsilon = {(0, 1): c(1)}
one = const(1)
X = mat([[0, 1], [1, 0]])
Y = mat([[0, (F(0), F(-1))], [II, 0]])
Z = mat([[1, 0], [0, -1]])


def da(z, j, A):
    return ma(md(z, j), ms(comm(A[j], z), II))


def parts(phi):
    return ([ms(ma(a, mh(a)), F(1, 2)) for a in phi],
            [ms(ma(a, ms(mh(a), -1)), (F(0), F(-1, 2))) for a in phi])


def moment(phi):
    A, B = parts(phi)
    return ma(*(da(B[j], j, A) for j in range(3)))


def curvature(phi):
    return [ma(md(phi[k], j), ms(md(phi[j], k), -1), ms(comm(phi[j], phi[k]), II))
            for j in range(3) for k in range(j+1, 3)]


def P(lam, A, B):
    return ma(ms(ma(*(da(da(lam, j, A), j, A) for j in range(3))), -1),
              ma(*(comm(b, comm(b, lam)) for b in B)))


def transform(phi, lam, wrong=False):
    second = mp(ms(mm(lam, lam), F(1, 2)), pm(epsilon, epsilon))
    g = ma(ident(2), ms(mp(lam, epsilon), -1), second)
    gi = ma(ident(2), mp(lam, epsilon), second)
    return [ma(mm(mm(gi, a), g), ms(mm(gi, md(g, j)), II if wrong else (F(0), F(-1))))
            for j, a in enumerate(phi)], g, gi


def rank(a):
    a = [[F(v) for v in row] for row in a]; rr = 0
    for j in range(len(a[0])):
        piv = next((i for i in range(rr, len(a)) if a[i][j]), None)
        if piv is None:
            continue
        a[rr], a[piv] = a[piv], a[rr]
        v = a[rr][j]; a[rr] = [x/v for x in a[rr]]
        for i in range(len(a)):
            if i != rr:
                v = a[i][j]; a[i] = [x-v*y for x, y in zip(a[i], a[rr])]
        rr += 1
        if rr == len(a):
            break
    return rr


@lru_cache(None)
def run():
    checks = {}
    def ck(k, value):
        checks[k] = bool(value)
        assert checks[k], k
    x2 = pm(px, px)
    A = [ma(mp(X, pa(one, px)), mp(Z, x2)), ma(ms(Y, 2), mp(Z, px)), ma(mp(Z, pa(one, x2)), X)]
    B = [ma(mp(Y, pa(const(2), px)), mp(Z, px)), ma(Z, mp(X, px)), ma(ms(X, 3), mp(Y, px))]
    phi = [ma(a, ms(b, II)) for a, b in zip(A, B)]
    lam = ma(mp(X, pa(one, px, x2)), mp(Y, pa(const(2), x2)), mp(Z, px))
    new, g, gi = transform(phi, lam); mu = moment(new)
    ck('separate_positive_not_unitary', equal(g, mh(g)) and not equal(mm(mh(g), g), ident(2)))
    ck('separate_inverse_and_determinant', equal(mm(gi, g), ident(2)) and not trace(lam)
       and pa(pm(g[0][0], g[1][1]), ps(pm(g[0][1], g[1][0]), -1)) == one)
    ck('separate_first_transform_sign', all(equal(coeff(a, 1), ma(ms(md(lam, j), II), comm(lam, phi[j]))) for j, a in enumerate(new)))
    ck('separate_second_transform', all(equal(coeff(a, 2), ms(ma(comm(lam, comm(lam, phi[j])), ms(comm(lam, md(lam, j)), II)), F(1, 2))) for j, a in enumerate(new)))
    hs = curvature(phi)
    ck('separate_covariance_full_jets', all(equal(a, mm(mm(gi, b), g)) for a, b in zip(curvature(new), hs)))
    wrong, _, _ = transform(phi, lam, True)
    ck('separate_wrong_sign_fails', any(not equal(a, mm(mm(gi, b), g)) for a, b in zip(curvature(wrong), hs)))
    ck('separate_real_moment_derivative', equal(coeff(mu, 1), ms(P(lam, A, B), -1)))
    ck('separate_generic_residuals_live', not zero(moment(phi)) and any(not zero(h) for h in hs))
    ck('separate_real_tracefree_moment', equal(mu, mh(mu)) and not trace(mu))
    ck('separate_second_moment_not_deleted', not zero(coeff(mu, 2)))
    ck('separate_frozen_jets_fail', not equal(P(lam, A, B), ma(*(comm(b, comm(b, lam)) for b in B))))
    Af = [Z, ms(Z, 2), ms(Z, 3)]; Bf = [ms(Z, 2), ms(Z, 3), ms(Z, 5)]
    flat = [ma(a, ms(b, II)) for a, b in zip(Af, Bf)]
    lf = ma(mp(X, pm(px, pa(one, ps(px, -1)))), mp(Y, pm(x2, pa(one, ps(px, -1)))))
    tf, gf, _ = transform(flat, lf)
    ck('separate_flat_harmonic_control', zero(moment(flat)) and all(zero(h) for h in curvature(flat)))
    ck('separate_complex_is_not_real_gauge', all(zero(h) for h in curvature(tf)) and not zero(moment(tf)))
    ck('separate_tangential_boundary_fixed', all(equal(me(a, k), me(b, k)) for a, b in zip(tf[1:], flat[1:]) for k in (0, 1)))
    ck('separate_normal_jets_free', all(not zero(me(ma(tf[0], ms(flat[0], -1)), k)) for k in (0, 1)))
    ck('separate_identity_frame_at_two_ends', all(equal(me(gf, k), ident(2)) for k in (0, 1)))
    energy = pa(*(trace(ma(mm(mh(da(lf, j, Af)), da(lf, j, Af)), mm(mh(comm(Bf[j], lf)), comm(Bf[j], lf)))) for j in range(3)))
    bulk = trace(mm(lf, P(lf, Af, Bf)))
    def integral(p):
        assert all(k == 0 and v[1] == 0 for (j, k), v in p.items())
        return sum((v[0]/(j+1) for (j, k), v in p.items()), F(0))
    en = integral(energy)
    ck('separate_Dirichlet_energy_positive_exact', en > 0 and en == integral(bulk))
    ck('separate_parallel_zero_fails_Dirichlet', zero(P(Z, Af, Bf)) and not zero(me(Z, 0)))
    wp = ms(ma(*(da(da(lf, j, Af), j, Af) for j in range(3)), *(comm(b, comm(b, lf)) for b in Bf)), -1)
    ck('separate_wrong_Higgs_sign_fails', not equal(P(lf, Af, Bf), wp))
    toy = []
    for t in (0, 1, 2):
        d0 = [[1], [0], [0], [t], [0]]; d1 = [[0, 1, 0, 0, 0]]
        r0, r1 = rank(d0), rank(d1)
        toy.append([1-r0, 5-r0-r1, 1-r1])
        ck('fraction_whole_counts_'+str(t), toy[-1] == [0, 3, 0])
    ck('fraction_mixed_zero_not_deck_invariant', sum(a*b for a, b in zip([1, 0, 0, 1, 0], [-1, 0, 0, 1, 0])) == 0
       and sum(a*b for a, b in zip([1, 0, 0, 1, 0], [-1, 0, 0, -1, 0])) != 0)
    closed_rank = rank([[0], [0], [0], [0], [0]])
    gap = [1-closed_rank, 5-closed_rank-1, 0]
    ck('fraction_index_not_endpoint_gap', gap == [1, 4, 0] and gap[1]-gap[0]-gap[2] == toy[0][1])
    records = {'moment_jets': [encode(coeff(mu, k)) for k in range(3)], 'dirichlet_energy': str(en),
               'toy_start': toy[0], 'toy_mixed': toy[1], 'toy_gap_closed': gap}
    return {'checks': checks, 'exact_predicates': len(checks), 'records': records,
            'symbolic_engine_imported': False, 'new_native_imported': False,
            'local_jets_epsilon_order': 2, 'global_silver_PDE_computed': False,
            'outside_acceptance': False, 'generated_selection': False, 'full_goal_achieved': False}


if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True, indent=2))
