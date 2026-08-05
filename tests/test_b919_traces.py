"""B919 locks: the 3/8 traces at their honest tier."""
import json
import os

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B919_weinberg_traces")


def _res():
    with open(os.path.join(ARC, "results.json")) as f:
        return json.load(f)


def test_traces_at_40123():
    r = _res()
    line = " ".join(r["40123"])
    assert "Tr27(T3^2) = 3" in line
    assert "Tr27(Y^2) = 5" in line
    assert "Tr27(T3·Y) = 0" in line
    assert "3/8" in line


def test_honest_tier_recorded():
    r = _res()
    assert r["two_prime_traces_3_5_0"] is False
    assert "ONE-PRIME" in r["tier"]
    assert "OPEN" in r["second_prime_status"]
