"""B819 — locks the frame-gap correction to B817.

The residue of unverdicted arcs is NOT explained by missing FINDINGS.md. Most of it was never
assigned. This lock fails if that stops being true -- e.g. after a third wave closes the gap --
which is the correct time to revisit the claim.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FRONTIER = ROOT / "frontier"


def _dirs_without_verdict():
    return [d for d in sorted(FRONTIER.iterdir())
            if d.is_dir() and not (d / "arc_verdict.json").is_file()]


def test_most_unverdicted_dirs_DO_have_findings():
    """The fact B817 got backwards."""
    no_v = _dirs_without_verdict()
    with_f = [d for d in no_v if (d / "FINDINGS.md").is_file()]
    assert len(no_v) > 0
    assert len(with_f) / len(no_v) > 0.5, (
        f"only {len(with_f)}/{len(no_v)} unverdicted dirs have FINDINGS.md -- B819's correction "
        f"assumed the majority do; re-check the residue's composition")


def test_b817_carries_the_correction():
    f = " ".join((FRONTIER / "B817_verdict_wave2" / "FINDINGS.md").read_text(
        encoding="utf-8").split())
    assert "CORRECTED by B819" in f
    assert "coverage-frame gap, not a data gap" in f


def test_b519_was_the_lone_nonstandard_layout_and_is_now_verdicted():
    """B819 found B519 the only arc recording its result in VERDICT.md rather than FINDINGS.md.

    B826 then gave it a verdict, so it no longer sits in the unverdicted set. The enduring facts
    are that the layout is still unique and that the arc is no longer stranded (B829).
    """
    import json as _json
    arc = FRONTIER / "B519_re_mining"
    assert not (arc / "FINDINGS.md").is_file() and (arc / "VERDICT.md").is_file()
    assert _json.loads((arc / "arc_verdict.json").read_text(encoding="utf-8"))["verdict"] == "RETRACTED"
    others = [d.name for d in _dirs_without_verdict()
              if not (d / "FINDINGS.md").is_file()
              and any(p.name.startswith("VERDICT") for p in d.glob("*.md"))]
    assert others == [], f"a new nonstandard-layout arc appeared unverdicted: {others}"


def test_the_frame_gap_is_real_and_large():
    """Distinct arc ids in frontier vs ids that carry a verdict -- the gap B819 names."""
    ids = {m.group(1) for d in FRONTIER.iterdir() if d.is_dir()
           for m in [re.match(r"(B\d+)[a-zA-Z]?_", d.name)] if m}
    judged = {json.loads(p.read_text(encoding="utf-8"))["id"]
              for p in FRONTIER.glob("*/arc_verdict.json")}
    assert len(ids - judged) > 50, (
        "the unjudged-id gap has closed -- revisit B819's 'one more wave' recommendation")
