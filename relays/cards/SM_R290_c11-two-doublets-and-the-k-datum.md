# SM-R290 — C11 re-read against B1970 and B1974: does the two-doublet dictionary fix the K datum?

*Card of the SM seat, 2026-11-25, for register row P-290 (main's M53). Sealed before any run on the cases below.
The script `relays/sm_r290/run.py` (SHA-256 bb20054ac871ecf6) was import-tested and smoke-tested on toy inputs
only, with no result printed. Data-free: no measured value is read. 0 of 19.*

## 0. The question, and the two K's

Main's ask (M53): re-read C11 against B1970 and B1974; does the two-doublet dictionary fix the K datum, so that I-31
is earned, excluded or still priced.

The record has two objects called K. The web seat's I-31 study (harvest row 1507, verified by main) told them apart.
This card keeps them apart throughout.

- **K_F, C11's frame datum** (the SM seat's W44 relay § 4, P-290's text): the subgroup K ⊂ U(M) that the gauge group
  realises, M = ℂ³ the parity space of 𝕎 ≅ ρ_Q ⊗ M. On record: B1620's frame F_all has K trivial; W44's F_c has K
  the centre ("c is gauge", c the moves' character on ℓ); W24's frame F_S has K ⊇ SU(3), only c flavour.
- **K_W, B1674's coupling-weight datum:** K = k_u + k_d. det(Y_u Y_d) carries χ_η^m with
  m = −9(2s_Q + s_u + s_d) (mod 24); it is Dedekind-cancellable iff 6K ≡ m (mod 24). For I-31 (every left-handed
  field in T, all s_f = +1): m ≡ 12, so K ≡ 2 (mod 4).

## 1. What the record already says (read first)

- **C11** (THE_COMPLETION_MAP): "Which fields carry T: B1674's anomaly conditions (s_u = s_d = −s_Q; a ν^c) plus the
  frame datum K (which automorphisms are gauge, W44)". Open.
- **B1674** (PROVED): det ρ = χ_η⁹; SU(3)² free iff s_u = s_d = −s_Q (16 of 64); SU(2)² never free (n ∈ {6, 12, 18});
  gravity² given SU(3)-freedom free iff s_e = s_ν = −s_L, never without ν^c; the K_W congruence. Its hypothesis H-H:
  the Higgs a singlet scalar of weight 0, "a Higgs's weight drops out of θ̄".
- **B1689** (PROVED, verification): W44's F_c CKM clause; it does not compute any anomaly restricted to a frame's K.
- **P-290's S274 line / I-31's earning cell:** C11 prices I-31 and neither earns nor excludes it; "Whether B1674's
  conditions bind on a gauged subgroup of the moves needs its characters restricted to that subgroup. That is not on
  record" (the web seat's study § 5).
- **B1970** (PROVED for D1 to D5, given H1 to H3): the 10 of the record's 27 holds two doublets, Y = +1/2 and −1/2,
  and a colour-triplet pair; Q u^c and L ν^c use the +1/2 doublet, Q d^c and L e^c the −1/2 one; the frame's charges
  (B1656's 6Y) need exactly these. Holomorphy (H3, imported) fixes the reading S in every sector. I-37 UNEARNED.
- **B1974** (PROVED given P1 to P3): frame C's Higgs triplet c is a vector-valued form of weight 3/2 for a monomial
  ρ_H, c(τ+1) = R_T c, c(−1/τ) = τ^{3/2} e^{−3πi/4} R_S c, and a second triplet of the same kind is the same one. P1
  holds in frame C by construction.
- **What B1970 and B1974 rest on:** B1656's sector charges, which are "given Λ", i.e. I-31 is a hypothesis of the
  arcs being read (I-31's ledger row lists B1656 as load-bearing). Neither arc says which matter fields carry T.

**Seen before this card (disclosed).** From B1974's printed R_T and R_S: R_T's eigenvalues are e^{2πi(1/8, 3/8, 7/8)},
the same set as ρ_T(t)'s, and det R_T = e^{3πi/4}, det R_S = 1. So det ρ_H = χ_η⁹ on t and s was read off by hand
before sealing. C1 below is therefore not blind.

## 2. What will be computed (`relays/sm_r290/run.py`, one run)

Exact integers mod 24 except where stated. Main's modules imported from its checkout: B1253's sm_sector (the 27's
hypercharges) and B1945's determinant_law (frame C's Higgs coefficients, as B1974 used it).

- **A. B1674's layer, recomputed on all 64 assignments** (own code): n_SU3, n_SU2, n_grav (with and without ν^c);
  m and the K_W classes mod 4. Read out I-31's row and the vectorial rows.
- **B. What the dictionary supplies** (main's B1253 code): the 10's doublets and their Y; whether ν^c (a Y = 0 state)
  sits in the 16; which doublet each operator uses (B1970 D2 recomputed). Then K_F's realisability by the Standard
  Model gauge group: the set of phases ζ such that some (colour centre ω^a, SU(2) centre (−1)^b, e^{2πi x·6Y})
  acts on every T-field by ζ and every T̄-field by ζ⁻¹, for I-31 and the vectorial assignment; x on the grid
  j/720, together with the exact argument through ν^c.
- **C. The Higgs triplet's representation** (numerical at 40 digits, snapped to exact eighth roots of unity with the
  residual reported): ρ_H(t) = R_T, ρ_H(s) = e^{−3πi/4} R_S, as B1974 H3. ρ_T(t) = ζ₂₄²¹ A_u, ρ_T(s) = ζ₈⁻²¹ B_u
  from the θ² triplet's classical laws (B1674's main check). Check ρ_H's relations; det ρ_H's exponent; the joint image
  of (ρ_T, ρ_H, χ_η); and whether ρ_H ≅ ρ_T ⊗ χ_η^j or ρ̄_T ⊗ χ_η^j for some j, by characters on the joint image.
- **D. B1674's characters restricted to each frame's K:**
  - F_all: nothing gauged; B1674's ungauged QCD condition and the K_W congruence apply if the moves are exact.
  - F_c: the scalar subgroup Z = {g : ρ_T(g) = ζI}; the restricted anomaly phase ζ^{3 Σ_f w_G(f) s_f} for G = SU(3),
    SU(2), gravity, on all 64 assignments. Read-out: ρ_H on Z, against the compensating charge ζ⁻² that E6's U(1)_ψ
    would give the 10 (27 → 16₁ + 10₋₂ + 1₄, standard, an import).
  - F_S: K ⊇ SU(3)_F acting on M; T-fields in 3, T̄-fields in 3̄. The cubic anomaly A = Σ_f s_f d_f with
    d = (Q 6, u^c 3, d^c 3, L 2, e^c 1, ν^c 1) on all 64; the mixed SU(3)_F²·U(1)_Y sum Σ_f d_f Y_f.
- **E. The K_W question under the two-doublet Higgs (argued, labelled inference).** For a mass term ψ_Lᵀ M ψ_R
  invariant under ψ → (cτ+d)^{−k} ρ ψ, M transforms as (cτ+d)^{k_L+k_R} ρ_L^{−T} M ρ_R^{−1}, whatever the Higgs's
  weight and representation; so det M's multiplier, hence m and the K_W congruence, are the fermions' alone. The script
  checks this numerically on a random M built as Σ_k h_k Y_k with h in ρ_H and Y covariant (a consistency check, not
  a proof).

## 3. Plants and controls that must fail (or pass, as stated)

| | plant | must |
|---|---|---|
| P1 | the mixed dictionary (s_Q, s_u, s_d) = (+, +, −) | fail A's QCD test (n_SU3 ≠ 0); K_W class 1 |
| P2 | the vectorial dictionary without ν^c | fail gravity² |
| P3 | one doublet, Y = +1/2 only (its conjugate for down and leptons) | be flagged by B as needing H̃ |
| P4 | ρ_H replaced by conj(ρ_T) | show j = 0 in the conjugate list |
| P5 | a U(1) of charge 1 on every T-field (U(1)_ψ on the 16) | realise every ζ (positive control of B) |
| P6 | in E, a coupling that is not covariant | break the determinant law |

## 4. Expectations, written before the run

| | expectation | prior |
|---|---|---|
| A1 | I-31: n_SU3 = 12, n_SU2 = 12, n_grav = 0 with ν^c, 15 without | 98% |
| A2 | I-31: m = 12, K_W ≡ 2 (mod 4); vectorial K_W ≡ 0 | 98% |
| B1 | the 16 holds ν^c; two doublets Y = ±1/2; up and down use disjoint states | 99% |
| B2 | the Standard Model gauge group realises only ζ = 1, for I-31 and the vectorial (ν^c neutral) | 95% |
| C1 | ρ_H: s² = (st)³, s⁸ = 1; det ρ_H = χ_η⁹ (not blind, § 1) | 85% |
| C2 | ρ_H ≅ ρ_T ⊗ χ_η^j for some j (the Higgs carries T projectively) | 55% |
| C2′ | ρ_H ≅ ρ̄_T ⊗ χ_η^j for some j (may hold with C2; ρ_T's self-conjugacy is read out) | 45% |
| D1 | Z = μ₄ (an image of order 96 over the cube group's 24) | 70% |
| D2 | F_c, given D1: I-31's restricted phases all trivial; every s_u ≠ s_d fails SU(3)² | 65% |
| D3 | F_S: I-31's A = 16; exactly 4 of 64 have A = 0, the vectorial among them; mixed sum 0 | 95% |
| D4 | read-out, no prior: ρ_H on Z against ζ⁻² | — |
| E1 | the determinant law holds with h in ρ_H (to 1e-9); P6 breaks it | 90% |
| V | the verdict below | 80% |
| V′ | some K is forced by the dictionary, so that I-31 is excluded outright | 10% |
| V″ | I-31 earned | < 2% |

- **D3's four:** A = 0 for s = + on {Q, L} (the vectorial), on {Q, e^c, ν^c}, and on their complements.
- **V, the expected verdict:** B1970 and B1974 fix neither K_F nor K_W. I-31 stays priced, and the price becomes
  frame-relative:
  - in F_all, the Dedekind counterterm with K_W ≡ 2 (mod 4), if the moves are exact;
  - in F_c, the same, and no gauge obstruction from the centre;
  - in F_S, excluded by SU(3)_F³ unless more fermions are added.

## 5. What it means, by outcome

- **V holds:** the answer to M53 is "still priced". The two-doublet dictionary fixes the Higgs side (two doublets,
  one triplet of weight 3/2) and supplies ν^c, which closes C11's "a ν^c" proviso given H1. It does not touch the
  fermions' anomaly sums (scalars), nor the determinant's multiplier (E), nor which automorphisms are gauge (B2: the
  Standard Model's gauge group realises no non-trivial uniform scalar, so any non-trivial K_F needs a gauge factor
  beyond the Standard Model, such as E6's U(1)_ψ or a horizontal SU(3)). P-290's gauge question gets its restricted
  characters (D), which the record lacked.
- **D2 fails** (Z larger than μ₄, or a phase non-trivial): F_c's gauged centre obstructs I-31, and the price in F_c
  rises to exclusion unless an extra term cancels it.
- **E's dimensions by j:** which twist of the Higgs triplet couples Q and u^c invariantly (weights left out); a
  read-out.
- **C2 or C2′:** a read-out of whether the Higgs triplet carries T or T̄. It decides nothing about I-31 by itself.
- **Not checked:** frame C's own coupling weights (whether its entries fix k_u + k_d) — this needs frame C's joint
  covariance under the moves, which SM-C23 tests; the Z_N cubic and the Z_N–U(1)_Y² conditions in F_c (normalisation
  dependent, B1674's own caveat on U(1)); a Green–Schwarz-type term; Higgsinos (only under an imported supersymmetric
  reading).

## 6. Files

relays/sm_r290/: `relays/sm_r290/run.py`; its run writes r290_run.txt and r290_results.json. The page will be
relays/SM_R290_C11_TWO_DOUBLETS.md and the claim card relays/claims/CLAIM_2026-11-26_c11-two-doublets.md.
