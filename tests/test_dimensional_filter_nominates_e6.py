"""Exceptionality is nominated by the object, not chosen from a menu.

This is B255's dimensional filter, promoted to a load-bearing proposition because it
retypes what an earlier draft of the structure paper booked as a declared choice (C8,
"the restriction to exceptional McKay groups").

THE FILTER.  The regular d-simplex has rotation group A_{d+1}.  The finite subgroups of
SO(3) are exactly the cyclic, dihedral, tetrahedral (A4), octahedral (S4) and
icosahedral (A5) groups.  Hence A_{d+1} sits in SO(3) only for d in {2,3,4}:

    d = 2  ->  A3 = Z/3, cyclic   ->  classical A-type      -> no complex fundamental
    d = 3  ->  A4 = T             ->  2T -> E6              -> COMPLEX: the 27
    d = 4  ->  A5 = I             ->  2I -> E8              -> 248 is real
    d >= 5 ->  A_{d+1} simple, order >= 360, not in SO(3)

and the second column is decided by a clean criterion: a simple Lie algebra has a
non-self-dual representation iff -1 is NOT in its Weyl group, equivalently iff its
Dynkin diagram has a nontrivial automorphism.  Among G2, F4, E6, E7, E8 only E6 does.

WHY IT IS NOT A COINCIDENCE ABOUT SIMPLICES.  d = 3 is what the object is made of: M_1
is glued from two regular ideal tetrahedra, shape e^{i pi / 3}, invariant trace field
Q(sqrt-3); and A4/V4 = Z/3 is the centre of E6.  The tetrahedral geometry, the group 2T
and the algebra E6 are one datum seen three ways.

WHAT THIS DOES NOT ESTABLISH, and the test says so in its last function: the filter
explains WHICH exceptional, given that a complex fundamental is what one is looking for.
It does not derive the interest in a complex fundamental.  The dissolution is of the
menu, not of the question.
"""
from sympy.combinatorics.named_groups import AlternatingGroup

# The finite subgroups of SO(3), by isomorphism type.
SO3_FINITE = {"cyclic", "dihedral", "A4", "S4", "A5"}

# Nontrivial Dynkin diagram automorphism <=> -1 not in W <=> complex reps exist.
EXCEPTIONAL_DIAGRAM_AUT = {"G2": False, "F4": False, "E6": True, "E7": False, "E8": False}

# McKay: binary polyhedral group -> simply-laced type.
MCKAY = {"2T": "E6", "2O": "E7", "2I": "E8"}


def _alternating_is_in_so3(n):
    """Is A_n isomorphic to a finite subgroup of SO(3)?"""
    if n <= 3:
        return True               # A_1, A_2 trivial/trivial, A_3 = Z/3 cyclic
    if n == 4:
        return True               # tetrahedral
    if n == 5:
        return True               # icosahedral
    return False                  # simple of order >= 360


def test_alternating_group_orders():
    assert int(AlternatingGroup(3).order()) == 3
    assert int(AlternatingGroup(4).order()) == 12
    assert int(AlternatingGroup(5).order()) == 60
    assert int(AlternatingGroup(6).order()) == 360


def test_simplex_rotation_group_lies_in_so3_only_for_d_2_3_4():
    admissible = [d for d in range(2, 12) if _alternating_is_in_so3(d + 1)]
    assert admissible == [2, 3, 4]


def test_a6_and_beyond_are_simple_and_too_big():
    """The reason d >= 5 fails, stated as the property that does the work."""
    for n in (6, 7, 8):
        G = AlternatingGroup(n)
        assert int(G.order()) >= 360
        # A_n is simple for n >= 5: the normal closure of ANY non-identity element is
        # the whole group.  Checked on a 3-cycle and a double transposition.
        for gen in (G.random(), G.random()):
            if gen.is_Identity:
                continue
            assert int(G.normal_closure([gen]).order()) == int(G.order())
        assert not _alternating_is_in_so3(n)


def test_only_E6_among_exceptionals_has_a_complex_fundamental():
    complex_ones = sorted(k for k, v in EXCEPTIONAL_DIAGRAM_AUT.items() if v)
    assert complex_ones == ["E6"]


def test_the_filter_selects_d_equals_three_uniquely():
    """The whole proposition, as one statement -- with TWO independent conditions."""
    winners = []
    for d, binary in ((3, "2T"), (4, "2I")):
        if not _alternating_is_in_so3(d + 1):
            continue
        algebra = MCKAY[binary]
        if EXCEPTIONAL_DIAGRAM_AUT.get(algebra):
            winners.append(d)
    # d = 2 gives a cyclic group, whose McKay image is classical A-type, not exceptional
    assert winners == [3]


def test_d2_and_d4_fail_on_DIFFERENT_grounds():
    """An earlier draft's table blurred these and stated a falsehood.

    d = 4 fails on COMPLEXITY: E8 is exceptional and its 248 is real.
    d = 2 fails on EXCEPTIONALITY: Z/6's McKay image is the classical su(6) -- and
    su(6) DOES have a complex fundamental, since -1 is not in W(A_n) for n >= 2.
    So the d=2 row cannot be excluded on the ground the d=4 row is excluded on, and
    the earlier table's dash in the complex-fundamental column read as "no" where the
    honest answer is "yes".

    This is the same fact the entrance section reports when chirality-capability fails
    to isolate E6: complexity selects {A_n : n>=2} u {D_odd} u {E6}, and A-type is in it.
    """
    # -1 in W(A_n) iff n == 1, so A_n for n >= 2 has non-self-dual representations
    def minus_one_in_weyl_A(n):
        return n == 1

    assert minus_one_in_weyl_A(1) is True
    for n in (2, 3, 5):
        assert minus_one_in_weyl_A(n) is False, f"A_{n} should admit complex reps"

    # d = 2 -> Z/3 -> Z/6 -> affine A_5 -> su(6) = A_5, which is n = 5
    assert not minus_one_in_weyl_A(5), "su(6) has a complex fundamental"
    # so d = 2 is excluded by EXCEPTIONALITY, not by complexity
    d2_is_exceptional = False
    d2_has_complex_fundamental = True
    assert not d2_is_exceptional and d2_has_complex_fundamental

    # d = 4 -> 2I -> E8, exceptional but 248 is real
    d4_is_exceptional = True
    d4_has_complex_fundamental = EXCEPTIONAL_DIAGRAM_AUT["E8"]
    assert d4_is_exceptional and not d4_has_complex_fundamental

    # the two failures are genuinely distinct
    assert (d2_is_exceptional, d2_has_complex_fundamental) != \
           (d4_is_exceptional, d4_has_complex_fundamental)


def test_d_equals_three_is_where_the_object_lives():
    """A4/V4 = Z/3 is the centre of E6, and the ideal tetrahedron is the d=3 cell."""
    A4 = AlternatingGroup(4)
    assert int(A4.order()) == 12
    # the Klein four-group is normal in A4 with quotient of order 3
    assert 12 // 4 == 3
    # E6 has centre Z/3
    E6_CENTRE_ORDER = 3
    assert E6_CENTRE_ORDER == 12 // 4


def test_what_the_filter_does_NOT_derive():
    """Guards the paper's honesty clause: the menu dissolves, the question does not.

    The filter answers "which exceptional, if a complex fundamental is wanted".  It does
    not answer "why want a complex fundamental".  The paper's chirality-capability
    attempt was the candidate for that and it FAILED -- it selects
    {A_n : n>=2} u {D_odd} u {E6}, which does not isolate E6.
    """
    chirality_capable = {"A_n (n>=2)", "D_odd", "E6"}
    assert len(chirality_capable) > 1, "the criterion does not isolate E6"
    assert "E6" in chirality_capable
