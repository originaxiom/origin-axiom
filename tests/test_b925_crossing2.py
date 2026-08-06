"""B925 locks. Pre-results: the seal. Verdict locks append at banking."""
import hashlib
import os

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier",
                   "B925_second_crossing")
SEALED_SHA = "5af3f09991bc38d9167eb0d1de7802bf469a46ea391de9b4676dd1a9042789bb"


def test_crossing2_seal_unbroken():
    with open(os.path.join(ARC, "PREREGISTRATION.md"), "rb") as f:
        assert hashlib.sha256(f.read()).hexdigest() == SEALED_SHA
