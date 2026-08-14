"""B1037 + B1038 locks — the θ-join (DISTINCT) and the retrieval arc."""
import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_b1037_verdict_and_record():
    ARC = ROOT / "frontier" / "B1037_theta_join"
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1037" and v["verdict"] == "PROVED"
    assert "DISTINCT" in v["claim_one_line"]
    assert "WRONG" in v["claim_one_line"]          # the prior scored honestly
    assert "J^2 = +1" in v["claim_one_line"]
    log = (ARC / "b1037_output.txt").read_text(encoding="utf-8")
    assert "VERDICT: DISTINCT" in log
    assert "J^2 scalar: True" in log
    flat = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8")
                    .replace("**", "").split())
    assert "prior was wrong" in flat.lower() or "prior (JOINED, weak) was WRONG" in flat
    assert "for the sealed projection" in flat      # the scope fence
    hashes = (ARC / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8")
    m = re.search(r"^([0-9a-f]{64})", hashes, re.M)
    assert m and m.group(1).startswith("63cd367a")
    import hashlib
    assert hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest() == m.group(1)


def test_b1038_census_reproduction():
    ARC = ROOT / "frontier" / "B1038_retrieval_typing"
    spec = importlib.util.spec_from_file_location("b1038_verify", ARC / "b1038_verify.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    r = mod.v1_census()
    assert r["internally consistent"]
    assert r["lines banking a 3+dp decimal"] == r["of those mentioning invariance-family keywords"] + r["without (the at-risk set)"]
    r2 = mod.v2_gauge_aware_floor()
    assert r2["single-vocabulary undercounts (the synonym-set principle)"]
    r3 = mod.v3_docs_installed()
    assert all(r3.values()), r3


def test_b1038_verdict():
    ARC = ROOT / "frontier" / "B1038_retrieval_typing"
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1038" and v["verdict"] == "PROVED"
    assert "REPRODUCED EXACTLY" in v["claim_one_line"]
    assert "not conflated" in v["claim_one_line"]
