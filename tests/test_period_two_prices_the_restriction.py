"""Pricing the period-one restriction: the period-TWO family selects the same member.

WHY THIS FILE EXISTS. The period-one restriction was the last genuinely UNPRICED
stipulation in the construction. Two external referee passes named it; Wave 2's
Architect C called computing its sibling "the highest-value unrun cell in the whole
campaign, and it is cheap". Run here.

THE SETUP. A purely periodic continued fraction of period two, [a; b, a, b, ...],
corresponds to

    M(a,b) = [[a,1],[1,0]] . [[b,1],[1,0]] = [[ab+1, a],[b, 1]].

TWO STRUCTURAL FACTS FALL OUT IMMEDIATELY:

  1. det M(a,b) = +1 ALREADY. A period-two word is orientation-preserving without
     squaring -- so the period-two family does not need the orientation stipulation
     at all. It is a genuinely different construction, not a relabelling.

  2. On the diagonal a = b = m, M(m,m) = [[m^2+1, m],[m, 1]] = phi_m. THE METALLIC
     FAMILY IS THE DIAGONAL OF THE PERIOD-TWO FAMILY. So period two is strictly
     LARGER, and relaxing the restriction genuinely adds members.

THE PRICE. Widening to period two adds a two-parameter family, and the homological
selection kills every new member:

    M(a,b) - I = [[ab, a],[b, 0]],  gcd of entries = gcd(a,b),  |det| = ab,
    so the invariant factors are ( gcd(a,b), lcm(a,b) ) and
    H_1 = Z + Z/gcd(a,b) + Z/lcm(a,b).

That is trivial iff gcd(a,b) = lcm(a,b) = 1 iff a = b = 1 -- THE GOLDEN.

CONSEQUENCE FOR THE COST LEDGER: the period-one stipulation is now PRICED. Relaxing
it does not reach a different object, because the criterion that selects inside the
metallic family selects the same member inside the strictly larger period-two family.
"""

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form


def M(a, b):
    return sp.Matrix([[a, 1], [1, 0]]) * sp.Matrix([[b, 1], [1, 0]])


def torsion(a, b):
    S = smith_normal_form(M(a, b) - sp.eye(2))
    return [abs(int(S[i, i])) for i in range(2)]


def test_period_two_is_orientation_preserving_without_squaring():
    """det = +1 already -- the orientation stipulation is not needed here."""
    a, b = sp.symbols("a b", positive=True, integer=True)
    assert sp.simplify(M(a, b).det()) == 1
    assert sp.simplify(M(a, b).trace() - (a * b + 2)) == 0


def test_the_metallic_family_is_the_diagonal():
    """a = b = m recovers phi_m exactly, so period two is strictly larger."""
    m = sp.Symbol("m", positive=True, integer=True)
    assert sp.simplify(M(m, m) - sp.Matrix([[m * m + 1, m], [m, 1]])) == sp.zeros(2, 2)


def test_torsion_is_gcd_and_lcm():
    """H_1 torsion = Z/gcd(a,b) + Z/lcm(a,b), the general form."""
    import math
    for a in range(1, 12):
        for b in range(1, 12):
            g, l = math.gcd(a, b), a * b // math.gcd(a, b)
            assert torsion(a, b) == sorted([g, l]), (a, b, torsion(a, b), g, l)


def test_only_the_golden_is_a_knot_complement_in_the_wider_family():
    """THE PRICE OF THE PERIOD-ONE RESTRICTION: relaxing it changes nothing.

    A knot complement in S^3 has H_1 = Z, so the torsion must vanish; that needs
    gcd(a,b) = lcm(a,b) = 1, i.e. a = b = 1.
    """
    hits = [(a, b) for a in range(1, 40) for b in range(1, 40)
            if torsion(a, b) == [1, 1]]
    assert hits == [(1, 1)], hits


def test_the_widening_is_not_vacuous():
    """A control: period two really does contain members outside the metallic family.

    If it did not, the pricing would be empty -- we would have 'widened' to the same
    set. (2,3) has trace 8, which is not of the form m^2+2 for integer m.
    """
    assert torsion(2, 3) == [1, 6]                      # a genuine new member
    tr = int(M(2, 3).trace())
    assert tr == 8
    assert not sp.sqrt(tr - 2).is_integer               # 6 is not a perfect square
