# W74 — the rule, recorded before the code

The SM-derivation seat, 2026-10-14. Committed before the code that reads it exists. What the seat worked by hand while
drafting is listed under "Seen before the rule", and the priors were set after that. Nothing here is a result.

## Why this arc

- **The strong phase is one of the 19.** The record's register row I-18 (B1243) reads the Standard Model's θ̄ through
  the object's Chern–Simons 2-torsion. B1246 priced it.
  - θ̄ = θ + arg det M is the invariant: a chiral rotation moves phase between θ and arg det M.
  - So "earning it now needs the dictionary **and** the Yukawa phase".
- **W72's Yukawa came out real.** Its imaginary parts are at most 1.5 × 10⁻¹³ of its entries, and det Y > 0. If that
  reality is structural, the surface frame pays the Yukawa half of I-18's price.
- **This arc asks why, and what it costs.** If the surface frame is CP-invariant, its Yukawas are real: they give no
  phase to θ̄, but also no CKM phase J. The phase that the data need must then come from whatever splits the sectors.

## Weave or thread?

- **Weave-type.** The involution acts on the whole modular curve and on every section at once, and the claim concerns
  the surface frame's coupling for every pair of modes.
- **The tags.** Given Λ (GENESIS FK11), B1644's coupling (P-108 owed), the surface frame with GENESIS FK10's unit, and
  H-surf. H-end is used only for the read-out of W73's normalised form.

## Seen before the rule (disclosed)

- **W72's stored Y** (Y₀ = 2.0) has imaginary parts at most 1.1 × 10⁻⁸ against entries up to 7.2 × 10⁴. Its
  determinant is 1.23 × 10¹⁰, positive, and its eigenvalues are −76 597, +2 788 and −57.4.
- **The hand argument.** Define, for a section f of weight k, f*(τ) = C · conj f(−τ̄) with C = diag(1, 1, −1).
  - **T.** f*(τ + 1) = C conj(ρ(T))⁻¹ C⁻¹ f*(τ). With ρ_R(T) = e^{iπ/4} L⁻¹ and L real orthogonal, this is
    e^{iπ/4} C L C. Since C L C = L⁻¹, f* has f's T-law.
  - **S.** For τ in the upper half plane, conj((−τ̄)^k) = (−τ)^k = e^{−iπk} τ^k, so f*(−1/τ) = e^{−iπk} τ^k
    C conj(ρ(S)) C⁻¹ f*(τ).
    - With ρ_R(S) = e^{iπ/4} P and C P C = P, this is f's S-law exactly when e^{−iπk} e^{−iπ/4} = e^{iπ/4}, that is
      k ≡ −½ (mod 2): the weights −½, 3/2 and 7/2.
    - For ρ′ = ρ_R ⊗ χ_i at k = 5/2 the condition reads e^{−5iπ/2} e^{−3iπ/4} = e^{3iπ/4}. That holds.
  - **The basis.** C conj B[e_i] = B[e_i], C conj B[v₊] = C B[v₋] = B[v₊], and C conj B[v₋] = B[v₋]. So f* has
    coefficients conj(a) on the same lines and exponents.
  - **The consequence.** Each one-unit space is one-dimensional, with its normalising coefficient 1 real. So f* = f,
    and every section's coefficients are real. So is h's. G_αβ's coefficients are real, since B[l]·B[l′] ∈ {0, 1, 2}.
    G·h̄ at (−x, y) is the conjugate of its value at (x, y), and the fundamental domain is symmetric under x ↦ −x, so
    Y is real.
- **What follows, by hand.**
  - With one coupling for every sector, M_u ∝ M_d ∝ Y, so arg det(M_u M_d) = 2 arg det Y = 0 (mod 2π) for real Y,
    whatever its sign. So θ̄ = θ, and the CKM matrix is 1 with J = 0.
  - With different real couplings per sector, arg det(M_u M_d) ∈ {0, π}, and J = 0 still.

## The method (fixed here)

- **The identities, exactly (sympy):**
  - C L C = L⁻¹ and C P C = P;
  - the S-phase condition e^{−iπk} e^{−iπ/4} = e^{iπ/4} for ρ_R at k = −½, 3/2 and 7/2;
  - its ρ′ form, e^{−iπk} e^{−3iπ/4} = e^{3iπ/4}, at k = 5/2;
  - the condition's failure at k = ½ and 1, as a control;
  - C conj B[l] = B[l] for each eigenline.
- **The stored data, read without recomputation:**
  - W72's Y (both settings, as W73 rebuilt them): the largest |Im Y| over the largest |Y|;
  - W72's stored h coefficients: the largest |Im|;
  - W73's H-end form: the sign of its determinant.
- **The consequences, exactly:** arg det(Y Y) for the stored Y, and the CKM matrix of two identical sectors (the
  identity, J = 0).

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **V1, the involution (exact)** | C L C = L⁻¹ and C P C = P. The S-phase condition holds for ρ_R at k = −½, 3/2 and 7/2, and for ρ′ at 5/2, and fails at k = ½ and 1. C conj B[l] = B[l] on all three eigenlines. | 97% |
| **V2, the reality in the data** | W72's Y has \|Im\| below 10⁻¹² of its largest entry in both settings. h's stored coefficients have \|Im\| below 10⁻³⁰. | 92% |
| **V3, the consequences** | arg det(Y Y) = 0 to 10⁻¹². With one coupling the CKM matrix is 1, and J = 0. | 95% |

**The read-outs (no prior).**
- The signs of the determinants of W72's Y and W73's H-end form.
- The eigenvalue signs.

## The reading, written before the run (predicted)

- **The surface frame is CP-invariant.** The modular curve's orientation reversal τ ↦ −τ̄, combined with C, maps
  every section to itself. So the surface frame's Yukawas are real.
- **So in this frame the Yukawa half of I-18's price is paid.** With the record's one coupling, arg det(M_u M_d) = 0,
  so θ̄ = θ, and I-18 rests on the dictionary alone, as it read before B1246.
- **But the same symmetry forbids the CKM phase.** J = 0 here, and the data need J ≈ 3 × 10⁻⁵.
- **So whatever splits the sectors must also break CP.** For main's P-128, by hand and not computed: a flat line at a
  half-period is CP-even, so it keeps J = 0. A generic complex line breaks CP and can give J ≠ 0, but generically gives
  arg det M ≠ 0 too. That is the strong-CP problem in this frame's terms: the phase the data need in J, and must not
  have in θ̄, both come from one place.
- **The count stays all 19 of the 19 free** (18 if I-18 is earned). I-18 is not earned: its dictionary half stands.
  0 of 19.

## Discipline

- **The rule is committed before the script, and there is one run.** A failed launch (a crash before the read-out) is
  disclosed and fixed, and does not count.
- **Each cell is recorded as computed.** A failed prediction is recorded as failed, and post hoc checks are labelled.
