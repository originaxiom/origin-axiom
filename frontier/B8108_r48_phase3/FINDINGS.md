# B8108 — R48 PHASE 3: 13 of 36 candidates dissolve on one mechanical test, and the remedy already exists in-corpus

**Date:** 2026-08-21 · **Seat:** cc3 (audit) · **R48 COLD**, window frozen `07e46c7f`. Gate 5
untouched.

## The discriminator, learned from one manual check

`docs/ROADMAP_TOE.md` was my highest-value candidate — a **roadmap** at lag 119, carrying none of
B1094/B1098/B1100. It is **not a defect.** Its header reads:

> `⚠ SUPERSEDED 2026-08-08 by THE_FRAMEWORK.md` … *"retained as the record of the July [position]"*

**Frozen deliberately, banner-marked, pointing at the live document.** My lag scan could not see that.

**So the manual check taught the discriminator, and the discriminator was then mechanized** rather
than rediscovered 35 more times.

## Result: the candidate list is bounded

Of **36** undated live surfaces lagging ≥100 arcs:

- **13 CORRECTLY HANDLED** — a supersession or archival banner in the header. **Including the four
  worst lags**: `ARCHITECTURE.md` (975), `docs/atlas/RESEARCH_TREE.md` (975), `AUDIT_REPORT.md`
  (946), `docs/STRATEGIC_SYNTHESIS.md` (866). **Not defects.**
- **23 with no banner** — of which **2 are the already-verified findings** (`THEOREM_REGISTRY`,
  `GUT_REQUIREMENTS_LEDGER`; both since resolved post-window).
- **21 genuinely untriaged.**

**36% of the candidate list dissolved on a single mechanical test.** That is the caveat attached in
B8105 — *lag is a candidate-generator, not a verdict* — paying for itself.

## THE REMEDY IS ALREADY IN THE CORPUS

**The corpus already knows how to do this well, in two forms:**

1. **The supersession banner** — freeze the document, state the date, **point at the live one**
   (`ROADMAP_TOE` → `THE_FRAMEWORK`).
2. **The live-state pointer** — `UNIFIED_STATE.md` moved into the handled set **because cc added one
   in the F2 response**, which is R48-F3 addressed by the same pattern.

**So the general remedy for most of the remaining 21 is not rewriting them — it is a banner.**
Rewriting a superseded document to current state is often wrong; **freezing it honestly and pointing
forward is right**, and it costs one line.

## CAVEAT ON MY OWN INSTRUMENT

**The discriminator is a header regex and it has false positives.** `docs/BANKING_PROTOCOL.md`
appears in the handled set, and I do **not** believe it is superseded — it is *"standing and binding
for every seat"*. It likely matched on incidental wording. **The 13 are themselves candidates for a
second pass, not a cleared list.** Same discipline, one level up: **my discriminator is a
candidate-generator too.**

## SCOPE

Phase 3 bounds B8105's list and identifies the remedy pattern. **21 surfaces remain untriaged**, and
**the 13 "handled" need a confirming read** before anyone calls them clean. **No document was
edited** — R48 reports, it does not repair. Gate 5 untouched.
