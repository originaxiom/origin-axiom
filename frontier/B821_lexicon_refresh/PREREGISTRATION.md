# B821 — PREREGISTRATION: the lexicon refresh (sealed before any edit to LEXICON)

cc banking seat, 2026-07-30. **Sealed and committed BEFORE the lexicon is touched.** This moves
every atlas figure, which is why it gets its own seal rather than riding inside a correction commit.
Gate 5 absolute: repository-instrument scope, no physical value, nothing to `CLAIMS.md`.

## The diagnosis this acts on (computed, read-only, before sealing)

21 arcs match zero motifs. They split by **size**, and the split is clean:

| group | n | FINDINGS size | reading |
|---|---|---|---|
| thin stubs | **14** | 409–1988 bytes | *"Logged observation, not a claim."* Blind because there is almost nothing to match — **correctly** invisible |
| substantial | **7** | 2523–5854 bytes | at or near the **4078-byte corpus median** — a genuine gap |

The 7: `B537 B679 B770 B793 B798 B818 B819`. **Six of the seven are about the programme's own
machinery** — gate reports, closure censuses, solver architecture, falsifier power/budget, verdict
vocabulary, coverage frames. The lexicon's 29 motifs cover the **object** and the **method**, and
**none covers the programme examining itself** — which is exactly the work that has dominated
recently, and is why recent arcs go blind at 12.2 % against 2.3 %.

## What will be changed

1. **One new motif**, for the self-audit / instrument layer: `conserved="tool"` (our own method, so
   its recurrence is a **selection effect**, never a first integral — the existing `tool` semantics
   apply exactly).
2. **The gate's metric is restricted to substantial arcs** (`FINDINGS.md` ≥ 2000 bytes). A count
   inflated by 14 permanent stubs cannot distinguish a rotting lexicon from an archive of short
   notes, and the stubs will never match anything no matter how good the lexicon becomes.

## Two-outcome criteria, fixed here and not adjustable afterwards

**SUCCESS** — both must hold:
- the new motif matches **≥ 5 of the 7** substantial blind arcs; **and**
- it matches **≤ 25 %** of the whole corpus.

**FAILURE** — either:
- it matches **< 5 of 7** → the motif is not the missing one; revert, and the gap is re-diagnosed; **or**
- it matches **> 25 %** of the corpus → it is a **catch-all**, which is worse than a gap: a motif
  matching everything carries no information and would make the atlas *look* healthier while
  telling a reader less. **Revert.**

The 25 % ceiling is the vacuity check, per `PRACTICES`: *check the criterion can pass AND can fail.*
A motif engineered to catch the 7 by matching everything would satisfy the first clause and must be
rejected by the second.

## Declared in advance

- **B537 is expected NOT to match** — it is the one of the seven that is not about the programme's
  machinery (a classical-surface result). If the new motif catches it too, that is evidence the
  patterns are too broad, and it is recorded as such rather than counted as a win.
- **The 14 thin stubs are expected to stay blind, and that is the correct outcome.** Any change that
  makes them match would mean the patterns are matching boilerplate.
- I expect SUCCESS. Recorded so the outcome cannot be softened afterwards.

## What this does not do

It does not re-ground the lexicon in K023–K025, and it does not revisit the other 29 motifs. Those
are separate and larger. **This closes one named gap and improves one metric; it is not the full
re-grounding B806 called for**, and must not be reported as such.
