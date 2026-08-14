"""B915 locks. Pre-results: the seal. The verdict locks append at banking."""
import hashlib
import os

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B915_the_crossing")
SEALED_SHA = "7a423aed95afc9a3e2edc79806c83cda9a592e8a079e81525c389febfe6d34de"


def test_crossing_seal_unbroken():
    with open(os.path.join(ARC, "PREREGISTRATION.md"), "rb") as f:
        assert hashlib.sha256(f.read()).hexdigest() == SEALED_SHA


def _res():
    import json
    with open(os.path.join(ARC, "results.json")) as f:
        return json.load(f)


def test_sealed_verdict_is_miss_with_the_banked_distance():
    r = _res()
    assert r["sealed_verdict"] == "MISS"
    assert 15.0 < r["d_min_euclidean_sigma"] < 17.0


def test_failure_geometry_banked():
    r = _res()
    g = r["failure_geometry"]["pairwise_meeting_scales_GeV"]
    assert 1e13 < g["g1=g2"] < 1.2e13
    assert 1.5e14 < g["g1=g3"] < 2e14
    assert 2.5e16 < g["g2=g3"] < 3.5e16
    assert r["failure_geometry"]["alpha_s_gap_at_dmin"] > 0.03


def test_one_input_only():
    r = _res()
    assert set(r["input"].keys()) == {"inv_alpha_em_MZ", "sigma"}
