"""B810 — locks wave-1 coverage and the write-safety invariants."""
import glob
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _verdicts():
    return glob.glob(str(ROOT / "frontier" / "*" / "arc_verdict.json"))


def test_coverage_grew_and_every_record_is_wellformed():
    vs = _verdicts()
    assert len(vs) >= 317, f"coverage regressed: {len(vs)} authored verdicts"
    allowed = {"PROVED", "NEGATIVE", "OPEN", "RETRACTED"}
    for p in vs:
        r = json.loads(Path(p).read_text())
        assert r["verdict"] in allowed, f"{p}: bad verdict {r['verdict']}"
        assert r.get("claim_one_line"), f"{p}: empty claim"
        assert isinstance(r.get("instrument"), bool)


def test_no_verdict_exists_for_a_nonexistent_arc():
    """The honesty test cc's own transcription error supplied: 6 bad IDs, 0 fabricated arcs."""
    for p in _verdicts():
        d = Path(p).parent
        assert (d / "FINDINGS.md").is_file(), f"verdict written for an arc with no FINDINGS: {d}"


def test_pilot_verdicts_were_not_overwritten_by_the_fanout():
    """3 arcs already carried authored verdicts; the writer must never replace one."""
    pilot = [p for p in _verdicts()
             if json.loads(Path(p).read_text()).get("authored_by") == "W1-pilot"]
    assert len(pilot) >= 30, f"pilot verdicts lost: {len(pilot)} remain"
