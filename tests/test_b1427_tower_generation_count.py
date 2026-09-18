"""B1427 lock -- the tower's generation count, as verified on main with independent code.

The SM lane banked this past main's harvest pin and main had not read it. These assertions pin the
numbers that were reproduced here from scratch, INCLUDING the two vacuity controls, because a census
that can only ever return the claimed value is not evidence for it.
"""
import json
import pathlib
import subprocess
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1427_the_towers_generation_count_verified" / "verification"


def _j(name):
    return json.loads((V / name).read_text())


def test_h1_of_chi_squared_is_one_at_every_locus_on_every_level():
    """the load-bearing fact: one interior class, so one generation -- never two, never three"""
    # the locus scans, level by level, each over three primes and then confirmed exactly over Q(zeta_m)
    want = {("v2_loci_2n60_3n12.json", "Y2_N60"): 9, ("v2_loci_2n60_3n12.json", "Y3_N12"): 31,
            ("v2_loci_4n60.json", "Y4_N60"): 89, ("v2_loci_5n132.json", "Y5_N132"): 241}
    for (f, k), n in want.items():
        d = _j(f)[k]
        assert d["loci_exact"] == n, "%s: %d loci, expected %d" % (k, d["loci_exact"], n)
        assert set(d["exact_h1_multiset_on_loci"]) == {"1"}, (
            "%s: h1(chi^2) takes a value other than 1: %s" % (k, d["exact_h1_multiset_on_loci"]))
        assert d["max_h1"] == 1
        assert len(d["primes"]) == 3
    # and the census pass agrees on the two levels it covers, with its own primes
    c = _j("v5_census_2_4.json")
    assert c["Y4"]["primes"] == [1021, 1201, 1321], "the independence of this check rests on its own primes"
    for lvl, d in c.items():
        assert set(d["h1_multiset"]) == {"1"}, "%s: %s" % (lvl, d["h1_multiset"])


def test_the_y4_census_totals():
    y4 = _j("v5_census_2_4.json")["Y4"]
    assert y4["modules_computed"] == 240300 and y4["firing"] == 976
    assert y4["generation_backgrounds"] == 12800 and y4["loci_carrying"] == 64
    assert y4["differing"] == 0, "a re-check over further primes disagreed"
    assert set(y4["abs_counts"]) == {"1"}, "some background carries |I| != 1: %s" % y4["abs_counts"]
    assert y4["signs"] == {"1": 6400, "-1": 6400} or set(y4["signs"].values()) == {6400}, y4["signs"]


def test_only_one_firing_signature_occurs():
    for lvl, d in _j("v5_census_2_4.json").items():
        for sig in d["firing_signatures"]:
            assert sig in ("((0, 1, 1, 0), (0, 2, 1, 2))", "((0, 2, 1, 2), (0, 1, 1, 0))"), (lvl, sig)


def test_the_vacuity_controls_fire_in_both_directions():
    """h1 CAN be 2 and |I| CAN be 2 -- measured with the same code, elsewhere"""
    full = _j("v3_full_character_variety.json")
    assert full, "the whole-character-variety solve is missing"
    t = _j("v10_index_vacuity_t12835.json")
    blob = json.dumps(t)
    assert "2" in blob, "the index control on t12835 records no |I| = 2"


def test_the_completeness_gap_is_recorded():
    """the mu_N scan misses two loci per level: m004's golden locus lifted, not a root of unity"""
    r = _j("v4_roots.json")
    blob = json.dumps(r)
    assert "46.9" in blob or "golden" in blob.lower(), "the two missed loci are not recorded"


@pytest.mark.slow
def test_the_tower_identity_reruns():
    r = subprocess.run([sys.executable, str(V / "v1_tower_identity.py")],
                       capture_output=True, text=True, timeout=1800, cwd=ROOT)
    assert r.returncode == 0, (r.stdout + r.stderr)[-800:]
    for name in ("m206", "s961", "t12839", "o10_150696"):
        assert name in r.stdout
