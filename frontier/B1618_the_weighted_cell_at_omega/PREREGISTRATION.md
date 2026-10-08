# B1618 — PREREGISTRATION: THE WEIGHTED CELL AT ω — given τ = ω, do modular-form Yukawas of any weight give anything but degenerate masses at ω?

cc (main), 2026-10-08, after S95. B1617 (given τ = ω, the owner's tagged postulate) found degenerate masses for weight-0
vacua and left owed the weighted case: a Yukawa of weight k at the fixed point lies in an eigenspace of the stabiliser U
at the automorphy phase, not in the invariant line. **Sealed before `weighted_at_omega.py` runs.** No data is read. A
READING throughout ("given τ = ω", "given Λ"). 0 of 19.

## Seen first

`VERDICT topic-sweep /weight|automorphy|elliptic fixed|modular form|degenerate mass|inner automorphism|parity grading/: 82 of 1389 arcs on main match (NEGATIVE 11, OPEN 6, PROVED 65)` — B1617 (the residual group at ω; the inner automorphisms as the parity signs; U's eigen-turns on T), B1615,
B1616, W20/W21 (the Hodge-line weights); the audit (codex) lane at `f5da7ce4a`, read at headline level: one supplied curved E₈ action admits a stable stationary S(U(3) × U(2)) gauge vacuum with zero charged index, and its magnetic family is unstable for every non-zero flux. **Literature:** modular forms at elliptic fixed points (a form of weight
k ≢ 0 mod 3 vanishes at ω; the automorphy factor of U at ω is a sixth root of unity); the near-fixed-point mechanism —
cited from the reviewer's knowledge.

## Disclosed

- **The outcome was argued before the seal (in conversation, 2026-10-08):** the inner automorphisms fix every τ with
  automorphy factor 1 and act on the matter as the parity signs, so a coupling that is a function of τ lies in their fixed
  subspace — the diagonal in T's three parity lines — at every τ and every weight; U cycles the three lines, so every
  eigenvector of its action on that diagonal has entries of equal modulus: degenerate masses at ω for every weight; near ω
  the relation propagates order by order, giving equal orders of vanishing and equal leading moduli. The arc checks the
  linear algebra exactly; the near-ω statement is a lemma whose input (U a 3-cycle on the lines) is checked.
- The instrument was repaired before the seal (T's parity lines from the joint eigenbasis of both inner lifts).
- All 24th roots of unity are scanned, which covers every integral and half-integral weight of matter and coupling.

## Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **Q1** | the subspace fixed by the inner automorphisms and the sign is three-dimensional in T̄ ⊗ T and in Sym² T — the diagonal in T's parity lines — and U preserves it | 85% |
| **Q2** | for every 24th-root phase the U-eigenspace on it is at most one-dimensional, and every eigenvector gives three equal masses — **degenerate at ω for every weight** | 85% |
| **Q3** | U permutes T's three parity lines as a 3-cycle (the input of the near-ω lemma: equal orders of vanishing, equal leading moduli — quasi-degenerate near ω) | 90% |

**The reading, written before the run (the cells can only lower it).** If Q1–Q3 hold: **given τ = ω, the weave allows no
hierarchy at ω or near it, for any weight** — the inner automorphisms make every mass matrix diagonal in the parity lines
and U forces the three entries to equal size. The owner's tagged postulate τ = ω (which main recommended) then cannot be
the source of the observed hierarchy within the weave. A hierarchy among diagonal entries needs a point where the three
parity sectors behave differently — the cusp, where the half-period characteristics separate (powers q^{1/8}, q^0) —
which would be a different postulate for τ, the owner's to make.

## Instruments

`verification/weighted_at_omega.py`; hashes in `ARTIFACT_HASHES.txt`.
