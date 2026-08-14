# B982 — the file-drawer lock's exemption list is partly unearned, and three exemptions rest on a numbering collision

**Date:** 2026-08-09 · **Seat:** cc (banking) · **Lane:** repository governance. Gate 5 untouched.
**Origin:** cc3's *Accounting of the 573* flagged B452/B501/B502/B503/B506 as *"`PREREGISTRATION.md`
only — sealed, unreported."* This seat's first check was **wrong**: it observed that all four sit in
`SEAL_LEDGER.md` and that `test_b837_file_drawer.py` passes, and treated that as reassurance.
**The lock passes because they are on an allowlist.** cc3's flag was right.

---

## The defect

`tests/test_b837_file_drawer.py` exempted **twelve** sealed-and-ledgered preregs from the reporting
obligation, under one comment:

> `# the 12 audited as REPORTED in a successor arc's findings (B837)`

**B837's `FINDINGS.md` names five of them.** Computed here:

| | |
|---|---|
| exempted as audited by B837 | B452, B473, **B501**, **B502**, **B503**, **B506**, B565, B568, B570, B580, B634, B652 |
| **actually named in B837's findings** | **B452, B568, B580, B634, B652** — five |
| **exempted with no mention in the cited audit** | **B473, B501, B502, B503, B506, B565, B570 — seven** |

## Worse: three of the seven were exempted on a NUMBERING COLLISION

`B521_audit_integration` states it in its own text:

> *"**B493–B503 collides with this trunk's B496–B503**"*

The arcs B521 cites are the **audit seat's** — `B501_gateB_reductions`, `B502_gateC_commensurator`,
`B503_tower_timebox`. Main's are `B501_universe_word`, `B502_parity_signature`,
`B503_external_contact`. **Different arcs. Same numbers.**

> **The exemption was granted on citations to another seat's arcs that happen to share numbers.**

This is the repo's own **`cited-as-sufficient`** kill form — occurring **inside a governance gate
whose entire purpose is to prevent it**, which is why the lock reported green over genuine
file-drawer entries. It is also the exact failure the parallel-seat rule warns about:
*integrate-don't-merge*, because the numbering ranges collide.

## Dispositions, one per arc

| arc | disposition |
|---|---|
| **B501** `universe_word` | **GENUINE FILE-DRAWER.** Its only citation is a **forward pointer** in **B500** — *"B501 (stationary measure = which fields a typical history births)"* — and **B500 precedes it**. No outcome reported anywhere. |
| **B502** `parity_signature` | **GENUINE FILE-DRAWER.** Same forward pointer in B500; the B521 hit is the colliding `B502_gateC_commensurator`. |
| **B503** `external_contact` | **Not a file-drawer entry, and not audited either.** Its own sealed text is **owner-gated**: *"Send = owner's hand only"*, *"fires only after the Closure Campaign's package merges."* Correctly unfired. It is owed a **disposition record**, not an exemption — the pattern B913 already established. |
| **B506** `critical_cancellation` | **GENUINELY REPORTED — but not by B837.** `B507_beta_function` engages its content directly: *"the B506 emergent drift has its SOURCE here"*, *"the B506-d consistency lock"*. The exemption is right; its **citation** was wrong. Corrected. |
| **B473, B565, B570** | Cited in successor findings but **not line-checked here**. Recorded as `UNVERIFIED_EXEMPTIONS` — **a named debt, not a clean pass.** Marking them verified without reading would repeat this arc's own finding. |

## The correction applied

The single comment is replaced by four explicitly-labelled sets, each carrying its real basis:
`KNOWN_UNREPORTED` (unchanged), **`UNREPORTED_FOUND_BY_B982` = {B501, B502}**,
**`DISPOSITION_NOT_REPORT` = {B503}**, `REPORTED_ELSEWHERE = {B506: B507_beta_function}`, and
**`UNVERIFIED_EXEMPTIONS` = {B473, B565, B570}** as a standing debt.

## The lesson, which is the day's lesson at gate level

**A gate is only as good as the provenance of its exemptions.** Every allowlist entry must name the
document that discharges it, and that document must actually contain the arc. An exemption whose
justification cannot be grepped is a silent hole — and a hole in a governance gate is worse than the
same error in an arc, because it reports green.

**Second-order note:** the parallel-seat numbering collision is a live hazard, not a historical one.
Any future audit that matches arc IDs across seats without checking the arc **name** will reproduce
this exactly.
