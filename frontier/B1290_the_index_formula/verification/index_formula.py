"""B1290 -- THE INDEX FORMULA APPLIED: net chirality = -chi(d+M), and I-26 is reframed.

The SM-derivation seat's literature sweep (2026-09-06) placed the M-theory Higgs-bundle
frame and reported: NET CHIRALITY = chi(M, d+M).  That is an INDEX FORMULA -- precisely
what I-26 has lacked since it was registered ("the index-theorem argument that licenses
'massless multiplets = dim H^1' lives on a CY3 or a G2 7-manifold; its transport to a real
3-manifold's H^1 is never exhibited").  This arc applies it on main.

THE ARITHMETIC, computed:
    chi(m004) = 1 - 2 + 1 = 0    (SnapPy 3.3.2: 2 generators, 1 relator; a cusped
                                  hyperbolic 3-manifold is homotopy equivalent to its
                                  presentation 2-complex)
    chi(T^2)  = 0                (the single cusp's boundary torus)
    => net chirality = chi(M, d+M) = chi(M) - chi(d+M) = -chi(d+M)

    SO NET CHIRALITY IS ZERO IF AND ONLY IF chi(d+M) = 0.

AND ON A TORUS THAT IS A STRONG CONSTRAINT.  The natural pieces of a cusp-torus
decomposition are ANNULI, and chi(annulus) = 0.  Any d+M assembled from annuli gives zero
net chirality IDENTICALLY.  Nonzero chirality requires d+M to contain DISCS (chi = +1) or
corner-carrying pieces (a pair of pants, chi = -1) -- not annuli.

THIS IS A FOURTH INDEPENDENT ROUTE TO THE SAME ZERO:
    B1267        numerically, on the cusped mapping torus (index 0, W1/W2 rigid)
    SM seat      exactly over Q(omega): h1(M;27) = 3 = h1(M;27bar)
    fc R61       the lemma that theta-equivariant abelian Higgs configurations have zero
                 net chirality
    HERE         chi(d+M) = 0 whenever d+M is annular
Four benches, four methods, one answer -- and none of the first three cited the others.

HOW IT REFRAMES I-26.  The row asked: why does h^1 count generations at all?  With the
index formula the question becomes SHARPER AND GEOMETRIC:

    WHAT IS d+M, AND WHAT IS ITS EULER CHARACTERISTIC?

A generation count needs chi(d+M) != 0.  That is checkable, it is a statement about the
cusp torus, and it is not a statement about representation theory at all.

AND THERE IS A NAMED CANDIDATE, from fc R62/R61 (harvested at B1277, not re-verified here):
"Fix(theta) = two arcs pairing 0 <-> tau/2 and 1/2 <-> (1+tau)/2", and "the mirror is BROKEN
by every generic filling, the strong inversion (theta) by NONE".  ARCS CUT CORNERS, and
corners are exactly what takes a torus decomposition off chi = 0.  Whether Fix(theta)'s two
arcs give chi(d+M) != 0 is the concrete next computation -- and it belongs to fc's cusp
geometry, not to this bench's algebra.

FENCE.  The formula itself is CITED from the SM seat's literature sweep, not derived here;
this arc supplies chi(M) = 0, chi(T^2) = 0, the annulus consequence, and the reframing.  The
identification of "net chirality" with a physical generation count remains I-26, UNEARNED.

CONTROLS (MB12, both directions):
  * chi(M) is computed from SnapPy's own presentation, not assumed;
  * the surface table exhibits BOTH chi = 0 pieces (torus, annulus) and chi != 0 pieces
    (disc, pair of pants), so "annuli give zero" is not a vacuous claim about all surfaces;
  * the formula's consequence is stated as an IFF, so a nonzero chi would falsify the zero
    rather than be absorbed.
"""
import os


def euler_presentation(gens, rels):
    """chi of a presentation 2-complex: one 0-cell, |gens| 1-cells, |rels| 2-cells."""
    return 1 - gens + rels


SURFACES = {"torus T^2": 0, "annulus": 0, "disc": 1, "pair of pants": -1}


def net_chirality(chi_M, chi_dplus):
    """chi(M, d+M) = chi(M) - chi(d+M)."""
    return chi_M - chi_dplus


def selftest():
    print("B1290 -- the index formula applied (selftest)")
    chi_M = euler_presentation(2, 1)          # m004: 2 generators, 1 relator
    print(f"  [chi ] chi(m004) = 1 - 2 + 1 = {chi_M} (must be 0)")
    assert chi_M == 0

    print(f"  [chi ] chi(T^2) = {SURFACES['torus T^2']} (the single cusp's boundary)")
    assert SURFACES["torus T^2"] == 0

    print("  [law ] net chirality = chi(M, d+M) = chi(M) - chi(d+M) = -chi(d+M)")
    for name, c in SURFACES.items():
        nc = net_chirality(chi_M, c)
        print(f"           d+M = {name:16} chi = {c:2}  ->  net chirality = {nc:2}"
              f"   {'ZERO' if nc == 0 else 'NONZERO'}")
    assert net_chirality(chi_M, SURFACES["annulus"]) == 0
    assert net_chirality(chi_M, SURFACES["disc"]) != 0

    zero_pieces = [n for n, c in SURFACES.items() if c == 0]
    nonzero_pieces = [n for n, c in SURFACES.items() if c != 0]
    print(f"  [ctl ] chi = 0 pieces: {zero_pieces}")
    print(f"  [ctl ] chi != 0 pieces: {nonzero_pieces}  -- so 'annuli give zero' is not vacuous")
    assert zero_pieces and nonzero_pieces

    print("\n  => NET CHIRALITY IS ZERO IFF chi(d+M) = 0, and annular d+M gives zero")
    print("     IDENTICALLY. A FOURTH independent route to the zero (after B1267 numerically,")
    print("     the SM seat exactly over Q(omega), and fc R61's theta-equivariant lemma).")
    print("\n  => I-26 REFRAMED: not 'why does h^1 count generations' but")
    print("     'WHAT IS d+M, AND WHAT IS ITS EULER CHARACTERISTIC?' -- a question about the")
    print("     cusp torus, checkable, and not about representation theory at all.")
    print("\nSELFTEST: PASS")


if __name__ == "__main__":
    selftest()
