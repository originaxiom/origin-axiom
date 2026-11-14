#!/usr/bin/env python3
"""W-F19: the class index at odd levels, a proof and its sealed check. Data-free; this seat's own code. The helpers
are taken by text from W-C8 part 2a's sealed script (definitions only).

    python3 -I -u wf19_checks.py          # the sealed run
    python3 -I -u wf19_checks.py --dev    # golden level 1 only (two doublets, part 2a's), used before the seal

DEFINITIONS
  The metallic tick tau_m: a -> a^m b, b -> a (m = 1 golden, 2 silver, 3 bronze); level n: G = <a, b, t | t x t^-1 =
  tau^n(x)>; odd n non-orientable, w(t) = -1, w = 1 on the fibre. lambda = [a, b]; mu = g^-1 t with
  tau^n(lambda) = g lambda^det g^-1 (g found by cyclic reduction and checked). P = <mu, lambda>.
  Characters (as W-F12): fibre part on coker(A - I) (exponent e), t-value any 2e-th root of unity. A character is
  fibre-trivial (ft) or not (fn); m(chi) = chi(mu). The doublets (as W-F12): for each extension character l with a
  class c (a non-coboundary cocycle) and each character alpha, V = [[alpha, c beta], [0, beta]], beta = alpha / l.
  n(V) = dim ker(H^1(G; V) -> H^1(P; V)); r^1(V) = h^1(G; V) - n(V); I_w(V) = n(V) - n(V* (x) w).

THE PROOF (by hand, written before the run; the note gives it in full)
  Step 1. For any module V of a one-cusped mapping torus, by twisted Poincare-Lefschetz duality, half-lives-half-dies
  on the cusp and Euler characteristic zero for G and P:
      I_w(V) = h^0(P; V* (x) w) + h^0(G; V) - h^0(G; V* (x) w) - r^1(V).
  Step 2. At odd levels (det -1, P a Klein bottle group, w(mu) = -1), over C with characters of finite order:
  W-F6's laws give h^1(G; chi) = [chi = 1] + [fn, m = -1], h^2(G; chi) = [fn, m = -1], restriction to P injective in
  degree 1; on P, h^0 = [m = 1], h^1 = [m = 1] + [m = -1], h^2 = [m = -1]. For a doublet, h^0(G; V) = [alpha = 1],
  h^0(G; V* (x) w) = [beta = w], h^0(P; V* (x) w) = [m(beta) = -1]. The extension character l is 1 or fn with
  m(l) = -1. Where a cup product is needed (l = 1 with alpha fn, m = -1; and beta = 1), it is non-zero because its
  restriction to P is the twisted Poincare duality pairing of the Klein bottle. Case by case (snake lemma on the
  restriction), r^1(V) = [m(beta) = -1] + [alpha = 1] - [beta = w], so I_w(V) = 0.
  The cases give (n(V), h^1(G; V)):
    l = 1, alpha = beta = chi:  chi = 1: (0, 1); chi = w: (0, 0); chi fn, m = -1: (0, 1); otherwise (0, 0).
    l fn, m(l) = -1:  beta = 1: (0, 0); beta = w: (0, 0);
                      beta fn, m = -1: alpha = 1: (0, 2), otherwise (0, 1);
                      beta fn, m = +1: alpha = w: (0, 0), otherwise (1, 1);
                      m(beta) not +-1: (0, 0).

EXPECTATIONS, written before the run:
  E0  W-F6's law on every character: h^1(G; chi) = [chi = 1] for ft, [m = -1] for fn (odd levels).
  E1  Step 1's formula holds term by term on every doublet at every odd level below, and on every record module at
      golden level 4 (even, w = 1; there I = +-1 on 4 + 4).
  E2  I_w(V) = 0 on every doublet at golden levels 1, 3, 5 (W-F12's, reproduced) and at the new levels bronze 1 and 3,
      silver 1 and 3 (blind).
  E3  (n(V), h^1(G; V)) is the case table's on every doublet; so n(V) = 1 on exactly (|T| - 1)(|T| - 2) doublets:
      golden 1, 3, 5: 0, 6, 90; bronze 1, 3: 2, 1,190; silver 1, 3: 0, 156.
  E4  The h^1 gap h^1(V) - h^1(V* (x) w) is +1 on |T|, -1 on |T|, +2 on |T| - 1, -2 on |T| - 1 doublets and 0 on the
      rest; |T| = 1, 4, 11 (golden), 3, 36 (bronze), 2, 14 (silver).
  Plant: the formula with h^0(P; V*) in place of h^0(P; V* (x) w) fails on some doublet at some odd level.
"""
import os
import sys
import time
from math import gcd

DEV = "--dev" in sys.argv
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = open(os.path.join(HERE, "..", "chat1_2026-11-14_wc8", "wc8_part2a_checks.py")).read()
ns = {}
exec(SRC.split("EXP = {}")[0], ns)
red, inv, apply, abel2, LAM = ns["red"], ns["inv"], ns["apply"], ns["abel2"], ns["LAM"]
Rep, cohomology, nullspace_mod, rank_mod, find_prime = (ns["Rep"], ns["cohomology"], ns["nullspace_mod"],
                                                        ns["rank_mod"], ns["find_prime"])


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


def tick_pow(m, n):
    T, f = {1: tuple([1] * m + [2]), 2: (1,)}, {1: (1,), 2: (2,)}
    for _ in range(n):
        f = {k: apply(T, v) for k, v in f.items()}
    return f


def cyc_reduce(wd):
    wd, u = list(wd), []
    while len(wd) >= 2 and wd[0] == -wd[-1]:
        u.append(wd[0])
        wd = wd[1:-1]
    return tuple(u), tuple(wd)


def find_conjugator(f, det):
    target = apply(f, LAM)
    u, c = cyc_reduce(target)
    base = LAM if det == 1 else inv(LAM)
    for k in range(len(base)):
        if base[k:] + base[:k] == c:
            g = red(u + inv(base[:k]))
            if red(g + base + inv(g)) == target:
                return g
    raise RuntimeError("no conjugator")


def setup(m, n):
    f = tick_pow(m, n)
    A = [[abel2(f[1])[0], abel2(f[2])[0]], [abel2(f[1])[1], abel2(f[2])[1]]]
    det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    tor = abs((A[0][0] - 1) * (A[1][1] - 1) - A[0][1] * A[1][0])
    g1 = gcd(gcd(A[0][0] - 1, A[0][1]), gcd(A[1][0], A[1][1] - 1))
    e = tor // g1
    g = find_conjugator(f, det)
    mu = red(inv(g) + (3,))
    rels = [red((3, 1, -3) + inv(f[1])), red((3, 2, -3) + inv(f[2]))]
    fib = [(a1, a2) for a1 in range(e) for a2 in range(e)
           if (a1 * A[0][0] + a2 * A[1][0] - a1) % e == 0 and (a1 * A[0][1] + a2 * A[1][1] - a2) % e == 0]
    return dict(f=f, A=A, det=det, tor=tor, e=e, g=g, mu=mu, rels=rels, fib=fib)


def odd_level(name, m, n, p, z, M, plant_hits):
    S = setup(m, n)
    e, rels, mu, (ga, gb) = S["e"], S["rels"], S["mu"], abel2(S["g"])
    mone = p - 1
    zf, zt = pow(z, M // e, p), pow(z, M // (2 * e), p)
    chars = [(pow(zf, a1, p), pow(zf, a2, p), pow(zt, j, p), (a1, a2)) for (a1, a2) in S["fib"] for j in range(2 * e)]

    def mval(ch):
        chig = pow(ch[0], ga, p) * pow(ch[1], gb, p) % p
        return pow(chig, p - 2, p) * ch[2] % p

    def kind(ch):
        ft = ch[3] == (0, 0)
        mv = mval(ch)
        if ft and ch[2] == 1:
            return "one"
        if ft and ch[2] == mone:
            return "w"
        if mv == 1:
            return "fn+" if not ft else "ft+"
        if mv == mone:
            return "fn-" if not ft else "ft-"
        return "other"
    ext, law_bad = [], 0
    for ch in chars:
        r1 = Rep({1: [[ch[0]]], 2: [[ch[1]]], 3: [[ch[2]]]}, p)
        F = [[r1.fox(r, gi)[0][0] for gi in (1, 2, 3)] for r in rels]
        Z = nullspace_mod(F, p, 3)
        cob = [(ch[i] - 1) % p for i in range(3)]
        base = [cob] if any(cob) else []
        cl = []
        for zz in Z:
            if rank_mod(base + cl + [zz], p) > len(base) + len(cl):
                cl.append(zz)
        want = (1 if ch[2] == 1 else 0) if ch[3] == (0, 0) else (1 if mval(ch) == mone else 0)
        law_bad += len(cl) != want
        for c in cl:
            ext.append((ch, c))
    T = S["tor"]
    nd = Inz = form_bad = table_bad = n1 = 0
    gaps = {}
    for (l, c) in ext:
        kl = kind(l)
        for al in chars:
            be = tuple(al[i] * pow(l[i], p - 2, p) % p for i in range(3)) + \
                (tuple((al[3][i] - l[3][i]) % e for i in range(2)),)
            mats = {gi: [[al[gi - 1], c[gi - 1] * be[gi - 1] % p], [0, be[gi - 1]]] for gi in (1, 2, 3)}
            V = Rep(mats, p)
            dual = {gi: [list(r) for r in zip(*V.inv[gi])] for gi in (1, 2, 3)}
            Vdw = Rep({1: dual[1], 2: dual[2], 3: [[x * mone % p for x in r] for r in dual[3]]}, p)
            Vd = Rep(dual, p)
            cV, cD = cohomology(V, rels, mu, LAM), cohomology(Vdw, rels, mu, LAM)
            I = cV["n"] - cD["n"]
            r1 = cV["h1"] - cV["n"]
            form_bad += I != cD["h0P"] + cV["h0"] - cD["h0"] - r1
            if plant_hits is not None:
                hP = cohomology(Vd, rels, mu, LAM)["h0P"]
                plant_hits[0] += I != hP + cV["h0"] - cD["h0"] - r1
            Inz += I != 0
            gap = cV["h1"] - cD["h1"]
            gaps[gap] = gaps.get(gap, 0) + 1
            n1 += cV["n"] == 1
            ka, kb = kind(al), kind(be)
            if kl == "one":
                pred = {"one": (0, 1), "fn-": (0, 1)}.get(ka, (0, 0))
            else:
                if kb in ("one", "w"):
                    pred = (0, 0)
                elif kb == "fn-":
                    pred = (0, 2) if ka == "one" else (0, 1)
                elif kb == "fn+":
                    pred = (0, 0) if ka == "w" else (1, 1)
                else:
                    pred = (0, 0)
            table_bad += (cV["n"], cV["h1"]) != pred
            nd += 1
    want_gaps = {k: v for k, v in {1: T, -1: T, 2: T - 1, -2: T - 1}.items() if v}
    rest = nd - sum(want_gaps.values())
    if rest:
        want_gaps[0] = rest
    res = dict(level=(name, n), T=T, e=e, chars=len(chars), ext=len(ext), law_bad=law_bad, doublets=nd,
               I_nonzero=Inz, formula_failures=form_bad, table_failures=table_bad, n_equals_1=n1,
               n1_predicted=(T - 1) * (T - 2), gaps=dict(sorted(gaps.items())), gaps_predicted=dict(sorted(want_gaps.items())))
    return res


def even_control(p):
    """golden level 4: the formula with w = 1 on every record module (W-F9's construction)."""
    S = setup(1, 4)
    e, rels, mu, (ga, gb) = S["e"], S["rels"], S["mu"], abel2(S["g"])
    gen = next(x for x in range(2, p) if all(pow(x, (p - 1) // q, p) != 1 for q in prime_factors(p - 1)))
    zz = pow(gen, (p - 1) // e, p)
    chars = [(pow(zz, a1, p), pow(zz, a2, p), pow(zz, (a1 * ga + a2 * gb) % e, p)) for (a1, a2) in S["fib"]
             if (a1, a2) != (0, 0)]
    cls = {}
    for ch in chars:
        r1 = Rep({1: [[ch[0]]], 2: [[ch[1]]], 3: [[ch[2]]]}, p)
        F = [[r1.fox(r, gi)[0][0] for gi in (1, 2, 3)] for r in rels]
        cls[ch] = None
        for zb in nullspace_mod(F, p, 3):
            lv = r1.cocycle_value({1: [zb[0]], 2: [zb[1]], 3: [zb[2]]}, LAM)[0] % p
            if lv:
                iv = pow(lv, p - 2, p)
                cls[ch] = [x * iv % p for x in zb]
                break
    nmod = bad = 0
    hist = {}
    for l in chars:
        c = cls[l]
        if c is None:
            continue
        for al in chars:
            if al == l:
                continue
            be = [al[i] * pow(l[i], p - 2, p) % p for i in range(3)]
            V = Rep({gi: [[al[gi - 1], c[gi - 1] * be[gi - 1] % p], [0, be[gi - 1]]] for gi in (1, 2, 3)}, p)
            D = Rep({gi: [list(row) for row in zip(*V.inv[gi])] for gi in (1, 2, 3)}, p)
            cV, cD = cohomology(V, rels, mu, LAM), cohomology(D, rels, mu, LAM)
            I = cV["n"] - cD["n"]
            bad += I != cD["h0P"] + cV["h0"] - cD["h0"] - (cV["h1"] - cV["n"])
            hist[I] = hist.get(I, 0) + 1
            nmod += 1
    return dict(modules=nmod, formula_failures=bad, hist=dict(sorted(hist.items())))


if __name__ == "__main__":
    t0 = time.time()
    LEVELS = [("golden", 1, 1)] if DEV else [("golden", 1, 1), ("golden", 1, 3), ("golden", 1, 5), ("silver", 2, 1),
                                              ("silver", 2, 3), ("bronze", 3, 1), ("bronze", 3, 3)]
    es = []
    for name, m, n in LEVELS:
        S = setup(m, n)
        es.append(S["e"])
        say(name, "level", n, "| det", S["det"], "| |T|", S["tor"], "| exponent", S["e"], "| conjugator checked")
    M = 1
    for e in es:
        M = M * (2 * e) // gcd(M, 2 * e)
    p = find_prime(M, 20000)
    gen = next(x for x in range(2, p) if all(pow(x, (p - 1) // q, p) != 1 for q in prime_factors(p - 1)))
    z = pow(gen, (p - 1) // M, p)
    say("prime", p)
    ok = dict(E0=True, E1=True, E2=True, E3=True, E4=True)
    plant = [0]
    for name, m, n in LEVELS:
        r = odd_level(name, m, n, p, z, M, plant if (name, n) in (("golden", 3), ("silver", 1), ("bronze", 1)) else None)
        say(r, "|", round(time.time() - t0, 1), "s")
        ok["E0"] &= r["law_bad"] == 0
        ok["E1"] &= r["formula_failures"] == 0
        ok["E2"] &= r["I_nonzero"] == 0
        ok["E3"] &= r["table_failures"] == 0 and r["n_equals_1"] == r["n1_predicted"]
        ok["E4"] &= r["gaps"] == r["gaps_predicted"]
    if not DEV:
        ctl = even_control(find_prime(20, 3000))
        say("golden level 4 (even, w = 1), record modules:", ctl)
        ok["E1"] &= ctl["formula_failures"] == 0 and ctl["modules"] == 12 and ctl["hist"] == {-1: 4, 0: 4, 1: 4}
        say("plant (h^0(P; V*) in place of h^0(P; V* (x) w)): formula failures", plant[0], "| fires:", plant[0] > 0)
    say("holds:", ok, "| total seconds", round(time.time() - t0, 1))
