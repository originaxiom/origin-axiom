"""B897 locks. Before results land, exactly one lock is meaningful: the seal.

The results locks are appended at banking; the sealed criteria are evaluated
verbatim in FINDINGS.md.
"""
import hashlib
import os

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B897_27_under_g20")
SEALED_SHA = "e293f095349b33ec0d29a9ff44755e779ec8eb7ebb9f394876b14979b60db205"


def test_prereg_seal_unbroken():
    with open(os.path.join(ARC, "PREREGISTRATION.md"), "rb") as f:
        assert hashlib.sha256(f.read()).hexdigest() == SEALED_SHA
