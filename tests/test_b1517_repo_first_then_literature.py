"""B1517 lock -- SEE THE REPO FIRST, THEN THE LITERATURE (the owner's rule of 2026-10-02) and its first sweep.

The owner: "i ljust lets make sure we dont miss any work and misclaim about it. make a rule to see the repo first and literature".
Locked here:
- the rule in WORKING_RULES and its PRACTICES row; the instrument's validate() controls in both directions; the schema constant;
- B1517's own prior_work record (the first under the rule), well formed, RE-DERIVED, with dated sources;
- the first sweep's mathematics, recomputed live: 758 word states (twice OEIS A000048) realise 536 manifolds (twice OEIS
  A000046); reverse(w) = (PJ) w^-1 (PJ)^-1 with det PJ = -1 on every word to length 12; main's firing list splits no pair and is
  87 of 536 per manifold; the SnapPy partition and orientations (slow);
- GENESIS v1.1's amended statements, B1516's dated note at C9, the README, OPEN_LEADS and the relay.
"""
import importlib.util
import json
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1517_repo_first_then_literature"
OWNER = "i ljust lets make sure we dont miss any work and misclaim about it. make a rule to see the repo first and literature"


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _norm(p):
    return " ".join(p.read_text(encoding="utf-8").split())


PW = _load("prior_work_b1517", ROOT / "scripts" / "checks" / "prior_work.py")
CB = _load("census_by_manifold_b1517", ARC / "verification" / "census_by_manifold.py")


# ------------------------------------------------------------------------------------------------- the rule
def test_rule_in_working_rules_and_practices():
    w = _norm(ROOT / "WORKING_RULES.md")
    assert "## Rule (2026-10-02, the owner's instruction — adopted): SEE THE REPO FIRST, THEN THE LITERATURE" in \
        (ROOT / "WORKING_RULES.md").read_text(encoding="utf-8")
    assert OWNER in w
    for phrase in ("**The repo first.**", "**The literature second.**", "**Record both legs as data.**",
                   "**Claim no more than the sweep saw.**", "**A miss found later**", "scripts/checks/prior_work.py"):
        assert phrase in w, phrase
    pr = _norm(ROOT / "docs" / "PRACTICES.md")
    assert "See the repo first, then the literature: every arc from B1517 records its sweep" in pr
    assert "## See the repo first, then the literature — TESTED (the record) + MANUAL (the reading)" in \
        (ROOT / "docs" / "PRACTICES.md").read_text(encoding="utf-8")


def test_validate_controls_both_directions():
    good = {"repo": {"heads": {"origin/main": "bd48dd28"}, "terms": ["x"], "hits": [{"where": "a", "bearing": "b"}]},
            "literature": {"queries": ["q"], "sources": [{"cite": "c", "where": "w", "read": "2026-10-02", "says": "s"}]},
            "standing": "RE-DERIVED"}
    assert PW.validate(good) == []
    bad_cases = []
    for mutate in (lambda d: d.update(standing="NEW"),
                   lambda d: d["repo"].update(heads={"origin/main": "nope"}),
                   lambda d: d.update(literature={"queries": [], "sources": []}),
                   lambda d: d["literature"]["sources"][0].update(read="today"),
                   lambda d: (d.update(standing="NOT-CHECKED"), d.pop("why", None)),
                   lambda d: (d["literature"].update(sources=[]), d["repo"].update(hits=[]))):
        d = json.loads(json.dumps(good))
        mutate(d)
        bad_cases.append(PW.validate(d))
    assert all(bad_cases), bad_cases
    assert PW.STANDINGS == ("KNOWN", "RE-DERIVED", "EXTENDS", "NEW-AS-SWEPT", "NOT-CHECKED")


def test_schema_requires_prior_work_from_b1517():
    schema = _load("schema_b1517", ROOT / "tests" / "test_arc_verdict_schema.py")
    assert schema.PRIOR_WORK_REQUIRED_FROM == 1517
    assert schema.NOVELTY.search("a novel identity") and not schema.NOVELTY.search(schema._unquoted('the word "novel"'))


def test_b1517_record_is_the_first_under_the_rule():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1517" and d["verdict"] == "PROVED" and d["instrument"] is False and d["creates_law"] is False
    pw = d["prior_work"]
    assert PW.validate(pw) == [] and pw["standing"] == "RE-DERIVED"
    heads = pw["repo"]["heads"]
    assert heads["origin/main"] == "bd48dd28" and heads["origin/audit/physical-bridge-2026-09-05"] == "64a96ea6"
    assert len(heads) >= 5
    cites = " ".join(s["cite"] for s in pw["literature"]["sources"])
    for c in ("OEIS A000048", "OEIS A000046", "Goodman", "Gueritaud", "Chun"):
        assert c in cites, c
    assert all(s["read"] == "2026-10-02" for s in pw["literature"]["sources"])
    wheres = " ".join(h["where"] for h in pw["repo"]["hits"])
    for w in ("B1434", "B1439", "B945", "B134", "B779", "64a96ea6"):
        assert w in wheres, w
    assert d["scope"]["frame"] == "none" and d["scope"]["reach"] == "general"
    assert "|" not in d["claim_one_line"]


# ------------------------------------------------------------------------------------------------- the mathematics, live
def test_live_census_identity_and_rates():
    rec = CB.checks(with_snappy=False)
    assert rec["passed"]
    assert rec["C1 word states"] == 758 and rec["C1 per length (unsigned)"] == [1, 1, 2, 3, 5, 9, 16, 28, 51, 93, 170]
    assert rec["C2 classes under rotation, swap and reversal"] == 536
    assert rec["C2 per length (unsigned)"] == [1, 1, 2, 3, 5, 8, 14, 21, 39, 62, 112]
    assert rec["C2 reversal pairs"] == 222 and rec["C2 first pair"] == ["+LLLRLRR", "+LLLRRLR"]
    assert rec["C6 reverse(w) = (PJ) w^-1 (PJ)^-1 on every word"] and rec["C6 words checked"] == 8190 and rec["C6 det(PJ)"] == -1
    assert rec["C5 pairs split by main's census (one member fires, the other not)"] == []
    assert rec["C5 rate per word state (with main B1434's two at lengths 2-6)"] == [95, 758]
    assert rec["C5 rate per manifold (with main B1434's two at lengths 2-6)"] == [87, 536]
    assert rec["C5 lengths 7-12: reversal-closed firing / states, paired firing / states"] == [77, 290, 16, 444]


def test_identity_can_fail():
    """The C6 comparison is live: the plain inverse and the transpose are not the reverse in general."""
    w = "LLLRLRR"
    rev = CB.word(w[::-1])
    assert rev != CB.inv(CB.word(w)) and rev != CB.mul(CB.mul(CB.P, CB.inv(CB.word(w))), CB.P)
    assert CB.canon_state(w[::-1]) != CB.canon_state(w) and CB.canon_manifold(w[::-1]) == CB.canon_manifold(w)


def test_main_extract_carries_its_source():
    m = json.loads((ARC / "verification" / "main_B1439_firing_own_states.json").read_text(encoding="utf-8"))
    assert "bd48dd28" in m["source"] and "census_summary.json" in m["source"]
    assert len(m["firing_own_states"]) == 93 and m["own_levels_total_lengths_7_to_12"] == 734


def test_run_record():
    r = json.loads((ARC / "verification" / "census_by_manifold_run.json").read_text(encoding="utf-8"))
    assert r["passed"] is True
    assert r["C3 distinct manifolds by isometry signature"] == 536 and r["C3 partition equals C2's"] is True
    assert r["C4 reverse orientation-preservingly isometric (cusp map det +1)"] == 222
    assert r["C4 swap has an orientation-reversing isometry (det -1)"] == 222
    assert r["C4 Chern-Simons equal for the reverse (mod 1/2)"] == 222 and r["C4 Chern-Simons negated for the swap (mod 1/2)"] == 222


@pytest.mark.slow
def test_live_snappy_partition_and_orientation():
    pytest.importorskip("snappy")
    rec = CB.checks(with_snappy=True)
    assert rec["passed"] and rec["C3 distinct manifolds by isometry signature"] == 536


# ------------------------------------------------------------------------------------------------- the amended surfaces
def test_genesis_v11():
    raw = (ROOT / "GENESIS.md").read_text(encoding="utf-8")
    g = " ".join(raw.split())
    assert "**Version 1.1 · 2026-10-02 · arcs B1516 and B1517 · canonical.**" in raw
    for s in ("A word and its reverse are two states realised by one manifold, with the same orientation",
              "**They realise 536 distinct manifolds**, twice OEIS A000046",
              "twice OEIS A000048 summed over those lengths",
              "(Goodman–Heard–Hodgson 2008, Lemma 3.2; Guéritaud 2006, §3.2)",
              "- **Signed powers.** For u primitive and k even, −uᵏ is a legal signed monodromy (GM5b) that is neither a state",
              "The audit lane's R78 (sealed 2026-10-02) raised it",
              "(Chun, Gukov, Park and Sopenko 2019, §2.2 eq. (11))",
              "87 of the 536 manifolds they realise (B1517 C5)",
              "A count over states names its unit, word states or manifolds",
              "- **v1.1 · 2026-10-02 · B1517.**"):
        assert s in g, s
    assert re.search(r"^- \*\*v1\.0 · 2026-10-02 · B1516\.\*\*$", raw, flags=re.M)


def test_dated_notes_and_surfaces():
    f16 = _norm(ROOT / "frontier" / "B1516_genesis_v1" / "FINDINGS.md")
    assert "*Note (2026-10-02, B1517).* The script's comment \"the state of B is (eps, root) at level k\" is wrong" in f16
    readme = _norm(ROOT / "README.md")
    assert "They realise 536 distinct manifolds, because a word and its reverse give the same manifold (B1517)" in readme
    leads = _norm(ROOT / "docs" / "OPEN_LEADS.md")
    assert "*Added 2026-10-02 (B1517).* A rate names its unit." in leads
    relay = ROOT / "SM_TO_CC_AND_CODEX_2026-10-02_THE_STATES_AND_THE_MANIFOLDS.md"
    assert relay.exists() and "536 manifolds" in relay.read_text(encoding="utf-8")
    ledger = (ROOT / "docs" / "RELAY_LEDGER.md").read_text(encoding="utf-8")
    assert "| `SM_TO_CC_AND_CODEX_2026-10-02_THE_STATES_AND_THE_MANIFOLDS.md` | OPEN | 2026-10-02 |" in ledger
    err = (ROOT / "docs" / "ERROR_LEDGER.md").read_text(encoding="utf-8")
    assert "| E59 instance (2026-10-02, B1516 and GENESIS v1.0)" in err and "| E11 instance (2026-10-02, B1516 C9)" in err


def test_findings_and_hygiene():
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert f.startswith("# B1517 — SEE THE REPO FIRST, THEN THE LITERATURE")
    for sec in ("## 0. The request", "## 1. The rule and its instrument", "## 2. The first sweep", "### 2.1 The repo leg",
                "### 2.2 The literature leg", "### 2.3 Standing, claim by claim", "## 3. The finding",
                "## 4. Two more things the sweep found", "## 6. What is not claimed"):
        assert sec in f, sec
    assert "0 of 19" in f
    private = bytes([98, 114, 97, 118, 101]).decode()
    for p in (ARC / "FINDINGS.md", ARC / "arc_verdict.json", ROOT / "WORKING_RULES.md", ROOT / "GENESIS.md",
              ROOT / "SM_TO_CC_AND_CODEX_2026-10-02_THE_STATES_AND_THE_MANIFOLDS.md", ROOT / "scripts" / "checks" / "prior_work.py"):
        assert private not in p.read_text(encoding="utf-8").lower(), p.name
