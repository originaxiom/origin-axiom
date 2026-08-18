"""B8073 locks -- the object's su(5) is NOT tau-stable.

The reproducer sweeps ~1557 characters at each of three primes and takes minutes, so the
locks read the arc's per-prime results files and assert the MATHEMATICS recorded there,
plus recompute the structural fact tau rests on.  Nothing asserts prose.
"""
import glob
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARC = os.path.join(ROOT, "frontier", "B8073_su5_reality")
sys.path.insert(0, os.path.join(ROOT, "frontier", "B8068_j2t_charge_field"))
import e8_build as E  # noqa: E402

PRIMES = (811, 991, 1093)


def _res():
    out = {}
    for f in glob.glob(os.path.join(ARC, "results_p*.json")):
        d = json.load(open(f))
        out[d["prime"]] = d
    return out


def test_all_three_split_primes_were_run():
    assert set(_res()) == set(PRIMES)


def test_the_banked_identity_reproduces_at_every_prime():
    """Nothing may be read until A = Stab(e_i, ebar_j, s) reproduces at (34, 24)."""
    for p, d in _res().items():
        assert d["A_dim_killingrank"] == [34, 24], f"A did not reproduce at p={p}"


def test_the_intertwining_gate_passes_everywhere():
    """T(X.v) = theta(X).T(v) over all 78 x 27 = 2106 pairs -- the check that is absent
    from cell16_reality.py, cell18_realforms.py and cell20_outer.py."""
    for p, d in _res().items():
        assert d["intertwining_pairs_tested"] == 78 * 27
        assert d["intertwining_failures"] == 0, f"tau does not intertwine at p={p}"


def test_no_character_in_the_swept_family_gives_killing_rank_24():
    """The headline.  The panel's (24,24) does not reproduce."""
    for p, d in _res().items():
        assert d["characters_giving_killing_rank_24"] == 0, f"rank 24 appeared at p={p}"


def test_the_generic_character_control_is_clean():
    """If random characters gave 24 the instrument would be measuring nothing."""
    for p, d in _res().items():
        assert d["random_characters_giving_24"] == 0


def test_the_instrument_can_still_say_45():
    """Instrument negative control: on the object the 254-case sweep actually measured,
    Stab(s) ^ Stab(tau s) must still return the banked (45, 45) -- so the declared
    alternative outcome was reachable and a 24 was not excluded by the tool."""
    for p, d in _res().items():
        assert d["instrument_negative_control_Stab_s"] == [45, 45]


def test_the_panels_discriminating_filter_discriminates_nothing():
    """tau(A) = (34,24) was reported as the filter pinning the spinor conjugation.
    It holds for every character swept, so it separates nothing."""
    for p, d in _res().items():
        assert d["tau_of_A_is_always_34_24"] is True


def test_the_negation_map_27_to_27bar_is_a_bijection():
    """RECOMPUTED, not read: tau rests on r -> -r carrying the 27 onto the 27-bar.
    In the E8 grading, r[6] % 3 == 1 for the 27 and == 2 for the 27-bar, so negation
    swaps the blocks; if it did not, no character-built tau could exist at all."""
    t27 = [r for r in E.ROOTS if r[6] % 3 == 1 and r[7] == 0]
    tbar = {r for r in E.ROOTS if r[6] % 3 == 2 and r[7] == 0}
    assert len(t27) == 27 and len(tbar) == 27
    assert all(tuple(-x for x in r) in tbar for r in t27)


def test_the_swept_family_is_recorded_so_the_negative_is_scoped():
    """An unearned negative is as bad as numerology: the arc must record WHAT was swept,
    so the claim is 'no character in this family', never 'no conjugation exists'."""
    for p, d in _res().items():
        cs = d["characters_swept"]
        assert cs["two_torsion_slice"] == 65
        assert cs["uniform_mu_family"] == p - 1
        assert cs["random_control"] == 400
        assert "NOT swept" in d["scope"]
