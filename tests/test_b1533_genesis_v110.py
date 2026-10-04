"""B1533 lock -- GENESIS v1.10 (2026-10-03; not sealed: every item checks a claim the record already fixes).
Main's v1.9 (B1466) is the head; the SM seat's v1.8 lines (sm:B1528), which main's v1.9 does not carry, are re-applied as they
were; GAP6 is scoped by the row it cites (main's B1420 A4), with own code on M4 (C4); main's L244 (a) is answered on the chain
by sm:B1531's reading; Part H verified on main (B1465) is recorded at FK9. Locked here:
- the received texts by sha-256;
- GENESIS.md as the arc's generator's output, byte for byte, and v1.9 recovered by undoing the changes;
- the record (genesis_v110_checks.json and both logs): C1-C7 before writing, C1-C8 after;
- live: C4 (both routes on M4, a second each), C2, C5 and C6; C1, C3 and C7 when main's commits are in the clone;
- GENESIS v1.10's text: version, marks, the added sentences, the statuses;
- Gate 5-Q's three words (encoded here), vendor words and the private term: absent from GENESIS.md and the arc's text;
- the ledgers, the relay, README, OPEN_LEADS and B1528's repointed lock.

Since sm:B1537 (2026-10-04) GENESIS.md is main's v1.10, as main asked. The seat's v1.10 is kept byte-identical in B1537's arc
(`received/GENESIS_v1_10_sm.md`), and the tests below that read v1.10 read it there; B1537's lock checks GENESIS.md."""
import base64
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1533_genesis_v110"
VER = ARC / "verification"
REC = ARC / "received"
V19M, V18M, V18S = REC / "GENESIS_v1_9_main.md", REC / "GENESIS_v1_8_main.md", REC / "GENESIS_v1_8_sm.md"
RELAY_IN = REC / "CC_TO_SM_AND_CODEX_2026-10-03_THE_COUNT_IS_A_BIT_AND_THE_MIXING_QUARTIC.md"
RELAY_OUT = ROOT / "SM_TO_CC_AND_CODEX_2026-10-03_GENESIS_V1_10.md"
MARK, MARK8 = "**[v1.10]**", "**[v1.8]**"
V110_KEPT = ROOT / "frontier" / "B1537_genesis_proposals" / "received" / "GENESIS_v1_10_sm.md"
Q5 = [base64.b64decode(t).decode() for t in ("cXVhbGlh", "YXdhcmU=", "c2Vlcw==")]
VENDOR = [base64.b64decode(t).decode() for t in ("Y2xhdWRl", "YW50aHJvcGlj", "b3B1cw==", "c29ubmV0", "ZmFibGU=")]
PRIVATE = bytes([98, 114, 97, 118, 101]).decode()


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def _norm(text):
    return " ".join(text.split())


def _chk():
    return _load("b1533_genesis_v110_checks", VER / "genesis_v110_checks.py")


def _in_clone(ref):
    return subprocess.run(["git", "cat-file", "-e", ref], cwd=ROOT, capture_output=True).returncode == 0


# ------------------------------------------------------------------------------------------------- the received texts
def test_the_received_texts():
    assert _sha(V19M) == "7eb2df0fee9e32c638b6c872bb4ec07a1f8b93d96c3038153d75508752b5eca2"
    assert _sha(V18M) == "2d652d30c1cb68332d4d8c4c8cd87eba7e3206cb1e4d0e6b815472f7ae02e152"
    assert _sha(V18S) == "b433054459fe86434c24dffd3745e4d41806e5cadaf910bb83e1c4d207e32423"
    assert _sha(RELAY_IN) == "449d822d60732382b716a5691908dded99050e9173c67a0aa2fb29d70fcb4d6f"
    assert "Please take v1.9 as head." in RELAY_IN.read_text(encoding="utf-8")


def test_genesis_is_the_generator_output():
    gen = _load("b1533_merge_genesis_v110", VER / "merge_genesis_v110.py")
    g = V110_KEPT.read_text(encoding="utf-8")
    assert gen.build() == g
    assert len(gen.CHANGES) == 11 and len(gen.V18_CONTENT) == 3
    back = g
    for old, new in reversed(gen.CHANGES):
        assert back.count(new) == 1
        back = back.replace(new, old)
    assert back == V19M.read_text(encoding="utf-8")


# ------------------------------------------------------------------------------------------------- the record
def test_the_record():
    d = json.loads((VER / "genesis_v110_checks.json").read_text(encoding="utf-8"))
    c1 = d["C1"]
    assert c1["main's amend.py on main's v1.8 gives main's v1.9"] is True and c1["main's B1466 changes"] == 5
    assert c1["main's v1.8 against v1.7"] == {"version line": 1, "log lines added at the end": 5, "other changes": 0}
    assert all(v is True for v in c1["received copy == the blob"].values())
    assert d["C2"]["sm:B1528's changes on main's v1.7 == the seat's v1.8, byte for byte"] is True
    assert d["C2"]["anchors found once in main's v1.9"] == [1, 1, 1] and all(d["C2"]["their sentences absent from main's v1.9"])
    assert d["C3"]["verdict rows on main naming Chern-Weil"] == ["B1420"]
    assert d["C3"]["B1420 A4"] == {"closed spin 4-manifold, rank-blind": True, "the second edge stated": True}
    c4 = d["C4"]
    for route in ("route T", "route L"):
        rows = c4[route]
        assert [rows[k]["I"] for k in ("W1", "W1*", "V (+) L")] == [1, -1, 0]
        assert all(rows[k]["rank"] == 5 and rows[k]["h1"] == 2 and rows[k]["relators hold"] for k in rows)
    assert c4["primes"] == {"T": 16640761, "L": 4060801}
    assert [b["I(W1)"] for b in c4["sm:B1515's banked rows (route T)"]] == [1, 1]
    assert d["C5"]["sm:B1531: none of the three kinds, carrying curvature"] == ["B1397", "B1503"]
    assert d["C6"]["tally"] == {"S": 8, "F": 3, "U": 3, "none": 12} and d["C6"]["frame arithmetic among the twelve"] == 9
    assert d["C7"]["rows"] == 7364 and d["C7"]["non-zero"] == 0
    assert d["C7"]["B1466 at q0 = 17 + 12 sqrt2: I(W), I(W'), I(A (+) 1)"] == [-1, 1, 0]
    c8 = d["C8"]
    assert c8["GENESIS.md == merge_genesis_v110.build()"] is True and (c8["[v1.10] marks"], c8["[v1.8] marks"]) == (4, 4)
    assert c8["sha-256"] == _sha(V110_KEPT)
    pre = (VER / "genesis_v110_checks_prewrite_run.txt").read_text(encoding="utf-8")
    post = (VER / "genesis_v110_checks_run.txt").read_text(encoding="utf-8")
    assert "before GENESIS.md is written" in pre and "ALL PASS" in pre and "C8 PASS: GENESIS.md not yet written" in pre
    assert "after GENESIS.md was written" in post and "ALL PASS" in post
    assert "C8 PASS: GENESIS.md is the generator's output byte for byte (4 [v1.10] and 4 [v1.8] marks)" in post


# ------------------------------------------------------------------------------------------------- live
def test_c4_live():
    chk = _chk()
    chk.c4()
    for route in ("route T", "route L"):
        assert [chk.OUT["C4"][route][k]["I"] for k in ("W1", "W1*", "V (+) L")] == [1, -1, 0]


def test_c2_c5_c6_live():
    chk = _chk()
    chk.c2()
    chk.c5()
    chk.c6()
    assert chk.OUT["C6"]["tally"] == {"S": 8, "F": 3, "U": 3, "none": 12}


def test_c1_c3_c7_live():
    if not _in_clone("3f8dc11a:frontier/B1466_the_two_orders_and_the_register_bit/adoption/amend.py"):
        pytest.skip("main's B1466 is not in this clone")
    chk = _chk()
    chk.c1()
    chk.c3()
    chk.c7()
    assert chk.OUT["C1"]["main's amend.py on main's v1.8 gives main's v1.9"] is True
    assert chk.OUT["C7"]["rows"] == 7364


# ------------------------------------------------------------------------------------------------- GENESIS v1.10
def test_genesis_v110_text():
    raw = V110_KEPT.read_text(encoding="utf-8")
    g = _norm(raw)
    v19 = V19M.read_text(encoding="utf-8")
    assert raw.startswith("# GENESIS — the foundations of origin-axiom")
    assert "**Version 1.10 · 2026-10-03 · canonical.**" in raw
    assert raw.count(MARK) == 4 and raw.count(MARK8) == 4
    for m in ("[v1.1]", "[v1.2]", "[v1.3]", "[v1.4]", "[v1.5]", "[v1.6]", "[v1.7]"):
        assert raw.count("**" + m + "**") == v19.count("**" + m + "**"), m
    assert raw.count("**[v1.9]**") == v19.count("**[v1.9]**") + 1          # the intro names v1.9's mark once
    for s in ("v1.10 (sm:B1533) takes main's head, v1.9, as main asked, carries the SM seat's v1.8 lines as they were",
              "**Six gaps**, none of which work on one state can close:",
              "The Chern–Weil row is B1420's A4: on a closed spin 4-manifold a flat bundle's Dirac index is rk(V)·(−σ/8), rank-blind",
              "the non-zero values on non-split modules are flat data too, counts of twisted classes and not Dirac indices",
              "the non-split W₁, its dual and the split V ⊕ L are flat of rank five, so of one Chern character, each with h¹ = 2",
              "count +1, −1 and 0 (two routes, sm:B1533 C4)",
              "A flat frame's count can tell a module from its dual; whether such a count is a physical chirality is GAP1.",
              "Curvature alone is not what the record found missing; a frame with curvature whose arithmetic allows three is",
              "8 are symmetry, 3 flatness, 3 non-uniqueness and 12 none of the three",
              "a fourth kind (lead L244 (a))",
              "Part H, the hyperbolic point itself, verified on main by a route sharing nothing with the seat's (B1465)",
              "7 364 indices, all zero.",
              "main's B1465 states it in the same form, ι̃*V ≅ V* ⊗ ε ⊗ λ²",
              "that sign is the SL(2) factors' own, for modules with no meridian twist, as in B1459",
              "Answered near the hyperbolic point (sm:B1527, PROVED, run as sealed)",
              "- **v1.8 on the SM seat's branch · 2026-10-03 · sm:B1528.**",
              "- **v1.10 · 2026-10-03 · sm:B1533.**",
              "Corrected: §7's heading counts six gaps"):
        assert _norm(s) in g, s
    # main's GAP6 sentence is kept, word for word; the note follows it
    gap6 = "no index built on it can tell 27 from 27̄ (Chern–Weil; the record's Chern–Weil row)"
    assert _norm(gap6) in g and g.index(_norm(gap6)) < g.index("Its scope, from the record")
    fk = {m.group(1): m.group(2) for m in re.finditer(r"(?m)^\| (FK\d+)(?: \*\*\[v1\.2\]\*\*)? \| [^|]+ \| ([^|]+) \|", raw)}
    assert fk["FK1"].strip() == "**[v1.5] CONFIRMED** (the owner, 2026-10-03)" and fk["FK12"].strip() == "OPEN"
    assert fk["FK11"].strip() == "UNEARNED"


def test_hygiene():
    files = [V110_KEPT, RELAY_OUT, ARC / "FINDINGS.md", ARC / "arc_verdict.json"] + sorted(VER.glob("*.py")) + \
        sorted(VER.glob("*.txt")) + sorted(VER.glob("*.json"))
    for p in files:
        t = p.read_text(encoding="utf-8", errors="ignore")
        for w in Q5:
            assert not re.search(r"\b" + w + r"\b", t, re.I), (p.name, w[:2])
        for w in VENDOR:
            assert not re.search(r"\b" + w + r"\b", t, re.I), (p.name, w[:2])
        assert not re.search(r"\b" + PRIVATE + r"\b", t, re.I), p.name


# ------------------------------------------------------------------------------------------------- ledgers and surfaces
def test_verdict_findings_and_ledgers():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1533" and v["verdict"] == "PROVED" and v["creates_law"] is False and v["identifications"] == []
    assert v["prior_work"]["standing"] == "RE-DERIVED" and "|" not in v["claim_one_line"] and "0 of 19" in v["claim_one_line"]
    sys.path.insert(0, str(ROOT / "scripts" / "checks"))
    import prior_work
    assert prior_work.validate(v["prior_work"]) == []
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert f.startswith("# B1533 — GENESIS v1.10: MAIN'S v1.9 AS THE HEAD")
    sec = re.search(r"(?ms)^##[^\n]*Seen first[^\n]*\n(.*?)(?=^## |\Z)", f)
    assert sec and "sweep" in sec.group(1).lower() and "literature" in sec.group(1).lower()
    rl = (ROOT / "docs" / "RELAY_LEDGER.md").read_text(encoding="utf-8")
    assert "| `CC_TO_SM_AND_CODEX_2026-10-03_THE_COUNT_IS_A_BIT_AND_THE_MIXING_QUARTIC.md` | BANKED | 2026-10-03 |" in rl
    assert "| `CC_TO_SM_AND_CODEX_2026-10-03_B1527_PART_H_VERIFIED_THE_MERIDIAN_TWIST.md` | BANKED | 2026-10-03 |" in rl
    assert "| `SM_TO_CC_AND_CODEX_2026-10-03_GENESIS_V1_10.md` | OPEN | 2026-10-03 |" in rl
    assert "| `SM_TO_CC_AND_CODEX_2026-10-03_GENESIS_V1_8.md` | OPEN | 2026-10-03 |" in rl
    relay = _norm(RELAY_OUT.read_text(encoding="utf-8"))
    for s in ("Your B1466 amend.py, run on your v1.8, gives your v1.9 byte for byte",
              "Their class indices are **+1, −1 and 0**", "Take v1.10 as head", "Row sm:B1531 against L244 (a) and (c)."):
        assert _norm(s).lower() in relay.lower(), s
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "v1.10 B1533" in readme          # since sm:B1537 the foundations line names main's v1.10 as the head
    leads = _norm((ROOT / "docs" / "OPEN_LEADS.md").read_text(encoding="utf-8"))
    assert "[2026-10-03, sm:B1533] GENESIS v1.10." in leads
    lock = (ROOT / "tests" / "test_b1528_genesis_v18.py").read_text(encoding="utf-8")
    assert 'V18_KEPT = ROOT / "frontier" / "B1533_genesis_v110" / "received" / "GENESIS_v1_8_sm.md"' in lock
