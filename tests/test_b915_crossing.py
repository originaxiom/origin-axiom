"""B915 locks. Pre-results: the seal. The verdict locks append at banking."""
import hashlib
import os

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B915_the_crossing")
SEALED_SHA = "7a423aed95afc9a3e2edc79806c83cda9a592e8a079e81525c389febfe6d34de"


def test_crossing_seal_unbroken():
    with open(os.path.join(ARC, "PREREGISTRATION.md"), "rb") as f:
        assert hashlib.sha256(f.read()).hexdigest() == SEALED_SHA
