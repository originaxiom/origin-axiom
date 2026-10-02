"""B1522 lock -- THE GOLDEN CHOICE (2026-10-02). Main's L242 (b) and the owner's "choice might be golden", run as sealed at
5d4eb5f7: on the levels M_1 ... M_12 of m004's Ballas family, which vacua nu (x) rho_q are fixed by a count-odd map. Outcome B:
the count-odd mirror breaks from M_5 on, exactly where no golden Galois reflection fixes the twist, and every one of the 196 banked
firing members is fixed. PROVED; creates_law (Lemma C, Lemma F).
Locked here:
- the seal's digest and markers, and every sealed file's hash (ARTIFACT_HASHES.txt);
- the records: the census (both routes, twelve levels, the firing members), the read-out (P1-P9, the golden reading, the
  after-the-run section) and the post-run checks (X1-X4);
- live:
  - both routes on M_1 ... M_7, character by character, with Lemma F's closed counts;
  - the criterion bypassed on M_5 (the direct module test over F_89 against all 80 symmetry words);
  - M_5's case-(b) members are exactly the twists no reflection fixes, ten on each golden sheet, held by rotations only;
  - Lemma F beyond the sealed range, on M_13 (X5);
- the kill-graph note on B1520, the registry row, the verdict, the findings' load-bearing sentences, and hygiene.
The census's full rerun (68 s) and the post-run checks' full rerun (64 s) are marked slow."""
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1522_the_golden_choice"
VER = ARC / "verification"
SEALED_SHA = "2e3e12cea442383e377cc1f0b302d266b4286f7a85e6526581277546f3e8e580"
ORDERS = [1, 5, 16, 45, 121, 320, 841, 2205, 5776, 15125, 39601, 103680]
GENERIC = [0, 0, 0, 0, 20, 96, 448, 1344, 4464, 12100, 35244, 93936]
UNITARY = [0, 0, 0, 0, 0, 96, 392, 1344, 4320, 12080, 34848, 93936]


LOCAL = ("route_fibre", "route_rs", "census", "read_out", "post_run_check", "controls", "lemma_f_beyond")


def _load(name):
    """this arc's module, with its sibling imports resolved to this arc's files: the generic names (census, controls) exist in
    other arcs, so a module of the same name left in sys.modules by another lock is dropped first"""
    if str(VER) in sys.path:
        sys.path.remove(str(VER))
    sys.path.insert(0, str(VER))
    for other in LOCAL:
        mod = sys.modules.get(other)
        if mod is not None and Path(str(getattr(mod, "__file__", ""))).resolve().parent != VER.resolve():
            del sys.modules[other]
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, VER / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def _json(name):
    return json.loads((VER / name).read_text(encoding="utf-8"))


# ------------------------------------------------------------------------------------------------- the seal
def test_the_seal_is_unchanged():
    """PREREGISTRATION.md is byte-identical to the sealed text (SEAL_LEDGER) and carries the provenance markers"""
    assert hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest() == SEALED_SHA
    txt = (ARC / "PREREGISTRATION.md").read_text(encoding="utf-8")
    assert "BANKED IDENTITY:" in txt and "PRIOR ART:" in txt
    assert SEALED_SHA in (ROOT / "docs" / "SEAL_LEDGER.md").read_text(encoding="utf-8")


def test_the_sealed_files_are_unchanged():
    """every file hashed at the seal (the instruments and the design-time controls) is byte-identical"""
    lines = [l.split() for l in (ARC / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8").splitlines() if l and not l.startswith("#")]
    assert len(lines) == 6
    for digest, rel in lines:
        assert hashlib.sha256((ARC / rel).read_bytes()).hexdigest() == digest, rel
    assert _json("controls.json")["all passed"] is True


# ------------------------------------------------------------------------------------------------- the records
def test_the_census_record():
    """twelve levels, both routes agreeing on every character, the unfixed counts as banked, and 196 of 196 firing members fixed"""
    c = _json("census.json")
    rows = c["levels"]
    assert [r["n"] for r in rows] == list(range(1, 13))
    assert [r["order"] for r in rows] == ORDERS
    assert [r["unfixed at generic lam"] for r in rows] == GENERIC
    assert [r["unfixed at unitary lam"] for r in rows] == UNITARY
    assert all(r["routes agree on every character"] and r["disagreements"] == [] for r in rows)
    assert [r["group order on characters"] for r in rows] == [4, 8] + [8 * n for n in range(3, 13)]
    assert rows[4]["generic unfixed described"]["by golden type at split primes"] == {"11:phi-line": 10, "11:phibar-line": 10}
    assert rows[6]["unitary unfixed described"]["by golden type at split primes"] == {"29:mixed": 392}
    f = c["firing"]
    assert f["members"] == 196 and f["fixed"] == 196 and f["unfixed"] == []


def test_the_read_out():
    """P1-P9 held, outcome B, the golden reading in its sealed form, and the after-the-run section marked as such"""
    r = _json("read_out.json")
    assert r["held"] == 9 and all(v["held"] for v in r["predictions"].values()) and r["outcome"] == "B"
    assert r["expected from the priors"] == 7.85
    g = r["golden reading"]
    assert g["sealed form holds (criterion route F = route R on n <= 12; criterion bypassed by X2 on n <= 6)"] is True
    assert g["unfixed exactly the single-sheet twists on"] == [5]
    lv = g["per level"]
    assert (lv["7"]["mixed only"], lv["9"]["with a single-sheet component"], lv["10"]["with a single-sheet component"]) == (392, 576, 2500)
    assert (lv["9"]["at |lam| = 1: single-sheet still unfixed"], lv["10"]["at |lam| = 1: single-sheet still unfixed"]) == (432, 2480)
    assert all(lv[k].get("no split prime") for k in ("6", "8", "12"))
    after = r["after the run (not sealed)"]
    for lam, row in after["M5 case-(b) members by lam"].items():
        assert row["members"] == 20 and row["equal to the 20 vacua no reflection fixes"], lam
        assert row["sheets"] == {"phi-line": 10, "phibar-line": 10, "other": 0} and (row["E"], row["A"]) == (0, 20), lam
    held = after["how each level's members are held"]
    assert held["level 5"]["only by a rotation (A, not E)"] == 80
    assert all(h["only by a rotation (A, not E)"] == 0 for k, h in held.items() if k != "level 5")


def test_the_post_run_record():
    """X1-X4 passed: the criterion bypassed on M_1-M_6 agrees character by character, only dualising words fix at q = 2, all 196
    members are fixed directly, and at q = 1 the instrument fixes more (Lemma U) with non-dualising words"""
    p = _json("post_run_check.json")
    assert p["all passed"] is True and p["X1"]["passed"] and p["X2"]["passed"] and p["X3"]["passed"] and p["X4"]["passed"]
    fixed = {"generic": [1, 5, 16, 45, 101, 224], "real": [1, 5, 16, 45, 101, 224], "unitary": [1, 5, 16, 45, 121, 224]}
    for kind, want in fixed.items():
        for n, w in zip(range(1, 7), want):
            row = p["X2"]["rows"][f"{n} {kind}"]
            assert row["fixed directly"] == w == row["fixed by the census"] and row["agree character by character"], (n, kind)
            assert row["non-dualising fixing words"] == 0 and row["largest Hom dimension"] == 1, (n, kind)
    assert p["X3"]["members"] == 196 and p["X3"]["fixed"] == 196
    x4 = p["X4"]["rows"]
    assert (x4["5 unitary"]["fixed directly"], x4["6 unitary"]["fixed directly"]) == (121, 320)
    assert (x4["5 generic"]["fixed directly"], x4["6 generic"]["fixed directly"]) == (101, 224)
    assert all(r["agree character by character"] and r["non-dualising fixing words"] > 0 for r in x4.values())


# ------------------------------------------------------------------------------------------------- live
def test_live_both_routes_and_lemma_F():
    """route F and route R agree on every character of M_1 ... M_7, with Lemma F's closed counts at n = 5 and 7"""
    C = _load("census")
    for n in range(1, 8):
        row = C.level_census(n)
        assert row["routes agree on every character"], n
        assert (row["unfixed at generic lam"], row["unfixed at unitary lam"]) == (GENERIC[n - 1], UNITARY[n - 1]), n
    for n, p in ((5, 11), (7, 29)):
        assert (p - 1) * (p + 1 - 2 * n) == GENERIC[n - 1] and (p - 1) * (p - 1 - 2 * n) == UNITARY[n - 1]


def test_live_the_criterion_bypassed_on_M5():
    """the direct module test over F_89 (no criterion) fixes exactly the census's 101 characters off the circle, and only by
    dualising words"""
    P = _load("post_run_check")
    RF = _load("route_fibre")
    L = P.Level(5)
    f = RF.flags(5)
    for v in L.chars:
        found = L.fixing_words(v, L.g, [("V", v, L.g)])
        assert bool(found) == f["flags"][v]["E"], v
        assert all(w["dualising"] for w in found), v


def test_live_M5_members_are_the_single_sheet_twists():
    """B1511/B1512's case-(b) members on M_5 are, at every lam in mu_4, exactly the twists no reflection fixes, ten on each golden
    sheet, and a golden rotation fixes each"""
    C = _load("census")
    RF = _load("route_fibre")
    chars, order, N = RF.characters(5)
    f = RF.flags(5)
    unfixed = {v for v in chars if not f["flags"][v]["E"]}
    pop = [m for m in C.firing_population() if m["level"] == 5 and m["source"].startswith("case (b)")]
    for lam in ("1", "-1", "i", "-i"):
        mem = {tuple(m["char"]) for m in pop if m["lam"] == lam}
        assert mem == unfixed, lam
        assert sorted(C.eigen_type(v, N, 11) for v in mem) == ["phi-line"] * 10 + ["phibar-line"] * 10
        assert all(f["flags"][v]["A"] for v in mem)


def test_live_lemma_F_beyond_the_sealed_range():
    """X5: on M_13 (L_13 = 521) independent code counts 257 920 and 256 880 unfixed, Lemma F's closed counts; the record agrees"""
    X = _load("lemma_f_beyond")
    out = X.run()
    assert out["passed"] and out["group order"] == 104
    assert (out["unfixed off the circle"], out["unfixed on the circle"]) == (257920, 256880)
    assert out["odd-n Lucas numbers mod 5 (n < 200)"] == [1, 4]
    rec = _json("lemma_f_beyond.json")
    assert {k: v for k, v in rec.items() if k != "seconds"} == {k: v for k, v in out.items() if k != "seconds"}


@pytest.mark.slow
def test_the_census_rerun():
    """the sealed census rerun in full reproduces every level's counts"""
    C = _load("census")
    for n in range(8, 13):
        row = C.level_census(n)
        assert row["routes agree on every character"] and row["order"] == ORDERS[n - 1]
        assert (row["unfixed at generic lam"], row["unfixed at unitary lam"]) == (GENERIC[n - 1], UNITARY[n - 1]), n


@pytest.mark.slow
def test_the_post_run_rerun_on_M6():
    """the direct module test on M_6 over F_241 reproduces 224 fixed at the unitary reading, only by dualising words"""
    P = _load("post_run_check")
    RF = _load("route_fibre")
    L = P.Level(6)
    f = RF.flags(6)
    lam, lam_inv = L.g, pow(L.g, -1, L.p)
    fixed = 0
    for v in L.chars:
        vbar = ((-v[0]) % L.N, (-v[1]) % L.N)
        found = L.fixing_words(v, lam, [("V", v, lam), ("conj", vbar, lam_inv)])
        assert bool(found) == (f["flags"][v]["E"] or f["flags"][v]["A"]), v
        assert all(w["dualising"] for w in found)
        fixed += bool(found)
    assert fixed == 224


# ------------------------------------------------------------------------------------------------- the record
def test_the_kill_graph_note_and_the_registry_row():
    """B1520's hatch 'a cyclic level's family with a larger outer group' carries the dated test; T-GOLDEN-CHOICE is rowed"""
    kg = json.loads((ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json").read_text(encoding="utf-8"))
    rec = [r for r in kg if r.get("id") == "B1520"]
    assert len(rec) == 1 and "TESTED (2026-10-02, sm:B1522)" in rec[0]["note"]
    reg = (ROOT / "docs" / "THEOREM_REGISTRY.md").read_text(encoding="utf-8")
    row = [l for l in reg.splitlines() if l.startswith("| T-GOLDEN-CHOICE |")]
    assert len(row) == 1 and "| B1522 |" in row[0] and "tests/test_b1522_the_golden_choice.py" in row[0]


def test_findings_verdict_and_hygiene():
    """the verdict is PROVED with creates_law, EXTENDS, 0 of 19; the findings carry the answer, the predictions, the checks, the
    after-the-run marking and the scope; the owner's private term, vendor words and Gate 5-Q's words are absent"""
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1522" and v["verdict"] == "PROVED" and v["creates_law"] is True and v["identifications"] == []
    assert v["prior_work"]["standing"] == "EXTENDS" and "b1522-tmp" not in v["prior_work"]["repo"]["heads"]
    assert v["scope"]["frame"] == "F-HE" and v["scope"]["reach"] == "class"
    assert "0 of 19" in v["claim_one_line"] and "I-26 stays UNEARNED" in v["claim_one_line"]
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    for needle in ("**Verdict: PROVED, outcome B.**", "## Seen first (the repo sweep and the literature)",
                   "| 11 | 39 601 | 199, 199 | 199 split | 88 | 35 244 | 34 848 |",
                   "Nine of nine held; 7.85 were expected.", "## 6. After the run (not sealed): where M₅'s chiral configurations sit",
                   "That part is theirs.", "*Terminology:*", "**The gloss \"a broken vacuum chooses a sheet\" is exact only on M₅.**",
                   "`5d4eb5f7`", "I-26 stays UNEARNED", "0 of 19"):
        assert needle in f, needle
    term = bytes([98, 114, 97, 118, 101]).decode()  # the owner's private term, kept out of the source text
    vendor = re.compile(r"\b(" + "|".join(__import__("base64").b64decode(b).decode() for b in
                                         (b"Y2xhdWRl", b"YW50aHJvcGlj", b"b3B1cw==", b"c29ubmV0", b"ZmFibGU=")) + r")\b", re.I)
    # Gate 5-Q (Q5): the arc's own text never uses the experiential vocabulary; the one occurrence allowed is the owner's
    # message, quoted verbatim as the seal's source (its own spelling marks the line)
    gate5q = re.compile(r"\b(qualia|aware|sees)\b", re.I)
    for path in list(ARC.glob("*.md")) + list(VER.glob("*.py")) + [ARC / "arc_verdict.json"]:
        text = path.read_text(encoding="utf-8")
        assert term not in text.lower(), path
        assert not vendor.search(text), path
        for line in text.splitlines():
            if gate5q.search(line):
                assert path.name == "PREREGISTRATION.md" and "all oallowed not just m004, choice might be golden" in line, (path, line)
