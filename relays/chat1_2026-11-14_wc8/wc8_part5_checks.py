#!/usr/bin/env python3
"""W-C8, part 5 (M20): the bronze rival beside the golden pair, in the frames this seat can compute without SnapPy.

Data-free; this seat's own code. Helpers (free group, Fox calculus over F_p, the cohomology routine) are taken by text
from W-C8 part 2a's sealed script (definitions only), which is not re-run.

    python3 -I -u wc8_part5_checks.py

DEFINITIONS
  The metallic tick tau_m: a -> a^m b, b -> a (abelianisation J_m = [[m, 1], [1, 0]], det -1). m = 1 is the golden tick
  sigma; m = 3 is the bronze tick. Level n: G = <a, b, t | t a t^-1 = tau_m^n(a), t b t^-1 = tau_m^n(b)>. Level 1 of the
  bronze tick is m005 (b-+RRR in SnapPy's name, as M20 gives it), level 2 is s464 (b++LLLRRR = L^3 R^3 = J_3^2), as M20
  names them; this seat does not check the names (no SnapPy). The cusp conjugator: tau_m(lambda) = a^m lambda^-1 a^-m,
  so g_1 = a^m, g_(k+1) = tau_m(g_k) a^m, s_k = (-1)^k. Everything else as in part 2a and its post hoc 1 and W-F3:
  characters with chi(mu) = 1 (fibre torsion) and with any t-value (all characters), the record's sector modules
  (c(lambda) = 1), non-split modules with any class c, twisted duality, and the cone relation lambda^k = 1.

EXPECTATIONS, written before the run (derived by hand from the definitions):
  R1  tau_3 abelianises to [[3, 1], [1, 0]] (det -1) and tau_3^2 to [[10, 3], [3, 1]] = L^3 R^3.
  R2  The fibre torsion |det(J_m^n - I)| at levels 1, 2, 3: golden 1, 1, 4; bronze 3, 9, 36. So the bronze pair has
      torsion in H_1 at its own levels (SE1 fails for both m005 and s464); the golden pair has none.
  R3  Free-cusp frame: b_1 = 1 and the cusp's rank 1 at levels 1 to 3 for both ticks: closed, like every word state.
  R4  Class-index frame at the roots' own levels:
        golden: no character at levels 1 and 2 (empty, as found in part 2a);
        bronze: at level 1 (m005, non-orientable) 2 fibre-torsion characters and no record sector module (the
        Klein-bottle cusp); at level 2 (s464, orientable) 8 fibre-torsion characters and a non-empty set of record
        sector modules, on which B1438's firing law n(V) = [s(alpha) = s(l)] holds.
  R5  Twisted duality h^2(V) = h^1_rel(V* (x) w) holds for every character and every non-split module at levels 1 to 3
      of both ticks; with w left out it fails on the odd levels where non-trivial modules exist.
  R6  The cone relation (k = 2, 3, 4) at levels 1 to 3 of both ticks: no class with c(lambda) != 0, and the only
      characters with a non-zero gap are the trivial character and w, on odd levels only.
  R7  Control: the golden counts at levels 1 to 3 reproduce part 2a and its post hoc 1 (characters 0, 0, 3 with
      chi(mu) = 1; all characters 2, 2, 16 at levels 1, 2, 3 with t-values the 2e-th roots, e = max(exponent, 1)).
  Reported: the gap census (h^1 gap, n gap) for every level and both ticks, side by side.
"""
import os
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = open(os.path.join(HERE, "wc8_part2a_checks.py")).read()
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


p = find_prime(2 * 16 * 9 * 5 * 11 * 29 * 7 * 13, 1)
gen = next(x for x in range(2, p) if all(pow(x, (p - 1) // q, p) != 1 for q in prime_factors(p - 1)))
say("prime", p)

f1 = tick_pow(3, 1)
f2 = tick_pow(3, 2)
r1 = [abel2(f1[1]), abel2(f1[2])] == [[3, 1], [1, 0]] and [abel2(f2[1]), abel2(f2[2])] == [[10, 3], [3, 1]]
say("R1 tau_3 abelianises to J_3 (columns):", [abel2(f1[1]), abel2(f1[2])], "; tau_3^2:", [abel2(f2[1]), abel2(f2[2])],
    "; holds:", r1)

OK = dict(R2=True, R3=True, R4=True, R5=True, R6=True, R7=True)
want_tor = {1: [1, 1, 4], 3: [3, 9, 36]}
for m in (1, 3):
    for n in (1, 2, 3):
        f = tick_pow(m, n)
        A = [[abel2(f[1])[0], abel2(f[2])[0]], [abel2(f[1])[1], abel2(f[2])[1]]]
        det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
        tor = abs((A[0][0] - 1) * (A[1][1] - 1) - A[0][1] * A[1][0])
        g1 = gcd(gcd(A[0][0] - 1, A[0][1]), gcd(A[1][0], A[1][1] - 1))
        e = tor // g1 if tor > 1 else 1
        g, s = conj_m(m, n)
        ok_conj = red(g + (LAM if s == 1 else inv(LAM)) + inv(g)) == apply(f, LAM) and s == det
        mu = red(inv(g) + (3,))
        t_exp = sum(1 if x == 3 else -1 if x == -3 else 0 for x in mu)
        b1 = 1 if tor != 0 else 2
        OK["R2"] &= tor == want_tor[m][n - 1]
        OK["R3"] &= b1 == 1 and t_exp == 1 and ok_conj
        w = p - 1 if n % 2 else 1
        z = pow(gen, (p - 1) // (2 * e), p)
        fib = [(a1, a2) for a1 in range(e) for a2 in range(e)
               if (a1 * A[0][0] + a2 * A[1][0] - a1) % e == 0 and (a1 * A[0][1] + a2 * A[1][1] - a2) % e == 0]
        ga, gb = abel2(g)
        tors = [(pow(z, 2 * a1, p), pow(z, 2 * a2, p), pow(z, 2 * ((a1 * ga + a2 * gb) % e), p)) for (a1, a2) in fib
                if (a1, a2) != (0, 0)]
        allch = [(pow(z, 2 * a1, p), pow(z, 2 * a2, p), pow(z, j, p)) for (a1, a2) in fib for j in range(2 * e)]
        base = [red((3, 1, -3) + inv(f[1])), red((3, 2, -3) + inv(f[2]))]

        def dualw(V):
            dual = {gi: [list(r) for r in zip(*V.inv[gi])] for gi in (1, 2, 3)}
            return Rep(dual, p), Rep({1: dual[1], 2: dual[2], 3: [[x * w % p for x in r] for r in dual[3]]}, p)

        # characters' classes; record sector modules (c(lambda) = 1) and non-split modules (any c)
        census, tw_all, pl_all, sector, fire_ok = {}, True, True, 0, True
        slopes, classes = {}, {}
        for l in tors:
            R1 = Rep({1: [[l[0]]], 2: [[l[1]]], 3: [[l[2]]]}, p)
            F = [[R1.fox(r, gi)[0][0] for gi in (1, 2, 3)] for r in base]
            Zb = nullspace_mod(F, p, 3)
            cob = [(l[0] - 1) % p, (l[1] - 1) % p, (l[2] - 1) % p]
            c = next((zb for zb in Zb if any((zb[i] * cob[j] - zb[j] * cob[i]) % p
                                             for i in range(3) for j in range(3))), None)
            classes[l] = c
            if c is not None:
                zz = {1: [c[0]], 2: [c[1]], 3: [c[2]]}
                lv = R1.cocycle_value(zz, LAM)[0]
                if lv:
                    il = pow(lv, p - 2, p)
                    zz = {k: [v[0] * il % p] for k, v in zz.items()}
                    slopes[l] = R1.cocycle_value(zz, mu)[0]
                    classes[l] = [zz[1][0], zz[2][0], zz[3][0]]
        nb = 0
        for l in tors:
            c = classes[l]
            if c is None:
                continue
            for al in tors:
                be = tuple(al[i] * pow(l[i], p - 2, p) % p for i in range(3))
                if be[:2] == (1, 1):
                    continue
                V = Rep({gi: [[al[gi - 1], c[gi - 1] * be[gi - 1] % p], [0, be[gi - 1]]] for gi in (1, 2, 3)}, p)
                Vd, Vdw = dualw(V)
                cV, cVd, cVdw = cohomology(V, base, mu, LAM), cohomology(Vd, base, mu, LAM), cohomology(Vdw, base, mu, LAM)
                tw_all &= cV["h2"] == cVdw["rel1"]
                pl_all &= cV["h2"] == cVd["rel1"]
                key = (cV["h1"] - cVdw["h1"], cV["n"] - cVdw["n"])
                census[key] = census.get(key, 0) + 1
                nb += 1
                if l in slopes:
                    sector += 1
                    fire = int(al in slopes and slopes[al] == slopes[l])
                    fire_ok &= cV["n"] == fire
        ccensus = {}
        for ch in allch:
            V = Rep({1: [[ch[0]]], 2: [[ch[1]]], 3: [[ch[2]]]}, p)
            Vd, Vdw = dualw(V)
            cV, cVd, cVdw = cohomology(V, base, mu, LAM), cohomology(Vd, base, mu, LAM), cohomology(Vdw, base, mu, LAM)
            tw_all &= cV["h2"] == cVdw["rel1"]
            pl_all &= cV["h2"] == cVd["rel1"]
            key = (cV["h1"] - cVdw["h1"], cV["n"] - cVdw["n"])
            ccensus[key] = ccensus.get(key, 0) + 1
        OK["R5"] &= tw_all and (n % 2 == 0 or len(tors) == 0 or not pl_all)
        # cone
        cone_ok = True
        for k in (2, 3, 4):
            rels = base + [red(LAM * k)]
            for l in tors:
                R1 = Rep({1: [[l[0]]], 2: [[l[1]]], 3: [[l[2]]]}, p)
                F = [[R1.fox(r, gi)[0][0] for gi in (1, 2, 3)] for r in rels]
                for zb in nullspace_mod(F, p, 3):
                    if R1.cocycle_value({1: [zb[0]], 2: [zb[1]], 3: [zb[2]]}, LAM)[0]:
                        cone_ok = False
            nz = []
            for ch in allch:
                V = Rep({1: [[ch[0]]], 2: [[ch[1]]], 3: [[ch[2]]]}, p)
                Vd, Vdw = dualw(V)
                gp = cohomology(V, rels, mu, LAM)["h1"] - cohomology(Vdw, rels, mu, LAM)["h1"]
                if gp:
                    nz.append(("trivial" if ch == (1, 1, 1) else "w" if ch == (1, 1, w) else "other", gp))
            cone_ok &= sorted(nz) == (sorted([("trivial", 1), ("w", -1)]) if n % 2 else [])
        OK["R6"] &= cone_ok
        if m == 1:
            OK["R7"] &= (len(tors), len(allch)) == ({1: 0, 2: 0, 3: 3}[n], {1: 2, 2: 2, 3: 16}[n])
        if (m, n) in ((1, 1), (1, 2)):
            OK["R4"] &= len(tors) == 0
        if (m, n) == (3, 1):
            OK["R4"] &= len(tors) == 2 and sector == 0
        if (m, n) == (3, 2):
            OK["R4"] &= len(tors) == 8 and sector > 0 and fire_ok
        say("tick", m, "level", n, "orientable", det == 1, "| torsion", tor, "exponent", e, "| conjugator", ok_conj,
            "| fibre-torsion characters", len(tors), "| all characters", len(allch), "| non-split modules", nb,
            "| record sector modules", sector, "| firing law", fire_ok, "| twisted duality", tw_all,
            "| untwisted holds", pl_all, "| cone (k = 2, 3, 4) as expected", cone_ok)
        say("   gap census, non-split modules:", sorted(census.items()), "; characters:", sorted(ccensus.items()))
for k in ("R2", "R3", "R4", "R5", "R6", "R7"):
    say(k, "holds:", OK[k])
