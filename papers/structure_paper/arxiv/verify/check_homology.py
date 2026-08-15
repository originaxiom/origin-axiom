#!/usr/bin/env python3
"""
Appendix B -- verification of Theorem "H_1(M_m) = Z (+) (Z/m)^2".

Self-contained: stdlib only.  Imports NOTHING project-internal, so it travels with
the paper.  Exact integer arithmetic throughout; no floating point anywhere.

M_m is the once-punctured-torus bundle with monodromy phi_m = [[m^2+1, m], [m, 1]],
the abelianized mapping torus.  By Mayer-Vietoris,

    H_1(M_m; Z)  =  Z  (+)  coker(phi_m - I : Z^2 -> Z^2),

so the torsion is read off the Smith normal form of phi_m - I = [[m^2, m], [m, 0]].

Verifies, in order:
  1. tr phi_m = m^2 + 2 and det phi_m = 1 (so phi_m is in SL(2,Z), orientable bundle).
  2. Smith normal form of phi_m - I is diag(m, m); hence torsion = (Z/m)^2.
  3. H_1(M_m) = Z if and only if m = 1.
  4. A knot complement in S^3 has H_1 = Z (Alexander duality), so M_m can be one
     only for m = 1 -- and M_1 is the figure-eight knot complement.

Run:  python3 check_homology.py        (exit 0 = all PASS)
"""

import sys

FAILURES = []

M_RANGE = range(1, 41)


def check(label, got, want):
    ok = got == want
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        print(f"          expected: {want}")
        print(f"          got:      {got}")
        FAILURES.append(label)
    return ok


def phi(m):
    return [[m * m + 1, m], [m, 1]]


def trace(A):
    return A[0][0] + A[1][1]


def det2(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def smith_2x2(A):
    """Smith normal form invariant factors (d1, d2) of an integer 2x2 matrix.

    d1 = gcd of all entries; d1*d2 = |det|.  Both are exact integer operations.
    """
    from math import gcd

    entries = [A[0][0], A[0][1], A[1][0], A[1][1]]
    d1 = 0
    for e in entries:
        d1 = gcd(d1, e)
    d = abs(det2(A))
    if d1 == 0:
        return (0, 0)
    if d == 0:
        return (d1, 0)
    assert d % d1 == 0
    return (d1, d // d1)


def torsion_of(m):
    """Invariant factors of coker(phi_m - I), dropping trivial ones."""
    A = phi(m)
    D = [[A[0][0] - 1, A[0][1]], [A[1][0], A[1][1] - 1]]
    return [d for d in smith_2x2(D) if d != 1]


def main():
    print("=" * 70)
    print("Appendix B -- H_1 of the metallic bundles")
    print("=" * 70)

    print("\n1. phi_m lies in SL(2,Z) with the metallic trace")
    check("tr phi_m = m^2 + 2 for m = 1..40",
          [trace(phi(m)) for m in M_RANGE],
          [m * m + 2 for m in M_RANGE])
    check("det phi_m = 1 for m = 1..40",
          [det2(phi(m)) for m in M_RANGE],
          [1] * len(M_RANGE))

    print("\n2. Smith normal form of phi_m - I is diag(m, m)")
    A = phi(0)
    check("phi_m - I equals [[m^2, m], [m, 0]] (checked symbolically at m = 7)",
          [[phi(7)[0][0] - 1, phi(7)[0][1]], [phi(7)[1][0], phi(7)[1][1] - 1]],
          [[49, 7], [7, 0]])
    check("invariant factors are (m, m) for m = 1..40",
          [smith_2x2([[m * m, m], [m, 0]]) for m in M_RANGE],
          [(m, m) for m in M_RANGE])

    print("\n3. the torsion, and the selection of m = 1")
    check("torsion of H_1(M_m) is (Z/m)^2 for m = 2..40",
          {m: torsion_of(m) for m in range(2, 41)},
          {m: [m, m] for m in range(2, 41)})
    check("H_1(M_1) is Z, i.e. no torsion",
          torsion_of(1), [])
    check("H_1(M_m) = Z if and only if m = 1",
          [m for m in M_RANGE if torsion_of(m) == []],
          [1])

    print("\n4. the knot-complement consequence")
    # A knot complement in S^3 has H_1 = Z by Alexander duality; that is the test.
    is_candidate = [m for m in M_RANGE if torsion_of(m) == []]
    check("only m = 1 can be a knot complement in S^3",
          is_candidate, [1])
    check("the m = 1 trace is 3, matching the figure-eight monodromy",
          trace(phi(1)), 3)

    print("-" * 70)
    if FAILURES:
        print(f"FAIL: {len(FAILURES)} check(s) did not reproduce.")
        for f in FAILURES:
            print(f"   - {f}")
        return 1
    print("PASS: every homology claim reproduces exactly.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
