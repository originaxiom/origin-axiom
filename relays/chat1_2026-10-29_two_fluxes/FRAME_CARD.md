# TWO THREE-GENERATION FLUXES (P-425's live question, P-419) — the frame card and the prediction, written before the script

chat1 (the web seat), 2026-10-29, at the owner's word ("continue", after THE INTEGERS named B1804's holomorphic frame and
P-425 as the shortest route to an integer-fixed τ). Data-free: no measured number is read. 0 of 19.

## The frame card (the 2026-10-29 rule, item 1)

- **The frame:** B1804's holomorphic flux frame, as B1808 computed it. T⁴ with LR acting holomorphically; the moduli
  (τ₁, τ₂) of abelian surfaces with real multiplication by ℤ[φ]; Λ_A, the LR-invariant lattice, with B1808's Gram matrix
  Q = [[0, −1, 0, 0], [−1, 0, 0, 0], [0, 0, 2, 1], [0, 0, 1, −2]] (det 5, signature (2, 2)), read from B1808's committed
  `three_generations_in_f2h.json`.
- **Continuous configurations:** (τ₁, τ₂).
- **Discrete choices:** the flux classes. The reading of the T⁴ index as a generation number is CHOSEN (B1808; I-34).
- **Outputs:** the isolated points and their CM fields. None of the 19.
- **Conditions built from the object:** LR-invariance (symmetry, FORCED by the monodromy); type (1,1) (holomorphy,
  CHOSEN with the frame, B1808).
- **No positive is claimed, so no null.**

## The question

B1808: one class w with Q(w) = −6 (|χ| = 3) is (1,1) on a curve; a point needs a second class, and with the second class
free the points are infinite modulo any isometry group, because det NS is unbounded. **What if the second class is also
a three-generation class, Q(u) = −6?** Then the plane ⟨w, u⟩ has Gram [[−6, b], [b, −6]] with |b| ≤ 5, its saturation
NS has det NS = (36 − b²)/k², and det NS is bounded. So the condition "two independent fluxes, each with |χ| = 3" can cut
the points to finitely many classes. Which NS lattices occur in Λ_A, and which CM fields? By B1808's referee (q2), the
CM field at a point is ℚ(√5, √(−5 det NS)) = ℚ(√5, √(−det NS)).

## The computation (fixed now)

- Every v ∈ Λ_A with Q(v) = −6 and coefficients |x_i| ≤ B, for B = 4, 6 and 8.
- Every pair (v, u) of them spanning a negative-definite plane (det Gram > 0, Q(v) < 0).
- Its saturation in ℤ⁴ (index k = the gcd of the 2 × 2 minors of [v u]); NS's basis, its Gram, Gauss-reduced; det NS.
- The distinct reduced NS classes, with the CM field's imaginary quadratic d (the squarefree part of det NS, up to the
  factor 5 that ℚ(√5) absorbs), and the number of planes found per class at each B.
- **Data-free control:** the a priori list of even negative-definite binary lattices of det ≤ 36 that contain two
  independent vectors of norm −6, computed separately; every class found must be in it.
- **Read-out:** whether the found classes are stable from B = 6 to B = 8.

## The prediction (written now)

- **Finitely many NS classes, more than one CM field.** Prior 85%. The a priori fields are ℚ(√5, √−d) with d among the
  squarefree parts of (36 − b²)/k² for b = 0…5: d ∈ {1, 2, 3, 7, 11} (36, 32 or 8, 27 or 3, 35, 11; 20 gives √−5, which
  ℚ(√5) turns into √−1).
- **d = 3, B1804's ℚ(√5, √−3) point, is among them** (A₂(−1) holds three pairs of norm −6 vectors; B1808's referee).
  Prior 95%.
- **d = 3 is the only field:** prior 5%.

## What each outcome means (written now)

- **More than one field:** "two three-generation fluxes" cut the frame to a finite menu of CM points, but they do not
  force ℚ(√5, √−3). The compositum is then one entry of a finite menu: a discrete choice of known size, which P-418 can
  count.
- **One field, d = 3:** the condition forces CM by the compositum. P-425's live question would then have an answer
  within this frame, conditional on the CHOSEN reading of the index as generations.
- **Infinitely many classes** (instability with B): the bound on det NS fails in some way not foreseen; reported as such.
