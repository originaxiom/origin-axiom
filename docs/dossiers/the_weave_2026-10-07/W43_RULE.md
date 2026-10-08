# W43 — the rule, recorded before the read-out

The SM-derivation seat, 2026-10-08. Committed before the code that reads it exists. The predictions below were derived
by hand before this was written. Nothing here is a result.

## Why this arc

- **Main's B1620 says TM1 is allowed under T ⊗ T.** Its §3 reads: "TM1 allowed under T̄ ⊗ T and T ⊗ T (P10 …; not
  under Sym² T)". The relay's title says the same, and P10's scope note in FALSIFIER_REGISTER follows it.
- **W42 suggests otherwise.** Under T ⊗ T no viable residual contains an odd rotation: every edge half-turn and
  quarter-turn carries c with c² = ±i. TM1's fixed column (⅔, ⅙, ⅙) is the overlap of a 3-cycle's eigenbasis with an
  edge half-turn's axis. So no T ⊗ T residual pair should give TM1. The family a pair can give is TM2, whose fixed
  column (⅓, ⅓, ⅓) is a parity line against a 3-cycle's eigenbasis.
- **B1620's own stored fits were read before this rule.** In `post_seal_tensors.json` (sha256 f74ecbe3…, as in
  B1620's ARTIFACT_HASHES at main d85301ad5; copied verbatim to `received/B1620_post_seal_tensors.json`), the T ⊗ T
  PMNS families below four dimensions are two. Both pair orders (3, 2), with block sums ⅓ and ⅔ in every row, which is
  TM2's column. Cell F2 classifies every such entry; it is a transcription, not a prediction.
- **Main's frame clause.** The relay says: "In a frame with a U(1) on T, Sym² T gains invariants and the TM1 question
  reopens."
  - That repeats W39's premise as first written (main read this branch at e077e4ba8, before the assurance round).
  - The assurance round (d62458221) replaced the premise and called "Sym² T gains the singlet" a renaming, withdrawn.
- **That withdrawal went too far, and this rule says so before any run.**
  - In a frame where c is gauge, a gauge U(1) acts on T by a phase and commutes with the holonomy. The flavour group is
    then the rotation group O acting by S.
  - Gauge invariance gives any Higgs that couples to T T the compensating charge. A Higgs that is a singlet of O then
    gives Sym² T's invariant δ: three equal masses.
  - The replacement's point stands: the selection rules depend only on each field's total transformation. Which Higgs
    counts as flavourless is frame-relative.
  - W43 computes that frame, so both seats' statements are tested against a computation and not against each other.

## Weave or thread?

- Every subgroup of each frame's group is taken as a possible residual, none chosen. The quantity, the trimaximal family
  a residual pair allows, is defined on the joint action's group. The claim is about all pairs at once: weave-type.
- A frame is a choice of which part of the group is gauge (GENESIS FK11's datum, open). Each frame is stated, never
  presented as forced.

## The objects

- **The record's frame (B1620's).** Every element c(g) S(g) of G acts as flavour. The residuals are W42's 68
  subgroups, with W42's viability.
- **The frame where c is gauge.**
  - The flavour group is O.
  - A Higgs with the charge T T needs breaks the U(1) to ±1.
  - The residuals are the subgroups of B₃ = {±1} × O, acting on T by ±S: the 48 signed permutation matrices.
  - Phase twists from Higgs fields in other representations of O are not covered, except the 3-cycles' twists in F4.
- **W24's frame** (S gauge, only c flavour) is not computed. Its flavour group acts on T by scalars, so it constrains no
  mixing at all (by hand).
- **The trimaximal families.** For a pair (H_ℓ, H_ν) viable under one tensor:
  - the mixing is U = W_ℓ† W_ν, with W the eigenvectors of M M† for generic invariant members;
  - the pair has a fixed TM1 column if, at every sampled member, one column of |U|² is (⅔, ⅙, ⅙) up to the order of
    its entries; it has a fixed TM2 column if that column is (⅓, ⅓, ⅓);
  - the family dimension is B1620's: the rank of the map from the couplings to the nine |U_ij|² and J.
- **"TM1 allowed"** means some pair has a fixed TM1 column with family dimension 2: the TM type, one angle and one phase.
  "TM2 allowed" is defined the same way.
- **Viable** is B1620's definition, decided exactly as in W42.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **F1** | **The record's frame.** Under T̄ ⊗ T, TM1 and TM2 are both allowed: TM1 from a 3-cycle group with a group containing an edge half-turn (such as ⟨RRL⟩, order 8), TM2 from a 3-cycle group with a face half-turn group. **Under T ⊗ T, TM1 is allowed by no pair, and TM2 is.** Under Sym² T neither is. | 90% |
| **F2** | **B1620's stored fits, transcribed.** Under T ⊗ T every PMNS family below four dimensions has a fixed TM2 column and none a TM1 column. Under T̄ ⊗ T both appear. (Read before this rule.) | (read) |
| **F3** | **The frame where c is gauge.** B₃ has 98 subgroups, 66 of them abelian. Viable: 66 under T̄ ⊗ T, 66 under T ⊗ T (every element is real, so every abelian character is real), and 49 under Sym² T (the subgroups whose every element squares to 1). The invariant of O in Sym² T is δ alone. TM1 and TM2 are allowed under T̄ ⊗ T and under T ⊗ T, and neither under Sym² T. | 85% |
| **F4** | **No twist rescues a 3-cycle under Sym² T.** For each of the 8 rotations t of order 3 and each twist u ∈ μ₂₄, every symmetric matrix fixed by u t has a degenerate pair of singular values or a zero one. By hand this holds for every u ∈ U(1): in t's eigenbasis an entry survives when u² χ_i χ_j = 1, which allows at most one diagonal entry and the complementary off-diagonal pair. | 97% |

**The reading, written before the run.**
- If F1 to F4 hold, main's TM1 is allowed under T̄ ⊗ T in both frames.
- Under T ⊗ T it is allowed only in the frame where c is gauge. In the record's frame the T ⊗ T family is TM2, and
  B1620's sentence holds for T̄ ⊗ T alone.
- Under Sym² T it is allowed in no frame. Every trimaximal column needs a 3-cycle residual, and no 3-cycle survives
  Sym² T under any twist.
- So given Λ, with E₆'s cubic and Higgs fields only in 27s (Sym² T), P10's TM1 comes from no residual pair in any frame.
  With an antisymmetric Yukawa (T ⊗ T, an E₆ 351), it needs the frame where c is gauge.
- Main's clause is right that Sym² T gains δ there. "The TM1 question reopens" holds under T ⊗ T, not under Sym² T.

## Discipline

- One run. A failed launch (a crash before the read-out) is disclosed and fixed, not counted as a run.
- Each cell is recorded as computed; a failed prediction is recorded as failed.
- Post-hoc checks are labelled.
