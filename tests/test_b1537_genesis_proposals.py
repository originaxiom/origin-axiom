"""B1537 lock -- GENESIS: main's v1.10 taken as head, and the SM seat's page changes offered as proposals P1-P9 to it
(2026-10-04; not sealed: every check compares texts or reads a banked record). Main's relay of 2026-10-03 (B1467) asked the seat
to take v1.10 as head and to number its next page changes as proposals to main's current version, not as versions. Locked here:
- the received texts by sha-256, and main's v1.10 against main's commit d295fc5d when it is in the clone;
- GENESIS.md as main's v1.10 at this arc's bank (a later arc that takes a newer head repoints this test, as this arc repointed
  B1533's lock);
- the proposed text: merge_proposals.py rebuilds it byte for byte, the nine marks, and undoing them gives main's v1.10;
- the record (genesis_proposals_checks.json and both run logs) and C3-C5 live;
- the proposals' texts as main will read them;
- Gate 5-Q's three words (encoded here), vendor words and the private term: absent from the arc's own text and the relay;
- the verdict, FINDINGS, the ledgers, the relay, README, OPEN_LEADS and the two repointed locks (B1533, B1516)."""
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
ARC = ROOT / "frontier" / "B1537_genesis_proposals"
VER = ARC / "verification"
REC = ARC / "received"
MAIN_V110, SEAT_V110 = REC / "GENESIS_v1_10_main.md", REC / "GENESIS_v1_10_sm.md"
RELAY_IN = REC / "CC_TO_SM_AND_CODEX_2026-10-03_YOUR_EVENING_ROWED_GENESIS_V1_10.md"
PROPOSED = ARC / "proposed" / "GENESIS_v1_10_with_proposals.md"
RELAY_OUT = ROOT / "SM_TO_CC_AND_CODEX_2026-10-04_GENESIS_PROPOSALS.md"
SHA_MAIN = "b3ac6129e6e63ed409c38a7f6fa603767da2194916ffb89463bb15ed3a45b6a8"
SHA_SEAT = "081ad626ad040a0fd0015f0da0e2cf6b0bc5d468d28bc532e5b76b61c857fee2"
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


def _mp():
    return _load("b1537_merge_proposals", VER / "merge_proposals.py")


def _chk():
    return _load("b1537_genesis_proposals_checks", VER / "genesis_proposals_checks.py")


# ------------------------------------------------------------------------------------------------- the received texts
def test_the_received_texts():
    assert _sha(MAIN_V110) == SHA_MAIN and _sha(SEAT_V110) == SHA_SEAT
    relay = _norm(RELAY_IN.read_text(encoding="utf-8"))
    assert "take v1.10 as head" in relay.lower() and "proposals" in relay
    if subprocess.run(["git", "cat-file", "-e", "d295fc5d:GENESIS.md"], cwd=ROOT, capture_output=True).returncode != 0:
        pytest.skip("main's d295fc5d is not in this clone")
    blob = subprocess.run(["git", "show", "d295fc5d:GENESIS.md"], cwd=ROOT, capture_output=True, check=True).stdout
    assert blob == MAIN_V110.read_bytes()


def test_genesis_is_mains_v110():
    assert (ROOT / "GENESIS.md").read_bytes() == MAIN_V110.read_bytes()


def test_the_seat_v110_is_sm_b1533s():
    gen = _load("b1537_b1533_merge", ROOT / "frontier" / "B1533_genesis_v110" / "verification" / "merge_genesis_v110.py")
    assert gen.build() == SEAT_V110.read_text(encoding="utf-8")


# ------------------------------------------------------------------------------------------------- the proposed text
def test_the_proposed_text():
    mp = _mp()
    prop = mp.build()
    assert PROPOSED.read_text(encoding="utf-8") == prop
    assert len(mp.changes()) == 9
    marks = {i: prop.count(f"**[sm P{i}]**") for i in range(1, 10)}
    assert marks == {**{i: 1 for i in range(1, 10)}, 3: 2}
    back = prop
    for old, new in reversed(mp.changes()):
        assert back.count(new) == 1
        back = back.replace(new, old, 1)
    assert back == MAIN_V110.read_text(encoding="utf-8")


def test_the_proposals_as_main_reads_them():
    g = _norm(PROPOSED.read_text(encoding="utf-8"))
    for s in ("**Six gaps** **[sm P1]**, none of which work on one state can close:",
              "**[sm P5]** On every finite abelian cover of M₂–M₆ no λ = 1 pulled-back member carries a generation-shaped count",
              "(sm:B1532, NEGATIVE, run as sealed; two routes, 68,596 counts each); the members at κ⁵ = 1 add none",
              "**[sm P6]** the finite abelian covers of the levels, which are in the class (sm:B1532: no generation-shaped count)",
              "every connected cover of degree ≤ 12 of m004 and m003 and their Q₈ towers are sealed as sm:B1536",
              "one generation in one W on the silver squares m135 and m136, through interior classes of the four, and none on the "
              "golden word states (sm:B1530)",
              "at most one at every finite-order member and every class of every word state and level (sm:B1535, Theorem C with "
              "Lemma W)",
              "**[sm P8]** At a finite-order member on any finite cover, at every class and in either order: N(5̄′) ≤ n(ν³ ⊗ ρ) and "
              "N(10′) ≤ b0 + n(ν⁴), so g generations need both supplies ≥ g (sm:B1535, Theorem C)",
              "**[sm P9]** F-HE where both of Theorem C's supplies can grow (sm:B1535, Corollary C3)"):
        assert _norm(s) in g, s
    # no proposal changes a status: FK1 and FK12 read as main's v1.10 has them
    mn = MAIN_V110.read_text(encoding="utf-8")
    fk = r"(?m)^\| (FK(?:1|12))(?: \*\*\[v1\.2\]\*\*)? \| [^|]+ \| ([^|]+) \|"
    assert dict(re.findall(fk, PROPOSED.read_text(encoding="utf-8"))) == dict(re.findall(fk, mn))


# ------------------------------------------------------------------------------------------------- the record and live checks
def test_the_record():
    d = json.loads((VER / "genesis_proposals_checks.json").read_text(encoding="utf-8"))
    assert d["all pass"] is True and all(d["passed"].values()) and sorted(d["passed"]) == [f"C{i}" for i in range(1, 8)]
    assert d["C1"]["sha-256"] == SHA_MAIN and d["C2"]["sha-256"] == SHA_SEAT
    assert d["C4"]["proposals"] == 9 and d["C4"]["undoing the proposals gives main's v1.10"] is True
    assert d["C6"]["GENESIS.md == main's v1.10"] is True and d["C6"]["sha-256"] == SHA_MAIN
    assert d["C7"]["hits"] == [] and d["C7"]["files checked"] >= 8
    pre = (VER / "genesis_proposals_checks_prewrite_run.txt").read_text(encoding="utf-8")
    post = (VER / "genesis_proposals_checks_run.txt").read_text(encoding="utf-8")
    assert "C6 (before writing): GENESIS.md is still the seat's v1.10" in pre and "before GENESIS.md is written: ALL PASS" in pre
    assert "after GENESIS.md was written: ALL PASS" in post


def test_c3_c4_c5_c7_live():
    chk = _chk()
    assert all(chk.c3().values())
    c4 = chk.c4()
    assert all(v for k, v in c4.items() if k not in ("proposals", "marks"))
    assert all(chk.c5().values())
    assert chk.c7()["hits"] == []


# ------------------------------------------------------------------------------------------------- hygiene
def test_hygiene():
    files = [PROPOSED, RELAY_OUT, ARC / "FINDINGS.md", ARC / "arc_verdict.json"] + sorted(VER.glob("*.py")) + \
        sorted(VER.glob("*.txt")) + sorted(VER.glob("*.json"))
    for p in files:
        t = p.read_text(encoding="utf-8", errors="ignore")
        for w in Q5 + VENDOR + [PRIVATE]:
            assert not re.search(r"\b" + w + r"\b", t, re.I), (p.name, w[:2])


# ------------------------------------------------------------------------------------------------- ledgers and surfaces
def test_verdict_findings_and_ledgers():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1537" and v["verdict"] == "PROVED" and v["creates_law"] is False and v["identifications"] == []
    assert v["instrument"] is False and v["scope"]["reach"] == "general"
    assert v["prior_work"]["standing"] == "RE-DERIVED" and "|" not in v["claim_one_line"] and "0 of 19" in v["claim_one_line"]
    sys.path.insert(0, str(ROOT / "scripts" / "checks"))
    import prior_work
    assert prior_work.validate(v["prior_work"]) == []
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert f.startswith("# B1537 — GENESIS: MAIN'S v1.10 TAKEN AS HEAD")
    sec = re.search(r"(?ms)^##[^\n]*Seen first[^\n]*\n(.*?)(?=^## |\Z)", f)
    assert sec and "sweep" in sec.group(1).lower() and "literature" in sec.group(1).lower()
    rl = (ROOT / "docs" / "RELAY_LEDGER.md").read_text(encoding="utf-8")
    assert "| `CC_TO_SM_AND_CODEX_2026-10-03_YOUR_EVENING_ROWED_GENESIS_V1_10.md` | BANKED | 2026-10-03 |" in rl
    assert "| `SM_TO_CC_AND_CODEX_2026-10-04_GENESIS_PROPOSALS.md` | OPEN | 2026-10-04 |" in rl
    relay = _norm(RELAY_OUT.read_text(encoding="utf-8"))
    for s in ("GENESIS.md on this branch is main's v1.10, byte for byte", "This seat numbers no further GENESIS versions",
              "proposed/GENESIS_v1_10_with_proposals.md", "removing them gives your v1.10 back"):
        assert _norm(s).lower() in relay.lower(), s
    assert "main's v1.10 as head B1537" in (ROOT / "README.md").read_text(encoding="utf-8")
    assert "[2026-10-04, sm:B1537]" in (ROOT / "docs" / "OPEN_LEADS.md").read_text(encoding="utf-8")
    lock1533 = (ROOT / "tests" / "test_b1533_genesis_v110.py").read_text(encoding="utf-8")
    assert 'V110_KEPT = ROOT / "frontier" / "B1537_genesis_proposals" / "received" / "GENESIS_v1_10_sm.md"' in lock1533
    lock1516 = (ROOT / "tests" / "test_b1516_genesis_v1.py").read_text(encoding="utf-8")
    assert 'rel.parent.name == "proposed" and re.fullmatch(r"GENESIS_v\\d+_\\d+_with_proposals\\.md", rel.name)' in lock1516
