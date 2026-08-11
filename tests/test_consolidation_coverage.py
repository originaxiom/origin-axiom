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
    """Both citation forms. CLAIMS.md cites its evidence by PATH (`frontier/B239_...`), where the
    trailing `_` defeats a `\bB239\b` boundary — so a bare-id test misses PROMOTION TO A CLAIM,
    the most important form of consolidation there is. It marked 49 arcs absent that are cited."""
    blob = "\n".join(_read(p) for p in files)
    return [(b, v) for b, v in arcs
            if not (re.search(rf"\b{b}\b", blob) or re.search(rf"{b}_", blob))]


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


def test_path_form_citations_are_counted__the_v3_correction(arcs):
    """49 arcs were marked absent by a bare-id regex while CLAIMS.md cites them by path."""
    blob = "\n".join(_read(p) for p in CURATED)
    bare_only = [b for b, _ in arcs
                 if not re.search(rf"\b{b}\b", blob) and re.search(rf"{b}_", blob)]
    assert len(bare_only) > 30, "the path form should catch a substantial set"
    # Representative victims: promoted claims whose ONLY citation is the path in CLAIMS.md.
    for b in ("B239", "B264", "B354"):
        assert b in bare_only, f"{b} should be path-cited only"
    # B575 is NOT one of them -- it appears both ways ("B575's exact computation" and the path).
    # Recorded because the v3 retraction first blamed the regex for B575; the real cause was that
    # a band note's correct scope ("absent from LAW_MAP/FRAMEWORK/CHAIN") was widened to "no
    # surface" when it was carried into the ledger, without re-checking against CLAIMS.
    assert re.search(r"B575_", blob) and re.search(r"\bB575\b", blob)


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
    assert "THIS FILE HAS BEEN CORRECTED TWICE" in t
    assert "absent-from-everything is 0" in t.lower()
    assert "Correction 2 — the regex" in t
    # the withdrawn B575 sub-claim must be recorded as withdrawn, not repeated as a finding
    assert "B575 IS cited" in t


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
        if dd.get("verdict") != "PROVED":
            continue
        if re.search(rf"\b{bid}\b", blob) or re.search(rf"{bid}_", blob):
            continue
        if dd.get("instrument"):
            inst += 1
        else:
            sub += 1
    assert inst > 20, "instrument arcs should be a real fraction of the raw count"
    assert 200 < sub < 280, f"substantive debt {sub} outside the v3 band"
    assert sub + inst > 240
    # the ledger must carry the split, not the raw number alone
    t = _read("docs/consolidation/DEBT_LEDGER.md")
    assert "SUBSTANTIVE debt candidates" in t
    assert "not debt by design" in t


# ---------------------------------------------------------------------------------------------
# B1033 — the reconciliation with the repository's OTHER, GATED debt register.
# This file measured a debt for three versions without ever naming `docs/REPRESENTATION_TRIAGE.md`,
# which is swept by `scripts/checks/representation_sweep.py` and enforced by a FAILING gate.
# These locks hold the cross-reference in place and pin the measured scope limit of that gate.
# ---------------------------------------------------------------------------------------------
import importlib.util as _ilu

_B1033 = _ilu.spec_from_file_location(
    "b1033", os.path.join(_ROOT, "frontier", "B1033_register_reconciliation", "verify.py"))
_b1033 = _ilu.module_from_spec(_B1033)
_B1033.loader.exec_module(_b1033)


def test_b1033_every_reconciliation_check_passes():
    failed = [k for k, c in _b1033.R["checks"].items() if not c["pass"]]
    assert failed == [], failed


def test_the_ledger_names_the_other_register_the_sweeper_and_the_gate():
    """The omission this file existed with for three versions."""
    t = _read("docs/consolidation/DEBT_LEDGER.md")
    for token in ("REPRESENTATION_TRIAGE", "representation_sweep", "representation-sweep"):
        assert token in t, token


def test_the_two_registers_are_measured_separately_and_overlap_little():
    n = _b1033.R["numbers"]
    assert n["ledger_rule"] > 150 and n["triage_rule_live"] < 30
    assert n["overlap"] < 10


def test_the_gates_substantiality_bar_cannot_see_the_early_corpus():
    """THE FINDING, pinned. Zero of the 731 pre-B800 arcs can clear `claim_one_line >= 500`,
    because that field changed from a one-line summary to an abstract around B800. If this ever
    stops holding, the sweeper's reach has genuinely changed and L158 should be revisited."""
    n = _b1033.R["numbers"]
    assert n["pre_B800_clearing_the_bar"] == 0
    assert n["pre_B800_arcs"] > 700
    med = n["median_claim_len_by_band"]
    assert max(med[f"B{lo}"] for lo in range(0, 800, 100)) < 200
    assert min(med[f"B{lo}"] for lo in (800, 900, 1000)) > 600


def test_the_rejected_repair_is_recorded_as_rejected_not_adopted():
    """MB12 discipline applied to a proposal: the band-relative threshold was tested BEFORE being
    offered and recovers 1 of 12 of the register's own calibration block."""
    assert _b1033.R["checks"]["the_obvious_band_relative_fix_FAILS_its_own_calibration"]["pass"]
    assert "1 of 12" in _read("docs/OPEN_LEADS.md")
    assert "L158" in _read("docs/REPRESENTATION_TRIAGE.md")


def test_the_ledger_refuses_to_stratify_by_a_bar_it_just_measured_as_era_bound():
    t = re.sub(r"\s+", " ", _read("docs/consolidation/DEBT_LEDGER.md"))
    assert "That is refused." in t
    assert "discard the entire pre-B800 corpus" in t
