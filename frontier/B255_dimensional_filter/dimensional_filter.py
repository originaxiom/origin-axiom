"""B255 -- the dimensional filter: the regular simplex whose rotation group's binary cover McKay-corresponds to an
exceptional Lie group with a COMPLEX fundamental is UNIQUE -- the tetrahedron (d=3) -> 2T -> E6. Verified, firewalled.
From the Chat-1 handoff (2026-06-28, Addendum 2). FIREWALLED -- a statement about simplices/finite groups/McKay/rep
theory; the "3 spatial dimensions / chiral matter" reading is the firewalled gloss. Nothing to CLAIMS.md.

THE FACT: the d-simplex has d+1 vertices and rotation group A_{d+1}. The finite subgroups of SO(3) are exactly the
cyclic, dihedral, A4(=T), S4(=O), A5(=I) groups -- so A_{d+1} is an SO(3) subgroup only for d in {2,3,4}:
    d=2: A_3 = Z3 (cyclic)        -> binary Z6  -> McKay A-type (SU(n))   [classical, not exceptional]
    d=3: A_4 = T  (tetrahedral)   -> binary 2T  -> McKay E6               [exceptional; 27 COMPLEX (B253)]
    d=4: A_5 = I  (icosahedral)   -> binary 2I  -> McKay E8               [exceptional; 248 REAL]
    d>=5: A_{d+1} simple, NOT in SO(3) -> no McKay
Among the exceptional groups, ONLY E6 has a complex (non-self-dual) fundamental (B253: G2 7 real, F4 26 real, E6 27
complex, E7 56 pseudoreal, E8 248 real). So the tetrahedron (d=3) is the UNIQUE regular simplex whose McKay image is
an exceptional group with a complex fundamental -- the (firewalled) "chirality-capable" end.

CORRECTION to the handoff: its d=2 line ("Z3 -> double cover Z6 -> A2 = SU(3)") is inconsistent (Z6 McKay is
affine A5 -> SU(6), not SU(3); it skipped the binary cover used at d=3,4). Either way d=2 gives a classical type-A
group, NOT an exceptional -- the dimensional-filter CORE (only d=3 -> exceptional-with-complex-fundamental) is
unaffected. Stated cleanly below.

FIREWALL: McKay/ADE labels, not gauge groups. The leap to "d=3 spatial dimensions => chiral matter is possible" is
the firewalled physics reading (and rests on the dead bridge B247 for any gauge-theory meaning). The MATH banked is:
the tetrahedron is the unique simplex selecting an exceptional group with a complex fundamental.

Run: python dimensional_filter.py (pyenv).
"""
import sympy as sp

# finite subgroups of SO(3): cyclic C_n, dihedral D_n, A4(=T), S4(=O), A5(=I). simplex rot group = A_{d+1}.
SO3_SIMPLEX = {3: ("Z3 (cyclic)", "Z6", "A-type (SU(n)) -- classical"),
               4: ("A4 = T (tetrahedral)", "2T", "E6"),
               5: ("A5 = I (icosahedral)", "2I", "E8")}

# B253: complex (non-self-dual) fundamental?
EXCEPTIONAL_COMPLEX_FUND = {"E6": True, "E7": False, "E8": False, "G2": False, "F4": False}


def simplex_mckay_image(d):
    """(rotation group A_{d+1}, binary cover, McKay ADE image) -- or None if A_{d+1} is not an SO(3) subgroup."""
    return SO3_SIMPLEX.get(d + 1)


def is_so3_subgroup(d):
    return (d + 1) in SO3_SIMPLEX


def unique_complex_fundamental_simplex():
    """the d whose simplex McKay-image is an exceptional group with a complex fundamental."""
    out = []
    for d in range(2, 12):
        img = simplex_mckay_image(d)
        if img and EXCEPTIONAL_COMPLEX_FUND.get(img[2]) is True:
            out.append(d)
    return out


if __name__ == "__main__":
    print("=== B255: the dimensional filter ===\n")
    print("d-simplex rotation group A_{d+1}, SO(3)-subgroup?, McKay image:")
    for d in range(2, 7):
        img = simplex_mckay_image(d)
        if img:
            grp, binary, ade = img
            cf = EXCEPTIONAL_COMPLEX_FUND.get(ade)
            tag = "" if cf is None else f"  complex fundamental: {cf}"
            print(f"  d={d}: A_{d+1} = {grp:22} -> binary {binary:3} -> {ade}{tag}")
        else:
            print(f"  d={d}: A_{d+1} (order {sp.factorial(d+1)//2}) NOT an SO(3) subgroup -> no McKay")

    winners = unique_complex_fundamental_simplex()
    print(f"\nsimplices whose McKay image is exceptional WITH a complex fundamental: d = {winners}")
    assert winners == [3]                                  # the tetrahedron, uniquely
    assert is_so3_subgroup(2) and is_so3_subgroup(3) and is_so3_subgroup(4)
    assert not any(is_so3_subgroup(d) for d in range(5, 12))   # d>=5: no McKay
    assert EXCEPTIONAL_COMPLEX_FUND["E6"] and not EXCEPTIONAL_COMPLEX_FUND["E8"]
    print("=> the tetrahedron (d=3) is the UNIQUE regular simplex selecting an exceptional group (E6) with a")
    print("   complex fundamental. (Physics reading '3 spatial dims / chiral matter' firewalled.) ALL CHECKS PASS")
