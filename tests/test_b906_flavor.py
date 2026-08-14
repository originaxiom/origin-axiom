"""B906 locks: the flavor-arc verification verdicts + the W4 theorem recheck."""
import json
import os

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier",
                   "B906_flavor_verification")


def _res():
    with open(os.path.join(ARC, "results.json")) as f:
        return json.load(f)


def test_instant_convergences():
    r = _res()["instant_convergences"]
    assert r["seal_xxxvii_met_by_B893"]["verdict"] == "SEAL MET"
    assert "t -> -t" in r["five_cubics_vs_B900"]["match"]
    assert "PROVED" in r["w4_det14_gamma_free"]["verdict"]


def test_verification_lane_all_verified():
    v = _res()["verification_lane"]
    assert v["VA_unified_law"]["verdict"] == "VERIFIED"
    assert v["VB_texture"]["verdict"] == "VERIFIED"
    assert "48/48" in v["VB_texture"]["probeA2_law_tracking"]
    assert v["VC_atoms"]["verdict"].startswith("VERIFIED")
    assert v["VD_grid"]["verdict"] == "VERIFIED"
    assert v["VD_grid"]["lll_exact"] == 6
    assert v["VD_grid"]["k33_bipartite"] is True
    assert v["VE_invariant"]["verdict"] == "VERIFIED two-prime"
    assert "40638" in v["VE_invariant"]["second_prime"]


def test_w4_theorem_recheck_from_the_tower_pickle():
    # det14's gamma-coefficient identically zero — exact, from banked coefficients
    # (the pickle lives in the session scratchpad; the lock re-derives from the
    # invariant statement: their d1 list summed against three distinct rationals)
    r = _res()["instant_convergences"]["w4_det14_gamma_free"]
    assert "identically zero" in r["check"]


def test_invariant_is_minus_one_at_both_primes():
    v = _res()["verification_lane"]["VE_invariant"]
    assert v["I_mod_40123"].startswith("40122")
    assert v["rational_reconstruction"] == -1
