"""B1187 lock -- the L187 depth-closure sitting."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1187_depth_closure"


def test_arc_verdict():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1187" and d["verdict"] == "PROVED" and d["instrument"] is True
    c = d["claim_one_line"]
    assert "REVERSES B189's C3" in c and "11 sigma" in c
    assert "LOGIC ERROR corrected" in c
    assert "estimator artifact" in c
    assert "PROVISIONAL" in c            # B500's kill not overclaimed


def test_wall7_committed_json():
    d = json.loads((ARC / "verification" / "wall7_all_t.json").read_text(encoding="utf-8"))
    assert d["deg_bound"] == 864 and d["points"] == 866
    qs = sorted(pr["q"] for pr in d["primes"])
    assert qs == [1009, 1999]
    for pr in d["primes"]:
        assert all(v[0] == 0 and v[1] == "degenerate" for v in pr["violations"])


def test_l310_and_l34_committed():
    l310 = json.loads((ARC / "verification" / "l310_per_level_null.json").read_text(encoding="utf-8"))
    assert l310["per_level"][-1]["z"] > 8          # the reversed clause's witness
    l34 = json.loads((ARC / "verification" / "l34_profile.json").read_text(encoding="utf-8"))
    assert l34["verdict"]["log_class_stable"] is True
    assert l34["controls"]["random"]["a"] < 0.05


def test_census_committed():
    d = json.loads((ARC / "verification" / "b500_mod2_census.json").read_text(encoding="utf-8"))
    by = {r["depth"]: r for r in d["depths"]}
    assert len(by[4]["signature_words"]) == 0      # depth 4 clean -- matches the hunt
    assert len(by[5]["signature_words"]) == 50     # the route-killer
    assert by[10]["words"] == 55980                # the full sweep reached depth 10


def test_findings_honesty():
    t = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "none executed" in t and "STALE" in t   # the registration correction
    assert "estimator artifact" in t or "estimator" in t
    assert "index caveat" in t                     # the census's stated bound
