# B1244 — THE GATE 5 AUDIT: pre-registration, sealed COLD

**Written 2026-09-03, BEFORE any item is evaluated and BEFORE the trinification material is
examined against the criteria.** The occasion for this audit is a downstream seat's measured-data
result (M_I ≈ 10^13 GeV from α₁ = α₂ running). That is exactly the circumstance in which a filter
gets loosened for a reason nobody notices, because the result looks good. Hence: criteria and
enumeration rule fixed and sealed first; evaluation second.

## 0. What this audit is NOT

It **sorts; it does not cross.** No item in this audit fires a comparison against measured data.
An item that PASSES becomes *eligible* for a crossing cell — which remains RED, owner-only, and
still requires its own seal. Nothing here promotes anything to `CLAIMS.md`.

## 1. The standing rule this audit applies (owner, 2026-07-12, verbatim in force)

> The firewall blocks **OVERCLAIMS, not PHYSICS**. It is a quality filter, not a prohibition.
> "we need to make sure firewall isn't blocking us from reaching concrete results on physics."

The five conditions a physics step must satisfy to pass:

1. the math behind it is **computed and proven** (not asserted, cited, or posited)
2. the claim is **exactly what was computed** — no inflation, no "this means X"
3. the **discriminating fact is in hand** (not deferred to a specialist, not theory-indicated)
4. the claim is **falsifiable** — a concrete computation could refute it
5. it is **not numerology** (not "this number = that number therefore physics")

## 2. Enumeration rule (mechanical, so the set is not my choice)

An item enters the audit iff, in a tracked `.md`, a **Gate-5 token** (`Gate 5`, `Gate 5-Q`,
`firewall`) occurs within **±3 lines** of a **fence token** (`fenced`, `held`, `HOLD`, `deferred`,
`not claimed`, `does not promote`, `no value promotes`, `absent`, `waits on`, `blocked`).
Every hit is an item, keyed by `(file, line, arc-or-lead-id if present)`. Duplicates of the same
underlying claim are merged and the merge is recorded. **The instrument that enumerates is written
and its output committed before any verdict is assigned.**

## 3. Verdicts (exactly three; no fourth, no "interesting, continue")

| verdict | meaning | what must be recorded |
|---|---|---|
| **PASSES** | all five conditions hold | which computation satisfies each of 1–5 |
| **HOLDS** | at least one condition fails | **the failing condition, by number** |
| **MISLABELED** | never a Gate 5 matter — the fence names the firewall for something that is not a scale/time/dynamics claim | what it actually is, and where it should sit |

A HOLDS verdict that does not name a numbered failing condition is not a verdict and is rejected.

## 4. Pre-registered expectations (so the audit can embarrass me)

Recorded now, checkable after:

- **E-1.** The MISLABELED pile is **non-empty**. Predicted ≥ 3 items.
- **E-2.** **C43 is MISLABELED.** Its "the desert is dead as a mechanism" is stated as a fact about
  the object; it looks like a fact about the desert configuration, which fails for every non-SUSY
  GUT without an intermediate scale. *If C43 comes out HOLDS or PASSES, E-2 is wrong and is
  recorded as wrong.*
- **E-3.** The PASSES pile is **small** — predicted ≤ 5 of the enumerated items. If PASSES comes
  out large, the likeliest explanation is that I loosened the criteria, not that the record was
  massively over-fenced; a large PASSES pile triggers a re-read of §1 before anything is released.
- **E-4.** No item passes on condition 3 (discriminating fact in hand) by pointing at a *literature*
  computation rather than an on-bench one. Any that does is HOLDS.

## 5. Kill condition for the audit itself

If applying the five conditions requires reinterpreting any of them, the audit **stops** and the
reinterpretation goes to the owner before proceeding. The criteria are not to be adjusted mid-run.

## 6. Order

Enumerate → assign verdicts item by item → tally against E-1..E-4 → report. The trinification
material is examined **last**, after every pre-existing item already has a verdict.

---

## AMENDMENT A1 — 2026-09-03, owner instruction, BEFORE any item is evaluated

> "verify all records when getting ready for gate5. never be called on data you dont verify
>  first, experience proved that they might be missinformed"

**Adopted as a binding condition of this audit, and it is stronger than condition 3.**

**A1. No item may be given a verdict from its own description.** For every enumerated item the
auditor must open the SOURCE — the arc's FINDINGS/verification, not its `claim_one_line`, not a
log entry, not another seat's summary — and confirm the fenced claim says what the fence says it
says. An item whose source cannot be opened is **HOLDS**, failing A1, regardless of its merits.

**A1(b). A citation inside an item is not evidence.** If an item's fence rests on a quoted line
from another arc, that line is located in the corpus before the item is graded. A quote that
cannot be located makes the item HOLDS and the missing quote is recorded.

**Why this is not paranoia — three instances in one session, all with authority attached:**
1. **C25** asserted the second measurement lands on the SM algebra "EXACTLY" while citing the arc
   whose own banner says that overstates by two abelian factors. Two downstream seats inherited it.
2. **The main seat (me)** graded another seat's T17 as "rests on a REFUTED identification" from a
   third seat's one-line summary, never opening T17 — which fences that very refutation in its own
   docstring. The wrong grade was accepted downstream within the hour (E58).
3. **A downstream seat** attributed a verbatim "scope line" to B1011 that does not exist anywhere
   in the corpus — searched tracked files of every type, then the whole disk, then loose variants.
   Zero hits. It was the load-bearing support for that seat's answer to the owner's question.

Each arrived as diligence. **A correction issued with more confidence than its verification
supports is not a fix; it is a swap of one unverified claim for another, and it is harder to catch
because it wears the clothes of a fix.** A1 makes opening the source a precondition of a verdict,
not a courtesy.

**A1(c). The auditor's own prior counts as unverified data.** Expectations E-1..E-4 above were
written before enumeration; they are predictions to be scored, never reasons to grade an item.
