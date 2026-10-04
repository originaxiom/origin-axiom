#!/usr/bin/env python3
"""B1538 route W -- the line's supply through the fibration (Wang), exactly.  Library; nothing sealed is computed on import.

For a cover N = M_(D,w) (punct_covers.Cover) and a character chi = (zeta, s) of H = pi_1 N with zeta != 1 on K:
  - H^0(K; zeta) = 0, so the Lyndon-Hochschild-Serre sequence of 1 -> K -> H -> <tau> -> 1 gives
        H^1(H; chi) = ker(Jbar - s) on H^1(K; zeta) = Z^1 / B^1,
    where J is the Fox Jacobian of the monodromy at zeta (J_ij = (d f(y_i) / d y_j)(zeta), left cocycles
    z(gh) = z(g) + zeta(g) z(h)), B^1 = C beta with beta_i = zeta(y_i) - 1, and Jbar is J on the quotient.
    For a cocycle z of H, z(f(k)) = s z(k) + (1 - zeta(k)) z(tau), so [z o f] = s [z]: the eigenvalue is s = chi(tau).
  - dim H^1(K; zeta) = |D|.  Jbar is read on the complement {v_i0 = 0} of B^1: Jbar_ij = J_ij - J_i0j beta_i / beta_i0.
  - The roots of unity s with h^1 >= 1 are found completely.  P(x) = charpoly(Jbar) over Q(zeta_m); its norm
    N(x) = Res_y(P(x, y), Phi_m(y)) lies in Z[x]; PARI's polcyclofactors lists N's cyclotomic factors Phi_k; every primitive
    k-th root s is then tested by the exact rank of Jbar - s over Q(zeta_lcm(m, k)).
  - n(chi) = h^1 - #{cusps where chi is trivial}, by half lives, half dies: for unitary chi the image of H^1(N) in H^1(dN)
    is half of it, and h^1(cusp torus) = 2 exactly where chi is trivial on it.  Route P reads n directly from the
    restrictions; the two must agree.

Exact arithmetic throughout (PARI over cyclotomic fields).  New code for B1538."""
from math import gcd

import punct_covers as F


def lcm(a, b):
    return a * b // gcd(a, b)


# ============================================================================================ the Fox Jacobian
def fox_jacobian(images, ez, m):
    """J[i][j] as {exponent: coefficient}, for the endomorphism y_i -> images[i] (a list of (j, +-1)) of a free group, at the
    character y_j -> z_m^ez[j] (exponents mod m), or with m = None at y_j -> t^ez[j] for a formal t (exponents in Z)"""
    n = len(images)
    J = [[{} for _ in range(n)] for _ in range(n)]
    for i, img in enumerate(images):
        pre = 0
        for j, e in img:
            if e == 1:
                k = pre % m if m else pre
                J[i][j][k] = J[i][j].get(k, 0) + 1
                pre += ez[j]
            else:
                pre -= ez[j]
                k = pre % m if m else pre
                J[i][j][k] = J[i][j].get(k, 0) - 1
    return J


def _poly(P, terms):
    """sum c y^k as a PARI polynomial in y"""
    y = P("y")
    out = P(0)
    for k, c in terms.items():
        if c:
            out += c * y ** k
    return out


def jbar(J, ez, m):
    """Jbar over Q(zeta_m) (PARI matrix of polmods), and i0"""
    P = F.pari()
    n = len(J)
    phi = P.polcyclo(m, "y")
    i0 = next(i for i in range(n) if ez[i] % m)
    beta = [P.Mod(_poly(P, {ez[i] % m: 1}) - 1, phi) for i in range(n)]
    Jm = [[P.Mod(_poly(P, J[i][j]), phi) for j in range(n)] for i in range(n)]
    idx = [i for i in range(n) if i != i0]
    rows = []
    for i in idx:
        for j in idx:
            rows.append(Jm[i][j] - Jm[i0][j] * beta[i] / beta[i0])
    return P.matrix(n - 1, n - 1, rows), i0


def lift_to(P, Mat, m, L):
    """the matrix over Q(zeta_m) read over Q(zeta_L), m | L (zeta_m = zeta_L^(L/m))"""
    phiL = P.polcyclo(L, "y")
    k = L // m
    n = len(Mat)
    out = []
    for i in range(n):
        for j in range(n):
            pol = P.lift(Mat[i, j])
            out.append(P.Mod(P.subst(pol, "y", P("y") ** k), phiL))
    return P.matrix(n, n, out)


def root_of_unity_eigenvalues(Jb, m):
    """([(j, k, h1)], charpoly, norm): every root of unity s = z_k^j (gcd(j, k) = 1) with h1 = dim ker(Jbar - s) >= 1,
    exactly"""
    P = F.pari()
    n = len(Jb)
    if n == 0:
        return [], None, None
    cp = P.charpoly(Jb, "x")
    norm = P.polresultant(P.lift(cp), P.polcyclo(m, "y"), "y")
    # polcyclofactors may return a product of distinct cyclotomic polynomials as one factor (Phi_5 Phi_15 = Phi_5(x^3) on
    # m003's (2,0,2) cover): the Phi_k are the irreducible factors of its entries
    ks = set()
    for fac in P.polcyclofactors(norm):
        fa = P.factor(fac)
        for r in range(int(P.matsize(fa)[0])):
            k = int(P.poliscyclo(fa[r, 0]))
            assert k > 0, ("a factor of the cyclotomic part is not cyclotomic", str(fa[r, 0]))
            ks.add(k)
    out = []
    for k in sorted(ks):
        L = lcm(m, k)
        JL = lift_to(P, Jb, m, L)
        phiL = P.polcyclo(L, "y")
        for j in range(k):
            if gcd(j, k) != 1:
                continue
            s = P.Mod(P("y") ** (j * (L // k)), phiL)
            r = int(P.matrank(JL - s * P.matid(n)))
            if r < n:
                out.append((j, k, n - r))
    return out, cp, norm


# ============================================================================================ the reading
def read(C, ez, m):
    """route W at the fibre character zeta = ez (mod m, zeta != 1 on K): every root of unity s with h^1(N; (zeta, s)) >= 1,
    with h^1, the trivial cusps and n"""
    assert any(e % m for e in ez), "zeta is trivial on K"
    J = fox_jacobian(C.fimg, ez, m)
    Jb, i0 = jbar(J, ez, m)
    eig, cp, norm = root_of_unity_eigenvalues(Jb, m)
    rows = []
    for j, k, h1 in eig:
        L = lcm(m, k)
        ezL = [e * (L // m) % L for e in ez]
        es = j * (L // k) % L
        triv = C.trivial_cusps(ezL, es, L)
        rows.append({"s": [j, k], "L": L, "h1": h1, "trivial cusps": len(triv), "n": h1 - len(triv)})
    return {"rows": rows, "charpoly degree": int(F.pari().poldegree(cp, "x")), "i0": i0}
