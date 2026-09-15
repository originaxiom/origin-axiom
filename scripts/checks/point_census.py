#!/usr/bin/env python3
"""point-census — the POINT ledger: where does the object supply a distinguished ELEMENT?

WHY THIS EXISTS (B1410; prereg sealed 9ac73d7a, pushed at 5dde7b3e before any sweep ran)
-----------------------------------------------------------------------------------------
H5 (`docs/OPEN_ITEMS_2026-09-05.md:135-145`) asks for a POINT:

    "find one banked case where the object supplies an other-referential point with no
     external input."

C16, B750, B1264, B1274 and B1409 are all censuses of REFUSALS. They measure the pattern's
REACH and cannot contain the falsifier, which lives in the complement -- the corpus's banked
POSITIVE points. That ledger did not exist. This builds it.

WHAT THIS INSTRUMENT IS, AND IS NOT
-----------------------------------
It EMITS CANDIDATES. It does not adjudicate. A keyword sweep over this corpus over-predicts
(the `sense_census.py` lesson), so the rows of `docs/POINT_LEDGER.json` are adjudicated by a
seat, each citing its evidence, exactly as `derive_lexicon.py` declares for its own output.
What IS mechanical is the DECISION RULE (`--classify`): once a row's fields are filled, the
verdict is computed, never judged.

THE SEALED DECISION RULE (prereg section 4; the axis is section 2)
------------------------------------------------------------------
"other-referential" is typed on the TARGET, not on the derivation. Typing it on the derivation
makes H5 analytic by construction: with no external input the only available referent is the
object, hence self-referential, hence permitted, hence the falsifier cannot fire.

    OTHER      target not object-generated AND identifications_used == [] AND anchors == 0
    SELF       target object-generated     AND object_unique is True
    GENERIC    target object-generated     AND object_unique is False
    UNDECIDED  otherwise -- naming the clause that failed

GENERIC is what stops the exception clause absorbing everything: H5 says THE OBJECT supplies
points about ITSELF; a point any comparable object also supplies is about the TYPE. The corpus
already refused a claim on exactly this ground -- I-17 REFUTED, "the recurrence is FORCED, not
evidence ... only the atom Q(sqrt-3) is object-specific" (B727).

THE CALIBRATION SETS ARE SEALED, AND THIS FILE MAY NOT DRIFT FROM THE SEAL
--------------------------------------------------------------------------
MUST_RECOVER / MUST_REJECT below are copied from the sealed preregistration. They are not a
recollection: `--calibrate` re-reads the sealed file and FAILS if any id here is absent from it.
That is the join rule this arc adopted -- a claim relating two artifacts (this list, that seal)
is checked over BOTH by one command, because the preceding window's every self-correction was a
join asserted rather than checked.
"""
from __future__ import annotations

import argparse
import glob
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
PREREG = ROOT / "frontier" / "B1410_the_point_ledger" / "PREREGISTRATION.md"
LEDGER = ROOT / "docs" / "POINT_LEDGER.json"
CLOSURE = ROOT / "docs" / "OBJECT_CLOSURE.json"

SETTLED = {"PROVED", "NEGATIVE", "RESOLVED", "RESOLVED-A", "THEOREM"}

# Sealed in PREREGISTRATION.md section 7. `--calibrate` proves these match the seal.
MUST_RECOVER = ["B287", "B1224", "B1345", "B1248", "B862"]
MUST_REJECT = ["B680", "B1406", "B1409"]

# The selection signature, built from the calibration arcs' OWN wording rather than invented:
#   B287  "is the unique torus-bundle closing among the ten exceptional fillings"
#   B862  "leaves Gamma in {1,Z2,Z3,Z6} ambiguous ... the chain FORCES"
# A selection needs BOTH a distinguished element AND a candidate set it is distinguished within.
DISTINGUISH = re.compile(
    r"\b(the uniq\w+|uniquely|exactly one|the only|forc\w+|select\w+|picks? out|"
    r"distinguish\w+|canonical\w*|singles? out|pins? down)\b", re.I)
CANDIDATE_SET = re.compile(
    r"\b(among (the )?\w+|out of (the )?\w+|of the (ten|nine|eight|seven|six|five|four|three|two|\d+)\b|"
    r"\{[^}]{2,60}\}|one of (the )?\w+|ambiguous|candidates?|menu|orbit|family|set of)\b", re.I)


def _arcs() -> dict[str, dict]:
    out = {}
    for f in sorted(glob.glob(str(ROOT / "frontier" / "*" / "arc_verdict.json"))):
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        i = str(d.get("id", "")).strip()
        if not i:
            continue
        d["_path"] = str(pathlib.Path(f).relative_to(ROOT))
        # arc ids are not unique (the grandfathered B58 collision); keep every file
        out.setdefault(i, []).append(d)
    return out


# B1410's own verdict quotes the selection vocabulary this matcher hunts, so it matches itself and
# the count drifts by one the moment the arc banks. Excluded on already_banked.py's own stated
# precedent, quoted from its scan(): "excluding it is honesty, not evasion" -- and because a
# measurement written back into the corpus it measures is E78, the self-including measurement,
# which this window minted.
SELF_ARC = "B1410"


def candidates(min_hits: int = 1) -> list[dict]:
    """POINT-SHAPED claims: a distinguished element AND a candidate set it sits in."""
    rows = []
    for i, ds in _arcs().items():
        if i == SELF_ARC:
            continue
        for d in ds:
            if str(d.get("verdict", "")).upper() not in SETTLED:
                continue
            text = str(d.get("claim_one_line", ""))
            a, b = DISTINGUISH.findall(text), CANDIDATE_SET.findall(text)
            if len(a) >= min_hits and len(b) >= min_hits:
                rows.append({"arc": i, "path": d["_path"],
                             "verdict": d["verdict"],
                             "distinguishers": sorted({x if isinstance(x, str) else x[0] for x in a})[:4],
                             "set_markers": sorted({(x[0] if isinstance(x, tuple) else x) for x in b})[:4],
                             "claim": text[:160]})
    return sorted(rows, key=lambda r: (-len(r["distinguishers"]) - len(r["set_markers"]), r["arc"]))


def classify(row: dict) -> tuple[str, str]:
    """The sealed rule. Computed, never judged."""
    t = row.get("target", {})
    dv = row.get("derivation", {})
    sp = row.get("specificity", {})
    gen = t.get("generated_by_object")
    ids = dv.get("identifications_used")
    a1, a2 = dv.get("anchors_T1"), dv.get("anchors_T2")
    uniq = sp.get("object_unique")

    if gen is None:
        return "UNDECIDED", "target.generated_by_object unset"
    if gen is False:
        if ids is None or a1 is None or a2 is None:
            return "UNDECIDED", "derivation fields unset on a non-object-generated target"
        if ids == [] and a1 == 0 and a2 == 0:
            return "OTHER", "non-object-generated target, no identification, no anchor"
        why = []
        if ids:
            why.append(f"identifications_used={ids}")
        if a1:
            why.append(f"anchors_T1={a1}")
        if a2:
            why.append(f"anchors_T2={a2}")
        return "UNDECIDED", "other-referential target but the derivation consumes " + ", ".join(why)
    if uniq is True:
        return "SELF", "object-generated target, object_unique measured true"
    if uniq is False:
        return "GENERIC", "object-generated target, but not object-specific (I-17's ground)"
    return "UNDECIDED", f"object_unique is {uniq!r} -- UNTESTED is not true (E67)"


def calibrate() -> int:
    """The join check: this file's sealed sets must appear in the sealed prereg."""
    if not PREREG.is_file():
        print("  point-census: SEALED PREREG MISSING -- calibration cannot be trusted")
        return 1
    seal = PREREG.read_text(encoding="utf-8")
    drift = [i for i in MUST_RECOVER + MUST_REJECT
             if not re.search(rf"`?{i}`?\b(?![0-9])", seal)]
    if drift:
        print(f"  point-census: CALIBRATION DRIFT -- {drift} not in the sealed prereg")
        return 1
    found = {r["arc"] for r in candidates()}
    rec = [i for i in MUST_RECOVER if i in found]
    wrong = [i for i in MUST_REJECT if i in found]
    print(f"  point-census: calibration against the seal ({PREREG.relative_to(ROOT)})")
    print(f"    recall on MUST_RECOVER : {len(rec)}/{len(MUST_RECOVER)}  {rec}")
    print(f"    MUST_REJECT flagged    : {len(wrong)}/{len(MUST_REJECT)} {wrong}  (lower is better)")
    print(f"    total candidates        : {len(found)}")
    return 0


def selftest() -> int:
    """MB12 both directions, on the RULE (the part that is mechanical)."""
    fails = []
    planted_other = {"target": {"generated_by_object": False},
                     "derivation": {"identifications_used": [], "anchors_T1": 0, "anchors_T2": 0},
                     "specificity": {"object_unique": "UNTESTED"}}
    v, _ = classify(planted_other)
    if v != "OTHER":
        fails.append(f"the can-fail witness does not classify OTHER (got {v}) -- H5 cannot lose")
    planted_self = {"target": {"generated_by_object": True},
                    "derivation": {"identifications_used": [], "anchors_T1": 0, "anchors_T2": 0},
                    "specificity": {"object_unique": True}}
    if classify(planted_self)[0] != "SELF":
        fails.append("an object-generated, object-unique row does not classify SELF")
    planted_generic = dict(planted_self, specificity={"object_unique": False})
    if classify(planted_generic)[0] != "GENERIC":
        fails.append("a non-object-specific row does not classify GENERIC -- the absorber is open")
    planted_untested = dict(planted_self, specificity={"object_unique": "UNTESTED"})
    if classify(planted_untested)[0] != "UNDECIDED":
        fails.append("UNTESTED is being read as true -- E67 violated")
    blocked = {"target": {"generated_by_object": False},
               "derivation": {"identifications_used": ["I-13"], "anchors_T1": 0, "anchors_T2": 0},
               "specificity": {}}
    if classify(blocked)[0] != "UNDECIDED":
        fails.append("a consumed identification does not block OTHER")
    # the matcher must separate the two sealed sets at all
    found = {r["arc"] for r in candidates()}
    if not (set(MUST_RECOVER) & found):
        fails.append("the matcher recovers NONE of the sealed MUST_RECOVER set")
    if set(MUST_REJECT) <= found:
        fails.append("the matcher flags EVERY sealed MUST_REJECT arc -- it measures the word")
    print("  point-census --selftest:", "PASS" if not fails else "FAIL")
    for f in fails:
        print("    " + f)
    return 1 if fails else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--calibrate", action="store_true")
    ap.add_argument("--candidates", action="store_true")
    ap.add_argument("--classify", action="store_true")
    ap.add_argument("--limit", type=int, default=40)
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.calibrate:
        return calibrate()
    if a.candidates:
        rows = candidates()
        print(f"  point-census: {len(rows)} POINT-SHAPED candidates (settled arcs only)")
        for r in rows[:a.limit]:
            print(f"    {r['arc']:<7} {r['verdict']:<9} {r['claim'][:104]}")
        return 0
    if a.classify:
        if not LEDGER.is_file():
            print(f"  point-census: {LEDGER.relative_to(ROOT)} does not exist yet")
            return 1
        led = json.load(open(LEDGER, encoding="utf-8"))
        counts = {}
        for row in led.get("rows", []):
            v, why = classify(row)
            counts[v] = counts.get(v, 0) + 1
            print(f"    {row.get('id','?'):<5} {row.get('arc','?'):<7} {v:<10} {why}")
        print(f"  point-census: {counts}")
        return 0
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
