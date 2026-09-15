# THE MINIMAL INTERNAL FACTOR — exact Weyl-dimension enumeration: every nontrivial e6 irrep in the exhaustive box has dim ≥ 27, with equality only for the 27 and its dual; the OA-C1087 category is now named
## (outside bench, 2026-08-26; sixty-sixth memo; wave-2 cell A5, verified CONFIRMED; one labeling preregistration corrected in-run — the stack's node ordering puts the minuscule pair at indices {0,5})

### THE FACTS (`certificates/minimal_factor.py`; sympy Rational, the stack's own invariant form; ρ cross-checked by ⟨ρ,αᵢ⟩ = 1)
- Anchors: dim(0) = 1, dim(ω₁) = 27, dim(adjoint) = 78, all by the exact Weyl formula.
- All 84 dominant weights with Σaᵢ ≤ 3 enumerated: **every nontrivial one has dim ≥ 27, equality exactly at the two minuscule fundamentals** (27 and 27̄).
- CITED (labeled): dominance-order monotonicity extends the exhaustive box to all dominant weights.
- **Conclusion for codex OA-C1087:** in the category {ℂ²⊗V : V a nontrivial irreducible e6-module}, the carrier is minimal up to internal duality. The requirement of a nontrivial internal factor remains a modelling choice — the fence stands, with the category now explicit.

### Certificates
`certificates/minimal_factor.py`; output `outputs/minimal_factor_out.txt` (in-lane rerun byte-identical).
