#!/usr/bin/env python3
"""sm:B1509 recomputed with main's own instruments: Ballas' convex-projective family of the figure-eight complement
(matrices as the seat's FINDINGS transcribes them), a central twist mu, the cocycles by linear algebra on the
two-generator presentation, and the class index by main's index_num (B1446) on the fibred presentation
u0 = n m^-1, u1 = m u0 m^-1, stable letter m, phi(u0) = u1, phi(u1) = u1 u0^-1 u1^2."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
for d in ("B1444_the_backgrounds_are_ends_of_periodic_curves", "B1445_the_mass_term_on_the_product_of_two_curves", "B1446_the_parabolic_points_and_the_branch_points"):
    sys.path.insert(0, str(HERE.parents[1] / d / "verification"))
import index_num as ix
from mpmath import mp, mpf, mpc, matrix, eye, zeros, inverse, sqrt, svd_c, nstr
mp.dps = 60
# phi([u0, u1]) = g [u0, u1] g^-1 with g = u1 u0^-1, so the meridian is t = g^-1 m: it commutes with the fibre's boundary,
# and t u t^-1 = g^-1 phi(u) g:  u0 -> u0 u1 u0^-1,  u1 -> u1^3 u0^-1.  index_num's peripheral group is <t, [x, y]>.
PHI = {1: [1, 2, -1], 2: [2, 2, 2, -1]}
REL = "mnMNmNMnmN"
def ballas(q, mu):
    t = mpf(q) / 2
    m = matrix([[1, 0, 1, t - 1], [0, 1, 1, t], [0, 0, 1, t + mpf(1) / 2], [0, 0, 0, 1]])
    n = matrix([[1, 0, 0, 0], [2 + 1 / t, 1, 0, 0], [2, 1, 1, 0], [1, 1, 0, 1]])
    return {"m": mu * m, "n": mu * n}
def word(w, g):
    r = eye(g["m"].rows)
    for ch in w: r = r * (g[ch] if ch.islower() else inverse(g[ch.lower()]))
    return r
def null(M, tol=mpf(10) ** (-30)):
    U, S, Vh = svd_c(M, full_matrices=True)
    r = sum(1 for i in range(len(S)) if abs(S[i]) > tol * max(1, abs(S[0])))
    return [Vh[i, :].H for i in range(r, M.cols)], r, [abs(S[i]) for i in range(len(S))]
def ext(g, c):
    """[[A, c], [0, 1]] on the generators"""
    out = {}
    for k in "mn":
        W = zeros(5, 5)
        for i in range(4):
            for j in range(4): W[i, j] = g[k][i, j]
            W[i, 4] = c[k][i]
        W[4, 4] = 1; out[k] = W
    return out
def cocycles(g):
    """a basis of Z^1 modulo B^1 for the 4-dim module: unknowns (c_m, c_n)"""
    cols = []
    for j in range(8):
        c = {"m": zeros(4, 1), "n": zeros(4, 1)}; c["mn"[j // 4]][j % 4] = 1
        R = word(REL, ext(g, c)); cols.append([R[i, 4] for i in range(4)])
    M = matrix(4, 8)
    for j in range(8):
        for i in range(4): M[i, j] = cols[j][i]
    Z, rk, S = null(M)
    Bm = matrix(8, 4)
    for j in range(4):
        v = zeros(4, 1); v[j] = 1; bm = (g["m"] - eye(4)) * v; bn = (g["n"] - eye(4)) * v
        for i in range(4): Bm[i, j] = bm[i]; Bm[4 + i, j] = bn[i]
    # rank of B and of [B | Z]
    Ub, Sb, Vb = svd_c(Bm); rb = sum(1 for i in range(len(Sb)) if abs(Sb[i]) > mpf(10) ** (-30))
    reps = []
    for zv in Z:
        T = matrix(8, 4 + len(reps) + 1)
        for i in range(8):
            for j in range(4): T[i, j] = Bm[i, j]
            for j, r in enumerate(reps): T[i, 4 + j] = r[i]
            T[i, 4 + len(reps)] = zv[i]
        U2, S2, V2 = svd_c(T)
        if sum(1 for i in range(len(S2)) if abs(S2[i]) > mpf(10) ** (-30)) > rb + len(reps): reps.append(zv)
    return reps, len(Z), rb
def fibred(W):
    u0 = W["n"] * inverse(W["m"]); u1 = W["m"] * u0 * inverse(W["m"])
    T = u0 * inverse(u1) * W["m"]; lam = u0 * u1 * inverse(u0) * inverse(u1); d = T * lam - lam * T
    assert max(abs(d[i, j]) for i in range(d.rows) for j in range(d.cols)) < mpf(10) ** (-40), "the meridian commutes with the fibre's boundary"
    return {1: u0, 2: u1}, T
def dualrep(W): return {k: inverse(W[k]).T for k in W}
def run(q, mu, label):
    g = ballas(q, mu); R = word(REL, g); assert max(abs(R[i, j] - (1 if i == j else 0)) for i in range(4) for j in range(4)) < mpf(10) ** (-45), "relator"
    reps, z, rb = cocycles(g); gd = dualrep(g); repsd, zd, rbd = cocycles(gd)
    print("%s: q = %s, mu = %s: dim Z1 %d, dim B1 %d, h1(A) = %d, h1(A*) = %d" % (label, nstr(q, 12), nstr(mu, 4), z, rb, len(reps), len(repsd)))
    for name, gg, rr in (("W1 = [[A, c], [0, 1]]", g, reps), ("W1[A*]", gd, repsd)):
        if not rr: continue
        c = {"m": matrix([rr[0][i] for i in range(4)]), "n": matrix([rr[0][4 + i] for i in range(4)])}
        W = ext(gg, c); h, T = fibred(W); I, a, b = ix.index(PHI, h, T)
        print("     %-22s index %+d   V: h0 %d h1 %d interior %d   V*: h0 %d h1 %d interior %d   smallest kept %s largest dropped %s" % (name, I, a["h0"], a["h1"], a["interior"], b["h0"], b["h1"], b["interior"], nstr(a["gaps"][1][0], 3), nstr(a["gaps"][1][1], 3)))
        # exterior square of the 5-dim module
        idx = [(i, j) for i in range(5) for j in range(i + 1, 5)]
        def lam2(Mx):
            L = zeros(10, 10)
            for a_, (i, j) in enumerate(idx):
                for b_, (k, l) in enumerate(idx): L[a_, b_] = Mx[i, k] * Mx[j, l] - Mx[i, l] * Mx[j, k]
            return L
        I2, a2, b2 = ix.index(PHI, {1: lam2(h[1]), 2: lam2(h[2])}, lam2(T))
        print("     exterior square        index %+d   h1 %d / %d interior %d / %d" % (I2, a2["h1"], b2["h1"], a2["interior"], b2["interior"]))
    # the bare module
    h, T = fibred(g); I, a, b = ix.index(PHI, h, T); print("     the four itself        index %+d   h1 %d / %d" % (I, a["h1"], b["h1"]))
if __name__ == "__main__":
    s2, s3 = sqrt(mpf(2)), sqrt(mpf(3))
    run(17 + 12 * s2, mpc(-1), "exceptional"); run(17 - 12 * s2, mpc(-1), "exceptional")
    run(7 + 4 * s3, mpc(0, 1), "exceptional"); run(7 - 4 * s3, mpc(0, -1), "exceptional")
    run(mpf(3), mpc(-1), "generic control"); run(17 + 12 * s2, mpc(1), "untwisted control")
