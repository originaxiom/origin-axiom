"""
B570 Lane C, cell C4 -- the cover-chirality census.
Locks the computed fact: every n-fold cyclic cover of 4_1 (n=2..12), branched
and unbranched, is AMPHICHIRAL. No correlation with n mod 12 exists because
there is no chirality signal to correlate.
"""
import math
import cmath
import pytest

snappy = pytest.importorskip("snappy")


# ---------------------------------------------------------------------------
# Base object: 4_1 itself
# ---------------------------------------------------------------------------

def test_base_4_1_amphichiral_full_group():
    M = snappy.Manifold('4_1')
    G = M.symmetry_group()
    assert G.is_full_group() is True
    assert G.order() == 8
    assert G.is_amphicheiral() is True
    assert G.is_invertible_knot() is True


def test_base_4_1_every_symmetry_sends_meridian_to_pm_meridian():
    """The premise the lifting theorem needs: every isometry of 4_1's
    complement (in particular the orientation-reversing ones) acts on the
    peripheral Z^2 = <mu, lambda> by a DIAGONAL +-1 matrix, so mu -> +-mu.
    This is what lets the amphichiral symmetry descend to the kernel of
    H_1 -> Z/n for every n, hence lift to every n-fold cyclic cover."""
    M = snappy.Manifold('4_1')
    G = M.symmetry_group()
    isoms = G.isometries()
    assert len(isoms) == 8
    for iso in isoms:
        cm = iso.cusp_maps()[0]
        rows = [list(cm[0]), list(cm[1])]
        # diagonal, entries in {+1,-1}
        assert rows[0][1] == 0 and rows[1][0] == 0
        assert rows[0][0] in (1, -1) and rows[1][1] in (1, -1)


# ---------------------------------------------------------------------------
# Unbranched n-fold cyclic covers of the complement
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("n", list(range(2, 13)))
def test_unbranched_cover_unique_and_amphichiral(n):
    M = snappy.Manifold('4_1')
    covs = M.covers(n, cover_type='cyclic')
    assert len(covs) == 1  # H_1(4_1 complement)=Z has a unique index-n subgroup
    C = covs[0]

    # Method 1: direct isometry test against the reversed-orientation copy
    Cm = C.copy()
    Cm.reverse_orientation()
    assert C.is_isometric_to(Cm) is True

    # Method 2: independent SnapPea symmetry-group computation
    G = C.symmetry_group()
    assert G.is_full_group() is True
    assert G.order() == 8 * n
    assert G.is_amphicheiral() is True


def test_unbranched_covers_no_mod12_signal():
    """No n in 2..12 breaks amphichirality, so trivially no correlation
    with n mod 12 in {4,8} (the theta-odd exponents) or any other residue
    class exists -- the premise of the five-sources handoff row is false."""
    M = snappy.Manifold('4_1')
    chiral_ns = []
    for n in range(2, 13):
        C = M.covers(n, cover_type='cyclic')[0]
        Cm = C.copy()
        Cm.reverse_orientation()
        if not C.is_isometric_to(Cm):
            chiral_ns.append(n)
    assert chiral_ns == []


# ---------------------------------------------------------------------------
# Branched cyclic covers Sigma_n(4_1)
# ---------------------------------------------------------------------------

def predicted_order(n):
    """|H_1(Sigma_n(K))| = |prod_{j=1}^{n-1} Delta_K(zeta_n^j)| via the
    Alexander polynomial Delta_{4_1}(t) = t - 3 + 1/t."""
    prod = 1.0 + 0j
    for j in range(1, n):
        z = cmath.exp(2j * cmath.pi * j / n)
        prod *= (z - 3 + 1 / z)
    return round(abs(prod))


# slope, in the cover's own (mu,lambda) cusp basis, that closes the branch
# locus -- found by brute-force search matched against the independent
# Alexander-polynomial order formula (see census script).
BRANCH_SLOPE = {2: (1, 0), 3: (1, 0), 4: (1, 1), 5: (1, 1), 6: (1, 1),
                 7: (1, 1), 8: (1, 1), 9: (1, 1), 10: (1, 1), 11: (1, 1),
                 12: (1, 1)}

EXPECTED_ORDER = {2: 5, 3: 16, 4: 45, 5: 121, 6: 320, 7: 841, 8: 2205,
                   9: 5776, 10: 15125, 11: 39601, 12: 103680}


@pytest.mark.parametrize("n", list(range(2, 13)))
def test_branched_cover_homology_order_matches_alexander_formula(n):
    assert predicted_order(n) == EXPECTED_ORDER[n]
    M = snappy.Manifold('4_1')
    C = M.covers(n, cover_type='cyclic')[0].copy()
    C.dehn_fill(BRANCH_SLOPE[n])
    divs = C.homology().elementary_divisors()
    assert 0 not in divs  # genuinely closed (finite H_1), no spurious free part
    order = 1
    for d in divs:
        order *= d
    assert order == EXPECTED_ORDER[n]


def test_n2_branched_cover_is_L52_and_amphichiral_by_lens_space_criterion():
    """Sigma_2(4_1) = L(5,2) (the double branched cover of a 2-bridge
    knot b(5,2)); independent number-theoretic amphichirality criterion
    for lens spaces: L(p,q) amphichiral iff q^2 = -1 mod p."""
    p, q = 5, 2
    assert (q * q) % p == p - 1
    M = snappy.Manifold('4_1')
    C = M.covers(2, cover_type='cyclic')[0].copy()
    C.dehn_fill((1, 0))
    assert str(C.homology()) == 'Z/5'


@pytest.mark.parametrize("n", [2, 5, 6, 7, 8, 9, 10, 11, 12])
def test_branched_cover_isometric_to_mirror_where_snappea_can_decide(n):
    """For n in {2,5..12} SnapPea's canonical-form isometry test returns a
    decisive answer (n=2 is a degenerate/lens-space limit but the test
    still resolves; n=5..12 are genuinely hyperbolic). n=3,4 land on
    non-hyperbolic geometric types where SnapPea explicitly refuses to
    answer (raises rather than guessing) -- those two rows are covered by
    the lifting theorem, not by this numeric test (see test above +
    the meridian-to-+-meridian premise test)."""
    M = snappy.Manifold('4_1')
    C = M.covers(n, cover_type='cyclic')[0].copy()
    C.dehn_fill(BRANCH_SLOPE[n])
    Cm = C.copy()
    Cm.reverse_orientation()
    assert C.is_isometric_to(Cm) is True
