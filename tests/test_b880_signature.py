"""Locks B880 -- the module-level magic-square signature."""
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B880_triality_signature"
RES = json.loads((_D / "results.json").read_text(encoding="utf-8"))
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split()).lower().replace("*", "")


def test_the_skeleton():
    assert RES["core_dim"] == 30 and RES["so8_dim"] == 28
    assert RES["sector_dims"] == [16, 16, 16]
    assert RES["charge_split"] == [[8, 8], [8, 8], [8, 8]]


def test_pairwise_inequivalent_with_certificates():
    assert RES["pairwise_inequivalent"] is True
    for i in range(3):
        for j in range(3):
            d, cert = RES["hom"][f"{i+1}{j+1}"]
            if i == j:
                assert d == 4 and float(cert) < 1e-20
            else:
                assert d == 0


def test_the_verdict_and_scope():
    assert RES["signature"].startswith("MAGIC-SQUARE COMPATIBLE")
    assert "the labels are relative" in _F or "the labels relative" in _F
    assert "priced, queued behind the 27 build" in _F
