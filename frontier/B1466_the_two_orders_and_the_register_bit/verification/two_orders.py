#!/usr/bin/env python3
"""B1466 -- the two stacking orders at the counted point, their counts, their duality, the cup product that decides whether
both can be carried at once, and the sourced potential.  Main's instruments only: B1453's join_own helpers (Ballas' matrices,
the relator, the fibred presentation), B1446's index_num.  Written before the seal; run after it."""
import sys, json, pathlib, itertools
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
import glob
for d in ("B1453_*", "B1444_*", "B1445_*", "B1446_*"):
    sys.path.insert(0, glob.glob(str(ROOT / "frontier" / d / "verification"))[0])
import join_own as jo, index_num as ix
from mpmath import mp, mpf, mpc, matrix, eye, zeros, inverse, sqrt, svd_c, nstr, norm
mp.dps = 60
REL = jo.REL; PHI = jo.PHI
TOL = mpf(10) ** (-30)


def blockS(g):
    """S = A (+) 1 as 5 x 5, A in the top-left block"""
    out = {}
    for k in "mn":
        W = zeros(5, 5)
        for i in range(4):
            for j in range(4): W[i, j] = g[k][i, j]
        W[4, 4] = 1; out[k] = W
    return out


def ext_down(g, c):
    """[[A, 0], [c, 1]] on the generators: 1 the submodule, A the quotient (A on top of 1); c a row (1 x 4) per generator"""
    out = {}
    for k in "mn":
        W = zeros(5, 5)
        for i in range(4):
            for j in range(4): W[i, j] = g[k][i, j]
            W[4, i] = c[k][i]
        W[4, 4] = 1; out[k] = W
    return out


def cocycles_down(g):
    """a basis of Z^1 modulo B^1 for the extensions [[A, 0], [c, 1]]: unknowns the rows c_m, c_n (8); coboundaries c_g = v (A_g - 1)"""
    cols = []
    for j in range(8):
        c = {"m": zeros(1, 4), "n": zeros(1, 4)}; c["mn"[j // 4]][0, j % 4] = 1
        R = jo.word(REL, ext_down(g, c)); cols.append([R[4, i] for i in range(4)])
    M = matrix(4, 8)
    for j in range(8):
        for i in range(4): M[i, j] = cols[j][i]
    Z, rk, S = jo.null(M)
    Bm = matrix(8, 4)
    for j in range(4):
        v = zeros(1, 4); v[0, j] = 1; bm = v * (g["m"] - eye(4)); bn = v * (g["n"] - eye(4))
        for i in range(4): Bm[i, j] = bm[0, i]; Bm[4 + i, j] = bn[0, i]
    Ub, Sb, Vb = svd_c(Bm); rb = sum(1 for i in range(len(Sb)) if abs(Sb[i]) > TOL)
    reps = []
    for zv in Z:
        T = matrix(8, 4 + len(reps) + 1)
        for i in range(8):
            for j in range(4): T[i, j] = Bm[i, j]
            for j, r in enumerate(reps): T[i, 4 + j] = r[i]
            T[i, 4 + len(reps)] = zv[i]
        U2, S2, V2 = svd_c(T)
        if sum(1 for i in range(len(S2)) if abs(S2[i]) > TOL) > rb + len(reps): reps.append(zv)
    return reps, len(Z), rb


def intertwiner(X, Y):
    """Q with Q X_g = Y_g Q for g = m, n (5 x 5); returns (Q, kept, dropped) from the null space; None if no one-dimensional solution"""
    n = X["m"].rows; rows = []
    for k in "mn":
        for i in range(n):
            for j in range(n):
                row = [mpc(0)] * (n * n)
                for a in range(n):
                    row[i * n + a] += X[k][a, j]           # (Q X)_{ij} = sum_a Q_{ia} X_{aj}
                    row[a * n + j] -= Y[k][i, a]           # (Y Q)_{ij} = sum_a Y_{ia} Q_{aj}
                rows.append(row)
    U, S, Vh = svd_c(matrix(rows), full_matrices=True)
    kept = abs(S[n * n - 2]); dropped = abs(S[n * n - 1])
    if not (dropped < TOL and kept > TOL): return None, kept, dropped
    v = [Vh[n * n - 1, i].conjugate() for i in range(n * n)]
    Q = matrix([[v[i * n + j] for j in range(n)] for i in range(n)])
    U2, S2, V2 = svd_c(Q); return Q, kept, dropped, abs(S2[n - 1])          # the last: Q's smallest singular value (invertibility)


# ---------------------------------------------------------------- the presentation complex and the obstruction
def series_word(word, g, phi, psi=None):
    """rho_eps(w) to order eps^2 with rho_eps(g) = rho(g)(1 + eps phi_g + eps^2 psi_g); returns (M0, M1, M2)"""
    n = g["m"].rows; I = eye(n)
    def gen(ch):
        k = ch.lower(); A = g[k]; P = phi[k]; Q = psi[k] if psi else zeros(n, n)
        if ch.islower(): return (A, A * P, A * Q)
        Ai = inverse(A)                                            # (A(1 + e P + e^2 Q))^-1 = (1 - e P + e^2 (P^2 - Q)) A^-1
        return (Ai, -P * Ai, (P * P - Q) * Ai)
    M0, M1, M2 = I, zeros(n, n), zeros(n, n)
    for ch in word:
        a0, a1, a2 = gen(ch)
        M0, M1, M2 = M0 * a0, M0 * a1 + M1 * a0, M0 * a2 + M1 * a1 + M2 * a0
    return M0, M1, M2


def d1_matrix(g):
    """the Fox map C^1 = End(S)^2 -> C^2 = End(S) as a 25 x 50 matrix: phi -> eps^1 coefficient of rho_eps(R)"""
    n = g["m"].rows; cols = []
    for k in "mn":
        for i in range(n):
            for j in range(n):
                phi = {"m": zeros(n, n), "n": zeros(n, n)}; phi[k][i, j] = 1
                M0, M1, M2 = series_word(REL, g, phi); cols.append([M1[a, b] for a in range(n) for b in range(n)])
    D = matrix(n * n, 2 * n * n)
    for j, c in enumerate(cols):
        for i in range(n * n): D[i, j] = c[i]
    return D


def obstruction_class(g, phi, D):
    """the eps^2 coefficient of rho_eps(R) (psi = 0) as a vector, and its residual modulo im(d1) with the projection's gap"""
    n = g["m"].rows
    M0, M1, M2 = series_word(REL, g, phi)
    o1 = norm(matrix([M1[a, b] for a in range(n) for b in range(n)]))           # must vanish: phi is a cocycle
    ob = matrix([M2[a, b] for a in range(n) for b in range(n)])
    U, S, Vh = svd_c(D, full_matrices=True)
    r = sum(1 for i in range(len(S)) if abs(S[i]) > TOL * max(1, abs(S[0])))
    # residual of ob orthogonal to the column space of D (spanned by the first r columns of U)
    proj = zeros(n * n, 1)
    for i in range(r):
        u = U[:, i]; coef = (u.H * ob)[0]; proj += coef * u
    res = ob - proj
    return dict(cocycle_residual=nstr(o1, 4), ob_norm=nstr(norm(ob), 8), residual_mod_im_d1=nstr(norm(res), 8), rank_d1=r, dim_H2=n * n - r,
                kept=nstr(abs(S[r - 1]), 4), dropped=nstr(abs(S[r]), 4) if r < len(S) else "none")


def run_point(q, mu, label, controls_only=False):
    g = jo.ballas(q, mu); R = jo.word(REL, g); assert max(abs(R[i, j] - (1 if i == j else 0)) for i in range(4) for j in range(4)) < mpf(10) ** (-45), "relator"
    out = dict(label=label, q=nstr(q, 20), mu=str(mu))
    reps_up, z_up, b_up = jo.cocycles(g); reps_dn, z_dn, b_dn = cocycles_down(g)
    out["h1_up(Ext(1,A))"] = len(reps_up); out["h1_down(Ext(A,1))"] = len(reps_dn)
    S = blockS(g); hS, TS = jo.fibred(S); I_S, aS, bS = ix.index(PHI, hS, TS); out["I_split"] = int(I_S)
    if not reps_up or not reps_dn: return out
    c1 = {"m": matrix([reps_up[0][i] for i in range(4)]), "n": matrix([reps_up[0][4 + i] for i in range(4)])}
    c2 = {"m": matrix([[reps_dn[0][i] for i in range(4)]]), "n": matrix([[reps_dn[0][4 + i] for i in range(4)]])}
    W = jo.ext(g, c1); Wd = ext_down(g, c2)
    for name, M in (("W (1 on top of A)", W), ("W' (A on top of 1)", Wd)):
        h, T = jo.fibred(M); I, a, b = ix.index(PHI, h, T)
        out["I " + name] = dict(I=int(I), h1=a["h1"], h1_dual=b["h1"], interior=a["interior"], interior_dual=b["interior"], gap=(nstr(a["gaps"][1][0], 4), nstr(a["gaps"][1][1], 4)))
    # C2: W* against iota^* W'
    Wstar = jo.dualrep(W); iotaWd = {"m": inverse(Wd["m"]), "n": inverse(Wd["n"])}
    Q = intertwiner(Wstar, iotaWd); out["C2 W* ~ iota*W'"] = dict(found=Q[0] is not None, kept=nstr(Q[1], 4), dropped=nstr(Q[2], 4), Q_min_sv=nstr(Q[3], 4) if Q[0] is not None else None)
    Q2 = intertwiner(Wstar, Wd); out["C2 control W* ~ W' (no iota)"] = dict(found=Q2[0] is not None, kept=nstr(Q2[1], 4), dropped=nstr(Q2[2], 4))
    # C3: the obstruction
    n = 5; Sinv = {k: inverse(S[k]) for k in "mn"}
    N1 = {k: zeros(n, n) for k in "mn"}; N2 = {k: zeros(n, n) for k in "mn"}
    for k in "mn":
        for i in range(4): N1[k][i, 4] = c1[k][i]; N2[k][4, i] = c2[k][0, i]
    phi1 = {k: Sinv[k] * N1[k] for k in "mn"}; phi2 = {k: Sinv[k] * N2[k] for k in "mn"}; phi12 = {k: phi1[k] + phi2[k] for k in "mn"}
    D = d1_matrix(S)
    out["C3 ob(c1)"] = obstruction_class(S, phi1, D); out["C3 ob(c2)"] = obstruction_class(S, phi2, D); out["C3 ob(c1 + c2)"] = obstruction_class(S, phi12, D)
    # the Hom(1,1) component of the cross term (the H^2(Gamma; C) block)
    M0, M1, M2 = series_word(REL, S, phi12); out["C3 cross term (4,4) entry"] = nstr(M2[4, 4], 10)
    return out


def main():
    s2, s3 = sqrt(mpf(2)), sqrt(mpf(3)); res = []
    for q, mu, label in ((17 + 12 * s2, mpc(-1), "q0 = 17 + 12 sqrt2, mu = -1"), (17 - 12 * s2, mpc(-1), "q0' = 17 - 12 sqrt2, mu = -1"),
                         (7 + 4 * s3, mpc(0, 1), "7 + 4 sqrt3, mu = i (control: counts 0)"), (mpf(2), mpc(-1), "q = 2, mu = -1 (control: h1 = 0)")):
        r = run_point(q, mu, label); res.append(r); print(json.dumps(r, indent=1, default=str), flush=True)
    json.dump(res, open(HERE / "two_orders.json", "w"), indent=1, default=str)

if __name__ == "__main__":
    main()
