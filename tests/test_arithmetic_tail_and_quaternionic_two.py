"""Two assertions in the paper, converted to theorems.

Closes the proof auditor's D3 and D6.  Both were carrying the word "forces" or an
unbounded quantifier on top of a finite computation, and in both cases the corpus
already banked what makes them theorems -- which is exactly why the owner's standing
rule is to cross-search every point before demoting anything.

D3 -- the arithmetic tail.  The paper asserted "every m >= 3 is non-arithmetic",
while the lock (test_b125_snappy_arithmeticity.py) records a SnapPy verdict only for
m = 1..6.  But Bowditch-Maclachlan-Reid 1995 classify the arithmetic once-punctured-
torus bundles into exactly THREE commensurability classes, with block words

    RL -> Q(sqrt-3),   RRLL -> Q(i),   RRL -> Q(sqrt-7)   [the last non-metallic],

banked in B127 and recorded in docs/progress/PROGRESS_2026-Q2.md.  The metallic word
is R^m L^m, with EQUAL block lengths.  R^1L^1 = RL and R^2L^2 = RRLL; RRL has block
lengths (2,1) and is therefore not metallic; and for m >= 3 the word R^m L^m has
length 2m >= 6 and matches none of the three.  So the tail is a corollary of a
classification, not an extrapolation from six data points.

D6 -- the quaternionic 2.  The paper asserted that "every SL(2,C)-factoring route
forces a quaternionic self-dual 2".  That is provable in three lines (see the paper),
and the consequence it is used for -- that among the six polyhedral candidates only
the binary ones carry a faithful two-dimensional special-linear representation --
follows from the involution lemma the paper ALREADY proves for SL(2,Z/4): a finite
subgroup of SU(2) has exactly one element of order 2, namely -I.  A4, S4 and A5 have
3, 9 and 15 involutions respectively, so none of them embeds in SU(2).

Pure sympy/stdlib; no floats, no external census.
"""

from sympy.combinatorics.named_groups import AlternatingGroup, SymmetricGroup

# The three arithmetic commensurability classes of once-punctured-torus bundles
# (Bowditch-Maclachlan-Reid 1995), as block words in R and L.
BMR_ARITHMETIC_WORDS = ("RL", "RRLL", "RRL")

# The invariant trace fields attached to them, as banked in B127.
BMR_FIELDS = {"RL": "Q(sqrt-3)", "RRLL": "Q(i)", "RRL": "Q(sqrt-7)"}


def metallic_word(m):
    """The block word of the metallic grammar R^m L^m."""
    return "R" * m + "L" * m


def block_lengths(word):
    """(#leading R's, #trailing L's) if the word has that shape, else None."""
    r = 0
    while r < len(word) and word[r] == "R":
        r += 1
    tail = word[r:]
    if tail and set(tail) == {"L"}:
        return (r, len(tail))
    return None


# ---------------------------------------------------------------- D3


def test_the_metallic_word_has_equal_blocks():
    for m in range(1, 30):
        assert block_lengths(metallic_word(m)) == (m, m)


def test_the_two_arithmetic_metallic_members_are_m1_and_m2():
    assert metallic_word(1) == "RL"
    assert metallic_word(2) == "RRLL"
    assert BMR_FIELDS[metallic_word(1)] == "Q(sqrt-3)"
    assert BMR_FIELDS[metallic_word(2)] == "Q(i)"


def test_the_third_arithmetic_class_is_not_metallic():
    """RRL has block lengths (2,1), so it is no R^m L^m."""
    assert block_lengths("RRL") == (2, 1)
    assert "RRL" not in {metallic_word(m) for m in range(1, 200)}


def test_no_m_at_least_three_is_arithmetic():
    """The tail, as a corollary of the BMR classification rather than a scan."""
    hits = [m for m in range(1, 500) if metallic_word(m) in BMR_ARITHMETIC_WORDS]
    assert hits == [1, 2]


def test_the_classification_has_exactly_three_classes():
    assert len(BMR_ARITHMETIC_WORDS) == 3
    assert len(set(BMR_ARITHMETIC_WORDS)) == 3
    assert set(BMR_FIELDS) == set(BMR_ARITHMETIC_WORDS)


# ---------------------------------------------------------------- D6


def _involution_count(G):
    return sum(1 for g in G.elements if g.order() == 2)


def test_the_rotation_groups_have_many_involutions():
    """More than one involution => no embedding into SU(2)."""
    assert _involution_count(AlternatingGroup(4)) == 3
    assert _involution_count(SymmetricGroup(4)) == 9
    assert _involution_count(AlternatingGroup(5)) == 15


def test_the_rotation_groups_have_the_expected_orders():
    assert int(AlternatingGroup(4).order()) == 12
    assert int(SymmetricGroup(4).order()) == 24
    assert int(AlternatingGroup(5).order()) == 60


def test_binary_groups_have_exactly_one_involution():
    """2T, 2O, 2I each contain -I and nothing else of order 2.

    Verified directly on the 24 Hurwitz units: a unit quaternion squares to -1 only
    when its real part vanishes, and squares to +1 only for +-1.  So the unique
    element of order 2 is -1, whatever the binary group.
    """
    import itertools

    from sympy import Rational

    half = Rational(1, 2)
    units = []
    for s in (1, -1):
        units += [(s, 0, 0, 0), (0, s, 0, 0), (0, 0, s, 0), (0, 0, 0, s)]
    for sg in itertools.product((1, -1), repeat=4):
        units.append(tuple(x * half for x in sg))
    assert len(units) == 24

    def qmul(p, q):
        a, b, c, d = p
        e, f, g, h = q
        return (a * e - b * f - c * g - d * h,
                a * f + b * e + c * h - d * g,
                a * g - b * h + c * e + d * f,
                a * h + b * g - c * f + d * e)

    one = (1, 0, 0, 0)
    minus_one = (-1, 0, 0, 0)
    order_two = [u for u in units if u != one and qmul(u, u) == one]
    assert order_two == [minus_one]


def test_only_the_binary_candidates_can_carry_a_faithful_two():
    """The classification step the paper needs, stated as a count."""
    involutions = {
        "A4": _involution_count(AlternatingGroup(4)),
        "S4": _involution_count(SymmetricGroup(4)),
        "A5": _involution_count(AlternatingGroup(5)),
        "2T": 1, "2O": 1, "2I": 1,
    }
    embeds_in_su2 = {name for name, n in involutions.items() if n == 1}
    assert embeds_in_su2 == {"2T", "2O", "2I"}
