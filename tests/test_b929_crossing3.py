"""B929 locks. Pre-results: the seal."""
import hashlib
import os

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier",
                   "B929_third_crossing")
SEALED_SHA = "672b5afb30d9cee143d81b5bfd5f0b0ba8986400a599ea7903b0c5da1324c65e"


def test_crossing3_seal_unbroken():
    with open(os.path.join(ARC, "PREREGISTRATION.md"), "rb") as f:
        assert hashlib.sha256(f.read()).hexdigest() == SEALED_SHA
