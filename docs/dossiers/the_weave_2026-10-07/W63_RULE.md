# W63 — the rule, recorded before the code

The SM-derivation seat, 2026-10-14. Committed before the code that reads it exists. What the seat worked by hand while
drafting is listed under "Seen before the rule", and the priors were set after that. Nothing here is a result.

## Why this arc

- **The owner chose "Verify B1644 (Recommended)"** (2026-10-14), after W62.
- **What main found.**
  - **B1644** (sealed `8fa3d82ba`; NEGATIVE as sealed, the structure proved). A Higgs in the adjoint of the quaternion
    structure, which is canonically the multiplicity space M, couples to the zero modes at the puncture. The coupling is
    symmetric with a non-zero diagonal. det Y(a) = (R·R)(a·a)(R·a), and Jacobi's identity makes the theta triplet R
    isotropic, so one generation is exactly massless for every direction and every τ.
  - **B1645** (PROVED): Y(a) = a Rᵀ + R aᵀ − (a·R)𝟙. For a real direction the other two masses have a ratio
    m ∈ [½, 1]. The ratio is 0 on the isotropic cone a·a = 0, and grows linearly with the distance from it.
- **What main asks (S120, P-115).** Does any content or potential on the seat's record fix a Higgs direction in M, near
  the isotropic cone? Does W60's parity Higgs, read as a section of the adjoint, have a direction at the selected line?
- **This arc verifies B1644 and B1645 with the seat's own code** ("repo first", and verify even what is proved) and
  answers P-115 from the record.

## Weave or thread?

- **Weave-type.** The zero modes are the weave's T on the shared fibre (W21, W49), and the Higgs is the weave's adjoint
  datum, all three generations at once.
- **The tags.** Given Λ (GENESIS FK11). Given B1644's coupling at the puncture, which is a hypothesis: its physical
  existence needs the audit lane's parent map (P-108).

## Seen before the rule (disclosed)

- **Main's instruments were read before the rule:** B1642's definitions, B1644's instrument and output, and B1645's
  findings. The conventions agree with the seat's:
  - the units QI = diag(i, −i), QJ = [[0, 1], [−1, 0]], QK = QI QJ;
  - ε = QJ;
  - the blocks C_p = j, i, k for (½, 0), (0, ½), (½, ½) (W61's BLOCKS);
  - the coupling Y(a)_pq = Res_{z=0} (C_p F)ᵀ ε Φ(a) (C_q F), with Φ(a) = Σ a_u u.
- **The residues, by hand.** Write F = (f(z), f(z + τ)) and Fᵀ ε X F = x₂₁ f² + (x₂₂ − x₁₁) f f′ − x₁₂ f′², where
  f′ = f(z + τ).
  - Res f² = θ₃(0 | 2τ)²/(2πη³) = (θ₃² + θ₄²)/(2 · 2πη³).
  - Res f′² = −θ₂(0 | 2τ)²/(2πη³) = −(θ₃² − θ₄²)/(2 · 2πη³).
  - Res f f′ = ∓i θ₂²/(2 · 2πη³), by duplication. The sign is the branch of √(θ₁(z) θ₁(z + τ)), a convention.
  - So R_i = ∓θ₂²/(2πη³), R_j = −θ₄²/(2πη³), R_k = iθ₃²/(2πη³), as main's table has them. R·R ∝ θ₂⁴ + θ₄⁴ − θ₃⁴ = 0
    by Jacobi, whatever the sign of R_i.
- **B1645's form, by hand, for any convention.** For any linear ρ on the quaternions with ρ(1) = 0 and ρ(u) = R_u:
  - −e_p e_u e_p is e_p if u = p, and −e_u otherwise;
  - −e_p e_u e_q (p ≠ q) is e_q if u = p, e_p if u = q, and ±1 otherwise.
  - So Y(a) = a Rᵀ + R aᵀ − (a·R)𝟙 in the units' labels, whatever the sign of R_i.
- **W60's Higgs as a direction, by hand.**
  - At a line w, the parity copy p is untwisted exactly when p + 3w ≡ 0. That has at most one solution p, so at most one
    copy is massless. At a half-period line it is p* = w (W60, W61), with the unit C_{p*} as its direction (W61's rule).
  - So the record's Higgs has a real direction e_u up to a phase, and B1645 gives m ≥ ½.
  - On τ = iy, R = (α, β, ig) with α, β, g real and g² = α² + β², so e_k lies in R's plane, and Y(e_k) has singular
    values 2g, g and 0: m(e_k) = ½ exactly.

## The method (fixed here)

- **Own instruments.** Theta functions from mpmath's jtheta at 30 digits, not B1642's series. 2πη³ = π θ₂θ₃θ₄.
- **Route 1, contour.** The residue of each single-valued product (f², f′², and f f′ with the branch constant written
  out) by the trapezoid rule on |z| = 0.04 with 96 points.
- **Route 2, closed forms.** The duplication forms above.
- **W21's branch.** W21's F, with principal square roots per factor as W61's Q3 evaluates it, is compared with the
  single-valued forms at 20 points near the contour. The cell reports the sign it gives to R_i.
- **The τ set.** i, ω, 4i, 2.0207i (W62's largest axis member), and six seeded random τ in the fundamental domain with
  0.8 ≤ y ≤ 2.
- **The coupling.** Y(a)_pq by residues of (C_p F)ᵀ ε Φ(a) (C_q F) directly, not through the identity.
- **The spectra.** Singular values in double precision, normalized by the largest. m = s₂/s₁.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **V1, the residues** | At the ten τ, the contour residues of Fᵀ ε u F equal the closed forms to 10⁻²⁰ relative, for u = i, j, k, with Res Fᵀ ε F = 0. R_j and R_k equal main's table; R_i equals it up to the branch sign, which W21's principal-branch F fixes (reported). | 90% |
| **V2, the structure** | At the ten τ, Y(e_i), Y(e_j), Y(e_k) and Y(a) for five seeded complex a are symmetric (to 10⁻²⁰) with a non-zero diagonal. Each equals a Rᵀ + R aᵀ − (a·R)𝟙 to 10⁻²⁰, with R the seat's residues, in the units' labels. | 95% |
| **V3, Jacobi** | At the ten τ: \|R·R\|/\|R\|² < 10⁻²⁰; Y(a) R = 0 and det Y(a) = 0 (relative 10⁻²⁰) for the five complex a. | 97% |
| **V4, the half bound and the cone** | At the ten τ: over 2000 real directions (a Fibonacci sphere), min m ≥ ½ − 10⁻¹⁰ and max m ≤ 1. m = ½ in the plane of Re R and Im R, and m = 1 normal to it (10⁻¹⁰). m < 10⁻¹⁰ on 200 seeded isotropic a. Near the cone, the log-log slope of m against \|a·a\|/\|a\|² is 1 within 2%. | 92% |
| **V5, W60's Higgs as a direction (P-115)** | For each unit e_u and each τ in {i, 1.5i, 2.0207i, 4i, ω} and W62's six arc points: m(e_u) ≥ ½ − 10⁻¹⁰. On the four axis points m(e_k) = ½ to 10⁻¹⁰. So the selected line's Higgs (p* = (½, ½), direction k) gives masses 0 : 1 : 2 on the imaginary axis. | 90% |
| **V6, main's numbers** | Main's five S3c examples at τ = 4i (directions regenerated from B1644's Fibonacci sphere, matched to the printed 4 digits): the seat's normalized singular values equal the printed ones to 10⁻⁷. | 85% |

**The read-outs (no prior).**
- m(e_u) at τ = ω for each unit, and along W62's axis members.
- The direction of R/|R| at τ = 4i and 8i, against main's cusp limit (0, −1, i)/√2.
- How close to the cone a direction must be for the observed second-to-third ratios: |a·a|/|a|² at m = 0.004, 0.02 and
  0.06 (from the near-cone fit; context, not a test).

## The reading, written before the run (predicted)

- **B1644's coupling and B1645's identity hold on the seat's own instruments.** One generation is exactly massless for
  every Higgs direction and every τ, by Jacobi. The other two have a ratio set by the direction alone.
- **P-115, from the record.** Nothing on the seat's record puts the Higgs near the isotropic cone.
  - W60's line makes at most one parity copy massless, so the record's Higgs has one real unit direction. B1645 then
    gives m ≥ ½.
  - On the imaginary axis, where W62's runaway goes, m = ½ exactly: the masses are 0 : 1 : 2.
  - No content or potential on record supplies a complex direction. The cone needs two massless copies with a relative
    phase ±i, which no line gives.
- **So the hierarchy between the second and third generations needs a datum the record lacks.** That datum would be a
  direction near the isotropic cone, with |a·a|/|a|² of a few percent: an end condition, or a second massless Higgs.
- **The count stays all 19 of the 19 free** (18 if I-18 is earned). 0 of 19.

## Discipline

- **The rule is committed before the script, and there is one run.** A failed launch (a crash before the read-out) is
  disclosed and fixed, and does not count.
- **Each cell is recorded as computed.** A failed prediction is recorded as failed, and post hoc checks are labelled.
