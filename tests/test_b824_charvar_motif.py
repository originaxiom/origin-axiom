"""B824 — locks the reverted motif and the ambient-subject finding."""
import glob
import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_SPEC = importlib.util.spec_from_file_location("atlas", ROOT / "scripts" / "atlas" / "atlas.py")
atlas = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(atlas)


def test_the_failed_motif_is_not_in_the_lexicon_under_this_name():
    assert "char_variety" not in atlas.LEXICON, (
        "B824's motif matched 18.4% against a 15% ceiling and was reverted per its seal")


def test_character_variety_is_ambient_not_a_topic():
    """The finding that killed it: one pattern carried the whole overshoot."""
    files = glob.glob(str(ROOT / "frontier" / "*" / "FINDINGS.md"))
    n = sum(1 for f in files
            if re.search("character variety",
                         open(f, encoding="utf-8", errors="replace").read(), re.I))
    share = n / len(files)
    # B824's motif matched 18.4% against a 15% ceiling. This test originally re-asserted the bare
    # term stayed above 10% -- an ABSOLUTE threshold on a GROWING corpus, i.e. a drifting proxy for
    # a claim about pervasiveness. It fell through the floor on 2026-08-29 at 9.98% (1112 arcs)
    # without anything about the programme changing; ten arcs gaining a FINDINGS document that day
    # was enough. The enduring invariant is comparative and does not drift: the term is PERVASIVE
    # rather than NICHE. Stated as ratios against two genuine topics.
    def _share(term):
        k = sum(1 for f in files
                if re.search(term, open(f, encoding="utf-8", errors="replace").read(), re.I))
        return k / len(files)
    niche = max(_share("Maass"), _share("quasicrystal"))
    assert share >= 2.5 * niche, (
        f"'character variety' at {share:.1%} is no longer pervasive relative to a niche topic "
        f"({niche:.1%}) -- B824's diagnosis (ambient subject matter, not a topic within it) "
        f"would need re-examining, which is exactly what should happen")
    assert n >= 50, f"only {n} arcs mention it; the comparison would stop meaning anything"


def test_b537_was_closed_by_the_NARROW_motif_not_this_one():
    """B824 left B537 an open GAP; B825 closed it -- with the ambient term DROPPED.

    The enduring point is not that B537 stayed open (it did not) but WHICH motif closed it: the
    narrow Markov-cubic one, never the character-variety one B824 reverted.
    """
    import json
    p = json.loads((ROOT / "scripts" / "atlas" / "atlas_data.json").read_text(encoding="utf-8"))
    motifs = p["probes"].get("B537", {}).get("motifs") or []
    assert "markov_cubic" in motifs, "B537 should be covered by B825's narrow motif"
    assert "char_variety" not in motifs, "B824's reverted motif must never be what covers it"
