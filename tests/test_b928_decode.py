"""B928 locks. Pre-results: the seal."""
import hashlib
import os

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B928_d2_decode")
SEALED_SHA = "5a7aa9731b227d0d9ca7c4f56c4787f8f035fcfe2becddf996c85f1e3f14eba8"


def test_decode_seal_unbroken():
    with open(os.path.join(ARC, "PREREGISTRATION.md"), "rb") as f:
        assert hashlib.sha256(f.read()).hexdigest() == SEALED_SHA
