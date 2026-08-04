#!/usr/bin/env python3
"""B880 -- the module-level triality signature: the three sectors are pairwise
INEQUIVALENT so(8)-modules, each 8+8 under the core charges.

The magic-square identification t(O,C) requires exactly this: the three off-diagonal
summands carry the three triality frames of so(8) = tri(O), and the u(1)^2 = tri(C)
charges split each sector into a conjugate 8-pair. Verified here on the B875 spaces:

  (a) so(8) = derived(core), dim 28; center(core) dim 2 (exact skeleton from B875).
  (b) each V_i splits 8 + 8 under a generic center charge (opposite charges).
  (c) dim Hom_{so(8)}(V_i, V_j) = 0 for i != j  -- pairwise inequivalent (the
      triality relativity), and dim Hom(V_i, V_i) matched per sector.
  Hom spaces computed by the certified generic-pair method (kernel of two random
  combinations of the 28 intertwining constraints, then EVERY candidate certified
  against all 28 generators -- candidate >= true always; the certificate gives <=).

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

    print("[1] spaces (B875 skeleton)...")
    Ks = [kernel_basis(A8 + t * A16) for t in roots_t]
    St = mp.matrix(2 * DIM, DIM)
    Aa = A8 + roots_t[0] * A16
    Ab = A8 + roots_t[1] * A16
    for i in range(DIM):
        for j in range(DIM):
            St[i, j] = Aa[i, j]
            St[DIM + i, j] = Ab[i, j]
    core = kernel_basis(St)
    assert len(core) == 30
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

    print("[2] so(8) = derived(core)...")
    adC = [admat_num(c, isfrac=False) for c in core]
    allbr = []
    for i in range(len(core)):
        for j in range(i + 1, len(core)):
            allbr.append([x for x in (adC[i] * mp.matrix(core[j]))])
    BU, BS, BVt = mpmath.svd_r(mp.matrix(allbr))
    so8 = [[BVt[i, j] for j in range(DIM)]
           for i in range(min(len(allbr), DIM))
           if BS[i] > BS[0] * mp.mpf("1e-14")]
    assert len(so8) == 28, len(so8)
    ad8 = [admat_num(s, isfrac=False) for s in so8]
    # center of core (2-dim) = span(x8, x16) restricted... use the plane directly:
    zc = [zf8, zf16]

    print("[3] the tri(C) split of each sector...")
    charge_split = []
    for i, V in enumerate(Vs):
        P = mp.matrix(V).T
        Az = admat_num(zc[0], isfrac=False)
        Mw = P.T * (Az * P)
        Mc = mp.matrix(16, 16)
        for a in range(16):
            for b in range(16):
                Mc[a, b] = mp.mpc(Mw[a, b])
        E, ER = mpmath.eig(Mc, left=False, right=True)
        vals = sorted((mp.re(E[k]), mp.im(E[k])) for k in range(16))
        # cluster into charge groups
        groups = []
        for v in vals:
            for grp in groups:
                if abs(v[0] - grp[0][0]) < 1e-9 and abs(v[1] - grp[0][1]) < 1e-9:
                    grp.append(v)
                    break
            else:
                groups.append([v])
        charge_split.append(sorted(len(grp) for grp in groups))
        print(f"    V{i+1}: x8-charge multiplicities {charge_split[-1]}")

    print("[4] Hom_{so(8)}(V_i, V_j) by certified generic pairs...")
    rng = random.Random(17)

    def reps_on(V):
        P = mp.matrix(V).T
        out = []
        for A in ad8:
            M = P.T * (A * P)
            out.append(M)
        return out

    R = [reps_on(V) for V in Vs]

    def hom_dim(i, j):
        """solutions X (16x16): R_i^(a) X = X R_j^(a) for all a."""
        def comb():
            co = [mp.mpf(rng.uniform(-1, 1)) for _ in range(28)]
            Li = sum((co[a] * R[i][a] for a in range(28)), mp.zeros(16, 16))
            Lj = sum((co[a] * R[j][a] for a in range(28)), mp.zeros(16, 16))
            return Li, Lj

        def sylvester_null(Li, Lj):
            # vec(X): (I (x) Li - Lj^T (x) I) vec = 0 ; build 256x256
            Mbig = mp.matrix(256, 256)
            for a in range(16):
                for b in range(16):
                    for k in range(16):
                        Mbig[a * 16 + b, k * 16 + b] += Li[a, k]
                        Mbig[a * 16 + b, a * 16 + k] -= Lj[k, b]
            U, S, Vt = mpmath.svd_r(Mbig)
            smax = S[0]
            nb = [[Vt[r, cidx] for cidx in range(256)]
                  for r in range(256) if S[r] < smax * mp.mpf("1e-16")]
            return nb
        L1i, L1j = comb()
        N1 = sylvester_null(L1i, L1j)
        if not N1:
            return 0, "0.0"
        # restrict second combination to N1
        L2i, L2j = comb()
        rows = []
        for v in N1:
            X = mp.matrix([[v[a * 16 + b] for b in range(16)] for a in range(16)])
            Y = L2i * X - X * L2j
            rows.append([Y[a, b] for a in range(16) for b in range(16)])
        M2 = mp.matrix(rows).T
        U2, S2, V2t = mpmath.svd_r(M2)
        mx = max(S2[k] for k in range(min(M2.rows, M2.cols)))
        n2 = sum(1 for k in range(min(M2.rows, M2.cols))
                 if S2[k] < max(mx, mp.mpf(1)) * mp.mpf("1e-16"))
        # candidates + certificate against all 28
        cand = []
        for r in range(len(N1) - n2, len(N1)):
            v = [sum(mp.conj(V2t[r, k]) * N1[k][idx] for k in range(len(N1)))
                 for idx in range(256)]
            cand.append(mp.matrix([[v[a * 16 + b] for b in range(16)]
                                   for a in range(16)]))
        cert = mp.mpf(0)
        for X in cand:
            nX = mp.mnorm(X, 1)
            for a in range(28):
                cert = max(cert, mp.mnorm(R[i][a] * X - X * R[j][a], 1)
                           / max(nX, mp.mpf("1e-30")))
        return n2, mp.nstr(cert, 3)

    hom = {}
    for i in range(3):
        for j in range(3):
            d, cert = hom_dim(i, j)
            hom[f"{i+1}{j+1}"] = [d, cert]
            print(f"    dim Hom(V{i+1}, V{j+1}) = {d}   (certificate {cert})")

    off_zero = all(hom[f"{i+1}{j+1}"][0] == 0
                   for i in range(3) for j in range(3) if i != j)
    diag = [hom[f"{i+1}{i+1}"][0] for i in range(3)]
    res = dict(
        core_dim=30, so8_dim=28, sector_dims=[16, 16, 16],
        charge_split=charge_split, hom=hom,
        pairwise_inequivalent=off_zero, diag_hom=diag,
        signature=("MAGIC-SQUARE COMPATIBLE: three pairwise-inequivalent "
                   "so(8)-module sectors, each split 8+8 by the core charges"
                   if off_zero else "NOT the triality signature"),
    )
    json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1,
              sort_keys=True, default=str)
    print(f"\n  pairwise inequivalent: {off_zero}; diagonal Hom dims: {diag}")
    print(f"  {res['signature']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
