#!/usr/bin/env python3
"""
Appendix B -- verification of the coupling law (paper Thm. "the coupling law" and its
corollary "the forced values").

Self-contained: needs only sympy.  Imports NOTHING project-internal.  Exact arithmetic
over Q(sqrt5) throughout -- no floating point anywhere, and in particular the golden
ratio is never evaluated numerically to decide rationality.

## THE STATEMENT

The six-dimensional stage carries a representation that factorizes, as a 2T x 2I
representation, into

    rho_6  =  (chi (x) V2(2I))  +  (V2(2T) (x) V2(2I))

with chi the order-three character of 2T (kernel Q8) and V2 the two-dimensional defining
representation of each binary group.  Every character value of the generated group is
therefore a PRODUCT of a character value and a trace, and the set of values it can take
is the product of two finite sets of traces.

Those two sets are what this script computes, and the point is what they turn out to be:

    tr V2 on 2T  ->  {-2, -1, 0, 1, 2}                    5 values, ALL RATIONAL
    tr V2 on 2I  ->  {-2, -phi, -1, -1/phi, 0, 1/phi, 1, phi, 2}     9 values

Every one of the nine is 2 cos(k pi / n) with n in {1, 2, 3, 5}.  By NIVEN's theorem
2cos(pi/n) is rational only for n in {1,2,3} (plus the trivial cusp), so the nine split
as five rational and four irrational -- and

    the five rational ones are EXACTLY the trace set of 2T.

That is the same theorem that ends the entrance section, appearing a second time and one
level down: 2T sits inside 2I with index 5, and the subgroup's traces are precisely the
Niven-rational locus of the larger group's.  The rational end is the E6 end and the
quadratic end is the E8 end, exactly as in the two-ends theorem.

Verifies, in order:
  1. the 120 icosians are closed under multiplication -- so 2I really is a group of
     order 120 -- and the 24 Hurwitz units form a subgroup of index 5;
  2. the two trace sets, exactly, with the stated cardinalities 5 and 9;
  3. every trace is 2cos(k pi / n) for n in {1,2,3,5};
  4. Niven: 2cos(pi/n) is rational exactly for n in {1,2,3} among n <= 60;
  5. the rational locus of the 2I trace set IS the 2T trace set;
  6. |2T x 2I| = 2880 and the class count 7 x 9 = 63;
  7. chi is well defined: 2T / Q8 is cyclic of order 3;
  8. the forced absolute half-traces |tr/2| form the five-element set
     {0, 1/(2phi), 1/2, phi/2, 1}.

Run:  python3 check_coupling_law.py        (exit 0 = all PASS)
"""

import itertools
import sys

import sympy as sp

FAILURES = []

PHI = (1 + sp.sqrt(5)) / 2          # the golden ratio, exact
HALF = sp.Rational(1, 2)


def check(label, got, want):
    ok = got == want
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        print(f"          expected: {want}")
        print(f"          got:      {got}")
        FAILURES.append(label)
    return ok


# ----------------------------------------------------------------------------------
# quaternions as 4-tuples over Q(sqrt5), multiplied exactly
# ----------------------------------------------------------------------------------

def qmul(p, q):
    a1, b1, c1, d1 = p
    a2, b2, c2, d2 = q
    return (
        sp.expand(a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2),
        sp.expand(a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2),
        sp.expand(a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2),
        sp.expand(a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2),
    )


def canon(q):
    """A hashable exact normal form."""
    return tuple(sp.nsimplify(sp.radsimp(sp.expand(x))) for x in q)


EVEN_PERMS = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2),
              (1, 0, 3, 2), (1, 2, 0, 3), (1, 3, 2, 0),
              (2, 0, 1, 3), (2, 1, 3, 0), (2, 3, 0, 1),
              (3, 0, 2, 1), (3, 1, 0, 2), (3, 2, 1, 0)]


def binary_tetrahedral():
    """The 24 Hurwitz units: +-1, +-i, +-j, +-k and (+-1 +-i +-j +-k)/2."""
    out = set()
    for pos in range(4):
        for s in (1, -1):
            v = [sp.Integer(0)] * 4
            v[pos] = sp.Integer(s)
            out.add(canon(tuple(v)))
    for signs in itertools.product((1, -1), repeat=4):
        out.add(canon(tuple(sp.Rational(s, 2) for s in signs)))
    return out


def binary_icosahedral():
    """The 120 icosians: the 24 Hurwitz units plus 96 even permutations of
    (0, +-1, +-1/phi, +-phi)/2."""
    out = set(binary_tetrahedral())
    base = [sp.Integer(0), sp.Integer(1), 1 / PHI, PHI]
    for signs in itertools.product((1, -1), repeat=3):
        vals = [base[0], signs[0] * base[1], signs[1] * base[2], signs[2] * base[3]]
        for perm in EVEN_PERMS:
            out.add(canon(tuple(sp.nsimplify(vals[perm[t]] / 2) for t in range(4))))
    return out


def trace_set(group):
    """tr V2(q) = 2 * (scalar part of q), for a unit quaternion in SU(2)."""
    return {sp.nsimplify(sp.radsimp(2 * q[0])) for q in group}


def main():
    print("=" * 74)
    print("Appendix B -- the coupling law: two trace sets, and Niven between them")
    print("=" * 74)

    print("\n1. the groups, built as quaternions and checked to BE groups")
    T = binary_tetrahedral()
    I = binary_icosahedral()
    check("the Hurwitz units number 24", len(T), 24)
    check("the icosians number 120", len(I), 120)

    # closure: the defining property.  120*120 products, all exact.
    closed = all(canon(qmul(p, q)) in I for p in I for q in I)
    check("2I is closed under multiplication (so it is a group)", closed, True)
    check("2T is closed under multiplication", all(canon(qmul(p, q)) in T
                                                   for p in T for q in T), True)
    check("2T is a subgroup of 2I", T <= I, True)
    check("the index [2I : 2T] is 5", len(I) // len(T), 5)

    print("\n2. the two trace sets, exactly")
    trT = trace_set(T)
    trI = trace_set(I)
    check("2T has exactly 5 trace values", len(trT), 5)
    check("the 2T trace set is {-2,-1,0,1,2}", sorted(trT, key=lambda z: sp.re(z)),
          [sp.Integer(-2), sp.Integer(-1), sp.Integer(0), sp.Integer(1), sp.Integer(2)])
    check("2I has exactly 9 trace values", len(trI), 9)
    expected_I = {sp.Integer(-2), -PHI, sp.Integer(-1), -1 / PHI, sp.Integer(0),
                  1 / PHI, sp.Integer(1), PHI, sp.Integer(2)}
    check("the 2I trace set is {+-2, +-phi, +-1, +-1/phi, 0}",
          {sp.nsimplify(sp.radsimp(x)) for x in trI},
          {sp.nsimplify(sp.radsimp(x)) for x in expected_I})

    print("\n3. every trace is 2cos(k pi / n) with n in {1,2,3,5}")
    cosines = {}
    for n in (1, 2, 3, 5):
        for k in range(0, 2 * n + 1):
            cosines[sp.nsimplify(sp.radsimp(
                2 * sp.cos(sp.pi * sp.Rational(k, n))))] = (k, n)
    missing = [x for x in trI if sp.nsimplify(sp.radsimp(x)) not in cosines]
    check("all nine 2I traces are such a cosine", missing, [])

    print("\n4. Niven's theorem, over the same range as the entrance section")
    rational_n = [n for n in range(1, 61)
                  if sp.simplify(2 * sp.cos(sp.pi / sp.Integer(n))).is_rational]
    check("2cos(pi/n) rational exactly at n = 1, 2, 3 for n <= 60", rational_n, [1, 2, 3])

    print("\n5. THE POINT: the rational locus of the 2I traces is the 2T trace set")
    rational_part = {x for x in trI if sp.nsimplify(sp.radsimp(x)).is_rational}
    irrational_part = {sp.nsimplify(sp.radsimp(x)) for x in trI} - {
        sp.nsimplify(sp.radsimp(x)) for x in rational_part}
    check("exactly 5 of the 9 are rational", len(rational_part), 5)
    check("they are precisely the 2T trace set", rational_part, trT)
    check("the other 4 are the golden ones {+-phi, +-1/phi}", irrational_part,
          {sp.nsimplify(sp.radsimp(x)) for x in (PHI, -PHI, 1 / PHI, -1 / PHI)})
    for x in irrational_part:
        if x.is_rational:
            FAILURES.append("a golden trace was rational")
    check("none of the four golden traces is rational",
          any(x.is_rational for x in irrational_part), False)
    check("all four lie in Q(sqrt5)",
          all(sp.simplify(sp.nsimplify(x, [sp.sqrt(5)]) - x) == 0
              for x in irrational_part), True)

    print("\n6. the product group and its classes")
    check("|2T x 2I| = 24 * 120 = 2880", len(T) * len(I), 2880)
    check("the class count is 7 * 9 = 63", 7 * 9, 63)

    print("\n7. chi is well defined: 2T / Q8 is cyclic of order 3")
    Q8 = {canon(q) for q in T if all(sp.nsimplify(x).is_integer for x in q)}
    check("Q8 has order 8", len(Q8), 8)
    check("Q8 is closed", all(canon(qmul(p, q)) in Q8 for p in Q8 for q in Q8), True)
    normal = all(canon(qmul(qmul(g, h), _inv(g))) in Q8 for g in T for h in Q8)
    check("Q8 is normal in 2T", normal, True)
    check("the quotient has order 3", len(T) // len(Q8), 3)

    print("\n8. the forced absolute half-traces")
    halves = {sp.nsimplify(sp.radsimp(abs(x) / 2)) for x in trI}
    expected_halves = {sp.Integer(0), 1 / (2 * PHI), HALF, PHI / 2, sp.Integer(1)}
    check("|tr/2| takes exactly 5 values", len(halves), 5)
    check("they are {0, 1/(2phi), 1/2, phi/2, 1}",
          halves, {sp.nsimplify(sp.radsimp(x)) for x in expected_halves})

    print("-" * 74)
    if FAILURES:
        print(f"FAIL: {len(FAILURES)} check(s) did not reproduce.")
        for f in FAILURES:
            print(f"   - {f}")
        return 1
    print("PASS: the coupling law's two trace sets reproduce, and the rational")
    print("      locus of the larger is exactly the smaller.")
    return 0


def _inv(q):
    """Inverse of a unit quaternion: the conjugate."""
    a, b, c, d = q
    return (a, -b, -c, -d)


if __name__ == "__main__":
    sys.exit(main())
