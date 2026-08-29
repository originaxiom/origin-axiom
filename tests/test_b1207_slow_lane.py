"""B1207 — the slow lane's first full run, discharged.

These locks pin the five conditions the discharge established. They deliberately run in the FAST
lane: the defects they cover were invisible for days precisely because their own locks were
slow-gated, so the repairs are checked where the repairs are cheap to check.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1207_slow_lane_discharge"


def test_no_arc_verification_script_carries_an_absolute_machine_path():
    """A1: a script with the author's machine path in it runs on one bench and nowhere else,
    which is the opposite of what a verification/ directory asserts."""
    # The needle is assembled at runtime rather than written literally: a checker that spells out
    # the string it forbids trips the repo-wide scanner on itself. Same class as B1202's
    # already_banked.py quoting its own test phrases -- the instrument matching its own arc.
    needle = "/" + "Users" + "/"
    bad = [str(p.relative_to(ROOT)) for p in ROOT.glob("frontier/*/verification/*.py")
           if needle in p.read_text(encoding="utf-8", errors="ignore")]
    assert not bad, f"absolute machine paths in arc verification scripts: {bad[:6]}"


def test_every_verdict_carrying_arc_carries_a_findings_document():
    """A2: the mirror of B1176. A verdict with no body is a claim nobody can read."""
    orphan = sorted(p.parent.name for p in ROOT.glob("frontier/B1*/arc_verdict.json")
                    if not (p.parent / "FINDINGS.md").exists())
    assert not orphan, f"verdicts with no findings document: {orphan}"


def test_the_ten_authored_documents_declare_their_provenance():
    """The documents were authored FROM the banked verdicts, not from memory, and each must say
    so -- an unstamped retro-authored document is indistinguishable from a contemporaneous one."""
    ten = ["B1176_record_surface_wave", "B1177_instrument_bundle", "B1178_l184_lazyfy",
           "B1179_outreach_and_papers", "B1181_amphichirality_closure", "B1182_c4prime_resolved",
           "B1183_one_class_theorem", "B1194_existence_audit", "B1195_close_loop_batch5a",
           "B1196_close_loop_batch5b"]
    for arc in ten:
        body = (ROOT / "frontier" / arc / "FINDINGS.md").read_text(encoding="utf-8")
        assert "Provenance of this document" in body, arc
        assert "`arc_verdict.json` is primary" in body, arc


def test_the_two_late_negatives_are_routed_with_a_real_kill_form():
    """A3: B833's backlog rebuilt by two within four days of the pass that cleared it. Routed
    means routed WITH content -- an unclassified placeholder would re-open the same hole."""
    kg = json.loads((ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json")
                    .read_text(encoding="utf-8"))
    rows = {r["id"]: r for r in kg if r.get("id") in ("B1203", "B1205")}
    assert set(rows) == {"B1203", "B1205"}
    for i, r in rows.items():
        assert r["kill_form"] != "unrouted-unclassified", i
        assert r["fact_computed"] is True, i
        assert len(r["hatch"]) > 80, f"{i}: a hatch is a revival route, not a word"


def test_b1113s_root_resolves_to_the_repo_not_to_frontier():
    """C: two dirnames where three were needed made every join read frontier/frontier/... and the
    verifier could not run for eight days. The depth is the whole bug."""
    src = (ROOT / "frontier" / "B1113_tmeter" / "b1113_tmeter_verify.py").read_text(encoding="utf-8")
    block = src[src.index("REPO_ROOT ="):src.index("CCB_PATH =")]
    assert block.count("os.path.dirname(") == 3, "the file sits three levels below the root"
    assert "frontier/frontier" not in src


def test_the_review_gates_id_strip_is_bounded_both_ways():
    """B1: MB12 in one test -- the strip must still expose a bare ID (or the lock is vacuous) and
    must NOT eat a colon-free reason (or the lock manufactures its own defect)."""
    ID = r"^R[\d-]+\s*[:→—-]?\s*"
    assert len(re.sub(ID, "", "R99-9").strip()) < 25
    assert len(re.sub(ID, "", "R49-5 → folded into R50-6 (T-GOLDEN-MERIDIAN verify).").strip()) >= 25


def test_the_triage_records_both_the_real_and_the_artifact_findings():
    """The arc's value is the CLASSIFICATION, so the record must keep the not-real ones too --
    reporting only the five real defects would hide the 22% drift artifact that motivates the
    quiescence rule."""
    r = json.loads((ARC / "b1207_results.json").read_text(encoding="utf-8"))
    assert len(r["triage"]) == 9 == r["run"]["failed"]
    assert sum(1 for t in r["triage"] if t["real"]) == 5
    assert sum(1 for t in r["triage"] if t["class"] == "D") == 2
    assert "quiescent" in r["method_fact"]


def test_the_pslq_grid_writer_truncates_and_the_aggregator_dedupes():
    """E1: append + no resume logic = every re-run triple-counts the grid, which inflates
    M_grid_cells and deflates the Sidak alpha off multiplicity nobody tested. Both ends are
    pinned: a grid run must produce exactly its own cells, and a legacy contaminated grid must
    still aggregate correctly."""
    arc = ROOT / "frontier" / "B1137_regulator_probe"
    probe = (arc / "pslq_probe.py").read_text(encoding="utf-8")
    assert "with open(out_path, 'w') as f:" in probe, "the grid writer must truncate, not append"
    agg = (arc / "aggregate.py").read_text(encoding="utf-8")
    assert "seen = set()" in agg and "(r.get('name'), r.get('D'), r.get('H'))" in agg
    report = json.loads((arc / "results" / "final_report.json").read_text(encoding="utf-8"))
    assert report["M_grid_cells"] == 216, "the real grid is 216 cells; anything larger is duplicates"
    assert report["overall_verdict"] == "DISJOINT"


def test_the_tmeter_verifier_records_no_machine_path():
    """E2: a verifier that writes the running bench's absolute paths into a tracked results file
    is not reproducing its banked output -- it is overwriting it with local detail."""
    res = json.loads((ROOT / "frontier" / "B1113_tmeter" / "b1113_results.json")
                     .read_text(encoding="utf-8"))
    needle = "/" + "Users" + "/"          # assembled, not spelled -- see the note above
    for k, v in res["paths"].items():
        assert needle not in v, f"{k} carries a machine path"
    assert res["paths"]["ccb_path_used"].startswith("<repo>/")
