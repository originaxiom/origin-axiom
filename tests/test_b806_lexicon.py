"""B806 — locks the lexicon-blindness finding and its ceiling."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _atlas():
    return json.loads((ROOT / "scripts" / "atlas" / "atlas_data.json").read_text())


def test_the_lexicon_is_a_small_hand_authored_closed_vocabulary():
    """The finding's premise: the atlas can only ever see what it was told to look for."""
    lex = _atlas()["lexicon"]
    assert len(lex) == 18, f"lexicon size changed from 18 to {len(lex)} -- re-derive B806's numbers"
    src = (ROOT / "scripts" / "atlas" / "atlas.py").read_text()
    assert "LEXICON = {" in src                      # hand-authored, not derived from the corpus
    assert "K001..K022" in src                       # and its grounding is frozen, by its own header


def test_zero_motif_probes_exist_and_include_a_substantive_recent_arc():
    """B798 defines the programme's own current falsifier and is invisible to the atlas."""
    P = _atlas()["probes"]
    blind = {k for k, v in P.items() if not v.get("motifs")}
    assert blind, "if this empties, the lexicon was widened -- update B806"
    assert "B798" in blind, (
        "B798 (the algebraicity falsifier's power box) was the decisive instance: the instrument "
        "built to detect what recurs could not see the programme's own falsifier")


def test_concentration_is_bounded_by_the_lexicon_not_measured_from_the_corpus():
    """3 motifs covering >90% is a statement about 18 labels, not about the object."""
    P = _atlas()["probes"]
    from collections import Counter
    mot = Counter(m for v in P.values() for m in v.get("motifs", []))
    assert len(mot) <= 18                            # cannot exceed the closed vocabulary
    top3 = {m for m, _ in mot.most_common(3)}
    cov = sum(1 for v in P.values() if set(v.get("motifs", [])) & top3) / len(P)
    assert cov > 0.85, "the concentration claim in B806 rests on this"
