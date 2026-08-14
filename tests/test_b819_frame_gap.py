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


def test_the_residue_INVERTED_once_the_wave_B819_asked_for_ran():
    """B819's finding was that MOST unverdicted dirs had FINDINGS -- they were simply never
    assigned. Waves 3a/3b judged exactly those, so the residue has inverted: what is left is
    overwhelmingly directories with NO findings document, which are unwritable by design.

    This lock fired as a tripwire when the inversion happened. It now asserts the inversion,
    which is the state B819's recommendation was supposed to produce (B835).
    """
    no_v = _dirs_without_verdict()
    with_f = [d for d in no_v if (d / "FINDINGS.md").is_file()]
    assert len(no_v) > 0
    assert len(with_f) / len(no_v) < 0.35, (
        f"{len(with_f)}/{len(no_v)} unverdicted dirs still have FINDINGS.md -- if this rises again, "
        f"a new population of judgeable arcs has appeared and needs a wave")


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


def test_the_frame_gap_has_CLOSED():
    """B819 measured a 229-id gap and recommended one more wave. Two ran; the gap is now ~47.

    The original assertion (gap > 50) was a TRIPWIRE whose message read "the unjudged-id gap has
    closed -- revisit B819's recommendation". It fired, and this is that revisit (B835): the
    recommendation was executed, so the lock now guards the closed state instead.
    """
    ids = {m.group(1) for d in FRONTIER.iterdir() if d.is_dir()
           for m in [re.match(r"(B\d+)[a-zA-Z]?_", d.name)] if m}
    judged = {json.loads(p.read_text(encoding="utf-8"))["id"]
              for p in FRONTIER.glob("*/arc_verdict.json")}
    gap = len(ids - judged)
    assert gap < 60, f"the unjudged gap has re-opened to {gap} -- a further wave is due"
    assert len(judged) / len(ids) > 0.90, "coverage regressed below 90% of arc ids"
