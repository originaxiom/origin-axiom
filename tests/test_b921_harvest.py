"""B921 locks: the manifest + the seal verification."""
import os
ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B921_branch_harvest")


def test_manifest_and_seals():
    with open(os.path.join(ARC, "HARVEST_MANIFEST.md")) as f:
        m = f.read()
    for h in ("8424a335", "da516046", "3ba81779", "169e9042"):
        assert h in m
    assert "REGISTRATION OVER PRESERVATION" in m


def test_sealed_copies_exist():
    base = os.path.join(ARC, "harvested")
    found = 0
    for root, _, files in os.walk(base):
        for f in files:
            if "PREREGISTRATION" in f:
                found += 1
    assert found >= 4
