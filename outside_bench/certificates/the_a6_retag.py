#!/usr/bin/env python3
"""A6 RETAG -- a REPRODUCTION, not a discovery.

Memo 235 tagged A6 (the sum rule's "b_2(X) >= 2 with the Z/3 moving the
harmonic forms") as GENUINELY OPEN, "not computable: it lives on an object
nobody has built".  THE TAG WAS WRONG.  frontier/B1357_the_objects_own_
joyce_orbifold (SM head only) BUILT the object's own compact flat G_2
orbifold and DECIDED A6 on it, in the same words:

    "left (a b_2 >= 2 with the deck acting irreducibly) is decided in the
     flat class: the irreducible occurs only on 3-forms"

This cell exists ONLY to check that memo 233's DERIVED condition and
B1357's COMPUTED one are the SAME statement.  The mathematics below is
B1356's and B1357's; NO PRIORITY IS CLAIMED FOR ANY OF IT.

Exact rational/integer arithmetic; stdlib only.
"""
from __future__ import annotations
from fractions import Fraction as F


def rule(t):
    print("\n" + "-" * 78); print(" " + t); print("-" * 78)


def perm_rep_character(n, orbit_sizes):
    """Character of the permutation representation of Z/n on a disjoint
    union of orbits.  chi(g) = number of points fixed by g."""
    chi = []
    for k in range(n):
        fixed = 0
        for sz in orbit_sizes:
            # a Z/n-orbit of size sz: g^k fixes all sz points iff sz | k
            fixed += sz if (k % sz == 0) else 0
        chi.append(fixed)
    return chi


def multiplicity_of_trivial(chi, n):
    """<chi, 1> = (1/n) sum_k chi(g^k).  Integer for a genuine character."""
    tot = sum(chi)
    assert tot % n == 0, "character does not decompose over Z"
    return tot // n


def main():
    ok = {}

    rule("THE QUESTION -- are memo 233's derived condition and B1357's "
         "computed one the SAME statement?")
    print("""  memo 233 (derived, from the sum rule + rep theory of Z/3 on R^{b_2}):
    a Z/3 that PERMUTES the apexes and FIXES w gives equal charges, so
    3q = 0, q = 0, NO INFLOW.  Escape needs b_2 >= 2 AND the Z/3 moving
    the harmonic forms.

  B1357 (computed, on the object's own compact flat G_2 orbifold):
    "left (a b_2 >= 2 with the deck acting irreducibly) is decided in the
     flat class: the irreducible occurs only on 3-forms"
    with cover b_2 = 2, b_3 = 10; descent b_2 = 2, b_3 = 4; and
    "the deck's irreducible occurs on four of the cover's ten 3-forms and
     ON NO 2-FORM".

  Same condition, two routes, neither citing the other.""")

    rule("THE ELEMENTARY FACT BEHIND THE CURVED CASE (B1356/B1357's, "
         "reproduced here)")
    print("""  THREE apexes permuted FREELY by Z/3 carry the permutation
  representation of Z/3 on R^3.  Its character is chi = (3, 0, 0).""")
    chi = perm_rep_character(3, [3])          # one free orbit of size 3
    print(f"    character of the free 3-orbit: {tuple(chi)}")
    triv = multiplicity_of_trivial(chi, 3)
    print(f"    multiplicity of the TRIVIAL rep: {triv}")
    print(f"    remaining dimension (the SUM-ZERO subspace): {3 - triv}")
    print("""    -> R^3 = (trivial) (+) (2-dimensional irreducible), and the
       SUM-ZERO part IS the irreducible: the deck acts on it by rotation.
    So a FREE 3-orbit of apexes supplies, by construction, exactly the
    thing the flat class was computed NOT to have.""")
    ok["free 3-orbit: R^3 = trivial (+) 2-dim irrep"] = (triv == 1)

    rule("CONTROL -- the routine MUST be able to report NO irreducible "
         "(memo 164)")
    print("  a Z/3 acting TRIVIALLY on three points (three fixed orbits of")
    print("  size 1) must come back as 3 x trivial, carrying NO irrep:")
    chi_t = perm_rep_character(3, [1, 1, 1])
    triv_t = multiplicity_of_trivial(chi_t, 3)
    print(f"    character: {tuple(chi_t)}   trivial multiplicity: {triv_t}"
          f"   irrep dimension: {3 - triv_t}")
    print("  and a single fixed point must be 1 x trivial:")
    chi_1 = perm_rep_character(3, [1])
    triv_1 = multiplicity_of_trivial(chi_1, 3)
    print(f"    character: {tuple(chi_1)}   trivial multiplicity: {triv_1}"
          f"   irrep dimension: {1 - triv_1}")
    ok["CONTROL -- trivial action reports NO irrep"] = (
        triv_t == 3 and (3 - triv_t) == 0 and triv_1 == 1)

    rule("CONTROLS")
    for k, v in ok.items():
        print(f"  {'PASS' if v else 'FAIL'}   {k}")

    rule("A6, RETAGGED")
    print("""  WAS (memo 235):  GENUINELY OPEN -- "not computable: it lives on an
                   object nobody has built".   WRONG.

  IS:   FLAT CLASS + ITS JOYCE RESOLUTION -- COMPUTED, AND FAILING.
          b_2 = 2 after resolution, so the FIRST clause is satisfied; but
          the deck acts TRIVIALLY on both added 2-forms, so the SECOND
          clause fails.  B1357, stage 7.
        CURVED CLASS -- OPEN, with the mechanism named: the U(1)^2 "must be
          born with the curved apexes", the local b_2(link) = 1 class at
          each cone over CP^3/2T (B1355), extended in the sum-zero
          combinations -- which the fact above shows carries the deck's
          irreducible automatically, BECAUSE the three apexes form a free
          Z/3-orbit.

  WHAT HAS NOT CHANGED: the compact curved closing is STILL NOT BUILT.
  A6 moved from "not computable" to "computed where it can be, failing
  there, and reduced to compactness alone in the curved case".  That is a
  SHARPER STATEMENT, NOT A SOLVED PROBLEM.

  NO PRIORITY IS CLAIMED: the construction, the computation and the
  sum-zero observation are B1356's and B1357's.  I-26 remains UNEARNED.""")
    print()
    return 0 if all(ok.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
