# W72 — the rule, recorded before the code

The SM-derivation seat, 2026-10-14. Committed before the code that reads it exists. What the seat worked by hand while
drafting is listed under "Seen before the rule", and the priors were set after that. Nothing here is a result.

## Why this arc

- **Main's S122 relay, §2, assigns it.** "In the surface frame τ is a coordinate integrated over. So a hierarchy there
  cannot be 'a power of |q| at a chosen Im τ'; it is an overlap integral over the surface, with the Higgs's departure
  from the cone weighted near the cusp. That removes the free Im τ, but it needs the overlap integrals, which neither
  record has."
- **The reading came first** (the dossier's "Reading: the end's field against main's B1649, by frame; and the surface
  frame's overlap", 0c3082d4a). It found the one canonical overlap and its limit.
- **The owner's order** is "we look what fixes τ then we count free numbers". In the surface frame τ is integrated over,
  so whatever this arc finds carries no free τ.

## Weave or thread?

- **Weave-type.** The surface frame's modes are vector-valued forms of the whole modular group, so every move acts at
  once. The overlap integrates over every τ, with none chosen.
- **The tags.**
  - Given Λ (GENESIS FK11) and B1644's coupling (P-108's parent map owed).
  - The surface frame is the frame of W45, W46 and W64, with the three chiral modes carrying one unit each at the
    cusp. That is GENESIS FK10's unit, a tagged working postulate.
  - H-surf (new): the Higgs is a zero mode of the surface frame, so it enters the four-dimensional overlap through
    its conjugate, as a gauge field's internal component does.

## Seen before the rule (disclosed; by hand, from the record's code and its stored outputs)

- **The modes.**
  - The matter modes are F_i, F₊ and F₋: weight 3/2 in ρ_R, one unit each at the cusp on e_i, v₊ and v₋. They span
    the three-dimensional space with end data (1, 1, 1) (W64's K5; W68; W69 solved them).
  - The residue triplet is R: weight −½, one unit on v₊ (W64, W65).
  - The conventions: ρ_R(T) = e^{iπ/4} L⁻¹ and ρ_R(S) = e^{iπ/4} P, with f(−1/τ) = τ^k ρ(S) f(τ). The eigenlines e_i,
    v₊ and v₋ have exponents ⅛, ⅞ and ⅜.
- **The multipliers.**
  - B[l]·B[l′] is non-zero only for (e_i, e_i), equal to 1, and for (v₊, v₋), equal to 2. Their exponent sums are ¼
    and 5/4. So every dot product of two ρ_R forms has exponents in ¼ + ℤ: multiplier i under T, and i τ^{k₁+k₂}
    under S.
  - B1644's coupling between two matter modes, f_αβ(a) = F_αᵀ Y(a; R) F_β, is a sum of products of two dot products.
    It has weight 2, multiplier −1 under T and −τ² under S: η¹²'s multiplier. So f = η¹² g with g of weight −4 and
    level 1. Its exponents lie in ½ + ℤ, so it has no constant term and no residue at the cusp. No holomorphic
    weight-2 form with that multiplier exists (η¹² M₋₄ = 0).
- **The canonical overlap.**
  - Write f_αβ(a) = a · G_αβ, with G_αβ = (R·F_β) F_α + (R·F_α) F_β − (F_α·F_β) R. It is symmetric in α and β, of
    weight 5/2, and of type ρ′ = ρ_R ⊗ χ_i: ρ′(T) = e^{3iπ/4} L⁻¹ and ρ′(S) = e^{3iπ/4} P.
  - ρ′ is unitary, so ⟨G, h⟩ = ∫_F G · h̄ y^{5/2} dμ is invariant for h of the same weight and type.
  - W45's formula at k = 5/2 for ρ′ (by hand): tr ρ′(S) = e^{3iπ/4}, tr ρ′(ST) = 0, and the exponents are ⅜, ⅛ and ⅝.
    χ = 3·(3/2)/12 + ¼ Re(e^{5iπ/4} e^{3iπ/4}) + 0 + 3/2 − 9/8 = 1. So dim M_{5/2}(ρ′) = 1, and it is cuspidal, since
    no exponent is 0. The Higgs's surface mode h is unique up to scale.
  - The pairing converges. Above any height the x-integral keeps only equal exponents, h has none below ⅛, and so the
    growing part of G never meets h.
- **What is physical.** The three modes grow at the cusp (their units), so their Petersson norms diverge. Without a
  normalisation, only basis-free facts about the bilinear form Y_αβ are physical: chiefly its rank. Mass ratios need
  the modes normalised.

## The method (fixed here)

- **The sections** at 40 digits with W65's and W68's collocation (`the_residual_charges_at_omega.py`, `solve`):
  - F_i, F₊ and F₋ at weight 3/2, one unit each;
  - E, R and R′ at weight −½;
  - each normalised by its leading coefficient. For each, the line with the smallest residual is kept, as W69 did.
- **The Higgs's surface mode h.**
  - The same collocation for ρ′ at weight 5/2, with no units: q-exponents ⅜ + n, ⅛ + n and ⅝ + n on e_i, v₊ and v₋.
  - The dimension first, in double precision (the singular-value null count, as W45's `dims` does). Then the 40-digit
    solve, normalised on the line whose lowest coefficient is largest in the double-precision null vector.
- **The q-series.** Each section's terms are kept with exact exponents, n + λ in eighths. The dot products and G_αβ
  are formed as series: products of terms, with B[l]·B[l′] as above.
- **The pairing** Y_αβ = ∫_F G_αβ · h̄ y^{½} dx dy, in two parts:
  - **above Y₀:** Σ over lines of w_l Σ_E g_E h̄_E Γ(3/2, 4πE Y₀)/(4πE)^{3/2}, with w = (1, 2, 2) the B-norms, and E
    each exponent present in both, with E > 0;
  - **below Y₀:** Gauss–Legendre in x on [−½, ½] and in y on [√(1 − x²), Y₀], with the sections evaluated in double
    precision from their series.
  - **Two settings:** (Y₀, nodes) = (1.25, 64) and (2.0, 96).
- **The rank.** The singular values of the 3 × 3 matrix Y in the basis (F_i, F₊, F₋). Rank is basis-free; the values
  themselves are not, and are read out only.
- **The multiplier checks.** f_αβ(a) and G_αβ are evaluated at W65's first five sample points, at τ + 1, and at −1/τ.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **X1, the multipliers (exact)** | B[l]·B[l′] is non-zero only on (e_i, e_i) and (v₊, v₋), with exponent sums ≡ ¼ (mod 1). Every exponent of every f_αβ(a) series, for all six pairs (α, β) and a ∈ {E, R, R′}, lies in ½ + ℤ. G_αβ's exponents on (e_i, v₊, v₋) lie in ⅜ + ℤ, ⅛ + ℤ and ⅝ + ℤ. | 97% |
| **X2, the multipliers (numerical, the record's sections)** | At the five sample points, f(τ + 1) = −f(τ) and f(−1/τ) = −τ² f(τ). G(τ + 1) = ρ′(T) G(τ) and G(−1/τ) = τ^{5/2} ρ′(S) G(τ). All to 10⁻¹⁰ relative, for all six pairs and all three a. | 90% |
| **X3, the Higgs's surface mode** | χ_{5/2}(ρ′) = 1 by W45's formula. The collocation's null count at weight 5/2 for ρ′ is 1, with a gap above 10⁻⁶ against below 10⁻⁹. The 40-digit solve has relative residual below 10⁻²⁰. | 80% |
| **X4, the Yukawa's rank** | Y_αβ agrees between the two settings to 10⁻⁸ relative, entry by entry. Its smallest singular value is above 10⁻⁶ of its largest. So Y has rank 3, and in the surface frame B1649's first-generation zero is lifted. | 70% |
| **X5, the modes' norms** | Each of F_i, F₊ and F₋ has a non-zero coefficient at a negative exponent (−⅞, −⅛ and −⅝). So ∫_F \|F\|² y^{3/2} dμ diverges for each, and the three are not normalisable. | 97% |
| **X6, the verdict** | The surface frame's Yukawa is parameter-free in shape (no τ), with rank 3, but carries no mass ratio until the three modes are normalised, which needs a source at the cusp (P024; GENESIS FK10). The count does not drop. | 70% |

**The read-outs (no prior).**
- Y's singular values in the basis (F_i, F₊, F₋). They are basis-dependent, so they are not masses.
- h's first coefficients on each line.
- The part of Y from above Y₀ and from below it.
- f_αβ(a)'s lowest exponent for each pair and a.

## The reading, written before the run (predicted)

- **In the surface frame, τ is gone and so is the first-generation zero.** The overlap pairs the matter's coupling
  vector with the Higgs's unique surface mode. It is a fixed bilinear form with no free number, and its rank is 3:
  B1649's zero belongs to the fibre frame at fixed τ, where R(τ) is one vector. The surface integrates over the family
  of R(τ), which spans more than one line.
- **But the surface frame does not yet give masses.** The three generations exist there only with a unit at the cusp,
  and that unit makes them grow. They are not normalisable, so their kinetic terms, and with them every mass ratio,
  are undefined.
- **So the surface frame meets P024 at its own end.** A source at the cusp would make the modes normalisable: the field
  at the edge. The same edge decides the count (W46), the field (W71), and now the masses.
- **The count stays all 19 of the 19 free** (18 if I-18 is earned). 0 of 19.

## Discipline

- **The rule is committed before the script, and there is one run.** A failed launch (a crash before the read-out) is
  disclosed and fixed, and does not count.
- **Each cell is recorded as computed.** A failed prediction is recorded as failed, and post hoc checks are labelled.
- **The scope.** Λ's frame (P-108 owed) and the surface frame. No data are used.
