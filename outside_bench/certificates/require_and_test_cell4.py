#!/usr/bin/env python3
"""CELL 4 -- the remaining section-A rows, and whether the value walls name the object.

Seal: outside_bench/seals/REQUIRE_AND_TEST_CELL4_PREREG.md
      sha256 f846c6e7a68dad615136629ac3b66bebe8a04661dc589e319b84eb39d4e83338

Rows 3-8 are mostly ASSEMBLY, not sweeps.  So the instrument is not a rate but
CITATION VERIFICATION: every quoted line is asserted present verbatim in the
file it is attributed to.  ERROR_LEDGER's E2 names "a reference table
transcribed wrong at sealing" as a defect class, and an assembly cell is
exactly where it lives.

THE ONE COMPUTABLE QUESTION (row 3): do the three theorems WHAT_WOULD_COUNT 4A
rests on mention the object at all?  Only each theorem's OWN STATEMENT is
consulted -- the arc_verdict claim line, or the LAW_MAP paragraph for B666.

Stdlib only.
"""
from __future__ import annotations

import json
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

OBJECT_TOKENS = ["m004", "figure-eight", "figure eight", "4_1", "4₁"]


def rule(t):
    print("\n" + "-" * 78)
    print(" " + t)
    print("-" * 78)


def norm(s):
    """NFC-normalise and collapse whitespace: the corpus stores some accents
    DECOMPOSED, and a quotation that differs only by that is still the line."""
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", s)).strip()


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return norm(fh.read())


# (label, file, the quoted string that must be present verbatim)
QUOTES = [
    ("A3 values", "docs/TOE_REQUIREMENTS_LEDGER.md",
     "19+ dimensionless parameters (couplings, masses, mixings, θ)"),
    ("A3 grade", "docs/TOE_REQUIREMENTS_LEDGER.md",
     "the values enter through measurements, not the object"),
    ("A4 dynamics", "docs/TOE_REQUIREMENTS_LEDGER.md",
     "an action (kinetic terms, interactions, a vacuum), a 4d Lorentzian limit"),
    ("A4 grade", "docs/TOE_REQUIREMENTS_LEDGER.md", "main has no derived action"),
    ("A5 gravity", "docs/TOE_REQUIREMENTS_LEDGER.md",
     "a propagating massless spin-2 with universal coupling"),
    ("A5 grade", "docs/TOE_REQUIREMENTS_LEDGER.md", "containment, not a theory"),
    ("A6 quantum", "docs/TOE_REQUIREMENTS_LEDGER.md",
     "anomaly cancellation, unitarity, UV behaviour"),
    ("A7 predictions", "docs/TOE_REQUIREMENTS_LEDGER.md",
     "at least one number or regime not used as input"),
    ("A8 endpoint", "docs/TOE_REQUIREMENTS_LEDGER.md",
     "a ToE claim must name its chain end"),
    ("V-3 wall", "docs/TOE_REQUIREMENTS_LEDGER.md",
     "no object period is an SM ratio"),
    ("E row 4 (I-26)", "docs/TOE_REQUIREMENTS_LEDGER.md",
     "the dimension gap not exhibited"),
    ("4A is E2/MB12, not disappointment", "docs/WHAT_WOULD_COUNT.md",
     "The re-scope is licensed by discipline, not by disappointment"),
    ("E2's own wording", "docs/WHAT_WOULD_COUNT.md",
     "cannot pass for any genuine object"),
    ("the coupling leg is NOT a theorem", "docs/WHAT_WOULD_COUNT.md",
     "This leg is empirical exhaustion, not theorem"),
    ("B666 scale-torsor no-go", "docs/LAW_MAP.md",
     "Hom(G, ℝ₊) = 0 for all"),
    ("B666's six verification groups", "docs/LAW_MAP.md",
     "Gal(L/ℚ(i)), 2I, PSL(2,7), 2I×ℤ/3, SL(2,ℤ/15), W(E6)"),
    ("falsifier 1 still open", "docs/WHAT_WOULD_COUNT.md",
     "not a proven impossibility"),
]

# (label, how to get the theorem's OWN statement)
THEOREMS = [
    ("B666 cell S -- the scale-torsor no-go", "docs/LAW_MAP.md", "paragraph"),
    ("B936 -- the value-invisibility theorem", "frontier/B936_cohomology_reading/arc_verdict.json", "claim"),
    ("B1096 -- the anomaly layer is identically zero", "frontier/B1096_anomaly_layer/arc_verdict.json", "claim"),
]


def claim_line(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        d = json.load(fh)
    for k in ("claim_one_line", "claim", "headline"):
        if d.get(k):
            return norm(d[k])
    raise RuntimeError(f"no claim line in {rel}")


def b666_paragraph():
    txt = read("docs/LAW_MAP.md")
    i = txt.find("UPGRADED TO A STANDALONE")
    j = txt.find("firewalled.", i)
    if i < 0 or j < 0:
        raise RuntimeError("B666 paragraph not located in LAW_MAP.md")
    return txt[i:j + len("firewalled.")]


def object_tokens_in(text):
    low = text.lower()
    return [t for t in OBJECT_TOKENS if t.lower() in low]


def main() -> int:
    print("=" * 78)
    print(" CELL 4 -- THE REMAINING ROWS, AND WHETHER THE VALUE WALLS NAME THE OBJECT")
    print("=" * 78)
    print("""
    seal  outside_bench/seals/REQUIRE_AND_TEST_CELL4_PREREG.md
    sha256 f846c6e7a68dad615136629ac3b66bebe8a04661dc589e319b84eb39d4e83338""")
    failures = []

    # ------------------------------------------------------------------ M1/M3
    rule("CONTROL M1 / M3 -- every quotation asserted present in its named file")
    cache = {}
    missing = []
    for label, rel, q in QUOTES:
        if rel not in cache:
            cache[rel] = read(rel)
        present = norm(q) in cache[rel]
        print(f"    [{'ok ' if present else 'MISS'}] {label:38s} {rel}")
        if not present:
            missing.append((label, rel, q))
    print(f"\n    quotations checked: {len(QUOTES)}   missing: {len(missing)}")
    assert len(QUOTES) > 0, "no quotations -- the B1197 vacuity trap"
    if missing:
        for label, rel, q in missing:
            print(f"      MISSING in {rel}: {q!r}")
        failures.append("M1")
    print(f"    -> {'PASS' if not missing else 'FAIL'}")

    # ------------------------------------------------------------------ M2
    rule("CONTROL M2 -- the object-token search must be shown to WORK")
    print("""
    M2 AS FIRST SEALED USED ONE PROBE, B1321's claim line -- which does NOT
    name the object: B1321 is about the SIBLING (m202, s959).  The run
    correctly FAILED.  The search was not broken; the probe was.  Corrected by
    seal ADDENDUM 1 to three probes that exercise three distinct spellings,
    because ERROR_LEDGER E54 records a search that missed its target "because
    the search lacked the DIGIT spelling".
""")
    probes = [
        ("frontier/B803_commensurability_audit/arc_verdict.json", "m004"),
        ("frontier/B282_e6_is_arithmetic_not_geometric/arc_verdict.json", "4\u2081 (digit subscript)"),
        ("frontier/B1163_w0_attempt/arc_verdict.json", "m004 and 4_1"),
    ]
    spellings = set()
    ok_m2 = True
    for rel, expect in probes:
        txt = claim_line(rel)
        found = object_tokens_in(txt)
        spellings.update(found)
        print(f"    {rel.split('/')[1]:46s} carries {expect:24s} -> found {found}")
        if not found:
            ok_m2 = False
    print(f"\n    distinct spellings exercised: {len(spellings)}  {sorted(spellings)}")
    if len(spellings) < 3:
        ok_m2 = False
    print(f"    -> {'PASS' if ok_m2 else 'FAIL'} (all three probes must hit; >= 3 spellings exercised)")
    if not ok_m2:
        failures.append("M2")

    # ------------------------------------------------------------------ the question
    rule("ROW 3 -- do the three theorems 4A rests on MENTION THE OBJECT?")
    print("""
    Only each theorem's OWN STATEMENT is consulted: the arc_verdict claim line,
    or the LAW_MAP paragraph for B666.  Not the arc directory, not its code.
""")
    any_named = False
    for label, rel, kind in THEOREMS:
        text = b666_paragraph() if kind == "paragraph" else claim_line(rel)
        toks = object_tokens_in(text)
        any_named = any_named or bool(toks)
        print(f"    {label}")
        print(f"      source     : {rel}  ({len(text)} chars)")
        print(f"      object tokens: {toks if toks else 'NONE'}")
        print(f"      opens       : {text[:150]}...")
        print()
    outcome = "II" if any_named else "I"
    print(f"    -> OUTCOME {outcome}")
    if outcome == "I":
        print("""    OBJECT-FREE.  All three statements are about finite/profinite groups,
    about E6's structure, and about the SM's own 16.  So the value criterion
    cannot pass for ANY object through these routes: row 3's base rate is 0
    for every object, and that is a fact about the REQUIREMENT, not m004.

    THE CORRECTION THIS FORCES, preregistered before the run:
      R144-4 wrote that when falsifier 2 fired the programme took reading (a)
      "values are the wrong success criterion" and never (b) "the object is
      the wrong object".  FOR ROW 3 THAT IS TOO STRONG: reading (a) is here a
      theorem, not a re-framing.  WHAT_WOULD_COUNT 4A says so in its own
      words -- "The re-scope is licensed by discipline, not by disappointment"
      -- and this cell confirms the three theorems it leans on name no object.
      R144's diagnosis stands for the programme; it does not stand for row 3.""")
    else:
        print("""    OBJECT-BOUND.  At least one wall is m004's, and re-scoping the
    criterion absorbed evidence that should have been read as about the object.""")

    # ------------------------------------------------------------------ the table
    rule("THE REMAINING ROWS -- verdicts, with what would make each computable")
    rows = [
        ("3 values", "P writable; T = LACKS (V-3)",
         f"B = 0 FOR EVERY OBJECT by the three theorems (OUTCOME {outcome})"),
        ("4 dynamics", "NOT-COMPUTABLE",
         "computable when an action is DERIVED; section E row 1 lists six declared inputs"),
        ("5 gravity", "NOT-COMPUTABLE",
         "'containment, not a theory': a spin-2 slot, no propagator, no coupling"),
        ("6 quantum consistency", "DOWNSTREAM, not independent",
         "anomaly-freedom is a property of a CLOSING; it cannot discriminate objects "
         "until a closing is derived rather than chosen"),
        ("7 predictions", "P writable; T = a REGIME, not a value",
         "P9 is conditional and sealed; computable when a number not used as input exists"),
        ("8 say which endpoint", "NOT A CELL",
         "the only section-A row whose status column is the ledger itself: a discipline "
         "rule on claims, not an object property"),
    ]
    for r, v, note in rows:
        print(f"    {r:24s} {v}")
        print(f"      {note}")

    rule("VERDICT")
    print(f"    ROW 3 = OUTCOME {outcome}    quotations verified {len(QUOTES) - len(missing)}/{len(QUOTES)}")
    print(f"    controls: {'ALL PASSED' if not failures else 'FAILED: ' + ', '.join(failures)}")
    print("""
    NOT CONCLUDED: that row 3's walls are the only walls, or that no route to
    values exists.  4A's own fence is kept: the coupling-channel leg is
    "empirical exhaustion, not theorem".  No value.""")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
