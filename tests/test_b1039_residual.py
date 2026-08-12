"""B1039 locks — the V-valued residual (sealed 874d9eee)."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1039_v_valued_residual"


def test_the_record_log():
    log = (ARC / "b1039_output.txt").read_text(encoding="utf-8")
    assert "h1(dbl; 27) = 5" in log
    assert log.count("dbl absent") == 15          # every pair, absent
    assert "PASS" in log and "CONTROL FAILED" not in log
    assert "EXISTENCE: NO -- the support is EMPTY" in log
    assert "conditional cell void" in log
    assert "['seam-born', 'seam-born', 'glued', 'glued', 'glued']" in log


def test_findings():
    flat = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8")
                    .replace("**", "").replace("−", "-").split())
    assert "sector-complete" in flat
    assert "closes completely" in flat
    assert "neither passed nor failed" in flat
    assert "three slots" in flat and "natural arity" in flat
    assert "prior HELD" in flat.lower() or "prior HELD" in flat


def test_verdict_and_seal():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1039" and v["verdict"] == "PROVED"
    assert "EXISTENCE NO, PRIOR HELD" in v["claim_one_line"]
    assert "NO TEST" in v["claim_one_line"]
    for dep in ("B632", "B1036"):
        assert dep in v["depends_on"]
    hashes = (ARC / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8")
    m = re.search(r"^([0-9a-f]{64})", hashes, re.M)
    assert m and m.group(1).startswith("874d9eee")
    import hashlib
    assert hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest() == m.group(1)
