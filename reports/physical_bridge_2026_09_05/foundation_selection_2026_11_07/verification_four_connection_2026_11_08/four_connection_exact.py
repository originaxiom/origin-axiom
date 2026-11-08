"""Unrun algebraic candidates; design sealed at e38c42a60 before source.

These finite exact routines do not establish global nonlinear existence,
the actual core spectrum, physical chirality or a foundational selection.
"""
from fractions import Fraction as F


def powers(nu, ell2):
    nu, ell2 = F(nu), F(ell2)
    if nu < 1 or ell2 <= 0:
        raise ValueError('Admitted Euclidean branch and positive metric required')
    return (1 - nu) / 2, (1 + nu) / 2, (nu * nu - 1) / (4 * ell2)


def green_at_integer_powers(nu, ell2, cut, y, z):
    """Exact point values on odd-integer nu controls only, not all real nu."""
    nu, ell2, cut, y, z = map(F, (nu, ell2, cut, y, z))
    rm, rp, _ = powers(nu, ell2)
    if cut <= 0 or min(y, z) < cut or rm.denominator != 1 or rp.denominator != 1:
        raise ValueError('Positive cut, tail points and integer power chart required')
    lo, hi = min(y, z), max(y, z)
    return (lo ** int(rp) * hi ** int(rm)
            - cut ** int(nu) * (y * z) ** int(rm)) / nu


def green_overlap(nu, a, b, cut):
    nu, a, b, cut = map(F, (nu, a, b, cut))
    rm, _, _ = powers(nu, 1)
    if min(a, b) < 2 or cut <= 0:
        raise ValueError('Retained pair powers and positive cut required')
    return cut ** 3 / ((a + b - 3) * (a - rm - 1) * (b - rm - 1))


def four_nu_overlap(np, nq, nr, nt, nk, cut):
    np, nq, nr, nt, nk, cut = map(F, (np, nq, nr, nt, nk, cut))
    if min(np, nq, nr, nt, nk) < 1 or cut <= 0:
        raise ValueError('Euclidean Poisson labels and positive cut required')
    return 8 * cut ** 3 / ((np + nq + nr + nt - 2)
                            * (np + nq + nk - 1) * (nr + nt + nk - 1))


def pair_current_parameters(np, nq, ell2):
    """Current factor after ordered-pair antisymmetrization, with Lie/i retained.

    j_mu=(q-p)_mu [Bp,Bq] u^-A/2;
    j_y=i [Bp,Bq] Y radial_coefficient u^radial_power.
    """
    np, nq, ell2 = map(F, (np, nq, ell2))
    _, _, sp = powers(np, ell2)
    _, _, sq = powers(nq, ell2)
    a = 1 + (np + nq) / 2
    return {'a': a, 'mu_coefficient': F(1, 2),
            'radial_coefficient': -(np - nq) / (4 * ell2),
            'radial_power': 1 - a, 'p2': sp, 'q2': sq}


def gauss_response(s, radial_current):
    if F(s) <= 0:
        raise ValueError('Zero exchange is a separate constrained channel')
    return -F(radial_current) / F(s)


def gaussian_minimum2(k, j):
    """Exact two-variable Gaussian algebra, NOT a replacement core operator."""
    k = [[F(x) for x in row] for row in k]
    j = list(map(F, j))
    if len(k) != 2 or any(len(row) != 2 for row in k) or len(j) != 2:
        raise ValueError('Explicit two-variable control required')
    det = k[0][0] * k[1][1] - k[0][1] * k[1][0]
    if k[0][1] != k[1][0] or k[0][0] <= 0 or det <= 0:
        raise ValueError('Positive symmetric Gaussian control required')
    v = [-(k[1][1] * j[0] - k[0][1] * j[1]) / det,
         -(-k[1][0] * j[0] + k[0][0] * j[1]) / det]
    energy = F(1, 2) * sum((v[i] * k[i][h] * v[h]
                            for i in range(2) for h in range(2)), F(0))
    energy += sum((v[i] * j[i] for i in range(2)), F(0))
    return v, energy


def longitudinal_zero_overlap(a, b, cut):
    a, b, cut = map(F, (a, b, cut))
    if min(a, b) < 2 or cut <= 0:
        raise ValueError('Convergent retained pair currents required')
    return cut ** 3 / ((a - 1) * (b - 1) * (a + b - 3))


def left_quaternion(q):
    a, b, c, d = map(F, q)
    return [[a, -b, -c, -d], [b, a, -d, c],
            [c, d, a, -b], [d, -c, b, a]]
