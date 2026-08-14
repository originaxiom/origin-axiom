# B912 PREREGISTRATION — R1, the e₆(2) norm cell (sealed before compute)

**Date sealed:** 2026-08-05 · **Seat:** cc (banking) · **Register:** ROADMAP
REGISTER v1, rung R1 · **Status:** SEALED BEFORE COMPUTE

## The question

B907 selected e₆(2): the wall is real exactly there, via two τ-twisted
conjugations σ± = φ±∘σ_split (banked, verified involutions). The value ladder's
rung R1: construct the canonical invariant Hermitian structure this real form
puts on the 27, and read the fifteen flavor-atom scales from it.

## The operation (MB12-checked)

1. **The antilinear intertwiner.** φ = τσ_χ maps the 27 to its dual (τ is the
   outer automorphism), so the e₆(2) conjugation σ equips the 27 with a
   conjugate-linear equivariant map J with ρ(φ(x)) ∘ J = J ∘ conj∘ρ(x)∘conj
   (the finite linear solve over the 78 generators; existence is forced by the
   rep theory — its failure is UNSTABLE, not an outcome).
2. **The Hermitian form.** H(u, v) := ⟨J ū, v⟩ via the frame's pairing,
   σ-invariance verified on all generators; H unique up to a real scale
   (27 irreducible) — fixed by a declared normalization (H on the first
   canonical vacuum line = +1).
3. **The readout.** The signature of H on the 27; H restricted to each of the
   15 flavor atoms (the banked tri-partition basis); per atom: the H-Gram, its
   signature, and |det| — the scale data. All exact where the tower permits,
   35-digit certified otherwise; both σ± checked (the global negation must give
   the same H up to the declared scale — a gate, not a result).

## The two-outcome criteria

- **OUTCOME A — SCALES EXIST:** H restricted to every atom is DEFINITE (all
  15 atom-Grams definite, signs possibly varying atom to atom). Then the
  fifteen scales s_i = |det Gram_i|^{1/dim_i} are well-defined positive
  numbers and the ratio table (R3's input) exists. The per-atom sign pattern
  is banked as structure.
- **OUTCOME B — OBSTRUCTION:** some atom-Gram is indefinite or degenerate —
  the scale assignment fails as posed; the signature data and WHERE it fails
  become the banked finding (R2/R3 then need a different construction, and
  the register requires a dated amendment).
- **UNSTABLE:** J fails to exist or the σ± cross-check fails — a computation
  error by rep theory; recompute before any verdict.

## The disclosed prior (stated, then the cell decides)

Lean A with a nontrivial sign pattern: e₆(2) is noncompact, so H on the full
27 should be INDEFINITE (a (p,q) signature), with definiteness holding
atom-by-atom and the sign pattern correlating with the frame's
compact/noncompact dichotomy. Confidence low — the last three sealed priors
lost, and are remembered here.

## What this cell does NOT decide (pre-stated)

R3's ratio table (a separate cell); any physics identification of the scales
(Gate 5); R4 remains sealed behind its own registered protocol.

## Files (after sealing)

- `norm_cell.py` → `results.json`; `FINDINGS.md` verbatim against these
  criteria; locks in `tests/test_b912_norm.py` (seal-integrity first).
