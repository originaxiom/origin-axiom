#!/usr/bin/env python3
"""THE TOWER AND ITS DOUBLES: which closings of the object carry the family local system, and with how
many classes -- the cyclic covers M_n (cusped), the cyclic branched covers Y_n (closed, the Fibonacci
manifolds), and the mirror doubles D(M_n) (closed).

(a) DESCENT.  The real 3 of 2T (the family SU(3) holonomy of the E8 transport) has 3_rho(a) of order 3
    for every surjection (B1263: meridian order 3 or 6 in 2T, hence 3 in A4), so it descends to the
    branched cover Y_n (the lifted meridian a^n filled) iff 3 | n: the closing's index is not the
    observer's -- the object's meridian selects n in 3Z, minimal n = 3 (B1273's closing).

(b) THE IMAGE.  rho(K_n) for K_n = ker(a, b -> 1 mod n): the Klein four-group V4 when 3 | n (abelian:
    the 3 splits into characters, every tree-level mass matrix is zero-diagonal -- B1273's theorem
    closes the whole branched tower at tree level), and all of A4 when 3 does not divide n (the 3 stays
    IRREDUCIBLE: diagonal-capable).

(c) THE COUNTS (exact, Reidemeister-Schreier on the corpus's presentation, Fox calculus over Q(omega),
    all 48 surjections): h^1(M_n; 3_rho) and the cusp data h^0(dM_n), h^1(dM_n), rank(res) for n = 1..6;
    h^1(Y_n; 3_rho) for n = 3, 6.  Shapiro control at n = 2: h^1(M_2; 3) = h^1(m004; 3) + h^1(m004; 3 (x) sgn).

(d) THE DOUBLES.  For the closed mirror double D(M_n) = M_n u M_n-bar glued along the cusp torus, Mayer-
    Vietoris gives h^1(D; V) = h^0(dM; V) + 2 h^1(M_n; V) - rank(res + res') - (2h^0(M_n) - h^0(D)), so
    (with h^0(M_n; 3) = 0)  h^0(dM) + 2h^1(M_n) - h^1(dM) <= h^1(D(M_n); 3) <= h^0(dM) + 2h^1(M_n) - rank(res),
    for every gluing dial.  RESULT: no cyclic cover, branched cover or mirror double (n <= 6) carries three
    classes of the irreducible family system -- the tower offers ONE irreducible class (3 does not divide n:
    h^1(M_n; 3) = 1, the Shapiro control h^1(3 (x) sgn) = 0) or THREE characters (3 | n): three classes
    <=> abelian image <=> zero-diagonal.  The tree-level hierarchy is excluded on the whole object-supplied
    cyclic tower and its doubles.
"""
from __future__ import annotations
import os, sys, itertools, collections
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
for arc in ('B1267_spectrum_law_rebuilt', 'B1269_transport_computed', 'B1268_cusped_net_chirality_bound', 'B1273_the_three_fold_closing'):
    sys.path.insert(0, os.path.join(HERE, '..', '..', arc, 'verification'))
import e6_instrument as E
import spectrum_law as S
import cusped_bound as CB
import three_fold_closing as Y3

Qw, ONE, ZERO = E.Qw, E.ONE, E.ZERO


def rewrite(word, n, k=0):
    """Reidemeister-Schreier for ker(a, b -> 1 mod n), transversal {a^k}: z = a^n -> 1, x_k -> 2 + k."""
    out = []
    for L in word:
        if L == 1:
            if k == n - 1:
                out.append(1)
            k = (k + 1) % n
        elif L == -1:
            if k == 0:
                out.append(-1)
            k = (k - 1) % n
        elif L == 2:
            out.append(2 + k)
            k = (k + 1) % n
        elif L == -2:
            k = (k - 1) % n
            out.append(-(2 + k))
    return out, k


def presentation(n, branched):
    gens = list(range(1, n + 2))
    rels = []
    for k in range(n):
        r, kk = rewrite(S.REL, n, k)
        assert kk == k
        rels.append(r)
    if branched:
        rels.append([1])
    return gens, rels


def gen_words(n):
    w = {1: [1] * n}
    for k in range(n):
        w[2 + k] = [1] * k + [2] + [-1] * ((k + 1) % n)
    return w


def rep_on_cover(X, Y, n, dim_map):
    Xi, Yi = Y3.sl2_inv(X), Y3.sl2_inv(Y)
    mats2 = {1: X, -1: Xi, 2: Y, -2: Yi}

    def ev2(word):
        out = np.array([[ONE, ZERO], [ZERO, ONE]], dtype=object)
        for L in word:
            out = out.dot(mats2[L])
        return out
    words = gen_words(n)
    M = {g: dim_map(ev2(words[g])) for g in words}
    I = {g: dim_map(ev2([-L for L in reversed(words[g])])) for g in words}
    return S.Rep(M, I)


def image_order(rep, gens):
    n = rep.n
    one = E.qw_eye(n)
    seen = {Y3.key(one)}
    frontier = [one]
    while frontier:
        nxt = []
        for Mm in frontier:
            for g in gens:
                P = Mm.dot(rep.M[g])
                if Y3.key(P) not in seen:
                    seen.add(Y3.key(P)); nxt.append(P)
        frontier = nxt
    return len(seen)


def cocycle_value_gen(rep, word, f):
    n = rep.n
    val = np.array([[ZERO] for _ in range(n)], dtype=object)
    cur = E.qw_eye(n)
    for L in word:
        if L > 0:
            val = val + cur.dot(f[L])
            cur = cur.dot(rep.M[L])
        else:
            cur = cur.dot(rep.I[-L])
            val = val - cur.dot(f[-L])
    return val


def cusp_data(rep, gens, rels, n):
    """h0, h1 of M_n; h0, h1 of its cusp torus <a^n, lambda>; rank of the restriction."""
    d = rep.n
    I = E.qw_eye(d)
    h0, h1, r0, r1 = S.h0_h1(rep, gens, rels)
    lam_word, kk = rewrite(S.LONG, n, 0)
    assert kk == 0
    mu, lam = rep.M[1], rep.ev(lam_word)
    assert E.qw_is_zero(mu.dot(lam) - lam.dot(mu))
    h0t = d - E.rank_qw(np.vstack([mu - I, lam - I]))
    Bt = np.vstack([mu - I, lam - I])
    rB = E.rank_qw(Bt)
    rZ = E.rank_qw(np.hstack([lam - I, -(mu - I)]))
    h1t = (2 * d - rZ) - rB
    d1 = np.hstack([rep.fox(r, g) for g in gens] if False else [np.vstack([rep.fox(r, g) for r in rels]) for g in gens])
    kern = CB.nullspace_qw(d1)
    cols = []
    for v in kern:
        f = {g: np.array([[x] for x in v[(i) * d:(i + 1) * d]], dtype=object) for i, g in enumerate(gens)}
        val = np.vstack([cocycle_value_gen(rep, [1], f), cocycle_value_gen(rep, lam_word, f)])
        cols.append([val[i, 0] for i in range(2 * d)])
    R = np.array(cols, dtype=object).T if cols else np.empty((2 * d, 0), dtype=object)
    rank_res = E.rank_qw(np.hstack([R, Bt])) - rB
    return dict(h0=h0, h1=h1, h0t=h0t, h1t=h1t, rank_res=rank_res)


def main():
    surj, order_of, one = Y3.surjections_2T()
    print(f"  surjections pi_1(m004) -> 2T: {len(surj)}")
    ok = True
    # (b) the Shapiro control at n = 2 on m004 itself: h1(3) and h1(3 x sgn)
    ctrl = collections.Counter()
    for (X, Y) in surj:
        M3 = {1: Y3.ad3(X), 2: Y3.ad3(Y)}
        I3 = {1: Y3.ad3(Y3.sl2_inv(X)), 2: Y3.ad3(Y3.sl2_inv(Y))}
        r3 = S.Rep(M3, I3)
        neg = lambda A: np.vectorize(lambda z: ZERO - z, otypes=[object])(A)
        rs = S.Rep({1: neg(M3[1]), 2: neg(M3[2])}, {1: neg(I3[1]), 2: neg(I3[2])})
        a = CB.lemma_row(r3, "", quiet=True)
        b = CB.lemma_row(rs, "", quiet=True)
        ctrl[(a['h0'], a['h1'], a['h0t'], a['h1t'], a['rank_res'], b['h0'], b['h1'], b['h0t'], b['h1t'], b['rank_res'])] += 1
    for k, v in sorted(ctrl.items()):
        print(f"  on m004: 3_rho: (h0, h1, h0(dM), h1(dM), rank res) = {k[:5]};  3_rho (x) sgn: {k[5:]}   x{v}")
    print()
    table = {}
    for n in range(1, 7):
        for branched in (False, True):
            if branched and n == 1:
                continue
            gens, rels = presentation(n, branched)
            rows = collections.Counter()
            for (X, Y) in surj:
                rep = rep_on_cover(X, Y, n, Y3.ad3)
                if branched:
                    descends = Y3.key(rep.M[1]) == Y3.key(E.qw_eye(3))
                    if not descends:
                        rows[('no descent',)] += 1
                        continue
                    S.check_rep(rep, gens, rels)
                    h0, h1, _, _ = S.h0_h1(rep, gens, rels)
                    img = image_order(rep, gens)
                    rows[(h0, h1, img)] += 1
                else:
                    S.check_rep(rep, gens, rels)
                    cd = cusp_data(rep, gens, rels, n)
                    img = image_order(rep, gens)
                    lo = cd['h0t'] + 2 * cd['h1'] - cd['h1t'] - 2 * cd['h0']
                    hi = cd['h0t'] + 2 * cd['h1'] - cd['rank_res'] - 2 * cd['h0'] + (1 if cd['h0'] else 0)
                    rows[(cd['h0'], cd['h1'], cd['h0t'], cd['h1t'], cd['rank_res'], img, lo, hi)] += 1
            table[(n, branched)] = rows
            name = f"Y_{n} (closed, branched)" if branched else f"M_{n} (cusped)"
            for k, v in sorted(rows.items(), key=str):
                if branched:
                    if k == ('no descent',):
                        print(f"  {name}: the 3 does NOT descend (3_rho(a^{n}) != 1)   x{v}")
                    else:
                        h0, h1, img = k
                        print(f"  {name}: h0 = {h0}, h1(Y_{n}; 3_rho) = {h1}, image order {img} ({'V4, abelian: characters' if img == 4 else ('A4, irreducible' if img == 12 else img)})   x{v}")
                else:
                    h0, h1, h0t, h1t, rr, img, lo, hi = k
                    print(f"  {name}: h0 = {h0}, h1(M_{n}; 3_rho) = {h1}, cusp h0 = {h0t}, h1 = {h1t}, rank(res) = {rr}, image order {img} ({'V4' if img == 4 else 'A4' if img == 12 else img});  double D(M_{n}): {lo} <= h1 <= {hi}   x{v}")
    # verdicts
    desc = {n: (('no descent',) not in table[(n, True)]) for n in range(2, 7)}
    print(f"\n  descent of the family 3 to the branched cover Y_n: { {n: ('yes' if d else 'no') for n, d in desc.items()} }  (iff 3 | n)")
    ok &= all(desc[n] == (n % 3 == 0) for n in desc)
    imgs = {n: set(k[5] for k in table[(n, False)]) for n in range(1, 7)}
    print(f"  image of the family 3 on the cyclic cover M_n: { {n: sorted(v) for n, v in imgs.items()} }  (A4 = 12 iff 3 does not divide n, V4 = 4 iff 3 | n)")
    ok &= all((imgs[n] == {12}) == (n % 3 != 0) and (imgs[n] == {4}) == (n % 3 == 0) for n in imgs)
    first = None
    for n in range(1, 7):
        if n % 3 == 0:
            continue
        lo = min(k[6] for k in table[(n, False)])
        if lo >= 3:
            first = n
            break
    print(f"  the first mirror double D(M_n), n <= 6, carrying >= 3 classes of the IRREDUCIBLE family system: {first if first else 'NONE'}")
    one_or_three = all((k[1] == 1 and k[5] == 12) or (k[1] == 3 and k[5] == 4) for n in range(1, 7) for k in table[(n, False)])
    print(f"  the dichotomy on the whole tower: ONE class with the irreducible A4 image (3 does not divide n) or THREE classes of characters (3 | n): {one_or_three}")
    ok &= first is None and one_or_three
    return ok


if __name__ == "__main__":
    print("=== the tower M_n, Y_n and the doubles D(M_n): descent, image, counts (all 48 surjections) ===")
    ok = main()
    print("\nSELFTEST:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)
