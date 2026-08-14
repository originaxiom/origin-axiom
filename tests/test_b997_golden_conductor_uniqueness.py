"""B997 — the golden is the UNIQUE metallic grammar whose own-conductor shadow
is a McKay group.

THE PAPER'S DISCRIMINATING THEOREM, AND UNTIL NOW ITS WEAKEST VERIFICATION LINK.
`frontier/B997_golden_conductor_uniqueness/` contains FINDINGS.md and
arc_verdict.json and NO SCRIPT — the arc was banked as a proof on paper. B1019
locks the siblings' divergence and B1002 discharges the conductor identification,
but the uniqueness statement itself had no runnable check. §5.4 of the structure
paper says so in the paper's own voice; this file is what that sentence was
waiting for.

Everything here is exact integer / Fraction arithmetic. No floats appear in any
assertion, and in particular the completeness argument is made WITHOUT invoking
6/pi^2: the arc's FINDINGS bounds prod_{p|N}(1-1/p^2) below by 1/zeta(2) ~ 0.6079
and concludes |SL(2,Z/N)| >= 0.6079*N^3 > 120 for N >= 6. That is true but
irrational. The elementary bound below is exact and slightly stronger where it
matters.
"""

from fractions import Fraction
from sympy import primefactors


# --------------------------------------------------------------------------
# The group order
# --------------------------------------------------------------------------

def sl2_order(N):
    """|SL(2, Z/N)| = N^3 * prod_{p|N} (1 - 1/p^2). Exact."""
    order = Fraction(N**3)
    for p in primefactors(N):
        order *= Fraction(p * p - 1, p * p)
    assert order.denominator == 1
    return order.numerator


def sl2_order_bruteforce(N):
    """Count matrices [[a,b],[c,d]] over Z/N with ad - bc = 1. Ground truth."""
    return sum(
        1
        for a in range(N)
        for b in range(N)
        for c in range(N)
        for d in range(N)
        if (a * d - b * c) % N == 1
    )


def test_order_formula_matches_bruteforce():
    """The formula is not taken on trust; it is counted."""
    for N in range(2, 9):
        assert sl2_order(N) == sl2_order_bruteforce(N), N


# --------------------------------------------------------------------------
# Fact (1): |SL(2,Z/N)| is a McKay-group order for EXACTLY N in {3,4,5}
# --------------------------------------------------------------------------

# ORDERS of the binary polyhedral groups of the exceptional McKay series.
# NOTE the wording: these are the orders |2T| = 24, |2O| = 48, |2I| = 120.
# Whether SL(2,Z/N) *is* the corresponding group is a SEPARATE question, and the
# answer is not uniformly yes -- see test_which_are_actually_binary_polyhedral.
MCKAY_ORDERS = {24: "|2T| -> E6", 48: "|2O| -> E7", 120: "|2I| -> E8"}


def test_the_three_exceptional_hits():
    assert sl2_order(3) == 24
    assert sl2_order(4) == 48
    assert sl2_order(5) == 120
    assert set(MCKAY_ORDERS) == {24, 48, 120}


def sl2_elements(N):
    els = [(a, b, c, d)
           for a in range(N) for b in range(N) for c in range(N) for d in range(N)
           if (a * d - b * c) % N == 1]

    def mul(x, y):
        a, b, c, d = x
        e, f, g, h = y
        return ((a * e + b * g) % N, (a * f + b * h) % N,
                (c * e + d * g) % N, (c * f + d * h) % N)

    return els, mul


def count_involutions(N):
    """Number of elements of order exactly 2 in SL(2,Z/N)."""
    els, mul = sl2_elements(N)
    ident = (1, 0, 0, 1)
    return sum(1 for x in els if x != ident and mul(x, x) == ident)


def test_which_are_actually_binary_polyhedral():
    """CORRECTION to B997's table, found 2026-08-15 by checking rather than trusting.

    B997 tabulates N = 3, 4, 5 as 2T -> E6, 2O -> E7, 2I -> E8 and concludes
    that these are "exactly the three exceptional McKay groups ... the whole
    exceptional series and nothing else". The ORDER statement is correct. The
    GROUP statement is not, at N = 4.

    Every finite subgroup of SU(2) contains exactly ONE element of order 2 --
    the centre -I -- because a finite subgroup of the unit quaternions has a
    unique involution. So "has more than one involution" REFUTES membership in
    the binary polyhedral family outright.

        SL(2,Z/3):   1 involution  -> genuinely 2T   (classical)
        SL(2,Z/4):   7 involutions -> NOT 2O; |48| is a coincidence
        SL(2,Z/5):   1 involution  -> genuinely 2I   (classical)

    SL(2,Z/4) additionally has NO element of order 8, while 2O does.
    """
    assert count_involutions(3) == 1
    assert count_involutions(4) == 7
    assert count_involutions(5) == 1

    # 2O contains elements of order 8; SL(2,Z/4) does not.
    els, mul = sl2_elements(4)
    ident = (1, 0, 0, 1)

    def order(x):
        o, y = 1, x
        while y != ident:
            y = mul(y, x)
            o += 1
        return o

    assert 8 not in {order(x) for x in els}


def test_the_golden_landing_survives_the_correction():
    """The uniqueness conclusion is UNAFFECTED, and is in fact cleaner.

    The golden's landing is N = conductor(1) = 5, and SL(2,Z/5) IS genuinely 2I.
    So the one grammar that lands, lands on a real McKay group. If one demands a
    genuine binary polyhedral GROUP rather than a matching order, N = 4 drops
    out of the target set entirely -- and m^2 + 4 = 4 forced the degenerate
    m = 0 anyway, so no metallic word was ever there to lose.

    What the correction DOES cost is the flourish: the three N do NOT realise
    "the whole exceptional series". E6 and E8 are realised as groups; E7's slot
    is an order coincidence. The paper must not repeat that sentence.
    """
    assert conductor(1) == 5
    assert count_involutions(5) == 1          # genuinely 2I
    assert sl2_order(5) == 120

    genuine = [N for N in (3, 4, 5) if count_involutions(N) == 1]
    assert genuine == [3, 5], genuine         # E6 and E8 ends; no E7

    # the golden still lands, and now on a group rather than on a number
    assert conductor(1) in genuine


def test_prime_factor_product_bound_is_exact():
    """prod_{p|N} (1 - 1/p^2) >= (N+1)/(2N), with NO appeal to zeta(2).

    The primes dividing N are a subset of {2,...,N}, and every factor
    (1 - 1/k^2) lies in (0,1), so dropping to the full range only decreases
    the product:

        prod_{p|N} (1-1/p^2)  >=  prod_{k=2}^{N} (1-1/k^2)  =  (N+1)/(2N),

    the telescoping identity prod_{k=2}^{K} (k-1)(k+1)/k^2 = (K+1)/(2K).
    """
    for N in range(2, 60):
        prod = Fraction(1)
        for p in primefactors(N):
            prod *= Fraction(p * p - 1, p * p)
        assert prod >= Fraction(N + 1, 2 * N), N

    # the telescoping identity itself
    for K in range(2, 40):
        tel = Fraction(1)
        for k in range(2, K + 1):
            tel *= Fraction(k * k - 1, k * k)
        assert tel == Fraction(K + 1, 2 * K), K


def test_completeness_no_further_mckay_orders():
    """For every N >= 6, |SL(2,Z/N)| > 120, so the list {3,4,5} is COMPLETE.

    From the bound above,  |SL(2,Z/N)| >= N^3 * (N+1)/(2N) = N^2(N+1)/2,
    which at N = 6 is already 126 > 120 and is strictly increasing.
    This is a PROOF over the infinite family, not a bounded search.
    """
    def lower_bound(N):
        return Fraction(N * N * (N + 1), 2)

    assert lower_bound(6) == 126
    assert lower_bound(6) > 120

    # strictly increasing in N, so N = 6 settles every N >= 6
    for N in range(6, 200):
        assert lower_bound(N + 1) > lower_bound(N), N
        assert lower_bound(N) > 120, N
        assert sl2_order(N) >= lower_bound(N), N
        assert sl2_order(N) > 120, N

    # and nothing below 6 sneaks in besides the three
    hits = [N for N in range(2, 6) if sl2_order(N) in MCKAY_ORDERS]
    assert hits == [3, 4, 5]


# --------------------------------------------------------------------------
# Fact (2): the metallic conductor, and where the two facts meet
# --------------------------------------------------------------------------

def conductor(m):
    """The metallic grammar R^m L^m has own-conductor m^2 + 4 (B1002)."""
    return m * m + 4


def test_conductor_values():
    assert conductor(1) == 5      # golden
    assert conductor(2) == 8      # silver
    assert conductor(3) == 13


def test_the_two_facts_meet_at_exactly_one_m():
    """m^2 + 4 in {3,4,5} has the unique metallic solution m = 1.

        m^2 + 4 = 3  =>  m^2 = -1   no integer solution
        m^2 + 4 = 4  =>  m = 0      degenerate, not a metallic word
        m^2 + 4 = 5  =>  m = 1      THE GOLDEN, unique
    """
    solutions = {}
    for N in (3, 4, 5):
        target = N - 4
        # integer solutions of m^2 = target with m >= 1 (a metallic word needs m >= 1)
        found = [m for m in range(0, 100) if m * m == target]
        solutions[N] = found

    assert solutions[3] == []            # m^2 = -1
    assert solutions[4] == [0]           # m = 0, degenerate
    assert solutions[5] == [1]           # m = 1, the golden

    metallic = [m for N in (3, 4, 5) for m in solutions[N] if m >= 1]
    assert metallic == [1], metallic


def test_uniqueness_over_the_whole_family():
    """No metallic m >= 1 other than the golden lands on a McKay shadow.

    Checked directly far past the arc's m = 40, and closed for ALL m by the
    completeness theorem above: conductor(m) = m^2 + 4 >= 6 for every m >= 2,
    and no N >= 6 gives a McKay order.
    """
    landing = [m for m in range(1, 5000) if sl2_order(conductor(m)) in MCKAY_ORDERS]
    assert landing == [1], landing

    # the closure argument, stated as an assertion rather than a search
    for m in range(2, 5000):
        assert conductor(m) >= 6, m
        assert sl2_order(conductor(m)) > 120, m


def test_the_golden_lands_on_2I_the_E8_end():
    """SCOPE, kept with the theorem: the end reached is E8, not E6.

    conductor(1) = 5 and SL(2,Z/5) has order 120 = 2I -> E8, which per B248 is
    the SPHERICAL/fiber-field end. The E6 arrival comes via Q(sqrt-3) -> 2T,
    which B993 showed is class-level. This theorem does NOT establish
    object-specificity at the E6 end, and the paper's Section 5.4 must not be
    read as claiming it does.
    """
    assert sl2_order(conductor(1)) == 120
    assert MCKAY_ORDERS[120] == "|2I| -> E8"
    assert MCKAY_ORDERS[sl2_order(conductor(1))].endswith("E8")
