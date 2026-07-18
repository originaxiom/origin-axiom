# PREREG — B700 cell 3 (cc2): the Coste–Gannon–Ng Galois action realizes the golden torsor

*Seat cc2 (read-only, advisory). Owner "yes please" on cc's task-split proposal
(relay CC_TO_CC2_2026-07-19_fiber_functor_program.md). Builds on cc's banked
cell 1 (golden torsor, sha 1bbdb15b) + cell 2 (V₄ uniformity, sha 060aaaee),
both re-read and accepted on this seat. Gate 5 throughout — pure modular
data + finite-group rep theory + Galois. No physics; "measurement" = a fiber
functor of a fusion category, NOT a physical measurement. Nothing to CLAIMS.*

## Claim
The Coste–Gannon–Ng (CGN) Galois action on the **golden stage's modular data**
is exactly the generator of cell-1's ℤ/2 torsor: the SAME field automorphism
σ: √5 ↦ −√5 (φ ↔ −1/φ) that swaps the two golden 2-dim irreps of 2I = SL(2,5).
The measurement torsor of cell 1 is thereby *realized* as the modular-data
Galois action (Tannakian), turning the K020-in-ear PLACEMENT one step further
toward a THEOREM.

## Two-sided-complete criterion (cc's cell 3a, banked)
cc's cell 3a (relay 2026-07-19) banked the TRACE-TOWER realization: the Galois
ℤ/2 on ℚ(√5) acts on the order-10 weld ⟨W⟩≅ℤ/10 as the unit-power map
Wᵏ ↦ W³ᵏ (the coset {3,7} of units mod 10; equivalently W↦W^{±3} — this seat's
independent derivation gave W↦W⁷, the inverse unit, same σ|_{ℚ(√5)}). Cell 3
(this seat) is the MODULAR-DATA half: compute the CGN S/T Galois action and test
whether it agrees with Wᵏ↦W³ᵏ. AGREEMENT ⇒ cell 3 is "two-sided complete"
(modular-data action = trace-tower action = cell-1 torsor generator).

## What gets computed (exact; Sage preferred, sympy fallback)
- **A — the golden modular data.** Fibonacci MTC (the minimal golden fusion
  category): S = (2+φ)^(−1/2)·[[1,φ],[φ,−1]], T = diag(1, θ_τ) with the
  standard golden twist. Verify S unitary, (ST)³ ∝ S², S² = charge conj.
  Report ℚ(S) and the ratio field ℚ(s̃_{ij}/s̃_{0j}) (expected = ℚ(√5)).
- **B — the CGN Galois action.** N = ord(T); Gal(ℚ(ζ_N)/ℚ) and its restriction
  to ℚ(√5). For the nontrivial σ ∈ Gal(ℚ(√5)/ℚ): the CGN permutation σ̂ of the
  labels and signs ε_σ (via σ(S_{0j}/S_{00}) → S_{0,σ̂(j)}/S_{00}). Report the
  exact (σ̂, ε_σ) table; confirm σ carries S to its Galois-conjugate datum
  (φ→−1/φ, the Yang–Lee/non-unitary form).
- **C — the 2I torsor and the realization.** Exact character table of
  2I = SL(2,5): confirm EXACTLY two 2-dim irreps, character field exactly ℚ(√5),
  Galois-conjugate with NO fixed one (= cell 1). The order-10 weld element W
  (B674): show σ(√5→−√5) acts on ⟨W⟩ ≅ ℤ/10 as a UNIT power W→W^{±3}
  (ζ₁₀→ζ₁₀^{±3} up to convention), NOT the squaring W→W² — print the trace
  orbit proving tr(W^7)=φ=σ(tr W) while tr(W²)=−φ≠σ(tr W). Then test whether
  the Part-B CGN σ IS this same automorphism.

## Two-outcome (sealed)
- **REALIZED**: the CGN Galois σ on the golden modular data = the field
  automorphism √5↦−√5 = the cell-1 torsor generator = the 2I golden-irrep swap,
  AND agrees with cc's cell-3a trace-tower map Wᵏ↦W³ᵏ (same σ|_{ℚ(√5)});
  the permutation/sign data is computed exactly and the identification is
  canonical (same σ, simply transitive on the 2-element set). ⇒ the measurement
  torsor is the modular-data Galois action, concretely — cell 3 "two-sided
  complete" with cell 3a.
- **DISTINCT / NOT**: the modular-data Galois action is a different ℤ/2, or not
  simply transitive, or the character field is larger than ℚ(√5) ⇒ the torsor is
  NOT realized by the modular data (bankable negative; would weaken the
  PLACEMENT→theorem path).

## Base-rate / convention gate (mandatory)
- "the golden category has a ℚ(√5) Galois action" is TRIVIAL and does not count.
  The CONTENT is (i) the exact CGN (σ̂, ε_σ) permutation/sign data; (ii) the
  identification of that σ with cell-1's 2I-irrep swap (same automorphism, not
  merely both ℤ/2); (iii) the unit-power correction on W (W→W^{±3}, refuting
  "Galois = W²" from chat-1's 2026-07-18 close, Fact 5).
- Normalization convention (D = √(2+φ) is degree 4) pinned in the FINDINGS:
  the Galois action is read on the ratio field ℚ(√5), not the total-dimension
  extension.

## Falsifiers (hard gates)
- S must be unitary and satisfy (ST)³ ∝ S² exactly (else the modular data is
  wrong — halt).
- 2I character orthogonality must hold exactly; exactly two 2-dim golden irreps.
- W-check: tr(W^7) = φ and tr(W²) = −φ exactly (proves the unit-power vs square
  distinction). If tr(W²) came out = σ(tr W), the correction is wrong — halt.

## Verification (this seat, after the agent returns)
- Independently recompute ONE CGN permutation entry and the W trace-orbit by
  hand/sympy; confirm ℚ(S) ratio field = ℚ(√5); confirm the 2I two-irrep swap.
- Two-seat gate: cc's cell 4 (second stage E₆ level 2 / PSL(2,7)) is the
  stage-uniformity check that licenses PLACEMENT→theorem; cell 3 alone does NOT
  claim the theorem.

## Firewall
Gate 5. Pure category/Galois/rep-theory arithmetic. The observer-coupling
reading stays firewalled. No comparison to any measured quantity.
