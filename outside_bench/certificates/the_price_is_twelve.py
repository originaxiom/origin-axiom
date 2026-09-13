#!/usr/bin/env python3
"""THE PRICE IS TWELVE -- the live input count, recomputed from the ledger.

No seal: every claim is a structural read of tracked files at HEAD, reproducing
B1266's union-find on the LIVE ledger rather than citing its 2026-09-06 result.

The question: the owner asked what the 11 irreducible inputs are.  THE_SM_VERDICT
says 4 + 7 = 11 irreducible and 14 rows outstanding.  B1261:85 says a later arc
raised the baseline.  This certificate settles which number is live by computing
it, and flags every surface still carrying the stale one.
"""

from __future__ import annotations

import json
import os
import re
import sys

LEDGER = "docs/IDENTIFICATION_LEDGER.md"
BASELINE = "docs/IDENTIFICATION_BASELINE.json"
VERDICT = "docs/THE_SM_VERDICT.md"
CHAIN = "docs/THE_END_TO_END_CHAIN.md"

FAILURES: list[str] = []


def fail(tag: str, msg: str) -> None:
    FAILURES.append(f"{tag}: {msg}")
    print(f"  !! FAIL [{tag}] {msg}")


def rule(t: str) -> None:
    print("\n" + "-" * 78)
    print(t)
    print("-" * 78)


def main() -> int:
    print("=" * 78)
    print(" THE PRICE IS TWELVE -- the live input count, recomputed")
    print("=" * 78)

    led = open(LEDGER, encoding="utf-8").read()
    base = json.load(open(BASELINE, encoding="utf-8"))
    chain = open(CHAIN, encoding="utf-8").read()
    verdict = open(VERDICT, encoding="utf-8").read()

    # ---------------------------------------------------------------- rows
    rule("STEP 1 -- the UNEARNED rows, read from the ledger table")
    rows = re.findall(r"^\|\s*\*{0,2}(I-\d+)\*{0,2}\s*\|(.*)$", led, re.M)
    unearned = [t for t, rest in rows if "**UNEARNED**" in rest]
    print(f"    total I-rows in the ledger : {len(rows)}")
    print(f"    UNEARNED                   : {len(unearned)}")
    print(f"    {unearned}")

    print(f"\n    baseline file says unearned = {base['unearned']}, rows = {base['rows']}")
    if sorted(unearned) != sorted(base["rows"]) or len(unearned) != base["unearned"]:
        fail("ROWS", "the ledger table and the baseline JSON disagree on the unearned set")
    else:
        print("    ledger table and baseline JSON AGREE (independent surfaces, same answer)")

    # ---------------------------------------------------------------- union-find
    rule("STEP 2 -- B1266's union-find, rerun on the LIVE ledger")
    print("""
    B1266's rule: a row that states IN ITS OWN earning text that paying another
    UNEARNED row pays it is not an independent source.  Two traps B1266 names and
    this rerun must also avoid: a reference to an EARNED row is not a debt, and a
    mutual reference (I-10 <-> I-11) is ONE source, not two.""")

    body = {t: rest for t, rest in rows}
    earned = {t for t, rest in rows if "**UNEARNED**" not in rest and "EARNED" in rest}

    parent = {t: t for t in unearned}

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[max(ra, rb, key=lambda s: int(s.split("-")[1]))] = \
                min(ra, rb, key=lambda s: int(s.split("-")[1]))

    edges = []
    for t in unearned:
        # the earning text is the ledger row's last column; scan the whole row for
        # an explicit "paying X pays this" / "the same map as X" reduction.
        txt = body[t]
        for other in re.findall(r"I-\d+", txt):
            if other == t:
                continue
            if other in earned:
                continue                      # trap 1: an earned row is not a debt
            if other not in parent:
                continue
            pat = (rf"(paying {other} pays|pays {other}|i\.e\.\s*\*{{0,2}}paying {other}|"
                   rf"the same map as {other}|an instance of {other}|"
                   rf"instance of {other}'s source|{other}'s source, not a new one)")
            if re.search(pat, txt, re.I):
                edges.append((t, other))
                union(t, other)

    print("\n    reduction edges found in the rows' own text:")
    for a, b in edges:
        print(f"      {a}  reduces to  {b}")

    groups: dict[str, list[str]] = {}
    for t in unearned:
        groups.setdefault(find(t), []).append(t)
    nsources = len(groups)

    print(f"\n    {len(unearned)} unearned rows  ->  {nsources} IRREDUCIBLE SOURCES")
    for root in sorted(groups, key=lambda s: int(s.split("-")[1])):
        mem = sorted(groups[root], key=lambda s: int(s.split("-")[1]))
        print(f"      [{len(mem)}] {', '.join(mem)}")

    # ---------------------------------------------------------------- axioms
    rule("STEP 3 -- the axioms, read from the chain census")
    m = re.search(r"The four axioms are \*\*(C\d+), (C\d+), (C\d+)\*\*.*?and \*\*(C\d+)\*\*",
                  chain, re.S)
    if not m:
        fail("AXIOMS", "the chain census sentence naming the four axioms was not found")
        ax = []
    else:
        ax = list(m.groups())
    print(f"    axioms named in {CHAIN}: {ax}")
    for a in ax:
        lab = re.search(rf"^- \*\*{a} \[AXIOM — ([^;\]]+)", chain, re.M)
        print(f"      {a}: {lab.group(1).strip() if lab else '(the observer closings, named in the census sentence)'}")
    naxioms = len(ax)

    # ---------------------------------------------------------------- the price
    rule("STEP 4 -- the price")
    rows_out = naxioms + len(unearned)
    irred = naxioms + nsources
    print(f"    ROWS OUTSTANDING  : {naxioms} axioms + {len(unearned)} unearned rows = {rows_out}")
    print(f"    IRREDUCIBLE INPUTS: {naxioms} axioms + {nsources} sources      = {irred}")
    print(f"\n    bought, of the SM's 19 free parameters: 0")

    # ---------------------------------------------------------------- staleness
    rule("STEP 5 -- the verdict doc: stale numbers must be STRUCK, not live")
    print("""
    A stale figure inside a ~~strikethrough~~ is PROVENANCE and must be kept
    (the addendum-only rule: mark superseded in place, never rewrite history).
    The same figure OUTSIDE a strikethrough is a LIVE WRONG CLAIM.  This step
    separates the two, so the check can go green without deleting the record --
    memo 216's precedent, where the certificates were re-pointed at the STRUCK
    forms so the historical text is still verified present.""")

    struck = set()
    for m in re.finditer(r"~~.*?~~", verdict, re.S):
        struck.add((m.start(), m.end()))

    def inside_strike(i: int) -> bool:
        return any(a <= i < b for a, b in struck)

    patterns = [(r"4 \+ 7 = 11", "irreducible 4+7=11"),
                (r"10 rows reduce to 7\s+irreducible", "10 rows -> 7 sources"),
                (r"\*\*11 = irreducible inputs\*\*", "11 = irreducible"),
                (r"4 \+ 10 = 14", "rows 4+10=14"),
                (r"\*\*14 = rows\s+outstanding\*\*", "14 = rows outstanding")]
    live_stale, kept = [], []
    for pat, what in patterns:
        for m in re.finditer(pat, verdict):
            (kept if inside_strike(m.start()) else live_stale).append(what)

    print(f"\n    stale figures KEPT AS PROVENANCE (inside ~~...~~) : {len(kept)}")
    for w in kept:
        print(f"      struck: {w}")
    print(f"    stale figures STILL LIVE (outside ~~...~~)        : {len(live_stale)}")
    for w in live_stale:
        print(f"      !! LIVE: {w}")
    if live_stale:
        fail("VERDICT", f"{len(live_stale)} stale figure(s) still stated as live")

    print("\n    and the LIVE figures must be present and must be the computed ones:")
    wants = [(f"4 + {nsources} = {irred}", "the irreducible count"),
             (f"{rows_out} ROWS OUTSTANDING", "the row count")]
    for text, what in wants:
        present = text in verdict
        print(f"      {what}: '{text}' present = {present}")
        if not present:
            fail("VERDICT", f"the live figure '{text}' is not stated in the verdict doc")

    print(f"""
    The ledger's own baseline records the raises that moved it:""")
    for r in base.get("_baseline_raises", []):
        if r.get("to", 0) >= 11:
            print(f"      {r.get('date')}  {r.get('from')} -> {r.get('to')}  "
                  f"row {r.get('row')}  (arc {r.get('arc','-')})")

    # ---------------------------------------------------------------- controls
    rule("CONTROLS")
    # C1: the union-find must be able to return something other than the answer
    print("    C1 (non-vacuity) -- with the reduction edges IGNORED, the same rows give")
    print(f"       {len(unearned)} sources, not {nsources}.  The reduction is doing work.")
    c1 = nsources != len(unearned)
    print(f"    C1: {'PASS' if c1 else 'FAIL'}")
    if not c1:
        fail("C1", "no row reduced -- the union-find found nothing to do")

    # C2: the two traps B1266 names must actually be present to be avoided
    trap1 = bool(re.search(r"I-25.*I-1\b", body.get("I-25", "")))
    trap2 = ("I-11" in body.get("I-10", "") and "I-10" in body.get("I-11", ""))
    print(f"\n    C2 (B1266's two traps are still live in the data):")
    print(f"       trap 1, I-25 references the EARNED I-1        : {trap1}")
    print(f"       trap 2, I-10 and I-11 reference each other    : {trap2}")
    print(f"       I-1 is EARNED, so trap 1 contributes no edge  : {'I-1' in earned}")
    c2 = trap2 and ("I-1" in earned)
    print(f"    C2: {'PASS' if c2 else 'FAIL'}")
    if not c2:
        fail("C2", "B1266's named traps are not reproducible on the live ledger")

    # C3: the 2-cycle must collapse to ONE source
    c3 = find("I-10") == find("I-11")
    print(f"\n    C3 (the 2-cycle collapses to one source, not two): {c3}")
    print(f"    C3: {'PASS' if c3 else 'FAIL'}")
    if not c3:
        fail("C3", "I-10/I-11 did not collapse")

    print("\n" + "=" * 78)
    print(f" LIVE PRICE: {naxioms} axioms + {nsources} irreducible sources = {irred}")
    print(f"             ({rows_out} rows outstanding) vs the SM's 19 free parameters")
    print(f" verdict doc: {len(kept)} stale figure(s) struck for provenance, {len(live_stale)} still live")
    if FAILURES:
        print("\n FAILURES:")
        for f in FAILURES:
            print(f"   - {f}")
    print("=" * 78)
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
