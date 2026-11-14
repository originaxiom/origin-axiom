#!/usr/bin/env python3
"""W-F12: the doublets' class index at the odd levels, extended to golden level 7. Data-free; this seat's own code.
The helpers are taken by text from W-C8 part 2a's sealed script (definitions only), which is not re-run.

    python3 -I -u wf12_checks.py

DEFINITIONS (as in part 2a and its post hoc 2)
  The golden tick sigma; level n: G_n = <a, b, t | t a t^-1 = sigma^n(a), t b t^-1 = sigma^n(b)>; odd n non-orientable,
  w(t) = -1. Characters: fibre part on coker(A_n - I) (exponent e), t-value any 2e-th root of unity. Doublets: for
  every character alpha and every extension character l with a non-coboundary class c (a basis of a complement of
  B^1 in Z^1(G; l)), V = [[alpha, c beta], [0, beta]] with beta = alpha / l. The class index I_w(V) = n(V) - n(V* (x) w);
  the h^1 gap h^1(V) - h^1(V* (x) w).

EXPECTATIONS, written before the run:
  C1  Control: at levels 3 and 5 the extension characters with a class number 4 and 11 (the trivial one and those with
      l(mu) = -1); the doublets number 64 and 2,662; I_w = 0 on every doublet; the h^1-gap census is +-1 on 4 + 4 and
      +-2 on 3 + 3 (level 3), +-1 on 11 + 11 and +-2 on 10 + 10 (level 5) (part 2a, post hoc 2, G2 and G3).
  C2  Level 7: h^1(G; l) = [l = 1] for fibre-trivial l and [l(mu) = -1] for fibre-non-trivial l, on all 1,682
      characters (W-F6's law), so 29 extension characters carry a class and the doublets number 48,778.
  C3  Level 7 (prediction by the pattern of levels 1, 3, 5, reported either way): I_w = 0 on every doublet; the h^1-gap
      census +-1 on 29 + 29 and +-2 on 28 + 28.
"""
import os
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = open(os.path.join(HERE, "..", "chat1_2026-11-14_wc8", "wc8_part2a_checks.py")).read()
ns = {}
exec(SRC.split("EXP = {}")[0], ns)
red, inv, sig_pow, abel2, LAM, conjugator = ns["red"], ns["inv"], ns["sig_pow"], ns["abel2"], ns["LAM"], ns["conjugator"]
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


M = 2 * 2 * 11 * 29
p = find_prime(M, 20000)
gen = next(x for x in range(2, p) if all(pow(x, (p - 1) // q, p) != 1 for q in prime_factors(p - 1)))
z = pow(gen, (p - 1) // M, p)
say("prime", p)
ok = dict(C1=True, C2=True, C3=True)
for n in (3, 5, 7):
    f = sig_pow(n)
    A = [[abel2(f[1])[0], abel2(f[2])[0]], [abel2(f[1])[1], abel2(f[2])[1]]]
    tor = abs((A[0][0] - 1) * (A[1][1] - 1) - A[0][1] * A[1][0])
    g1 = gcd(gcd(A[0][0] - 1, A[0][1]), gcd(A[1][0], A[1][1] - 1))
    e = tor // g1
    g, s = conjugator(n)
    mu = red(inv(g) + (3,))
    ga, gb = abel2(g)
    rels = [red((3, 1, -3) + inv(f[1])), red((3, 2, -3) + inv(f[2]))]
    fib = [(a1, a2) for a1 in range(e) for a2 in range(e)
           if (a1 * A[0][0] + a2 * A[1][0] - a1) % e == 0 and (a1 * A[0][1] + a2 * A[1][1] - a2) % e == 0]
    zf, zt = pow(z, M // e, p), pow(z, M // (2 * e), p)
    chars = [(pow(zf, a1, p), pow(zf, a2, p), pow(zt, j, p), (a1, a2)) for (a1, a2) in fib for j in range(2 * e)]
    mone = p - 1
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
        chig = pow(ch[0], ga, p) * pow(ch[1], gb, p) % p
        chimu = pow(chig, p - 2, p) * ch[2] % p
        if ch[3] == (0, 0):
            want = 1 if ch[2] == 1 else 0
        else:
            want = 1 if chimu == mone else 0
        law_bad += len(cl) != want
        for c in cl:
            ext.append((ch, c))
    plus1 = minus1 = plus2 = minus2 = Inz = nd = 0
    for (l, c) in ext:
        for al in chars:
            be = tuple(al[i] * pow(l[i], p - 2, p) % p for i in range(3))
            mats = {gi: [[al[gi - 1], c[gi - 1] * be[gi - 1] % p], [0, be[gi - 1]]] for gi in (1, 2, 3)}
            V = Rep(mats, p)
            dual = {gi: [list(r) for r in zip(*V.inv[gi])] for gi in (1, 2, 3)}
            Vdw = Rep({1: dual[1], 2: dual[2], 3: [[x * mone % p for x in r] for r in dual[3]]}, p)
            hV, hD = cohomology(V, rels, mu, LAM), cohomology(Vdw, rels, mu, LAM)
            gap = hV["h1"] - hD["h1"]
            plus1 += gap == 1
            minus1 += gap == -1
            plus2 += gap == 2
            minus2 += gap == -2
            Inz += hV["n"] != hD["n"]
            nd += 1
    say("level", n, "| characters", len(chars), "| extension characters with a class", len(ext),
        "| law failures", law_bad, "| doublets", nd, "| class index non-zero on", Inz,
        "| h1 gap +1/-1/+2/-2:", plus1, minus1, plus2, minus2)
    T = tor
    if n in (3, 5):
        want = {3: (4, 64, 4, 3), 5: (11, 2662, 11, 10)}[n]
        ok["C1"] &= (len(ext), nd, Inz) == (want[0], want[1], 0) and (plus1, minus1, plus2, minus2) == \
            (want[2], want[2], want[3], want[3])
    else:
        ok["C2"] &= law_bad == 0 and len(ext) == 29 and nd == 48778
        ok["C3"] &= Inz == 0 and (plus1, minus1, plus2, minus2) == (29, 29, 28, 28)
for key in ("C1", "C2", "C3"):
    say(key, "holds:", ok[key])
