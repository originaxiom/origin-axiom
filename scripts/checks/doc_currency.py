#!/usr/bin/env python3
"""doc-currency — detect living documents that no longer reflect the corpus.

B984. The failure this catches: a document that was true when written and was never
updated as the corpus moved past it. `ROADMAP_TOE.md` described the programme's position
as "the kinematic/symmetry frame is forced arithmetic" for a month after B862/B863/B864
made that false; `THE_SM_VERDICT.md` shipped omitting eleven of the twelve cascade arcs.
Neither was caught by any gate, because every gate checked *arcs*, not *surfaces*.

The measure is deliberately crude and honest: for each registered living document, the
newest arc it cites, against the newest arc that exists. A document whose newest citation
lags the corpus by more than its declared tolerance is STALE — not wrong, but owed a read.

A document may declare `<!-- doc-currency: frozen -->` to opt out permanently (records,
dated snapshots, superseded files kept for provenance). That is a *visible* opt-out: the
gate reports frozen documents in its summary so an opt-out cannot hide.
"""
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
FRONTIER = ROOT / "frontier"

ARC_RE = re.compile(r"\bB(\d{1,4})\b")
# B989: the marker counts only when it IS a marker -- i.e. the line begins with the HTML
# comment. docs/PRACTICES.md *documents* the marker inside a code span and thereby froze
# itself: a document explaining the opt-out, opting itself out. Same mention-vs-use failure
# that hit retraction-sweep the same day, in a second gate.
FROZEN_RE = re.compile(r"^\s*<!--\s*doc-currency:\s*frozen", re.I | re.M)

# Living surfaces: a reader forms their picture of the programme from these, so each one
# being current matters more than any single arc being current. Tolerance = how many arcs
# may be banked before the document is owed a read.
LIVING = {
    # qL163's port (owner: YES, 2026-08-13): the three governed registers were
    # outside the watch — the registers that RECORD debts were themselves unwatched.
    "docs/ERROR_LEDGER.md": 40,
    "docs/RETRACTIONS.md": 60,
    "docs/REPRESENTATION_TRIAGE.md": 60,

    "docs/THE_FRAMEWORK.md": 10,
    "docs/THE_LADDER.md": 10,
    "docs/COMPUTE_THE_PROGRAM.md": 25,
    "docs/THE_SM_VERDICT.md": 15,
    "docs/LAW_MAP.md": 10,
    "docs/CAMPAIGN_STATUS.md": 5,
    "docs/OPEN_LEADS.md": 10,
    "CLAIMS.md": 40,
    "docs/SM_SPECIFICATION_LEDGER.md": 30,
    "docs/GUT_REQUIREMENTS_LEDGER.md": 30,
    "docs/RETRACTED_PHRASES.md": 30,
    "docs/THEOREM_LEDGER.md": 30,
    "WORKING_RULES.md": 40,
    "docs/PRACTICES.md": 40,
    "docs/TOOLBOX.md": 40,
}


def newest_arc_in_repo() -> int:
    best = 0
    for d in FRONTIER.iterdir():
        if not d.is_dir():
            continue
        m = re.match(r"B(\d{1,4})", d.name)
        if m:
            best = max(best, int(m.group(1)))
    return best


def newest_arc_cited(path: pathlib.Path) -> int:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return -1
    nums = [int(m.group(1)) for m in ARC_RE.finditer(text)]
    return max(nums) if nums else 0


# A DECLARED DEBT is not an exemption. B982 found seven gate exemptions resting on an audit
# that never named them; the fix is that every pass-through must name WHAT is owed and WHEN it
# was declared, and must be REPORTED LOUDLY on every run. Debts do not silence the gate -- they
# appear in its output every time, and `test_b984_doc_currency.py` fails if the set grows.
DECLARED_DEBT = {
    "docs/TOOLBOX.md": ("declared 2026-08-09 (B984): 613 arcs stale. The owner's own protocol "
                        "says read the toolset before any important probe, so this is the "
                        "highest-priority debt on the board.", "2026-08-09"),
    "CLAIMS.md": ("declared 2026-08-09 (B984): 129 arcs stale. Gate 5 governs what may enter, "
                  "not whether it is current; the cascade layer (B860-B873) is absent.",
                  "2026-08-09"),
    "docs/THEOREM_LEDGER.md": ("declared 2026-08-09 (B984): 63 arcs stale.", "2026-08-09"),
    "docs/GUT_REQUIREMENTS_LEDGER.md": ("declared 2026-08-09 (B984): 31 arcs stale, just over "
                                        "tolerance.", "2026-08-09"),
}


def check() -> tuple[list[str], list[str]]:
    head = newest_arc_in_repo()
    existing_ids = sorted(
        int(m.group(1))
        for d in FRONTIER.iterdir() if d.is_dir()
        for m in [re.match(r"B(\d{1,4})", d.name)] if m
    )
    stale, frozen = [], []
    for rel, tol in sorted(LIVING.items()):
        p = ROOT / rel
        if not p.is_file():
            stale.append(f"{rel}: MISSING (a registered living document must exist)")
            continue
        if FROZEN_RE.search(p.read_text(encoding="utf-8", errors="ignore")):
            frozen.append(rel)
            continue
        cited = newest_arc_cited(p)
        # lag counts EXISTING arcs newer than the citation, not numeric distance:
        # the reserved range B1045-B1059 (the cloud-collision resolution) made
        # max-number lag count phantom arcs -- an E38 in this checker's own
        # threshold semantics, repaired 2026-08-13. "Owed a read" can only be
        # owed for arcs that exist.
        lag = sum(1 for n in existing_ids if n > cited)
        if lag > tol and rel not in DECLARED_DEBT:
            stale.append(f"{rel}: newest citation B{cited}, corpus head B{head} "
                         f"(lag {lag} existing arcs > tolerance {tol})")
    return stale, frozen


def main() -> int:
    stale, frozen = check()
    if DECLARED_DEBT:
        head = newest_arc_in_repo()
        print(f"  doc-currency: {len(DECLARED_DEBT)} DECLARED DEBTS (visible, never silent) --")
        for rel, (why, when) in sorted(DECLARED_DEBT.items()):
            cited = newest_arc_cited(ROOT / rel)
            print(f"    {rel}: B{cited} vs B{head} (lag {head - cited}) -- {why}")
    if frozen:
        print(f"  doc-currency: {len(frozen)} frozen (visible opt-out): {', '.join(frozen)}")
    if stale:
        print("  doc-currency: STALE living documents --")
        for s in stale:
            print(f"    {s}")
        print("  a stale surface is not wrong; it is owed a read. Update it or freeze it "
              "explicitly with <!-- doc-currency: frozen -->.")
        return 1
    print(f"  doc-currency: ok ({len(LIVING) - len(frozen)} living documents current)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
