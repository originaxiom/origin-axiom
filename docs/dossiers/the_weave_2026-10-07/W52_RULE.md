# W52 — the rule, recorded before the read-out

The SM-derivation seat, 2026-10-09. Committed before the code that reads it exists. The predictions below were derived
by hand before this was written. Nothing here is a result.

## Why this arc

- **The owner's order (2026-10-09):** "we look what fixes τ then we count free numbers."
- **W51 settled the first half.** The weave's joint determinant over its three parities is flat, so τ is free. Every
  other canonical functional picks only ω (degenerate couplings) or the cusp.
- **W50 set up the second half.** On the ruled branch, couplings in τ alone are holomorphic vector-valued modular forms
  for the weave's own representation, and they break its group.
- **This arc counts the flavour numbers that structure leaves free, and says why.** It covers every weight assignment
  in a stated range, in both frames on record.

## Weave or thread?

- The forms are equivariant under the weave's whole group (every word in L and R), and τ is a state of the weave.
- The count is a property of that joint structure, made for every weight assignment at once. Weave-type.
- The tags: on the ruled branch; given Λ (GENESIS FK11); couplings in τ alone, holomorphic, with one flavour-blind
  Higgs per sector.

## The setting

- **The 13 flavour numbers** are the dimensionless ones in the record's typing (`docs/SM_SPECIFICATION_LEDGER.md`): the
  nine charged-fermion Yukawas and the CKM matrix's three angles and one phase.
- **The other six** are cited, not computed:
  - g₁, g₂, g₃ are scale-anchored and supplied by the reader;
  - v and m_H are dimensionful and supplied by the reader;
  - θ_QCD is a bit the object constrains (B1224, through I-18, unearned).
- **The two frames on record (W39, W43):**
  - **T ⊗ T (the Standard Model's fields, all in T given Λ).** Each sector's Yukawa is a form for ρ_T^∨ ⊗ ρ_T^∨: the
    diagonal piece D, the symmetric off-diagonal O₊ and the antisymmetric O₋ (W50).
  - **Sym² T (E₆'s 27³).** D and O₊ only.
- **A sector's coupling.** The sector s ∈ {u, d, e} has an odd weight k_s, and its Yukawa is
  Y_s(τ) = Σ_i α_{s,i} F^{(i)}_{k_s}(τ), over a basis of the d(k_s)-dimensional coupling space, with complex
  coefficients α.
- **The parameters.** τ gives two real numbers. Each sector gives 2d(k_s) − 1, since rephasing its right-handed field
  removes one phase. So:

  P = 2 + Σ_s (2 d(k_s) − 1).

- **The observables.**
  - The nine log singular values of Y_u, Y_d and Y_e.
  - |V₁₂|, |V₂₃|, |V₁₃| and J = Im(V₁₂ V₂₃ V₁₃* V₂₂*), from V = U_u^† U_d, with the left singular vectors ordered by
    increasing singular value.
- **The free flavour numbers** are the rank r of the 13 × P Jacobian of the observables in the parameters, at generic
  points. 13 − r is the number of relations the structure predicts.

## The facts by hand

1. **The dimensions (W50's N4), at k = 1, 3, 5, 7.** T ⊗ T: d = 1, 2, 4, 5. Sym² T: d = 1, 1, 3, 3.
2. **Two sectors share a coupling** when they have the same weight and that weight's space is one-dimensional. Their
   Yukawas are then proportional: their ratios agree, and if the two are u and d, V is a phase matrix.
3. **How many observables can vary.** Group the sectors by sharing. Each group contributes its two mass ratios, the
   three scales always vary, and the CKM's four vary only if u and d are in different groups:

   N_var = 2·(number of groups) + 3 + (4 if u and d are not grouped, else 0).

   This gives 13 (no sharing), 11 (d with e, or u with e), 7 (u with d) and 5 (all three).
4. **The rank.** Generically r = min(P, N_var). The forms' τ-dependence is not degenerate, and independent
   coefficients act independently.
5. **The geometry's weight.**
   - W45's four-dimensional reading puts T at weight 3/2. A Yukawa of two T's and a weight-0 Higgs then has k = 3.
   - T ⊗ T at k = 3 for all three sectors (d = 2) gives P = 2 + 3·3 = 11 = r: two predicted relations.
   - Sym² T at k = 3 (d = 1) gives P = 5 = r with V trivial. That contradicts the observed mixing.
6. **The smallest structures with mixing that is not a phase matrix** (u and d not grouped). P is odd, since it is
   2 plus three odd terms.
   - In T ⊗ T, d = 2 only at k = 3 and d = 1 only at k = 1. So P = 7 needs one sector at k = 3 and two at k = 1, with u
     and d at different weights: (3, 1, 1) and (1, 3, 1), six relations. P = 5 needs every k = 1, which groups u with
     d.
   - In Sym² T, P = 5 at (1, 3, ·) and (3, 1, ·): eight relations.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **C1** | The coupling spaces' dimensions, recomputed, are fact 1's. | 95% |
| **C2** | For every assignment (k_u, k_d, k_e) ∈ {1, 3, 5, 7}³ in both frames (128 assignments), the Jacobian's rank at three generic points equals min(P, N_var), the same at all three points. | 75% |
| **C3** | At the geometry's weight (all k = 3): T ⊗ T has r = 11 (P = 11, two relations); Sym² T has r = 5 with \|V₁₂\| = \|V₂₃\| = \|V₁₃\| = 0. | 85% |
| **C4** | The smallest P with mixing that is not a phase matrix is 7 in T ⊗ T and 5 in Sym² T, at the assignments of fact 6, and there r = P. | 85% |

**Extra read-outs (no prior).**
- The singular values of the k = 1 and k = 3 couplings along x = 0, at y = 1.2, 2 and 3. They show how deep a
  hierarchy the forms reach toward the cusp.
- The Jacobian's singular-value gap at each assignment.

**The reading, written before the run.**
- **If C1 to C4 hold, the free flavour numbers are τ plus the couplings' normalizations,** one complex number per
  independent form per sector, less one phase per sector. How many there are is set by the weights.
- **The principle does not fix the weights** (forced to choose, not forced which).
  - At the weight W45's reading gives, the Standard Model frame leaves 11 of the 13 free, and predicts two relations.
  - The smallest structures leave 7, in the Standard Model frame, or 5, in the E₆ frame.
  - Whether any of them fits the data is the next arc, a fit. This arc counts; it does not fit.
- **The tally of the 19,** a reading on the record's typing:
  - the flavour count r (11 at the geometry's weight, if that structure fits; 13 if no smaller structure does);
  - the three gauge couplings and v and m_H, supplied by the reader;
  - θ_QCD, a bit if I-18 is earned.
  - So at the geometry's weight at most 17 of the 19 are free on the ruled branch, given Λ. With the smallest
    structures, at most 13 in the Standard Model frame (7 + 6) or 11 in the E₆ frame (5 + 6).
- **Why each one is free.**
  - τ: the weave's joint determinant is flat (W51). The weave supplies the space of vacua and withholds the point,
    the record's torsor pattern (`docs/THE_FORCED_AND_THE_FREE.md`).
  - The normalizations: the weave fixes each form's shape but not its coefficient (Schur's lemma, per form).
  - The weights: nothing fixes the Higgs's weight.
- **If C2 fails at some assignment,** that assignment has a hidden degeneracy, a relation of its own. It is recorded,
  and the count there is the computed rank.

## Discipline

- One run. A failed launch (a crash before the read-out) is disclosed and fixed, not counted as a run.
- Each cell is recorded as computed; a failed prediction is recorded as failed.
- Post-hoc checks are labelled.
