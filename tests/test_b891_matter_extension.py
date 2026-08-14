"""Locks B891 -- the sealed matter-extension cell."""
import hashlib
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B891_matter_extension"
RES = json.loads((_D / "results.json").read_text(encoding="utf-8"))
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split()).lower().replace("*", "")


def test_seal_unbroken():
    h = hashlib.sha256((_D / "PREREGISTRATION.md").read_bytes()).hexdigest()
    assert h == (_D / "seal.txt").read_text().split()[0]
    assert h.startswith("a08398c5")


def test_distinct_all_frames():
    assert RES["overall"] == "DISTINCT"
    for ri in ("0", "1", "2"):
        assert RES["frames"][ri]["verdict"] == "DISTINCT"
        assert float(RES["frames"][ri]["max_dev"]) > 1e-6


def test_the_fence_and_the_next_layer():
    assert "the solo seat's §5 fence stands" in _F
    assert "not decided" in _F and "mechanism-hood" in _F
    assert "recorded, not interpreted" in _F
