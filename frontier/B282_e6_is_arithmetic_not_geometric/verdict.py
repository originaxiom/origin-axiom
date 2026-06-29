"""B282 verdict (pyenv-safe; heavy SnapPy+GAP in e6_specificity_gap.py).

The figure-eight's E6 is ARITHMETIC, not geometric. The 2T surjection (sole source of McKay E6) is present only for
the arithmetic cusped manifolds, absent for non-arithmetic hyperbolic knots; the character-variety E6 structure is
generic to all. So the only object-specific E6 content is the arithmetic 2T atom. FIREWALLED; nothing to CLAIMS.md.
"""
# 2T = SL(2,3) surjection counts (sage-python + GAP, 2026-06-29):
SURJECTIONS_2T = {"4_1": 2, "m003": 2, "5_2": 0, "6_1": 0, "6_2": 0, "7_4": 0}
ARITHMETIC = {"4_1", "m003"}

# what is figure-eight-SPECIFIC about E6 vs GENERIC (true of any hyperbolic knot / any Lie type):
OBJECT_SPECIFIC = ["2T arithmetic surjection (4_1 = unique arithmetic knot, Reid; -> McKay E6)",
                   "tau = E6 outer automorphism (needs amphichirality; NEEDS-SPECIALIST kernel)"]
GENERIC = ["dim H^1 = rank (MFP, any 1-cusped hyperbolic, any G)", "smoothness (MFP)",
           "irreducibility/density (B281, any G; knot-independent Lie fact)", "exponent grading / 27 / central charges",
           "conformal embedding (E6)_1 > SU(3)xSU(2)xU(1) (a property of the chiral algebra, manifold-independent)"]


def verdict():
    arith_2T = all(SURJECTIONS_2T[k] > 0 for k in ARITHMETIC)
    nonarith_no2T = all(v == 0 for k, v in SURJECTIONS_2T.items() if k not in ARITHMETIC)
    return arith_2T and nonarith_no2T


if __name__ == "__main__":
    print("2T surjections:", SURJECTIONS_2T)
    print("object-specific E6 facts:", OBJECT_SPECIFIC)
    print("generic (over-read) structure:", GENERIC)
    print("verdict (E6 is arithmetic-specific, geometry generic):", verdict())
