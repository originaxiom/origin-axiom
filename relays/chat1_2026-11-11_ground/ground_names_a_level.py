#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
WHAT LEVEL DOES A GROUND NAME?   A sealed card: data-free, integers only.

The web seat (chat1), 2026-11-11.  Kind: thread (facts about one history, the ground), bearing on a ruling
about the weave.
A stress test of one sentence on main's record, at the owner's word to the seat: "id love if we can stress
teat some of them", and of the order the seat proposed, "order ok" (2026-11-11; relayed, not confirmed to
main).

THE SENTENCE UNDER TEST
  B1876 section 1: "If the ground is the act itself, there is one: the tick, at level 5."
  B1876 section 4: "If the ground is the act, level 5 is named without ranking and the choice of a ground could
  leave the budget."
  The owner ruled, to main, on 2026-11-11: the tick is an act, and a ground is the act itself (register rows
  P-771 and P-774).  Main holds the route as a postulate and not as a derivation.
  The sentence does not say by which rule a ground has a level.  The record holds two readings for a thread:
    (own lines)  B1733: "The lines A fixes up to sign are the points of coker(A - I) and coker(A + I)", and
                 "a line of exact order N is fixed iff N divides d2(A - I) or d2(A + I)".  P-721 reads the
                 object's own level from the twisted fixed points of the ground's own map, v = -Av.
    (direction)  B1876, H10: the tick's fixed direction is the golden one; the discriminant is 5.
  This card asks what each gives for the tick, for its other side, and for its square, and whether a rule
  with no ranking in it names one level.

CONVENTIONS (those of the seat's earlier fact scripts; the row convention of B1733)
  L = rows (1,0),(1,1);  R = rows (1,1),(0,1);  P = rows (0,1),(1,0) is the bare exchange.
  The tick is F = L.P, its other side is F' = P.F.P.  Vectors are rows and act by v -> v.g.
  A line of order N is a cyclic subgroup of order N of (Z/N)^2; it is kept by g when g carries it to itself.
  A primitive vector v is kept up to sign when v.g = v or v.g = -v modulo N.
  For an integer matrix M of non-zero determinant, d1(M) is the greatest common divisor of its entries and
  d2(M) = |det M| / d1(M).

CELLS
  C0  Controls: F.F = L.R;  F'.F' = R.L;  P.L.P = R;  F' = R.F.R^-1;  det F = det F' = -1;
      v0 = (1,3) has v0.(L.R) = -v0 and v0.F = 3.v0 modulo 5.
  C1  The record's rule of own lines on the four golden grounds F, F', L.R, R.L: d1 and d2 of g - I and g + I.
  C1b The same by brute force: for N = 2..200 the number of primitive vectors kept up to sign.
  C2  Lines kept as sets, for N = 2..200, on the four golden grounds; compared with the number of roots of the
      characteristic polynomial modulo N, counted separately, and with a closed form.
  C3  At N = 5: the orbits of F, of F', of L.R and of R.L on the four non-zero vectors of the line each keeps.
  C4  Every non-negative integer matrix with entries 0..8 and determinant -1: which have d2(g - I) = 1 and
      d2(g + I) = 1, that is, no line of their own at any level.
  C5  REPORTED, NOT PREDICTED.  The seven other histories that B1876 (H6) counts as roots when every history may
      be a ground (traces 4, 5, 6): the same quantities.

PREDICTIONS (each decided by exact comparison of integers)
  P0  Every control of C0 holds.
  P1  F and F': d2(g - I) = 1 and d2(g + I) = 1.  L.R and R.L: d2(g - I) = 1 and (d1, d2)(g + I) = (1, 5).
  P1b For every N in 2..200, F and F' keep no primitive vector up to sign.  L.R and R.L keep four at N = 5 and
      none at any other N.
  P2  For each of F, F', L.R, R.L and every N in 2..200, the number of lines kept equals the number of roots of
      the characteristic polynomial modulo N, and both equal rho(N), where rho is multiplicative with
      rho(5) = 1, rho(5^a) = 0 for a >= 2, rho(p^a) = 2 for a prime p = 1 or 4 modulo 5, and 0 for every
      other prime power.  So exactly one line is kept at N = 5 and at no other N in the range.
  P3  At N = 5, F and F' act on the four non-zero vectors of their line in one orbit of length 4.
      L.R and R.L act in two orbits of length 2.
  P4  In C4 the matrices with no line of their own at any level are exactly F and F'.

WHAT EACH OUTCOME MEANS (written before the run)
  If P1 and P1b hold: under the record's rule of own lines, and under P-721's twisted fixed points, the tick
  has no line and no level.  Its square has the line of order 5.
  If P2 holds: a rule with no ranking in it, "the level at which the ground keeps exactly one line", names 5
  and only 5 in the range, for the tick and for its square alike.
  If P3 holds: what the tick keeps at that level is the whole line, both twins as one datum, and never one
  twin up to sign.  Its square keeps each twin.
  If P4 holds: among the histories with an odd number of ticks in that range, the tick is the only one with
  no line of its own.
  Taken together they would say: "the tick, at level 5, with nothing ranked" holds under the second reading and
  not under the first; the postulate needs a clause that says which; and with that clause the mark is both
  twins.  If P2 fails, no such rule names one level and the sentence is not supported by this card.
  Nothing here says that a ground must be the act, or that the level is physical.  It selects no value.

SEEN FIRST (swept from main at 015be0cc7; each line is cut before its list of other lanes)
  VERDICT topic-sweep /named without ranking|without a ranking|a ground is|the act itself|ground itself|root class/ (full text): 4 of 1624 arcs on main match (NEGATIVE 1, PROVED 3); 4 register rows match (DONE 2, QUEUED 2)
  VERDICT topic-sweep /twisted fixed point|coker\(|cokernel|det\(A \+ I\)|det\(LR \+ I\)|object-native level/ (full text): 24 of 1624 arcs on main match (NEGATIVE 4, PROVED 20); 4 register rows match (DONE 2, QUEUED 2)
  VERDICT topic-sweep /keeps no vector|multiplies the mark|tick multiplies|no vector up to sign|golden fixed direction|has the golden one/ (full text): 3 of 1624 arcs on main match (PROVED 3); 0 register rows match (none)
  VERDICT topic-sweep /selection criterion|criterion of selection|choice of a ground|choice of the ground|ground could leave|leave the budget/ (full text): 6 of 1624 arcs on main match (PROVED 6); 3 register rows match (DONE 1, QUEUED 2)
  VERDICT topic-sweep /exactly one (invariant |fixed |flat )?line|keeps exactly one|single invariant line|unique invariant line|one line and no other|only invariant line/ (full text): 2 of 1624 arcs on main match (NEGATIVE 1, PROVED 1); 0 register rows match (none)
  VERDICT topic-sweep /level of the tick|tick.s level|level of the ground|ground.s level|level a ground|names? a level|level is named/ (full text): 0 of 1624 arcs on main match (none); 0 register rows match (none)
  On record already: the rule of own lines and the pair {v, 2v} (B1733); that a symmetry reversing the
  orientation exchanges the pair (B1733 section 2); that the tick multiplies the mark by 3 and keeps no vector
  up to sign at level 5 (B1876, H13); the four atoms and F.F = L.R (B1323, B1876 H1); the discriminants 0, 0, 5, 5
  (B1876, H10); the cokernel of L.R + I (the seat's relay under P-721).  Not found on record: the rule of own
  lines applied to the tick at every level; a rule that reads a level from a ground; the count of lines kept as
  sets across levels.

DISCLOSED
  Worked by hand before the seal, and the predictions rest on it: det(F + I) = 1 and det(F - I) = -1;
  det(L.R + I) = 5; the roots of x^2 - x - 1 and of x^2 - 3x + 1 modulo 5 and 25; that F' = R.F.R^-1; and, for
  C5, the first history of each of the traces 4, 5 and 6 modulo 2, 3, 4, 7, 8 and 9.  That hand work suggested
  that L.L.R keeps exactly one line at 2, 3 and 6, L.L.L.R at 3, 7 and 21, and L.L.L.L.R at 2.  C5 is reported
  and not predicted for that reason.
  Nothing was run before the seal.  The script was parsed for its syntax only.
  The range 2..200 and the bound 8 are choices of the card.  The bound 8 is that of B1876, H1.
"""
import sys
from math import gcd

NMAX = 200
BOUND = 8

L = ((1, 0), (1, 1))
R = ((1, 1), (0, 1))
P = ((0, 1), (1, 0))
I2 = ((1, 0), (0, 1))


def mul(a, b):
    return ((a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]),
            (a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]))


def det(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def tr(a):
    return a[0][0] + a[1][1]


def shift(a, s):
    """a + s.I"""
    return ((a[0][0] + s, a[0][1]), (a[1][0], a[1][1] + s))


F = mul(L, P)
FP = mul(mul(P, F), P)
ATOM = {'L': L, 'R': R, 'F': F, 'f': FP}


def word(s):
    m = I2
    for ch in s:
        m = mul(m, ATOM[ch])
    return m


def smith(m):
    """(d1, d2) for a 2x2 integer matrix; d2 = 0 when the determinant is 0."""
    g = gcd(gcd(abs(m[0][0]), abs(m[0][1])), gcd(abs(m[1][0]), abs(m[1][1])))
    d = abs(det(m))
    if d == 0:
        return (g, 0)
    return (g, d // g)


def act(v, g, n):
    return ((v[0] * g[0][0] + v[1] * g[1][0]) % n, (v[0] * g[0][1] + v[1] * g[1][1]) % n)


def primitive(n):
    out = []
    for a in range(n):
        for b in range(n):
            if gcd(gcd(a, b), n) == 1:
                out.append((a, b))
    return out


def factor(n):
    f = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            f[p] = f.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def phi(n):
    r = n
    for p in factor(n):
        r = r // p * (p - 1)
    return r


def rho(n):
    r = 1
    for p, a in factor(n).items():
        if p == 5:
            r *= 1 if a == 1 else 0
        elif p % 5 in (1, 4):
            r *= 2
        else:
            r *= 0
    return r


def roots(g, n):
    t, d = tr(g), det(g)
    return sum(1 for x in range(n) if (x * x - t * x + d) % n == 0)


def counts(g, n, prim, ph):
    """(number of lines kept as sets, number of primitive vectors kept up to sign)"""
    nl = 0
    ns = 0
    for v in prim:
        w = act(v, g, n)
        if (v[0] * w[1] - v[1] * w[0]) % n == 0:
            nl += 1
        if w == v or w == ((-v[0]) % n, (-v[1]) % n):
            ns += 1
    if nl % ph != 0:
        raise SystemExit('lines: count not a multiple of phi at N = %d' % n)
    return nl // ph, ns


def orbit_lengths(g, v0, n):
    """orbit lengths of g on the non-zero multiples of v0 modulo the prime n"""
    todo = [((c * v0[0]) % n, (c * v0[1]) % n) for c in range(1, n)]
    seen = set()
    out = []
    for v in todo:
        if v in seen:
            continue
        k = 0
        w = v
        while w not in seen:
            seen.add(w)
            w = act(w, g, n)
            k += 1
        out.append(k)
    return sorted(out)


def line_of(g, n):
    """the primitive vectors v modulo n with v.g a unit multiple of v, as a sorted list"""
    out = []
    for v in primitive(n):
        w = act(v, g, n)
        if (v[0] * w[1] - v[1] * w[0]) % n == 0:
            out.append(v)
    return out


RESULTS = []


def verdict(name, ok, note=''):
    RESULTS.append((name, bool(ok)))
    print('%s: %s%s' % (name, 'HOLDS' if ok else 'FAILS', (' -- ' + note) if note else ''))


def main():
    print('WHAT LEVEL DOES A GROUND NAME?  N = 2..%d; entries to %d' % (NMAX, BOUND))
    print()
    LR = mul(L, R)
    RL = mul(R, L)
    golden = [('F', F), ("F'", FP), ('L.R', LR), ('R.L', RL)]

    # ---------------------------------------------------------------- C0
    print('C0  controls')
    Rinv = ((1, -1), (0, 1))
    c = []
    c.append(('F.F = L.R', mul(F, F) == LR))
    c.append(("F'.F' = R.L", mul(FP, FP) == RL))
    c.append(('P.L.P = R', mul(mul(P, L), P) == R))
    c.append(("F' = R.F.R^-1", mul(mul(R, F), Rinv) == FP and mul(R, Rinv) == I2))
    c.append(("det F = det F' = -1", det(F) == -1 and det(FP) == -1))
    v0 = (1, 3)
    c.append(('v0.(L.R) = -v0 mod 5', act(v0, LR, 5) == ((-v0[0]) % 5, (-v0[1]) % 5)))
    c.append(('v0.F = 3.v0 mod 5', act(v0, F, 5) == ((3 * v0[0]) % 5, (3 * v0[1]) % 5)))
    for name, ok in c:
        print('    %-24s %s' % (name, ok))
    print('    F = %s   F\' = %s   L.R = %s   R.L = %s' % (F, FP, LR, RL))
    verdict('P0', all(ok for _, ok in c))
    print()

    # ---------------------------------------------------------------- C1
    print('C1  the rule of own lines: (d1, d2) of g - I and of g + I; trace, determinant, discriminant')
    ok1 = True
    for name, g in golden:
        sm, sp = smith(shift(g, -1)), smith(shift(g, 1))
        disc = tr(g) ** 2 - 4 * det(g)
        print('    %-4s tr %d det %+d disc %d   g - I: %s   g + I: %s' % (name, tr(g), det(g), disc, sm, sp))
        if name in ('F', "F'"):
            ok1 = ok1 and sm[1] == 1 and sp[1] == 1
        else:
            ok1 = ok1 and sm[1] == 1 and sp == (1, 5)
    verdict('P1', ok1)
    print()

    # ---------------------------------------------------------------- C1b, C2
    print('C1b, C2  for N = 2..%d: vectors kept up to sign; lines kept as sets; roots; rho' % NMAX)
    kept_sign = dict((name, {}) for name, _ in golden)
    kept_line = dict((name, {}) for name, _ in golden)
    ok2 = True
    bad2 = []
    for n in range(2, NMAX + 1):
        prim = primitive(n)
        ph = phi(n)
        r = rho(n)
        for name, g in golden:
            nl, ns = counts(g, n, prim, ph)
            kept_line[name][n] = nl
            kept_sign[name][n] = ns
            rt = roots(g, n)
            if not (nl == rt == r):
                ok2 = False
                bad2.append((name, n, nl, rt, r))
    ok1b = True
    for name, _ in golden:
        nz = sorted((n, k) for n, k in kept_sign[name].items() if k)
        print('    %-4s vectors kept up to sign, as (N, number): %s' % (name, nz if nz else 'none at any N'))
        if name in ('F', "F'"):
            ok1b = ok1b and nz == []
        else:
            ok1b = ok1b and nz == [(5, 4)]
    verdict('P1b', ok1b)
    for name, _ in golden:
        nz = sorted((n, k) for n, k in kept_line[name].items() if k)
        ones = [n for n, k in nz if k == 1]
        print('    %-4s lines kept, as (N, number): %s' % (name, nz))
        print('    %-4s exactly one line at N = %s' % (name, ones))
    same = all(kept_line[name] == kept_line['F'] for name, _ in golden)
    print('    the four grounds keep the same number of lines at every N: %s' % same)
    if bad2:
        print('    mismatches (ground, N, lines, roots, rho): %s' % bad2[:20])
    only5 = all([n for n, k in kept_line[name].items() if k == 1] == [5] for name, _ in golden)
    verdict('P2', ok2 and only5, 'lines = roots = rho at every N: %s; exactly one line only at 5: %s' % (ok2, only5))
    print()

    # ---------------------------------------------------------------- C3
    print('C3  at N = 5: the line each ground keeps, and the orbits on its four non-zero vectors')
    ok3 = True
    for name, g in golden:
        ln = line_of(g, 5)
        ol = orbit_lengths(g, ln[0], 5) if ln else []
        print('    %-4s line %s   orbit lengths %s' % (name, ln, ol))
        if name in ('F', "F'"):
            ok3 = ok3 and len(ln) == 4 and ol == [4]
        else:
            ok3 = ok3 and len(ln) == 4 and ol == [2, 2]
    verdict('P3', ok3)
    print()

    # ---------------------------------------------------------------- C4
    print('C4  non-negative matrices with entries 0..%d' % BOUND)
    n_pm = 0
    n_minus = 0
    none = []
    by_trace = {}
    rng = range(BOUND + 1)
    for a in rng:
        for b in rng:
            for cc in rng:
                for d in rng:
                    g = ((a, b), (cc, d))
                    dg = det(g)
                    if dg in (1, -1):
                        n_pm += 1
                    if dg != -1:
                        continue
                    n_minus += 1
                    sm, sp = smith(shift(g, -1)), smith(shift(g, 1))
                    by_trace.setdefault(tr(g), []).append((sm, sp))
                    if sm[1] == 1 and sp[1] == 1:
                        none.append(g)
    print('    determinant +1 or -1: %d matrices (B1876, H1 has 174); determinant -1: %d' % (n_pm, n_minus))
    for t in sorted(by_trace)[:6]:
        ex = sorted(set(by_trace[t]))
        print('    trace %d: %d matrices; (d1,d2)(g - I), (d1,d2)(g + I) occurring: %s' % (t, len(by_trace[t]), ex[:6]))
    print('    with no line of their own at any level: %s' % none)
    verdict('P4', sorted(none) == sorted([F, FP]))
    print()

    # ---------------------------------------------------------------- C5
    print('C5  REPORTED, NOT PREDICTED: the other root histories of B1876, H6')
    others = ['LLR', 'LRR', 'LLLR', 'LRRR', 'LLLLR', 'LRRRR', 'LLRR']
    data = dict((w, {'one': [], 'sign': []}) for w in others)
    mats = dict((w, word(w)) for w in others)
    for n in range(2, NMAX + 1):
        prim = primitive(n)
        ph = phi(n)
        for w in others:
            nl, ns = counts(mats[w], n, prim, ph)
            if nl == 1:
                data[w]['one'].append(n)
            if ns:
                data[w]['sign'].append((n, ns))
    for w in others:
        g = mats[w]
        disc = tr(g) ** 2 - 4 * det(g)
        print('    %-6s tr %d disc %d   g - I: %s   g + I: %s' % (w, tr(g), disc, smith(shift(g, -1)), smith(shift(g, 1))))
        print('           exactly one line at N = %s' % data[w]['one'])
        print('           vectors kept up to sign, as (N, number): %s' % data[w]['sign'])
    print()

    held = sum(1 for _, ok in RESULTS if ok)
    print('PREDICTIONS: %d of %d hold  (%s)' % (held, len(RESULTS), ', '.join('%s %s' % (n, 'holds' if ok else 'FAILS') for n, ok in RESULTS)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
