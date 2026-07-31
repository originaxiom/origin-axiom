"""B833 — locks the measurement and the unit-mismatch finding."""
import glob
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KG = ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json"


def _graph():
    return json.loads(KG.read_text(encoding="utf-8"))


def _negatives():
    out = {}
    for p in glob.glob(str(ROOT / "frontier" / "*" / "arc_verdict.json")):
        d = json.loads(Path(p).read_text(encoding="utf-8"))
        if d.get("verdict") == "NEGATIVE":
            out[d["id"]] = d
    return out


def test_the_unrouted_count_is_inside_b801s_predicted_interval():
    """A sampling estimate checked against the census it predicted."""
    ids = {r.get("id") for r in _graph() if isinstance(r.get("id"), str)}
    unrouted = set(_negatives()) - ids
    assert 55 <= len(unrouted) <= 168, (
        f"{len(unrouted)} unrouted negatives is outside B801's 95% CI of 55-168; "
        f"either the estimate or the count needs re-deriving")


def test_the_kill_graph_is_NOT_an_arc_level_register():
    """45 of its keys are not arc ids at all -- so a ratio against arc verdicts is unitless."""
    ids = [r.get("id") for r in _graph() if isinstance(r.get("id"), str)]
    non_arc = [i for i in ids if not (i.startswith("B") and i[1:].isdigit())]
    assert len(non_arc) >= 20, (
        "the kill graph should still carry cell/wall keys; if it does not, B833's unit-mismatch "
        "finding needs revisiting")


def test_kill_records_legitimately_sit_on_PROVED_arcs():
    """An arc can prove one thing while killing another; this is correct, not contradictory."""
    verd = {}
    for p in glob.glob(str(ROOT / "frontier" / "*" / "arc_verdict.json")):
        d = json.loads(Path(p).read_text(encoding="utf-8"))
        verd[d["id"]] = d["verdict"]
    ids = [r.get("id") for r in _graph() if isinstance(r.get("id"), str)]
    on_proved = [i for i in ids if verd.get(i) == "PROVED"]
    assert len(on_proved) >= 10, (
        "B833's finding is that kill records frequently sit on net-positive arcs")


def test_the_findings_refuses_both_coverage_percentages():
    f = " ".join((ROOT / "frontier" / "B833_negative_routing"
                  / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert 'neither 66 % nor 33.5 % is "the coverage of negatives"' in f
    assert "fact_computed" in f and "unset rather than guessed" in f
