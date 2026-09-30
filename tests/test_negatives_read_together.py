"""The negatives read together (2026-09-30) -- locks the classification of the chirality chain's kill records and the rule
it restores: a record this seat routes carries its content (B1207's A3), held by this lock rather than by memory (E45).

docs/THE_NEGATIVES_READ_TOGETHER_2026-09-30.md; frontier/B738_pathfinder_compiler/kill_graph.json."""
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KG = ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json"
DOC = ROOT / "docs" / "THE_NEGATIVES_READ_TOGETHER_2026-09-30.md"
FAMILIES = {"symmetry-cannot-select", "closed-sum-zero", "frame-arithmetic", "end-datum-input", "absence-at-depth",
            "no-landing-site"}


def _graph():
    return json.loads(KG.read_text(encoding="utf-8"))


def _table():
    rows = re.findall(r"^\| (B\d+) \| (PROVED|NEGATIVE) \| ([a-z-]+) \|", DOC.read_text(encoding="utf-8"), re.M)
    return {a: (v, f) for a, v, f in rows}


def _family(rec):
    return rec["kill_form"].split(" (")[0]


def test_this_seats_routings_carry_content():
    """E45's fix for this seat: every record it routes names a kill form, locates its deciding computation, and gives a hatch
    that is a revival route (B1207's bar: longer than 80 characters)."""
    mine = [r for r in _graph() if str(r.get("routed_from") or "").startswith("sm-branch-")]
    assert len(mine) >= 26
    for r in mine:
        assert r["kill_form"] != "unrouted-unclassified", r["id"]
        assert r["fact_computed"] is True, r["id"]
        assert isinstance(r.get("hatch"), str) and len(r["hatch"]) > 80, r["id"]
        assert r["priority"] in {"P1", "P2", "P3", "P4", "LOW"} and isinstance(r["revival_score"], int), r["id"]
        assert isinstance(r["faces_consulted"], list) and r["faces_consulted"], r["id"]
        assert "DELIBERATELY UNSET" not in r.get("note", ""), f"{r['id']}: the note contradicts the filled fields (B830)"


def test_the_table_is_the_graph():
    table = _table()
    assert len(table) == 26
    g = {r["id"]: r for r in _graph() if isinstance(r.get("id"), str)}
    for arc, (verdict, family) in table.items():
        assert family in FAMILIES, arc
        assert _family(g[arc]) == family, arc
        d = next((ROOT / "frontier").glob(f"{arc}_*"))
        assert json.loads((d / "arc_verdict.json").read_text(encoding="utf-8"))["verdict"] == verdict, arc


def test_the_tally():
    c = Counter(f for _, f in _table().values())
    assert c == Counter({"frame-arithmetic": 9, "symmetry-cannot-select": 8, "closed-sum-zero": 4, "end-datum-input": 3,
                         "absence-at-depth": 1, "no-landing-site": 1})
    doc = " ".join(DOC.read_text(encoding="utf-8").split())
    assert ("`frame-arithmetic` 9 · `symmetry-cannot-select` 8 · `closed-sum-zero` 4 · `end-datum-input` 3 · "
            "`absence-at-depth` 1 · `no-landing-site` 1, 26 records") in doc


def test_every_located_computation_exists():
    """fact_computed = true is a claim that the deciding computation is in the repository (B833): the note names its lock, and
    the lock and the arc's verification exist."""
    g = {r["id"]: r for r in _graph() if isinstance(r.get("id"), str)}
    for arc in _table():
        note = g[arc]["note"]
        locks = re.findall(r"tests/test_b\d+_[a-z0-9_]+\.py", note)
        assert locks and all((ROOT / p).exists() for p in locks), arc
        assert list((next((ROOT / "frontier").glob(f"{arc}_*")) / "verification").glob("*.py")), arc


def test_the_proved_arcs_entered_are_new_records_and_the_placeholders_left_are_not_this_seats():
    g = _graph()
    new = [r["id"] for r in g if r.get("routed_from") == "sm-branch-2026-09-30-read-together"]
    assert sorted(new) == ["B1351", "B1385", "B1389", "B1390", "B1392", "B1393", "B1394", "B1395", "B1396", "B1500"]
    left = [r for r in g if r.get("kill_form") == "unrouted-unclassified"]
    assert not [r["id"] for r in left if str(r.get("routed_from") or "").startswith("sm-branch-")]


def test_the_flags_are_recorded():
    doc = " ".join(DOC.read_text(encoding="utf-8").split())
    strings = sorted(r["id"] for r in _graph() if isinstance(r.get("faces_consulted"), str))
    assert strings == ["B1084", "B1086", "B1094", "B1096", "B1108", "B1137", "B1140", "B1142", "B1258", "B1259", "B1262",
                       "B1300"]
    assert all(a in doc for a in strings) and "Flagged, not changed" in doc
    for a in ("B1352", "B1354", "B1370", "B1377", "B1381"):
        assert a in doc, f"{a}: out of scope, and the note must say so"
