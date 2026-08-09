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
    # 19 since B825 added `markov_cubic`. This tripwire fired and its demand was MET rather than
    # bumped: B806's numbers were re-derived (B829). Top-3 coverage is now 0.8845, against the
    # 93.3 % B806 states -- and the drift is entirely CORPUS GROWTH, verified by recomputing with
    # markov_cubic excluded and getting the identical 0.8845.
    assert len(lex) == 19, f"lexicon size changed from 19 to {len(lex)} -- re-derive B806's numbers"
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
    """3 motifs covering >90% is a statement about 18 labels, not about the object.

    THE 0.85 FLOOR WAS BREACHED AND IS NOT REPLACED BY A LOWER ONE (B1008, 2026-08-09).
    Series: B806 stated 0.933 -> B829 re-derived 0.8845 -> B1008 measured 0.8496. Bumping the
    number to keep the lock green is the post-hoc rescue this repository forbids, and B829 set
    the opposite precedent: when this tripwire fires, RE-DERIVE.

    The re-derivation superseded the statistic. The aggregate turned out to be a weighted
    average across an instrument that works in one era and not another (B1008's epoch table),
    so an aggregate floor was measuring the corpus's age mix, not the claim. B806's actual
    thesis -- concentration is a fact about the LABELS, not the object -- is now locked by
    test_the_lexicon_is_epoch_specific below, which tests it far more sharply and can fail.
    """
    P = _atlas()["probes"]
    from collections import Counter
    mot = Counter(m for v in P.values() for m in v.get("motifs", []))
    assert len(mot) <= len(_atlas()["lexicon"])      # structural: cannot exceed the closed vocabulary
    top3 = {m for m, _ in mot.most_common(3)}
    cov = sum(1 for v in P.values() if set(v.get("motifs", [])) & top3) / len(P)
    # Recorded, not defended: the aggregate is superseded by the epoch table. The wide band
    # only catches a gross regression (a lexicon rewrite or a broken probe attachment).
    assert 0.5 < cov < 0.95, f"top-3 coverage {cov:.4f} is outside any regime B1008 measured"


def test_the_lexicon_is_epoch_specific():
    """B1008 — THE REPLACEMENT LOCK, and the sharper form of B806's thesis.

    A statistic about the OBJECT would be stable across the corpus. This one is fitted to an
    era: coverage peaks where the lexicon was authored (B201-400) and collapses in the
    SM-structure campaign (B801-900). That gap IS the evidence that concentration measures the
    labels rather than the object, and unlike the old aggregate floor it can genuinely fail --
    widening the lexicon, or re-grounding it on the current corpus, would close the gap.
    """
    import re
    from collections import Counter
    P = _atlas()["probes"]
    mot = Counter(m for v in P.values() for m in v.get("motifs", []))
    top3 = {m for m, _ in mot.most_common(3)}

    def band(lo, hi):
        sel = [v for k, v in P.items()
               if (m := re.search(r"B(\d+)", k)) and lo <= int(m.group(1)) <= hi]
        assert sel, f"band B{lo}-{hi} is empty -- the probe keys changed shape"
        return (sum(1 for v in sel if set(v.get("motifs", [])) & top3) / len(sel),
                sum(1 for v in sel if v.get("motifs")) / len(sel),
                sum(len(v.get("motifs", [])) for v in sel) / len(sel))

    early_cov, _, early_den = band(201, 400)     # 0.995, 5.95 at B1008
    late_cov, late_any, late_den = band(801, 900)  # 0.629, 0.921, 2.98 at B1008

    assert early_cov - late_cov > 0.2, (
        f"the epoch gap has closed ({early_cov:.3f} vs {late_cov:.3f}) -- if the lexicon was "
        "widened or re-grounded, B1008's finding needs re-deriving, not this lock relaxing")
    assert early_den > 1.5 * late_den, (
        f"motif DENSITY no longer halves ({early_den:.2f} vs {late_den:.2f}) -- that collapse "
        "is B1008's discriminating fact separating under-labelling from vocabulary drift")
    assert late_any > 0.85, (
        f"recent arcs carry SOME motif ({late_any:.3f}); if this falls they are invisible "
        "rather than under-labelled, which is a different finding and needs its own arc")


def test_the_recent_corpus_has_no_words_in_the_lexicon():
    """B1008's root cause: 14 of 14, and it is why the density halved.

    The lexicon's grounding is frozen at knowledge/K001..K022 -- the EARLY knowledge base --
    so the concepts the programme has spent its last 200 arcs on have no labels at all. This
    lock exists to make widening the lexicon a DELIBERATE, banked act: whoever adds these words
    changes every motif count in the repository and must say so.
    """
    lex = set(_atlas()["lexicon"])
    # the recent corpus's own vocabulary, by arc count at B800+ (B1008's table)
    absent = {"cascade", "e6", "the_27", "rank", "chirality", "measurement", "generation",
              "centralizer", "observer", "hypercharge", "anomaly", "higgs", "value_layer",
              "maass"}
    present = absent & lex
    assert not present, (
        f"{sorted(present)} entered the lexicon -- widening it re-dates every recurrence claim "
        "in the repository, so it must be banked as its own arc (B1008 §6), and B806/B1008's "
        "numbers must be re-derived at the same time")
