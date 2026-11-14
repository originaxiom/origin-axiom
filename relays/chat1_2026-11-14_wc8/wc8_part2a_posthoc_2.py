#!/usr/bin/env python3
"""W-C8, part 2a, post hoc 2: written after the referee's read of part 2a's note, committed before its own run.

NOT BLIND. The referee's read (a separate session, with its own code) reported that on the odd levels non-split doublets
DO exist when the extension character l has l(mu) = -1 (the Wang sequence: H^1(G; l) ~ H^1(F; l)^t, and t acts on that
line by s * l(mu)), that their n-gap is 0, and which characters carry the odd-level gap. This file recomputes those
statements on this seat's code. Definitions as in part 2a (imported by text, not re-run).
  Characters: chi o sigma^n = chi on the fibre, chi(t) any 2e-th root of unity (all characters, family (a)).
  Doublets: for every ordered pair (alpha, beta) of characters, l = alpha / beta, and every vector of a basis of a
  complement of B^1 in Z^1(G; l): V = [[alpha, c beta], [0, beta]].
EXPECTATIONS (taken from the referee's report, written before this run):
  G1  On levels 3 and 5 there are doublets with c(lambda) != 0, and every one of them has l(mu) = -1.
  G2  On levels 1, 3 and 5 the n-gap n(V) - n(V* (x) w) is 0 on every doublet; on levels 2 and 4 it is non-zero on
      some (the record's sector modules).
  G3  The number of doublets and their h^1-gap census: level 3, 64 doublets, gap +-1 on 4 + 4 and +-2 on 3 + 3;
      level 5, 2,662 doublets, +-1 on 11 + 11 and +-2 on 10 + 10.
  G4  On levels 1, 3 and 5 the characters with gap +1 are the trivial character and the fibre-non-trivial characters
      with chi(mu) = -1; those with gap -1 are w and the fibre-non-trivial characters with chi(mu) = +1.

    python3 -I -u wc8_part2a_posthoc_2.py
"""
import os
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = open(os.path.join(HERE, "wc8_part2a_checks.py")).read()
ns = {}
exec(SRC.split("EXP = {}")[0], ns)
red, inv, sig_pow, abel2, LAM, conjugator = ns["red"], ns["inv"], ns["sig_pow"], ns["abel2"], ns["LAM"], ns["conjugator"]
Rep, cohomology, nullspace_mod, rank_mod, find_prime = (ns["Rep"], ns["cohomology"], ns["nullspace_mod"],
                                                        ns["rank_mod"], ns["find_prime"])


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


p = find_prime(2 * 16 * 9 * 5 * 11 * 29, 1)
gen = next(x for x in range(2, p) if all(pow(x, (p - 1) // q, p) != 1 for q in prime_factors(p - 1)))
G = dict(G1=True, G2=True, G3=True, G4=True)
want3 = {3: (64, {(1,): 4, (-1,): 4, (2,): 3, (-2,): 3}), 5: (2662, {(1,): 11, (-1,): 11, (2,): 10, (-2,): 10})}
for n in (1, 2, 3, 4, 5):
    f = sig_pow(n)
    A = [[abel2(f[1])[0], abel2(f[2])[0]], [abel2(f[1])[1], abel2(f[2])[1]]]
    tor = abs((A[0][0] - 1) * (A[1][1] - 1) - A[0][1] * A[1][0])
    g1 = gcd(gcd(A[0][0] - 1, A[0][1]), gcd(A[1][0], A[1][1] - 1))
    e = tor // g1 if tor > 1 else 1
    g, s = conjugator(n)
    mu = red(inv(g) + (3,))
    w = p - 1 if n % 2 else 1
    z = pow(gen, (p - 1) // (2 * e), p)
    fib = [(a1, a2) for a1 in range(e) for a2 in range(e)
           if (a1 * A[0][0] + a2 * A[1][0] - a1) % e == 0 and (a1 * A[0][1] + a2 * A[1][1] - a2) % e == 0]
    chars = [(pow(z, 2 * a1, p), pow(z, 2 * a2, p), pow(z, j, p)) for (a1, a2) in fib for j in range(2 * e)]
    base = [red((3, 1, -3) + inv(f[1])), red((3, 2, -3) + inv(f[2]))]

    def rep1(ch):
        return Rep({1: [[ch[0]]], 2: [[ch[1]]], 3: [[ch[2]]]}, p)

    def chi_mu(ch):
        R = rep1(ch)
        return R.of(mu)[0][0]

    def dualw(V):
        dual = {gi: [list(r) for r in zip(*V.inv[gi])] for gi in (1, 2, 3)}
        return Rep({1: dual[1], 2: dual[2], 3: [[x * w % p for x in r] for r in dual[3]]}, p)

    # characters' gaps and G4
    plus, minus = set(), set()
    for ch in chars:
        V = rep1(ch)
        gp = cohomology(V, base, mu, LAM)["h1"] - cohomology(dualw(V), base, mu, LAM)["h1"]
        if gp == 1:
            plus.add(ch)
        elif gp == -1:
            minus.add(ch)
        elif gp != 0:
            G["G4"] = False
    if n % 2:
        fib_triv = lambda ch: ch[0] == 1 and ch[1] == 1
        want_plus = {ch for ch in chars if (ch == (1, 1, 1)) or (not fib_triv(ch) and chi_mu(ch) == p - 1)}
        want_minus = {ch for ch in chars if (ch == (1, 1, w)) or (not fib_triv(ch) and chi_mu(ch) == 1)}
        G["G4"] &= plus == want_plus and minus == want_minus
    # doublets
    census, ngap_nonzero, cl_nonzero, cl_bad_mu, nd = {}, 0, 0, 0, 0
    for al in chars:
        for be in chars:
            l = tuple(al[i] * pow(be[i], p - 2, p) % p for i in range(3))
            R = rep1(l)
            F = [[R.fox(r, gi)[0][0] for gi in (1, 2, 3)] for r in base]
            Z = nullspace_mod(F, p, 3)
            cob = [(l[i] - 1) % p for i in range(3)]
            rk_cob = rank_mod([cob], p)
            basis = []
            for zb in Z:
                if rank_mod([cob] * (rk_cob > 0) + basis + [zb], p) > rank_mod([cob] * (rk_cob > 0) + basis, p):
                    basis.append(zb)
            for c in basis:
                V = Rep({gi: [[al[gi - 1], c[gi - 1] * be[gi - 1] % p], [0, be[gi - 1]]] for gi in (1, 2, 3)}, p)
                cV, cW = cohomology(V, base, mu, LAM), cohomology(dualw(V), base, mu, LAM)
                k1 = cV["h1"] - cW["h1"]
                census[(k1,)] = census.get((k1,), 0) + 1
                ngap_nonzero += (cV["n"] - cW["n"]) != 0
                lv = R.cocycle_value({1: [c[0]], 2: [c[1]], 3: [c[2]]}, LAM)[0]
                if lv:
                    cl_nonzero += 1
                    cl_bad_mu += chi_mu(l) != p - 1
                nd += 1
    nonzero_census = {k: v for k, v in census.items() if k != (0,)}
    print("level", n, "orientable", n % 2 == 0, "| characters", len(chars), "| gap +1:", len(plus), "gap -1:", len(minus),
          "| doublets", nd, "| h1-gap census (non-zero):", sorted(nonzero_census.items()),
          "| doublets with c(lambda) != 0:", cl_nonzero, "of them with l(mu) != -1:", cl_bad_mu,
          "| doublets with non-zero n-gap:", ngap_nonzero, flush=True)
    if n in (3, 5):
        G["G1"] &= cl_nonzero > 0 and cl_bad_mu == 0
        G["G3"] &= nd == want3[n][0] and nonzero_census == want3[n][1]
    if n % 2:
        G["G2"] &= ngap_nonzero == 0
    elif n in (2, 4):
        G["G2"] &= (ngap_nonzero > 0) if n == 4 else True
for k in ("G1", "G2", "G3", "G4"):
    print(k, "holds:", G[k])
