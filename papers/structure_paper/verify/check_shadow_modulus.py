#!/usr/bin/env python3
"""
Appendix B -- verification of the telescoping lemma, the shadow-modulus theorem,
and the group-versus-order proposition (paper Lem. "telescope", Thm. "shadow",
Prop. "group versus order").

Self-contained: stdlib only.  Imports NOTHING project-internal, so it travels with
the paper.  Exact rational/integer arithmetic throughout -- the order formula is
evaluated as an exact integer and every bound is an integer inequality.  No float
decides anything.

The shadow modulus of the metallic grammar R^m L^m is N_m = m^2 + 4 (the value of
the characteristic polynomial at -1).  The claim under test is that

    |SL(2, Z/N)|  is  24, 48 or 120   <=>   N in {3, 4, 5},

so that over the whole metallic family the exceptional binary polyhedral orders are
met only at m = 1, where N_1 = 5 and |SL(2,Z/5)| = 120 = |2I|.

The infinite tail is closed by the telescoping bound, not by sampling:

    prod_{p | N} (1 - p^-2)  >=  (N+1)/(2N)      =>   |SL(2,Z/N)| >= N^2 (N+1)/2,

which at N = 6 already gives 126 > 120.  (The arc's original bound was
prod (1 - p^-2) >= 1/zeta(2) = 6/pi^2, which is irrational and cannot be checked
exactly; the telescoping form is the exact replacement.)

Run:  python3 check_shadow_modulus.py        (exit 0 = all PASS)
"""

import sys
from fractions import Fraction

FAILURES = []

EXCEPTIONAL_ORDERS = {24, 48, 120}          # |2T|, |2O|, |2I|
SCAN = 4000                                  # exhaustive scan bound; the tail is proved


def check(label, got, want):
    ok = got == want
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        print(f"          expected: {want}")
        print(f"          got:      {got}")
        FAILURES.append(label)
    return ok


def check_true(label, got):
    return check(label, bool(got), True)


def prime_factors(n):
    ps, d = set(), 2
    while d * d <= n:
        while n % d == 0:
            ps.add(d)
            n //= d
        d += 1
    if n > 1:
        ps.add(n)
    return ps


def order_sl2_zmod(N):
    """|SL(2, Z/N)| = N^3 prod_{p|N} (1 - 1/p^2), computed as an exact integer."""
    val = Fraction(N**3)
    for p in prime_factors(N):
        val *= Fraction(p * p - 1, p * p)
    assert val.denominator == 1
    return val.numerator


def shadow_modulus(m):
    """chi_m(-1) where chi_m(t) = t^2 - (m^2+2)t + 1."""
    return 1 + (m * m + 2) + 1


def main():
    print("=" * 70)
    print("Appendix B -- the shadow modulus and the exceptional orders")
    print("=" * 70)

    print("\n1. the order formula, against known small values")
    check("|SL(2,Z/2)| = 6", order_sl2_zmod(2), 6)
    check("|SL(2,Z/3)| = 24", order_sl2_zmod(3), 24)
    check("|SL(2,Z/4)| = 48", order_sl2_zmod(4), 48)
    check("|SL(2,Z/5)| = 120", order_sl2_zmod(5), 120)
    check("|SL(2,Z/6)| = 144", order_sl2_zmod(6), 144)
    # For prime p the formula must reduce to p(p^2-1).
    check("prime case reduces to p(p^2-1) for p < 200",
          all(order_sl2_zmod(p) == p * (p * p - 1)
              for p in range(2, 200) if len(prime_factors(p)) == 1 and p in prime_factors(p)),
          True)

    print("\n2. the telescoping lemma, exactly")
    bad = []
    for N in range(2, SCAN + 1):
        lhs = Fraction(1)
        for p in prime_factors(N):
            lhs *= Fraction(p * p - 1, p * p)
        if not lhs >= Fraction(N + 1, 2 * N):
            bad.append(N)
    check(f"prod (1 - p^-2) >= (N+1)/(2N) for all 2 <= N <= {SCAN}", bad, [])

    print("\n3. the consequent lower bound, and the tail it closes")
    check("|SL(2,Z/N)| >= N^2 (N+1)/2 for all N in the scan",
          [N for N in range(2, SCAN + 1)
           if not order_sl2_zmod(N) * 2 >= N * N * (N + 1)],
          [])
    check("the bound at N = 6 is 126", 6 * 6 * 7 // 2, 126)
    check_true("126 > 120, so every N >= 6 exceeds the largest exceptional order",
               6 * 6 * 7 // 2 > max(EXCEPTIONAL_ORDERS))
    # Monotonicity of N^2(N+1)/2 in N does the rest, so the scan is a courtesy.
    check("no N in 6..SCAN attains an exceptional order",
          [N for N in range(6, SCAN + 1) if order_sl2_zmod(N) in EXCEPTIONAL_ORDERS],
          [])

    print("\n4. the theorem")
    check("|SL(2,Z/N)| in {24,48,120} exactly for N in {3,4,5}",
          [N for N in range(2, SCAN + 1) if order_sl2_zmod(N) in EXCEPTIONAL_ORDERS],
          [3, 4, 5])

    print("\n5. the metallic family meets the set only at m = 1")
    check("N_m = m^2 + 4", [shadow_modulus(m) for m in range(1, 8)],
          [m * m + 4 for m in range(1, 8)])
    check("N_1 = 5", shadow_modulus(1), 5)
    check("N_m >= 8 for every m >= 2, hence past the N >= 6 tail",
          [m for m in range(2, 200) if shadow_modulus(m) < 6], [])
    check("only m = 1 has |SL(2,Z/N_m)| exceptional",
          [m for m in range(1, 200)
           if order_sl2_zmod(shadow_modulus(m)) in EXCEPTIONAL_ORDERS],
          [1])

    print("\n6. group versus order: the E_7 slot is unoccupied")
    # Elements of SL(2, Z/4), by brute force over the 4^4 candidate matrices.
    N = 4
    elts = [(a, b, c, d)
            for a in range(N) for b in range(N) for c in range(N) for d in range(N)
            if (a * d - b * c) % N == 1]
    check("|SL(2,Z/4)| = 48 by enumeration", len(elts), 48)

    def mul(X, Y):
        a, b, c, d = X
        e, f, g, h = Y
        return ((a * e + b * g) % N, (a * f + b * h) % N,
                (c * e + d * g) % N, (c * f + d * h) % N)

    ident = (1, 0, 0, 1)

    def order_of(X):
        k, Y = 1, X
        while Y != ident:
            Y = mul(Y, X)
            k += 1
        return k

    orders = [order_of(X) for X in elts]
    check("SL(2,Z/4) has exactly 7 elements of order 2",
          sum(1 for o in orders if o == 2), 7)
    check("SL(2,Z/4) has no element of order 8",
          sum(1 for o in orders if o == 8), 0)
    print("          (a finite subgroup of SU(2) has exactly ONE involution, its")
    print("           centre -I; and 2O does contain elements of order 8.)")
    check_true("hence SL(2,Z/4) is not isomorphic to 2O despite |both| = 48",
               sum(1 for o in orders if o == 2) != 1)
    # Prime-level restatement: p(p^2-1) is never 48.
    check("p(p^2-1) = 48 has no prime solution",
          [p for p in range(2, 500)
           if prime_factors(p) == {p} and p * (p * p - 1) == 48],
          [])

    print("-" * 70)
    if FAILURES:
        print(f"FAIL: {len(FAILURES)} check(s) did not reproduce.")
        for f in FAILURES:
            print(f"   - {f}")
        return 1
    print("PASS: every shadow-modulus claim reproduces exactly.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
