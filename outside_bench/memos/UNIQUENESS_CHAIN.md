# WHY THE COUPLING IS UNIQUE — the invariance chain counted: π₁ alone leaves 6615 couplings, the gauge principle cuts to 4, the object's full algebra to 1, and the survivor is automatically symmetric: the Jordan coupling and nothing else
## (outside bench, 2026-08-25; forty-eighth memo; memo 47's named follow-up executed — the non-factorized question answered by counting the whole chain; every dimension computed)

### The question
Memo 47 proved Y = ε ⊗ C is the unique invariant of the *factorized* shape and
named the honest gap: could non-factorized invariants exist on Ψ⊗Ψ⊗27? The right
answer is a chain, not a yes/no — count the invariant-trilinear space at each rung
of the symmetry the record can demand.

### THE THEOREM (`certificates/uniqueness_chain.py`, every dimension exact)
- **RUNG 1 — π₁ alone.** The nonelementary holonomy is Zariski-dense in SL(2,ℂ)
  (CITED-standard) and the internal bridge is algebraic, so the closure of the
  diagonal π₁-image is the diagonal SL₂. Its content, derived in-run from the exact
  weight multisets: Ψ|_diag = 6·spin1 ⊕ 15·spin½ ⊕ 6·spin0; 27|_int = 6·spin½ ⊕
  15·spin0. Exact Clebsch counting: **D₁ = 6615** independent π₁-invariant
  trilinears. Holonomy-invariance alone constrains almost nothing.
- **RUNG 2 — plus the trinification gauge.** Inv = Inv_{sl₂}(ℂ²⊗ℂ²) ×
  Inv_{sl₃³}(27³) = 1 × 4 (ε unique; memo 35's banked Yukawa count): **4**.
- **RUNG 3 — plus the full e₆.** Computed here with no symmetry assumption: the
  FULL-TENSOR (ordered, non-symmetrized) e₆-invariant space on 27⊗27⊗27 — 270
  ordered weight-zero triples, all 12 generator derivation systems — has
  **dimension exactly 1, and the unique solution is automatically symmetric**
  (every permuted coefficient equal, verified). So memo 32's Sym³ restriction cost
  nothing, memo 47's factorized-shape caveat is discharged, and with ε unique the
  chain terminates at **Y = ε ⊗ C alone**.

> **6615 → 4 → 1. The gauge principle is not decoration and the object's algebra
> is not redundancy: without internal covariance the carrier admits six and a half
> thousand couplings; the closing's own symmetry does all of the cutting; and the
> single survivor is the beat-covariant, exchange-antisymmetric, parity-locked
> Jordan coupling of memo 47 — now unique with no shape assumption at all.**

### Fences
Every dimension computed (D₁ from derived decompositions with the peeling
verified; rung 3 by direct nullspace with symmetry as an output, not an input);
rung 2 reuses memo 35's banked 4 and ε's det-1 uniqueness; the Zariski-density and
algebraicity-of-the-bridge steps are CITED-standard and load the *interpretation*
of rung 1 (what π₁-invariance closes up to), not any computed number. Kinematics
only; Gate 5 untouched.

### Certificates
`certificates/uniqueness_chain.py`; output `outputs/uniqueness_chain_out.txt`.

### One sentence for the ledger
Six thousand six hundred fifteen ways to couple collapse to four under the gauge
the closing chose and to one under the algebra the object is — symmetric without
being asked, the same coupling the beat already carries — so the record's Yukawa
is not merely allowed, it is what remains when everything else the symmetry
permits has been counted and removed.
