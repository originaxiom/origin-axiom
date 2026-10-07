"""sm:B1552 THE CHIRAL TRIPLET'S COUNT -- the lock on the banked record (reads only; writes nothing tracked).

The seal's hashes, the complete record (432 readings per route), the read-out's verdict, and the counts: every reading
(0, 0), the two routes and the draws agreeing.
"""
import gzip
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1552_the_chiral_triplets_count"
VER = ARC / "verification"
SEAL_SHA = "556910b631c715867352057dad3401a50b41e949c077bdcf9ef58178f0c20e69"


def _rows(route):
    with gzip.open(VER / f"run_{route}.jsonl.gz", "rt") as f:
        return [json.loads(line) for line in f]


def test_seal_hash():
    assert hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest() == SEAL_SHA


def test_artifact_hashes():
    for line in (ARC / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        digest, name = line.split()
        assert hashlib.sha256((ARC / name).read_bytes()).hexdigest() == digest, name


def test_record_complete():
    for route in (1, 2):
        rows = _rows(route)
        done = {r["state"] for r in rows if r.get("done")}
        readings = [r for r in rows if "count" in r]
        assert len(done) == 12 and len(readings) == 432, (route, len(done), len(readings))


def test_every_count_zero_and_routes_agree():
    c1 = Counter(tuple(r["count"]) for r in _rows(1) if "count" in r)
    c2 = Counter(tuple(r["count"]) for r in _rows(2) if "count" in r)
    assert c1 == c2 == Counter({(0, 0): 432})


def test_read_out_verdict():
    d = json.loads((VER / "read_out.json").read_text(encoding="utf-8"))
    assert d["complete"] and d["P1"] and d["P2"] and d["P3"] and d["P4"]
    assert not any(v for m in d["P5"].values() for v in m.values())
    assert d["verdict"] == "NEGATIVE as sealed"


def test_identity_held():
    d = json.loads((VER / "identity.json").read_text(encoding="utf-8"))
    assert d["all held"] is True and d["I1"]["counts"] == [[-1, -1], [-1, -1]]


def test_arc_verdict():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1552" and d["verdict"] == "NEGATIVE" and d["instrument"] is False
    assert "|" not in d["claim_one_line"]


def test_w11_the_zero_is_a_theorem_checked():
    d = json.loads((ROOT / "docs" / "dossiers" / "the_weave_2026-10-07" / "the_spin_zero.json").read_text(encoding="utf-8"))
    assert d["all held"] is True
    assert d["(1) T2 on sm:B1552's record"]["readings"] == 864
    assert d["(2) the act on V is in a finite group, every state to length 12"]["states"] == 758
