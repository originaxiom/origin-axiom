# B913 — R3c, the cone-respecting colored magnitude: **DISPOSITION RECORD**

**Date:** 2026-08-05 (sealed) · **Disposition recorded:** 2026-08-07 · **Seat:** cc
**Seal:** `8afdc2f88c55bd36818748acb13c8b61a770d18906e2b2c030b47ac05770879a`
(`docs/SEAL_LEDGER.md` line 479)

---

## Why this file exists, and why it is not a FINDINGS

The file-drawer lock (`tests/test_b837_file_drawer.py`) requires that **every
sealed, ledgered preregistration ends in either a reported result or a recorded
disposition.** B913 has no result to report, and that is not an omission — it is
what the cell sealed itself to be:

> **This design seal is the cell's entire content; no computation follows under
> this ID.** (PREREGISTRATION.md, §Files, verbatim)

This is the disposition record. It closes the obligation without inventing a
computation that was never run. It is deliberately **`VERDICT.md`, not
`FINDINGS.md`**: the arc asserts no proposition, so it takes no entry in the
`PROVED / NEGATIVE / OPEN / RETRACTED` vocabulary — and stretching one of those
labels to cover a design decision would be exactly the verdict-vocabulary drift
the wave-1 lock exists to catch.

## What B913 decided

A **choice**, made and frozen *before* any colored ratio existed, so that it
could never be retrofitted to a wanted answer. B912 had proved the six colored
atoms carry **Lorentzian (1,2,0)** Grams under the canonical H, so R3′ needed a
magnitude that respects the cone instead of pretending definiteness.

**The sealed choice: |det Gram|^{1/3}, with the (1,2,0) signature carried
alongside as a mandatory tag** — every colored ratio reported as (magnitude
ratio, signature pair). The stated rationale, fixed at seal time: it is the one
candidate already fully computed, basis-invariant, and requiring **zero further
construction** — each further construction being a fresh place for unintended
freedom, which is the drift rule applied to the mathematics itself.

The two rejected candidates (the compact-direction restriction; the polar/
singular spectrum) were **not** discarded as mathematics. They were registered
as future refinement cells **gated behind R4**, explicitly so that the crossing
could not be tuned by magnitude-shopping.

## Where it was consumed

**B914** (R2′+R3′). Its FINDINGS names the seal in its opening lines and honors
the no-substitution clause throughout:

> "B913-sealed magnitude |det Gram|^{1/3} with mandatory (1,2,0) signature tags
> — **no other magnitude appears anywhere in this cell**."

and records the three colored pairs as magnitudes-with-tags rather than as
scales (1867.6882465…, 702.46…, 451.72…, each ×2), with the colored sector
entering descriptively only and **no colored ratio** formed. The design did the
work it was sealed to do: it removed a degree of freedom from R3′ and from the
crossing that followed.

## Status of the deferred candidates

Still gated. Candidates 2 and 3 may be run **after** the crossing, each as its
own sealed cell, and **compared against — never substituted into — the R4
verdict.** That gate remains binding; R4 (B915) has since fired, so these are
now runnable as refinement cells under their own seals.

---

**Disposition: DESIGN-ONLY, CONSUMED.** No computation was performed or is owed
under this ID. The obligation the seal created is discharged by B914's use of
the choice, and by this record.
