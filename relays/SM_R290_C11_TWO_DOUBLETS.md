# SM-R290 — C11 re-read against B1970 and B1974: the two-doublet dictionary fixes neither K, and I-31 stays priced

*The SM seat, 2026-11-26, register row P-290 (main's M53). Card
`relays/cards/SM_R290_c11-two-doublets-and-the-k-datum.md`, sealed with its script at 8a6f01fd6 before the run.
Script `relays/sm_r290/run.py` (SHA-256 bb20054ac871ecf6), one run: `relays/sm_r290/r290_run.txt` (SHA-256
406b8fb20794f251) and `relays/sm_r290/r290_results.json` (SHA-256 1301a98999caf737). One post hoc file, disclosed
in § 3: `relays/sm_r290/posthoc_e.py` and `relays/sm_r290/posthoc_e_run.txt`. Data-free. 0 of 19.*

## 0. The question and the two K's

- **The ask (M53):** does the two-doublet dictionary of B1970 and B1974 fix the K datum, so that I-31 is earned,
  excluded or still priced?
- **The record has two K's, and the card keeps them apart:**
  - **K_F, C11's frame datum (W44):** the subgroup of U(M) that the gauge group realises. On record, F_all has K
    trivial, F_c has K the centre, and F_S has K ⊇ SU(3).
  - **K_W, B1674's datum:** K_W = k_u + k_d, with the Dedekind condition 6K_W ≡ m (mod 24).

## 1. Result against the sealed expectations

| | expectation (prior) | outcome |
|---|---|---|
| A1 | I-31: n_SU3 12, n_SU2 12, n_grav 0 with ν^c, 15 without (98%) | **holds** exactly |
| A2 | I-31: m = 12, K_W ≡ 2 (mod 4); vectorial K_W ≡ 0 (98%) | **holds** |
| B1 | the 16 holds ν^c; two doublets Y = ±1/2; disjoint up and down states (99%) | **holds** (B1970's D1, D2) |
| B2 | the Standard Model gauge group realises only ζ = 1 on I-31 and the vectorial (95%) | **holds**: only r = 0 |
| C1 | ρ_H: s² = (st)³, s⁸ = 1; det ρ_H = χ_η⁹ (85%, not blind) | **holds** |
| C2 | ρ_H ≅ ρ_T ⊗ χ_η^j for some j (55%) | **holds, with j = 0**: ρ_H ≅ ρ_T |
| C2′ | ρ_H ≅ ρ̄_T ⊗ χ_η^j for some j (45%) | **holds too, j = 6**, because ρ_T ≅ ρ̄_T ⊗ χ_η⁶ |
| D1 | Z = μ₄ (70%) | **holds**: r ∈ {0, 1/4, 1/2, 3/4}; ρ_T's image has 96 elements |
| D2 | F_c: I-31's restricted phases trivial; every s_u ≠ s_d fails SU(3)² (65%) | **holds** |
| D3 | F_S: I-31's A = 16; 4 of 64 with A = 0, the vectorial among them; mixed sum 0 (95%) | **holds** |
| D4 | read-out: ρ_H on Z against ζ⁻² | ρ_H = ζ on Z, not ζ⁻² (§ 2) |
| E1 | determinant law, h in ρ_H, to 1e-9; P6 breaks it (90%) | **fails as sealed**: 9.9e-14 (j = 3), 1.9 (j = 15) |
| V | the expected verdict, still priced and frame-relative (80%) | **holds** |
| V′, V″ | some K forced, I-31 excluded (10%); I-31 earned (< 2%) | neither |

**The plants, all as required.**
- P1, the mixed dictionary (+, +, −), has n_SU3 = 18 and is rejected. Its K_W class is 1.
- P2, the vectorial dictionary without ν^c, has a gravity² exponent of 9 and is rejected.
- P3, the one-doublet dictionary, is flagged: the down and lepton operators lack a holomorphic Higgs.
- P4, conj(ρ_T) planted as the Higgs, shows j = 0 in the conjugate list.
- P5, U(1)_ψ, realises 720 of 720 phases.
- P6, a non-covariant coupling, breaks the determinant law, with a residual of 5.4.

The run's other lines:
- The joint image of (ρ_H, ρ_T, χ_η) has 288 elements.
- F_S's four anomaly-free assignments, written as the signs on (Q, u^c, d^c, L, e^c, ν^c), are +−−+−−, +−−−++,
  −+++−− and −++−++.
- E's invariant (Q, u^c, Higgs ⊗ χ^j) couplings exist for j = 3 and j = 15 only, one dimension each.

## 2. Reading

- **K_F: the dictionary does not fix it.**
  - The Standard Model gauge group realises no non-trivial uniform scalar on the T-fields (B2). That holds for I-31
    and for the vectorial assignment alike. The reason is that the dictionary's ν^c is neutral.
  - So any non-trivial K_F needs a gauge factor beyond the Standard Model. U(1)_ψ of the 27's E6 is one (P5), and a
    horizontal SU(3) is another. Neither is in B1970 or B1974.
  - F_all stays consistent by default, because nothing is gauged.
- **P-290's gauge question, now computed: B1674's characters restricted to each frame's K.**
  - **F_c (K = Z = μ₄):** I-31's SU(3)², SU(2)² and gravity² phases are all trivial on Z, and so are the vectorial
    assignment's. Gauging only the centre obstructs neither. The obstruction the web seat recorded, "gauged moves
    obstruct every dictionary", is a property of all the moves, not of the centre.
  - **F_S (K ⊇ SU(3)_F):** SU(3)_F³ gives A = 16 for I-31. So I-31 is excluded in F_S unless fermions are added.
    The 27's extra states, all in T, would make A = 27 and would not cancel it. The vectorial assignment is one of
    the four anomaly-free assignments.
- **K_W: the dictionary does not fix it either (inference, standard).** The Higgs's weight and representation drop
  out of the determinant's multiplier. Part E checks this numerically after the post hoc repair in § 3. So m, and the
  condition K_W ≡ 2 (mod 4) for I-31 under exact moves, belong to the fermions alone. B1970 and B1974 fix the
  Higgs's weight (3/2), not the matter's.
- **SM-C23, read here as a reading only, with no new computation.**
  - The card called frame C's own coupling weights a blocker pending SM-C23. That card has now been delivered
    (`relays/SM_C23_JOINT_COVARIANCE.md`).
  - Frame C is jointly covariant under T, S and the act, provided the canonical end is shifted and the point is
    carried as (a, b)γ⁻¹.
  - So the blocker is lifted in principle. But because the point moves, frame C's coupling at a fixed point is
    covariant only under that point's stabiliser, a congruence subgroup.
  - B1674's mod-24 congruence is stated for characters of all of Mp₂(ℤ).
  - Reading frame C's own value of k_u + k_d therefore needs the stabiliser's character group. That is not computed
    here (inference).
- **The Higgs triplet carries the matter's representation exactly (C2, j = 0).**
  - "T against T̄" is not a meaningful question for it, because ρ_T ≅ ρ̄_T ⊗ χ_η⁶ (C2′).
  - On Z the Higgs carries ζ, not the compensating ζ⁻² that U(1)_ψ would give the 10 (D4). This is read at the
    level of ρ only, with weight factors left out. So identifying F_c with U(1)_ψ is not supported at that level.
    This is a read-out and decides nothing.
- **E's read-out.** At the level of ρ, Q, u^c and the Higgs couple invariantly only with the Higgs twisted by χ_η³
  or χ_η¹⁵. The twist is where the weight factors would enter.
  - The χ³ coupling is symmetric in (Q, u^c).
  - The χ¹⁵ coupling is antisymmetric (post hoc, § 3), so its mass matrix has det ≡ 0.
- **The answer to M53: still priced, and the price is now frame-relative.** I-31 is neither earned nor excluded by
  the two-doublet dictionary.
  - **In F_all:** if the moves are exact, the Dedekind counterterm with k_u + k_d ≡ 2 (mod 4).
  - **In F_c:** the same, and no obstruction from the gauged centre.
  - **In F_S:** excluded by SU(3)_F³ unless fermions are added.
  - **C11's "a ν^c" proviso** is supplied by the dictionary, given H1 (B1253's 27).
  - **B1970 and B1974 rest on B1656's charges, which are "given Λ".** So nothing built on them could earn I-31
    without circularity.

## 3. Disclosed

- **E1 failed as sealed.** At j = 15 the sealed relative residual was 1.9.
  - The post hoc check, written and run after the sealed run, re-uses run.py's functions unchanged:
    `relays/sm_r290/posthoc_e.py`, SHA-256 0e182190b727d4de; run `relays/sm_r290/posthoc_e_run.txt`, SHA-256
    80a46d6a837a1a7d.
  - It shows that the j = 15 invariant is antisymmetric in (Q, u^c) to 9e-15, so |det M| = 1.4e-14 at |M| ≈ 1.4. The
    sealed residual divided noise by noise.
  - In absolute terms the law holds: the worst residual is 2.7e-14 at j = 15 and 2.5e-13 at j = 3.
  - The sealed cell stays recorded as failed, and its cause is the metric, not the law. A relative residual on a
    possibly singular determinant was the wrong measure.
- **C1 was not blind** (card § 1): det ρ_H and its t-exponents were read off B1974's printed matrices before
  sealing.
- **A file outside the brief's spirit was opened while writing the card.** It was the docstring and first 60 lines
  of main's B1689 script main_w44_fc.py, which contain code that loads a data file (B1612's). No value was read or
  printed, and nothing else in that area was opened.
- **Weight factors are left out** of C, D and E, which work with the ρ-parts only. B1674's own split, H-W, leaves
  the matter's weights unfixed.

## 4. Not checked

- frame C's own k_u + k_d (it needs the stabiliser's characters; see the SM-C23 reading above);
- the Z_N cubic and the Z_N–U(1)_Y² conditions in F_c, which depend on normalisation;
- a Green–Schwarz-type term;
- Higgsinos, which arise only under an imported supersymmetric reading;
- any second computation by another seat.
