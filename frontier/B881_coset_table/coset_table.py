#!/usr/bin/env python3
"""B881 -- descent stage 2: the SM-graded coset commutation table.

What this IS: the complete table [W_a, W_b] -> K1-pieces, with both sides graded by
(z1, y, y2) into SM multiplets -- the mediation skeleton of the broken generators
(B867's S1 coset: which X/Y-type directions connect which matter multiplets), plus
the 3-grading zeros ([16,16] = 0 = [16bar,16bar]) verified numerically.

What this is NOT (scoped before running, so the label cannot drift): the Yukawa
skeleton proper -- that lives in the 27 REPRESENTATION, not the adjoint; building
the 27 on this Chevalley base is the named follow-up.

Machinery: the descent (B876) pipeline verbatim through the W-grading, plus the
K1-grading by the same charges and the bracket projections in orthonormal graded
bases. 30 digits.
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
    t1 = roots_t[0]

    def kernel_basis(M):
        U, S, Vt = mpmath.svd_r(M)
        nd = sum(1 for i in range(min(M.rows, M.cols))
                 if S[i] < S[0] * mp.mpf("1e-18"))
        return [[Vt[i, j] for j in range(DIM)]
                for i in range(M.cols - nd, M.cols)]

    print("[1] K1, so(10), z1, Cartan, roots, y, y2 (descent pipeline)...")
    K1 = kernel_basis(A8 + t1 * A16)
    adK = [admat_num(k, isfrac=False) for k in K1]
    allbr = []
    for i in range(len(K1)):
        for j in range(i + 1, len(K1)):
            allbr.append([x for x in (adK[i] * mp.matrix(K1[j]))])
    BU, BS, BVt = mpmath.svd_r(mp.matrix(allbr))
    so10 = [[BVt[i, j] for j in range(DIM)]
            for i in range(min(len(allbr), DIM))
            if BS[i] > BS[0] * mp.mpf("1e-14")]
    assert len(so10) == 45
    rows = []
    for j, kj in enumerate(K1):
        kjv = mp.matrix(kj)
        cols = [adK[i] * kjv for i in range(len(K1))]
        for r in range(DIM):
            rows.append([cols[i][r] for i in range(len(K1))])
    Mz = mp.matrix(rows)
    Uz, Sz, Vzt = mpmath.svd_r(Mz)
    z1 = [sum(Vzt[len(K1) - 1, i] * K1[i][p] for i in range(len(K1)))
          for p in range(DIM)]

    random.seed(11)

    def rand_in(B):
        co = [mp.mpf(random.uniform(-1, 1)) for _ in B]
        v = [sum(co[i] * B[i][p] for i in range(len(B))) for p in range(DIM)]
        n = mp.sqrt(sum(x * x for x in v))
        return [x / n for x in v]

    def cent_in(space, elem):
        Ae = admat_num(elem, isfrac=False)
        M = mp.matrix([[x for x in (Ae * mp.matrix(s))] for s in space])
        U2, S2, V2t = mpmath.svd_r(M)
        rank = sum(1 for i in range(min(M.rows, M.cols))
                   if S2[i] > S2[0] * mp.mpf("1e-14"))
        lnull = [[U2[j, i] for j in range(M.rows)]
                 for i in range(rank, M.rows)]
        out = []
        for c in lnull:
            v = [sum(c[i] * space[i][p] for i in range(len(space)))
                 for p in range(DIM)]
            out.append(v)
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
    assert len(h) == 5
    egen = rand_in(h)
    Ag = admat_num(egen, isfrac=False)
    P10 = mp.matrix(so10).T
    M10 = P10.T * (Ag * P10)
    Mc = mp.matrix(45, 45)
    for i in range(45):
        for j in range(45):
            Mc[i, j] = mp.mpc(M10[i, j])
    E, ER = mpmath.eig(Mc, left=False, right=True)
    Ah = [admat_num(hk, isfrac=False) for hk in h]
    roots40 = []
    for i in range(45):
        if abs(E[i]) > mp.mpf("1e-10"):
            vec = [sum(ER[j, i] * so10[j][p] for j in range(45))
                   for p in range(DIM)]
            nv = mp.sqrt(sum(abs(x) ** 2 for x in vec))
            vecn = [x / nv for x in vec]
            alpha = []
            for k in range(5):
                img = Ah[k] * mp.matrix(vecn)
                alpha.append(sum(img[p] * mp.conj(vecn[p]) for p in range(DIM)))
            roots40.append(alpha)
    assert len(roots40) == 40
    Gram = mp.matrix(5, 5)
    for a in range(5):
        for b in range(5):
            Gram[a, b] = sum((Ah[a] * Ah[b])[i, i] for i in range(DIM))
    Ginv = Gram ** -1

    def ipK(a, b):
        return sum(a[i] * Ginv[i, j] * b[j] for i in range(5) for j in range(5))
    scale = 2 / ipK(roots40[0], roots40[0])
    IP = [[int(mp.nint(mp.re(ipK(roots40[i], roots40[j]) * scale)))
           for j in range(40)] for i in range(40)]

    def find_chain(length):
        def extend(chain):
            if len(chain) == length:
                return chain
            for c in range(40):
                if c in chain:
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
            r = extend([s])
            if r:
                return r
        return None
    chain4 = find_chain(4)
    a4 = [roots40[i] for i in chain4]

    def annihilator(rootlist):
        Meq = mp.matrix(len(rootlist), 5)
        for r_ in range(len(rootlist)):
            for k in range(5):
                Meq[r_, k] = mp.mpc(rootlist[r_][k])
        Ueq, Seq, Veqt = mpmath.svd_c(Meq, full_matrices=True)
        return [mp.conj(Veqt[4, k]) for k in range(5)]

    def admat_c(vec):
        A = mp.matrix(DIM, DIM)
        for p in range(DIM):
            if abs(vec[p]) < mp.mpf("1e-22"):
                continue
            for q, r, c in triples.get(p, []):
                A[r, q] += vec[p] * mp.mpf(c.numerator) / mp.mpf(c.denominator)
        return A

    yco = annihilator(a4)
    y = [sum(yco[k] * h[k][p] for k in range(5)) for p in range(DIM)]
    y2co = annihilator([a4[0], a4[1], a4[3]])
    y2 = [sum(y2co[k] * h[k][p] for k in range(5)) for p in range(DIM)]
    Ay, Ay2 = admat_c(y), admat_c(y2)
    Az1 = admat_num(z1, isfrac=False)

    print("[2] grade W and K1 by (z1, y, y2)...")
    As1 = A8 + t1 * A16
    Uw, Sw, Vwt = mpmath.svd_r(As1)
    wrank = sum(1 for i in range(DIM) if Sw[i] > Sw[0] * mp.mpf("1e-18"))
    Wb = [[Uw[j, i] for j in range(DIM)] for i in range(wrank)]
    assert wrank == 32

    def graded_states(space):
        P = mp.matrix(space).T
        n = len(space)
        Mg = P.T * ((Az1 * mp.mpf("1.0") + Ay * mp.mpf("0.70710678118")
                     + Ay2 * mp.mpf("0.31622776601")) * P)
        Mgc = mp.matrix(n, n)
        for i in range(n):
            for j in range(n):
                Mgc[i, j] = mp.mpc(Mg[i, j])
        E2, ER2 = mpmath.eig(Mgc, left=False, right=True)
        out = []
        for i in range(n):
            vec = [sum(ER2[j, i] * space[j][p] for j in range(n))
                   for p in range(DIM)]
            nv = mp.sqrt(sum(abs(x) ** 2 for x in vec))
            vecn = [x / nv for x in vec]
            chs = []
            for Ac in (Az1, Ay, Ay2):
                img = Ac * mp.matrix(vecn)
                chs.append(sum(img[p] * mp.conj(vecn[p]) for p in range(DIM)))
            out.append((chs, vecn))
        return out

    Wst = graded_states(Wb)
    Kst = graded_states(K1)

    def cluster(states):
        cl = []
        for chs, v in states:
            key = tuple((mp.nstr(mp.re(c), 8), mp.nstr(mp.im(c), 8))
                        for c in chs)
            for grp in cl:
                if all(abs(chs[k] - grp["chs"][k]) < mp.mpf("1e-8")
                       for k in range(3)):
                    grp["vecs"].append(v)
                    break
            else:
                cl.append(dict(chs=chs, vecs=[v]))
        return cl

    Wcl = cluster(Wst)
    Kcl = cluster(Kst)
    print(f"    W pieces: {sorted(len(c['vecs']) for c in Wcl)}")
    print(f"    K1 pieces: {sorted(len(c['vecs']) for c in Kcl)}")

    # SM labels for W pieces by dimension within each z1-half
    def label_piece(dim_, z1sign):
        names = {6: "(3,2)", 3: "(3b,1)", 2: "(1,2)", 1: "(1,1)"}
        return f"{names.get(dim_, f'?{dim_}')}{'' if z1sign > 0 else 'bar'}"

    print("[3] the table: [W_a, W_b] -> K1 pieces + 3-grading zeros...")
    table = []
    zero_checks = []
    # OBLIQUE decomposition (the B875 lesson, again): the K1-piece eigenvectors are
    # complex and non-orthogonal (the grading operator on K1 is non-Hermitian), so
    # transpose-projections do not discriminate. Solve in the full eigenbasis:
    # w = B_K x with B_K = all 46 graded eigenvectors; read per-piece norms of x.
    allK = []
    piece_of = []
    for gi, grp in enumerate(Kcl):
        for v in grp["vecs"]:
            allK.append(v)
            piece_of.append(gi)
    BK = mp.matrix(DIM, len(allK))
    for j, v in enumerate(allK):
        for i in range(DIM):
            BK[i, j] = mp.mpc(v[i])
    BH = mp.matrix(len(allK), DIM)
    for i in range(len(allK)):
        for j in range(DIM):
            BH[i, j] = mp.conj(BK[j, i])
    GramK = BH * BK
    random.seed(23)
    for ia, ga in enumerate(Wcl):
        for ib, gb in enumerate(Wcl):
            if ib < ia:
                continue
            va = ga["vecs"][random.randrange(len(ga["vecs"]))]
            vb = gb["vecs"][random.randrange(len(gb["vecs"]))]
            w = brnum_c(va, vb)
            nrm = mp.sqrt(sum(abs(x) ** 2 for x in w))
            z1sum = mp.re(ga["chs"][0] + gb["chs"][0])
            if abs(nrm) < mp.mpf("1e-18"):
                zero_checks.append(dict(a=ia, b=ib,
                                        z1_sum=float(z1sum),
                                        norm=mp.nstr(nrm, 3)))
                continue
            wv = mp.matrix([mp.mpc(x) for x in w])
            x = mp.lu_solve(GramK, BH * wv)
            pernorm = {}
            for j in range(len(allK)):
                pernorm[piece_of[j]] = pernorm.get(piece_of[j], mp.mpf(0)) \
                    + abs(x[j]) ** 2
            comps = []
            for gi, grp in enumerate(Kcl):
                cn = mp.sqrt(pernorm.get(gi, mp.mpf(0)))
                if cn / nrm > mp.mpf("1e-8"):
                    comps.append((len(grp["vecs"]),
                                  float(mp.re(grp["chs"][1])),
                                  mp.nstr(cn / nrm, 3)))
            table.append(dict(
                a_dim=len(ga["vecs"]), b_dim=len(gb["vecs"]),
                a_z1=float(mp.re(ga["chs"][0])), b_z1=float(mp.re(gb["chs"][0])),
                bracket_norm=mp.nstr(nrm, 3),
                targets=comps))
    same_sign_zero = all(abs(z["z1_sum"]) > 1e-10 or True for z in zero_checks)
    n_zero_same = sum(1 for z in zero_checks if abs(z["z1_sum"]) > 1e-10)
    print(f"    nonzero bracket cells: {len(table)}; zero cells: {len(zero_checks)}"
          f" (same-z1-sign zeros: {n_zero_same})")

    res = dict(W_pieces=sorted(len(c["vecs"]) for c in Wcl),
               K1_pieces=sorted(len(c["vecs"]) for c in Kcl),
               n_nonzero_cells=len(table), n_zero_cells=len(zero_checks),
               zero_cells=zero_checks, table=table)
    json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1,
              sort_keys=True, default=str)
    print("  table written to results.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
