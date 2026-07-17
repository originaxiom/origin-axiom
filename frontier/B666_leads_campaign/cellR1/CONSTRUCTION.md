# B666 cell R1 — L63/Q-C: the transport map, CONSTRUCTED (outcome: constructed-with-certificate)

**Verdict: Q-C = c.** The B469/B303 orientation residue transports through the
geometric E₆ holonomy as **c** (conjugation/orientation), not as θ (the E₆→F₄
fold). Delivered per B578-D2's sharpening: the constructed transport MAP with
its defining property verified exactly — not an elimination — and the flagged
in-lineage T-NORM conflict adjudicated in the same pass.

Reproducer: `b666_r1_transport.py` (36 exact checks, ALL PASS; full output
`cellR1_output.txt`; script sha256
`5f253155b33031cf71ce0f5275dec960fe683a359ba8f6580bcfa811c8a64069`).

## The map T

- **Domain (the residue object, B578-D2's "scale-axis object").**
  R_m = the half-monodromy class: X_m = [[m,1],[1,0]] ∈ GL(2,ℤ) with
  det X_m = −1, X_m² = A_m, X_m = companion matrix of the metallic unit's
  minimal polynomial t² − mt − 1, so det X_m = N(λ_m) = −1 (BR-N — the three
  realizations of the one residue bit; re-verified symbolically in m, Part 0).
  Via Nielsen (Out(F₂) ≅ GL(2,ℤ)) the carrier is the mapping class
  σ_m ∈ Out(F₂); at m = 1: σ₁: a↦ab, b↦a, H₁(σ₁) = X₁, H₁(σ₁²) = A₁ = the
  fig-8 monodromy (Part 1) — the Gieseking deck class (BR2/B466, banked).
- **The map.** T = (precomposition functoriality) ∘ (θ-fixed principal
  embedding ι: SL₂ → F₄ = E₆^θ ⊂ E₆):
  **σ_m ↦ σ_m\* : X(F₂, E₆(ℂ)) → X(F₂, E₆(ℂ)), χ ↦ χ∘σ_m**, restricted to
  the geometric orbit {χ_g, χ̄_g}. Every arrow is banked or forced: the deck
  class (BR2/B466), functoriality of X(F₂, −) (definitional), ι θ-fixed
  (B570-QA level 1, re-verified in Part 4). No invented stand-in: the domain
  IS the residue's own carrier; the codomain IS the structure ⟨θ, c⟩ acts on.
- **Defining property (the certificate, all exact):**
  **σ₁\*(χ_g) = c(χ_g) ≠ χ_g = θ(χ_g).**

## The certificate (decisive numbers)

1. **SL₂ trace coordinates** (generic-matrix rational identities, Part 2):
   σ₁\*(x,y,z) = (z, x, xz−y); κ = tr[A,B] invariant.
2. **The geometric locus** (Part 3): σ₁\* preserves the B67 fixed-locus curve
   y = z = x/(x−1), acting by x ↦ x/(x−1); the cusp locus is
   x²(x²−3x+3)/(x−1)²; the geometric pair x_± = (3±√−3)/2 is **swapped**, and
   the full character points P_± = (x_±, x_∓, x_∓) satisfy
   **σ₁\*(P₊) = P₋ = conj(P₊)** exactly, with κ(P₊) = −2 (irreducible). The
   σ₁\*-fixed characters on the curve are {0, 2} — both non-geometric: **no
   geometric character is fixed** (the θ-type option is structurally empty).
3. **The E₆ lift** (Part 4): E₆-principal ≡ F₄-principal on the 27 — grading
   multiset = V₁₇⊕V₉⊕V₁ strings, Jordan type (17,9,1) both sides (B570's
   banked computation replicated + multiset-verified) ⇒ θ∘ι = ι (Kostant
   conjugacy, cited as banked in B570-QA). The 27/78 character polynomials
   derived exactly from the grading: P₂₇ = U₁₆(t/2)+U₈(t/2)+1,
   P₇₈ = Σ_{e∈{1,4,5,7,8,11}} U₂ₑ(t/2) ∈ ℤ[t] (verified against the grading
   character; P₂₇(2)=27, P₇₈(2)=78). At the geometric point:
   **tr₂₇ = (6807 + 4965√−3)/2, tr₇₈ = (286145 − 29805√−3)/2 — both
   NON-REAL** elements of ℚ(√−3), Galois-equivariant (P(x₋) = conj(P(x₊))),
   and **P₂₇(σ₁\*-image of x₊) = conj(P₂₇(x₊))** — the transport closes at E₆.
4. **Klein-four bookkeeping** (Part 5): on the geometric orbit θ acts
   trivially (θ∘ι = ι), c acts by the swap, σ₁\* acts by the swap. The
   Klein four ⟨θ, c⟩ acts through its quotient ⟨θ,c⟩/⟨θ⟩ ≅ ℤ/2 (the
   c-column); **the transported residue hits that ℤ/2's generator**; the
   θ-hypothesis (transport = fold-action = trivial on the orbit) is refuted.

## What it transports, and what it proves

- **Transports:** the residue's ℤ/2 — carried as its **deck/Galois
  realization** (the mapping class, det −1), never as its unit-norm
  realization. On the geometry axis the image is the nontrivial element of
  Gal(ℚ(√−3)/ℚ) = the restriction of c.
- **Proves:** Q-C closes — the residue occupies the **c-column** of the
  two-chiralities picture (LAW-row candidate per the R1 spec, with Q-A's
  Klein four). Upgrade of B448/B466: "the heartbeat orbit IS the σ-orbit"
  now holds AT E₆ — the object's own non-orientable-quotient deck action
  realizes the Galois flip of its trace field on the geometric E₆ character.
- **The in-lineage conflict (T-NORM), adjudicated:** T-NORM (re-verified:
  imaginary-quadratic norm forms are sums of squares; norm −1 impossible)
  confines the NORM realization to the real-quadratic scale axis — and the
  constructed map never asks it to cross: functoriality transports the
  automorphism, not the unit. BR-N clause 3 ("only the scale end can carry
  the norm-realization") and this map ("the geometry end carries the
  deck/Galois realization") are the two halves of one statement. The old
  D2 cell's contradiction dissolves: its error was reading the norm
  realization as the thing transported.

## Honest scope

- The E₆ certificate is at **m = 1** (the geometric E₆ holonomy is the fig-8
  stage). The SL₂-level swap is banked family-wide for computed m = 1..4
  (B469 BR3 wave 2); an m-uniform E₆ statement is neither banked nor claimed.
- On the geometric orbit θ is trivial, so c and θ∘c act identically there;
  Q-C's question — which column receives the residue — is exactly the
  quotient ℤ/2 statement proved above. Globally σ₁\* is holomorphic
  (precomposition) while c is antiholomorphic; they agree on the
  ℚ(√−3)-rational geometric locus. That agreement is the precise content of
  "transports as c."
- The Kostant-conjugacy step is classical, cited exactly as in banked
  B570-QA; the in-sandbox discriminating fact is the (17,9,1) equality.
- Certificate level: fiber character variety (where the deck class lives;
  B466 Gate B — fiber characters on the B67 fixed locus are the ones that
  extend). The complement-level extension is the banked deck-action statement
  (BR2/B466; Gieseking standard).

Firewalled. No SM claim; nothing to CLAIMS.md. All verification internal.
