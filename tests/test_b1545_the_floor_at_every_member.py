"""B1545 -- THE FLOOR AT EVERY MEMBER: the lock (PROVED, not sealed).

  - Lemma F at members, checked: every reading of members_check.json holds (h0(dN; W1*) = 2|A| + |B| and h1(dN; W1) as the
    proof says, exactly; r1(W1) <= 3|A| + |B| - k; I(W1) >= k - |A| - b0; the identity), with both values of b0 and cusps of
    every kind present;
  - Corollary G's census: on the four room-3 covers the puncture values are constant on cusps and multiply to 1, and a character
    whose fourth power is a puncture character kills the punctures of at most two of the four cusps;
  - the verdict, the registry row and the kill entry.
Nothing here writes a tracked file."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1545_the_floor_at_every_member"
V = ARC / "verification"
FOUR = ("m135.D8.2-0-4.w1", "m135.D8.4-0-2.w4", "m136.D8.2-0-4.w3", "m136.D8.4-0-2.w5")


def test_lemma_f_at_members_holds_at_every_reading():
    rec = json.loads((V / "members_check.json").read_text())
    rows = rec["rows"]
    assert rec["all hold"] is True and rec["n"] == len(rows) >= 250
    for r in rows:
        A, B, k, b0 = len(r["A"]), len(r["B"]), r["k"], r["b0"]
        assert r["h0(dN;W*)"] == r["pred h0(dN;W*)"] == 2 * A + B
        assert r["h1(dN;W)"] == r["pred h1(dN;W)"]
        assert r["r1(W)"] <= 3 * A + B - k == r["bound r1"]
        assert r["I(W)"] >= k - A - b0 == r["bound I"]
        assert r["identity"] is True and set(r["A"]).isdisjoint(r["B"]) and k <= A
    assert {r["b0"] for r in rows} == {0, 1}
    assert any(r["B"] for r in rows) and any(len(r["A"]) + len(r["B"]) < r["cusps"] for r in rows)
    assert {r["cover"] for r in rows} >= set(FOUR) and len({r["cover"] for r in rows}) >= 30


def test_corollary_g_census():
    c = json.loads((V / "orbit_census.json").read_text())
    assert set(c) == set(FOUR)
    for cid in FOUR:
        x = c[cid]
        assert x["cusps"] == 4
        assert x["zeta(l_x) constant on pi-orbits"] is True and x["product over the punctures = 1"] is True
        assert x["most cusps whose punctures zeta kills, when zeta^4 is a puncture character"] <= 2
        assert x["with zeta^4 a puncture character"] > 0


def test_the_verdict_and_its_records():
    v = json.loads((ARC / "arc_verdict.json").read_text())
    assert v["id"] == "B1545" and v["verdict"] == "PROVED" and v["creates_law"] is True and v["instrument"] is False
    reg = (ROOT / "docs" / "THEOREM_REGISTRY.md").read_text()
    assert "| T-THE-VANISHING-CUSPS-AT-EVERY-MEMBER |" in reg
    kills = json.loads((ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json").read_text())
    assert [x["kill_form"].split(" ")[0] for x in kills if x.get("id") == "B1545"] == ["too-few-trivial-cusps"]
    f = (ARC / "FINDINGS.md").read_text()
    assert "cc (the SM-derivation seat), 2026-10-06." in f and "## Seen first" in f and "0 of 19" in f
