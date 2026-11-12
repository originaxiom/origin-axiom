#!/usr/bin/env python3
"""WP-1.2, first step, on main's own code: what excludes the abelian carrier, what does not exclude a nilpotent one,
which surface is left, and which prime a single sector keeps.

Everything is exact: reduced words in the free group on a, b; integer and Gaussian-integer matrices; exponents of a
root of unity as integers mod p.  No number is measured and none is compared with data.

THE STATEMENTS CHECKED
  A. NATURALITY DOES NOT DECIDE.  The abelian quotient q: F_2 -> Z^2 commutes with every move (q o phi = phi_ab o q),
     so no argument from naturality can prefer F_2 to Z^2.
  B. THE REMAINDER DECIDES AGAINST Z^2.  Through Z^2 the commutator [a, b] is the identity, so its trace in any
     representation to SL(2) is +2; the quaternion point has trace -2.  The moves keep the class of [a, b]
     (orientation-preserving moves) or send it to the class of its inverse (the swap, the tick).
  C. THE REMAINDER DOES NOT DECIDE FOR F_2.  The quaternion point factors through the quaternion group and through the
     integral Heisenberg group F_2 / gamma_3: there [a, b] is not the identity and every triple commutator is.  In a
     faithful copy of F_2 the triple commutator [[a, b], a] is not the identity.
  D. THE SURFACE.  The compact surfaces with free fundamental group of rank two are four.  On one of them only is
     every boundary curve in the commutator subgroup: the once-punctured torus, whose boundary is [a, b].  A word
     outside the commutator subgroup is conjugate to no power of [a, b] in any free basis.
  E. THE PRIME OF ONE SECTOR.  In the Heisenberg (clock and shift) representation of dimension p the commutator is the
     scalar zeta^k; the swap and the tick send it to zeta^-k.  One irreducible sector is carried to itself only when
     zeta^k = zeta^-k, which among primes happens at p = 2 alone; the sum of a sector and its conjugate is carried to
     itself for every p.

HOW EACH COULD FAIL is in the planted section: a move that is not an automorphism, a boundary word changed, a
commutator computed in the wrong order, a prime at which the scalar is real.

    python3 carrier_and_prime_on_main.py          # prints every check; exit 1 if one fails
"""
import itertools, json, pathlib, sys
from fractions import Fraction

HERE = pathlib.Path(__file__).resolve().parent
CHECKS, FAILS = [], []


def check(name, ok, detail=""):
    CHECKS.append({"check": name, "holds": bool(ok), "detail": detail})
    if not ok:
        FAILS.append(name)
    print("%s  %s%s" % ("ok  " if ok else "FAIL", name, ("  [%s]" % detail) if detail else ""))


# ------------------------------------------------------------------------------------------ the free group on a, b
def reduce(w):
    out = []
    for g, e in w:
        if out and out[-1][0] == g and out[-1][1] == -e:
            out.pop()
        else:
            out.append((g, e))
    return tuple(out)


def W(s):
    """'abAB' -> a b a^-1 b^-1 (a capital letter is an inverse)"""
    return reduce(tuple((ch.lower(), 1 if ch.islower() else -1) for ch in s))


def mul(*ws):
    return reduce(tuple(x for w in ws for x in w))


def inv(w):
    return tuple((g, -e) for g, e in reversed(w))


def comm(x, y):
    return mul(x, y, inv(x), inv(y))


def power(w, k):
    return mul(*([w] * k)) if k >= 0 else mul(*([inv(w)] * (-k)))


def apply(phi, w):
    """phi = {'a': word, 'b': word}; the image of w"""
    return mul(*[(phi[g] if e == 1 else inv(phi[g])) for g, e in w])


def cyc(w):
    """the conjugacy class of w: its cyclically reduced form, least over rotations"""
    w = list(w)
    while len(w) >= 2 and w[0][0] == w[-1][0] and w[0][1] == -w[-1][1]:
        w = w[1:-1]
    return min(tuple(w[i:] + w[:i]) for i in range(len(w))) if w else ()


def ab(w):
    return (sum(e for g, e in w if g == "a"), sum(e for g, e in w if g == "b"))


A, B = W("a"), W("b")
K = comm(A, B)                                             # [a, b] = a b a^-1 b^-1
MOVES = {                                                   # the record's moves and the two that reverse orientation
    "a -> ab": {"a": W("ab"), "b": B}, "a -> ba": {"a": W("ba"), "b": B},
    "b -> ba": {"a": A, "b": W("ba")}, "b -> ab": {"a": A, "b": W("ab")},
    "the swap (a, b) -> (b, a)": {"a": B, "b": A},
    "the tick (a, b) -> (ab, a)": {"a": W("ab"), "b": A},
}
PRESERVING = ["a -> ab", "a -> ba", "b -> ba", "b -> ab"]
REVERSING = ["the swap (a, b) -> (b, a)", "the tick (a, b) -> (ab, a)"]


def is_automorphism(phi):
    """a pair of words is a free basis exactly when it carries [a, b] to a conjugate of [a, b] or of its inverse (Nielsen)"""
    return cyc(comm(phi["a"], phi["b"])) in (cyc(K), cyc(inv(K)))


def words(maxlen):
    for n in range(1, maxlen + 1):
        for s in itertools.product("abAB", repeat=n):
            w = W("".join(s))
            if len(w) == n:
                yield w


# ------------------------------------------------------------------------------------------------------- A and B
def part_A_and_B():
    for name, phi in MOVES.items():
        check("%s is an automorphism" % name, is_automorphism(phi))
    ws = list(words(6))
    for name, phi in MOVES.items():
        m = (ab(phi["a"]), ab(phi["b"]))                    # the induced map on Z^2: columns are the images of a and b
        nat = all(ab(apply(phi, w)) == (ab(w)[0] * m[0][0] + ab(w)[1] * m[1][0], ab(w)[0] * m[0][1] + ab(w)[1] * m[1][1]) for w in ws)
        check("A: the abelian quotient commutes with %s" % name, nat, "%d words to length 6" % len(ws))
    check("B: [a, b] is the identity in Z^2", ab(K) == (0, 0))
    for name in PRESERVING:
        check("B: %s keeps the class of [a, b]" % name, cyc(apply(MOVES[name], K)) == cyc(K))
    for name in REVERSING:
        check("B: %s sends [a, b] to the class of its inverse" % name, cyc(apply(MOVES[name], K)) == cyc(inv(K)) != cyc(K))
    # which classes of length at most 8 do the four preserving moves keep?  only powers of [a, b]
    kept = sorted({cyc(w) for w in words(8) if all(cyc(apply(MOVES[n], w)) == cyc(w) for n in PRESERVING)}, key=len)
    powers = {cyc(power(K, k)) for k in (-2, -1, 1, 2)}
    check("B: the classes to length 8 that the four record moves keep are powers of [a, b]", set(kept) <= powers and len(kept) >= 2,
          "%d classes kept, lengths %s" % (len(kept), sorted({len(c) for c in kept})))


# ------------------------------------------------------------------------------------------------- matrices, exact
def mat_mul(x, y):
    n = len(x)
    return tuple(tuple(sum(x[i][k] * y[k][j] for k in range(n)) for j in range(n)) for i in range(n))


def mat_id(n):
    return tuple(tuple(1 if i == j else 0 for j in range(n)) for i in range(n))


def mat_inv2(x):
    (p, q), (r, s) = x
    d = p * s - q * r
    assert d == 1
    return ((s, -q), (-r, p))


def rep(images, inverses, w):
    n = len(images["a"]); out = mat_id(n)
    for g, e in w:
        out = mat_mul(out, images[g] if e == 1 else inverses[g])
    return out


def trace(x):
    return sum(x[i][i] for i in range(len(x)))


def part_C():
    I = complex(0, 1)
    # the quaternion point: a -> diag(i, -i), b -> [[0, 1], [-1, 0]]
    qa, qb = ((I, 0), (0, -I)), ((0, 1), (-1, 0))
    Q = {"a": qa, "b": qb}; Qi = {"a": mat_inv2(qa), "b": mat_inv2(qb)}
    check("C: at the quaternion point the three traces are 0, 0, 0", (trace(qa), trace(qb), trace(mat_mul(qa, qb))) == (0, 0, 0))
    check("C: at the quaternion point tr[a, b] = -2", trace(rep(Q, Qi, K)) == -2 and rep(Q, Qi, K) == ((-1, 0), (0, -1)))
    kappa = lambda x, y, z: x * x + y * y + z * z - x * y * z - 2          # Fricke: tr[a, b] from (tr a, tr b, tr ab)
    check("C: Fricke's polynomial gives -2 at (0, 0, 0) and +2 at the trivial point (2, 2, 2)", (kappa(0, 0, 0), kappa(2, 2, 2)) == (-2, 2))
    check("C: Fricke's polynomial agrees with the matrices at the quaternion point and at a faithful pair",
          kappa(trace(qa), trace(qb), trace(mat_mul(qa, qb))) == trace(rep(Q, Qi, K))
          and kappa(2, 2, trace(mat_mul(((1, 2), (0, 1)), ((1, 0), (2, 1))))) == trace(rep({"a": ((1, 2), (0, 1)), "b": ((1, 0), (2, 1))},
                                                                                         {"a": ((1, -2), (0, 1)), "b": ((1, 0), (-2, 1))}, K)))
    triple = [comm(K, A), comm(K, B), comm(K, inv(A)), comm(K, inv(B))]
    check("C: at the quaternion point every triple commutator is the identity", all(rep(Q, Qi, t) == mat_id(2) for t in triple))
    # an abelian pair: any two commuting matrices give [a, b] = 1; shown on a family of diagonal and of unipotent pairs
    ok = True
    for x, y in itertools.product(range(1, 5), repeat=2):
        d1, d2 = ((Fraction(x), 0), (0, Fraction(1, x))), ((Fraction(y), 0), (0, Fraction(1, y)))
        u1, u2 = ((1, x), (0, 1)), ((1, y), (0, 1))
        for p, q in ((d1, d2), (u1, u2)):
            R = {"a": p, "b": q}; Ri = {"a": mat_inv2(p), "b": mat_inv2(q)}
            ok = ok and trace(rep(R, Ri, K)) == 2
    check("C: through a commuting pair tr[a, b] = +2", ok, "32 pairs, a control of the reader: for any commuting pair [a, b] maps to the identity")
    # the integral Heisenberg group: a -> 1 + E12, b -> 1 + E23
    ha, hb = ((1, 1, 0), (0, 1, 0), (0, 0, 1)), ((1, 0, 0), (0, 1, 1), (0, 0, 1))
    hai, hbi = ((1, -1, 0), (0, 1, 0), (0, 0, 1)), ((1, 0, 0), (0, 1, -1), (0, 0, 1))
    H = {"a": ha, "b": hb}; Hi = {"a": hai, "b": hbi}
    check("C: in the Heisenberg group [a, b] is not the identity", rep(H, Hi, K) == ((1, 0, 1), (0, 1, 0), (0, 0, 1)))
    check("C: in the Heisenberg group every triple commutator is the identity", all(rep(H, Hi, t) == mat_id(3) for t in triple))
    # every word the Heisenberg group kills, the quaternion point kills: checked on all words to length 8
    n_killed, bad = 0, 0
    for w in words(8):
        if rep(H, Hi, w) == mat_id(3):
            n_killed += 1
            if rep(Q, Qi, w) != mat_id(2):
                bad += 1
    check("C: every word to length 8 that is trivial in the Heisenberg group is trivial at the quaternion point", bad == 0 and n_killed > 0,
          "%d such words" % n_killed)
    # a faithful copy of F_2 (Sanov): a -> [[1, 2], [0, 1]], b -> [[1, 0], [2, 1]]
    sa, sb = ((1, 2), (0, 1)), ((1, 0), (2, 1))
    S = {"a": sa, "b": sb}; Si = {"a": mat_inv2(sa), "b": mat_inv2(sb)}
    check("C: in a faithful copy of F_2 the triple commutator [[a, b], a] is not the identity", rep(S, Si, comm(K, A)) != mat_id(2))
    faithful = all(rep(S, Si, w) != mat_id(2) for w in words(8))
    check("C: no reduced word to length 8 is trivial in that copy", faithful)


# ------------------------------------------------------------------------------------------------------------- D
def surfaces():
    """the compact surfaces with boundary whose fundamental group is free of rank two: Euler characteristic -1.
    orientable of genus g with b boundary curves: 2 - 2g - b = -1; non-orientable with k crosscaps: 2 - k - b = -1."""
    out = []
    for g in range(0, 3):
        for b in range(1, 6):
            if 2 - 2 * g - b == -1:
                out.append(("orientable", g, b))
    for k in range(1, 4):
        for b in range(1, 6):
            if 2 - k - b == -1:
                out.append(("non-orientable", k, b))
    return out


BOUNDARY = {                                                # the boundary curves as words in a free basis of the fundamental group
    ("orientable", 1, 1): [K],                              # the once-punctured torus: [a, b]
    ("orientable", 0, 3): [A, B, inv(W("ab"))],             # the pair of pants: a, b, (ab)^-1
    ("non-orientable", 1, 2): [B, inv(W("aab"))],           # a^2 c1 c2 = 1 with c1 = b: the curves b and (a^2 b)^-1
    ("non-orientable", 2, 1): [inv(W("aabb"))],             # a^2 b^2 c = 1: the curve (a^2 b^2)^-1
}


def part_D(boundary=BOUNDARY, label=""):
    S = surfaces()
    check("D%s: four compact surfaces have a free fundamental group of rank two" % label, len(S) == 4 and set(S) == set(boundary), str(S))
    null = [s for s in S if all(ab(w) == (0, 0) for w in boundary[s])]
    check("D%s: every boundary curve is in the commutator subgroup on one surface only, the once-punctured torus" % label,
          null == [("orientable", 1, 1)], str(null))
    # the relation each presentation must satisfy: the product of the boundary curves with the handles or crosscaps is trivial
    rel = {("orientable", 1, 1): mul(K, inv(boundary[("orientable", 1, 1)][0])),
           ("orientable", 0, 3): mul(*boundary[("orientable", 0, 3)]),
           ("non-orientable", 1, 2): mul(W("aa"), *boundary[("non-orientable", 1, 2)]),
           ("non-orientable", 2, 1): mul(W("aabb"), *boundary[("non-orientable", 2, 1)])}
    check("D%s: each list of boundary curves satisfies its surface's relation" % label, all(r == () for r in rel.values()))
    # THE ARGUMENT THAT NEEDS NO COMMUTATOR.  A homeomorphism permutes the boundary curves, so the homology classes of a
    # surface's boundary curves (with their negatives) are a FINITE set carried to itself by every move.  A non-zero
    # vector of Z^2 has an infinite orbit under the two transvections; shown here by the orbit's growth.
    T1 = lambda v: (v[0] + v[1], v[1]); T2 = lambda v: (v[0], v[0] + v[1])
    def orbit_size(v, steps):
        seen, frontier = {v}, [v]
        for _ in range(steps):
            frontier = [w for u in frontier for w in (T1(u), T2(u)) if w not in seen and not seen.add(w)]
        return len(seen)
    grow = {}
    for s in S:
        for w in boundary[s]:
            v = ab(w)
            grow[(s, v)] = (orbit_size(v, 6), orbit_size(v, 12))
    check("D%s: the homology class of a boundary curve has a finite orbit under the moves only when it is zero" % label,
          all((a == b == 1) == (v == (0, 0)) and (v == (0, 0) or b > a) for (s, v), (a, b) in grow.items()),
          "; ".join("%s %s: %d then %d" % (s[0][:3] + str(s[1:]), v, a, b) for (s, v), (a, b) in sorted(grow.items())))
    return null


# ------------------------------------------------------------------------------------------------------------- E
def heisenberg(p):
    """the clock and shift in dimension p, entries as exponents of zeta: a matrix is a dict (i, j) -> k meaning zeta^k
    (an absent entry is 0).  X: e_j -> e_{j+1};  Z: e_j -> zeta^j e_j."""
    X = {((j + 1) % p, j): 0 for j in range(p)}
    Z = {(j, j): j % p for j in range(p)}
    return X, Z


def mono_mul(x, y, p):
    out = {}
    for (i, k), e1 in x.items():
        for (k2, j), e2 in y.items():
            if k == k2:
                assert (i, j) not in out
                out[(i, j)] = (e1 + e2) % p
    return out


def mono_inv(x, p):
    return {(j, i): (-e) % p for (i, j), e in x.items()}


def mono_rep(images, w, p):
    out = {(j, j): 0 for j in range(p)}
    for g, e in w:
        out = mono_mul(out, images[g] if e == 1 else mono_inv(images[g], p), p)
    return out


def scalar(x, p):
    """k if the matrix is zeta^k times the identity, else None"""
    if set(x) == {(j, j) for j in range(p)} and len(set(x.values())) == 1:
        return next(iter(x.values()))
    return None


def one_sector_kept(p, moves):
    """is the sector's scalar the same after each of the given moves?"""
    X, Z = heisenberg(p); R = {"a": X, "b": Z}
    k = scalar(mono_rep(R, K, p), p)
    return all(scalar(mono_rep(R, apply(MOVES[n], K), p), p) == k for n in moves)


def part_E(primes=(2, 3, 5, 7, 11, 13)):
    res = {}
    for p in primes:
        X, Z = heisenberg(p); R = {"a": X, "b": Z}
        k = scalar(mono_rep(R, K, p), p)
        after = {name: scalar(mono_rep(R, apply(MOVES[name], K), p), p) for name in MOVES}
        res[p] = {"the commutator is zeta to the": k, "after each move": after}
        check("E: at p = %d the commutator is a scalar zeta^k with k not 0" % p, k is not None and k % p != 0, "k = %s" % k)
        check("E: at p = %d the four record moves keep the scalar" % p, all(after[n] == k for n in PRESERVING))
        check("E: at p = %d the swap and the tick send zeta^k to zeta^-k" % p, all(after[n] == (-k) % p for n in REVERSING))
        fixed = one_sector_kept(p, REVERSING)
        check("E: at p = %d one sector is carried to itself by the swap and the tick: %s" % (p, "yes" if p == 2 else "no"), fixed == (p == 2))
        # the sum of the sector and its conjugate: the pair {k, -k} is carried to itself
        check("E: at p = %d the sector and its conjugate together are carried to themselves" % p,
              all({after[n], (-after[n]) % p} == {k, (-k) % p} for n in MOVES))
    return res


# ------------------------------------------------------------------------------------------------------- planted
def planted():
    out = {}
    # 1. a pair of words that is not a free basis must be refused
    out["a pair that is not a basis is refused"] = not is_automorphism({"a": W("aa"), "b": B})
    # 2. a boundary word changed: the pair of pants given a commutator for one of its curves breaks its relation
    bad = dict(BOUNDARY); bad[("orientable", 0, 3)] = [K, B, inv(W("ab"))]
    rel = mul(*bad[("orientable", 0, 3)])
    out["a changed boundary word breaks the surface's relation"] = rel != ()
    # 3. the commutator in the other order is the inverse class, not the class
    out["[b, a] is not in the class of [a, b]"] = cyc(comm(B, A)) != cyc(K)
    # 4. the verdict on one sector depends on the moves it is asked about: asked about the record moves alone, which keep
    #    orientation, every prime would be kept, and the conclusion "2 alone" would be lost
    out["asked about the record moves alone, the sector at 3 is kept: the verdict comes from the swap and the tick"] = \
        one_sector_kept(3, PRESERVING) and not one_sector_kept(3, REVERSING)
    # 5. the Heisenberg group is not abelian: a b a^-1 is not b
    ha, hb = ((1, 1, 0), (0, 1, 0), (0, 0, 1)), ((1, 0, 0), (0, 1, 1), (0, 0, 1))
    out["in the Heisenberg group a and b do not commute"] = mat_mul(mat_mul(ha, hb), ((1, -1, 0), (0, 1, 0), (0, 0, 1))) != hb
    # 6. a surface given a boundary curve that is a commutator would be counted with the torus: the census reads the words
    bad2 = dict(BOUNDARY); bad2[("non-orientable", 2, 1)] = [K]
    out["a planted commutator as the Klein bottle's boundary is counted: the census reads the words it is given"] = \
        [s for s in surfaces() if all(ab(w) == (0, 0) for w in bad2[s])] == [("orientable", 1, 1), ("non-orientable", 2, 1)]
    for k, v in out.items():
        check("planted: " + k, v)
    return out


if __name__ == "__main__":
    part_A_and_B(); part_C(); part_D(); E = part_E(); P = planted()
    res = {"checks": CHECKS, "failing": FAILS, "count": len(CHECKS), "E": {str(p): v for p, v in E.items()}}
    (HERE / "carrier_and_prime_on_main.json").write_text(json.dumps(res, indent=1) + "\n", encoding="utf-8")
    print("\n%d checks, %d failing" % (len(CHECKS), len(FAILS)))
    sys.exit(1 if FAILS else 0)
