#!/usr/bin/env python3
"""THE BRANCH GAP -- this bench has been reasoning on a tree 35 arcs stale.

No seal: this cell ASSERTS NOTHING NEW.  It audits what this branch is missing
against a sibling branch and files the consequences, including against itself.

WHY IT EXISTS.  Phase 3's plan was written on the premise that the multi-cusp
index was "named and never run", taken from B1324's wording and from THIS
BRANCH's frontier/ listing.  It had been run -- twice -- on arcs that are not
on this branch.  That is exactly the failure class the record numbers:

  BENCH ERROR #17 (cloud memo 158): "THE LIVE ROUTE IS NOT UNRUN, IT IS RUN
  AND SECTOR-COMPLETE" -- a seat asserting an unrun cell from a directory
  listing it never opened, WHILE WRITING A MEMO CHARGING EXACTLY THAT FAILURE.

B1338 (NEGATIVE, also missing here) reports that the anti-rediscovery
instrument built against that class is ITSELF BLIND.  This cell is that
instrument applied to this bench, by hand.

Stdlib + git only.
"""
from __future__ import annotations

import json
import subprocess
import sys

SIB = "origin/<remote>/paper-verification-ufp0zn"


def rule(t):
    print("\n" + "-" * 78)
    print(" " + t)
    print("-" * 78)


def git(*a):
    r = subprocess.run(["git"] + list(a), capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(a)}: {r.stderr.strip()}")
    return r.stdout


def verdict_of(arc):
    try:
        d = json.loads(git("show", f"{SIB}:frontier/{arc}/arc_verdict.json"))
    except Exception:
        return "-", ""
    return d.get("verdict", "?"), (d.get("claim_one_line") or "")


# arcs whose subject collides with something THIS BENCH asserted in phases 1-3
COLLISIONS = {
    "B1341_the_action_of_the_object":
        "Phase 2 cell 10 and Phase 3's plan both reported TOE row 4 (DYNAMICS) as "
        "NOT-COMPUTABLE.  This arc is PROVED and is, in its own words, 'an attempt at "
        "TOE row 4 (dynamics) rather than a report on it'.",
    "B1330_the_best_case_object":
        "Phase 2 cell 8 intersected the 112-member family with chirality to find a "
        "witness.  This arc did the same intersection FOR THE INDEX and went further: "
        "8 members, 4 ONE-CUSPED (s958, v2873, t12833, t12835) -- so no multi-cusp "
        "extension is owed at all -- and v2873 returns ZERO over 952 in-domain sectors.",
    "B1333_the_index_on_several_cusps":
        "Phase 3's plan called the multi-cusp index 'the named-never-run next "
        "computation', from B1324's wording.  This arc ran it on all 54 multi-cusped "
        "chiral covers: 38 070 sectors, NON-ZERO INDEX 0.",
    "B1335_the_vanishing_is_not_formal_exhibited":
        "Memo 230 said live non-vacuity in char 0 was never established.  Still true -- "
        "this arc's nonzero is over F_p and is REFUTED in char 0 -- but the arc itself "
        "was not on this branch when that was written.",
    "B1338_the_instrument_is_blind":
        "Names the failure class this very cell is an instance of, and reports that the "
        "instrument built against it (B1202) is itself blind.",
    "B1345_the_jorgensen_number":
        "Phase-1 predecessor work reached this independently; BENCH ERROR #31 was filed "
        "for searching phrasings and walking past a directory named for it.",
    "B1406_the_mirror_and_the_bulk":
        "Same title as this bench's memo 229 -- the same question answered twice, on "
        "two branches, without either seeing the other.",
}


def main() -> int:
    print("=" * 78)
    print(" THE BRANCH GAP -- what this branch does not know")
    print("=" * 78)

    here = set(git("ls-tree", "-d", "--name-only", "HEAD", "frontier/").split())
    sib = set(git("ls-tree", "-d", "--name-only", SIB, "frontier/").split())
    here = {p.split("/", 1)[1] for p in here if "/" in p}
    sib = {p.split("/", 1)[1] for p in sib if "/" in p}
    missing = sorted(sib - here)
    extra = sorted(here - sib)

    rule("THE DIFF")
    print(f"    arcs on HEAD                     : {len(here)}")
    print(f"    arcs on the sibling branch       : {len(sib)}")
    print(f"    ON THE SIBLING, ABSENT HERE      : {len(missing)}")
    print(f"    on HEAD, absent there            : {len(extra)}")
    assert missing, "empty diff -- the B1197 vacuity trap"

    counts = {}
    rows = []
    for a in missing:
        v, c = verdict_of(a)
        counts[v] = counts.get(v, 0) + 1
        rows.append((v, a, c))
    print(f"\n    by verdict: {dict(sorted(counts.items()))}")

    rule("THE 35, BY VERDICT")
    for v in ("PROVED", "NEGATIVE", "OPEN", "?", "-"):
        sel = [r for r in rows if r[0] == v]
        if not sel:
            continue
        print(f"\n    {v} ({len(sel)}):")
        for _, a, _ in sel:
            mark = "  <-- COLLIDES" if a in COLLISIONS else ""
            print(f"      {a}{mark}")

    rule("THE COLLISIONS -- arcs that answer or pre-empt what this bench asserted")
    for a, why in COLLISIONS.items():
        v, _ = verdict_of(a)
        present = a in sib
        print(f"\n    {a}  [{v}]{'' if present else '  (NOT FOUND ON SIBLING)'}")
        for line in why.split(". "):
            if line.strip():
                print(f"      {line.strip()}{'.' if not line.endswith('.') else ''}")

    rule("BENCH ERROR #34 -- filed against this bench, at point of occurrence")
    print("""
    THE ERROR.  Phase 3's plan asserted that the multi-cusp index was "named
    and never run", and Phase 2 cell 10 reported TOE row 4 (dynamics) as
    NOT-COMPUTABLE.  Both were read off THIS BRANCH's frontier/ listing.  Both
    are wrong on the record as a whole: B1333 ran the index at 38 070 sectors,
    and B1341 is a PROVED attempt at row 4.

    THE CLASS IS ALREADY NUMBERED.  Cloud memo 158, BENCH ERROR #17: "THE LIVE
    ROUTE IS NOT UNRUN, IT IS RUN AND SECTOR-COMPLETE" -- a seat asserting an
    unrun cell from a directory listing it never opened, while writing a memo
    charging exactly that failure.  This is the same error, seventeen numbers
    later, by a bench that had read #17's own description this session.

    WHAT THE STANDING RULES DID AND DID NOT CATCH.  already_banked.py and
    absence_sweep.py were both run, repeatedly, and neither fired -- because
    BOTH SEARCH THE HEADS THIS BRANCH KNOWS ABOUT, and absence_sweep's own
    output says "13 heads enumerated".  The sibling branch's 35 arcs were
    inside that enumeration as a HEAD but the tools report per-phrase presence,
    not per-arc coverage, so a phrase absent from this tree reads as absent
    from the record.  THE INSTRUMENT IS NOT AT FAULT FOR A QUESTION IT WAS NOT
    ASKED; the bench is at fault for not asking it.

    THE FIX, and it is one line of discipline: BEFORE calling anything unrun,
    DIFF THE FRONTIER AGAINST EVERY HEAD, not just this one.  That is what this
    certificate does, and it should run before any "never run" claim.""")

    rule("WHAT IS ACTUALLY STILL OPEN, from the arcs this branch was missing")
    print("""
    B1330 closes with a NAMED, BOUNDED, UN-RUN computation -- verbatim:

      "NOT DONE: s958, t12833 and t12835 carry three-generator presentations,
       where brute-force SL(2,F_p) enumeration is 336^3 and was not run; they
       are named, not computed."

    These are the remaining ONE-CUSPED best-case objects: chiral, in m004's own
    commensurability class, carrying Galois-unprotected order-3 twists, and in
    the index's own stated domain with NO multi-cusp extension owed.  v2873 --
    the one that was computed -- returned ZERO over 952 in-domain sectors, and
    B1330 calls that "THE FIFTH INDEPENDENT REGIME RETURNING ZERO".

    HONEST WEIGHT: a sixth zero would add little; the vanishing is already
    "the strongly favoured reading" in B1330's own words.  A NONZERO would be
    the first live positive in characteristic zero anywhere in the record.
    That asymmetry is the whole reason the computation is still worth doing.""")

    rule("VERDICT")
    print(f"    {len(missing)} arcs absent from this branch; {len(COLLISIONS)} of them "
          f"collide with claims this bench made.")
    print("    BENCH ERROR #34 filed.  No prior result of this bench is retracted by")
    print("    this cell except the two NOT-RUN/NOT-COMPUTABLE assertions named above.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
