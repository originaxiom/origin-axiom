"""B1235 addendum — the nine recovered relays READ. Locks the corrections, not the reading.

If a later edit restores "three generations … banked" without B897's scope, or re-fuses the field with the knot
at THE_FRAMEWORK's Layer 2, the suite reds. These are the two E53 instances (#11, #12) that lived 24–25 days on
flagship docs because the relay that flagged them was untracked and lost.
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _t(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def test_three_generations_carries_its_scope_on_both_surfaces():
    for rel in ("docs/THE_SM_VERDICT.md", "docs/THE_FRAMEWORK.md"):
        s = _t(rel)
        line = next(l for l in s.splitlines() if "three generations" in l and "B897, B928" in l)
        assert "generation-SHAPED at the tiling level" in line, rel
        assert "mechanism-hood FENCED" in line, rel
        assert "B298" in line and "B891" in line, rel


def test_layer2_names_the_field_not_the_knot():
    s = _t("docs/THE_FRAMEWORK.md")
    i = s.index("E₆-across-faces is forced** (B727) — the atom being ℚ(√−3) as the unique arithmetic knot")
    window = s[i:i + 900]
    assert "forced by the **field** ℚ(√−3)" in window
    assert "commensurability-class invariant (B803:81)" in window
    assert "ZERO steps" in window and "B993:49" in window


def test_layer3_and_layer5_cross_references():
    s = _t("docs/THE_FRAMEWORK.md")
    assert "split by B994 — the ENDPOINT is forced by registerability alone" in s
    assert "banked as B1022 C1 — the weight ledger" in s


def test_b718_addendum_names_line_95_only_and_the_check_reproduces():
    a = _t("frontier/B718_child_program/ADDENDUM_2026-09-02_cusp_area_not_longitude_B1235.md")
    assert "b718_probe4.py:95" in a and "**What is NOT wrong.** Line 148" in a
    out = _t("frontier/B1235_two_seat_harvest/verification/b718_cusp_area_check.txt")
    assert "|longitude| == area at the maximal cusp: True" in out
    assert "is pi^2 * (cusp AREA)" in out and "Line 148" in out


def test_ledgers_carry_the_read():
    e = _t("docs/ERROR_LEDGER.md")
    assert "E53 instances #11–#12" in e and "E51 CLOSED on content" in e
    r = _t("docs/RELAY_LEDGER.md")
    for name in ("FRAMEWORK_DELTA", "HARVEST_MANIFEST", "DAY_LOG", "PROGRAMME_ASSEMBLY", "L114_DISCHARGE", "CORNERSTONE_PLAN"):
        row = next(l for l in r.splitlines() if f"CC3_TO_CC_2026-08-09_{name}.md" in l)
        assert row.split(" | ")[1] == "BANKED", name
    o = _t("docs/OPEN_LEADS.md")
    assert "## L195 — THE REVIVABLE INDEX" in o and "## L196 — B1–B5 HAVE NO `arc_verdict.json`" in o
    add = _t("frontier/B1235_two_seat_harvest/ADDENDUM_2026-09-02_the_nine_relays_read_B1235.md")
    assert "E53 instance** (#11)" in add


def test_l196_b1_b5_carry_verdicts():
    """L196 (B1235 addendum): the five genesis probes carry verdicts; the two negatives are routed."""
    import json
    want = {"B1_gluing_chern_simons": "OPEN", "B2_moduli_evolution": "NEGATIVE", "B3_regge_complex": "OPEN",
            "B4_bkl_gutzwiller": "OPEN", "B5_wheeler_dewitt": "NEGATIVE"}
    for d, verdict in want.items():
        v = json.loads((ROOT / "frontier" / d / "arc_verdict.json").read_text(encoding="utf-8"))
        assert v["verdict"] == verdict and v["id"] == d.split("_")[0] and v["identifications"] == [], d
    g = json.loads((ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json").read_text(encoding="utf-8"))
    rows = {e["id"]: e for e in g}
    assert rows["B2"]["kill_form"] == "kind-mismatch" and "B67" in rows["B2"]["note"]
    assert rows["B5"]["kill_form"] == "kind-mismatch" and "B980" in rows["B5"]["note"]
