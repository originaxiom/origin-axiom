"""B1546 -- Proposition L, checked in one route (PREREGISTRATION.md section 3).  Structure only: the cup map delta1_W(c),
never a count.

Notation.  V_j^int is the interior part of tau's zeta^j eigenspace of H^1(N; rho), E_m the zeta^m eigenspace of H^1(N; C)
(dimensions 1, 2, 2, 2, 2), and B_jm(c) the block of the cup map of c in V_j on E_m.  K_m = {c : c u E_m = 0}.

  L0  the images of the blocks with j + m = t span subspaces H2_t of H^2(N; rho) whose sum is direct.
  L1  (a) for twisted j and each m outside {0, -j}, the pencil y -> (c -> c u y) on V_j^int (y in E_m) has rank exactly 2 for
      every y != 0, and its kernel lies in K_-j for every y; so a class of V_j^int outside K_-j has rank-2 blocks at the
      three m outside {0, -j}.  (b) the blocks of V_0^int have rank <= 1.  With L0 this gives: an interior class of cup rank
      <= 2 has every twisted part c_j in K_-j (the argument is in the PREREGISTRATION).
  L2  on Kc = V_0^int + sum_j (K_-j)^int the cup map's image is 4-dimensional, one line v_t in each H2_t (t != 0), so
      delta1_W(c) = sum_t v_t (x) Phi_t(c); on Kc0 = V_0^int + sum_j (K_0 cap K_-j)^int each block of Phi lies along one
      direction f_m of E_m* and the E_0 column vanishes; the gamma-part H (the E_0 column and the parts of each slot off
      f_m, a 4 x 5 matrix linear in the z_j-coordinates gamma of Kc / Kc0) has every 3 x 3 minor in an ideal containing
      gamma_j^3 for every j: rank <= 2 forces gamma = 0.
  L3  on Kc0 the f-coefficients form a 4 x 4 matrix F(c); every eigen-line of Kc0 (u_j, w_j, v_a, v_b) fills the entries
      predicted, the entries (t, m) and (5 - m, 5 - t) carry the same line, and the six ratios of their constants are a
      coboundary: F is persymmetric after scaling rows, columns and lines, so F J is a generic symmetric matrix S(c)."""
import itertools

import numpy as np
import sympy as sp


def _poly_gcd(a, b, p):
    """gcd of univariate polynomials (coefficient lists, low degree first) mod p"""
    def trim(x):
        x = [c % p for c in x]
        while x and x[-1] == 0:
            x.pop()
        return x
    a, b = trim(a), trim(b)
    while b:
        inv = pow(b[-1], p - 2, p)
        while len(a) >= len(b) and a:
            f = a[-1] * inv % p
            sh = len(a) - len(b)
            for i, c in enumerate(b):
                a[sh + i] = (a[sh + i] - f * c) % p
            a = trim(a)
        a, b = b, a
    return a


def check(G, LR):
    """every check of Proposition L in G's route (LR: the arc's lowrank_lib module, loaded by path)"""
    p, COLS = G.p, G.COLS
    rank = lambda A: LR._rank(np.asarray(A) % p, p)
    out = {}
    Vi = {j: G.vint(j) for j in range(5)}
    dims = {j: G.n(Vi[j]) for j in range(5)}
    out["dim V_j^int"] = [dims[j] for j in range(5)]
    Mv = {j: G.mats(Vi[j]) for j in range(5)}
    h = Mv[0][0].shape[0]
    # L0
    spans = {}
    for t in range(5):
        blocks = [Mv[j][i][:, COLS[(t - j) % 5]] for j in range(5) for i in range(dims[j])]
        spans[t] = LR._colbasis(np.hstack(blocks) % p, p)
    tot = rank(np.hstack([spans[t] for t in range(5)]))
    out["L0: dim H2_t"] = [spans[t].shape[1] for t in range(5)]
    out["L0: the sum is direct"] = bool(tot == sum(spans[t].shape[1] for t in range(5)))
    # L1a
    pencil = {}
    for j in range(1, 5):
        Bneg = np.vstack([np.stack([Mv[j][i][:, y] for i in range(dims[j])], axis=1) for y in COLS[(-j) % 5]]) % p
        for m in range(1, 5):
            if (j + m) % 5 == 0:
                continue
            A1 = np.stack([Mv[j][i][:, COLS[m][0]] for i in range(dims[j])], axis=1) % p
            A2 = np.stack([Mv[j][i][:, COLS[m][1]] for i in range(dims[j])], axis=1) % p
            # (i) the 2 x 2 minors (binary quadratics) have no common zero on P^1
            g, inf_common = None, True
            for r in itertools.combinations(range(h), 2):
                for cc in itertools.combinations(range(dims[j]), 2):
                    def q(y1, y2):
                        M = (y1 * A1[np.ix_(r, cc)] + y2 * A2[np.ix_(r, cc)]) % p
                        return int(M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]) % p
                    al, ga = q(1, 0), q(0, 1)
                    be = (q(1, 1) - al - ga) % p
                    if ga:
                        inf_common = False
                    if al or be or ga:
                        g = [al, be, ga] if g is None else _poly_gcd(g, [al, be, ga], p)
                if g is not None and len(g) == 1 and not inf_common:
                    break
            rank2_everywhere = g is not None and len(g) == 1 and not inf_common
            # (ii) [A(y); c -> c u E_-j] has rank <= 2 at five points of P^1: its minors (degree <= 3) vanish identically
            inside = all(rank(np.vstack([(A1 + t * A2) % p, Bneg])) == 2 for t in range(2, 7))
            pencil[f"j={j},m={m}"] = [rank2_everywhere, inside]
    out["L1a: pencil rank 2 at every y; kernels in K_-j"] = pencil
    # L1b
    l1b = True
    for m in range(5):
        for t in range(3):
            x = [1, t] if dims[0] == 2 else [1]
            B = sum(xx * Mv[0][i][:, COLS[m]] for i, xx in enumerate(x)) % p
            l1b &= rank(B) <= (0 if m == 0 else 1)
    out["L1b: V_0^int's blocks have rank <= 1 (0 on E_0)"] = bool(l1b)
    # L2
    KN = {j: G.zero_on(Vi[j], [(-j) % 5]) for j in range(1, 5)}
    out["dim (K_-j)^int"] = [G.n(KN[j]) for j in range(1, 5)]
    Kc = G.stack(Vi[0], *[KN[j] for j in range(1, 5)])
    Mk = G.mats(Kc)
    I4 = LR._colbasis(np.hstack(Mk) % p, p)
    out["L2: dim of the image on Kc"] = int(I4.shape[1])
    # graded basis of the image: v_t spanning I4 cap H2_t
    vt = {}
    for t in range(5):
        A = np.hstack([I4, (-spans[t]) % p]) % p
        N = LR._null(A, p)
        if N.shape[1]:
            vt[t] = (np.array(I4, dtype=object).dot(np.array(N[:I4.shape[1], :1], dtype=object)) % p).astype(np.int64).ravel()
    out["L2: image meets H2_t in"] = {t: int(t in vt) for t in range(5)}
    V4 = np.stack([vt[t] for t in range(1, 5)], axis=1) % p

    def phi(Mb):
        """X with V4 X = Mb (4 x 9), exact"""
        A = np.hstack([V4, Mb % p]) % p
        Ab = [[int(x) for x in r] for r in A]
        # solve by elimination on the augmented system
        rows, ncol = len(Ab), 4
        piv, r = [], 0
        for c in range(ncol):
            pr = next((i for i in range(r, rows) if Ab[i][c] % p), None)
            if pr is None:
                continue
            Ab[r], Ab[pr] = Ab[pr], Ab[r]
            inv = pow(Ab[r][c], p - 2, p)
            Ab[r] = [(x * inv) % p for x in Ab[r]]
            for i in range(rows):
                if i != r and Ab[i][c]:
                    f = Ab[i][c]
                    Ab[i] = [(x - f * y) % p for x, y in zip(Ab[i], Ab[r])]
            piv.append(c)
            r += 1
        assert piv == [0, 1, 2, 3]
        assert all(all(x == 0 for x in Ab[i][4:]) for i in range(4, rows)), "M(b) not in the image span"
        return np.array([Ab[i][4:] for i in range(4)], dtype=np.int64)
    nm = G.named()
    names0 = ["va", "vb"] + [f"{a}{j}" for j in range(1, 5) for a in "uw"]
    P0 = {x: phi(G.mats(nm[x])[0]) for x in names0}
    # f_m: the common direction of Kc0's slot entries
    fm, l2 = {}, True
    for m in range(1, 5):
        ents = [P0[x][t, COLS[m]] for x in names0 for t in range(4) if P0[x][t, COLS[m]].any()]
        l2 &= rank(np.stack(ents, axis=0)) == 1
        fm[m] = ents[0]
    l2 &= all(not P0[x][:, 0].any() for x in names0)
    out["L2: on Kc0 each slot lies along one f_m and the E_0 column vanishes"] = bool(l2)
    # z_j and H(gamma)
    gam = sp.symbols("g1:5")
    PZ = {}
    for j in range(1, 5):
        for i in range(G.n(KN[j])):
            P = phi(G.mats(G.col(KN[j], i).reshape(-1, 1) if G.F else G.col(KN[j], i).reshape(1, -1))[0])
            if P[:, 0].any():
                PZ[j] = P
                break

    def hpart(P):
        Hm = np.zeros((4, 5), dtype=np.int64)
        Hm[:, 0] = P[:, 0]
        for m in range(1, 5):
            for t in range(4):
                e = P[t, COLS[m]]
                Hm[t, m] = (int(fm[m][0]) * int(e[1]) - int(fm[m][1]) * int(e[0])) % p
        return Hm
    out["L2: H vanishes on Kc0"] = bool(all(not hpart(P0[x]).any() for x in names0))
    Hs = sp.zeros(4, 5)
    for j in range(1, 5):
        Hj = hpart(PZ[j])
        Hs += gam[j - 1] * sp.Matrix(Hj.tolist())
    minors = []
    for r in itertools.combinations(range(4), 3):
        for cc in itertools.combinations(range(5), 3):
            d = sp.expand(Hs.extract(list(r), list(cc)).det())
            if d != 0:
                minors.append(d)
    GB = sp.groebner(minors, *gam, modulus=p, order="grevlex")
    out["L2: gamma_j^3 in the ideal of H's 3 x 3 minors"] = [bool(GB.reduce(g ** 3)[1] == 0) for g in gam]
    # L3
    F = {}
    for x in names0:
        Fx = np.zeros((4, 4), dtype=np.int64)
        for t in range(4):
            for m in range(1, 5):
                e = P0[x][t, COLS[m]]
                k = 0 if fm[m][0] % p else 1
                Fx[t, m - 1] = int(e[k]) * pow(int(fm[m][k]), p - 2, p) % p
        F[x] = Fx
    supp = {x: sorted((t + 1, m + 1) for t in range(4) for m in range(4) if F[x][t, m]) for x in names0}
    pred = {}
    for j in range(1, 5):
        t = (3 * j) % 5
        pred[f"u{j}"] = [(t, (2 * j) % 5)]
    for x in names0:
        if x[0] in "wv":
            pred[x] = supp[x]
    l3a = all(supp[f"u{j}"] == pred[f"u{j}"] for j in range(1, 5))
    l3b = all(len(supp[x]) == 2 and supp[x][1] == (5 - supp[x][0][1], 5 - supp[x][0][0]) for x in names0 if x[0] in "wv")
    cover = sorted(sum(supp.values(), []))
    l3c = cover == sorted((t, m) for t in range(1, 5) for m in range(1, 5))
    inv = lambda a: pow(int(a) % p, p - 2, p)
    kap = {}
    for x in names0:
        if x[0] in "wv":
            (a1, b1), (a2, b2) = supp[x]
            kap[(a1, 5 - b1)] = int(F[x][a1 - 1, b1 - 1]) * inv(F[x][a2 - 1, b2 - 1]) % p

    def kk(a, b):
        if (a, b) in kap:
            return kap[(a, b)]
        if (b, a) in kap:
            return inv(kap[(b, a)])
        return None
    cyc = [kk(a, c) == kk(a, b) * kk(b, c) % p for a, b, c in itertools.permutations(range(1, 5), 3)
           if None not in (kk(a, b), kk(b, c), kk(a, c))]
    out["L3: u_j fills (3j, 2j); w_j, v_a, v_b fill a pair (t, m), (5-m, 5-t); the lines fill all 16 entries"] = \
        [bool(l3a), bool(l3b), bool(l3c)]
    out["L3: the pair ratios are a coboundary (persymmetric after scaling)"] = bool(cyc and all(cyc) and len(kap) == 6)
    out["L3: supports"] = {x: supp[x] for x in names0}
    return out


def holds(res):
    """True iff every check of Proposition L holds"""
    ok = res["L0: the sum is direct"] and res["L1b: V_0^int's blocks have rank <= 1 (0 on E_0)"]
    ok &= all(a and b for a, b in res["L1a: pencil rank 2 at every y; kernels in K_-j"].values())
    ok &= res["L2: dim of the image on Kc"] == 4 and res["L2: image meets H2_t in"] == {0: 0, 1: 1, 2: 1, 3: 1, 4: 1}
    ok &= res["L2: on Kc0 each slot lies along one f_m and the E_0 column vanishes"] and res["L2: H vanishes on Kc0"]
    ok &= all(res["L2: gamma_j^3 in the ideal of H's 3 x 3 minors"])
    ok &= all(res["L3: u_j fills (3j, 2j); w_j, v_a, v_b fill a pair (t, m), (5-m, 5-t); the lines fill all 16 entries"])
    ok &= res["L3: the pair ratios are a coboundary (persymmetric after scaling)"]
    ok &= res["dim V_j^int"] == [2, 4, 4, 4, 4] and res["dim (K_-j)^int"] == [3, 3, 3, 3]
    return bool(ok)
