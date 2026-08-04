"""Locks B890 -- the sealed foreign-pair cell."""
import hashlib
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B890_foreign_pair"
RES = json.loads((_D / "results.json").read_text(encoding="utf-8"))
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split()).lower().replace("*", "")


def test_the_seal_is_unbroken():
    h = hashlib.sha256((_D / "PREREGISTRATION.md").read_bytes()).hexdigest()
    assert h == (_D / "seal.txt").read_text().split()[0]
    assert h.startswith("ea66fc34")


def test_the_verdict_distinct_all_frames():
    assert RES["overall"] == "DISTINCT"
    for ri in ("0", "1", "2"):
        fr = RES["frames"][ri]
        assert fr["verdict"] == "DISTINCT"
        assert float(fr["max_dev"]) > 1e-6


def test_the_prior_is_recorded_as_wrong():
    assert "the disclosed prior was wrong" in _F
    assert "that is the system working" in _F


def test_the_fence_and_the_continuation():
    assert "stands — strengthened as a candidate, not yet a mechanism" in _F
    assert "that is the next sealed cell" in _F
