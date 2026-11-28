#!/usr/bin/env python3
"""The web seat's peer check of queue card Q0023 (fam3-v1-high-03): a second computation in other code, by other means.

The card counts, over the 1 199 orientable one-cusped census manifolds with at most six ideal tetrahedra, those whose
fundamental group maps onto 2T, 2O and 2I, with m004's count, two "plants" on H_1, and three manifold-free group-theory
steps. This script recomputes those counts from presentations this seat extracted itself (q0023_extract.py, run once,
output q0023_presentations.json beside this script), with its own groups and its own counting: 2T = SL(2, F_3),
2I = SL(2, F_5), and 2O built as a subgroup of order 48 of SL(2, F_7) (the card builds 2O from quaternions);
automorphism groups found by brute force over generating pairs; surjections counted with the first generator's image
taken over Aut(G)-orbit representatives, weighted by orbit size, and the total divided by |Aut(G)| (Aut(G) acts freely
on surjections). Standard library only. It imports nothing of the producer's and reads no file of theirs.

THE DEFINITIONS USED (the card's definitions field). A manifold "admits a surjection onto G" when Hom(pi_1, G) has a
surjective element; its count is the number of surjections modulo Aut(G). The Z/3 plant: the number of nonzero
homomorphisms to F_3 equals 3^d - 1, d = dim H_1(M; F_3), here d from the rank mod 3 of the relators' exponent-sum
matrix and the count by enumeration. The (Z/2)^3 plant: dim H_1(M; F_2) >= 3. Post-E_6 steps: the kernel of
SU(3) x SU(2) x U(1) -> S(U(3) x U(2)), (A, B, z) -> (A z^2, B z^-3), restricted to the centres, is the set of
(a mod 3, b mod 2, x mod 1) with a/3 + 2x and b/2 - 3x integers (such x lie in (1/6)Z, since x = 3x - 2x); the
traceless commutant of su(3) + su(2) in 5 x 5 matrices; Tr(T_3^2) / Tr(Q^2) on the 5 with T_3 = diag(0,0,0,1/2,-1/2),
Y = (-1/6) diag(2,2,2,-3,-3), Q = T_3 + Y.

THE CONDITION, written before any of this was run. The card holds where this seat checks it if and only if all of:
  G1. The census holds 1 199 manifolds, 1 041 with two-generator presentations and 158 with three.
  G2. The three groups have orders 24, 48, 120, each a single involution, the element-order counts of the binary
      tetrahedral, octahedral and icosahedral groups, and |Aut| = 24, 48, 120.
  G3. 384 manifolds admit a surjection onto 2T, 304 of them with exactly 2 classes; 362 onto 2O; 609 onto 2I; m004's
      counts are (2T, 2O, 2I) = (2, 0, 0); every count is a whole number.
  G4. The Z/3 plant holds on all 1 199 (count 3^d - 1, with d >= 1); the (Z/2)^3 plant fails on all 1 041
      two-generator presentations.
  G5. The kernel has 6 elements with orders [1, 2, 3, 3, 6, 6] and is cyclic; the traceless commutant is 1-dimensional,
      spanned by diag(2, 2, 2, -3, -3); Tr(T_3^2) / Tr(Q^2) = 3/8.
  Any one failing is a fault in the card as this seat reads it, or in this seat's reading; the note says which.

NOT CHECKED HERE: the 400 B993 control manifolds and their per-object match (B993's own results are not read); the
fractions as rates beyond the counts; the card's identification of the three structural grades with the 2T route
(a reading, not a computation); its planted controls and float count.

    python3 relays/chat1_2026-11-28_peer/q0023_check.py            # the check; exits 0, prints the verdict
    python3 relays/chat1_2026-11-28_peer/q0023_check.py --control  # a target and m004's relator made wrong; exits 1
"""
import itertools
import json
import math
import pathlib
import sys
from fractions import Fraction

CONTROL = "--control" in sys.argv


def say(text):
    print("DECISIVE: " + text, flush=True)


# ---------------------------------------------------------------- finite groups as tables
def sl2(p):
    return [(a, b, c, d) for a in range(p) for b in range(p) for c in range(p) for d in range(p)
            if (a * d - b * c) % p == 1]


def mmul(p):
    return lambda x, y: ((x[0] * y[0] + x[1] * y[2]) % p, (x[0] * y[1] + x[1] * y[3]) % p,
                         (x[2] * y[0] + x[3] * y[2]) % p, (x[2] * y[1] + x[3] * y[3]) % p)


def closure(gens, mul, one):
    S, frontier = {one}, [one]
    while frontier:
        new = []
        for x in frontier:
            for g in gens:
                y = mul(x, g)
                if y not in S:
                    S.add(y)
                    new.append(y)
        frontier = new
    return S


def table(elems, mul):
    idx = {g: i for i, g in enumerate(elems)}
    M = [[idx[mul(x, y)] for y in elems] for x in elems]
    e = next(i for i in range(len(elems)) if all(M[i][j] == j for j in range(len(elems))))
    inv = [next(j for j in range(len(elems)) if M[i][j] == e) for i in range(len(elems))]
    return M, e, inv


def orders(M, e):
    out = []
    for i in range(len(M)):
        n, x = 1, i
        while x != e:
            x, n = M[x][i], n + 1
        out.append(n)
    return out


def group_2o():
    """a subgroup of order 48 of SL(2, F_7): the first one met, generated by an element of order 8 and one of order 3"""
    G = sl2(7)
    mul = mmul(7)
    one = (1, 0, 0, 1)

    def order_of(x):
        n, y = 1, x
        while y != one:
            y, n = mul(y, x), n + 1
        return n

    o8 = [x for x in G if order_of(x) == 8]
    o3 = [x for x in G if order_of(x) == 3]
    for a in o8:
        for b in o3:
            S = closure([a, b], mul, one)
            if len(S) == 48:
                return sorted(S), mul
    return None, mul


def automorphisms(M, e, inv, ords):
    """all automorphisms as permutations, by brute force over images of a generating pair"""
    n = len(M)
    gen = next((x, y) for x in range(n) for y in range(n) if len(closure_idx([x, y], M, e)) == n)
    x0, y0 = gen
    order_bfs, parent = [e], {e: None}
    for g in order_bfs:
        for s in (x0, y0):
            h = M[g][s]
            if h not in parent:
                parent[h] = (g, s)
                order_bfs.append(h)
    auts = []
    for x in range(n):
        if ords[x] != ords[x0]:
            continue
        for y in range(n):
            if ords[y] != ords[y0]:
                continue
            img = {x0: x, y0: y}
            phi = [None] * n
            phi[e] = e
            for g in order_bfs[1:]:
                pg, s = parent[g]
                phi[g] = M[phi[pg]][img[s]]
            if len(set(phi)) != n:
                continue
            if all(phi[M[g][s]] == M[phi[g]][img[s]] for g in range(n) for s in (x0, y0)):
                auts.append(phi)
    return auts


def closure_idx(gens, M, e):
    S, frontier = {e}, [e]
    while frontier:
        new = []
        for x in frontier:
            for g in gens:
                y = M[x][g]
                if y not in S:
                    S.add(y)
                    new.append(y)
        frontier = new
    return S


def build():
    groups = {}
    for name, (elems, mul) in (("2T", (sl2(3), mmul(3))), ("2O", group_2o()), ("2I", (sl2(5), mmul(5)))):
        M, e, inv = table(elems, mul)
        ords = orders(M, e)
        auts = automorphisms(M, e, inv, ords)
        seen, reps = set(), []
        for g in range(len(M)):
            if g in seen:
                continue
            orb = {phi[g] for phi in auts}
            seen |= orb
            reps.append((g, len(orb)))
        hist = {}
        for o in ords:
            hist[o] = hist.get(o, 0) + 1
        groups[name] = {"M": M, "e": e, "inv": inv, "aut": len(auts), "reps": reps, "hist": dict(sorted(hist.items()))}
    return groups


# ---------------------------------------------------------------- counting surjections
def compile_word(w, gens):
    return [(gens.index(c.lower()), c.isupper()) for c in w]


def count_surj(pres, G):
    M, e, inv = G["M"], G["e"], G["inv"]
    n = len(M)
    gens = pres["generators"]
    k = len(gens)
    rels = [compile_word(r, gens) for r in pres["relators"]]
    total = 0
    for r0, size in G["reps"]:
        good = 0
        for rest in itertools.product(range(n), repeat=k - 1):
            img = (r0,) + rest
            fwd = [(img[i], inv[img[i]]) for i in range(k)]
            ok = True
            for rel in rels:
                p = e
                for i, t in rel:
                    p = M[p][fwd[i][1] if t else fwd[i][0]]
                if p != e:
                    ok = False
                    break
            if ok and len(closure_idx(list(img), M, e)) == n:
                good += 1
        total += size * good
    return Fraction(total, G["aut"])


def rank_mod(rows, p):
    rows = [[x % p for x in r] for r in rows]
    rank, col, ncol = 0, 0, len(rows[0]) if rows else 0
    while rank < len(rows) and col < ncol:
        piv = next((i for i in range(rank, len(rows)) if rows[i][col] % p), None)
        if piv is None:
            col += 1
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        f = pow(rows[rank][col], -1, p)
        rows[rank] = [(x * f) % p for x in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][col]:
                c = rows[i][col]
                rows[i] = [(a - c * b) % p for a, b in zip(rows[i], rows[rank])]
        rank, col = rank + 1, col + 1
    return rank


def plants(pres):
    gens = pres["generators"]
    k = len(gens)
    ex = [[sum((1 if c == g else -1 if c == g.upper() else 0) for c in r) for g in gens] for r in pres["relators"]]
    d3 = k - rank_mod(ex, 3) if ex else k
    d2 = k - rank_mod(ex, 2) if ex else k
    homs3 = sum(1 for v in itertools.product(range(3), repeat=k)
                if all(sum(a * b for a, b in zip(row, v)) % 3 == 0 for row in ex))
    return homs3 - 1 == 3 ** d3 - 1 and d3 >= 1, d2 >= 3


# ---------------------------------------------------------------- the manifold-free steps
def post_e6():
    kern = []
    for a in range(3):
        for b in range(2):
            for k6 in range(6):
                x = Fraction(k6, 6)
                if (Fraction(a, 3) + 2 * x).denominator == 1 and (Fraction(b, 2) - 3 * x).denominator == 1:
                    o = math.lcm(3 // math.gcd(a, 3), 2 // math.gcd(b, 2), x.denominator)
                    kern.append(o)
    z6 = sorted(kern) == [1, 2, 3, 3, 6, 6] and 6 in kern
    # the commutant: X with [X, T] = 0 for T in sl(3) + sl(2) (rational basis) and Tr X = 0
    basis = []
    for blk in ((0, 1, 2), (3, 4)):
        for i in blk:
            for j in blk:
                if i != j:
                    basis.append({(i, j): 1})
        for i, j in zip(blk, blk[1:]):
            basis.append({(i, i): 1, (j, j): -1})
    eqs = []
    for T in basis:
        for r in range(5):
            for c in range(5):
                row = [Fraction(0)] * 25            # ([X, T])_{rc} = sum_m X_rm T_mc - T_rm X_mc
                for (m, cc), v in T.items():
                    if cc == c:
                        row[r * 5 + m] += v
                for (rr, m), v in T.items():
                    if rr == r:
                        row[m * 5 + c] -= v
                eqs.append(row)
    eqs.append([Fraction(1) if i % 6 == 0 else Fraction(0) for i in range(25)])
    null = nullspace(eqs, 25)
    one = len(null) == 1
    if one:
        v = null[0]
        s = v[0] / 2
        com = all(v[i] == 0 for i in range(25) if i % 6) and [v[i * 6] / s for i in range(5)] == [2, 2, 2, -3, -3]
    else:
        com = False
    T3 = [Fraction(0)] * 3 + [Fraction(1, 2), Fraction(-1, 2)]
    Y = [Fraction(-1, 6) * x for x in (2, 2, 2, -3, -3)]
    Q = [a + b for a, b in zip(T3, Y)]
    ratio = sum(x * x for x in T3) / sum(x * x for x in Q)
    return z6, one and com, ratio


def nullspace(rows, n):
    rows = [r[:] for r in rows]
    pivots, rank = [], 0
    for col in range(n):
        piv = next((i for i in range(rank, len(rows)) if rows[i][col] != 0), None)
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        f = rows[rank][col]
        rows[rank] = [x / f for x in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][col] != 0:
                c = rows[i][col]
                rows[i] = [a - c * b for a, b in zip(rows[i], rows[rank])]
        pivots.append(col)
        rank += 1
    free = [c for c in range(n) if c not in pivots]
    out = []
    for f in free:
        v = [Fraction(0)] * n
        v[f] = Fraction(1)
        for r, pc in enumerate(pivots):
            v[pc] = -rows[r][f]
        out.append(v)
    return out


def main():
    data = json.loads(pathlib.Path(__file__).with_name("q0023_presentations.json").read_text(encoding="utf-8"))
    mans = data["manifolds"]
    if CONTROL:   # wrong on purpose: m004's relator altered
        mans = [dict(m, relators=["aaabABBAbb"]) if m["name"] == "m004" else m for m in mans]
    n2 = sum(1 for m in mans if len(m["generators"]) == 2)
    n3 = sum(1 for m in mans if len(m["generators"]) == 3)
    g1 = len(mans) == 1199 and n2 == 1041 and n3 == 158
    say("G1 census: %d manifolds, %d two-generator, %d three-generator: %s" % (len(mans), n2, n3, g1))
    G = build()
    want_hist = {"2T": {1: 1, 2: 1, 3: 8, 4: 6, 6: 8}, "2O": {1: 1, 2: 1, 3: 8, 4: 18, 6: 8, 8: 12},
                 "2I": {1: 1, 2: 1, 3: 20, 4: 30, 5: 24, 6: 20, 10: 24}}
    g2 = all(len(G[k]["M"]) == o and G[k]["hist"] == want_hist[k] and G[k]["aut"] == a
             for k, o, a in (("2T", 24, 24), ("2O", 48, 48), ("2I", 120, 120)))
    say("G2 orders %s, |Aut| %s, element orders as the binary polyhedral groups': %s"
        % ([len(G[k]["M"]) for k in ("2T", "2O", "2I")], [G[k]["aut"] for k in ("2T", "2O", "2I")], g2))
    counts, whole = {}, True
    for m in mans:
        c = tuple(count_surj(m, G[k]) for k in ("2T", "2O", "2I"))
        whole = whole and all(x.denominator == 1 for x in c)
        counts[m["name"]] = tuple(int(x) for x in c)
    nT = sum(1 for c in counts.values() if c[0] > 0)
    nT2 = sum(1 for c in counts.values() if c[0] == 2)
    nO = sum(1 for c in counts.values() if c[1] > 0)
    nI = sum(1 for c in counts.values() if c[2] > 0)
    wantT = 385 if CONTROL else 384    # wrong on purpose in the control
    g3 = (nT, nT2, nO, nI) == (wantT, 304, 362, 609) and counts.get("m004") == (2, 0, 0) and whole
    say("G3 onto 2T: %d (with 2 classes: %d); onto 2O: %d; onto 2I: %d; m004: %s; whole numbers: %s; as the card "
        "says: %s" % (nT, nT2, nO, nI, counts.get("m004"), whole, g3))
    z3, z2 = [], []
    for m in mans:
        a, b = plants(m)
        z3.append(a)
        if len(m["generators"]) == 2:
            z2.append(b)
    g4 = all(z3) and len(z3) == 1199 and not any(z2) and len(z2) == 1041
    say("G4 Z/3 plant holds on %d of %d; (Z/2)^3 plant holds on %d of %d two-generator presentations: %s"
        % (sum(z3), len(z3), sum(z2), len(z2), g4))
    z6, com, ratio = post_e6()
    g5 = z6 and com and ratio == Fraction(3, 8)
    say("G5 kernel Z_6 with orders [1, 2, 3, 3, 6, 6]: %s; commutant spanned by diag(2,2,2,-3,-3): %s; "
        "Tr(T_3^2)/Tr(Q^2) = %s: %s" % (z6, com, ratio, g5))
    verdict = g1 and g2 and g3 and g4 and g5
    if CONTROL:
        print("CONTROL: the checks %s the error made on purpose" % ("caught" if not verdict else "MISSED"))
        return 1 if not verdict else 0
    say("VERDICT: the card holds where this seat checks it (G1-G5): %s" % verdict)
    return 0


if __name__ == "__main__":
    sys.exit(main())
