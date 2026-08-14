#!/usr/bin/env python3
"""B872 -- the coset leg of the charge-measurement theorem: 32 = 16 + 16bar, both legs.

B866 verified the three distinguished charge lines and (addendum) the TYPE of the enhanced
centralizer: so(10)+u(1), on this seat's own build. What remained THEIRS was the coset:
that the 32-dim complement of the centralizer in e6 is the spinor pair 16 + 16bar. This
arc verifies it on two independent legs:

LEG A (exact, over Z) -- root combinatorics of the REGULAR so(10)+u(1) in E6: delete an
end node of the long arm; the 40 vanishing-coefficient roots form D5 (diagram verified);
the 32 complement roots carry u(1)-charge = the deleted-node coefficient, EXACTLY +-1,
16 each; each 16 is a SINGLE Weyl(D5) orbit through a FORK-NODE fundamental weight (the
spinor); the two charges land on the TWO fork nodes (16 vs 16bar).

LEG B (numeric at 40 digits, at ALL THREE Galois roots of the banked cubic) -- on the
actual enhancement points of the (8,16)-pencil, using B854's exact build: kernel dim 46,
center dim 1 (z), the complement W = im(ad s) splits under ad(z) into two 16-dim
eigenspaces of opposite charge; each is ABSOLUTELY IRREDUCIBLE under the centralizer
(commutant dim 1 -- generic-vector cyclicity would NOT prove irreducibility, the
commutant does); Killing-isotropic (B(W+,W+) = 0) with B(W+,W-) nondegenerate, so
W- is W+'s dual: 16bar. All integer verdicts must agree across the three roots.

Mathematics scope; nothing to CLAIMS.md; Gate 5 untouched.
"""
import json
import os
import random
from fractions import Fraction as Fr
from itertools import product

import mpmath
from mpmath import mp

HERE = os.path.dirname(os.path.abspath(__file__))
B854 = os.path.normpath(os.path.join(HERE, "..", "B854_centralizer_exact",
                                     "e6_centralizer.py"))

# ============================================================ LEG A: exact over Z
CART = [[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0],
        [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]]


def leg_a():
    def ip(a, b):
        return sum(a[i] * b[j] * CART[i][j] for i in range(6) for j in range(6))
    pos = [t for t in product(range(4), repeat=6) if any(t) and ip(t, t) == 2]
    roots = pos + [tuple(-x for x in t) for t in pos]
    assert len(roots) == 72

    DEL = 0                                  # end of the long arm: 0-2-3(-1)-4-5
    sub = [i for i in range(6) if i != DEL]  # candidate D5 nodes
    subC = [[CART[i][j] for j in sub] for i in sub]
    degrees = sorted(sum(1 for j in range(5) if i != j and subC[i][j] != 0)
                     for i in range(5))
    d5_diagram = (degrees == [1, 1, 1, 2, 3])   # D5: three ends, one chain, one fork

    d5 = [r for r in roots if r[DEL] == 0]
    plus = [r for r in roots if r[DEL] == 1]
    minus = [r for r in roots if r[DEL] == -1]
    charges_only_pm1 = (len(d5) + len(plus) + len(minus) == 72)

    def d5_weight(r):
        # Dynkin labels of the restriction: <r, alpha_i^vee> for the D5 simples
        return tuple(sum(r[j] * CART[i][j] for j in range(6)) for i in sub)

    def orbit(w0):
        seen, stack = {w0}, [w0]
        while stack:
            w = stack.pop()
            for i in range(5):
                s = list(w)
                li = w[i]
                for j in range(5):
                    s[j] -= li * subC[j][i]
                s = tuple(s)
                if s not in seen:
                    seen.add(s)
                    stack.append(s)
        return seen

    wplus = [d5_weight(r) for r in plus]
    wminus = [d5_weight(r) for r in minus]
    orb_p = orbit(wplus[0])
    orb_m = orbit(wminus[0])
    single_orbit_p = set(wplus) == orb_p and len(wplus) == len(set(wplus)) == 16
    single_orbit_m = set(wminus) == orb_m and len(wminus) == len(set(wminus)) == 16

    # fork nodes of the D5 diagram (indices within `sub`): the two degree-1 nodes
    # adjacent to the degree-3 node
    deg = [sum(1 for j in range(5) if i != j and subC[i][j] != 0) for i in range(5)]
    center = deg.index(3)
    forks = [i for i in range(5)
             if deg[i] == 1 and subC[i][center] != 0]
    fund = {i: tuple(1 if j == i else 0 for j in range(5)) for i in forks}
    hw_p = [i for i in forks if fund[i] in set(wplus)]
    hw_m = [i for i in forks if fund[i] in set(wminus)]
    spinor_split = (len(forks) == 2 and len(hw_p) == 1 and len(hw_m) == 1
                    and hw_p != hw_m)

    return dict(d5_count=len(d5), plus_count=len(plus), minus_count=len(minus),
                d5_diagram=d5_diagram, charges_only_pm1=charges_only_pm1,
                single_orbit_plus=single_orbit_p, single_orbit_minus=single_orbit_m,
                spinor_fundamental_split=spinor_split,
                fork_nodes=[sub[i] for i in forks],
                ok=all([d5_diagram, charges_only_pm1, len(d5) == 40,
                        single_orbit_p, single_orbit_m, spinor_split]))


# ============================================================ LEG B: the real points
CUBIC = [500716339200, -159667200, -28224, 1]     # leading .. constant (B866, banked)


def load_b854():
    src = open(B854, encoding="utf-8").read()
    g = {"__file__": B854, "__name__": "b854"}
    exec(compile(src, B854, "exec"), g)
    return g


def leg_b():
    mp.dps = 40
    g = load_b854()
    DIM, N = g["DIM"], g["N"]
    br, hvec, evec, ROOTS = g["br"], g["hvec"], g["evec"], g["ROOTS"]

    # exact structure triples: [b_p, b_q] = sum_r T[(p,q,r)] b_r
    basis = [hvec(i) for i in range(N)] + [evec(r) for r in ROOTS]
    triples = {}
    for p in range(DIM):
        for q in range(DIM):
            v = br(basis[p], basis[q])
            for r, c in enumerate(v):
                if c:
                    triples.setdefault(p, []).append((q, r, c))
    # exact Killing form B_ab = sum_{(q,r)} T[a,q,r] T[b,r,q]
    tdict = {}
    for a, lst in triples.items():
        for q, r, c in lst:
            tdict[(a, q, r)] = c
    KILL = [[Fr(0)] * DIM for _ in range(DIM)]
    for a in range(DIM):
        for q, r, c in triples.get(a, []):
            for b in range(DIM):
                c2 = tdict.get((b, r, q))
                if c2:
                    KILL[a][b] += c * c2
    KILLm = mp.matrix([[mp.mpf(x.numerator) / mp.mpf(x.denominator) for x in row]
                       for row in KILL])

    def admat_num(vec):
        A = mp.zeros(DIM, DIM)
        for p in range(DIM):
            vp = vec[p]
            if abs(vp) < mp.mpf(10) ** (-mp.dps + 8):
                continue
            for q, r, c in triples.get(p, []):
                A[r, q] += vp * mp.mpf(c.numerator) / mp.mpf(c.denominator)
        return A

    A8 = admat_num([mp.mpf(c.numerator) / mp.mpf(c.denominator) for c in g["INV"][8]])
    A16 = admat_num([mp.mpf(c.numerator) / mp.mpf(c.denominator) for c in g["INV"][16]])

    # NORMALIZATION (established mod p, cubic_modp_check.py): today's deterministic
    # B854 build carries the SOLO seat's rho-normalization -- the pencil's enhancement
    # cubic equals banked(t/13) up to a unit, so the enhancement points sit at
    # t = 13 * (banked roots). This is also a third independent re-derivation of the
    # B866 cubic (F_p Lagrange radical), on top of the two banked builds.
    roots_t = mpmath.polyroots([mp.mpf(c) for c in CUBIC], maxsteps=200,
                               extraprec=120)
    roots_t = sorted(13 * mp.re(r) for r in roots_t)

    out = []
    for t in roots_t:
        A = A8 + t * A16
        U, S, Vt = mpmath.svd_r(A)
        svals = [S[i] for i in range(DIM)]
        kdim = sum(1 for s in svals if s < mp.mpf("1e-20"))
        gap = svals[DIM - kdim - 1] / max(svals[DIM - kdim], mp.mpf("1e-99")) \
            if kdim else mp.mpf(0)
        # kernel basis: rows of Vt with tiny sigma; image basis: cols of U, big sigma
        kern = [[Vt[i, j] for j in range(DIM)] for i in range(DIM - kdim, DIM)]
        img = [[U[j, i] for j in range(DIM)] for i in range(DIM - kdim)]

        # center of c: z = sum u_i kern_i with [z, kern_j] = 0 for all j
        adk = [admat_num(k) for k in kern]
        Mrows = []
        for j, kj in enumerate(kern):
            kjv = mp.matrix(kj)
            cols = [adk[i] * kjv for i in range(kdim)]
            for r in range(DIM):
                Mrows.append([cols[i][r] for i in range(kdim)])
        M = mp.matrix(Mrows)
        Um, Sm, Vmt = mpmath.svd_r(M)
        cdim = sum(1 for i in range(kdim) if Sm[i] < mp.mpf("1e-18"))
        zcoef = [Vmt[kdim - 1, i] for i in range(kdim)]
        z = [sum(zcoef[i] * kern[i][p] for i in range(kdim)) for p in range(DIM)]
        Az = admat_num(z)

        # restrict ad(z) to W = im(ad s)
        Uimg = mp.matrix(img).T          # DIM x 32
        Mw = Uimg.T * (Az * Uimg)        # 32 x 32
        wdim = DIM - kdim
        q2 = sum(sum(Mw[i, k] * Mw[k, i] for k in range(wdim))
                 for i in range(wdim)) / wdim
        # SIGNED q2: the charge operator generates a COMPACT u(1), so the spectrum
        # on W is +-i*omega (q2 < 0) -- the split lives over C.
        lam = mp.sqrt(mp.mpc(q2))
        res_sq = mp.mnorm(Mw * Mw - q2 * mp.eye(wdim), 1) / max(
            mp.mnorm(Mw * Mw, 1), mp.mpf("1e-99"))

        def null_dim_and_basis(Mat):
            Ue, Se, Ve = mpmath.svd_c(Mat)
            smax = max(Se[i] for i in range(wdim))
            tol = smax * mp.mpf("1e-25")
            nd = sum(1 for i in range(wdim) if Se[i] < tol)
            nb = [[mp.conj(Ve[i, j]) for j in range(wdim)]
                  for i in range(wdim - nd, wdim)]
            return nd, nb
        Mc = mp.matrix(wdim, wdim)
        for i in range(wdim):
            for j in range(wdim):
                Mc[i, j] = mp.mpc(Mw[i, j])
        dp, bp = null_dim_and_basis(Mc - lam * mp.eye(wdim))
        dm, bm = null_dim_and_basis(Mc + lam * mp.eye(wdim))

        def ctrans(A):
            B = A.T
            for i in range(B.rows):
                for j in range(B.cols):
                    B[i, j] = mp.conj(B[i, j])
            return B

        # commutant of the c-action on W+ (and W-): dim 1 <=> absolutely irreducible
        # (generic-vector cyclicity would NOT prove irreducibility; the commutant does).
        # Method: ker of TWO random combinations (generic pair), then a full
        # CERTIFICATE against all 46 generators -- candidate >= true always holds;
        # the certificate shows candidate <= true, hence equality. Fast AND rigorous.
        def commutant_dim(bhalf, dhalf):
            P = mp.matrix(bhalf).T                       # 32 x 16, cols orthonormal
            PH = ctrans(P)
            reps = []
            for i in range(kdim):
                R = PH * (Uimg.T * (adk[i] * (Uimg * P)))   # 16 x 16
                reps.append(R)
            rng = random.Random(7)

            def comb():
                return sum((mp.mpf(rng.uniform(-1, 1)) * R for R in reps),
                           mp.zeros(dhalf, dhalf))

            def admap_matrix(L, basis_mats):
                cols = []
                for X in basis_mats:
                    C = L * X - X * L
                    cols.append([C[a, b] for a in range(dhalf) for b in range(dhalf)])
                return mp.matrix(cols).T
            E = [mp.matrix([[mp.mpc(1) if (a, b) == (i, j) else mp.mpc(0)
                             for b in range(dhalf)] for a in range(dhalf)])
                 for i in range(dhalf) for j in range(dhalf)]
            M1 = admap_matrix(comb(), E)                 # 256 x 256
            U1, S1, V1 = mpmath.svd_c(M1)
            sm1 = max(S1[i] for i in range(dhalf * dhalf))
            n1 = sum(1 for i in range(dhalf * dhalf) if S1[i] < sm1 * mp.mpf("1e-20"))
            NB = []
            for i in range(dhalf * dhalf - n1, dhalf * dhalf):
                v = [mp.conj(V1[i, j]) for j in range(dhalf * dhalf)]
                NB.append(mp.matrix([[v[a * dhalf + b] for b in range(dhalf)]
                                     for a in range(dhalf)]))
            M2 = admap_matrix(comb(), NB)                # 256 x n1
            U2, S2, V2 = mpmath.svd_c(M2)
            sm2 = max(S2[i] for i in range(min(M2.rows, M2.cols)))
            n2 = sum(1 for i in range(min(M2.rows, M2.cols))
                     if S2[i] < sm2 * mp.mpf("1e-18"))
            cand = []
            for i in range(n1 - n2, n1):
                X = mp.zeros(dhalf, dhalf)
                for j in range(n1):
                    X += mp.conj(V2[i, j]) * NB[j]
                cand.append(X)
            # certificate: every candidate commutes with ALL 46 generators
            cert = mp.mpf(0)
            for X in cand:
                nX = mp.mnorm(X, 1)
                for R in reps:
                    cert = max(cert, mp.mnorm(R * X - X * R, 1)
                               / max(nX * mp.mnorm(R, 1), mp.mpf("1e-99")))
            return n2, mp.nstr(cert, 3)
        cdp, certp = commutant_dim(bp, dp) if dp == 16 else (-1, "n/a")
        cdm, certm = commutant_dim(bm, dm) if dm == 16 else (-1, "n/a")

        # Killing isotropy (complex-BILINEAR: plain transpose, no conjugation):
        # B(W+, W+) = 0, B(W+, W-) nondegenerate  =>  W- = (W+)^* : the 16bar
        Pp = mp.matrix(bp).T; Pm = mp.matrix(bm).T
        Wp = Uimg * Pp; Wm = Uimg * Pm
        Bpp = Wp.T * (KILLm * Wp)
        Bpm = Wp.T * (KILLm * Wm)
        iso = mp.mnorm(Bpp, 1) / max(mp.mnorm(Bpm, 1), mp.mpf("1e-99"))
        Ub, Sb, Vb = mpmath.svd_c(Bpm)
        sbmax = max(Sb[i] for i in range(min(dp, dm)))
        bpm_rank = sum(1 for i in range(min(dp, dm))
                       if Sb[i] > sbmax * mp.mpf("1e-20"))

        out.append(dict(
            t=mp.nstr(t, 25), kernel_dim=kdim, center_dim=cdim,
            svd_gap_orders=float(mp.log10(gap)) if gap else None,
            q2_sign=(-1 if q2 < 0 else 1), q=mp.nstr(lam, 20),
            adz_sq_residual=mp.nstr(res_sq, 3),
            plus_dim=dp, minus_dim=dm,
            commutant_plus=cdp, commutant_minus=cdm,
            commutant_certificates=[certp, certm],
            isotropy_norm=mp.nstr(iso, 3), Bpm_rank=bpm_rank,
            verdict_16_16bar=(kdim == 46 and cdim == 1 and dp == 16 and dm == 16
                              and cdp == 1 and cdm == 1 and bpm_rank == 16)))
    return out


def main():
    random.seed(2)
    a = leg_a()
    b = leg_b()
    res = dict(leg_a=a, leg_b=b,
               galois_consistent=len({json.dumps(
                   {k: r[k] for k in ("kernel_dim", "center_dim", "plus_dim",
                                      "minus_dim", "commutant_plus",
                                      "commutant_minus", "Bpm_rank")},
                   sort_keys=True) for r in b}) == 1,
               coset_is_16_16bar=(a["ok"] and all(r["verdict_16_16bar"]
                                                  for r in b)))
    json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1,
              sort_keys=True)

    print("=" * 74)
    print("B872 -- the coset leg: 32 = 16 + 16bar")
    print("=" * 74)
    print(f"\n  LEG A (exact/Z): D5 roots {a['d5_count']}, charges +1/-1: "
          f"{a['plus_count']}/{a['minus_count']}, diagram D5 {a['d5_diagram']}")
    print(f"    single Weyl orbits: {a['single_orbit_plus']}/{a['single_orbit_minus']}"
          f"   spinor fundamental split across fork nodes {a['fork_nodes']}: "
          f"{a['spinor_fundamental_split']}")
    print(f"    LEG A ok: {a['ok']}")
    for r in b:
        print(f"\n  LEG B at t = {r['t'][:14]}...: kern {r['kernel_dim']} "
              f"center {r['center_dim']} split {r['plus_dim']}/{r['minus_dim']} "
              f"commutant {r['commutant_plus']}/{r['commutant_minus']} "
              f"B(W+,W-) rank {r['Bpm_rank']}")
        print(f"    gap 10^{r['svd_gap_orders']:.0f}, |ad(z)^2 - q^2|={r['adz_sq_residual']}, "
              f"isotropy {r['isotropy_norm']}  -> 16+16bar: {r['verdict_16_16bar']}")
    print(f"\n  Galois-consistent across the three roots : {res['galois_consistent']}")
    print(f"  COSET = 16 + 16bar (both legs)           : {res['coset_is_16_16bar']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
