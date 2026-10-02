"""B1516 lock -- GENESIS v1 (2026-10-02). The owner asked for the genesis to be locked once, with every document reflecting
it, and feared that negatives computed on m004 alone were being read as blocks on the whole programme. GENESIS.md v1.0 states
the foundations once, with IDs unused anywhere else (PF, GM, SE, T-ROOT, F-xx, FK, GAP), and the scope tag became data.
PROVED (re-derived with own code; nothing was an open outcome, so nothing was sealed).
Locked here:
- the verification record (C1-C10) and its load-bearing values;
- live: the integer checks C1-C4 and C8-C10 re-run (about a second);
- GENESIS.md: version, sections, every v1.0 ID, the statuses of SE1, T-ROOT and SE2, the corrected class count, well-formed
  tables, and the citation rule for its IDs elsewhere;
- the scope tag: on the arc verdict, required by the schema from B1516 on, and present on every kill-graph entry this seat
  wrote from B1369 on (the ranges B1369-B1399 and B1500 on), with the over-reach notes on B1385, B1504, B1506 and B1511;
- the views: the closed-door map's scope section and the reviewer page's object paragraph;
- the uniqueness theorem's pointer and its corrected section 5;
- the findings' load-bearing sentences, and hygiene."""
import functools
import importlib.util
import json
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1516_genesis_v1"
VER = ARC / "verification"
GENESIS = ROOT / "GENESIS.md"
KG = ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json"

V1_IDS = (["PF1", "PF2", "PF3", "GM1", "GM2", "GM3", "GM4", "GM5a", "GM5b", "GM5c", "GM5d", "SE1", "SE2", "T-ROOT",
           "F-FC", "F-CI", "F-HE", "F-AP"] + [f"FK{i}" for i in range(1, 12)] + [f"GAP{i}" for i in range(1, 6)])
ID_TOKEN = re.compile(r"\b(PF[1-3]|GM[1-5][a-d]?|SE[12]|T-ROOT|FK(?:[1-9]|1[01])|GAP[1-5])\b")


@functools.lru_cache(maxsize=None)
def _checks():
    spec = importlib.util.spec_from_file_location("b1516_foundations_checks", VER / "foundations_checks.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@functools.lru_cache(maxsize=None)
def _record():
    return json.loads((VER / "foundations_checks_run.txt").read_text(encoding="utf-8"))


@functools.lru_cache(maxsize=None)
def _genesis():
    return GENESIS.read_text(encoding="utf-8")


def _seat_entry(eid):
    m = re.fullmatch(r"B(\d+)", eid)
    return bool(m) and (1369 <= int(m.group(1)) <= 1399 or int(m.group(1)) >= 1500)


# ------------------------------------------------------------------------------------------------ the record
def test_record_all_passed():
    r = _record()
    assert r["all passed"] is True
    for k in ("C1 records route", "C2 torsion selector", "C3 order bit", "C4 word census", "C8 necessity (integer part)",
              "C9 the unit shears generate every state", "C10 the metallic family", "C5-C7 SnapPy"):
        assert r[k]["passed"] is True, k


def test_record_values():
    r = _record()
    c2 = r["C2 torsion selector"]
    assert (c2["unimodular matrices"], c2["hyperbolic"], c2["torsion-free hyperbolic matrices"]) == (616, 408, 48)
    assert c2["their (det, trace)"] == [[-1, -1], [-1, 1], [1, 3]] and c2["unmatched"] == []
    c4 = r["C4 word census"]
    assert c4["states per length (signed)"] == [2, 2, 4, 6, 10, 18, 32, 56, 102, 186, 340] and c4["total"] == 758
    assert c4["torsion-free states"] == ["+LR"]
    s = r["C5-C7 SnapPy"]
    assert s["C5 orientable states to length 6"] == 24 == s["C5 distinct census names"]
    assert s["C5 names"]["+LR"] == "m004" and s["C5 names"]["-LR"] == "m003" and s["C5 names"]["-LLR"] == "m010"
    assert s["C5 non-orientable bundles read (to length 6)"] == 46
    assert s["C5 torsion-free non-orientable bundles"] == ["m000"]
    assert [s["C6 tower names (n = 1..6)"][str(n)]["name"] for n in range(1, 7)] == [
        "m004", "m206", "s961", "t12839", "o10_150696", "otet12_00013"]
    assert s["C6 orientation cover of m000"] == "m004" and s["C6 m000 orientable"] is False
    assert s["C6 tower torsion |2 - tr A^n| (n = 1..12)"][:6] == [1, 5, 16, 45, 121, 320]
    f = s["C7 fillings of m004"]
    assert f["(1, 0)"]["H1"] == "0" and f["(1, 0)"]["pi1 generators after simplification"] == 0
    assert f["(0, 1)"]["H1"] == "Z" and f["(5, 1)"]["H1"] == "Z/5" and abs(f["(5, 1)"]["volume"] - 0.981369) < 1e-6
    assert s["C8 5_2: H1, solution, volume"][:2] == ["Z", "all tetrahedra positively oriented"]
    assert s["C10 b++L^mR^m: H1 (m = 1..5)"]["1"] == "Z" and s["C10 b++L^mR^m: H1 (m = 1..5)"]["3"] == "Z/3 + Z/3 + Z"
    n = r["C8 necessity (integer part)"]
    assert n["without GM3: non-hyperbolic det-1 matrices with torsion-free H1, by trace"] == {"1": 12, "2": 17}
    g = r["C9 the unit shears generate every state"]
    assert g["hyperbolic det-1 matrices"] == 168 and g["not reduced"] == 0
    assert g["reduced to +-(positive word with both letters), explicit SL(2,Z) conjugator found"] == 168


# ------------------------------------------------------------------------------------------------ live
def test_live_integer_checks():
    m = _checks()
    assert m.check_records_route()["passed"]
    assert m.check_order_bit()["passed"]
    c4, rows = m.check_census()
    assert c4["passed"] and c4["total"] == 758
    assert m.check_necessity()["passed"]
    assert m.check_metallic()["passed"]
    assert m.check_generation(rows, box=3)["passed"]


def test_live_torsion_selector_small_box():
    m = _checks()
    out = m.check_torsion_selector(box=3, bound=5)
    assert out["passed"] and out["their (det, trace)"] == [(-1, -1), (-1, 1), (1, 3)]


def test_live_torsion_formula_and_golden_square():
    m = _checks()
    G = m.mul(m.L, m.P)
    assert G == ((1, 1), (1, 0)) and m.mul(G, G) == m.mul(m.L, m.R)
    assert m.torsion(m.mul(m.L, m.R)) == 1 and m.torsion(G) == 1
    assert m.coker_minus_identity(((1, -1), (1, 0))) == (0, [])            # the order-6 monodromy: H1 = Z


@pytest.mark.slow
def test_live_snappy_part():
    pytest.importorskip("snappy")
    out = _checks().snappy_checks()
    assert out.get("passed") is True


# ------------------------------------------------------------------------------------------------ GENESIS.md
def test_genesis_version_and_sections():
    g = _genesis()
    assert g.startswith("# GENESIS — the foundations of origin-axiom")
    # v1.0 is B1516's; a later arc amends the head line and adds its own log entry (B1517, main's B1454, B1519), so the head
    # line is pinned by form and v1.0 by its log entry. From v1.1 the page is main's and the SM seat's together, and the
    # seat's arc numbers carry `sm:` (main's B1454; GENESIS §0).
    assert re.search(r"^\*\*Version 1\.\d+ · \d{4}-\d{2}-\d{2} · (?:arcs? [^*]*B1516[^*]* · )?canonical\.\*\*", g, flags=re.M)
    heads = re.findall(r"^## (\d+)\. ", g, flags=re.M)
    assert heads == [str(i) for i in range(11)]
    assert "Where any document disagrees with this file, this file holds" in g
    assert "Only an arc may change it." in g and re.search(r"^- \*\*v1\.0 · 2026-10-02 · (?:sm:)?B1516\.\*\*", g, flags=re.M)


def test_genesis_ids_and_statuses():
    g = _genesis()
    for i in V1_IDS:
        assert re.search(r"(?<![\w-])" + re.escape(i) + r"(?![\w])", g), i
    rows = {m.group(1): m.group(0) for m in re.finditer(r"^\| (SE1|T-ROOT|SE2|GM[1-5][a-d]?) \|.*$", g, flags=re.M)}
    assert "| POSTULATED |" in rows["SE1"] and "| DERIVED |" in rows["T-ROOT"] and "| CHOSEN |" in rows["SE2"]
    assert "| OPEN |" in rows["GM5b"] and "| OPEN |" in rows["GM5c"] and "| CHOSEN |" in rows["GM5d"]
    for old in ("| G1 |", "| S1 |", "| K1 |", "| P1 |"):                 # the colliding draft labels are not IDs
        assert old not in g


def test_genesis_load_bearing_statements():
    g = " ".join(_genesis().split())                                    # wrapping-independent
    assert re.search(r"\*\*Four inputs suffice, and each is needed\*\* \((?:sm:)?B1516 C8\)\.", g)
    assert "m004's class has 99 census members, the arithmetic part of B1186's 112-member family" in g
    assert "they are conjugate in SL(2,ℤ) by L, since L⁻¹(LR)L = RL (not by P, whose determinant is −1)" in g
    assert "**The family is the intended shape.**" in g
    assert "the object preceded the axioms" in g
    assert "**A result is a statement about a frame applied to an object, never about the architecture as such.**" in g
    assert "**0 of 19**" in g


def test_genesis_tables_well_formed():
    lines = _genesis().splitlines()
    tables, i = 0, 0
    while i < len(lines):
        if lines[i].startswith("|") and i + 1 < len(lines) and re.match(r"^\|(\s*-+\s*\|)+\s*$", lines[i + 1]):
            tables += 1
            n = lines[i].count("|")
            j = i + 2
            while j < len(lines) and lines[j].startswith("|"):
                assert lines[j].count("|") == n, (j + 1, lines[j][:60])
                j += 1
            i = j
        else:
            i += 1
    assert tables == 9


def _sealed_unchanged(p, ledger):
    """A preregistration whose current sha-256 is recorded in SEAL_LEDGER is frozen by its hash (B1518)."""
    import hashlib
    return p.name == "PREREGISTRATION.md" and hashlib.sha256(p.read_bytes()).hexdigest() in ledger


def test_v1_ids_are_cited_as_genesis_elsewhere():
    """Outside GENESIS.md and this arc, a v1.0 ID appears only in a paragraph that names GENESIS (the citation rule).
    The rule binds living text. A sealed preregistration, unchanged since its hash was ledgered, cannot be amended and is
    exempt (B1518's seal carried 'T-ROOT' in a paragraph without the word; ERROR_LEDGER, 2026-10-02)."""
    skip_dirs = {".git", "node_modules", "__pycache__"}
    ledger = (ROOT / "docs" / "SEAL_LEDGER.md").read_text(encoding="utf-8")
    bad = []
    for p in ROOT.rglob("*.md"):
        rel = p.relative_to(ROOT)
        if set(rel.parts) & skip_dirs or rel == Path("GENESIS.md") or rel.parts[:2] == ("frontier", ARC.name):
            continue
        if _sealed_unchanged(p, ledger):
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        if not ID_TOKEN.search(text):
            continue
        for para in re.split(r"\n\s*\n", text):
            if ID_TOKEN.search(para) and "GENESIS" not in para:
                bad.append((str(rel), ID_TOKEN.search(para).group(0)))
    assert not bad, bad[:10]


# ------------------------------------------------------------------------------------------------ scope as data
def test_arc_verdict():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1516" and d["verdict"] == "PROVED" and d["instrument"] is False
    assert d["creates_law"] is False and d["identifications"] == []
    sc = d["scope"]
    assert sc["frame"] == "none" and sc["reach"] == "general" and sc["object"] and isinstance(sc["hypotheses"], list)
    assert "|" not in d["claim_one_line"] and "0 of 19" in d["claim_one_line"]


def test_schema_requires_scope_from_b1516():
    t = (ROOT / "tests" / "test_arc_verdict_schema.py").read_text(encoding="utf-8")
    assert "SCOPE_REQUIRED_FROM = 1516" in t and 'SCOPE_REACH = {"single", "class", "general"}' in t


def test_kill_graph_scope_on_this_seats_entries():
    kg = json.loads(KG.read_text(encoding="utf-8"))
    seat = [e for e in kg if _seat_entry(e["id"])]
    assert len(seat) >= 29
    for e in seat:
        sc = e.get("scope")
        assert isinstance(sc, dict), e["id"]
        assert sc["frame"] in {"F-FC", "F-CI", "F-HE", "F-AP", "none"} or sc["frame"], e["id"]
        assert sc["reach"] in {"single", "class", "general"} and sc["object"], e["id"]
        assert isinstance(sc["hypotheses"], list) and sc["hypotheses"], e["id"]
    by = {e["id"]: e["scope"] for e in seat}
    assert by["B1385"]["frame"] == "F-FC" and "main B1439" in by["B1385"]["note"]
    assert any("q != 1" in h for h in by["B1511"]["hypotheses"]) and "q != 1" in by["B1511"]["note"]
    assert "m004's own data" in by["B1504"]["note"]
    assert by["B1506"]["frame"] == "F-CI" and by["B1506"]["reach"] == "single"
    assert all(by[i]["frame"] == "F-HE" and by[i]["reach"] == "single" for i in
               ("B1509", "B1510", "B1511", "B1513", "B1514", "B1515"))


def test_scope_pass_is_idempotent():
    spec = importlib.util.spec_from_file_location("b1516_scope_pass", VER / "scope_pass.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    kg = json.loads(KG.read_text(encoding="utf-8"))
    by = {e["id"]: e.get("scope") for e in kg}
    assert all(by[k] == v for k, v in mod.SCOPES.items())


def test_views_carry_the_scope():
    cd = (ROOT / "docs" / "views" / "CLOSED_DOORS.md").read_text(encoding="utf-8")
    assert "## How far each closure reaches (" in cd and "| `B1515` | `F-HE` | single |" in cd
    rv = " ".join((ROOT / "docs" / "views" / "REVIEWER.md").read_text(encoding="utf-8").split())
    assert "A generated state space, stated once in `GENESIS.md`" in rv
    assert "never about the architecture as such" in rv


# ------------------------------------------------------------------------------------------------ the pointers and the findings
def test_uniqueness_pointer_and_correction():
    u = (ROOT / "docs" / "UNIQUENESS_THEOREM.md").read_text(encoding="utf-8")
    assert "**Canonical status (2026-10-02): `../GENESIS.md` v1.0.**" in u
    assert "A5 → SE1 (a POSTULATED criterion; what it selects, T-ROOT, is DERIVED)" in u
    assert "conjugate in `SL(2,ℤ)` by `L`" in u and "that is a `GL(2,ℤ)` conjugation" in u


def test_findings_and_hygiene():
    f = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert f.startswith("# B1516 — GENESIS v1:")
    assert "**SE1 is a criterion, and it is postulated.**" in f
    assert "four inputs suffice, and each is needed" in f
    assert "the draft called B1186's 112-member family \"m004's class\"" in f
    assert "I-26 stays UNEARNED. **0 of 19.**" in f
    term = bytes([98, 114, 97, 118, 101]).decode()  # the owner's private term, kept out of the source text
    for p in [GENESIS, ARC / "FINDINGS.md", ARC / "arc_verdict.json", VER / "foundations_checks.py", VER / "scope_pass.py",
              Path(__file__)]:
        assert term not in p.read_text(encoding="utf-8").lower(), p.name
