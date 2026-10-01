"""B1432 lock -- the three-fold cover fires off the lift.

Main's B1427 reported "Y_3: 0 firing". Its scan could only reach modules whose extension character is a square.
These assertions pin the complete census: on s961 all 72 firing modules sit on the 12 non-square loci and carry 48
generation-shaped backgrounds in 16 deck orbits of three, none of which lifts. The s961 census is recomputed live on
two fields (three primes, and exactly over Q(i)); the larger levels are pinned from the recorded runs.
"""
import json
import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1432_the_three_fold_cover_fires_off_the_lift" / "verification"
sys.path.insert(0, str(V))


def _j(name):
    return json.loads((V / name).read_text())


def test_s961_complete_census_live():
    """the load-bearing level, recomputed: 16 loci, 12 not squares, 72 firing, 48 backgrounds, 16 orbits of three"""
    import cover_census as cc
    o, bgs, I, chars, _ = cc.census(3, 4, 5000, verbose=False)
    assert (o["loci"], o["loci_nonsquare"], o["candidates"]) == (16, 12, 256)
    assert (o["firing"], o["firing_on_square_loci"], o["firing_on_nonsquare_loci"]) == (72, 0, 72)
    assert (o["generation_backgrounds"], o["lifted"]) == (48, 0)
    assert o["signs"] == {1: 24, -1: 24} and o["abs_counts"] == {1: 48}
    assert o["background_orbits"] == {"3": 16} and o["index_deck_invariant"] and o["background_orbits_closed"]
    assert o["differing_at_other_primes"] == 0 and o["h1_multiset"] == {"1": 16}


def test_the_lifted_scan_could_not_have_seen_it():
    """bite: restricted to square extension characters -- what B1427's scan reached -- s961 is silent"""
    import cover_census as cc
    o, bgs, I, chars, _ = cc.census(3, 4, 5000, verbose=False)
    squares = set(tuple((2 * x) % 4 for x in c) for c in chars)
    assert len(squares) == 4
    assert sum(1 for (lam, al) in I if lam in squares) == 0
    assert sum(1 for (lam, al) in I if lam not in squares) == 72


def test_the_root_and_the_odd_torsion_levels_reproduce_b1427():
    """controls: where every character is a square the complete census equals the lifted one"""
    import cover_census as cc
    for n, N, want in ((1, 1, (1, 0, 0, 0)), (2, 5, (5, 0, 8, 0))):
        o, *_ = cc.census(n, N, 3000, verbose=False)
        assert (o["loci"], o["loci_nonsquare"], o["firing"], o["generation_backgrounds"]) == want, n
    d = _j("census_M1_M5.json")
    assert (d["M4"]["firing"], d["M4"]["generation_backgrounds"], d["M4"]["lifted"]) == (488, 256, 256)   # x50 = 12 800
    assert (d["M5"]["firing"], d["M5"]["generation_backgrounds"], d["M5"]["lifted"]) == (2200, 400, 400)  # x2  = 800


@pytest.mark.slow
def test_s961_exact_over_Qi_equals_the_prime_field_table():
    """no prime field: the 256-module index table over Q(i) is the prime-field table, entry by entry"""
    import os
    os.environ["OA_CYC"] = "4"
    import cover_census as cc
    import exact_lib as E
    ng, rels, mu, lam, tau = cc.cover(3)
    chars = cc.characters(rels, mu, ng, 4)
    exact = {}
    for lc in chars:
        for al in chars:
            i = E.exact_index(3, 4, lc, al)
            if i:
                exact[(lc, al)] = i
    o, bgs, I, _, _ = cc.census(3, 4, 5000, verbose=False)
    assert exact == I and len(exact) == 72


def test_m6_recorded():
    o = _j("census_M6.json")["M6"]
    assert (o["loci"], o["loci_nonsquare"], o["candidates"]) == (320, 240, 102400)
    assert (o["firing"], o["firing_on_square_loci"], o["firing_on_nonsquare_loci"]) == (12536, 1352, 11184)
    assert (o["generation_backgrounds"], o["lifted"], o["not_lifted"]) == (2160, 336, 1824)
    assert o["backgrounds_by_orbit_size"] == {"6": 2112, "3": 48}
    assert o["abs_counts"] == {"1": 2160}


def test_the_bad_prime_is_recorded_and_isolated():
    """1721 invents 960 firings and loses 96; five other primes agree on all 12 536"""
    d = _j("m6_prime_diag.json")
    assert d["1721"]["firing"] == 13400 and d["1721"]["disagree_with_majority"] == 1056
    for p in ("1481", "1601", "2081", "2161", "2281"):
        assert d[p]["firing"] == 12536 and d[p]["disagree_with_majority"] == 0


def test_the_deck_word_map_is_conjugation_by_a_squared():
    """the web seat's map is the Schreier rewriting of g -> a^2 g a^-2; the substituted one is not"""
    import cover_census as cc
    n = 6
    web = {1: [1], 2: [4], 3: [5], 4: [6], 5: [7, -1], 6: [1, 2, -1], 7: [1, 3]}
    sub = {1: [1], 2: [4], 3: [5], 4: [6], 5: [7], 6: [1, 2, -1], 7: [1, 3, -1]}
    got = {g: cc.schreier([1, 1] + cc.base_word(g, n) + [-1, -1], n, 0) for g in range(1, 8)}
    assert all(got[g] == (web[g], 0) for g in range(1, 8))
    assert any(got[g][0] != sub[g] for g in range(1, 8))
