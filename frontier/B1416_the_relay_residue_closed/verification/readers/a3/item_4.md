# Item 4 — "the trigger needs a second surface for non-merging seats"

Source:
`<home>/origin-axiom/audit/wt-braver/CC3_TO_CC_2026-08-12_REVIEW_INPUT_THE_AUDIT_SEAT.md`.

## HEADLINE (verbatim)

*"⚠ WHY THIS SEAT HAS NEVER TRIGGERED A REVIEW: the trigger is merge-count, and this
seat does not merge ... RECOMMENDATION: the trigger needs a second surface for
non-merging seats — commits-on-branch, or relays-dispositioned, or arcs-influenced. Pick
any; the point is that one surface cannot see every seat. The cloud seat's 62-vs-20 is
the same gap from the other side."*

## WHAT TRIGGER, WHAT SECOND SURFACE

The trigger: the decadal review cadence (fires nominally every ~10 merges — cc3 measured
R44 firing at 25 merges) is keyed to **merge count into main**. Measured at the time: the
`audit/b775-braver-questions` branch had 2424 commits, 176 that window, **zero merges
into main**, so the merge-count trigger structurally cannot see this seat's practice
(only its *findings*, harvested piecemeal, get reviewed — 81 mentions in `REVIEWS.md`).
The recommendation: add any non-merge surface — commits pushed to the branch,
relays dispositioned, or arcs the seat's work influenced — so a seat that legitimately
never merges (by the standing "seat branches never merge" governance rule) is not
therefore invisible to the review cadence.

## COMPUTED / CITED / ASSERTED

**ASSERTED** as a governance/process recommendation, backed by measured counts (2424
commits / 176 this window / 0 merges / 81 REVIEWS.md mentions) that are themselves
CITED as evidence, not fresh sandbox computation. This is process design, not mathematics
— appropriately, cc3 frames it as "input, not a review."

## ON MAIN ALREADY?

**YES — implemented, and the implementation names this exact seat.**
`scripts/checks/harvest_debt.py` (landed as **B1307**, 2026-09-09 —
`docs/CAMPAIGN_STATUS.md:37`, "THE HARVEST GATE: THE SEAT BRANCHES ARE COUNTED THE HOUR
THEY ARE PUSHED") is precisely a second, non-merge-count surface: its docstring (lines
1-26) states the rule as "every seat branch is READ within 21 days of a push, and every
seat item has a ledger row," and it reports, per seat, **NEW** (paths changed since the
last-read pin), **BACKLOG**/**STALE** (index items vs. ledger rows — "commits-on-branch"
+ "arcs-influenced" reconciliation), **RELAYS** (relay files with no `RELAY_LEDGER` row —
"relays-dispositioned," cc3's own second suggestion, verbatim), and **MIRROR** (origin
vs. codeberg lag). `--strict` gates `gates.py review-due`
(`scripts/checks/harvest_debt.py:25`, `docs/PRACTICES.md:84,639`), so the review cadence
itself now opens on this debt, not on a bare merge tally.

**The seat this relay is about is literally in the gate's seat list:**
`scripts/checks/harvest_debt.py:67-68` — `dict(key="braver", label="cc3 (braver-questions
branch)", branch="b775-braver-questions", ...)`. It is tracked by pushes/relays, not
merges, exactly as recommended. `docs/SEAT_REGISTER.md:4` (2026-09-15 rule change, owner-
approved) further formalizes the underlying model: *"'Seat branches never merge' applies
to seats with their OWN numbering ... they are HARVESTED, item by item"* — vs. lanes that
share main's numbering, which DO merge. This resolves the structural tension cc3
diagnosed (a merge-based trigger applied to a governance rule that forbids merging) by
making harvest — not merge — the seat's unit of review-visibility. The braver branch
itself was subsequently retired 2026-09-15 (`docs/SEAT_REGISTER.md`'s retirements line:
`archive/braver-questions@53da05f6`, tag+delete on both remotes) after B1412's harvest
met the gate.

**CONTRADICTED (partially): `docs/RELAY_LEDGER.md:323`** (this repo's own tracking row
for this relay) says: *"OPEN — the specific recommendation ('the trigger needs a second
surface for non-merging seats') has no confirmed adopted fix on main ... no dedicated
main text found addressing the merge-count review-trigger gap itself."* This appears to
be a search miss of the same kind as item 1's: `docs/CAMPAIGN_STATUS.md:37`'s own B1307
entry states the harvest gate's purpose in almost cc3's own words ("the seat branches are
counted the hour they are pushed") and the gate's SEATS list names the braver branch by
its own key. A `grep -rn "harvest_debt\|non-merging\|counted the hour" docs/
scripts/checks/` finds it directly.

## NEEDS COMPUTATION HERE

DOCUMENTARY. No arithmetic is owed — the fix already exists and runs (`python3
scripts/checks/harvest_debt.py` reads live remote-tracking refs; not re-run here per the
~2-minute bound and no-tracked-file-edit rule). The only outstanding action is
correcting `docs/RELAY_LEDGER.md:323`'s row from OPEN to SUPERSEDED, citing
`scripts/checks/harvest_debt.py` (B1307, 2026-09-09) and `docs/SEAT_REGISTER.md`'s
2026-09-15 rule change by name.

## GRADE PROPOSAL

**SUPERSEDED.** The recommendation is not merely addressed in spirit; the concrete gate
implements two of cc3's three named alternatives (relays-dispositioned via RELAYS,
arcs-influenced via BACKLOG/STALE) plus a fourth cc3 didn't name (mirror lag), gates the
review cadence itself, and lists the very seat that raised the issue as a tracked entry.
**DISPUTED against `docs/RELAY_LEDGER.md:323`**, which still marks this OPEN as of the
2026-09-15 escalation — that row should be corrected.
