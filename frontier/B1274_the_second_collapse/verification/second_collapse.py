"""B1274 -- THE SECOND COLLAPSE: I-25's multiplicity 4 falls to a point, and both collapses
run through the object's own 2T.

B1273's addendum collapsed I-6's binary by TWO CONCORDANT SELECTORS (the owner's arithmetic
one -- holonomy mod (1-omega) -- and codex's topological one -- extension over m000).  That
was the FIRST of the H5 census's eight measured multiplicities to become a point rather than
a count.  This arc asks whether it was a one-off.  It was not.

I-25 HAS TWO SELECTORS ALREADY IN THE RECORD, AND NOBODY HAD CHECKED THEY AGREE:
    SELECTOR 1 (B1257, geometric)  the unique E6 nilpotent orbit whose Slodowy slice meets
        the nilpotent cone in a SURFACE -- which Brieskorn-Slodowy identifies as C^2/2T, the
        very group that BUILT E6 by McKay.  One orbit of thirty.
    SELECTOR 2 (B1256 addendum, representation-theoretic)  of the FOUR labellings that type
        h^1 = 3 as three chiral, the only one with NO even-dimensional summand -- i.e. the
        only one admissible for the object's CANONICAL PSL(2,C) holonomy, since even-
        dimensional (Sym^odd) reps are not PSL(2,C) representations at all.

COMPUTED HERE: both return (2,2,2,0,2,2), the SUBREGULAR, 27 = 13 + 9 + 5.  I-25's
multiplicity 4 COLLAPSES TO A POINT.

THE SHAPE IS THE SAME AS I-6's, AND THE COMMON FACTOR IS 2T:
    I-6   geometric: the holonomy reduced mod (1-omega) lands in a specific 2T quotient
          topological: that quotient is the one extending over m000
    I-25  geometric: the slice that returns C^2/2T
          representation-theoretic: the embedding the PSL(2,C) holonomy admits
In BOTH, one selector is "the structure that returns the object's own 2T" and the other is a
compatibility condition.  The object's 2T is doing the selecting.

WHAT THIS DOES TO H5.  OPEN_ITEMS H5 says the object supplies every SPACE and never a POINT.
Two of the census's eight measured multiplicities are now POINTS, each pinned by two
independent concordant criteria.  That is a genuine counter-pressure on the pattern.

BUT IT IS NOT A FALSIFICATION, and this arc does not claim one.  H5's falsifier asks for an
OTHER-referential point.  "Which 2T quotient" and "which sl2 embedding" are both facts about
how the object sits in structures the object itself generated (E6 came from its own 2T by
McKay) -- so they are SELF-referential, which H5 explicitly permits.  What has changed is the
pattern's reach, not its truth: the object is far more decisive about ITSELF than the census
suggested, and the remaining multiplicities should each be attacked for a selector rather
than counted.

CONTROLS (MB12, both directions):
  * each selector is recomputed here from its own definition, not read from the parent arcs;
  * SELECTOR 2's discriminating power is exhibited: it starts from FOUR candidates and cuts
    to one, so agreement is not vacuous;
  * SELECTOR 1's uniqueness is checked against all 30 integral labellings;
  * the two are compared as SETS, so a mismatch would be reported rather than assumed away.
"""
import itertools, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(REPO, "frontier", "B1257_brieskorn_selection", "verification"))
sys.path.insert(0, os.path.join(REPO, "frontier", "B1256_sl2_embedding", "verification"))
import brieskorn_selection as BR
import sl2_embedding as SL


def selector_brieskorn():
    rows, _ = BR.table()
    return [c for c, dims, dO in rows if BR.DIM_N - dO == 2], rows


def selector_psl():
    WT, Cinv = SL.weights_27(), SL.CARTAN.inv()
    cand, free = [], []
    for c in itertools.product((0, 1, 2), repeat=6):
        vals = SL.h_on_27(c, WT, Cinv)
        if any(v != int(v) for v in vals):
            continue
        d = SL.decompose([int(v) for v in vals])
        if d is None:
            continue
        dims = [k + 1 for k in d]
        if sum(1 for t in dims if t % 2 == 1 and t > 1) == 3 and 1 not in dims:
            cand.append(c)
            if all(t % 2 == 1 for t in dims):
                free.append(c)
    return cand, free


def selftest():
    print("B1274 -- the second collapse (selftest)")
    br, rows = selector_brieskorn()
    print(f"  [S1  ] Brieskorn (slice = SURFACE) over {len(rows)} integral labellings: {br}")
    assert br == [(2, 2, 2, 0, 2, 2)]

    cand, free = selector_psl()
    print(f"  [ctl ] SELECTOR 2 starts from {len(cand)} candidates (h^1 = 3, all chiral)")
    assert len(cand) == 4, "agreement would be vacuous if there were only one candidate"
    print(f"  [S2  ] ...PSL(2,C)-admissible (no even-dim summand): {free}")
    assert free == [(2, 2, 2, 0, 2, 2)]

    print(f"  [JOIN] the two selectors agree: {br == free}")
    assert br == free
    dims = next(dd for cc, dd, _ in rows if cc == br[0])
    print(f"         both pick the SUBREGULAR {br[0]}, 27 = {' + '.join(map(str, dims))}")
    assert dims == [13, 9, 5]

    print("\n  => I-25's multiplicity 4 COLLAPSES TO A POINT -- the SECOND of the H5 census's")
    print("     eight measured multiplicities, after I-6's binary (B1273 addendum).")
    print("     In both, one selector returns the object's own 2T and the other is a")
    print("     compatibility condition. The object's 2T is doing the selecting.")
    print("\nSELFTEST: PASS")


if __name__ == "__main__":
    selftest()
