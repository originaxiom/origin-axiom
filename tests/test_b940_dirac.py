"""B940 locks. Pre-results: the seal + the O3 language gate."""
import hashlib
import os

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B940_dirac_sealed")
SEALED_SHA = "6c513b0634c743df4015fc694d5dbd23dbf38e35829b838012a71dbfa75311fe"


def test_dirac_seal_unbroken():
    with open(os.path.join(ARC, "PREREGISTRATION.md"), "rb") as f:
        assert hashlib.sha256(f.read()).hexdigest() == SEALED_SHA


def test_the_first_gate_is_stated():
    with open(os.path.join(ARC, "PREREGISTRATION.md")) as f:
        t = " ".join(f.read().split())
    assert 'No banked sentence may contain the word "first"' in t
    assert "MathSciNet/zbMATH grade" in t
