"""B913 locks: the R3c design seal + the no-substitution clause."""
import hashlib
import os

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B913_r3c_design")
SEALED_SHA = "8afdc2f88c55bd36818748acb13c8b61a770d18906e2b2c030b47ac05770879a"


def test_design_seal_unbroken():
    with open(os.path.join(ARC, "PREREGISTRATION.md"), "rb") as f:
        assert hashlib.sha256(f.read()).hexdigest() == SEALED_SHA


def test_no_substitution_clause_present():
    with open(os.path.join(ARC, "PREREGISTRATION.md")) as f:
        t = " ".join(f.read().split())
    assert "NO alternative magnitude may enter" in t
    assert "never substituted into" in t
