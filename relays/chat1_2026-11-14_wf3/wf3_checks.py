#!/usr/bin/env python3
"""W-F3: the cone-point loophole. Replace the puncture by a cone point of order k: is every gap then zero?

Data-free; this seat's own code. The helpers (free group, Fox calculus over F_p, the cohomology routine) are taken by
text from W-C8 part 2a's sealed script (definitions only, up to its census), which is not re-run.

    python3 -I -u wf3_checks.py

DEFINITIONS
  For the tick sigma (a -> ab, b -> a) and level n: G_n = <a, b, t | t a t^-1 = sigma^n(a), t b t^-1 = sigma^n(b)> (the
  puncture, k = infinity), and G_n,k = the same with lambda^k = 1, lambda = [a, b] (the fibre's puncture replaced by a
  cone point of order k: a closed 3-orbifold). Levels n = 2..6; odd n non-orientable, w(t) = (-1)^n.
  Modules: (a) every character with chi o sigma^n = chi on the fibre and chi(t) any 2e-th root of unity; (b) every
  non-split module [[alpha, c beta], [0, beta]] with alpha, beta fibre-torsion characters (chi(mu) = 1), l = alpha/beta
  non-trivial, c a class of H^1(G; l) that is not a coboundary, if any. The gap: h^1(V) - h^1(V* (x) w).
  A record sector module needs c(lambda) = 1 (B1438's normalisation).

EXPECTATIONS, written before the run (the agy-exp lane's question, relayed by the author; this seat's hand derivation):
  K1  For every finite k in 2..6 and every level n in 2..6: no class of H^1(G_n,k; l) has c(lambda) != 0
      (c(lambda^k) = k c(lambda) = 0, with p prime to k), so no record sector module exists on a cone point.
  K2  For every finite k in 2..6, every level, every module of (a) and (b): gap = 0 (closed orbifold, rational duality,
      and V^G = 0 = (V* (x) w)^G for the modules with non-zero gap at k = infinity).
  K3  Control, k = infinity (the puncture): some module has a non-zero gap on every level n in 3..6 (as in W-C8
      part 2a: sector modules on even levels, characters on odd ones). Level 2 (m004 itself) has no fibre torsion and
      is reported only.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = open(os.path.join(HERE, "..", "chat1_2026-11-14_wc8", "wc8_part2a_checks.py")).read()
ns = {}
exec(SRC.split("EXP = {}")[0], ns)
red, inv, sig_pow, abel2, LAM, conjugator = ns["red"], ns["inv"], ns["sig_pow"], ns["abel2"], ns["LAM"], ns["conjugator"]
Rep, cohomology, nullspace_mod, find_prime = ns["Rep"], ns["cohomology"], ns["nullspace_mod"], ns["find_prime"]
from math import gcd


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


p = find_prime(2 * 16 * 9 * 5 * 11 * 29 * 7, 1)  # prime to every k in 2..6? check below
assert all(p % k for k in range(2, 7))
gen = next(x for x in range(2, p) if all(pow(x, (p - 1) // q, p) != 1 for q in prime_factors(p - 1)))
say("prime", p)

k1_ok, k2_ok, k3_ok = True, True, True
for n in range(2, 7):
    f = sig_pow(n)
    A = [[abel2(f[1])[0], abel2(f[2])[0]], [abel2(f[1])[1], abel2(f[2])[1]]]
    tor = abs((A[0][0] - 1) * (A[1][1] - 1) - A[0][1] * A[1][0])
    g1 = gcd(gcd(A[0][0] - 1, A[0][1]), gcd(A[1][0], A[1][1] - 1))
    e = tor // g1
    g, s = conjugator(n)
    mu = red(inv(g) + (3,))
    w = p - 1 if n % 2 else 1
    z = pow(gen, (p - 1) // (2 * e), p) if e > 1 else pow(gen, (p - 1) // 2, p)
    ee = max(e, 1)
    fib = [(a1, a2) for a1 in range(ee) for a2 in range(ee)
           if (a1 * A[0][0] + a2 * A[1][0] - a1) % ee == 0 and (a1 * A[0][1] + a2 * A[1][1] - a2) % ee == 0]
    chars = [(pow(z, 2 * a1, p), pow(z, 2 * a2, p), pow(z, j, p)) for (a1, a2) in fib for j in range(2 * ee)]
    ga, gb = abel2(g)
    tors = [(pow(z, 2 * a1, p), pow(z, 2 * a2, p), pow(z, 2 * ((a1 * ga + a2 * gb) % ee), p)) for (a1, a2) in fib
            if (a1, a2) != (0, 0)]
    base = [red((3, 1, -3) + inv(f[1])), red((3, 2, -3) + inv(f[2]))]
    for k in (2, 3, 4, 5, 6, None):
        rels = base + ([LAM * k] if k else [])
        rels = [red(r) for r in rels]
        gaps_nonzero, sector_exists, nb = 0, False, 0

        def gap(mats):
            V = Rep(mats, p)
            dual = {gi: [list(r) for r in zip(*V.inv[gi])] for gi in (1, 2, 3)}
            Vdw = Rep({1: dual[1], 2: dual[2], 3: [[x * w % p for x in r] for r in dual[3]]}, p)
            return cohomology(V, rels, mu, LAM)["h1"] - cohomology(Vdw, rels, mu, LAM)["h1"]

        for ch in chars:
            gaps_nonzero += gap({1: [[ch[0]]], 2: [[ch[1]]], 3: [[ch[2]]]}) != 0
        for l in tors:
            r1 = Rep({1: [[l[0]]], 2: [[l[1]]], 3: [[l[2]]]}, p)
            F = [[r1.fox(r, gi)[0][0] for gi in (1, 2, 3)] for r in rels]
            Zb = nullspace_mod(F, p, 3)
            cob = [(l[0] - 1) % p, (l[1] - 1) % p, (l[2] - 1) % p]
            c = next((zb for zb in Zb if any((zb[i] * cob[j] - zb[j] * cob[i]) % p
                                             for i in range(3) for j in range(3))), None)
            if c is None:
                continue
            zz = {1: [c[0]], 2: [c[1]], 3: [c[2]]}
            if r1.cocycle_value(zz, LAM)[0] % p:
                sector_exists = True
            for al in tors:
                be = tuple(al[i] * pow(l[i], p - 2, p) % p for i in range(3))
                if be[:2] == (1, 1):
                    continue
                mats = {gi: [[al[gi - 1], c[gi - 1] * be[gi - 1] % p], [0, be[gi - 1]]] for gi in (1, 2, 3)}
                gaps_nonzero += gap(mats) != 0
                nb += 1
        say("level", n, "k", k if k else "infinity", "| characters", len(chars), "| non-split modules", nb,
            "| a class with c(lambda) != 0:", sector_exists, "| modules with a non-zero gap:", gaps_nonzero)
        if k:
            k1_ok &= not sector_exists
            k2_ok &= gaps_nonzero == 0
        elif n >= 3:
            k3_ok &= gaps_nonzero > 0
say("K1 holds:", k1_ok, "; K2 holds:", k2_ok, "; K3 holds:", k3_ok)
