"""B844 — locks the continuation-line-aware review-actions gate.

The old block regex matched only a CONTIGUOUS run of "- [.]" lines, so an action item that wrapped
onto a second line truncated the block. For recent reviews it saw ONE item each and reported 0 open
items in superseded blocks when the true count was 13.
"""
import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_S = importlib.util.spec_from_file_location("gates", ROOT / "scripts" / "gates" / "gates.py")
g = importlib.util.module_from_spec(_S)
_S.loader.exec_module(g)
REV = ROOT / "docs" / "progress" / "REVIEWS.md"


def test_the_gate_sees_whole_blocks_not_just_the_first_run():
    """The defect: multi-line items truncated the block. Blocks must now be many items each."""
    t = REV.read_text(encoding="utf-8")
    parts = re.split(r"### Action items \(Review [^)]+\)\n", t)
    blocks = [p.split("\n## ")[0].split("anchor-commit")[0] for p in parts[1:]]
    recent = blocks[-5:]
    counts = [len(re.findall(r"^- \[", b, re.M)) for b in recent]
    assert all(c >= 4 for c in counts), (
        f"recent blocks parse to {counts} items -- the old regex saw 1 each, which is the bug")


def test_the_gate_passes_and_can_still_fail():
    ok, msg = g.gate_review_actions()
    assert ok, msg
    # negative control: an open item in a superseded block must fail
    t = REV.read_text(encoding="utf-8")
    try:
        REV.write_text(t.replace("- [x] R34-7:", "- [ ] R34-7:", 1), encoding="utf-8")
        bad, m2 = g.gate_review_actions()
        assert not bad and "open item" in m2, "the gate must fail on a reopened superseded item"
    finally:
        REV.write_text(t, encoding="utf-8")


def test_carried_items_state_WHY_they_are_carried():
    """A `[>]` with no reason is a deferral wearing a disposition's name.

    The property is that an explanation FOLLOWS the id -- not that any particular word appears.
    An earlier form of this test looked for the literal "CARRIED" and flagged nine items that each
    gave a perfectly good reason in different words: a lock pinned to a magic string rather than
    the invariant, which is the defect class B829/B835 named.
    """
    t = REV.read_text(encoding="utf-8")
    carried = re.findall(r"^- \[>\] (R[\d-]+[^\n]*)", t, re.M)
    assert carried, "no carried items found"
    # The prefix strip must remove the ID and its separator ONLY. An earlier form used
    # `^R[\d-]+[^:]*:?` -- greedy up to a colon -- so a colon-free item had its entire reason
    # eaten by the strip and was then flagged for having no reason: the lock's own regex
    # manufacturing the defect it hunts (first seen 2026-08-29, on two items that each read
    # "R49-N -> folded into R50-M (...)"). Bounded here; the bare-ID control below still fires.
    _ID = r"^R[\d-]+\s*[:\u2192\u2014-]?\s*"
    bare = [c[:60] for c in carried
            if len(re.sub(_ID, "", c).strip()) < 25]
    assert not bare, f"carried items with no substantive reason: {bare}"
    # MB12: the strip must still expose a bare ID, or the lock passes over anything.
    assert len(re.sub(_ID, "", "R99-9").strip()) < 25
