# xB002 — DESIGN (SEALED POST-HOC; labelled, per WORKING_RULES §3)

**Honest provenance, stated first.** The computations under this arc were run during an
adversarial review session BEFORE this design was written. WORKING_RULES §3 requires the seal
before the first run and requires late seals to be **labelled post-hoc**. This one is. Nothing
here may be read as pre-registered, and the seal certifies integrity only, never chronology —
the same limit the verification package's own README states.

## Purpose

Pay two debts that `docs/THE_LADDER.md` X15 ranks (1) and (2) and records as **"still unwritten
as of B1101"**: the scope-correction notes for **L1** (the object's own selection) and **L54**
(gate A's quantifier). B8097's finding stands behind both: *"noticing has been treated as
discharging. A row that says this is a debt is not payment."*

## Two-outcome criteria, declared

| cell | criterion | PASS | FAIL |
|---|---|---|---|
| 1 | separator set over the ℚ(√−3) shape-field family at ≤ 6 tetrahedra | exactly `['h1_is_Z']` | any other set — L1's corrected statement would be wrong |
| 1b | family size at that bound vs B1136's banked 14 | either agrees (14) or the discrepancy is explained exactly | an unexplained discrepancy stops the arc |
| 2 | family members at non-integer volume ratio to m004 | at least one — a cover census cannot reach the class | none — L54's §3 argument would collapse |

Both criteria can pass and can fail on the instance (WORKING_RULES §8): cell 1 fails if any
second property separates or if no property does; cell 2 fails if every family member sits at an
integer ratio.

## Conventions declared (WORKING_RULES §4)

- **Census.** `snappy.OrientableCuspedCensus()`, bounded by `num_tetrahedra() <= 6` — a
  *tetrahedron* bound, stated, not a census-index bound.
- **Shape field.** All tetrahedron shapes quadratic over ℚ with squarefree discriminant −3.
  Coefficients bounded by 10⁴ and residual < 1e−11 (snappy's default shapes carry ~1e−16, so the
  bar is set above the noise and below any plausible spurious fit).
- **Cusp-trivial group.** Smith normal form of the relator matrix with the peripheral words
  adjoined — i.e. `H₁(M)/⟨image of the peripheral subgroup⟩`.
- **Amphichirality.** `SymmetryGroup.is_amphicheiral()` (orientation-aware).
- **Cover test.** Volume ratio to m004 integral — a *necessary* condition only, used one way.

## Scope, declared

Scope notes, **not reopenings**. No banked result is withdrawn by this arc. No SM quantity enters
(Gate 5 untouched: pure topology). No value, no generation count.
