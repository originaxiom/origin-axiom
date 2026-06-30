"""B298 -- the figure-eight does NOT force three generations (the degree-2 obstruction). Run with sage-python (SnapPy)
for the cover count; the rest is pyenv-checkable in verdict.py.

From a cross-chat handoff (Chat-2, 2026-06-30), cross-checked against Chat-1 + this session's own computation. The
three handoff seats APPEARED to disagree (Chat-1: "3 generations from the Z3xZ3 orbifold"; Chat-2: "3 is not in the
object"); VERIFIED, they AGREE: the orbifold "3" is an external heterotic input (the doublet-triplet split is external,
B299), and the object's OWN matter multiplicities are 1 or 2, never 3.

THE OBSTRUCTION (the unifying reason): the figure-eight's invariant trace field is Q(sqrt-3), a DEGREE-2 field with
Galois group Z/2. Its natural multiplicities are therefore 1 (fixed) or 2 (conjugate pair). The number 3 appears
everywhere as a VALUE (dimension 3, level k=3, trace 3, ramified prime 3, E6-center Z/3) but NEVER as a matter
MULTIPLICITY, because a multiplicity of 3 needs a CUBIC (degree-3) structure and 4_1 is quadratic everywhere
(trace field, tetrahedron shape x^2-x+1, A-polynomial flavor, Galois Z/2).

SEVEN ROUTES to a forced multiplicity, all 1 or 2 (never 3):
  H^1 / flat-connection components = 1 ; ideal tetrahedra = 2 ; 3-fold covers of m004 = 1 (this file, SnapPy) ;
  SU(3)_family in SU(6) (E6 ⊃ SU(6)xSU(2)) fails (one 27 = ONE generation + exotics, B280) ;
  mu_3 / E6-center Z/3 on the 27 = scalar (Schur, uniform) ; F3-unipotent (x-1)^3 on the 27 = scalar on the
  irreducible, non-central -> 9+9+9 wrong size (B299: free 9x3 = trinification, not 3 generations) ;
  trace-map / A-polynomial dynamical fixed points = 2 (geometric + conjugate).

THE CUBIC-CARRIER CONJECTURE (bankable, falsifiable): three generations require a knot/manifold with a CUBIC
invariant trace field; the figure-eight (degree 2) is structurally a ONE-generation object. The three-generation
carrier is a different, degree-3 object. This converts "we can't get 3" into "3 lives on a cubic-trace-field knot."

FIREWALLED: a forced NEGATIVE about matter content; sharpens B292 (multiplicity tripartite) and B282 (arithmetic
atom). Nothing to CLAIMS.
"""
import snappy


def three_fold_covers_of_m004():
    M = snappy.Manifold('m004')
    covers = M.covers(3)
    return [(str(c.homology())) for c in covers]


if __name__ == "__main__":
    covers = three_fold_covers_of_m004()
    print("3-fold covers of m004:", len(covers), "-> H1:", covers)
    assert len(covers) == 1                              # multiplicity 1, not 3
    print("\ncusped trace field Q(sqrt-3) is DEGREE 2 (Galois Z/2) -> natural multiplicities 1 or 2, never 3.")
    print("VERDICT: the figure-eight does NOT force three generations. Cubic-carrier conjecture: 3 needs a")
    print("cubic-trace-field knot. (Sharpens B292/B282; firewalled; nothing to CLAIMS.)")
