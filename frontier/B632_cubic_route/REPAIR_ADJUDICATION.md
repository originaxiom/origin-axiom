# B632 cell 2 — THE REPAIR ADJUDICATION (audit Gate 0; 2026-07-15)

**Trigger: the external read-only audit (oaudit2 WALL_DIAGNOSIS
2026-07-15) found the repair TRAIL deficient even though the final
mathematics passed its exhaustive verification (162/162 coboundary
descent checks, external). This document supplies the adjudication the
trail lacked. Per the hashed-errata house pattern (L85 V1′/V3′).**

## The run history, restored verbatim

1. **FAILED_RUN_1.txt** (recovered byte-faithfully from the session task
   record; sha bc517ead…): the first run crashed at the V(16)
   highest-vector step — the code filtered `nullspace(h−T·I)` basis
   vectors individually for `e·v = 0`, which fails when the eigenbasis
   returned is not e-adapted. REPAIR 1: the stacked-kernel construction
   ker(h−T·I) ∩ ker(e) (dimension exactly 1 at T = 16, 8). This repair
   is convention-neutral (it computes the same mathematical object by a
   correct method) and happened BEFORE any outcome-bearing value
   existed.
2. **FAILED_RUN_2.txt** (recovered byte-faithfully; the run whose
   transcript the green run later overwrote — the audit is right that
   overwriting was a hygiene failure): the naive bar-cocycle 2-cell
   evaluation produced nonzero diagonal self-cups, antisymmetry
   [True, True, False], and a FAILED coboundary-invariance control.
   These gate failures were sealed in CELL2_PREREGISTRATION.md before
   the run; they fired exactly as designed. REPAIR 2: the
   inverse-letter comparison chain (for each x_i = ℓ⁻¹, subtract the
   evaluation on p_{i−1}[ℓ⁻¹|ℓ]) — the standard Fox-resolution
   comparison for 1-relator groups (Fenn–Sjerve); after it, all sealed
   gates pass.
3. The corrected `cell2_texture.py` is hashed in the ledger
   (f02d4aad…), LABELED POST-HOC: the hash was appended after the run
   it produced, which violates the code-hash-before-rerun standard.
   Recorded as a process defect, not repaired retroactively.

## The adjudication

- Both repairs were DRIVEN BY SEALED GATES (the prereg's own O2/control
  clauses), not by outcome preference; the final formula is validated
  independently (the audit's exhaustive verifier, adopted into this
  directory as `verify_cell2_exhaustive.py`, which re-derives the cup
  values by a separately coded canonical bar-chain and checks all
  27 × 2 × 3 = 162 coboundary descents, all diagonals, all exchanges,
  and the exact rank).
- **The corrected result, in corrected language:**
  Ω: Λ²H¹(M;27) → H²(M;27*) is a SURJECTIVE ALTERNATING cohomology
  operation of **rank 2 with 1-dimensional kernel** — NOT
  "full/nondegenerate" (the earlier FINDINGS wording overstated; the
  target is 2-dimensional). The printed H² coordinates used a mixed
  nullspace basis; a block-adapted basis is a registered residual.
- **Relabelings (binding henceforth):** v₀ = "the invariant-section
  generator" (an invariant line, NOT a dynamically selected vev);
  the three H¹ summands = "three inequivalent local-system modes"
  (one class in each of three inequivalent principal-SL(2) blocks, NOT
  three copies of one representation, NOT generations).
- The transcript-grep lock is REPLACED by mathematical assertions
  (tests/test_b632_cell2.py updated: the exhaustive verifier runs under
  OA_SLOW; the fast tier asserts the corrected facts, not strings).

## Process lessons banked

Preserve failed outputs before rerunning (never overwrite a transcript
that carried gate verdicts); hash corrected code BEFORE the rerun it
produces; locks assert mathematics, not transcript strings.
