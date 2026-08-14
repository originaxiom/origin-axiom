"""P5 Draft v1 — WITHDRAWN (Phase 3). These locks now guard the withdrawal, not the claims.

The draft's core is Baake-Grimm-Joseph 1993. Its disciplines were sound and its content was not;
keeping the old assertions green would say the opposite.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "papers" / "P5_monoid" / "DRAFT_v1.md"


def _t():
    """Normalised text: strip blockquote markers and emphasis before joining.

    A first version joined raw whitespace and missed two phrases because markdown `>` continuation
    markers interleaved mid-sentence ("would be > false"). Same class as the bolded-value miscount
    in B845 -- a lock defeated by formatting rather than by content.
    """
    raw = D.read_text(encoding="utf-8")
    # strip REPEATED blockquote markers: the draft nests them ("> >"), and a single-level strip
    # left a stray ">" mid-sentence. Fifth instance of formatting defeating a literal lock this
    # week -- the normaliser must be idempotent, not one-pass.
    lines = [re.sub(r"^(?:\s*>\s?)+", "", ln) for ln in raw.splitlines()]
    return " ".join(" ".join(lines).replace("**", "").split())


def test_the_draft_is_marked_WITHDRAWN():
    """It must not be possible to read DRAFT_v1 without meeting the verdict first."""
    head = D.read_text(encoding="utf-8")[:400]
    assert head.startswith("# ⚠️ WITHDRAWN"), "the withdrawal banner must be the first thing in the file"
    t = _t()
    assert "Baake, Grimm & Joseph" in t and "1993" in t
    assert "Do not cite it" in t


def test_the_disciplines_are_still_recorded_even_though_the_draft_failed():
    """The two-cell rows and the cited toral floor were RIGHT; only the content was pre-empted."""
    t = _t()
    for k in ("EVIDENCE", "HYPOTHESIS VERIFIED", "generated FREELY by L and R", "Reutenauer"):
        assert k in t, f"{k} must survive in the withdrawn text as a record of the method"
