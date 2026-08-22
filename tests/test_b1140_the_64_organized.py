"""B1140 lock -- THE 64 ORGANIZED (the finale): the E6(-26) spacetime branch's 64 fixed
dimensions decompose under su(2)xsu(2)xsu(3) as a graviton (two color-singlet spin-2) + 54
colored bi-vectors, with INVARIANT CONTENT ZERO -- so hypercharge cannot organize there. The
campaign's tenth honest value-negative, the first by STRUCTURE (= the rep-level restatement of
the fork z=0, B1138). Verified two-bench (cloud memo 27 + this bench's own re-derivation,
slot-independent). The full re-derivation runs in ~7s directly in the lock."""
import json
import subprocess
import sys
from pathlib import Path

ARC = Path(__file__).resolve().parents[1] / "frontier" / "B1140_the_64_organized"
RESULTS = ARC / "b1140_results.json"
FINDINGS = ARC / "FINDINGS.md"
VERIF = ARC / "verification"
REPO = Path(__file__).resolve().parents[1]
KILLGRAPH = REPO / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json"


def _load():
    return json.loads(RESULTS.read_text(encoding="utf-8"))


# ---------------------------------------------------------------- the subalgebra = the fork's
def test_subalgebra_is_the_fork():
    d = _load()["subalgebra"]
    assert d["dim"] == 14 and d["rank"] == 14
    assert d["ladder"] == [16, 8, 8, 0]      # the fork's own ladder (B1138)
    assert d["joint_centralizer"] == 0        # = the invariant-content-zero core


# ---------------------------------------------------------------- the 64 + decomposition
def test_the_64_decomposition_pinned():
    r = _load()
    assert r["complement"]["dim"] == 64 == r["dim_check"]      # 5+5+27+27
    dec = r["decomposition"]
    dims = sorted(p["dim"] for p in dec)
    assert dims == [5, 5, 27, 27]
    # exactly two color-singlet spin-2 gravitons
    gravitons = [p for p in dec if p["su3"] == "1"]
    assert len(gravitons) == 2 and all(p["dim"] == 5 for p in gravitons)
    assert {(p["spin_T1"], p["spin_T2"]) for p in gravitons} == {(2, 0), (0, 2)}
    # the other 54 are colored (3 + 3bar), each spin-1 x spin-1
    colored = [p for p in dec if p["su3"] in ("3", "3bar")]
    assert sum(p["dim"] for p in colored) == 54
    assert all((p["spin_T1"], p["spin_T2"]) == (1, 1) for p in colored)


# ---------------------------------------------------------------- the load-bearing negative
def test_invariant_content_zero_and_checks():
    c = _load()["checks"]
    assert c["invariant_content_zero"] == "CONFIRMED"
    assert c["total_dim_64"] == "CONFIRMED"
    assert c["two_color_singlet_spin2_gravitons"] == "CONFIRMED"
    assert c["remaining_54_all_colored"] == "CONFIRMED"
    assert c["slot_independent"].startswith("CONFIRMED")


# ---------------------------------------------------------------- the honest scope note
def test_theta_gluing_flagged_unchecked():
    r = _load()
    assert "NOT checked" in r["scope_note"] and "NOT confirmed, NOT refuted" in r["scope_note"]
    t = FINDINGS.read_text(encoding="utf-8")
    assert "graviton" in t and "colored bi-vectors" in t
    assert "TENTH" in t or "tenth" in t                # the tenth honest negative
    assert "nothing shared" in t                       # the closing composition


# ---------------------------------------------------------------- the negative is routed (B836)
def test_negative_routed_into_kill_graph():
    kg = json.loads(KILLGRAPH.read_text(encoding="utf-8"))
    entry = [e for e in kg if e.get("id") == "B1140"]
    assert len(entry) == 1, "B1140 must be routed into the kill-graph (B836)"
    e = entry[0]
    assert "value hypothesis" in e["claim_killed"]
    assert "INVARIANT CONTENT ZERO" in e["kill_form"] or "invariant content" in e["kill_form"].lower()


# ---------------------------------------------------------------- the reproduction (~7s)
def test_the_64_reproduces_independently():
    """Own Killing-complement + joint highest-weight enumeration on the banked e6 --
    the whole finale re-derived from scratch, slot-independent."""
    r = subprocess.run([sys.executable, str(VERIF / "verify_memo27.py")],
                       capture_output=True, text=True, cwd=str(REPO), timeout=300)
    assert r.returncode == 0, r.stderr[-2000:]
    out = r.stdout
    assert "(a) total dim 64:" in out and "CONFIRMED" in out
    assert "(b) invariant content = 0:" in out
    assert "ALL CHECKS: CONFIRMED" in out
    assert "slot-independent" in out
