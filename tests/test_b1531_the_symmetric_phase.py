"""B1531 lock -- THE SYMMETRIC PHASE: chat 1's reframing (philosophy/P023) checked against the record (2026-10-03; not sealed:
every check reads a banked record, re-derives a fact a record states, or applies a theorem read at source).
Locked here:
- the record (symmetric_phase_checks.json): C1-C6 and C2b hold, with their numbers;
- live: C2b's reading against the kill graph; C3 exactly (zeta, Euler product, mirror counts, beta_c); C6's conjugation;
  the whole-word count of C1 on this branch (the substring count is the error caught before banking);
- the FINDINGS table carries C2b's reading record by record;
- P023 holds chat 1's text verbatim (its hash), and the experiential words stay in philosophy/;
- hygiene and the verdict.
C4 (route E on m135, about 7 s) and C6's SnapPy half are re-run in the slow test only."""
import base64
import hashlib
import importlib.util
import json
import re
import subprocess
from fractions import Fraction
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1531_the_symmetric_phase"
VER = ARC / "verification"
P023 = ROOT / "philosophy" / "P023_the_symmetric_phase.md"
# sha256 of chat 1's text as relayed (after the owner's one-line preface), the body P023 quotes verbatim
CHAT1_SHA256 = "eb39ecd22777ee6c103dc070f7003c14adbc94fe41062dfe5a0184d84d36934a"


def _checks():
    spec = importlib.util.spec_from_file_location("b1531_symmetric_phase_checks", VER / "symmetric_phase_checks.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _record():
    return json.loads((VER / "symmetric_phase_checks.json").read_text(encoding="utf-8"))


def test_the_record():
    r = _record()
    c1 = r["C1"]["counts"]
    assert r["C1"]["holds (the phrases are present)"] is True
    for ref in ("origin/main", "HEAD", "origin/audit/physical-bridge-2026-09-05", "origin/sep16-branch"):
        assert c1[ref]["symmetric phase"]["where"] == ["docs/OPEN_LEADS.md", "frontier/B849_order_parameter/PREREGISTRATION.md",
                                                     "frontier/B853_two_faces_ssb/relay_verify.py"], ref
    assert c1["origin/main"]["symmetric phase (substring, for comparison)"]["files"] == 4
    assert c1["origin/audit/physical-bridge-2026-09-05"]["symmetric phase (substring, for comparison)"]["files"] == 7
    assert c1["files under papers/ (either phrase, any head read)"] == []
    assert r["C2"]["records"] == 821
    assert r["C2"]["the chain's tally as the 2026-09-30 note states it"] is True
    assert r["C2b"]["tally"] == {"S": 8, "F": 3, "U": 3, "none": 12}
    assert r["C2b"]["covered by the three kinds"] == 14
    assert r["C2b"]["none of the three, carrying curvature"] == ["B1397", "B1503"]
    assert r["C3"]["holds"] is True
    assert r["C3"]["2 log phi"].startswith("0.9624236501192")
    assert r["C3"]["2 log(1 + sqrt 2)"].startswith("1.762747174039")
    assert r["C3"]["+LR"]["orbits of least period 1..6 (c_m)"] == [1, 2, 5, 10, 24, 50]
    assert r["C3"]["-LLRR"]["N_1..N_6"] == [8, 32, 200, 1152, 6728, 39200]
    assert r["C4"]["holds"] is True
    assert r["C4"]["readings (I(W), I(Lambda^2 W))"] == {"the split vacuum V (+) 1": [0, 0], "W1 at the interior class": [-1, -1],
                                                       "W2 (the dual order) at the interior class": [1, 1]}
    assert r["C5"]["holds"] is True and all(all(d.values()) for d in r["C5"]["quotes found"].values())
    assert len(r["C5"]["quotes found"]) == 11
    assert r["C6"]["holds"] is True
    assert all(v["amphicheiral"] for v in r["C6"]["SnapPy"].values())


def test_c1_whole_words_on_this_branch():
    """the whole-word count (git grep -w) on this branch's head, against the substring count it replaced"""
    def files(*flags):
        out = subprocess.run(["git", "grep", "-i", "-l", *flags, "symmetric phase", "HEAD", "--"], cwd=ROOT,
                             capture_output=True, text=True).stdout.split()
        return sorted(x.split(":", 1)[1] for x in out)
    assert files("-w") == ["docs/OPEN_LEADS.md", "frontier/B849_order_parameter/PREREGISTRATION.md",
                           "frontier/B853_two_faces_ssb/relay_verify.py"]


def test_c2b_the_reading_against_the_kill_graph():
    S = _checks()
    r = S.c2b()
    assert r["tally"] == {"S": 8, "F": 3, "U": 3, "none": 12}
    assert r["family x kind"] == {"absence-at-depth -> none": 1, "closed-sum-zero -> F": 3, "closed-sum-zero -> none": 1,
                                  "end-datum-input -> U": 3, "frame-arithmetic -> none": 9, "no-landing-site -> none": 1,
                                  "symmetry-cannot-select -> S": 8}


def test_c3_the_critical_point_exactly():
    S = _checks()
    r = S.c3()
    assert r["holds"] is True
    for key in ("+LR", "-LR", "+LLRR", "-LLRR"):
        v = r[key]
        assert v["zeta = (1 - sign z)^2/(1 - t z + z^2) exactly to order 40"]
        assert v["Euler product over orbits to order 40"] and v["N_n(f^-1) = N_n(f) to n = 40"]
    assert r["+LR"]["beta_c = log lambda"] == r["2 log phi"]
    assert r["+LLRR"]["beta_c = log lambda"] == r["2 log(1 + sqrt 2)"]


def test_c6_the_quarter_turn_conjugates_each_monodromy_to_its_inverse():
    K, Kinv = ((0, 1), (-1, 0)), ((0, -1), (1, 0))

    def mul(X, Y):
        return tuple(tuple(sum(X[i][k] * Y[k][j] for k in range(2)) for j in range(2)) for i in range(2))
    for A in (((2, 1), (1, 1)), ((1, 2), (2, 5))):
        for s in (1, -1):
            B = tuple(tuple(s * x for x in row) for row in A)
            Binv = tuple(tuple(s * x for x in row) for row in ((A[1][1], -A[0][1]), (-A[1][0], A[0][0])))
            assert mul(mul(K, B), Kinv) == Binv
    assert K[0][0] * K[1][1] - K[0][1] * K[1][0] == 1


def test_the_findings_table_carries_the_reading():
    S = _checks()
    words = {"S": "symmetry", "F": "flatness", "U": "non-uniqueness", "none": "none"}
    text = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    for b, (kind, _) in S.READING.items():
        row = [ln for ln in text.splitlines() if ln.startswith(f"| {b} |")]
        assert len(row) == 1, b
        assert f"| {words[kind]}" in row[0], (b, kind)
    assert "## Seen first" in text and "sweep" in text and "literature" in text


def test_p023_holds_the_text_verbatim():
    t = P023.read_text(encoding="utf-8")
    body = t.split("## The text, verbatim\n\n", 1)[1].split("\n\n## Why it is kept", 1)[0].rstrip("\n")
    lines = [ln[2:] if ln.startswith("> ") else ("" if ln == ">" else None) for ln in body.split("\n")]
    assert None not in lines
    unquoted = "\n".join(lines)
    assert hashlib.sha256(unquoted.encode("utf-8")).hexdigest() == CHAT1_SHA256
    assert "Philosophy — motivation only" in t and "B1531" in t


def test_hygiene():
    """no vendor word or the private term in the arc, the lock or P023; the Gate 5-Q words stay out of the arc"""
    vendor = [base64.b64decode(x).decode() for x in ("Y2xhdWRl", "YW50aHJvcGlj", "b3B1cw==", "c29ubmV0", "ZmFibGU=")]
    private = bytes([98, 114, 97, 118, 101]).decode()
    gate5q = [base64.b64decode(x).decode() for x in ("cXVhbGlh", "YXdhcmU=", "c2Vlcw==")]
    arc_files = [p for p in ARC.rglob("*") if p.is_file() and p.suffix in (".md", ".py", ".txt", ".json")]
    for p in arc_files + [P023, Path(__file__)]:
        t = p.read_text(encoding="utf-8", errors="ignore").lower()
        for w in vendor:
            assert w not in t, (p.name, "vendor word")
        assert not re.search(r"\b" + private + r"\b", t), p.name
    for p in arc_files:
        t = p.read_text(encoding="utf-8", errors="ignore").lower()
        for w in gate5q:
            assert not re.search(r"\b" + re.escape(w), t), (p.name, w[:2])


def test_the_verdict():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1531" and v["verdict"] == "PROVED" and v["creates_law"] is False and v["instrument"] is False
    assert v["prior_work"]["standing"] == "EXTENDS"
    assert v["scope"]["reach"] == "class"
    spec = importlib.util.spec_from_file_location("prior_work", ROOT / "scripts" / "checks" / "prior_work.py")
    pw = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(pw)
    assert pw.validate(v["prior_work"]) == []


@pytest.mark.slow
def test_c4_and_c6_live():
    S = _checks()
    assert S.c4()["holds"] is True
    assert S.c6()["holds"] is True
