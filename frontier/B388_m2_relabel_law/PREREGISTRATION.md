# B388 (W3.i) — PRE-REGISTRATION: the m=2 single-seed transport law 15 → 45

**Committed before computation. Target: the exact law relating the level-45 m=2 singles
(12-dim basis {1,c₁,c₂}⊗{1,√5,√−3,√−15}, banked E16) to the level-15 m=2 singles (banked,
t2_level15_singles.json). Both live on the same ord-12 grid.**

## Registered candidate laws (tested in this order; first exact 12/12 wins)

- **C0 (identity):** bare-H block of t₄₅(a) = t₁₅(a) for all a.
- **C1 (bare relabel):** bare-H block of t₄₅(a) = t₁₅(σ(a)) for one affine σ(a) = ua+v,
  u ∈ (ℤ/12)ˣ, v ∈ ℤ/12.
- **C2 (Galois-average collapse):** the ℚ(ζ₉)⁺→ℚ trace-average (c-blocks → 0) equals
  t₁₅ ∘ σ — equivalent to C1; listed for bookkeeping.
- **C3 (the specialization law — the structural candidate):** the CUBE-MAP evaluation
  ζ₉ → ζ₃ (i.e. c₁ → −1, c₂ → −1: spec(t₄₅) = bare − c₁-block − c₂-block) satisfies
      spec(t₄₅(a)) = γ(a) · t₁₅(σ(a))   for all a ∈ ℤ₁₂,
  with σ affine as above and γ(a) ∈ {id, σ_√5, τ₃, σ_√5τ₃} given by a CHARACTER RULE
  (constant, or depending only on a mod 2 / a mod 3 / a mod 4 — a named congruence class
  rule, not a per-cell lookup). VACUITY GUARD: the law must be stated by (σ, γ-rule) with
  ≤ 3 parameters and verified on all 12 cells including the zeros (support must map to
  support, zeros to zeros).

KILL: none of C0–C3 holds — bank the mismatch table exactly (the transport is then genuinely
non-specializing, itself a structural fact about the level tower).

Machinery: pure Fraction arithmetic on the two banked JSONs. Locks from the output JSON.
Firewalled level statements.
