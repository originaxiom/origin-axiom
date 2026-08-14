"""B929 locks. Pre-results: the seal."""
import hashlib
import os

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier",
                   "B929_third_crossing")
SEALED_SHA = "672b5afb30d9cee143d81b5bfd5f0b0ba8986400a599ea7903b0c5da1324c65e"


def test_crossing3_seal_unbroken():
    with open(os.path.join(ARC, "PREREGISTRATION.md"), "rb") as f:
        assert hashlib.sha256(f.read()).hexdigest() == SEALED_SHA


def _res():
    import json
    with open(os.path.join(ARC, "results.json")) as f:
        return json.load(f)


def test_verdict_hit_shape_verbatim():
    r = _res()
    assert r["sealed_verdict"] == "HIT-SHAPE"
    assert r["T1"]["pass"] is True
    assert r["T2"]["pass"] is False
    assert 1 < r["T1"]["a"] < 3


def test_the_blind_triple_and_the_gap():
    r = _res()
    s = r["object_triple_s"]
    assert abs(s[0] - 0.862898) < 1e-4
    # the quantitative gap: both forward ratios off by > 2x
    assert all(x > 2 for x in r["T2"]["ratios_fwd"])


def test_priced_bits_recorded():
    assert _res()["priced_bits"] == 2
