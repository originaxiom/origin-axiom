"""Locks the consolidation-coverage measurement — BOTH tiers, so the corrected metric cannot
silently revert to the wrong one.

History this exists to prevent repeating: the first version of
`docs/consolidation/DEBT_LEDGER.md` measured citation in FIVE curated surfaces and published the
result as "62 % of the corpus is cited on NO surface a reader navigates by". That was false.
Re-run against all thirteen navigational surfaces, **every** arc is carried somewhere — all 579
by `docs/views/VERDICT_LEDGER.md` (a generated index of every verdicted arc) and by the atlas.

The repository's architecture is deliberately two-tier (`GOVERNANCE` §12: *"Freeze the substrate;
generate the views; govern by metadata … Everything a reader or reviewer navigates by is a
view."*). Measuring one tier and reporting it as both is the error. These locks hold the two
tiers apart by construction.
"""
import glob
import json
import os
import re

import pytest

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Hand-written, distilled. Selective BY DESIGN — absence here is "not distilled".
CURATED = ["docs/LAW_MAP.md", "docs/THE_FRAMEWORK.md", "docs/THEOREM_LEDGER.md",
           "CLAIMS.md", "docs/THE_LADDER.md"]
# Regenerated from metadata, or append-only working registers. Complete BY DESIGN.
GENERATED_AND_WORKING = ["docs/views/VERDICT_LEDGER.md", "docs/views/CLOSED_DOORS.md",
                         "scripts/atlas/atlas_data.json", "docs/OPEN_LEADS.md",
                         "docs/progress/REVIEWS.md", "docs/CAMPAIGN_STATUS.md",
                         "docs/HINT_LEDGER.md", "docs/SEAL_LEDGER.md"]


def _read(rel):
    with open(os.path.join(_ROOT, rel), encoding="utf-8") as f:
        return f.read()


@pytest.fixture(scope="module")
def arcs():
    """Distinct B-numbers with an authored verdict. DISTINCT is load-bearing: B58 has three arc
    directories, and the first version of this measurement counted it twice (934 vs 933)."""
    seen, out = set(), []
    for d in sorted(glob.glob(os.path.join(_ROOT, "frontier", "B*"))):
        m = re.match(r"B(\d+)_", os.path.basename(d))
        if not m or not os.path.isfile(os.path.join(d, "arc_verdict.json")):
            continue
        bid = f"B{m.group(1)}"
        if bid in seen:
            continue
        seen.add(bid)
        with open(os.path.join(d, "arc_verdict.json"), encoding="utf-8") as f:
            out.append((bid, json.load(f).get("verdict", "")))
    return out


def _absent_from(files, arcs):
    blob = "\n".join(_read(p) for p in files)
    return [(b, v) for b, v in arcs if not re.search(rf"\b{b}\b", blob)]


def test_arc_ids_are_counted_distinctly_not_per_directory(arcs):
    ids = [b for b, _ in arcs]
    assert len(ids) == len(set(ids)), "a B-number was counted more than once"
    assert len(ids) > 900


def test_every_arc_is_carried_by_SOME_navigational_surface(arcs):
    """THE CORRECTION, pinned. Absent-from-everything must be ZERO.

    If this ever fails, an arc has genuinely fallen out of every index — a real defect. It must
    not fail because someone re-narrowed the surface list.
    """
    missing = _absent_from(CURATED + GENERATED_AND_WORKING, arcs)
    assert missing == [], f"arcs carried by no surface at all: {[b for b, _ in missing][:20]}"


def test_the_generated_verdict_ledger_alone_carries_every_arc(arcs):
    """Why the corrected number is 0: the generated view is a complete index by construction."""
    missing = _absent_from(["docs/views/VERDICT_LEDGER.md"], arcs)
    assert missing == [], f"generated verdict ledger is incomplete: {[b for b, _ in missing][:20]}"


def test_the_curated_gap_is_real_and_large(arcs):
    """The finding that SURVIVES the correction: the curated tier carries a minority.

    Bounded rather than pinned exactly, so ordinary consolidation work does not break the lock —
    but a collapse or a silent jump to full coverage both fail it.
    """
    absent = _absent_from(CURATED, arcs)
    share = len(absent) / len(arcs)
    assert 0.40 < share < 0.80, f"curated-absent share {share:.3f} outside the measured band"
    proved = [b for b, v in absent if v == "PROVED"]
    assert len(proved) > 200, f"only {len(proved)} PROVED arcs absent from curated surfaces"


def test_the_two_tiers_are_not_the_same_measurement(arcs):
    """The lock that makes the distinction structural rather than a comment: the curated tier
    must be strictly worse than the full set, or the correction has been undone by widening
    CURATED to include a generated view."""
    assert len(_absent_from(CURATED, arcs)) > len(_absent_from(CURATED + GENERATED_AND_WORKING, arcs))
    for p in CURATED:
        assert "views/" not in p and "atlas" not in p, f"{p} is generated, not curated"


def test_the_ledger_carries_the_correction_not_the_withdrawn_claim():
    """The withdrawn sentence must not reappear in the ledger."""
    t = _read("docs/consolidation/DEBT_LEDGER.md")
    assert "CORRECTED 2026-08-11" in t
    assert "Absent-from-everything is 0" in t
    assert "cited on NO surface at all" not in t.split("⚠ CORRECTED")[-1].split("---")[0].replace(
        '"580 of 934 arcs are cited on NO surface at all"', "")


def test_instrument_arcs_are_excluded_from_the_debt_count(arcs):
    """REFINEMENT: an instrument arc has no law to consolidate, so its absence is not debt.

    Counting them inflated the first cut by 53. The split also sharpens the target: B800+ is
    roughly half instrument, while B100-B499 is almost purely substantive.
    """
    import glob
    blob = "\n".join(_read(p) for p in CURATED)
    sub = inst = 0
    seen = set()
    for d in sorted(glob.glob(os.path.join(_ROOT, "frontier", "B*"))):
        m = re.match(r"B(\d+)_", os.path.basename(d))
        vp = os.path.join(d, "arc_verdict.json")
        if not m or not os.path.isfile(vp):
            continue
        bid = f"B{m.group(1)}"
        if bid in seen:
            continue
        seen.add(bid)
        with open(vp, encoding="utf-8") as f:
            dd = json.load(f)
        if dd.get("verdict") != "PROVED" or re.search(rf"\b{bid}\b", blob):
            continue
        if dd.get("instrument"):
            inst += 1
        else:
            sub += 1
    assert inst > 20, "instrument arcs should be a real fraction of the raw count"
    assert sub > 200, f"substantive debt collapsed to {sub}"
    assert sub + inst > 250
    # the ledger must carry the split, not the raw number alone
    t = _read("docs/consolidation/DEBT_LEDGER.md")
    assert "SUBSTANTIVE debt candidates" in t
    assert "an INSTRUMENT arc is not consolidation debt" in t
