#!/usr/bin/env python3
"""B875 -- the triality-tiling theorem, verified on this seat's build.

The solo seat's claim (JOINT NOTE 2026-08-03, their three-prime certificates):

    e6 = (so(8) + u(1)^2) + V1 + V2 + V3,   dim Vi = 16,
    Ki = core + Vi  (the three enhanced centralizers),
    Ki ^ Kj = core (30), span = 78,
    [Vi,Vi] <= core,   [Vi,Vj] = Vk  (cyclic).

Verified here on this seat's fully independent B854 build, three legs:

  LEG 1 (skeleton, 30 digits): kernels at the three enhancement points
    (t = 13 x banked-cubic roots, the [[b854-pencil-normalization-13x]] fact);
    all pairwise intersections dim 30, joint span 78.
  LEG 2 (core type, mod p = 40009 and 40037): the plane centralizer has
    dim 30, derived 28, center 2; with derived rank <= 4 the unique fit is
    D4 = so(8). The soft plane of the B874 census is the triality direction.
  LEG 3 (the multiplication law, 30 digits, OBLIQUE coordinates): canonical
    sectors Vi = ad(z)(Ki), z = x8 + 0.371 x16 generic in the core's center
    (= span(x8,x16): each xi is central in its own centralizer). THE SECTORS
    ARE NEARLY PARALLEL (the three roots differ by ~1e-3), so orthogonal
    projections CANNOT separate them -- a naive projector test reads 1.0
    everywhere. The law must be read in the direct-sum basis [core|V1|V2|V3]
    (exact rank 78 by Leg 1; condition ~1e11, fine at 30 digits): every
    bracket component is then unambiguous at ~1e-24.

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


def load():
    src = open(B854, encoding="utf-8").read()
    g = {"__file__": B854, "__name__": "b854"}
    exec(compile(src, B854, "exec"), g)
    return g


def build_triples(g):
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
    return basis, triples


def main():
    mp.dps = 30
    g = load()
    DIM = g["DIM"]
    basis, triples = build_triples(g)

    def admat_num(vec, isfrac=True):
        A = mp.zeros(DIM, DIM)
        for p in range(DIM):
            vp = vec[p]
            if isfrac:
                if not vp:
                    continue
                vp = mp.mpf(vp.numerator) / mp.mpf(vp.denominator)
            else:
                if abs(vp) < mp.mpf("1e-20"):
                    continue
            for q, r, c in triples.get(p, []):
                A[r, q] += vp * mp.mpf(c.numerator) / mp.mpf(c.denominator)
        return A

    def brnum(u, w):
        out = [mp.mpf(0)] * DIM
        for p in range(DIM):
            if abs(u[p]) < mp.mpf("1e-25"):
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
        smax = S[0]
        nd = sum(1 for i in range(min(M.rows, M.cols))
                 if S[i] < smax * mp.mpf("1e-18"))
        return [[Vt[i, j] for j in range(DIM)]
                for i in range(M.cols - nd, M.cols)]

    def stackrank(vecs):
        M = mp.matrix(vecs)
        U, S, Vt = mpmath.svd_r(M)
        return sum(1 for i in range(min(M.rows, M.cols))
                   if S[i] > S[0] * mp.mpf("1e-18"))

    # ---- LEG 1: skeleton
    Ks = [kernel_basis(A8 + t * A16) for t in roots_t]
    kdims = [len(K) for K in Ks]
    pair_int = {}
    for (i, j) in ((0, 1), (0, 2), (1, 2)):
        r = stackrank(Ks[i] + Ks[j])
        pair_int[f"K{i+1}^K{j+1}"] = kdims[i] + kdims[j] - r
    span = stackrank(Ks[0] + Ks[1] + Ks[2])

    # ---- LEG 3: canonical sectors + the law in oblique coordinates
    St = mp.matrix(2 * DIM, DIM)
    Aa = A8 + roots_t[0] * A16
    Ab = A8 + roots_t[1] * A16
    for i in range(DIM):
        for j in range(DIM):
            St[i, j] = Aa[i, j]
            St[DIM + i, j] = Ab[i, j]
    corebasis = kernel_basis(St)
    zf = [mp.mpf(c.numerator) / mp.mpf(c.denominator) for c in g["INV"][8]]
    z16 = [mp.mpf(c.numerator) / mp.mpf(c.denominator) for c in g["INV"][16]]
    z = [zf[p] + mp.mpf("0.371") * z16[p] for p in range(DIM)]
    Az = admat_num(z, isfrac=False)
    Vs = []
    for K in Ks:
        img = [[x for x in (Az * mp.matrix(k))] for k in K]
        VU, VS, VVt = mpmath.svd_r(mp.matrix(img))
        Vs.append([[VVt[i, j] for j in range(DIM)]
                   for i in range(len(img))
                   if VS[i] > VS[0] * mp.mpf("1e-12")])
    vdims = [len(v) for v in Vs]

    cols = corebasis + Vs[0] + Vs[1] + Vs[2]
    B = mp.matrix(cols).T
    U, S, Vt = mpmath.svd_r(B)
    cond = S[0] / S[DIM - 1]

    random.seed(3)

    def rand_in(Bb):
        co = [mp.mpf(random.uniform(-1, 1)) for _ in Bb]
        v = [sum(co[i] * Bb[i][p] for i in range(len(Bb))) for p in range(DIM)]
        n = mp.sqrt(sum(x * x for x in v))
        return [x / n for x in v]

    segs = [(0, 30), (30, 46), (46, 62), (62, 78)]

    def components(w):
        x = mp.lu_solve(B, mp.matrix(w))
        nw = mp.sqrt(sum(t * t for t in mp.matrix(w)))
        return [float(mp.sqrt(sum(x[i] ** 2 for i in range(a, b))) / nw)
                for a, b in segs]

    law = {}
    SAMPLES = 3
    for i in range(3):
        for j in range(i, 3):
            comps = [components(brnum(rand_in(Vs[i]), rand_in(Vs[j])))
                     for _ in range(SAMPLES)]
            worst = [max(c[s] for c in comps) for s in range(4)]
            law[f"[V{i+1},V{j+1}]"] = worst

    def law_ok():
        tol = 1e-15
        for i in range(3):
            for j in range(i, 3):
                w = law[f"[V{i+1},V{j+1}]"]
                if i == j:
                    if not (w[0] > 0.9 and max(w[1:]) < tol):
                        return False
                else:
                    k = ({0, 1, 2} - {i, j}).pop()
                    tgt = [0.0, 0.0, 0.0, 0.0]
                    if not (w[k + 1] > 0.9 and w[0] < tol
                            and max(w[s + 1] for s in range(3) if s != k) < tol):
                        return False
        return True

    # ---- LEG 2: core type mod two primes
    def core_type_mod(p):
        def tomod(fr):
            return int(fr.numerator) * pow(int(fr.denominator), -1, p) % p

        def admod(v):
            A = [[0] * DIM for _ in range(DIM)]
            for pp in range(DIM):
                if not v[pp]:
                    continue
                vp = tomod(v[pp])
                for q, r, c in triples.get(pp, []):
                    A[r][q] = (A[r][q] + vp * tomod(c)) % p
            return A
        M = admod(g["INV"][8]) + admod(g["INV"][16])
        nr = len(M)
        Mw = [row[:] for row in M]
        piv = {}
        r = 0
        for c in range(DIM):
            pr = next((i for i in range(r, nr) if Mw[i][c] % p), None)
            if pr is None:
                continue
            Mw[r], Mw[pr] = Mw[pr], Mw[r]
            inv = pow(Mw[r][c], -1, p)
            Mw[r] = [(x * inv) % p for x in Mw[r]]
            for i in range(nr):
                if i != r and Mw[i][c]:
                    f = Mw[i][c]
                    Mw[i] = [(Mw[i][j] - f * Mw[r][j]) % p for j in range(DIM)]
            piv[c] = r
            r += 1
        ker = []
        for fc in [c for c in range(DIM) if c not in piv]:
            v = [0] * DIM
            v[fc] = 1
            for c, rr in piv.items():
                v[c] = (-Mw[rr][fc]) % p
            ker.append(v)
        n = len(ker)

        def brmod(u, w):
            out = [0] * DIM
            for a in range(DIM):
                if not u[a]:
                    continue
                for q, r2, c in triples.get(a, []):
                    if w[q]:
                        out[r2] = (out[r2] + u[a] * w[q] * tomod(c)) % p
            return out

        def rank(rowsM, ncols):
            M2 = [row[:] for row in rowsM]
            rr = 0
            for c in range(ncols):
                pr = next((i for i in range(rr, len(M2)) if M2[i][c] % p), None)
                if pr is None:
                    continue
                M2[rr], M2[pr] = M2[pr], M2[rr]
                inv = pow(M2[rr][c], -1, p)
                for i in range(len(M2)):
                    if i != rr and M2[i][c]:
                        f = (M2[i][c] * inv) % p
                        M2[i] = [(M2[i][j] - f * M2[rr][j]) % p
                                 for j in range(ncols)]
                rr += 1
            return rr
        allbr = [brmod(ker[i], ker[j]) for i in range(n)
                 for j in range(i + 1, n)]
        dd = rank(allbr, DIM)
        bigrows = []
        for j in range(n):
            colsb = [brmod(ker[i], ker[j]) for i in range(n)]
            for r2 in range(DIM):
                bigrows.append([colsb[i][r2] for i in range(n)])
        zdim = n - rank(bigrows, n)
        return n, dd, zdim

    core_types = {str(p): core_type_mod(p) for p in (40009, 40037)}

    res = dict(
        kernel_dims=kdims, pairwise_intersections=pair_int, span=span,
        sector_dims=vdims, basis_condition=mp.nstr(cond, 3),
        law={k: [f"{x:.2e}" for x in v] for k, v in law.items()},
        law_ok=law_ok(),
        core_type_mod_p=core_types,
        core_is_so8_u1u1=all(t == (30, 28, 2) for t in
                             (tuple(v) for v in core_types.values())),
        nearly_parallel_note="orthogonal projections read 1.0 across sectors; "
                             "the law is only readable in oblique coordinates",
        tiling_verified=(kdims == [46, 46, 46]
                         and all(v == 30 for v in pair_int.values())
                         and span == 78 and vdims == [16, 16, 16]
                         and law_ok()
                         and all(tuple(v) == (30, 28, 2)
                                 for v in core_types.values())),
    )
    json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1,
              sort_keys=True)

    print("=" * 74)
    print("B875 -- the triality tiling, verified on this seat's build")
    print("=" * 74)
    print(f"  kernels {kdims}, pairwise ^ {pair_int}, span {span}")
    print(f"  sectors {vdims}, basis condition {res['basis_condition']}")
    for k in sorted(law):
        print(f"  {k} components (core,V1,V2,V3): {res['law'][k]}")
    print(f"  law holds: {res['law_ok']}")
    print(f"  core type mod p: {core_types}  -> so(8)+u(1)^2: "
          f"{res['core_is_so8_u1u1']}")
    print(f"  TILING VERIFIED: {res['tiling_verified']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
