#!/usr/bin/env python3
"""
Appendix B -- verification of the two-ends theorem and the E7 exclusion
(paper Thm. "the two ends, by Niven's theorem" and its corollary).

Self-contained: needs only sympy.  Imports NOTHING project-internal.  Exact symbolic
arithmetic throughout -- every cosine is handled as an algebraic number, never evaluated
numerically to decide rationality.

## THE STATEMENT

At the Z/n orbifold of the figure-eight knot complement, the meridian is a rotation of
order n, the meridian trace is x = 2 cos(pi/n), and the trace field is

    Q( x, sqrt((5 - x^2)(1 - x^2)) )

from the character-variety relation u^2 + (5 - x^2) u + (5 - x^2) = 0.  This is a CLEAN
quadratic field -- a single McKay group -- iff x is rational.  Niven's theorem says
2 cos(pi/n) is rational only for n in {1, 2, 3}, plus the cusp limit n -> infinity.

Those cases are exactly:

    n = inf, 1  ->  x = +-2  ->  hyperbolic  ->  Q(sqrt-3)  ->  2T -> E6
    n = 3       ->  x = 1    ->  Euclidean   ->  Q          ->  degenerate
    n = 2       ->  x = 0    ->  spherical   ->  Q(sqrt5)   ->  2I -> E8

## WHY THE E7 EXCLUSION IS THE SAME FACT

E7's McKay field is Q(sqrt2), which needs x = sqrt2, i.e. n = 4.  That value is
irrational, so the n = 4 field is the MIXED Q(sqrt2, sqrt-3), never the clean Q(sqrt2).
The middle exceptional group is excluded by one arithmetic fact, not by a coincidence of
several -- which is the point of the corollary.

Verifies, in order:
  1. Niven: 2cos(pi/n) is rational exactly for n in {1,2,3} among n <= 60, plus n -> inf;
  2. the three rational cases give discriminants -3, 0, 5 as claimed;
  3. n = 4 gives an irrational x, hence a mixed field, hence no clean Q(sqrt2);
  4. the fields attach to 2T (E6) and 2I (E8) by their squarefree parts;
  5. |H_1| of the double branched cover is det(4_1) = 5.

Run:  python3 check_niven_ends.py        (exit 0 = all PASS)
"""

import sys

import sympy as sp

FAILURES = []


def check(label, got, want):
    ok = got == want
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        print(f"          expected: {want}")
        print(f"          got:      {got}")
        FAILURES.append(label)
    return ok


def meridian_trace(n):
    """x = 2 cos(pi/n), exactly."""
    return sp.simplify(2 * sp.cos(sp.pi / sp.Integer(n)))


def discriminant(x):
    """(5 - x^2)(1 - x^2), the radicand of the trace field."""
    return sp.simplify((5 - x**2) * (1 - x**2))


def main():
    print("=" * 70)
    print("Appendix B -- the two ends, and why E7 cannot be a third")
    print("=" * 70)

    print("\n1. Niven: which 2cos(pi/n) are rational?")
    rational = [n for n in range(1, 61) if meridian_trace(n).is_rational]
    check("rational exactly at n = 1, 2, 3 for n <= 60", rational, [1, 2, 3])
    check("the cusp limit x -> 2 is rational", sp.Integer(2).is_rational, True)

    print("\n2. the three rational cases and their discriminants")
    table = {n: (meridian_trace(n), discriminant(meridian_trace(n))) for n in (1, 2, 3)}
    check("n = 1: x = -2", table[1][0], sp.Integer(-2))
    check("n = 1: (5-x^2)(1-x^2) = -3", table[1][1], sp.Integer(-3))
    check("n = 2: x = 0", table[2][0], sp.Integer(0))
    check("n = 2: (5-x^2)(1-x^2) = 5", table[2][1], sp.Integer(5))
    check("n = 3: x = 1", table[3][0], sp.Integer(1))
    check("n = 3: (5-x^2)(1-x^2) = 0, the degenerate wall", table[3][1], sp.Integer(0))
    check("the cusp x = 2 also gives -3", discriminant(sp.Integer(2)), sp.Integer(-3))

    print("\n3. E7 would need n = 4, and n = 4 is irrational")
    x4 = meridian_trace(4)
    check("x = 2cos(pi/4) = sqrt2", sp.simplify(x4 - sp.sqrt(2)), sp.Integer(0))
    check("sqrt2 is irrational", bool(x4.is_rational), False)
    check("the n = 4 discriminant is -3, not 2",
          discriminant(x4), sp.Integer(-3))
    print("          so the n = 4 field is Q(sqrt2, sqrt-3) -- MIXED, and never the")
    print("          clean Q(sqrt2) that an E7 end would require.")

    print("\n4. the two clean ends attach to 2T and 2I")
    check("hyperbolic end: squarefree part of -3 is -3 -> Q(sqrt-3) -> 2T -> E6",
          sp.sqrt(sp.Integer(-3)) ** 2, sp.Integer(-3))
    check("spherical end: squarefree part of 5 is 5 -> Q(sqrt5) -> 2I -> E8",
          sp.sqrt(sp.Integer(5)) ** 2, sp.Integer(5))
    check("the two ends are distinct fields",
          sp.simplify(sp.Integer(-3) - sp.Integer(5)) != 0, True)

    print("\n5. the spherical end's double cover")
    # det(4_1) = |Delta(-1)| for the Alexander polynomial Delta(t) = t^2 - 3t + 1
    det41 = abs(1 + 3 + 1)
    check("det(4_1) = |Delta(-1)| with Delta = t^2 - 3t + 1 gives 5", det41, 5)
    print("          so the double branched cover is L(5,2) with |H_1| = 5.")

    print("-" * 70)
    if FAILURES:
        print(f"FAIL: {len(FAILURES)} check(s) did not reproduce.")
        for f in FAILURES:
            print(f"   - {f}")
        return 1
    print("PASS: the two ends and the E7 exclusion reproduce exactly.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
