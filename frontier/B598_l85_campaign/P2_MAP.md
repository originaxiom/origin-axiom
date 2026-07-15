# STEP 4 — THE TYPED P2 MAP (the quantization arrow, made explicit)

Opened 2026-07-15. The chain's step 4 (seat-4 audit): "Gates A/B alone are
insufficient; the banked P2 is gates + data + a structural verdict, NOT the
map." This document is the map's TYPE SIGNATURE; every slot is either
COMPUTED (with the script and lock named) or DECLARED (a convention that
must be sealed into the step-8 prereg BEFORE any outcome-bearing
comparison). Nothing here is fitted to stage values.

## The map (candidate)

P2 : Dom → Cod, the finite-dimensional avatar of chat-1's shifted-saddle
state integral, under the role-separation law (structure from the object's
field ℚ(√−3); values from the stage's field).

## The eight slots

1. **Domain** [COMPUTED — step4a_domain.py + step4b gate (i)]
   THE BENDING FRAME (declared): Dom = ⊕_{m ∈ {1,4,5,7,8,11}} H⁰(T²; V_m)
   — the bending lines at the weld torus (Johnson–Millson bending of the
   mirror-double along the separating T²). This is EXACTLY the family the
   banked classical data computes (B599-ALG's twist exp(t·v_m); the lemma
   cell's J-welds): the twist by a peripherally-fixed v is the deformation
   whose class is the Mayer–Vietoris image δ(v) ∈ H¹(double). Gates:
   4b-(i) certifies v_m = the block's top vector is peripherally fixed
   (the line is realized); 4a computes dim H⁰(T²; V_m) exactly (= the
   number of bending parameters per block).
   THE CUSP CROSS-CHECK: P1's classes live in H¹(π_K; V_m) (six lines,
   dim 1 each, B575-G4); step 4a types that picture too — dim H¹(T²; V_m),
   res injective per block (half-lives-half-dies face) — and the step-3
   universal ratio (I_λ/I_μ = −2√−3) is its gauge-invariant content. The
   H¹ data pairs with the bending H⁰ through T²-duality; it constrains,
   but is not, the domain.

2. **Codomain** [COMPUTED — step 6, banked]
   Cod = the stage ε²-amplitude lines: the golden amplitude
   u†M_odd u ∈ ℚ(ζ₅) (B593, exact) and the three E₆₂ pair amplitudes
   −(2/√7)sin(2πj′/7)ζ₁₄ᵏ ∈ ℚ(ζ₈₄) (step 6, exact).

3. **Formula** [COMPUTED classical side — step 4b; the comparison itself is
   P3's and happens only after steps 7–9]
   For each block m: bend the mirror-double by c = exp(t·v_m) (copy-2
   letters conjugated: y = c·b̄·c⁻¹ — the banked r4b frame, exact), and
   take the t¹- and t²-coefficients of the J-paired responses
   ⟨v0, ρ_t(w)·v0⟩_J on the frozen word list (B599-R4's 20 words, with
   ⟨·,·⟩_J replacing the raw dot per the chain's step-5 mandate). No
   second-order integration ambiguity arises: the bending family is
   polynomial-exact, not a jet. The candidate law: the t² response vector,
   normalized per slot 8, is what the stage amplitude computes. The
   degree-2 truncation is validated against B599-ALG's banked Lagrange
   witnesses (4b gate (ii), exact integers).

4. **Equivariance** [COMPUTED — step 4b]
   θ swaps nothing at the block level (each V_m is θ-homogeneous with sign
   ε_m: even {1,5,7,11}, odd {4,8}); the move-across lemma
   ⟨Xu,v⟩_J = −ε_X⟨u,Xv⟩_J forces the t² response parity: the map must
   send ε_m-odd lines into the conjugation-odd stage sector (the hearing
   channel) and ε_m-even lines into the deaf sector. Verified on the
   computed responses.

5. **Rank** [COMPUTED — step 4b] of the assembled response matrix
   (six columns = blocks; rows = frozen words).

6. **Kernel** [COMPUTED — step 4b] ditto; the forced-zero criterion
   (step 5) predicts which entries vanish structurally BEFORE the
   computation — recorded as predictions in the 4b script docstring.

7. **Polarization** [DECLARED + COMPUTED ambiguity]
   η_m is ambiguous by a first-order cocycle; the t² response is
   well-defined only modulo the image of first-order responses. The
   declared polarization: quotient the row space by the span of the
   first-order (t¹) response vectors; 4b computes that image explicitly
   and reports the quotient responses.

8. **Cross-domain normalization** [DECLARED — sealed into the step-8
   prereg; NOT fitted]
   The per-block scale relating the classical cocycle normalization
   (P1's table convention) to the stage's ε. Declared convention:
   normalize ξ_m so that ξ_m(μ)'s leading coordinate (P1 table order) = 1,
   and compare stage/classical only through scale-free quantities
   (ratios within a block; cross-block ratios of like-parity blocks).
   Any comparison requiring an absolute scale is OUT OF SCOPE for P3 v1.

## Status

- 4a (domain typing): COMPUTED GREEN — `step4a_domain.py` + output; h⁰=1,
  h¹=2, h²=1 uniformly; res injective at all six blocks.
- 4b (responses, equivariance, rank, kernel, polarization): COMPUTED
  GREEN — `step4b_responses.py` + output. R1 = 0 (even forced, odd
  genuine); rank R2 = 2, supported exactly on the θ-odd lines; the column
  law N₄(1+√−3) / N₈(1−√−3) with the mixed word conjugated; polarization
  quotient trivial. The registered parity prediction failed honestly and
  is preserved in the script header.
- Slots 7/8 declarations: frozen here, to be hashed into the step-8 prereg.
- STEP 4 IS COMPLETE. The map's classical content = (N₄, N₈, the universal
  word-pattern, the conjugate-phase assignment).
