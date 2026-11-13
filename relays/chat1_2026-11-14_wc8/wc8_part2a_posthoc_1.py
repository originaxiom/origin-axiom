#!/usr/bin/env python3
"""W-C8, part 2a, post hoc 1: written after the sealed run, committed before its own run.

WHAT THE SEALED RUN SHOWED. On the odd (non-orientable) levels 3, 5, 7 there are fibre-torsion characters (3, 10, 28)
but no sector module: no class of H^1(G; l) is 1 on lambda. By hand: the cusp is a Klein bottle, mu lambda mu^-1 =
lambda^-1, and for a character trivial on mu and lambda a cocycle has c(lambda) = c(mu lambda mu^-1) = c(lambda^-1) =
-c(lambda), so c(lambda) = 0. B1438's normalisation u(lambda) = 1, and with it the slope and the record's sector module,
does not exist there. So E5's twisted-duality test and its control were empty on the odd levels.

THIS FILE tests twisted duality and main's expectation on the odd levels with modules that do exist there, keeping every
sealed definition (imported from the sealed file, which runs again; its output is discarded):
  (a) every 1-dimensional character chi of G_n with chi o sigma^n = chi on the fibre (trivial on the fibre included) and
      chi(t) any 2e-th root of unity;
  (b) the non-split modules [[alpha, c beta], [0, beta]] for fibre-torsion characters (chi(mu) = 1) with c any class of
      H^1(G; alpha/beta) that is not a coboundary (no normalisation).
EXPECTATIONS, written before the run:
  H1  On levels 3, 5, 7, for every module of (a) and (b): h^2(V) = h^1_rel(V* (x) w). Control: h^2(V) = h^1_rel(V*) fails
      for some module on each odd level.
  H2  Reported, no expectation: the census of (h^1(V) - h^1(V* (x) w), n(V) - n(V* (x) w)) on levels 3..8 for (a) and (b).

    python3 -I -u wc8_part2a_posthoc_1.py
"""
import contextlib, io, os, runpy

HERE = os.path.dirname(os.path.abspath(__file__))
with contextlib.redirect_stdout(io.StringIO()):
    S = runpy.run_path(os.path.join(HERE, "wc8_part2a_checks.py"))
Rep, cohomology, red, inv, EXP, nullspace_mod = S["Rep"], S["cohomology"], S["red"], S["inv"], S["EXP"], S["nullspace_mod"]
abel2, prime_factors, LAM = S["abel2"], S["prime_factors"], S["LAM"]
p = S["P1"]


def say(*a):
    print(*a, flush=True)


gen = next(x for x in range(2, p) if all(pow(x, (p - 1) // q, p) != 1 for q in prime_factors(p - 1)))
for n in range(3, 9):
    e, f, mu, A, g = EXP[n]["expo"], EXP[n]["f"], EXP[n]["mu"], EXP[n]["A"], EXP[n]["g"]
    rels = [red((3, 1, -3) + inv(f[1])), red((3, 2, -3) + inv(f[2]))]
    w = p - 1 if n % 2 else 1
    z = pow(gen, (p - 1) // (2 * e), p)  # order 2e
    fib = [(k1, k2) for k1 in range(e) for k2 in range(e)
           if (k1 * A[0][0] + k2 * A[1][0] - k1) % e == 0 and (k1 * A[0][1] + k2 * A[1][1] - k2) % e == 0]
    chars = [(pow(z, 2 * k1, p), pow(z, 2 * k2, p), pow(z, j, p)) for (k1, k2) in fib for j in range(2 * e)]
    ga, gb = abel2(g)
    tors = [(pow(z, 2 * k1, p), pow(z, 2 * k2, p), pow(z, 2 * ((k1 * ga + k2 * gb) % e), p)) for (k1, k2) in fib
            if (k1, k2) != (0, 0)]
    ok_tw, ok_plain, census_a, census_b = True, True, {}, {}

    def test(mats, census):
        global ok_tw, ok_plain
        V = Rep(mats, p)
        dual = {gi: [list(r) for r in zip(*V.inv[gi])] for gi in (1, 2, 3)}
        Vd = Rep(dual, p)
        Vdw = Rep({1: dual[1], 2: dual[2], 3: [[x * w % p for x in r] for r in dual[3]]}, p)
        cV, cVd, cVdw = cohomology(V, rels, mu, LAM), cohomology(Vd, rels, mu, LAM), cohomology(Vdw, rels, mu, LAM)
        tw = cV["h2"] == cVdw["rel1"]
        pl = cV["h2"] == cVd["rel1"]
        k = (cV["h1"] - cVdw["h1"], cV["n"] - cVdw["n"])
        census[k] = census.get(k, 0) + 1
        return tw, pl

    tw_all, pl_all = True, True
    for ch in chars:
        tw, pl = test({1: [[ch[0]]], 2: [[ch[1]]], 3: [[ch[2]]]}, census_a)
        tw_all &= tw
        pl_all &= pl
    nb = 0
    for l in tors:
        r1 = Rep({1: [[l[0]]], 2: [[l[1]]], 3: [[l[2]]]}, p)
        F = [[r1.fox(r, gi)[0][0] for gi in (1, 2, 3)] for r in rels]
        Zb = nullspace_mod(F, p, 3)
        cob = [(l[0] - 1) % p, (l[1] - 1) % p, (l[2] - 1) % p]
        c = None
        for zb in Zb:
            # not a coboundary: not proportional to cob
            if any((zb[i] * cob[j] - zb[j] * cob[i]) % p for i in range(3) for j in range(3)):
                c = zb
                break
        if c is None:
            continue
        for al in tors:
            be = tuple(al[i] * pow(l[i], p - 2, p) % p for i in range(3))
            if be[:2] == (1, 1):
                continue
            mats = {gi: [[al[gi - 1], c[gi - 1] * be[gi - 1] % p], [0, be[gi - 1]]] for gi in (1, 2, 3)}
            tw, pl = test(mats, census_b)
            tw_all &= tw
            pl_all &= pl
            nb += 1
    say("level", n, "orientable", n % 2 == 0, "| (a) characters:", len(chars), "| (b) non-split modules:", nb,
        "| h2(V) = h1_rel(V* w) for all:", tw_all, "| h2(V) = h1_rel(V*) for all:", pl_all)
    say("   census (h1 gap, n gap) (a):", sorted(census_a.items()))
    say("   census (h1 gap, n gap) (b):", sorted(census_b.items()))
