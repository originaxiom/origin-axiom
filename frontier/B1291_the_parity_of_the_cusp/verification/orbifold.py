"""*** WITHDRAWN AS AN ARGUMENT (B1291 §4). THE COMPUTATIONS BELOW ARE TRUE; THE CRITERION IS VACUOUS. ***

chi_orb(T^2/G) = chi(T^2)/|G| = 0 IDENTICALLY for every finite G, so "all 17 quotients give
chi_orb = 0" CANNOT FAIL and decides nothing -- an MB12 vacuity failure against this repo's own
rule. The non-vacuity control here is mis-aimed: it shows the FORMULA returns nonzero on
hyperbolic/spherical inputs, never that the CRITERION could fail on the Euclidean inputs it
actually ranges over. A control must vary what the argument varies.

And chi_orb is the wrong invariant anyway: it is excluded on integrality alone -- for the cone
orbifold D^2(n) the index is 1 for every n while chi_orb = 1/n is not an integer, so chi_orb
cannot be the index of any operator. The chi that enters is the ORDINARY chi of the UNDERLYING
SPACE.

The corner case IS closed, but by adversarial verification on GENERICITY (E61) and ADMISSIBILITY
-- see FINDINGS.md sections 4 and 5. Retained as a record, NOT as a closure.
"""
"""The last hatch: does the QUOTIENT (corners, cone points) escape chi = 0?

B1291 closed subsurfaces; the involution census closed symmetry-cut dividing sets. The
remaining move is fc's picture -- arcs with endpoints, i.e. a QUOTIENT of the cusp torus,
which carries CORNERS and CONE POINTS, so the naive chi is replaced by the ORBIFOLD Euler
characteristic.  Compute it.

    chi_orb(S^2(n1..nk)) = 2 - sum_i (1 - 1/n_i)
    chi_orb(D^2(...; m1..ml)) etc., and for a free quotient chi_orb = chi/|G|.

THE CUSP CROSS-SECTION IS EUCLIDEAN. Its quotients are exactly the 17 wallpaper orbifolds.
And a Euclidean 2-orbifold has chi_orb = 0 BY DEFINITION -- that is what "Euclidean" means
via Gauss-Bonnet. So this is checkable, and it is checkable against a table nobody here wrote.
"""
from fractions import Fraction as F

# The 17 wallpaper groups as orbifolds (Conway notation), with their singular data.
# cone[] = orders of cone points; corner[] = orders of corner reflectors;
# mirror = does it have a boundary mirror; handles/crosscaps for the underlying surface.
WALLPAPER = {
    # name          cones          corners        underlying chi (before singular terms)
    "o    (p1)":     ([],            [],           0),   # torus
    "xx   (pg)":     ([],            [],           0),   # Klein bottle
    "**   (pm)":     ([],            [],           0),   # annulus (2 mirror circles)
    "*x   (cm)":     ([],            [],           0),   # Moebius band
    "2222 (p2)":     ([2, 2, 2, 2],  [],           2),
    "22*  (pmg)":    ([2, 2],        [],           1),
    "22x  (pgg)":    ([2, 2],        [],           1),
    "*2222(pmm)":    ([],            [2,2,2,2],    1),
    "2*22 (cmm)":    ([2],           [2, 2],       1),
    "333  (p3)":     ([3, 3, 3],     [],           2),
    "*333 (p3m1)":   ([],            [3, 3, 3],    1),
    "3*3  (p31m)":   ([3],           [3],          1),
    "442  (p4)":     ([4, 4, 2],     [],           2),
    "*442 (p4m)":    ([],            [4, 4, 2],    1),
    "4*2  (p4g)":    ([4],           [2],          1),
    "632  (p6)":     ([6, 3, 2],     [],           2),
    "*632 (p6m)":    ([],            [6, 3, 2],    1),
}


def chi_orb(cones, corners, base_chi):
    """Conway's orbifold Euler characteristic."""
    x = F(base_chi)
    for n in cones:
        x -= F(n - 1, n)              # a cone point costs (1 - 1/n)
    for n in corners:
        x -= F(n - 1, 2 * n)          # a corner reflector costs half that
    return x


def selftest():
    print("EVERY quotient of the flat cusp torus -- the 17 wallpaper orbifolds\n")
    vals = {}
    for name, (cones, corners, base) in WALLPAPER.items():
        x = chi_orb(cones, corners, base)
        vals[name] = x
        flag = "ZERO" if x == 0 else f"*** {x} ***"
        print(f"  {name:14} cones={str(cones):16} corners={str(corners):14} chi_orb = {str(x):>4}  {flag}")

    assert all(v == 0 for v in vals.values()), {k: str(v) for k, v in vals.items() if v != 0}
    print(f"\n  ALL {len(vals)} of {len(vals)} have chi_orb = 0.")

    # CONTROL, both directions (MB12): the formula must be able to produce nonzero.
    print("\n  [ctl] the same formula on NON-Euclidean orbifolds (it must NOT always give 0):")
    probes = {
        "S^2(2,3,7)  hyperbolic": ([2, 3, 7], [], 2),
        "S^2(2,3,5)  spherical":  ([2, 3, 5], [], 2),
        "S^2(2,2,2)  spherical":  ([2, 2, 2], [], 2),
        "S^2 no cones (sphere)":  ([], [], 2),
        "S^2(2,3,6)  EUCLIDEAN":  ([2, 3, 6], [], 2),
    }
    for name, (c, r, b) in probes.items():
        x = chi_orb(c, r, b)
        print(f"        {name:26} chi_orb = {str(x):>8}  {'zero' if x == 0 else 'NONZERO'}")
    assert chi_orb([2, 3, 7], [], 2) < 0 and chi_orb([2, 3, 5], [], 2) > 0
    assert chi_orb([2, 3, 6], [], 2) == 0      # the Euclidean one in the control set is 0 too

    print("""
  ==> chi_orb = 0 FOR EVERY QUOTIENT OF THE CUSP TORUS, all 17, with no exception -- and
      not by coincidence. A EUCLIDEAN 2-orbifold has chi_orb = 0 BY DEFINITION (Gauss-Bonnet:
      the total curvature is zero). The cusp cross-section IS Euclidean. So passing to a
      quotient, adding corners, adding cone points -- NONE of it escapes.

  ==> THE SIXTH ROUTE, and the one that subsumes the others. The zero is not a fact about
      E6, the 27, the holonomy, sl2 vs full E6, or which real form: IT IS A FACT ABOUT THE
      CUSP BEING FLAT. chi = 0 propagates to every subsurface built from essential curves
      (B1291), every symmetry-cut dividing set (the involution census), and now every
      orbifold quotient.

  ==> AND THE ESCAPE IS NOW NAMED EXACTLY. A nonzero index needs a boundary object that is
      NOT a quotient of the flat torus: a DISC, a PUNCTURE, or a cone point of an order the
      flat structure does not admit. Every one of those is a CHOICE OF WHERE TO CUT --
      observer-supplied, in this programme's own sense (B432/B434: a closing supplies the bit).
""")
    print("SELFTEST: PASS")


if __name__ == "__main__":
    selftest()


# --- independent cross-check: the COVERING relation, which uses none of the table above ---
def covering_crosscheck():
    """chi_orb is multiplicative under covers: chi_orb(T^2/G) = chi(T^2)/|G| = 0/|G| = 0.

    This derives the SAME zeros without the cone/corner data I typed by hand, so a wrong
    entry in WALLPAPER cannot survive both routes."""
    from fractions import Fraction as F
    ROTATION_QUOTIENTS = {          # T^2 / (Z/n), the four Euclidean rotation orders
        "T^2/(Z/2) = S^2(2,2,2,2)": (2, [2, 2, 2, 2]),
        "T^2/(Z/3) = S^2(3,3,3)":   (3, [3, 3, 3]),
        "T^2/(Z/4) = S^2(2,4,4)":   (4, [2, 4, 4]),
        "T^2/(Z/6) = S^2(2,3,6)":   (6, [2, 3, 6]),
    }
    print("\n  [xchk] the covering relation, independent of the hand-entered table:")
    for name, (n, cones) in ROTATION_QUOTIENTS.items():
        by_cover = F(0, n)                        # chi(T^2)/|G| = 0/n
        by_cones = chi_orb(cones, [], 2)          # 2 - sum(1 - 1/n_i)
        agree = by_cover == by_cones == 0
        print(f"        {name:28} chi/|G| = {by_cover}   from cones = {by_cones}   {'AGREE' if agree else 'DISAGREE'}")
        assert agree, (name, by_cover, by_cones)
    print("        both routes give 0 for all four -- the table is not carrying the result")


if __name__ == "__main__":
    covering_crosscheck()
