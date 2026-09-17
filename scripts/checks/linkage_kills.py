#!/usr/bin/env python3
"""LINKAGE-KILL CHECKER (xB008) — the identification discipline, extended from promotions to
KILLS.

WHY THIS EXISTS. B1231's Identification Rule polices claims of the form "X here IS Y there".
It is gated (`gate_identification_register`) and ledgered (`docs/IDENTIFICATION_LEDGER.md`),
and BOTH act on PROMOTIONS ONLY: an arc declares `identifications` in its arc_verdict.json
when it CLAIMS a sameness, never when it USES one to DISCARD evidence.

xB005's Q3 asserted that four Z/3's were "all canonically linked" -- hence one fact, hence not
evidence -- on links that connected only three of them. Nothing in the repository caught it.
The kill was wrong in a way a promotion could not have been, because only promotions are
checked. The standing rule this instrument enforces:

    A KILL NEEDS THE SAME MAP A PROMOTION NEEDS.

WHAT IT CHECKS -- COMPLETENESS, NEVER JUDGMENT (B1231's own wording). It cannot tell whether a
link is true. It enforces that, where an arc discards evidence by asserting a sameness, the
link is named somewhere a reader can find it: a map, or a named theorem or definition.

A RATCHET, NOT A BLOCKER, for B1231's own stated reason -- a hard block on what is already
present would make the fastest path to green RELABELLING EXISTING KILLS AS SOUND, pressuring
exactly the judgment the gate protects. docs/LINKAGE_BASELINE.json freezes xB006's hand
adjudication of the corpus as it stood; a NEW linkage kill with no exhibited link reds the
suite AT CREATION, which is when xB005's Q3 would have been caught.

RECALL IS BOUNDED AND INHERITED (the B806 trade, measured in xB006): the lexicon is narrow on
purpose -- a wide net flags every sentence in this caps-heavy corpus and gets ignored. A kill
phrased without one of these constructs is invisible to this checker. It REDUCES the class; it
does not close it. Precision was measured, not assumed: 30 raw hits -> 3 after adjudication.

    python3 scripts/checks/linkage_kills.py             # report
    python3 scripts/checks/linkage_kills.py --selftest  # planted controls, both directions
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
BASELINE = ROOT / "docs" / "LINKAGE_BASELINE.json"

# --- the linkage lexicon, as CALIBRATED in xB006 -------------------------------------------
# Each alternative does EVIDENTIAL work in a kill: it says a recurrence carries no information.
# "by construction" was in a first draft, is descriptive prose ("golden BY CONSTRUCTION", B425),
# drove 27 of an initial 46 candidates on its own, and is deliberately ABSENT.
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
MAP = re.compile(
    r"\bmap\b|\bmorphism\b|\bisomorphism\b|\bhomomorphism\b|\bembedding\b|\bsurjection\b"
    r"|\bfunctor\b|\bequivariant\b|\bexhibit\w*\b|\bacts?\s+(?:faithfully|transitively|on)\b"
    r"|\bconjugat\w+\b|\bcommutes?\s+with\b|\bby\s+definition\b|\brestated\s+as\b",
    re.I,
)
NAMED_THEOREM = re.compile(
    r"\bMcKay\b|\bMostow\b|\bThurston\b|\bADE\s+classification\b|\bclassification\s+theorem\b"
    r"|\bMilgram\b|\bNeumann[-–]Reid\b|\bPorti\b|\bFricke\b|\bMarkov\b|\bNielsen[-–]Thurston\b"
    r"|\bGauss[-–]Bonnet\b|\bPoincar\w*\s+duality\b|\bby\s+a\s+theorem\b|\bis\s+a\s+theorem\b"
    r"|\bWeil\b|\bMaclachlan[-–]Reid\b|\bCao[-–]Meyerhoff\b|\bRiemann[-–]Roch\b"
    r"|\bSchur\b|\bBurnside\b|\bSylow\b|\bGalois\s+theory\b|\bclass\s+field\b|\bMinkowski\b"
    r"|\bDirichlet\b|\bGalois[-–]stable\b",
    re.I,
)
# a COMPUTED base rate is a different and sound kind of argument -- xB006 measured 10 of 30.
BASE_RATE = re.compile(
    r"\bbase[- ]rate\b|\blook[- ]elsewhere\b|\bgeneric\s+at\b|\b\d+\s*(?:in|of)\s*\d+\b"
    r"|\bmultiple[- ]comparisons\b|\bexpected\s+by\s+chance\b|\bp\s*<\s*0?\.\d+"
    r"|\bpost[- ]hoc\b|\bpercentile\b|\bper\s+decade\b|\bdensity\b",
    re.I,
)
KILLWORD = re.compile(
    r"\bKILLED\b|\bREFUTED\b|\bNEGATIVE\b|\bdead\b|\bdoes\s+not\s+survive\b|\bfails\b"
    r"|\bclosed\b|\bno\s+evidence\b|\bcannot\b|\bis\s+not\b", re.I)

WINDOW = 600


def is_kill(verdict, claim):
    return verdict == "NEGATIVE" or bool(KILLWORD.search((claim or "")[:400]))


def adjudicate(blob):
    """(hits, klass, why).  klass: None (no hit) | 'A' theorem | 'B' map | 'R' base rate
    | 'C' NO LINK EXHIBITED -- the defect this gate exists for."""
    hits = list(LINKAGE.finditer(blob or ""))
    if not hits:
        return [], None, ""
    win = "\n".join(blob[max(0, m.start()-WINDOW): m.end()+WINDOW] for m in hits)
    m = NAMED_THEOREM.search(win)
    if m:
        return hits, "A", f"named theorem in the linkage window: {m.group(0)}"
    m = MAP.search(win)
    if m:
        return hits, "B", f"map-language in the linkage window: {m.group(0)}"
    m = BASE_RATE.search(win)
    if m:
        return hits, "R", f"a computed base rate, not a sameness claim: {m.group(0)}"
    return hits, "C", ("no map, no named theorem and no computed base rate within "
                       f"{WINDOW} chars of the linkage claim")


def scan():
    out = []
    for p in sorted(ROOT.glob("frontier/*/arc_verdict.json")):
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        claim = d.get("claim_one_line", "")
        if not is_kill(d.get("verdict"), claim):
            continue
        f = p.parent / "FINDINGS.md"
        txt = f.read_text(encoding="utf-8", errors="replace") if f.exists() else ""
        hits, k, why = adjudicate(claim + "\n" + txt)
        if hits and k == "C":
            out.append((p.parent.name, why))
    return out


def baseline():
    try:
        return set(json.loads(BASELINE.read_text(encoding="utf-8")).get("frozen", []))
    except Exception:
        return set()


def check():
    frozen = baseline()
    hits = scan()
    novel = [(n, w) for n, w in hits if n not in frozen]
    return novel, hits, frozen


# --- the two-way self-test -----------------------------------------------------------------
PLANT_BAD = ("the object's Z/5, the lattice's Z/5 and the group's Z/5 are ALL canonically linked, "
             "so the recurrence is NOT EVIDENCE: it is one fact wearing three hats. REFUTED.")
PLANT_OK_THM = ("the three faces are forced, not evidence: one ADE classification theorem "
                "produces all three, so the recurrence is generic. KILLED.")
PLANT_OK_RATE = ("surjecting onto 2T is generic at roughly 1 in 3, so the equal counts are "
                 "not evidence of distinction. NEGATIVE.")
# xB005's Q3 AS IT STOOD BEFORE ADDENDUM 1 -- the error this gate was designed from.
Q3_ORIGINAL = (
    "Q3, THE FINDING: mu_3 in Q(sqrt-3), Z(E6), 2T/Q8 and the node's order-3 action. "
    "mu_3 <-> Q(sqrt-3): Q(zeta_3) = Q(sqrt-3), the SAME OBJECT. "
    "node's Z/3 <-> 2T/Q8: IDENTICAL, not merely isomorphic. "
    "ALL FOUR ARE CANONICALLY LINKED. By section 2's own standard the recurrence is NOT "
    "EVIDENCE: it is one fact -- the ramification of 3 -- wearing four hats. REFUTED.")
# and the CORRECTED Q3, which names the dissociation -- the gate must pass this.
Q3_CORRECTED = (
    "Q3 CORRECTED: the links connect {node, 2T/Q8, Z(E6)} only and leave the arithmetic hat "
    "joined by no edge. Testing the missing edge: on m004's own tower (LR)^n the invariant "
    "trace field is constant while the node order runs 3, 3, 1, 3, and 31 of 34 order-3 "
    "bundles are not Q(sqrt-3) -- so the hats are two independent facts. The recurrence is "
    "still NOT EVIDENCE, but by pricing (0.58 bits, a base rate of 8 in 12 in A_4), not by "
    "sameness. REFUTED.")


def selftest():
    fails = []

    def cls(blob):
        return adjudicate(blob)[1]

    for nm, blob, want, why in (
        ("planted E82 kill", PLANT_BAD, "C", "must be caught"),
        ("sound: named theorem", PLANT_OK_THM, "A", "must be cleared"),
        ("sound: computed base rate", PLANT_OK_RATE, "R", "must be cleared"),
        ("xB005 Q3, ORIGINAL", Q3_ORIGINAL, "C", "THE ERROR THIS GATE WAS DESIGNED FROM"),
        ("xB005 Q3, CORRECTED", Q3_CORRECTED, "R", "the repair must be recognised"),
    ):
        got = cls(blob)
        ok = got == want
        print(f"  [{'ok' if ok else 'FAIL'}] {nm:<28} want {want}, got {got}   ({why})")
        if not ok:
            fails.append(nm)
    # the record's own sound form must not be a candidate
    b727 = ROOT / "frontier" / "B727_base_rate_the_structure" / "FINDINGS.md"
    if b727.exists():
        hits, k, why = adjudicate(b727.read_text(encoding="utf-8", errors="replace"))
        ok = bool(hits) and k != "C"
        print(f"  [{'ok' if ok else 'FAIL'}] {'B727 (the sound form)':<28} tripped {bool(hits)}, "
              f"class {k}   (must trip and must NOT be C)")
        if not ok:
            fails.append("B727")
    return fails


def selftest_quiet():
    """the same two-way self-test, silent -- for the gate to run before trusting any finding."""
    import io
    import contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        return selftest()


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        f = selftest()
        print("\nSELFTEST", "PASS" if not f else f"FAIL: {f}")
        sys.exit(0 if not f else 1)
    novel, hits, frozen = check()
    print(f"linkage-kills: {len(hits)} unexhibited linkage kills, {len(frozen)} frozen, "
          f"{len(novel)} NEW")
    for n, w in novel:
        print(f"  NEW  {n}: {w}")
    sys.exit(1 if novel else 0)
