#!/usr/bin/env python3
"""B876 -- THE DESCENT: the triality sectors tracked down the fused chain.

The joint cell agreed with the solo seat (their (a), the priority): fix K1's breaking,
impose the fused-chain Levi (the object's own torus does NOT supply the step-2 charge
-- B874 addendum -- so the breaking is B861's, as it should be), and ask whether the
Galois triple survives to the SM as three of anything.

Pipeline (30 digits throughout; the B875 oblique-coordinates lesson applied):
  1. K1 at the first enhancement point; core; canonical sectors V1, V2, V3 (B875).
  2. so(10)_1 = the derived algebra of K1 (dim 45); z1 = K1's center (dim 1).
  3. A Cartan h of so(10)_1 by iterated centralizers of generic elements.
  4. The root system of so(10)_1 w.r.t. h by joint diagonalization (40 roots).
  5. The u(5) Levi: pick 4 roots forming an A4 subsystem (inner-product graph via
     the trace form); y = the Cartan direction with alpha(y) = 0 exactly on the A4
     span (20 roots) -- centralizer check: dim 25 inside so(10)_1.
  6. The SM Levi one rung down: an A2+A1 subsystem inside the A4; y2 with
     alpha(y2) = 0 on it; centralizer check: dim 13 inside u(5) (su(3)+su(2)+2u(1)).
  7. Grade THE COSET W = im(ad s1) = V2+V3 (the K1-module; the individual
     sectors are NOT stable under the Levi charges -- design correction recorded
     in-line) by the commuting charges (z1, y, y2): the 16+16bar branching and
     its SM refinement.
  8. TRANSVERSALITY: the oblique V2/V3 components of every graded piece -- the
     quantitative answer to whether the triple's identity survives within a
     single breaking. The table IS the deliverable.

Mathematics scope; nothing to CLAIMS.md; Gate 5 untouched.
"""
import json
import os
import random

import mpmath
from mpmath import mp

HERE = os.path.dirname(os.path.abspath(__file__))
B854 = os.path.normpath(os.path.join(HERE, "..", "B854_centralizer_exact",
                                     "e6_centralizer.py"))
CUBIC = [500716339200, -159667200, -28224, 1]


def main():
    mp.dps = 30
    src = open(B854, encoding="utf-8").read()
    g = {"__file__": B854, "__name__": "b854"}
    exec(compile(src, B854, "exec"), g)
    DIM, N = g["DIM"], g["N"]
    br, hvec, evec, ROOTS = g["br"], g["hvec"], g["evec"], g["ROOTS"]
    basis = [hvec(i) for i in range(N)] + [evec(r) for r in ROOTS]
    triples = {}
    for p in range(DIM):
        for q in range(DIM):
            v = br(basis[p], basis[q])
            for r, c in enumerate(v):
                if c:
                    triples.setdefault(p, []).append((q, r, c))

    def admat_num(vec, isfrac=True):
        A = mp.zeros(DIM, DIM)
        for p in range(DIM):
            vp = vec[p]
            if isfrac:
                if not vp:
                    continue
                vp = mp.mpf(vp.numerator) / mp.mpf(vp.denominator)
            else:
                if abs(vp) < mp.mpf("1e-22"):
                    continue
            for q, r, c in triples.get(p, []):
                A[r, q] += vp * mp.mpf(c.numerator) / mp.mpf(c.denominator)
        return A

    def brnum(u, w):
        out = [mp.mpf(0)] * DIM
        for p in range(DIM):
            if abs(u[p]) < mp.mpf("1e-26"):
                continue
            for q, r, c in triples.get(p, []):
                out[r] += u[p] * w[q] * mp.mpf(c.numerator) / mp.mpf(c.denominator)
        return out

    def brnum_c(u, w):
        out = [mp.mpc(0)] * DIM
        for p in range(DIM):
            if abs(u[p]) < mp.mpf("1e-26"):
                continue
            for q, r, c in triples.get(p, []):
                out[r] += u[p] * w[q] * mp.mpf(c.numerator) / mp.mpf(c.denominator)
        return out

    A8 = admat_num(g["INV"][8])
    A16 = admat_num(g["INV"][16])
    roots_t = sorted(13 * mp.re(r) for r in mpmath.polyroots(
        [mp.mpf(c) for c in CUBIC], maxsteps=200, extraprec=120))

    def kernel_basis(M):
        U, S, Vt = mpmath.svd_r(M)
        nd = sum(1 for i in range(min(M.rows, M.cols))
                 if S[i] < S[0] * mp.mpf("1e-18"))
        return [[Vt[i, j] for j in range(DIM)]
                for i in range(M.cols - nd, M.cols)]

    print("[1] spaces...")
    Ks = [kernel_basis(A8 + t * A16) for t in roots_t]
    St = mp.matrix(2 * DIM, DIM)
    Aa = A8 + roots_t[0] * A16
    Ab = A8 + roots_t[1] * A16
    for i in range(DIM):
        for j in range(DIM):
            St[i, j] = Aa[i, j]
            St[DIM + i, j] = Ab[i, j]
    corebasis = kernel_basis(St)
    zf8 = [mp.mpf(c.numerator) / mp.mpf(c.denominator) for c in g["INV"][8]]
    zf16 = [mp.mpf(c.numerator) / mp.mpf(c.denominator) for c in g["INV"][16]]
    zgen = [zf8[p] + mp.mpf("0.371") * zf16[p] for p in range(DIM)]
    Azgen = admat_num(zgen, isfrac=False)
    Vs = []
    for K in Ks:
        img = [[x for x in (Azgen * mp.matrix(k))] for k in K]
        VU, VS, VVt = mpmath.svd_r(mp.matrix(img))
        Vs.append([[VVt[i, j] for j in range(DIM)]
                   for i in range(len(img)) if VS[i] > VS[0] * mp.mpf("1e-12")])
    assert [len(v) for v in Vs] == [16, 16, 16]

    # ---- [2] so(10)_1 = derived(K1); z1 = center(K1)
    print("[2] so(10)_1 and z1...")
    K1 = Ks[0]
    adK = [admat_num(k, isfrac=False) for k in K1]
    allbr = []
    for i in range(len(K1)):
        for j in range(i + 1, len(K1)):
            allbr.append([x for x in (adK[i] * mp.matrix(K1[j]))])
    BU, BS, BVt = mpmath.svd_r(mp.matrix(allbr))
    so10 = [[BVt[i, j] for j in range(DIM)]
            for i in range(min(len(allbr), DIM))
            if BS[i] > BS[0] * mp.mpf("1e-14")]
    assert len(so10) == 45, len(so10)
    rows = []
    for j, kj in enumerate(K1):
        kjv = mp.matrix(kj)
        cols = [adK[i] * kjv for i in range(len(K1))]
        for r in range(DIM):
            rows.append([cols[i][r] for i in range(len(K1))])
    Mz = mp.matrix(rows)
    Uz, Sz, Vzt = mpmath.svd_r(Mz)
    assert sum(1 for i in range(len(K1)) if Sz[i] < Sz[0] * mp.mpf("1e-15")) == 1
    z1 = [sum(Vzt[len(K1) - 1, i] * K1[i][p] for i in range(len(K1)))
          for p in range(DIM)]

    # ---- [3] a Cartan of so(10)_1 by iterated centralizers
    print("[3] Cartan...")
    random.seed(11)

    def rand_in(B):
        co = [mp.mpf(random.uniform(-1, 1)) for _ in B]
        v = [sum(co[i] * B[i][p] for i in range(len(B))) for p in range(DIM)]
        n = mp.sqrt(sum(x * x for x in v))
        return [x / n for x in v]

    def cent_in(space, elem):
        """centralizer of elem inside span(space)."""
        Ae = admat_num(elem, isfrac=False)
        M = mp.matrix([[x for x in (Ae * mp.matrix(s))] for s in space])
        U, S, Vt = mpmath.svd_r(M.T)   # columns = images; nullspace in coeff space
        # want coeffs c with sum c_i [e, s_i] = 0: nullspace of M^T? M rows = images
        # M is (len(space) x DIM): row i = [e, s_i]. Need c with sum c_i row_i = 0:
        # nullspace of M^T (DIM x n) -> right null of M^T = left null of M.
        U2, S2, V2t = mpmath.svd_r(M)
        nd = sum(1 for i in range(min(M.rows, M.cols))
                 if (S2[i] if i < min(M.rows, M.cols) else 0) < S2[0] * mp.mpf("1e-14"))
        # rows of V2t beyond rank give right-null of M (coeff-space? no: M x = 0 with
        # x in R^DIM). Wrong space. Use left-null: columns of U2 beyond rank.
        rank = M.cols and sum(1 for i in range(min(M.rows, M.cols))
                              if S2[i] > S2[0] * mp.mpf("1e-14"))
        lnull = [[U2[j, i] for j in range(M.rows)]
                 for i in range(rank, M.rows)]
        out = []
        for c in lnull:
            v = [sum(c[i] * space[i][p] for i in range(len(space)))
                 for p in range(DIM)]
            out.append(v)
        # orthonormalize
        if not out:
            return []
        OU, OS, OVt = mpmath.svd_r(mp.matrix(out))
        return [[OVt[i, j] for j in range(DIM)]
                for i in range(len(out)) if OS[i] > OS[0] * mp.mpf("1e-14")]

    h = so10
    while len(h) > 5:
        e = rand_in(h)
        h2 = cent_in(h, e)
        if len(h2) < len(h):
            h = h2
    assert len(h) == 5, len(h)

    # ---- [4] roots of so(10)_1 w.r.t. h
    print("[4] roots...")
    egen = rand_in(h)
    Ag = admat_num(egen, isfrac=False)
    # restrict ad(egen) to so(10) (invariant) and eigen-decompose over C
    P10 = mp.matrix(so10).T
    M10 = P10.T * (Ag * P10)
    Mc = mp.matrix(45, 45)
    for i in range(45):
        for j in range(45):
            Mc[i, j] = mp.mpc(M10[i, j])
    E, ER = mpmath.eig(Mc, left=False, right=True)
    rootvecs = []   # (eigenvalue, vector in C^DIM)
    for i in range(45):
        if abs(E[i]) > mp.mpf("1e-10"):
            vec = [sum(ER[j, i] * so10[j][p] for j in range(45))
                   for p in range(DIM)]
            rootvecs.append((E[i], vec))
    assert len(rootvecs) == 40, len(rootvecs)
    # root coordinates alpha(h_k) via [h_k, X] = alpha_k X
    Ah = [admat_num(hk, isfrac=False) for hk in h]
    roots40 = []
    for ev, vec in rootvecs:
        nv = mp.sqrt(sum(abs(x) ** 2 for x in vec))
        vecn = [x / nv for x in vec]
        alpha = []
        for k in range(5):
            img = Ah[k] * mp.matrix(vecn)
            # alpha_k = <img, vecn> (vec is an eigenvector)
            a = sum(img[p] * mp.conj(vecn[p]) for p in range(DIM))
            alpha.append(a)
        roots40.append((alpha, vecn))

    # ---- [5] the u(5) Levi over C: Killing-Gram inner products, integer root
    # graph, an A4 chain by combinatorial search, COMPLEX annihilator charge y.
    # (The descent is a C-statement -- 16 -> 10+5bar+1 lives in the complexified
    # algebra -- so y need not be real; a mixed Cartan's complex roots are fine.)
    print("[5] u(5) Levi...")
    # Gram of h under the trace form; inner products on roots via G^{-1} (bilinear)
    Gram = mp.matrix(5, 5)
    for a in range(5):
        for b in range(5):
            Gram[a, b] = sum((Ah[a] * Ah[b])[i, i] for i in range(DIM))
    Ginv = Gram ** -1
    alphas = [a for a, _ in roots40]

    def ipK(a, b):
        return sum(a[i] * Ginv[i, j] * b[j] for i in range(5) for j in range(5))

    n2s = [ipK(a, a) for a in alphas]
    scale = 2 / n2s[0]
    IP = [[None] * 40 for _ in range(40)]
    for i in range(40):
        for j in range(40):
            v = ipK(alphas[i], alphas[j]) * scale
            vi = int(mp.nint(mp.re(v)))
            assert abs(v - vi) < mp.mpf("1e-8"), (i, j, mp.nstr(v, 8))
            IP[i][j] = vi
    assert all(IP[i][i] == 2 for i in range(40)), "not simply-laced-normalized"

    def find_chain(length, avoid=()):
        """a chain a1-...-an with consecutive IP = -1, others 0."""
        def extend(chain):
            if len(chain) == length:
                return chain
            for c in range(40):
                if c in chain or c in avoid:
                    continue
                if IP[chain[-1]][c] != -1:
                    continue
                if any(IP[x][c] != 0 for x in chain[:-1]):
                    continue
                r = extend(chain + [c])
                if r:
                    return r
            return None
        for s in range(40):
            if s in avoid:
                continue
            r = extend([s])
            if r:
                return r
        return None

    chain4 = find_chain(4)
    assert chain4, "no A4 chain in the root graph"
    a4 = [alphas[i] for i in chain4]

    def annihilator(rootlist):
        """complex y in h_C with alpha(y) = 0 for the given roots (coords in h)."""
        Meq = mp.matrix(len(rootlist), 5)
        for r_ in range(len(rootlist)):
            for k in range(5):
                Meq[r_, k] = mp.mpc(rootlist[r_][k])
        Ueq, Seq, Veqt = mpmath.svd_c(Meq, full_matrices=True)
        return [mp.conj(Veqt[4, k]) for k in range(5)]

    yco = annihilator(a4)
    y = [sum(yco[k] * h[k][p] for k in range(5)) for p in range(DIM)]
    Ay_full = None  # built below

    def admat_c(vec):
        A = mp.matrix(DIM, DIM)
        for p in range(DIM):
            vp = vec[p]
            if abs(vp) < mp.mpf("1e-22"):
                continue
            for q, r, c in triples.get(p, []):
                A[r, q] += vp * mp.mpf(c.numerator) / mp.mpf(c.denominator)
        return A

    Ay = admat_c(y)
    # dim Cent_{so(10)}(y) = 45 - rank(ad y | so10): expect 25 for u(5)
    P10c = mp.matrix(DIM, 45)
    for i in range(DIM):
        for j in range(45):
            P10c[i, j] = mp.mpc(so10[j][i])
    My = P10c.T * (Ay * P10c)
    Uy, Sy, Vyt = mpmath.svd_c(My)
    rky = sum(1 for i in range(45) if Sy[i] > Sy[0] * mp.mpf("1e-14"))
    print(f"    dim Cent_so10(y) = {45 - rky}  (u(5) needs 25)")

    # ---- [6] the SM Levi: A2+A1 = the chain minus its 3rd node
    print("[6] SM Levi...")
    sm_sub = [a4[0], a4[1], a4[3]]
    y2co = annihilator(sm_sub)
    y2 = [sum(y2co[k] * h[k][p] for k in range(5)) for p in range(DIM)]
    Ay2 = admat_c(y2)
    My2 = P10c.T * (Ay2 * P10c)
    U2s, S2s, V2st = mpmath.svd_c(My2)
    rky2 = sum(1 for i in range(45) if S2s[i] > S2s[0] * mp.mpf("1e-14"))
    # joint centralizer: rank of stacked (ad y, ad y2) on so10
    Mst = mp.matrix(90, 45)
    for i in range(45):
        for j in range(45):
            Mst[i, j] = My[i, j]
            Mst[45 + i, j] = My2[i, j]
    Us, Ss, Vst = mpmath.svd_c(Mst)
    rks = sum(1 for i in range(45) if Ss[i] > Ss[0] * mp.mpf("1e-14"))
    c_both_dim = 45 - rks
    print(f"    dim Cent_so10(y2) = {45 - rky2};  dim Cent_so10(y, y2) = "
          f"{c_both_dim}  (SM+2u1 needs 13)")

    # ---- [7] grade THE COSET by (z1, y, y2) -- the well-posed object.
    # DESIGN CORRECTION, recorded: the individual sectors V_i are NOT stable under
    # the Levi charges (y does not commute with the ad(x_j) defining them), so
    # "grade each sector" is ill-posed -- the first draft's per-sector charges
    # refused to cluster, which is how this was caught. The K1-module is the coset
    # W = im(ad s1) = V2 + V3 as a SPACE (B872's 16+16bar); z1, y, y2 all lie in
    # K1 and commute pairwise, so they grade W simultaneously. The descent question
    # becomes: how do W's SM-graded pieces sit relative to the V2/V3 split?
    print("[7] grading the coset W = V2+V3 by (z1, y, y2)...")
    s1vec = [zf8[p] + roots_t[0] * zf16[p] for p in range(DIM)]
    As1 = admat_num(s1vec, isfrac=False)
    Uw, Sw, Vwt = mpmath.svd_r(As1)
    wrank = sum(1 for i in range(DIM) if Sw[i] > Sw[0] * mp.mpf("1e-18"))
    Wb = [[Uw[j, i] for j in range(DIM)] for i in range(wrank)]
    assert wrank == 32, wrank
    Az1 = admat_num(z1, isfrac=False)
    PW = mp.matrix(Wb).T                      # 78 x 32, orthonormal columns
    def restr(A):
        M = PW.T * (A * PW)
        Mc = mp.matrix(32, 32)
        for i in range(32):
            for j in range(32):
                Mc[i, j] = mp.mpc(M[i, j])
        return Mc
    Rz1, Ry, Ry2 = restr(Az1), restr(Ay), restr(Ay2)
    # simultaneous eigenbasis via a generic combination
    Mmix = Rz1 * mp.mpf("1.0") + Ry * mp.mpf("0.70710678118") \
        + Ry2 * mp.mpf("0.31622776601")
    Em, ERm = mpmath.eig(Mmix, left=False, right=True)
    states = []
    for i in range(32):
        v = mp.matrix([ERm[j, i] for j in range(32)])
        nv = mp.sqrt(sum(abs(v[j]) ** 2 for j in range(32)))
        v = v * (1 / nv)
        chs = []
        for R in (Rz1, Ry, Ry2):
            img = R * v
            chs.append(sum(img[j] * mp.conj(v[j]) for j in range(32)))
        states.append((chs, v))

    def cluster_vals(vals, tol="1e-9"):
        cl = []
        for idx, v in enumerate(vals):
            for c in cl:
                if abs(v - c[0]) < mp.mpf(tol) * max(1, abs(v)):
                    c[1].append(idx)
                    break
            else:
                cl.append([v, [idx]])
        return cl

    zcl = cluster_vals([s[0][0] for s in states])
    print(f"    z1-charge clusters on W: {sorted(len(c[1]) for c in zcl)}"
          f"  (16+16bar needs [16, 16])")
    ycl = cluster_vals([s[0][1] for s in states])
    ymults = sorted((len(c[1]) for c in ycl), reverse=True)
    print(f"    y-charge multiplicities on W: {ymults}"
          f"  (16+16bar -> 10+5b+1+conj needs [10, 10, 5, 5, 1, 1])")
    # joint (y, y2) clustering = the SM-multiplet pattern
    jcl = cluster_vals([s[0][1] * 1000 + s[0][2] for s in states])
    jmults = sorted((len(c[1]) for c in jcl), reverse=True)
    print(f"    joint (y,y2) multiplicities: {jmults}"
          f"  (16 -> 6+3+3+2+1+1 doubled)")

    # ---- [8] TRANSVERSALITY: oblique V2/V3 components of each graded piece
    print("[8] transversality of the SM grading vs the V2/V3 split...")
    cols = corebasis + Vs[0] + Vs[1] + Vs[2]
    Bob = mp.matrix(cols).T
    segs = [(0, 30), (30, 46), (46, 62), (62, 78)]

    def oblique(wfull):
        x = mp.lu_solve(Bob, mp.matrix(wfull))
        nw = mp.sqrt(sum(abs(t) ** 2 for t in mp.matrix(wfull)))
        return [float(mp.sqrt(sum(abs(x[i]) ** 2 for i in range(a, b))) / nw)
                for a, b in segs]

    trans = []
    for c in ycl:
        yval = c[0]
        piece = c[1]
        v2c, v3c = [], []
        for idx in piece:
            v = states[idx][1]
            wfull = [sum(v[j] * mp.mpc(Wb[j][p]) for j in range(32))
                     for p in range(DIM)]
            comp = oblique(wfull)
            v2c.append(comp[2])
            v3c.append(comp[3])
        trans.append(dict(y=mp.nstr(yval, 8), dim=len(piece),
                          v2_min=min(v2c), v2_max=max(v2c),
                          v3_min=min(v3c), v3_max=max(v3c)))
        print(f"    y-piece dim {len(piece):2d}: V2-component range "
              f"[{min(v2c):.3f}, {max(v2c):.3f}], V3 range "
              f"[{min(v3c):.3f}, {max(v3c):.3f}]")

    print("[9] per-sector grading is ill-posed (recorded); summary...")
    res = dict(
        cent_y=45 - rky, cent_y2=45 - rky2, cent_both=c_both_dim,
        sector_dims=[len(v) for v in Vs], so10_dim=len(so10),
        z1_clusters=sorted(len(c[1]) for c in zcl),
        y_multiplicities=ymults,
        joint_multiplicities=jmults,
        transversality=trans,
        per_sector_grading_ill_posed=True,
    )
    json.dump(res, open(os.path.join(HERE, "results_stage1.json"), "w"),
              indent=1, sort_keys=True, default=str)
    print("stage-1 written; the graded law runs as stage 2 once the grading is confirmed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
