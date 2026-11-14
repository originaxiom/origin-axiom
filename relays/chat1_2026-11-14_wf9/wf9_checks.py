#!/usr/bin/env python3
"""W-F9: the order at the scar. Data-free; this seat's own code. The helpers (free group, Fox calculus over F_p, the
cohomology routine) are taken by text from W-C8 part 2a's sealed script (definitions only), which is not re-run.

    python3 -I -u wf9_checks.py

DEFINITIONS
  The metallic tick tau_m (m = 1 golden, m = 3 bronze); level n: G = <a, b, t | t a t^-1 = tau^n(a), t b t^-1 =
  tau^n(b)>, orientable for even n. lambda = [a, b], mu = g^-1 t (g_1 = a^m, g_(k+1) = tau(g_k) a^m).
  The record's data (B1438): fibre-torsion characters chi (non-trivial on the fibre, chi(mu) = 1). The record module
  V(l, alpha) = [[alpha, c beta], [0, beta]], beta = alpha / l, c the class of H^1(G; l) with c(lambda) = 1, for l and
  alpha fibre-torsion with alpha != l (so beta != 1). V* is the dual (inverse transpose). n(W) = the interior classes
  (main's B1297), I(V) = n(V) - n(V*). Levels: golden 4, 6, 8; bronze 2.

EXPECTATIONS, written before the run (by hand):
  O1  For every record module, (h^0, h^1, n) of V* equals that of V(l, l alpha^-1): duality maps the record set to
      itself, alpha -> l alpha^-1 at fixed l (an involution). Modules: golden 12, 210, 1,892; bronze 56.
  O2  I(V(l, l alpha^-1)) = -I(V(l, alpha)) for every module; the numbers with I = +1 and I = -1 are equal at every
      level: golden 4 and 4, 36 and 36, 244 and 244; bronze 8 and 8 (part 2a, part 5).
  Plant: the wrong partner V(l, alpha^-1) in place of V(l, l alpha^-1) fails O1 for some module at every level.
"""
import os
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = open(os.path.join(HERE, "..", "chat1_2026-11-14_wc8", "wc8_part2a_checks.py")).read()
ns = {}
exec(SRC.split("EXP = {}")[0], ns)
red, inv, apply, abel2, LAM = ns["red"], ns["inv"], ns["apply"], ns["abel2"], ns["LAM"]
Rep, cohomology, nullspace_mod, find_prime = ns["Rep"], ns["cohomology"], ns["nullspace_mod"], ns["find_prime"]


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


def tick(m):
    return {1: tuple([1] * m + [2]), 2: (1,)}


def tick_pow(m, n):
    T, f = tick(m), {1: (1,), 2: (2,)}
    for _ in range(n):
        f = {k: apply(T, v) for k, v in f.items()}
    return f


def conj_m(m, n):
    T, g, s = tick(m), tuple([1] * m), -1
    for _ in range(n - 1):
        g, s = red(apply(T, g) + tuple([1] * m)), -s
    return g, s


LEVELS = [("golden", 1, 4), ("golden", 1, 6), ("golden", 1, 8), ("bronze", 3, 2)]
data = []
Mtot = 1
for name, m, n in LEVELS:
    f = tick_pow(m, n)
    A = [[abel2(f[1])[0], abel2(f[2])[0]], [abel2(f[1])[1], abel2(f[2])[1]]]
    tor = abs((A[0][0] - 1) * (A[1][1] - 1) - A[0][1] * A[1][0])
    g1 = gcd(gcd(A[0][0] - 1, A[0][1]), gcd(A[1][0], A[1][1] - 1))
    e = max(tor // g1, 1)
    g, s = conj_m(m, n)
    assert s == 1 and apply(f, LAM) == red(g + LAM + inv(g))
    fib = [(a1, a2) for a1 in range(e) for a2 in range(e)
           if (a1 * A[0][0] + a2 * A[1][0] - a1) % e == 0 and (a1 * A[0][1] + a2 * A[1][1] - a2) % e == 0
           and (a1, a2) != (0, 0)]
    rels = [red((3, 1, -3) + inv(f[1])), red((3, 2, -3) + inv(f[2]))]
    data.append((name, n, e, fib, abel2(g), red(inv(g) + (3,)), rels))
    Mtot = Mtot * e // gcd(Mtot, e)
p = find_prime(Mtot, 200000)
gen = next(x for x in range(2, p) if all(pow(x, (p - 1) // q, p) != 1 for q in prime_factors(p - 1)))
z = pow(gen, (p - 1) // Mtot, p)
say("prime", p, "M", Mtot)

o1 = o2 = plant = True
for name, n, e, fib, (ga, gb), mu, rels in data:
    chars = {}
    for (a1, a2) in fib:
        va, vb = pow(z, (Mtot // e) * a1, p), pow(z, (Mtot // e) * a2, p)
        vt = pow(va, ga, p) * pow(vb, gb, p) % p  # chi(t) = chi(g): chi(mu) = 1
        chars[(a1, a2)] = (va, vb, vt)

    def cls(l):
        r1 = Rep({1: [[l[0]]], 2: [[l[1]]], 3: [[l[2]]]}, p)
        F = [[r1.fox(r, gi)[0][0] for gi in (1, 2, 3)] for r in rels]
        Z = nullspace_mod(F, p, 3)
        for zb in Z:
            lv = r1.cocycle_value({1: [zb[0]], 2: [zb[1]], 3: [zb[2]]}, LAM)[0] % p
            if lv:
                iv = pow(lv, p - 2, p)
                return [x * iv % p for x in zb]
        return None

    def module(l, al, c):
        be = tuple(al[i] * pow(l[i], p - 2, p) % p for i in range(3))
        return {gi: [[al[gi - 1], c[gi - 1] * be[gi - 1] % p], [0, be[gi - 1]]] for gi in (1, 2, 3)}

    def h(mats):
        r = cohomology(Rep(mats, p), rels, mu, LAM)
        return (r["h0"], r["h1"], r["n"])

    def dual(mats):
        R = Rep(mats, p)
        return {gi: [list(row) for row in zip(*R.inv[gi])] for gi in (1, 2, 3)}

    I, bad1, badp, nmod = {}, 0, 0, 0
    for kl, l in chars.items():
        c = cls(l)
        if c is None:
            continue
        for ka, al in chars.items():
            if ka == kl:
                continue
            V = module(l, al, c)
            hv, hd = h(V), h(dual(V))
            kp = ((kl[0] - ka[0]) % e, (kl[1] - ka[1]) % e)  # l alpha^-1
            hp = h(module(l, chars[kp], c))
            bad1 += hd != hp
            kw = ((-ka[0]) % e, (-ka[1]) % e)  # the wrong partner alpha^-1
            if kw != kl and kw in chars:
                badp += hd != h(module(l, chars[kw], c))
            I[(kl, ka)] = hv[2] - hd[2]
            nmod += 1
    anti = all(I[(kl, ka)] == -I[(kl, ((kl[0] - ka[0]) % e, (kl[1] - ka[1]) % e))] for (kl, ka) in I)
    plus, minus = sum(v == 1 for v in I.values()), sum(v == -1 for v in I.values())
    want = {("golden", 4): (12, 4), ("golden", 6): (210, 36), ("golden", 8): (1892, 244), ("bronze", 2): (56, 8)}
    o1 &= bad1 == 0 and nmod == want[(name, n)][0]
    o2 &= anti and plus == minus == want[(name, n)][1]
    plant &= badp > 0
    say(name, "level", n, "| modules", nmod, "| O1 failures", bad1, "| I = +1:", plus, "| I = -1:", minus,
        "| I odd under the involution:", anti, "| wrong-partner failures:", badp)
say("O1 holds:", o1)
say("O2 holds:", o2)
say("plant fires:", plant)
