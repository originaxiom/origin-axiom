#!/usr/bin/env python3
"""W-F11: does a world of five distinctions carry the frame's matter? Data-free; this seat's own code. The helpers
(free reduction, automorphisms of free groups, Rep with Fox calculus over F_p, ranks, nullspaces) are taken by text
from W-C8 part 2a's sealed script (definitions only), which is not re-run.

    python3 -I -u wf11_checks.py

DEFINITIONS
  W_n = <s_1..s_n | s_i^2>; the records E_n are free on x_i = s_i s_(i+1), i = 1..n-1. Hurwitz moves h_i as in W-F8;
  H_n = h_1 h_2^-1 h_3 h_4^-1 ... (W-F8's history). phi = the automorphism of E_n induced by H_n (an even s-word is
  rewritten in the x_i pair by pair). The scar lambda = p^2 with p = s_1...s_n (odd n: one cusp), as an x-word; H_n keeps
  p, so phi(lambda) = lambda and the cusp group of the mapping torus is <t, lambda>, mu = t.
  Level N: G = <x_1..x_(n-1), t | t x_i t^-1 = phi^N(x_i)>. Fibre torsion: coker(A^N - I), A = phi's abelianisation.
  The record's recipe (B1438) carried over: l a character of the fibre torsion, non-trivial, with l(t) = 1, and a class
  c of H^1(G; l) normalised by c(lambda) = 1 (the first basis class with c(lambda) != 0); modules V(l, alpha) =
  [[alpha, c beta], [0, beta]], beta = alpha / l, for alpha of the same kind with alpha != l. n(W) = the interior
  classes (restriction to <mu, lambda> a coboundary); I(V) = n(V) - n(V*).

EXPECTATIONS, written before the run:
  V1  Control, n = 3, level 2 (H_3 acts as [[2, -1], [-1, 1]], the golden act's class): fibre torsion 5; 4 record
      characters, each with h^1 = 1 and a class with c(lambda) != 0; 12 modules; I = +1 on 4 and -1 on 4 (golden
      level 4 in part 2a and W-F9).
  V2  n = 5: phi(lambda) = lambda exactly; det(A - I) = 1 (level 1 has no fibre torsion, so no record data);
      |det(A^2 - I)| = 29 with cyclic cokernel (exponent 29).
  V3  n = 5, level 2 (prediction by analogy with the once-punctured torus, reported either way): each of the 28 record
      characters carries a class with c(lambda) != 0.
  V4  n = 5, level 2 (prediction, reported either way): some module has I != 0, so the frame's matter exists at five
      distinctions; and the numbers with I = +1 and I = -1 are equal (W-F9's involution).
  Both primes give the same counts.
"""
import os
from itertools import combinations
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = open(os.path.join(HERE, "..", "chat1_2026-11-14_wc8", "wc8_part2a_checks.py")).read()
ns = {}
exec(SRC.split("EXP = {}")[0], ns)
red, inv, apply = ns["red"], ns["inv"], ns["apply"]
Rep, rank_mod, nullspace_mod, find_prime, madd, ident = (ns["Rep"], ns["rank_mod"], ns["nullspace_mod"],
                                                          ns["find_prime"], ns["madd"], ns["ident"])


def say(*a):
    print(*a, flush=True)


def prime_factors(m):
    fs, d = set(), 2
    while d * d <= m:
        while m % d == 0:
            fs.add(d)
            m //= d
        d += 1
    if m > 1:
        fs.add(m)
    return fs


# ---------- W_n, Hurwitz moves, the induced automorphism of the records ----------
def red_s(w):
    out = []
    for g in w:
        if out and out[-1] == g:
            out.pop()
        else:
            out.append(g)
    return tuple(out)


def img_s(f, w):
    out = []
    for g in w:
        out.extend(f[g])
    return red_s(out)


def comp_s(f, g):
    return {k: img_s(f, v) for k, v in g.items()}


def hmove(n, i, inverse=False):
    f = {k: (k,) for k in range(1, n + 1)}
    if not inverse:
        f[i], f[i + 1] = (i + 1,), (i + 1, i, i + 1)
    else:
        f[i], f[i + 1] = (i, i + 1, i), (i,)
    return f


def to_x(w):
    assert len(w) % 2 == 0
    out = []
    for k in range(0, len(w), 2):
        j, l = w[k], w[k + 1]
        out.extend(range(j, l) if j < l else [-i for i in range(j - 1, l - 1, -1)])
    return red(tuple(out))


def setup(n):
    H = {k: (k,) for k in range(1, n + 1)}
    for i in range(1, n):
        H = comp_s(H, hmove(n, i, inverse=(i % 2 == 0)))
    k = n - 1
    phi = {i: to_x(img_s(H, (i, i + 1))) for i in range(1, k + 1)}
    p_ = tuple(range(1, n + 1))
    lam = to_x(red_s(p_ + p_))
    return phi, lam, k


def abel(w, k):
    v = [0] * k
    for g in w:
        v[abs(g) - 1] += 1 if g > 0 else -1
    return v


def det(M):
    if len(M) == 1:
        return M[0][0]
    return sum((-1) ** j * M[0][j] * det([r[:j] + r[j + 1:] for r in M[1:]]) for j in range(len(M)))


def invariants(B):
    k = len(B)
    out, prev = [], 1
    for r in range(1, k + 1):
        g = 0
        for rows in combinations(range(k), r):
            for cols in combinations(range(k), r):
                g = gcd(g, abs(det([[B[i][j] for j in cols] for i in rows])))
        out.append(g // prev)
        prev = g
    return out


def coh(rep, rels, gens, mu, lam):
    p, d = rep.p, rep.d
    G = len(gens)
    F = []
    for r in rels:
        blocks = [rep.fox(r, g) for g in gens]
        for i in range(d):
            F.append([blocks[gi][i][j] for gi in range(G) for j in range(d)])
    rkF = rank_mod(F, p)
    Dm = []
    for g in gens:
        Dm.extend(madd(rep.m[g], ident(d), p, -1))
    rkD = rank_mod(Dm, p)
    h0, h1 = d - rkD, G * d - rkF - rkD
    Z = nullspace_mod(F, p, G * d)
    Cmu, Clam = madd(rep.of(mu), ident(d), p, -1), madd(rep.of(lam), ident(d), p, -1)
    imgs = []
    for zb in Z:
        z = {gens[gi]: zb[gi * d:(gi + 1) * d] for gi in range(G)}
        imgs.append(rep.cocycle_value(z, mu) + rep.cocycle_value(z, lam))
    Pcob = [[Cmu[i][j] for i in range(d)] + [Clam[i][j] for i in range(d)] for j in range(d)]
    rk_all = rank_mod(imgs + Pcob, p) if imgs else rank_mod(Pcob, p)
    rk_P = rank_mod(Pcob, p)
    n_int = len(Z) - (rk_all - rk_P) - rkD
    return dict(h0=h0, h1=h1, n=n_int, Z=Z, rkD=rkD)


def run_case(n, level, p, zM, M):
    phi, lam, k = setup(n)
    assert apply(phi, lam) == lam, "phi keeps the scar"
    T = k + 1
    gens = list(range(1, k + 2))
    f = {i: (i,) for i in range(1, k + 1)}
    for _ in range(level):
        f = {i: apply(phi, w) for i, w in f.items()}
    A = [[abel(f[j], k)[i] for j in range(1, k + 1)] for i in range(k)]
    B = [[A[i][j] - (1 if i == j else 0) for j in range(k)] for i in range(k)]
    inv_ = invariants(B)
    tor = abs(det(B))
    e = inv_[-1]
    rels = [red((T, i, -T) + inv(f[i])) for i in range(1, k + 1)]
    mu = (T,)
    fib = []
    if e > 1:
        def rec(prefix):
            if len(prefix) == k:
                if all(sum(B[i][j] * prefix[i] for i in range(k)) % e == 0 for j in range(k)) and any(prefix):
                    fib.append(tuple(prefix))
                return
            for a in range(e):
                rec(prefix + [a])
        rec([])
    assert len(fib) == max(tor, 1) - 1, (len(fib), tor)

    def vals(v):
        return [pow(zM, (M // e) * a, p) for a in v] + [1]

    def rep_of(vs, d=1, mats=None):
        return Rep(mats if mats else {g: [[vs[g - 1]]] for g in gens}, p)

    rec_chars, h1dist = {}, {}
    for v in fib:
        vs = vals(v)
        r1 = rep_of(vs)
        res = coh(r1, rels, gens, mu, lam)
        h1dist[res["h1"]] = h1dist.get(res["h1"], 0) + 1
        cob = [(x - 1) % p for x in vs]
        base = [cob] if any(cob) else []
        cls = []
        for zb in res["Z"]:
            if rank_mod(base + cls + [zb], p) > len(base) + len(cls):
                cls.append(zb)
        for c in cls:
            lv = r1.cocycle_value({g: [c[g - 1]] for g in gens}, lam)[0] % p
            if lv:
                iv = pow(lv, p - 2, p)
                rec_chars[v] = (vs, [x * iv % p for x in c])
                break
    I = {}
    for vl, (ls, c) in rec_chars.items():
        for va in fib:
            if va == vl:
                continue
            al = vals(va)
            be = [al[i] * pow(ls[i], p - 2, p) % p for i in range(k + 1)]
            V = {g: [[al[g - 1], c[g - 1] * be[g - 1] % p], [0, be[g - 1]]] for g in gens}
            RV = Rep(V, p)
            assert all(RV.of(r) == ident(2) for r in rels)
            Vd = {g: [list(row) for row in zip(*RV.inv[g])] for g in gens}
            nV = coh(RV, rels, gens, mu, lam)["n"]
            nVd = coh(Rep(Vd, p), rels, gens, mu, lam)["n"]
            I[(vl, va)] = nV - nVd
    plus, minus = sum(x == 1 for x in I.values()), sum(x == -1 for x in I.values())
    other = sum(x not in (-1, 0, 1) for x in I.values())
    return dict(tor=tor, inv=inv_, e=e, record=len(rec_chars), h1=h1dist, modules=len(I), plus=plus, minus=minus,
                other=other, nonzero=plus + minus + other)


M = 2 * 5 * 29
res_all = []
for start in (70000, 90000):
    p = find_prime(M, start)
    gen = next(x for x in range(2, p) if all(pow(x, (p - 1) // q, p) != 1 for q in prime_factors(p - 1)))
    zM = pow(gen, (p - 1) // M, p)
    out = {}
    for n, level in ((3, 1), (3, 2), (5, 1), (5, 2)):
        out[(n, level)] = run_case(n, level, p, zM, M)
        say(p, "n =", n, "level", level, out[(n, level)])
    res_all.append(out)
c = res_all[0]
v1 = c[(3, 2)]["tor"] == 5 and c[(3, 2)]["record"] == 4 and c[(3, 2)]["h1"] == {1: 4} and \
    c[(3, 2)]["modules"] == 12 and c[(3, 2)]["plus"] == 4 and c[(3, 2)]["minus"] == 4
phi5, lam5, _ = setup(5)
v2 = apply(phi5, lam5) == lam5 and c[(5, 1)]["tor"] == 1 and c[(5, 2)]["tor"] == 29 and c[(5, 2)]["e"] == 29
v3 = c[(5, 2)]["record"] == 28
v4 = c[(5, 2)]["nonzero"] > 0 and c[(5, 2)]["plus"] == c[(5, 2)]["minus"]
say("the scar at n = 5 as an x-word:", lam5)
say("V1 holds:", v1)
say("V2 holds:", v2)
say("V3 holds:", v3)
say("V4 holds:", v4)
say("both primes give the same counts:", res_all[0] == res_all[1])
