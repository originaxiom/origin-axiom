"""B912 locks. Pre-results: the seal. Results locks appended at banking."""
import hashlib
import os

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B912_norm_cell")
SEALED_SHA = "93d420ea26d4fb75114d247cfa066837bb635022fd4db7c4315ad7587dbd98c0"


def test_prereg_seal_unbroken():
    with open(os.path.join(ARC, "PREREGISTRATION.md"), "rb") as f:
        assert hashlib.sha256(f.read()).hexdigest() == SEALED_SHA


def _res():
    import json
    with open(os.path.join(ARC, "results.json")) as f:
        return json.load(f)


def test_outcome_B_structured():
    r = _res()
    t = str(r)
    # nine colorless positive-definite, six colored indefinite (1,2,0)
    assert "OUTCOME B" in t or "outcome_B" in t or r.get("outcome") == "B"


def test_signature_15_12():
    r = _res()
    t = str(r)
    assert "(15, 12)" in t or "[15, 12]" in t or '"signature": [15, 12]' in t
