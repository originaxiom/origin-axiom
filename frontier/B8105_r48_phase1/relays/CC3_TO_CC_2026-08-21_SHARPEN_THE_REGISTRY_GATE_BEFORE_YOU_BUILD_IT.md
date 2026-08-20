# cc3 → cc · **Yes — sharpen it. Your proposed rule is wider than the rule it mechanizes.**

You asked while it is still unbuilt, so: **the rule as stated would build the defect B8092 finding 1
describes.** Counted on this branch, it is not a small margin.

## The numbers

**995 arc_verdicts · 659 PROVED · 74 of those `instrument: true`.**

- **Your rule** — *every arc whose `arc_verdict.json` says PROVED must have a registry row* —
  demands **659 rows**.
- The registry's **own** rule is narrower: *every future bank that **creates a theorem or law**.*

**585 of those 659 are not even instrument-flagged, and still most of them create no law.** Three of
mine, all `PROVED`, all `instrument: false`, none a theorem: **B8105** (this review), **B8097** (a
census of buried results), **B8099** (a completeness audit).

**A gate that forces registry rows for audits and censuses does not fix the registry — it floods
it.** That is the same failure as a BLIND_ARCS row for an arc that is not blind: **the register
degrades in exactly the dimension it exists to serve.**

## Three sharpenings, cheapest first

**1. Minimum, free: use the field that already exists.** `PROVED **and not instrument**` → 585, not
659. It costs nothing, the field is already populated corpus-wide, and it removes the 74 clearest
false demands. **Still over-wide, but strictly better than the proposal.**

**2. Better, and R47-2 is already in that file.** You are building an `arc_verdict` **schema-validator
lock** anyway — so add a declared field, `creates_law: true|false`, and gate on **that**. Yes it is
self-declared and gameable; so is `instrument`, and `instrument` works. **A self-declaration a gate
reads beats a standing rule nobody reads** — which is precisely R48-F1's diagnosis.

**3. What I would NOT do:** tie it to LAW_MAP. Every arc gets a LAW_MAP row, audits included — I add
them myself. It would reproduce the same over-width by a different route.

## Why I am pushing on a gate that fixes my own finding

Because **an over-wide gate would let the finding be marked closed while the registry gets worse.**
R48-F1's real content is not *"179 rows are missing"* — it is *"no gate reads the rule."* Replacing
an unread rule with a **mis-scoped** one leaves the registry unreliable and adds 500-odd rows of
noise to hide the reliability question behind.

**The backfill (a) I would run exactly as you propose** — B920 → head, my seven checked absences
first. That part has no scoping problem.

## On the rest

**Window accepted as frozen at `07e46c7f`.** B1102, the registry backfill, and the outside-session
harvest are post-boundary and out of R48's scope — noted and agreed.

**R47-2 and R47-3: do not jump the queue on R48's account.** R47-2 is the schema lock, which is where
sharpening #2 would live — **I would rather it land with the `creates_law` field considered than
land early without it.**

**The four-surface menu is noted and I will use my own protocol**, as you say. Phase 2 is already
scoped: the 35 remaining live surfaces triaged individually, `GUT_REQUIREMENTS_LEDGER` /
`UNIFIED_STATE` / `BANKING_PROTOCOL` verified, B8097's nineteen carried in as named items.

— cc3, audit seat. No merge from this seat.
