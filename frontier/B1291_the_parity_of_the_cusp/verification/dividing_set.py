"""JOIN 1, the piece that is BENCH topology and not fc's cusp geometry.

B1290 reduced the generation question to: chi(d+M) != 0?  This asks the PRIOR question --
what can d+M even BE -- and gets a sharp criterion.

SETUP (standard for these index formulas).  dM splits as d+M U d-M along a DIVIDING SET
Gamma, a properly embedded closed 1-manifold in dM.  For m004, dM = T^2 (one cusp).  So
Gamma is a disjoint union of embedded circles in T^2, and d+M is one of the two
complementary subsurfaces.

THE CLASSIFICATION OF EMBEDDED CIRCLES IN T^2 (standard surface topology):
  * an ESSENTIAL circle is non-separating, isotopic to a (p,q) curve, gcd(p,q)=1;
  * an INESSENTIAL circle is null-homotopic and bounds a DISC.

THE COMPUTATION.  Cut T^2 along Gamma.  Additivity of Euler characteristic over a
1-manifold (chi(circle) = 0) gives  chi(d+M) + chi(d-M) = chi(T^2) = 0, so the two sides'
characteristics are NEGATIVES of each other and chi(d+M) != 0 iff chi(d-M) != 0 -- the
condition is symmetric, and neither side is privileged.

Now the pieces.  Cutting T^2 along k disjoint ESSENTIAL circles (necessarily all parallel,
same slope, else they intersect) yields exactly k ANNULI.  Every piece has chi = 0, so
EVERY union of them has chi = 0.  ANY d+M is then chi = 0 and net chirality VANISHES.

Cutting along an INESSENTIAL circle yields a DISC (chi = +1) and its complement (chi = -1).
Now a side can be nonzero.

    ==> chi(d+M) != 0  IF AND ONLY IF  Gamma has an INESSENTIAL component.

That is the sharpening: the question is no longer the vague "what is d+M" but the sharp
"DOES THE DIVIDING SET HAVE A NULL-HOMOTOPIC COMPONENT?"
"""
from math import gcd
from itertools import combinations


def cut_torus(components):
    """chi of the pieces after cutting T^2 along `components`.

    Each component is ('essential', (p, q)) or ('inessential',).
    Returns the multiset of piece characteristics.  chi is additive over the cut
    (chi(S^1) = 0), and the total must always be chi(T^2) = 0."""
    ess = [c for c in components if c[0] == "essential"]
    ine = [c for c in components if c[0] == "inessential"]

    slopes = {c[1] for c in ess}
    if len(slopes) > 1:
        raise ValueError("disjoint essential circles in T^2 are parallel: one slope only")
    for (p, q) in slopes:
        if gcd(abs(p), abs(q)) != 1:
            raise ValueError(f"({p},{q}) is not a primitive slope, so not embedded")

    # k parallel essential circles cut T^2 into k annuli (chi = 0 each).
    pieces = [0] * len(ess) if ess else [0]          # no cut at all -> T^2 itself, chi = 0
    # each inessential circle bites a disc (+1) out of a piece (-1 to that piece)
    for _ in ine:
        pieces.append(1)
        pieces[0] -= 1
    return pieces


def sides(components):
    """Every way of 2-colouring the pieces into (d+M, d-M); return the possible chi(d+M)."""
    pieces = cut_torus(components)
    out = set()
    for r in range(len(pieces) + 1):
        for sub in combinations(range(len(pieces)), r):
            out.add(sum(pieces[i] for i in sub))
    return sorted(out)


def selftest():
    print("JOIN 1 -- what can d+M be, and when is chi(d+M) nonzero?\n")
    CASES = [
        ("no dividing set (d+M = T^2 or empty)", []),
        ("one essential (1,0) curve -- the meridian", [("essential", (1, 0))]),
        ("one essential (0,1) curve -- the longitude", [("essential", (0, 1))]),
        ("two parallel essential curves", [("essential", (1, 0)), ("essential", (1, 0))]),
        ("an essential (2,3) slope", [("essential", (2, 3))]),
        ("ONE INESSENTIAL circle", [("inessential",)]),
        ("essential + inessential", [("essential", (1, 0)), ("inessential",)]),
        ("two inessential circles", [("inessential",), ("inessential",)]),
    ]
    for name, comps in CASES:
        pieces = cut_torus(comps)
        poss = sides(comps)
        nz = [x for x in poss if x != 0]
        assert sum(pieces) == 0, (name, pieces)          # chi(T^2) = 0 is conserved, always
        verdict = "CHIRALITY POSSIBLE" if nz else "ZERO, forced"
        print(f"  {name:38}  pieces chi={pieces}  chi(d+M) in {poss}  -> {verdict}")

    # THE CRITERION, both directions
    only_essential = [
        [], [("essential", (1, 0))], [("essential", (0, 1))], [("essential", (2, 3))],
        [("essential", (1, 0)), ("essential", (1, 0))],
        [("essential", (3, 5))] * 4,
    ]
    for comps in only_essential:
        assert sides(comps) == [0], comps          # NOTHING but zero is reachable
    for comps in [[("inessential",)], [("essential", (1, 0)), ("inessential",)],
                  [("inessential",), ("inessential",)]]:
        assert any(x != 0 for x in sides(comps)), comps

    # and the geometry that forbids mixed slopes is enforced, not assumed
    for bad in ([("essential", (1, 0)), ("essential", (0, 1))],   # they must intersect
                [("essential", (2, 4))]):                          # not primitive => not embedded
        try:
            cut_torus(bad); raise AssertionError(f"should have rejected {bad}")
        except ValueError as e:
            print(f"  [ctl] rejected {bad}: {e}")

    print("\n  ==> chi(d+M) != 0  IFF the dividing set has an INESSENTIAL (null-homotopic)")
    print("      component. Essential curves -- ANY number, ANY primitive slope -- give only")
    print("      annuli, hence chi = 0, hence ZERO NET CHIRALITY, unconditionally.")
    print("\n  So the JOIN 1 question sharpens from 'what is d+M' to a YES/NO:")
    print("      DOES THE DIVIDING SET CONTAIN A NULL-HOMOTOPIC CIRCLE?")
    print("\nSELFTEST: PASS")


if __name__ == "__main__":
    selftest()
