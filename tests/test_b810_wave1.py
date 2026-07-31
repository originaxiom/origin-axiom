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
        # B826 widened this: the rule is "no verdict without a substantive findings document",
        # not "without a file named FINDINGS.md". B519 records its result in VERDICT.md.
        assert any((d / n).is_file() for n in ("FINDINGS.md", "VERDICT.md")), \
            f"verdict written for an arc with no findings document: {d}"


def test_pilot_verdicts_were_not_overwritten_by_the_fanout():
    """3 arcs already carried authored verdicts; the writer must never replace one."""
    # Prefix match, not equality: B834 APPENDED correction provenance to two pilot records
    # ("W1-pilot; corrected by B834 ..."), and an exact-match read that as two lost verdicts.
    # The invariant is that the pilot's record survives, not that its string is byte-identical.
    pilot = [p for p in _verdicts()
             if (json.loads(Path(p).read_text()).get("authored_by") or "").startswith("W1-pilot")]
    assert len(pilot) >= 30, f"pilot verdicts lost: {len(pilot)} remain"
