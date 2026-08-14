# B908 DESIGN — the I-exactness pin (the solo seat's V2, taken up by cc)

## The reduction (found at design time, 2026-08-05)

Let R = the row-pencil couplings, C = the column-pencil couplings of the colorless
3×3 grid (six lll values, all exact 1-dim computations). Set

  u := ∏R · ∏C   (fully symmetric under every Galois action and the pencil swap)
  v := ∏R + ∏C   (symmetric likewise: any σ preserves-or-swaps the pencils,
                   because the coupling graph is CONNECTED BIPARTITE (K₃,₃), whose
                   bipartition is unique — so {∏R, ∏C} is σ-stable as a set)

Then u, v ∈ ℚ, and t := I + 1/I = (v² − 2u)/u. Hence:

  **I = −1  ⟺  v = 0  (one rational number vanishing)**

## The three legs

1. **The symmetry lemma (structural, provable now):** the atom/coupling construction
   is ℚ-defined as a whole; σ permutes atoms and couplings preserving the graph;
   connected-bipartite uniqueness ⟹ pencil preserve-or-swap ⟹ u, v ∈ ℚ. (The graph
   facts checkable on the banked incidence; the equivariance from the construction.)
2. **The multi-prime congruences (running):** v ≡ 0 mod p at every full-tower prime
   (equivalent to I ≡ −1). Each prime multiplies the counterfactual's cost; with 7
   primes N ≈ 4×10³², but a naive Hadamard height bound on v blows past the
   reconstruction threshold — so the congruences are EVIDENCE, not yet proof.
3. **The vanishing mechanism (the registered proof target):** find the explicit
   involution τ (a Galois transposition realized through B900's diagonal cocycle +
   twists) that swaps the pencils and multiplies the coupling product by −1 through
   an ODD orientation count on the atoms — then v = ∏R + ∏C = ∏R − ∏R = 0
   structurally, no height bound needed. The −1 would be the program's chirality
   sign surfacing as an orientation parity — consistent with the solo seat's fenced
   "−1 vein" reading, and with B903's root-parity mechanism shape.

## Status

Leg 2 in flight (five new full-tower primes 40693, 40897, 40903, 40927, 40939 —
the towers derived with the solo seat's own construction). Legs 1 and 3 queued
behind Review 38's close.
