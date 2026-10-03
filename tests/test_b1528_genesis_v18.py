"""B1528 lock -- GENESIS v1.8 (2026-10-03; not sealed: every item checks a claim the record already fixes).
Main's v1.7 (B1462) is the head; its corrected FK12 (ii) sentence is made exact (a meridian twist enters squared; P fixes
Ballas' family); sL-10 item 8 is recorded as answered (sm:B1527). Locked here:
- the received texts by sha-256;
- GENESIS.md as the arc's generator's output, byte for byte;
- the record (genesis_v18_checks.json and both logs): C1-C5 before writing, C1-C6 after;
- live: C4 (exact); C1 when origin/main's B1462 is in the clone; C2 and C3 in a slow test (60-digit characters);
- GENESIS v1.8's text: version, marks, the added sentences, the statuses;
- Gate 5-Q's three words (encoded here), vendor words and the private term: absent from GENESIS.md and the arc's text;
- the ledgers, the relay, README, and B1526's repointed lock."""
import base64
import hashlib
import importlib.util
import json
import re
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1528_genesis_v18"
VER = ARC / "verification"
REC = ARC / "received"
V17M, V16S = REC / "GENESIS_v1_7_main.md", REC / "GENESIS_v1_6_sm.md"
RELAY_IN = REC / "CC_TO_SM_AND_CODEX_2026-10-03_YOUR_SIX_ARCS_HARVESTED_GENESIS_V1_7.md"
RELAY_OUT = ROOT / "SM_TO_CC_AND_CODEX_2026-10-03_GENESIS_V1_8.md"
MARK = "**[v1.8]**"
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


# ------------------------------------------------------------------------------------------------- the received texts
def test_the_received_texts():
    assert _sha(V17M) == "8b8ec814df3ae205a08fe5a7d263aacceb114982335e86518fb7cc19a9948e16"
    assert _sha(V16S) == "59ef40a678a2aa7b11d37599300b6d3cacc481edb0568f30eda852ba176faf36"
    assert _sha(RELAY_IN) == "b8ba95a58b3ae7d95d26034b56bbe5b5c0db8437f5792b22cbfba11319b5ddc3"
    assert "Please take v1.7 as head" in RELAY_IN.read_text(encoding="utf-8")


def test_genesis_is_the_generator_output():
    gen = _load("b1528_merge_genesis_v18", VER / "merge_genesis_v18.py")
    assert gen.build() == (ROOT / "GENESIS.md").read_text(encoding="utf-8")
    assert len(gen.CHANGES) == 6


# ------------------------------------------------------------------------------------------------- the record
def test_the_record():
    d = json.loads((VER / "genesis_v18_checks.json").read_text(encoding="utf-8"))
    assert d["C1"]["v1.6 + main's changes == main's v1.7, byte for byte"] is True and d["C1"]["changes"] == 4
    c2 = d["C2"]
    assert c2["P"] == "a -> A, b -> B, t -> babt" and c2["extension words found (length <= 6)"] == ["bab"]
    assert c2["P fixes rho_hyp"] is True
    rows = {r["lambda"]: r for r in c2["rows"]}
    assert all(r["P*V ~ V* (x) (t -> lambda^2)"] for r in rows.values()) and len(rows) == 6
    assert [k for k, r in rows.items() if r["P*V ~ V*"]] == ["1", "-1"]
    assert [k for k, r in rows.items() if r["P*V ~ V* (x) (t -> -1)"]] == ["i"]
    q2, q1 = d["C3"]["rows"]
    assert q2["P fixes rho_q"] and not q2["rho_q self-dual"] and not q2["P carries rho_q to its dual"]
    assert q1["P fixes rho_q"] and q1["rho_q self-dual"]
    assert all(r["square is T"] and r["fourth power is the identity"] for r in d["C4"]["rows"])
    assert d["C5"]["verdict"] == "PROVED" and d["C6"]["[v1.8] marks"] == 4
    assert d["C6"]["GENESIS.md == merge_genesis_v18.build()"] is True
    pre = (VER / "genesis_v18_checks_prewrite_run.txt").read_text(encoding="utf-8")
    post = (VER / "genesis_v18_checks_run.txt").read_text(encoding="utf-8")
    assert "before GENESIS.md is written" in pre and "ALL PASS" in pre and "C6 PASS" not in pre
    assert "after GENESIS.md was written" in post and "ALL PASS" in post
    assert "C6 PASS: GENESIS.md is the generator's output byte for byte (4 [v1.8] marks)" in post


# ------------------------------------------------------------------------------------------------- live
def _chk():
    return _load("b1528_genesis_v18_checks", VER / "genesis_v18_checks.py")


def test_c4_live():
    chk = _chk()
    chk.c4()
    assert all(r["square is T"] for r in chk.OUT["C4"]["rows"])


def test_c1_live():
    r = subprocess.run(["git", "cat-file", "-e", "origin/main:frontier/B1462_the_seats_harvested_p_is_the_swap_and_the_levels/"
                        "adoption/amend.py"], cwd=ROOT, capture_output=True)
    if r.returncode != 0:
        pytest.skip("main's B1462 is not in this clone")
    chk = _chk()
    chk.c1()
    assert chk.OUT["C1"]["v1.6 + main's changes == main's v1.7, byte for byte"] is True


@pytest.mark.slow
def test_c2_c3_live():
    chk = _chk()
    P = chk.c2()
    chk.c3(P)
    assert chk.OUT["C2"]["P"] == "a -> A, b -> B, t -> babt"
    assert not chk.OUT["C3"]["rows"][0]["rho_q self-dual"]


# ------------------------------------------------------------------------------------------------- GENESIS v1.8
def test_genesis_v18_text():
    raw = (ROOT / "GENESIS.md").read_text(encoding="utf-8")
    g = _norm(raw)
    assert raw.startswith("# GENESIS — the foundations of origin-axiom")
    assert "**Version 1.8 · 2026-10-03 · canonical.**" in raw and raw.count(MARK) == 4
    for s in ("that sign is the SL(2) factors' own, for modules with no meridian twist, as in B1459",
              "P*V ≅ V* ⊗ (t ↦ λ²), so P carries V to its dual up to a sign exactly when λ² = ±1",
              "on Ballas' family P fixes ρ_q, which is not self-dual for q ≠ 1, so P does not carry it to its dual",
              "Answered near the hyperbolic point (sm:B1527, PROVED, run as sealed)",
              "Open: the eigenvalue-one locus of the infinite-volume part (sL-10 item 9).",
              "answered near the hyperbolic point in finite volume (sm:B1527)",
              "- **v1.8 · 2026-10-03 · sm:B1528.**"):
        assert _norm(s) in g, s
    v17 = V17M.read_text(encoding="utf-8")
    gen = _load("b1528_merge_genesis_v18_t", VER / "merge_genesis_v18.py")
    back = raw
    for o, n in gen.CHANGES:                           # undoing the six changes gives main's v1.7 exactly
        assert back.count(n) == 1
        back = back.replace(n, o)
    assert back == v17
    for o, n in gen.CHANGES[1:]:                       # and inside each change main's words survive, in order
        wo, wn = re.findall(r"\w+", o), iter(re.findall(r"\w+", n))
        assert all(any(w == x for x in wn) for w in wo), o[:60]
    fk = {m.group(1): m.group(2) for m in re.finditer(r"(?m)^\| (FK\d+)(?: \*\*\[v1\.2\]\*\*)? \| [^|]+ \| ([^|]+) \|", raw)}
    assert fk["FK1"].strip() == "**[v1.5] CONFIRMED** (the owner, 2026-10-03)" and fk["FK12"].strip() == "OPEN"


def test_hygiene():
    files = [ROOT / "GENESIS.md", RELAY_OUT, ARC / "FINDINGS.md"] + sorted(VER.glob("*.py")) + sorted(VER.glob("*.txt"))
    for p in files:
        t = p.read_text(encoding="utf-8", errors="ignore")
        for w in Q5:
            assert not re.search(r"\b" + w + r"\b", t, re.I), (p.name, w[:2])
        for w in VENDOR:
            assert not re.search(r"\b" + w + r"\b", t, re.I), (p.name, w[:2])
        assert not re.search(r"\b" + PRIVATE + r"\b", t, re.I), p.name


# ------------------------------------------------------------------------------------------------- ledgers and surfaces
def test_verdict_and_ledgers():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1528" and v["verdict"] == "PROVED" and v["creates_law"] is False
    assert v["prior_work"]["standing"] == "RE-DERIVED"
    rl = (ROOT / "docs" / "RELAY_LEDGER.md").read_text(encoding="utf-8")
    assert "| `CC_TO_SM_AND_CODEX_2026-10-03_YOUR_SIX_ARCS_HARVESTED_GENESIS_V1_7.md` | BANKED | 2026-10-03 |" in rl
    assert "| `SM_TO_CC_AND_CODEX_2026-10-03_GENESIS_V1_8.md` | OPEN | 2026-10-03 |" in rl
    relay = _norm(RELAY_OUT.read_text(encoding="utf-8"))
    for s in ("Your amend.py, run on this branch's v1.6, gives your v1.7 byte for byte",
              "P*V ≅ V* ⊗ (t ↦ λ²) for V = ρ_hyp twisted by t ↦ λ", "Take v1.8 as head"):
        assert _norm(s) in relay, s
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "[`GENESIS.md`](GENESIS.md) v1.8 is canonical on this branch: main's v1.7 (its B1462)" in readme
    leads = _norm((ROOT / "docs" / "OPEN_LEADS.md").read_text(encoding="utf-8"))
    assert "[2026-10-03, sm:B1528] GENESIS v1.8." in leads
    lock = (ROOT / "tests" / "test_b1526_genesis_v16.py").read_text(encoding="utf-8")
    assert 'V16_KEPT = ROOT / "frontier" / "B1528_genesis_v18" / "received" / "GENESIS_v1_6_sm.md"' in lock
