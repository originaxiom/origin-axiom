"""B1161 lock -- the frontier sweep (compute-all-we-can): 6 cells typed, the computable frontier mapped +
exhausted; the bypass door IS SEAM-A (one obstruction = the missing archimedean marking). Asserts on
COMMITTED files only. Own reproducer for the SEAM-A PSLQ-vacuity + generation-index NULL. Gate 5 clean."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1161_frontier_sweep"


def _d():
    return json.loads((ARC / "b1161_results.json").read_text(encoding="utf-8"))


def test_arc_verdict_open():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1161" and d["verdict"] == "OPEN"
    assert d["instrument"] is False and d["creates_law"] is False


def test_bypass_door_is_seam_a():
    h = _d()["headline_unification"]
    assert "BYPASS DOOR IS SEAM-A" in h
    assert "FREE-ORBIT THEOREM" in h and "freely" in h.lower()
    assert "ARCHIMEDEAN MARKING" in h and "W0" in h
    assert "same" in h.lower() and "obstruction" in h.lower()


def test_crown_not_forced_scoped_positives():
    c = _d()["cells"]["P1P2_force"]
    assert c["outcome"].startswith("NOT-FORCED")
    assert "unique" in c["scoped_positives"].lower() and "coprime CRT split" in c["scoped_positives"]
    assert "K-rational" in c["scoped_positives"]


def test_l132_dual_homed():
    c = _d()["cells"]["L132_B892"]
    assert c["outcome"].startswith("CONVERGES")
    assert "A2+A2" in c["own_verified"] and "36/36 SM" in c["own_verified"]


def test_seam_a_pslq_vacuous_stays_floor():
    c = _d()["cells"]["SEAM_A_seal"]
    assert "VACUOUS" in c["outcome"] and "NEEDS-SPECIALIST" in c["outcome"]
    assert "PSLQ is LIVE" in c["own_verified"] and "recovers B682" in c["own_verified"]
    assert "Arakelov/W0" in c["exact_bar"] and "RETIRED as vacuous" in c["exact_bar"]


def test_generation_null_one_generation():
    c = _d()["cells"]["generation_index"]
    assert c["outcome"].startswith("NULL")
    assert "NEVER 3" in c["own_verified"]
    assert "ONE generation" in c["result"]


def test_down_yukawa_present_unlike_up():
    c = _d()["cells"]["down_Yukawa"]
    assert "3x3x4 tensor" in c["structural_result"]
    assert "UNLIKE the up-Yukawa" in c["structural_result"] and "ABSENT" in c["structural_result"]


def test_reproduce_runner_committed_and_reproduces():
    runners = list((ARC / "verification").glob("reproduce*.sh"))
    assert runners and "REPRODUCES" in runners[0].read_text(encoding="utf-8")
    out = (ARC / "verification" / "frontier_checks.txt").read_text(encoding="utf-8")
    assert "REPRODUCES" in out
    assert "PSLQ(Vol, sqrt3*L)= [-2, 3]" in out and "PSLQ(1/6, Vol)    = None" in out
    assert "NEVER 3" in out
    # the full frontier map is committed too
    assert (ARC / "verification" / "frontier_map.txt").exists()


def test_firewall_gate5_clean():
    d = _d()
    assert d["firewall_gate5"].startswith("CLEAN") and "No firewall crossing" in d["fences"]


def test_the_generation_index_cell_carries_its_scope_note():
    """Added 2026-11-13 by the building session (card C17; register row P-606, verified by main at B1906, section 3a):
    the cell's words stay, and the dated note scoping them stands below the table and in the verdict line."""
    import json, re
    arc = Path(__file__).resolve().parents[1] / "frontier" / "B1161_frontier_sweep"
    flat = lambda t: re.sub(r"\s+", " ", re.sub(r"^\s*>\s?", "", t, flags=re.M).replace("**", "").replace("`", ""))
    page = flat((arc / "FINDINGS.md").read_text(encoding="utf-8"))
    scoped = "Scoped, it holds: a Galois orbit in a quadratic field has one or two elements, since the group has order 2."
    unscoped = "Unscoped, B298's headline is false, three ways on m004"
    old = page.index("| generation-index | NULL |")
    note = page.index("Dated note, 2026-11-13 (register row P-606", old)
    assert note - old < 2500 and scoped in page[note:] and unscoped in page[note:]
    line = json.loads((arc / "arc_verdict.json").read_text(encoding="utf-8"))["claim_one_line"]
    assert "NEVER 3" in line and line.index("NEVER 3") < line.index("DATED NOTE 2026-11-13, register row P-606")
    assert scoped in line and unscoped in line
