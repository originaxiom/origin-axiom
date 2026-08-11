"""B1028 locks — the global freedom ledger (Lane I-1, sealed e13d09a5)."""
import importlib.util
import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1028_freedom_ledger"


def _walk():
    spec = importlib.util.spec_from_file_location("b1028_walk", ARC / "b1028_walk.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_links_all_cited_and_zero():
    m = _walk()
    L = m.links()
    # eleven arrows, none skipped; every priced zero must carry a cite (or the explicit
    # faces row whose content is the separation of ledgers)
    assert len(L) == 11
    assert all(r["price"] == 0.0 for r in L)
    cited = [r for r in L if r["cite"] != "--"]
    assert len(cited) == 10
    # the two named risks are present and marked resolved
    joined = " ".join(r["note"] for r in L)
    assert "NAMED RISK 1 IN THE SEAL, RESOLVED" in joined
    assert "NAMED RISK 2 IN THE SEAL, RESOLVED" in joined
    # the flags are not silently dropped
    assert "FLAG" in joined and "P5" in joined


def test_cite_machinery_actually_checks():
    """The desk audit must FAIL on a wrong phrase — the self-check is load-bearing."""
    m = _walk()
    try:
        m._cite("B994_rule_variation", "THIS PHRASE IS NOT IN THE BANKED VERDICT")
        raised = False
    except AssertionError:
        raised = True
    assert raised, "_cite must reject a phrase absent from the banked claim line"


def test_outputs_and_arithmetic():
    m = _walk()
    O = m.outputs()
    total = sum(r["bits"] for r in O)
    assert abs(total - (2.0 + math.log2(3) + 1.0)) < 1e-12
    # conservative rules visible in the rows themselves
    amb = " ".join(r["ambient"] for r in O)
    assert "CONTINUUM PIN" in amb and "EXCLUDED" in amb
    v = m.verdict()
    assert v["outcome"] == "COMPRESSION"
    assert v["retroactive_bits_in"] == 0.0
    assert abs(v["conservative_bits_out"] - 4.584962500721156) < 1e-12
    assert v["declared_input_bits"] == 3.0


def test_findings_carry_the_verdict():
    t = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    flat = " ".join(t.replace("**", "").replace("−", "-").split())
    assert "COMPRESSION" in flat
    assert "0.000 bits" in flat and "4.585" in flat
    assert "named risks both RESOLVE" in flat or "named risks" in flat
    assert "The stop rule does not fire" in flat
    # the both-ways comparison (the strongest honest sentence) is present
    assert "1.585 bits > 0" in flat
    # the pending trit stays pending (not silently adopted)
    assert "recorded pending, not adopted" in flat or "PENDING, not adopted" in flat


def test_verdict_json():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1028" and v["verdict"] == "PROVED"
    assert "COMPRESSION" in v["claim_one_line"]
    assert "THE STOP RULE DOES NOT FIRE" in v["claim_one_line"]
    for dep in ("B994", "B897", "B862", "B864", "B991", "B997", "B1019"):
        assert dep in v["depends_on"]


def test_prereg_seal_intact():
    hashes = (ARC / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8")
    m = re.search(r"^([0-9a-f]{64})\s+frontier/B1028_freedom_ledger/PREREGISTRATION\.md",
                  hashes, re.M)
    assert m and m.group(1).startswith("e13d09a5")
    import hashlib
    actual = hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest()
    assert actual == m.group(1), "sealed prereg must remain byte-identical"
