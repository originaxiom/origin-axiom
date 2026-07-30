"""B821 — locks the REVERT and the decomposition that corrects B820.

A failed experiment needs locks as much as a successful one: the lock is what stops the reverted
change from creeping back in, and what pins the finding that justified reverting it.
"""
import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_SPEC = importlib.util.spec_from_file_location("atlas", ROOT / "scripts" / "atlas" / "atlas.py")
atlas = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(atlas)


def test_the_failed_motif_is_NOT_in_the_lexicon():
    """Sealed criterion 2 failed at 46.2% vs a 25% ceiling. It stays out."""
    assert "self_audit" not in atlas.LEXICON, (
        "the self_audit motif matched 46.2% of the corpus and was reverted per B821's seal")


def test_obstacles_values_are_all_keyword_lists():
    """The wiring bug: a lexicon-shaped dict landed in OBSTACLES, whose classifier iterates values
    as keyword lists. Handed a dict it would have scored arcs against 'kind'/'gloss'/'patterns'."""
    bad = {k: type(v).__name__ for k, v in atlas.OBSTACLES.items() if not isinstance(v, list)}
    assert not bad, f"OBSTACLES values must be keyword lists; got {bad}"


def test_lexicon_entries_all_have_patterns():
    bad = [k for k, v in atlas.LEXICON.items()
           if not isinstance(v, dict) or "patterns" not in v]
    assert not bad, f"LEXICON entries must be dicts with patterns; got {bad}"


def test_the_ambient_register_finding_holds():
    """'prereg' is in >20% of arcs -- which is WHY the meta-layer cannot be a distinguishing motif."""
    files = list((ROOT / "frontier").glob("*/FINDINGS.md"))
    n = sum(1 for f in files
            if re.search("prereg", f.read_text(encoding="utf-8", errors="replace"), re.I))
    assert n / len(files) > 0.20, (
        f"'prereg' now in {n}/{len(files)} arcs -- B821's ambient-register argument assumed >20%")


def test_b537_was_the_single_genuine_gap_and_is_now_closed():
    """B821 named B537 the one real lexicon gap. B825 closed it -- with a NARROW motif.

    The enduring claim is B821's DECOMPOSITION (14 stubs + 6 instrument + exactly 1 real gap),
    not that the gap stayed open. Locking it closed by the narrow motif preserves both.
    """
    d = json.loads((ROOT / "scripts" / "atlas" / "atlas_data.json").read_text(encoding="utf-8"))
    motifs = d["probes"].get("B537", {}).get("motifs") or []
    assert "markov_cubic" in motifs, (
        "B537 was the single genuine gap B821 identified; B825 closed it and that must hold")


def test_findings_records_the_correction_to_b820():
    f = " ".join((ROOT / "frontier" / "B821_lexicon_refresh" / "FINDINGS.md").read_text(
        encoding="utf-8").split())
    assert "CORRECTS B820" in f
    assert "one arc, not twenty-one" in f
    assert "pre-stated expectation was SUCCESS. It was wrong" in f
