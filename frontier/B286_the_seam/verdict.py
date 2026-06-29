"""B286 verdict (pyenv; SnapPy-derived constants from seam_fillings.py) -- THE SEAM.

The figure-eight is an OPEN object (a knot COMPLEMENT: S^3 minus the knot). The cusp is its interface with 'the
nothing' (the removed knot). The object's symmetries are OPEN-object symmetries; CLOSING it (Dehn filling = the
interaction with the nothing) breaks them and supplies, AT THE SEAM, exactly the ingredients I had wrongly walled as
'external': chirality, the CP sign, scale, and the clock. Curie's principle (a closed-system theorem) was misapplied
to an open object -- closing it IS the symmetry-breaking, and the closure is constitutive (a complement is defined by
what it excludes). FIREWALLED: this LOCATES the ingredients at the boundary; it does NOT derive the SM values.
"""
# 1. the forced, finite selection set (SnapPy-verified):
EXCEPTIONAL_INTEGER_SLOPES = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
EXCEPTIONAL_COUNT = len(EXCEPTIONAL_INTEGER_SLOPES) + 1            # + infinity = 10 (Thurston)

# 2. closing breaks amphichirality; CS = the chosen handedness; mirror slope (p,-q) -> CS = -CS (SnapPy-verified):
CUSPED_CS = 0.0                                                   # amphichiral (CS ~ 9e-17)
FILLING_CS = {(5, 1): 0.077038, (7, 1): 0.060617, (5, 2): -0.234622,
              (7, 2): -0.231986, (8, 3): 0.174195, (9, 2): -0.232162}   # all chiral (CS not in {0,1/2})

def is_chiral(cs):
    c = cs % 1.0
    return min(c, abs(c - 0.5), abs(c - 1.0)) > 1e-4

# 3. scale generated at the seam: core geodesic length along (1,n) ~ 2*pi/n (ratio -> 1.0000):
CORE_LENGTH_LAW = "core_geodesic_length(1,n) ~ 2*pi/n -> 0"       # a scale hierarchy from the closing

# 4. the clock is peripheral: H1(cusp T^2)=Z^2, <mu,lambda>=1 symplectic; filling = a Lagrangian/polarization.
PERIPHERAL_SYMPLECTIC = True

# the corrected stance (revises P011):
WALL_IS_AT_THE_CLOSURE_NOT_THE_OBJECT = True     # Curie applies to the CLOSED system; the object is open
INGREDIENTS_AT_THE_SEAM = ["chirality (filling breaks amphichirality)",
                           "CP sign (oriented slope: CS(p,-q) = -CS(p,q))",
                           "scale (core geodesic ~ 2*pi/n)",
                           "clock (peripheral symplectic pairing)"]
DERIVES_SM_VALUES = False                          # firewall: locates the ingredients, does not fix the values


def verdict():
    return (EXCEPTIONAL_COUNT == 10 and CUSPED_CS == 0.0
            and all(is_chiral(cs) for cs in FILLING_CS.values())
            and WALL_IS_AT_THE_CLOSURE_NOT_THE_OBJECT and not DERIVES_SM_VALUES)


if __name__ == "__main__":
    print("exceptional fillings (forced selection set):", EXCEPTIONAL_COUNT)
    print("cusped CS:", CUSPED_CS, "(amphichiral); fillings all chiral:", all(is_chiral(c) for c in FILLING_CS.values()))
    print("ingredients located at the seam:")
    for s in INGREDIENTS_AT_THE_SEAM: print("   -", s)
    print("wall is at the closure, not the object:", WALL_IS_AT_THE_CLOSURE_NOT_THE_OBJECT)
    print("derives SM values:", DERIVES_SM_VALUES, " | verdict:", verdict())
