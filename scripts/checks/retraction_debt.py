#!/usr/bin/env python3
"""retraction-debt — every RETRACTED arc carries a row, or its retraction is invisible.

THE FAILURE THIS EXISTS TO STOP (B921-9b; the design is `relay_debt.py`'s, re-pointed)
--------------------------------------------------------------------------------------
`retraction-sweep` is GREEN on a corpus where seven of the twelve RETRACTED arcs have no
row in `docs/RETRACTIONS.md` at all — and **that is correct behaviour, not a bug.** Its
docstring is *"Registered retracted phrases must not appear as live claims"*: it polices
the CONTENT of rows that exist. The comment introducing `relay-debt` in
`scripts/gates/gates.py` already named the gap in the corpus's own words:

    "`lawmap-scope` and `retraction-sweep` police the CONTENT of rows that exist;
     neither notices a row that was NEVER WRITTEN."

That comment built the third gate for exactly this failure — **for relays. Nothing did it
for retractions.** So this is not a new discovery; it is L143's gap, still open on a second
surface, found by a lead row (B921-9) that had been sitting on it since 2026-08.

Why it matters more here than anywhere else: `RETRACTIONS.md`'s own preamble says the
index exists because *"a reader of an old FINDINGS could still act on them."* An
unregistered retraction is precisely that reader's hazard — the arc's own file may carry
a correction banner, but nothing tells a reader who never opens that file. And
`RETRACTED_PHRASES` (which `retraction-sweep` reads) is populated FROM this index, so an
unwritten row also means the retracted wording is never swept for.

THE RULE
--------
Every arc whose `arc_verdict.json` says `verdict: RETRACTED` is NAMED in
`docs/RETRACTIONS.md`, on a line that also carries a retraction verb. The verb
requirement is what stops a bare incidental mention ("see B731 for the index table")
from discharging the debt: the row has to SAY the arc was retracted.

WHAT THIS GATE DELIBERATELY DOES NOT DO
---------------------------------------
It does not judge a row's content — that is `retraction-sweep`'s job, and the two are
complementary by construction (existence here, content there). It does not require a row
for a SUPERSEDED arc: `gate_supersession_backlinks` already covers those, and its own
docstring draws the line — *"superseding an arc is not retracting it, and the 12
RETRACTED arcs are a separate, deliberate act."*

MB12: this check is shown FAILING (7 debts) before the rows that fix it, in the same
commit's message. A check that cannot fail is not a check.
"""
from __future__ import annotations

import glob
import json
import os
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
# OA_RETRACTIONS_LEDGER points the check at a copy, for tests only -- the failure path has to
# be exercisable against a real-shaped file without editing the real one (relay_debt.py does the
# same with OA_RELAY_TODAY). The gate never sets it.
LEDGER = pathlib.Path(os.environ.get("OA_RETRACTIONS_LEDGER")
                      or ROOT / "docs" / "RETRACTIONS.md")

# The corpus's retraction vocabulary, as actually used in this ledger's existing rows:
# RETRACTED (B519), REFUTED (B90), CORRECTED (B95), REPLACED (PC13), WITHDRAWN (B438),
# RELABELED (B225), DISSOLVED (B615), SUPERSEDED (B609), OVERTURNED (B216's own banner),
# NEGATED (B58's own banner), VACUOUS (B780's). Case-insensitive: the 2026-08-08 block
# heads with a lower-case "withdrawn".
VERB_RE = re.compile(
    r"retract|refut|withdraw|correct|replaced|relabel|dissolv|supersed|overturn|negated|vacuous",
    re.I)


def retracted_arcs() -> dict[str, list[str]]:
    """{arc id: [paths of its verdict files]} for every arc whose verdict is RETRACTED.

    The value is a LIST because arc ids are not unique: `gates.py` grandfathers the **B58**
    collision (`frontier/B58_stage1` NEGATIVE, `frontier/B58_sl4_tower_test` RETRACTED), and
    GOVERNANCE forbids renaming banked paths, so the collision is permanent. Keyed to a single
    path, a second RETRACTED arc sharing an id would silently overwrite the first and vanish
    from the debt list -- a silent exemption, which is the exact failure this gate exists to
    stop, one level down. Non-RETRACTED siblings never enter at all.
    """
    out: dict[str, list[str]] = {}
    for f in sorted(glob.glob(str(ROOT / "frontier" / "*" / "arc_verdict.json"))):
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception:
            # A malformed verdict file is `arc-verdicts`' business, not this gate's; but do
            # not silently EXEMPT it -- E66's shape is a gate that skips what it cannot parse.
            out.setdefault(f"<unparsed:{os.path.relpath(f, ROOT)}>", []).append(f)
            continue
        if str(d.get("verdict", "")).strip().upper() == "RETRACTED":
            i = str(d.get("id", "")).strip()
            if i:
                out.setdefault(i, []).append(os.path.relpath(f, ROOT))
    return out


def registered(text: str) -> set[str]:
    """arc ids named on a line of the ledger that also carries a retraction verb."""
    found = set()
    for line in text.splitlines():
        if not VERB_RE.search(line):
            continue
        # `B437` must not be matched by `B4370`; `B437_child_abelian_book` must match.
        for m in re.finditer(r"\bB([0-9]{1,4})(?![0-9])", line):
            found.add("B" + m.group(1))
    return found


def check() -> tuple[list[str], dict]:
    if not LEDGER.is_file():
        return ([f"{LEDGER.relative_to(ROOT)} is MISSING — the index is constitutive"], {})
    text = LEDGER.read_text(encoding="utf-8", errors="ignore")
    have = registered(text)
    arcs = retracted_arcs()
    debts = []
    for i in sorted(arcs, key=lambda s: (int(s[1:]) if s[1:].isdigit() else 10 ** 9, s)):
        if i not in have:
            debts.append(f"{i}: RETRACTED in {', '.join(arcs[i])} — NO ROW in {LEDGER.name}")
    return debts, {"retracted": len(arcs), "registered": len(arcs) - len(debts)}


def main() -> int:
    debts, counts = check()
    if counts:
        print(f"  retraction-debt: {counts['registered']} of {counts['retracted']} "
              f"RETRACTED arcs registered")
    if debts:
        print(f"  retraction-debt: {len(debts)} UNREGISTERED RETRACTION(S) "
              f"— a row that was never written is invisible to every gate that reads rows --")
        for d in debts:
            print(f"    {d}")
    return 1 if debts else 0


if __name__ == "__main__":
    sys.exit(main())
