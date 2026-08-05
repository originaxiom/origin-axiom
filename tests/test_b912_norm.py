"""B912 locks. Pre-results: the seal. Results locks appended at banking."""
import hashlib
import os

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B912_norm_cell")
SEALED_SHA = "93d420ea26d4fb75114d247cfa066837bb635022fd4db7c4315ad7587dbd98c0"


def test_prereg_seal_unbroken():
    with open(os.path.join(ARC, "PREREGISTRATION.md"), "rb") as f:
        assert hashlib.sha256(f.read()).hexdigest() == SEALED_SHA
