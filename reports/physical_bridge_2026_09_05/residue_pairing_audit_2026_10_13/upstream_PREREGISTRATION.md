# B1642 — PREREGISTRATION: THE GOLDEN COUPLING AS THE ZERO MODES' RESIDUE AT THE PUNCTURE — is the weave's lowest coupling what its own zero modes give to a Higgs localized at the fibre's puncture?

cc (main), 2026-10-13. **Sealed before `residue_coupling.py` runs.** No data. 0 of 19. POINT_REGISTER slot Q3, first
arc (P-088; P-020, P-022, P-073 and P-087 in part). The owner: "if the principle is the seed, we miss the field."

**Why it matters.**
- The golden coupling (B1636, B1638, B1639) was found as a vector-valued modular form: a shape the weave allows, not a
  coupling anything computes.
- The frame audit's strongest unpursued lead (L251) is to compute couplings as overlaps of the fibre's own zero modes.
  That replaces free coefficients with computed ones.
- W49 shows the three generations are one zero mode three times, so overlaps in the bulk of the fibre cannot tell them
  apart (P-087(a)).
- This arc tests the one place a coupling can be computed and still separate the parities: the residue at the fibre's
  puncture. That is the point where W46's puncture conditions live.

**The derivation, by hand, written before the run** (θ_n(z; τ) in the πz convention, q = e^{iπτ}).
1. **The zero mode.** It is W21's F = (f(z), f(z + τ)) dz with f = θ₃(z; 2τ)/√θ₁(z; τ). In parity block p it is
   F_p = C_p F, with C_p the quaternion units j, i, k for the parities (½, 0), (0, ½), (½, ½).
2. **The shifted values.** From θ₃(z + τ; 2τ) = e^{−iπτ/2 − iπz} θ₂(z; 2τ) and
   θ₁(z + τ; τ) = −e^{−iπτ − 2πiz} θ₁(z; τ):
   - f(z + τ)² = −θ₂(z; 2τ)²/θ₁(z; τ);
   - f(z) f(z + τ) = ∓i θ₂θ₃(z; 2τ)/θ₁(z; τ), the sign set by the square root's branch.
3. **The duplication identities:** θ₃(z)θ₃(0) = θ₃² + θ₂², θ₄(z)θ₄(0) = θ₃² − θ₂² and θ₂(z)θ₂(0) = 2θ₂θ₃, each right side
   at (z; 2τ). With ε = j (the SU(2)-invariant form, gᵀεg = ε) this gives:
   - Fᵀ ε F = 0;
   - Fᵀ ε i F = ∓θ₂(z)θ₂(0)/θ₁(z);
   - Fᵀ ε j F = −θ₄(z)θ₄(0)/θ₁(z);
   - Fᵀ ε k F = i θ₃(z)θ₃(0)/θ₁(z).
4. **The coupling.** F_pᵀ ε F_q = Fᵀ ε C_p⁻¹C_q F. On the diagonal this is 0. Off the diagonal C_p⁻¹C_q is ± the third
   unit, so the entry is c·θ_r(0)θ_r(z)/θ₁(z), with r read off the third block's unit (i → θ₂, j → θ₄, k → θ₃). Each such
   entry is a section of the third block's parity character.
5. **At the puncture.** θ₁(z) ≈ πθ₂θ₃θ₄·z = 2πη³·z, so the residue at z = 0 is c·θ_r²/(2πη³).
   - A Higgs localized at the puncture, one component per parity, therefore couples by
     Y_pq = c_pq θ_r²/(2πη³), zero on the diagonal.
   - The singular values of a zero-diagonal symmetric matrix depend only on the moduli of its entries (the diagonal
     rephasing of B1636's sum rule). So Y has B1636's golden coupling's spectrum, which is 1 : φ⁻¹ : φ⁻² on every
     discriminant-5 geodesic (B1639).

## Seen first

`VERDICT topic-sweep /residue|puncture|zero mode|overlap|Yukawa|Szeg|duplication/: 128 of 1413 arcs on main match (NEGATIVE 19, OPEN 16, PROVED 92, RETRACTED 1)`
— none computes couplings as residues of the zero modes at the puncture. The nearest are object-era Yukawa arcs:
- B308: the texture is not forced by the object;
- B323: the ω-circulant Yukawa is tautological;
- B881 and B884: the E₆ cubic and its SM-graded support.
Read before this seal:
- B1636, B1638, B1639, B1640 and B1641;
- the SM seat's W21 (the zero mode's form), W41 (its weight) and W49 (one zero mode three times);
- the frame audit's referee reports (L251's overlap reading).
- the SM seat's commits to c5f343d14, read 2026-10-13 before this seal:
  - W56's result: the E₆ d–e identity; a Higgs like a generation has no coupling at 9/2; the dual triplet;
  - W57: not a typical draw, and the seed supplies the first step of hierarchy;
  - relay §66: a flat Wilson line is an allowed state of the field, and W59 is announced, "couplings as overlaps of the
    zero modes on the shared fibre" — the same question by another route, not yet run;
  - the W58 rule.
- Barger, arXiv:2609.09262 (abstract only): level-four modular symmetry read off the masses' pattern, a theta-constant
  parameterisation and a magnetized-torus completion. No golden pattern and no couplings from zero modes or punctures
  in its abstract.

**Literature:** the duplication (Landen) identities of Jacobi's theta functions; θ₁′(0) = θ₂θ₃θ₄ = 2η³; Yukawa
couplings localized at points or curves of an internal space (intersecting and magnetized brane models, where couplings
are theta functions with characteristics).

## Disclosed

- **Every prediction was derived by hand before the seal;** no cell was computed. The constants c (signs and a factor of
  i) come from the derivation, and the square root's branch fixes one sign. The cells allow either sign where the
  derivation leaves one.
- **The Higgs's localization at the puncture is a hypothesis, not derived.** So is its coupling through the residue: the
  natural pairing of a field on the puncture section with the zero modes' leading coefficients. The arc tests what
  follows from it, not the hypothesis itself.
- **R1 is an identity of form** (an antisymmetric form on one vector).
- **Everything is at zero Wilson line.** A flat Wilson line, an allowed state of the field (the SM seat's correction,
  relay §66), shifts the zero modes' elliptic argument and would deform the residue. Its effect is owed (POINT_REGISTER
  P-090).
- **This arc is sealed before the SM seat's W59 runs,** so that the two routes stay independent; they are compared after
  both (P-096).

## Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **R1** | Fᵀ ε F = 0 at 20 random (z, τ), to 1e-25 (a consistency check) | 99% |
| **R2** | for C ∈ {i, j, k}: Fᵀ ε C F = c_C θ_r(0)θ_r(z)/θ₁(z) with (C, r) = (i, 2), (j, 4), (k, 3) and c_i = ±1, c_j = −1, c_k = i, at 20 random (z, τ) to 1e-25 relative | 85% |
| **R3** | the residue at z = 0 of each, computed by a contour integral of radius 0.05, equals c_C θ_r(0)²/(πθ₂θ₃θ₄) = c_C θ_r²/(2πη³) at 10 random τ, to 1e-20 relative | 85% |
| **R4** | Y_pq = Res F_pᵀ ε F_q (F_p = C_p F, C_p = j, i, k) has zero diagonal; its singular values equal those of B1636's golden coupling [[0, θ₄², θ₃²], [θ₄², 0, θ₂²], [θ₃², θ₂², 0]] at 10 random τ to 1e-15 relative; on the tick's axis (5 points) they are 1 : φ⁻¹ : φ⁻² to 1e-15 | 85% |
| **R5** | each off-diagonal g_r(z) = Fᵀ ε C F is a section of the third block's parity character: g_r(z + 1) = χ(a) g_r(z), g_r(z + τ) = χ(b) g_r(z), with (χ(a), χ(b)) = (+1, −1) for θ₂, (−1, +1) for θ₄, (−1, −1) for θ₃, at 10 points | 90% |
| **R6** | control: the non-invariant bilinear B = diag(1, 2) gives FᵀBF that factors as const·θ_r(0)θ_r(z)/θ₁(z) for no r (best relative misfit > 1e-3) | 90% |

**The reading, written before the run (the cells can only lower it).**
- **If R1–R5 hold,** the weave's lowest coupling is no longer a free shape. It is the coupling the zero modes themselves
  give to a Higgs localized at the fibre's puncture and carrying parity.
  - The SU(2)-invariant pairing kills the diagonal.
  - The duplication identities put a theta constant in each off-diagonal entry; the residue puts in the second one.
  - The golden spectrum on the discriminant-5 geodesics is then the zero modes' own, given that Higgs. The free-number
    count drops to τ and the Higgs's three components at the puncture.
  - This is a field the principle locates: its own puncture, where W46's end conditions live. It is not tacked on.
- **If R2 or R3 fails,** the identities or the residue are wrong as derived, and the arc names where.
- **If R4 fails while R2–R3 hold,** the pairing of blocks to theta constants differs from B1636's in a way that changes
  the moduli, and the coupling is not B1636's.

## Instruments

`verification/residue_coupling.py` (mpmath at 40 digits, the theta functions as series in τ); hashes in
`ARTIFACT_HASHES.txt`.
