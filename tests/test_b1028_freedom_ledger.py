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
    # CORRECTED 2026-11-11 (the audit's finding E7): the verdict was PROVED.  The ledger's zero is a sum of eleven prices typed
    # 0.0, and its check is a substring match; the verdict is OPEN, and the claim as first asserted is kept after the correction.
    assert v["id"] == "B1028" and v["verdict"] == "OPEN"
    c = v["claim_one_line"]
    assert c.startswith("CORRECTED 2026-11-11 (the audit's finding E7") and "ORIGINAL CLAIM AS ASSERTED: THE GLOBAL FREEDOM LEDGER" in c
    for s in ("NOT PRICED", "the family declaration", "the door set is {1, 4}", "the principal embedding", "THE ONE ENDPOINT IT CREDITS is the algebra of dimension 14"):
        assert s in c, s
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


def test_the_zero_is_typed_and_the_check_is_a_substring_match():
    """the audit's finding E7, shown on the walk itself: every price is the literal 0.0 in the source, and the citation
    check passes on a claim line that has since been corrected to say the opposite of what the link needs"""
    m = _walk()
    src = (ARC / "b1028_walk.py").read_text(encoding="utf-8")
    assert src.count("price=0.0") == 11 and len(m.links()) == 11            # eleven typed zeros, and nothing else is summed
    assert "assert bits_in == 0.0" in src
    b997 = json.loads((ROOT / "frontier" / "B997_golden_conductor_uniqueness" / "arc_verdict.json").read_text(encoding="utf-8"))["claim_one_line"]
    assert "UNIQUE METALLIC GRAMMAR" in b997 and "the door set is {1, 4}" in b997      # the phrase the walk matches, and its correction, in one line
    assert m._cite("B997_golden_conductor_uniqueness", "UNIQUE METALLIC GRAMMAR", "INFINITE FAMILY") == "B997"     # the check still passes


MARK = "the freedom ledger's zero is not a computed quantity"
CARRIED = ("frontier/B1028_freedom_ledger/FINDINGS.md", "frontier/B1028_freedom_ledger/arc_verdict.json", "ROADMAP.md", "docs/THE_CLAIM.md", "docs/THE_FRAMEWORK.md",
           "docs/THE_FINAL_ATTACK_2026-10-29.md", "docs/THE_CROSSINGS_CENSUS_2026-10-13.md", "frontier/B1643_the_crossings_census/FINDINGS.md",
           "frontier/B1030_price_lock_verification/FINDINGS.md", "frontier/B1030_price_lock_verification/arc_verdict.json", "frontier/B1222_symmetry_vanishing_thesis/FINDINGS.md")
# what was said at the time, or says something else by the same words: the logs, the campaign's status history, the plan of the
# campaign, other ledgers' own prices, and the programme's pages on the audit
HISTORY = ("PROGRESS_LOG.md", "CHANGELOG.md", "docs/CAMPAIGN_STATUS.md", "docs/progress/", "docs/handoffs/", "docs/views/", "docs/THE_WHY_CAMPAIGN.md", "docs/CROSSING_REQUIREMENTS.md",
           "docs/FIELD_EXPLORATION_REPORT.md", "docs/GRAND_COMPUTATION_v0.md", "docs/THE_FINAL_ACTS_BAR_2026-10-29.md", "frontier/B1015_", "frontier/B1128_", "frontier/B1349_",
           "frontier/B1861_", "frontier/B1870_", "frontier/B1028_freedom_ledger/ADDENDUM", "frontier/B1028_freedom_ledger/PREREGISTRATION")


def test_every_page_that_states_the_zero_carries_the_correction():
    for rel in CARRIED:
        assert MARK.lower() in (ROOT / rel).read_text(encoding="utf-8").lower(), rel
    old = re.compile(r"0\.000 bits|0\.000 BITS|zero (?:retroactive )?designer freedom", re.I)
    loose = []
    for top in ("docs", "frontier", "papers"):
        for p in (ROOT / top).rglob("*.md"):
            rel = p.relative_to(ROOT).as_posix()
            if any(rel.startswith(h) or h in rel for h in HISTORY):
                continue
            try:
                text = p.read_text(encoding="utf-8")
            except Exception:
                continue
            if MARK.lower() in text.lower():
                continue
            if any(old.search(line) and re.search(r"designer|freedom ledger|B1028", line) for line in text.splitlines()):
                loose.append(rel)
    for rel in ("ROADMAP.md", "README.md", "GENESIS.md", "CLAIMS.md", "GOVERNANCE.md"):
        text = (ROOT / rel).read_text(encoding="utf-8")
        if MARK.lower() not in text.lower() and any(old.search(line) and re.search(r"designer|freedom ledger|B1028", line) for line in text.splitlines()):
            loose.append(rel)
    assert not loose, loose
