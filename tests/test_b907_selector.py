"""B907 locks. Pre-results: the seal. Results locks appended at banking."""
import hashlib
import os

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier",
                   "B907_real_form_selector")
SEALED_SHA = "cd7aae3b1e102359f40fa0e6d3db12a08d68517bff263dd2f7f80548ba518690"


def test_prereg_seal_unbroken():
    with open(os.path.join(ARC, "PREREGISTRATION.md"), "rb") as f:
        assert hashlib.sha256(f.read()).hexdigest() == SEALED_SHA
