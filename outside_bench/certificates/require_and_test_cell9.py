#!/usr/bin/env python3
"""CELL 9 -- row 4 is not closed, and the closure is stale by one day.

Seal: outside_bench/seals/REQUIRE_AND_TEST_CELL9_PREREG.md
      sha256 13619e617eaacff03688114072d1a7ba3559574245cfbe646a98e9cc3ade14ef

Phase 1's cell 4 showed WHAT_WOULD_COUNT 4A's three walls name no object.  It
never asked whether they are as GENERAL as they look.  Rule #26: quote
hypotheses from a STATEMENT of the theorem, not from a sentence about it.

Every quoted line is asserted present verbatim in the file it is attributed to
(ERROR_LEDGER E2's defect class).  Control R2 fixes cell 4's M2 failure: the
citation search is first shown able to find a term 4A demonstrably contains.

Stdlib only.
"""
from __future__ import annotations

import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def rule(t):
    print("\n" + "-" * 78)
    print(" " + t)
    print("-" * 78)


def norm(s):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", s)).strip()


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return norm(fh.read())


def raw(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


PN = "frontier/B666_leads_campaign/cellS/PROOF_NOTE.md"
CSO = "frontier/B666_leads_campaign/cellS/cellS_output.txt"
B1116 = "frontier/B1116_asymptotic_channel/FINDINGS.md"
WWC = "docs/WHAT_WOULD_COUNT.md"
GCL = "docs/GRAND_COMPUTATION_LEDGER.md"
VERDICT = "docs/THE_SM_VERDICT.md"

# (label, file, the line that must be present verbatim)
QUOTES = [
    ("T1 Definition 1 (the clause itself)", PN,
     "A *framework output* is an element of a fixed number field F, carried by a representation of"),
    ("T1 the arc's own Scope admission", PN,
     "the one assembly ingredient this note consumes rather than reproves"),
    ("T1 the named falsifier, never taken up", PN,
     "exhibit a banked output NOT stabilized by a finite/profinite structure"),
    ("T1 the w = 0 exemption", PN,
     "weight w = 0 is outside its hypothesis"),
    ("T2 what was verified exactly", CSO,
     "THE RIGIDITY STEP IS VERIFIED EXACTLY ON ALL BANKED STRUCTURES"),
    ("T3 B1116's quantifier finding", B1116,
     "Every banked value/scale no-go quantifies over SINGLE-LEVEL invariants"),
    ("T3 B1116's verdict", B1116,
     "the archimedean/growth-rate channel is not excluded by any banked no-go"),
    ("T3 the caveat must travel", GCL,
     "must ride with the headline"),
    ("fence: values still not produced", VERDICT,
     "no SM number is produced"),
    ("fence: 4A's own non-theorem leg", WWC,
     "This leg is empirical exhaustion, not theorem"),
    ("4A is not disappointment", WWC,
     "The re-scope is licensed by discipline, not by disappointment"),
    ("T5 B1116's banked date", "docs/CAMPAIGN_STATUS.md",
     "THE BREAKTHROUGH PACKET pt.1 (2026-08-21)"),
    ("T5 that packet names B1116", "docs/CAMPAIGN_STATUS.md",
     "B1116 asymptotic channel (value door not-excluded"),
]


ADDENDUM_MARK = "### ADDENDUM 2026-09-14 — \u00a74A's no-goes are SINGLE-LEVEL"


def section_4A(text, exclude_own_addendum=True):
    """The 4A section of WHAT_WOULD_COUNT, from its heading to section 5.

    REPRODUCIBILITY: cell 10 later APPENDS this bench's own addendum inside
    section 4A, and that addendum names B1116.  A re-run would then find the
    citation it is testing for -- the certificate measuring its own edit, which
    silently flipped this cell's outcome on the first re-run.  So the section
    is cut at the addendum marker, and BOTH states are reported.
    """
    i = text.find("## 4A.")
    j = text.find("## 5.", i if i >= 0 else 0)
    if i < 0:
        return None
    sec = text[i:j if j > i else len(text)]
    if exclude_own_addendum:
        k = sec.find(ADDENDUM_MARK)
        if k >= 0:
            sec = sec[:k]
    return sec


def main() -> int:
    print("=" * 78)
    print(" CELL 9 -- IS ROW 4 AS CLOSED AS THE TABLE SAYS?")
    print("=" * 78)
    print("""
    seal  outside_bench/seals/REQUIRE_AND_TEST_CELL9_PREREG.md
    sha256 13619e617eaacff03688114072d1a7ba3559574245cfbe646a98e9cc3ade14ef""")
    failures = []

    # ------------------------------------------------------------------ R1
    rule("CONTROL R1 -- every quotation asserted present in its named file")
    cache = {}
    missing = []
    for label, rel, q in QUOTES:
        if rel not in cache:
            cache[rel] = read(rel)
        ok = norm(q) in cache[rel]
        print(f"    [{'ok ' if ok else 'MISS'}] {label:42s} {rel}")
        # ECHO the verified string, so this output file is a STANDALONE record
        # rather than a list of labels (caught by cell 10's control S2).
        print(f"           \"{q}\"")
        if not ok:
            missing.append((label, rel, q))
    print(f"\n    quotations checked: {len(QUOTES)}   missing: {len(missing)}")
    assert len(QUOTES) > 0, "no quotations -- the B1197 vacuity trap"
    for label, rel, q in missing:
        print(f"      MISSING in {rel}: {q!r}")
    if missing:
        failures.append("R1")
    print(f"    -> {'PASS' if not missing else 'FAIL'}")

    # ------------------------------------------------------------------ T1/T2
    rule("T1 / T2 -- B666's two halves, graded separately")
    print("""
    THE PROVED HALF.  Hom(G, R_+) = 0, elementary and exactly verified.
    cellS_output.txt closes:
      "THE RIGIDITY STEP IS VERIFIED EXACTLY ON ALL BANKED STRUCTURES"
    and that file is, line for line, a per-group computation of |G|, [G,G],
    G^ab, exp(G^ab) and the positive-real solutions of x^e = 1.  The
    STABILIZATION clause is nowhere computed in it.

    THE OTHER HALF.  "every output is stabilized by a finite/profinite
    structure" is PROOF_NOTE.md's Definition 1 -- a stipulation of what
    COUNTS as a framework output -- and the arc's own Scope says the factual
    premise behind it is imported:
      "the one assembly ingredient this note consumes rather than reproves"
""")
    t1 = "DECLARED (Definition 1) + ASSUMED (imported premise)"
    t2 = "the Hom vanishing ONLY"
    print(f"    T1 verdict: {t1}")
    print(f"    T2 verdict: {t2}")
    print("""
    And the arc names its own falsifier:
      "exhibit a banked output NOT stabilized by a finite/profinite structure"
    No arc in the corpus has taken it up.""")

    # ------------------------------------------------------------------ R2
    rule("CONTROL R2 -- the citation search must be shown able to FIND something")
    print("""
    Cell 4's M2 failed because a single probe could not pass.  Before
    concluding that 4A does NOT cite B1116, the same search is run for terms
    4A demonstrably DOES contain.""")
    wwc_raw = raw(WWC)
    sec = section_4A(wwc_raw)
    if sec is None:
        print("    FATAL: section 4A not located")
        failures.append("R2-locate")
        sec = ""
    sec_full = section_4A(wwc_raw, exclude_own_addendum=False) or ""
    own = len(sec_full) - len(sec)
    print(f"    section 4A located: {len(sec)} chars"
          + (f"   (excluding this bench's own {own}-char addendum, appended by cell 10)"
             if own > 0 else "   (this bench has appended nothing to it yet)"))
    positives = ["B1096", "B936", "B666"]
    found_pos = {t: (t in sec) for t in positives}
    for t, v in found_pos.items():
        print(f"      probe {t:8s} present in 4A: {v}")
    ok_r2 = all(found_pos.values()) and len(sec) > 0
    print(f"    -> {'PASS' if ok_r2 else 'FAIL'} (all positive probes must hit)")
    if not ok_r2:
        failures.append("R2")

    # ------------------------------------------------------------------ T4
    rule("T4 -- does section 4A cite B1116 or its channel?")
    targets = ["B1116", "asymptotic", "growth rate", "growth-rate", "T-ASYMPTOTIC"]
    hits = {t: (t.lower() in sec.lower()) for t in targets}
    for t, v in hits.items():
        print(f"    {t:14s} in 4A: {v}")
    cites = any(hits.values())
    print(f"    -> 4A AS THE RECORD CARRIED IT {'CITES' if cites else 'DOES NOT CITE'} "
          f"B1116 or its channel")
    if own > 0:
        hits_after = {t: (t.lower() in sec_full.lower()) for t in targets}
        print(f"    after this bench's cell-10 addendum: "
              f"{'CITES' if any(hits_after.values()) else 'still does not cite'} "
              f"-- by our own insertion, which is the point of the addendum, "
              f"and is excluded from the measurement above")

    # ------------------------------------------------------------------ T5
    rule("T5 -- the dates")
    m = re.search(r"## 4A\..*?\(owner-directed (\d{4}-\d{2}-\d{2})\)", sec, re.S)
    d4a = m.group(1) if m else "not stated in the heading"
    print("""
    B1116's own FINDINGS header carries NO date, and this branch's git dates
    are unusable (the history is squashed: B1116 and 4A both show 2026-08-25).
    So the date is taken from the corpus's own dated packet line, asserted
    verbatim above:
      CAMPAIGN_STATUS.md:2815  "THE BREAKTHROUGH PACKET pt.1 (2026-08-21). ...
      B1116 asymptotic channel (value door not-excluded ...)"
""")
    db = "2026-08-21"
    print(f"    section 4A : {d4a}   (stated in its own heading)")
    print(f"    B1116      : {db}   (CAMPAIGN_STATUS.md:2815, asserted above)")
    try:
        later = (tuple(map(int, db.split("-"))) > tuple(map(int, d4a.split("-"))))
        print(f"    B1116 is {'ONE DAY LATER than' if later else 'NOT later than'} 4A")
    except Exception:
        later = None
        print("    ordering: NOT ESTABLISHED from the record")
    print("""
    The ordering does NOT carry the outcome, and is reported for the record
    only: if B1116 were EARLIER, 4A's failure to cite it would be worse, not
    better.  The outcome rests on T1, T3 and T4 alone.""")

    # ------------------------------------------------------------------ outcome
    rule("THE PREREGISTERED OUTCOME")
    declared = t1.startswith("DECLARED")
    scopes = ("Every banked value/scale no-go quantifies over SINGLE-LEVEL invariants"
              in cache.get(B1116, read(B1116)))
    outcome = "A" if (declared and scopes and not cites) else "B"
    print(f"    Definition 1 DECLARED/ASSUMED : {declared}")
    print(f"    B1116 scopes the no-goes      : {scopes}")
    print(f"    4A cites B1116                : {cites}")
    print(f"\n    -> OUTCOME {outcome}")
    if outcome == "A":
        print("""    ROW 4 MUST BE RESTATED.

      WAS: values -- LACKS; base rate 0 FOR EVERY OBJECT.
      IS : values -- LACKS; 0 for every object THROUGH THE ROUTES 4A NAMES,
           and those routes are SINGLE-LEVEL invariants.  The tower
           growth-rate channel is reached by NO banked no-go (B1116), and 4A
           predates that audit by one day and does not cite it.

      So row 4 is CLOSED AT SINGLE LEVEL, OPEN AT THE ARCHIMEDEAN ONE.""")
    else:
        print("    ROW 4 STANDS AS WRITTEN.")

    rule("WHAT THIS DOES NOT SAY")
    print("""    Values are NOT derivable on the strength of this cell.  B1116 opens a
    CHANNEL, not a number, and THE_SM_VERDICT's own words ride along:
      "VALUE-matching remains OPEN -- no SM number is produced."
    4A's coupling leg is exactly what 4A calls it -- "This leg is empirical
    exhaustion, not theorem" -- now at eight misses, the last B1128
    INSTRUMENT-NULL.  And B666 is not wrong: its Hom-vanishing half is proved
    and exactly verified on six groups.  Gate 5 untouched.  No value.""")

    rule("VERDICT")
    print(f"    OUTCOME {outcome}   quotations verified {len(QUOTES) - len(missing)}/{len(QUOTES)}")
    print(f"    controls: {'ALL PASSED' if not failures else 'FAILED: ' + ', '.join(failures)}")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
