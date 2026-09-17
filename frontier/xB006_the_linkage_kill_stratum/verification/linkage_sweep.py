#!/usr/bin/env python3
"""xB006 cells S1-S2 - the LINKAGE-KILL sweep, exactly as sealed in PREREGISTRATION.md
(sha256 94b1f14c..., commit 504d6bd, pushed BEFORE this file existed).

Hunts the E82 stratum: kills whose force rests on 'these things are the same / forced /
not independent', where the link is NOT exhibited.  B742's sweep cannot see these -- an
E82 kill IS earned by computation and its computation is CORRECT.

Each cell asserts its own mathematics.  Gate 5 untouched.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]

# --- the linkage lexicon -------------------------------------------------------------------
# NARROW by construction (the B806 lexicon-blindness lesson, and xB001's own measurement that a
# bare emphatic "IS the" gives 272 candidates, overwhelmingly false).  Each alternative is a
# construct that does EVIDENTIAL work in a kill: it says the recurrence carries no information.
LINKAGE = re.compile(
    r"\bforced,?\s+not\s+evidence\b"
    r"|\bgeneric,?\s+not\s+evidence\b"
    r"|\bnot\s+evidence\b"
    r"|\bis\s+not\s+a\s+coincidence\b"
    r"|\bthe\s+same\s+fact\b"
    r"|\bone\s+fact\b"
    r"|\bcanonically\s+linked\b"
    r"|\bnot\s+independent\b"
    r"|\bcarries\s+no\s+(?:new\s+)?information\b"
    r"|\bno\s+new\s+information\b"
    r"|\bevidentially\s+empty\b"
    r"|\balready\s+implied\b"
    r"|\bwearing\s+\w+\s+hats\b"
    r"|\bis\s+automatic\b|\bare\s+automatic\b",
    re.I,
)
# WITHDRAWN before any count was reported: a first draft of this lexicon also carried
# "by construction".  It is NOT in the sealed list, it was added while coding, and it drove
# 27 of an initial 46 candidates on its own -- it is descriptive prose ("golden BY
# CONSTRUCTION", B425), not an evidential-linkage construct that does work in a kill.
# Removing it restores the lexicon the PREREGISTRATION actually sealed.
# --- an EXHIBITED link: a map, or a named theorem doing the work ---------------------------
MAP = re.compile(
    r"\bmap\b|\bmorphism\b|\bisomorphism\b|\bhomomorphism\b|\bembedding\b|\bsurjection\b"
    r"|\bfunctor\b|\bequivariant\b|\bexhibit\w*\b|\bacts?\s+(?:faithfully|transitively|on)\b"
    r"|\bconjugat\w+\b|\bcommutes?\s+with\b",
    re.I,
)
NAMED_THEOREM = re.compile(
    r"\bMcKay\b|\bMostow\b|\bThurston\b|\bADE\s+classification\b|\bclassification\s+theorem\b"
    r"|\bMilgram\b|\bNeumann[-–]Reid\b|\bPorti\b|\bFricke\b|\bMarkov\b|\bNielsen[-–]Thurston\b"
    r"|\bGauss[-–]Bonnet\b|\bPoincar\w*\s+duality\b|\bby\s+a\s+theorem\b|\bis\s+a\s+theorem\b"
    r"|\bWeil\b|\bMaclachlan[-–]Reid\b|\bRiemann[-–]Roch\b|\bSchur\b|\bBurnside\b"
    r"|\bSylow\b|\bGalois\s+theory\b|\bclass\s+field\b|\bMinkowski\b|\bDirichlet\b",
    re.I,
)
KILLWORD = re.compile(
    r"\bKILLED\b|\bREFUTED\b|\bNEGATIVE\b|\bdead\b|\bdoes\s+not\s+survive\b|\bfails\b"
    r"|\bclosed\b|\bno\s+evidence\b|\bcannot\b|\bis\s+not\b", re.I)


def arcs():
    for p in sorted(ROOT.glob("frontier/*/arc_verdict.json")):
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        f = p.parent / "FINDINGS.md"
        txt = f.read_text(encoding="utf-8", errors="replace") if f.exists() else ""
        yield p.parent.name, d, txt


def is_kill(d, txt):
    if d.get("verdict") == "NEGATIVE":
        return True
    return bool(KILLWORD.search(d.get("claim_one_line", "")[:400]))


def context(txt, m, w=600):
    return txt[max(0, m.start()-w): m.end()+w]


def classify(name, d, txt):
    """return (hits, klass, why) -- A link exhibited, B standard/citable, C no link."""
    blob = d.get("claim_one_line", "") + "\n" + txt
    hits = list(LINKAGE.finditer(blob))
    if not hits:
        return [], None, ""
    windows = [context(blob, m) for m in hits]
    joined = "\n".join(windows)
    if NAMED_THEOREM.search(joined):
        return hits, "A", "named theorem in the linkage window: " + \
            NAMED_THEOREM.search(joined).group(0)
    if MAP.search(joined):
        return hits, "B", "map-language in the linkage window: " + MAP.search(joined).group(0)
    return hits, "C", "no map and no named theorem within 600 chars of the linkage claim"


# ---------------------------------------------------------------------------------------
def S1():
    print("S1       building the sweep and CALIBRATING it before any count is reported")
    # planted control 1 -- a synthetic E82 kill.  MUST land in C.
    plant_bad = {"verdict": "NEGATIVE", "claim_one_line":
                 "the object's Z/5 and the lattice's Z/5 and the group's Z/5 are ALL canonically "
                 "linked, so the recurrence is not evidence: one fact wearing three hats."}
    h, k, why = classify("PLANT_BAD", plant_bad, "")
    print(f"         control 1 (planted E82 kill, no map, no theorem) -> class {k}")
    assert h and k == "C", (k, why)
    # planted control 2 -- the SOUND form.  MUST NOT land in C.
    plant_ok = {"verdict": "NEGATIVE", "claim_one_line":
                "the three E6 faces are forced, not evidence: one ADE classification theorem "
                "produces all three, so the recurrence is generic."}
    h2, k2, why2 = classify("PLANT_OK", plant_ok, "")
    print(f"         control 2 (sound form, a named classification theorem) -> class {k2}")
    assert h2 and k2 == "A", (k2, why2)
    # the REAL two-way control the seal names: B727 itself must not be a candidate.
    b727 = None
    for name, d, txt in arcs():
        if name.startswith("B727"):
            b727 = (name, d, txt)
    assert b727, "B727 not found -- the calibration control is missing"
    h3, k3, why3 = classify(*b727)
    print(f"         control 3 (B727, the record's own sound form) -> class {k3}  [{why3[:60]}]")
    assert h3, "B727 does not even trip the lexicon -- the lexicon is too narrow"
    assert k3 != "C", f"B727 classed as an E82 candidate: THE INSTRUMENT IS MISCALIBRATED ({why3})"
    print("S1 PASS  the lexicon fires on a planted E82 kill, and does NOT class the record's own")
    print("         sound form (B727) as a candidate. The instrument is calibrated both ways.")


def S2():
    total = kills = tripped = 0
    buckets = {"A": [], "B": [], "C": []}
    for name, d, txt in arcs():
        total += 1
        if not is_kill(d, txt):
            continue
        kills += 1
        hits, k, why = classify(name, d, txt)
        if not hits:
            continue
        tripped += 1
        buckets[k].append((name, d.get("verdict"), why, len(hits)))
    print(f"\nS2       corpus at this head: {total} arcs, {kills} read as kills")
    print(f"         linkage lexicon trips on {tripped} of them")
    for k in "ABC":
        print(f"           class {k}: {len(buckets[k]):>4}", end="")
        print({"A": "  link exhibited (named theorem)",
               "B": "  map-language present (standard/citable)",
               "C": "  NO LINK EXHIBITED -- E82 candidates"}[k])
    print(f"\n         the E82 candidates ({len(buckets['C'])}):")
    for name, v, why, n in buckets["C"]:
        print(f"           {v:<9} {name}   ({n} linkage hit{'s' if n > 1 else ''})")
    if not buckets["C"]:
        print("\nS2 -> OUTCOME B: |C| = 0. E82 IS NOT A CLASS IN THIS CORPUS.")
    else:
        print(f"\nS2 -> OUTCOME A: |C| = {len(buckets['C'])}. E82 is a class; candidates named above.")
    return buckets


if __name__ == "__main__":
    S1()
    b = S2()
    print("\nVERIFIED")
