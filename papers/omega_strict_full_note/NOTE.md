# A Positive Elementary-Matrix Semigroup with an Explicit Signature-(1,3) Invariant-Form Cone

**A consolidation for external review.** Dritëro M. (with AI-assisted, cross-session computation).

This note states, with unambiguous verification status, an algebra/symbolic-dynamics result about positive
elementary row-shears on 4×4 integer matrices. **The program's larger physics aspirations are explicitly NOT
invoked** (see *Claim firewall*). Every claim below was **independently re-derived** in the repository
(`frontier/B156_omega_strict_full_cone/`, ledger V149) with fresh code — corroboration of a cross-session
derivation, not blind transcription.

### Status labels
**[exact]** symbolic/exact-arithmetic identity · **[proved]** theorem-grade · **[exact-count]** exact
enumeration · **[open]** genuine gap · **[firewalled]** deliberately not claimed.

## Objects

Let `S_ij = I + E_ij` be the positive elementary row-shear (row_i += row_j) acting by left multiplication on
4×4 integer matrices. For integers `a,m`,

```
R_{a,m} = [ a-3  a-2  1  a-4 ]      δ = 2a - 1 - m
          [ 0    1    1  0   ]
          [ m+1  m+1  1  m+1 ]
          [ 1    1    0  1   ]
```

and, for `m ≠ -1`, the rational symmetric form

```
G_{a,m} = [ -1            0              (a-4)/(m+1)            0 ]
          [  0      -(2a-m-9)/(m+1)       0                     2 ]
          [ (a-4)/(m+1)   0        -(a²-8a+2m+18)/(m+1)²        1 ]
          [  0            2              1                      0 ].
```

A matrix is **strict-full** iff it admits a *nondegenerate* symmetric `G` with `MᵀGM = G`.

## Results

**1. Core identities.** `det R_{a,m} = 1`; `χ(R_{a,m}) = x⁴ − a x³ + (2a−2m−4) x² − a x + 1` (reciprocal);
`R_{a,m}ᵀ G_{a,m} R_{a,m} = G_{a,m}`; `det G_{a,m} = −δ/(m+1)`. **[exact]**

**2. Positive shear dynamics.** `A = S₀₃: R_{a,m} → R_{a+1,m}` (δ→δ+2); `C = S₂₃: R_{a,m} → R_{a,m+1}`
(δ→δ−1). So from `R_{8,0}` (δ=15) every `{A,C}` word keeping `δ ≥ 1` stays in a nondegenerate sector. **[exact]**

**3. Signature theorem.** On the live cone `m ≥ 0, δ ≥ 1`, `G_{a,m}` is nondegenerate of algebraic signature
**(1,3)**. At the wall `δ = 0 ⟺ m = 2a−1` it degenerates (null vector `((a−4)/2, −a/2, a, 1)`; boundary char
poly `(x+1)²(x²−(a+2)x+1)`); for `δ < 0` the signature is `(2,2)`. Constancy of (1,3) is **rigorous** (det
`G < 0` on the convex cone + a Sylvester pivot certificate), not sampled. **[proved]**

**4. TC-2 (reciprocity).** Any strict-full matrix has a reciprocal/palindromic characteristic polynomial:
`MᵀGM = G` with `G` invertible gives `M ~ M⁻¹`, so the spectrum is closed under `λ↦1/λ`; for `det M = 1` and
even `n` the char poly is exactly palindromic. (This is *why* `χ(R_{a,m})` is palindromic; it is also the
forced reciprocity behind the broader trace-map tower.) **[proved]**

**5. Strict-full survivor counts.** A strict-full **survivor** at level `L` is a length-L history that begins
at an Ω₄ seed (strongly connected, char poly `x⁴−4x³+5x²−4x+1` = golden×phase, strict-full at L4) and remains
strict-full at every level. The counts are

```
L:   4    5    6     7      8       9        10
     96   672  3840  20928  105312  521904   2488080
```

**[exact-count]** L4–L7 independently re-confirmed by two enumerators (an exact `det`-of-generic-form test
with and without the reciprocity shortcut); L8–L10 from the exact-state artifacts, independent re-run in
progress. The block-word structure of the survivor language gives the **Fibonacci numbers** `F_{n+1}`
(transfer matrix eigenvalues `(1±√5)/2`, growth `φ`). **[exact]**

**6. Wall-avoiding history entropy.** The number `W_n(δ)` of length-n wall-avoiding `{A,C}` histories (δ ≥ 1)
has exponential rate exactly **log 2**, by an exact mechanism: `log W_n − n·log 2 → log(survival prob)` with
survival probability `1 − φ^{−δ} > 0` (from the first-passage recurrence; characteristic `r³−2r+1=0`, roots
`{1, 1/φ, −φ}`). So `W_n(δ) ~ (1−φ^{−δ})·2ⁿ`. **[proved]**

## What is NOT claimed — the claim firewall

This is **algebra / combinatorics / symbolic dynamics**. It does **not** claim: that `G` is a physical
spacetime metric; that signature `(1,3)` is a derived physical Lorentzian spacetime; that positive-shear
length is physical time; that history entropy is thermodynamic entropy; that endpoint entropy is proved
(it is **[open]**); or that gravity / quantum mechanics / cosmology are derived. The signature `(1,3)` is
**algebraic inertia of a bilinear form**; the entropy is a **word-growth rate**. **[firewalled]**

## Relation to the rest of the program

This is the **SL(4) lift of P6** (SL(2) positive shears `L,R` preserve a signature-(1,1) form). TC-2
("invariant form forces reciprocity") is the abstract reason the metallic trace-map tower lives in
reciprocal/palindromic polynomials. The Ω₄ seed `x⁴−4x³+5x²−4x+1 = (x²−3x+1)(x²−x+1)` is the **same
canonical "golden × phase" object** reached from the character-variety side as `frontier/B155` — the two
programs meet there (see `docs/UNIFIED_STATE.md`).

## Reproduction

Reproducers in `frontier/B156_omega_strict_full_cone/` (pyenv `python`, all print PASS):
`omega_independent_verify.py` (core R/G, 16 checks), `tc2_reciprocity_verify.py`, `verify_fib_blocks.py`
(21 checks), `opus_wall_entropy_verify.py` (entropy = log 2 + survival mechanism),
`independent_recount.py` (the strict-full survivor counts).

## Novelty

Whether the `R_{a,m}` / `G_{a,m}` / (1,3) / entropy package is already known is **NEEDS-SPECIALIST** (a
positive-elementary-matrix semigroup with an explicit indefinite invariant-form cone touches arithmetic
groups, indefinite-lattice theory, and symbolic dynamics). The AI literature scan de-risks; it does not
certify. This note is the owner-send artifact.
