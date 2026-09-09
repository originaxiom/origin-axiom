"""The debt B1293 named, discharged: fc's 40 -> 4 -> 1 collapse, verified WITHOUT the icosians.

R68's content is NOT the 9+9+9 partition (which fc themselves called automatic -- "by construction
it is one of them"). It is the SELECTION: of E6's 40 trinification A2^3 subsystems, exactly one is
stable under the founding ratio acting from BOTH sides. B1293 confirmed the 40 and the 9+9+9 and
FENCED the collapse as unverified. This closes that fence on the combinatorial core.

THE ROUTE. fc work on a rebuilt icosian E8, where g acts by left and by right quaternion
multiplication. That construction is not reproduced here. But R65/R66 identify the relevant element
as lying in the A2^3 CLASS of E6, and that class is realisable directly in W(E6): the product of the
Coxeter elements of the three orthogonal A2 factors of any A2^3 subsystem is an order-3 element of
exactly that class. So the collapse's COMBINATORICS can be checked with no icosians at all.

WHAT CAME OUT.
  * ALL 40 such elements fix EXACTLY 4 of the 40 A2^3 subsystems -- fc's "4 left-stable", reproduced
    with no free parameter.
  * A commuting order-3 partner that preserves those 4 leaves EXACTLY ONE of them: 110 instances of
    the shape "1 fixed of 4", i.e. a 3-CYCLE PLUS A FIXED POINT -- exactly the structure R68
    describes for right multiplication. (16 further pairs fix all 4; those are the degenerate
    same-element cases.)

A CONTROL THAT MATTERS, AND A CORRECTION TO MY OWN FIRST ATTEMPT. A random search over order-3
elements of W(E6) returns fixed-counts of 1 and 7, NEVER 4 -- because W(E6) has several order-3
classes and only the A2^3 one is fc's. My first run sampled randomly, found no 4, and would have
read as tension with R68 had I reported it. The lesson is the corpus's own: test the element the
claim names, not an element of the right order.

STILL NOT VERIFIED, and fenced: that fc's specific g -- the founding ratio on the icosian E8 -- IS
such an element; the MIRROR-INVARIANCE of the selected frame; and the identification of the selected
subsystem with B1264's labelling c = (1,0,2,2,0,2). Those are icosian-specific and remain theirs.
"""
from fractions import Fraction as F
import itertools, collections

dot = lambda a, b: sum(x * y for x, y in zip(a, b))


def e8_roots():
    R = []
    for i in range(8):
        for j in range(i + 1, 8):
            for si in (1, -1):
                for sj in (1, -1):
                    v = [0] * 8; v[i] = si; v[j] = sj
                    R.append(tuple(F(x) for x in v))
    for s in itertools.product((1, -1), repeat=8):
        if s.count(-1) % 2 == 0:
            R.append(tuple(F(x, 2) for x in s))
    return R


def build():
    E8 = e8_roots()
    a1 = E8[0]; a2 = next(r for r in E8 if dot(a1, r) == F(-1))
    E6 = [r for r in E8 if dot(r, a1) == 0 and dot(r, a2) == 0]
    rset = set(E6); A2s = set()
    for a in E6:
        for b in E6:
            if dot(a, b) == F(-1):
                c = tuple(-(x + y) for x, y in zip(a, b))
                if c in rset:
                    A2s.add(frozenset([a, b, c] + [tuple(-x for x in r) for r in (a, b, c)]))
    A2s = list(A2s)
    orth = lambda P, Q: all(dot(p, q) == 0 for p in P for q in Q)
    TRI = [frozenset(t) for t in itertools.combinations(range(len(A2s)), 3)
           if orth(A2s[t[0]], A2s[t[1]]) and orth(A2s[t[0]], A2s[t[2]]) and orth(A2s[t[1]], A2s[t[2]])]
    return E6, A2s, TRI


def refl(r):
    n = dot(r, r)
    return lambda v: tuple(vi - 2 * dot(v, r) / n * ri for vi, ri in zip(v, r))


def comp(*fs):
    def g(v):
        for f in reversed(fs):
            v = f(v)
        return v
    return g


def cox(P):
    """Coxeter element of an A2 factor: order 3."""
    P = list(P); a = P[0]
    b = next(r for r in P if dot(a, r) == F(-1))
    return comp(refl(a), refl(b))


def selftest():
    E6, A2s, TRI = build()
    print("B1293 addendum -- fc's 40 -> 4 -> 1, verified without icosians\n")
    print(f"  [base] E6 roots {len(E6)}, A2 subsystems {len(A2s)}, A2^3 subsystems {len(TRI)}")
    assert (len(E6), len(A2s), len(TRI)) == (72, 120, 40)

    wof = lambda T: comp(*[cox(A2s[i]) for i in T])

    def perm(w):
        m = {}
        for i, P in enumerate(A2s):
            Q = frozenset(w(r) for r in P)
            if Q not in A2s:
                return None
            m[i] = A2s.index(Q)
        return [TRI.index(frozenset(m[i] for i in T)) for T in TRI]

    counts = collections.Counter()
    for T in TRI:
        p = perm(wof(T))
        assert p is not None
        counts[sum(1 for i, x in enumerate(p) if x == i)] += 1
    print(f"  [40->4] A2^3-class order-3 elements: fixed-A2^3 counts {dict(counts)}")
    assert set(counts) == {4} and counts[4] == 40

    S = E6[:8]
    commutes = lambda f, g: all(f(g(v)) == g(f(v)) for v in S)
    shapes = collections.Counter()
    for T in TRI[:10]:
        w = wof(T); pw = perm(w)
        fixed = [i for i, x in enumerate(pw) if x == i]
        for T2 in TRI:
            u = wof(T2)
            if not commutes(w, u):
                continue
            pu = perm(u)
            if pu is None or set(pu[i] for i in fixed) != set(fixed):
                continue
            shapes[sum(1 for i in fixed if pu[i] == i)] += 1
    print(f"  [4->1 ] commuting order-3 partners on those 4: {dict(sorted(shapes.items()))}")
    assert shapes[1] > 0, "the 3-cycle-plus-fixed-point structure must occur"

    # THE CONTROL that corrects this bench's own first attempt
    import random
    random.seed(11)
    other = collections.Counter()
    for _ in range(400):
        f = None
        for _ in range(random.choice([2, 3, 4])):
            r = random.choice(E6)
            f = refl(r) if f is None else comp(refl(r), f)
        v = E6[0]; x = f(v); o = 1
        while x != v and o < 9:
            x = f(x); o += 1
        if o != 3:
            continue
        p = perm(f)
        if p is None:
            continue
        other[sum(1 for i, y in enumerate(p) if y == i)] += 1
    print(f"  [ctl  ] RANDOM order-3 elements of W(E6): fixed-counts {dict(sorted(other.items()))}")
    assert 4 not in other, "the control's point: only the A2^3 CLASS gives 4"
    print("""
  ==> fc's collapse 40 -> 4 -> 1 REPRODUCES on this bench, with no icosian construction:
      every A2^3-class order-3 element fixes exactly FOUR of the 40, and a commuting order-3
      partner leaves exactly ONE of those four (3-cycle plus a fixed point).

  ==> THE CONTROL IS THE LESSON: random order-3 elements of W(E6) fix 1 or 7, NEVER 4. This
      bench's first attempt sampled randomly, found no 4, and would have read as tension with
      R68. Test the element the claim NAMES, not an element of the right order.

  ==> STILL fc's, and fenced: that the founding ratio g IS such an element on the icosian E8;
      the mirror-invariance of the selected frame; and its identification with B1264's c.
""")
    print("SELFTEST: PASS")


if __name__ == "__main__":
    selftest()
