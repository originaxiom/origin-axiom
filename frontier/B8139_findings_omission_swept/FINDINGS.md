# B8139 — the FINDINGS.md omission, and why a lock that works caught nothing for five days

**Arc dated:** 2026-08-26 · **Seat:** cc3 (audit) · **Lane:** PROCESS.
**Gate 5:** no physical identification; nothing here touches CLAIMS.md.

## The finding

**This seat stopped writing `FINDINGS.md` at B8110 and the omission ran unbroken through B8134 —
sixteen consecutive arcs, five days, all of them mine.**

The lock that catches this
(`test_b817_wave2::test_writer_safety_no_verdict_without_a_findings_document`) **exists, works, and
was never weakened.** It simply was never *reached*: it lives in a suite of **1038 files and 4528
tests whose collection alone takes 421 seconds**, and two background runs were killed by timeout
before finishing. The first reached 73%.

> **A lock nobody can afford to run is not a lock.** The failure mode here is not a missing check,
> not a silent pass, and not a weakened assertion — it is **cost**. That is a distinct class and it
> deserves its own name, because every remedy for the other three is useless against it.

## How it surfaced

Drafting the four series papers forced a full-suite run. **The run was killed at 73% — but it had
already emitted five `F`s, and reading the killed run's partial output instead of discarding it is
what exposed them.** A killed run is not a run that told you nothing.

## The five failures, triaged

| # | failure | whose |
|---|---|---|
| 1 | `instrument` banked as a **string**; the schema is a **bool** (928 `False` / 96 `True`) | **mine, new** |
| 2 | 16 arcs with a verdict and no findings document — **I added 4 more** | pre-existing **+ mine** |
| 3 | two verdicts outside the sealed vocabulary (`B8068`, `B8080`) | pre-existing, **my seat** |
| 4 | 6 `NEGATIVE` arcs unrouted in the kill graph | pre-existing |
| 5 | `atlas-fresh` broke **because of my fix** to (2) | **mine, caused by the fix** |

## What was done

- **20 `FINDINGS.md` written** (16 reconstructed + my 4 new). Every reconstruction is generated from
  its own arc's banked record and **carries a header saying it is not contemporaneous.** Nothing is
  backdated.
- **Two verdicts normalised** into the live vocabulary: `B8068` → `PROVED`, `B8080` → `NEGATIVE`.
  **`PARTIAL` was considered and rejected** — it is in wave-2's vocabulary but not wave-1's, *and it
  is used by zero arcs*; the live vocabulary is exactly four tokens across 1026 arcs, so normalising
  into it beats widening a lock. **Both originals preserved** in `verdict_original` with a stated
  rationale.
- **7 `NEGATIVE` arcs routed** to the kill graph on B836's convention, with the judgement fields
  **deliberately unset** — setting `fact_computed` mechanically would fabricate the exact signal it
  exists to carry. (`B8080` became the 7th once its verdict was normalised.)
- **Atlas and views regenerated**, never hand-edited, since `views-generated` byte-compares.

## Suite coverage actually achieved

The full suite cannot complete in a session, so it was run in slices: **0–73%** from the killed
run's partial output, **62–82%** re-run, **80–100%** in four chunks. Three failures remain, **all
pre-existing**: two trace to the six standing gate debts, and the third is
`SUBMISSION_METADATA.md` carrying the owner's contact email.

## ⚠ Flagged for the owner, not touched

**`papers/structure_paper/SUBMISSION_METADATA.md` contains a personal email address on a tracked,
dual-pushed surface, and a lock exists specifically to keep email-shaped text off that surface.**
It is the owner's own address, supplied deliberately on 2026-08-15 for arXiv. Removing it would
undo a deliberate act and could break the submission; leaving it unmentioned would suppress a
privacy-relevant conflict between a decision and a standing lock. **So it is flagged and left
alone.**

## SCOPE

- **The suite cost is NOT fixed.** This arc is a sweep, not a remedy. The same drift class can
  recur, and will, unless the suite becomes runnable.
- The reconstructed documents are **faithful to the banked record but not contemporaneous**, and
  each says so in its own header.
