# W-B2, corrected: with the Szegő zero alone moved to the Higgs's point h = c·q_H·w, frame D1's coupling, at residue level, is covariant under τ ↦ τ + 1 and τ ↦ −1/τ, and periodic in w, at c = ±2. At c = −2 it is frame C's coupling transposed (the same singular values); at c = +2 it is frame C at the charges (2q_L + q_R, q_L + 2q_R). B1947's twisted triplet stays non-covariant, and the Higgs's sign does not act as the reading. No mixing computed

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` (data-free). It replaces the headline and § 2 of
`CHAT1_TO_CC_2026-11-15_W-B2_FRAME_D1S_COUPLING_IS_NOT_COVARIANT_IN_EITHER_PLACEMENT.md` (5bcee3bcb). That note was
withdrawn in part at 028709f3f, and the withdrawal stands. Card W-B2 (7557aa1f5); M34.

**Under the author's ruling of 2026-11-15** (outputs computed; no data, no comparison). **No mixing** was computed.

**The error, and how it was found.**
- Stage 1's K2 shifted more than the Szegő zero.
- Frame C's bilinear factorises as v_x(u) v_y(u)ᵀ / θ₁(u, τ), with v = (θ[a, b](u, 2τ), −i θ[a + ½, b](u, 2τ)). The
  factors e^(−iπu) (in den) and e^(−2πiu) (inside θ₁(u + τ)) belong to the matter doublets.
- The first build moved them too. So it was the correct placement conjugated by diag(1, e^(iπh)), which is not unitary,
  and it was not periodic in the Higgs's point.
- The referee of the first note found this, and computed the corrected placement without sealing it. This stage
  recomputes it, sealed, and is **not blind** to that computation.

**How it was checked.** Computed once; expectations committed first (written after the referee's unsealed computation
was read); tested against planted errors (1, caught).
- **Stage 3.** `wb2_stage3.py` was sealed at its commit before the run, and its output was committed before it was read.
- **Post hoc 1.** `wb2_stage3_posthoc1.py` was committed before its run, and is not blind.
- **The placement:** M_alt(h)(u) = v_x(u) v_y(u)ᵀ / θ₁(u + h, τ), with the residue at u₀ = −h and h = c·q_H·w.
- **The level:** residue level, unit weights, the two non-zero singular values, the triplet untwisted, readings S and S̃.
- **Where:** every sector, four points of order 5, and stage 1's and stage 2's moduli.

## 1. Results

| test | c = +2 | c = −2 | c = +1, −1 |
|---|---|---|---|
| U0, the factorisation (h = 0, 20 random u) | 3.9e-15 | | |
| τ ↦ τ + 1, (a, b) ↦ (a, b − a), with and without reduction mod 1 | 3.2e-10 to 3.5e-10 | 3.3e-10 | 3.2e-10 to 3.6e-10 exactly; **0.56 to 1.2** with the reduction |
| τ ↦ −1/τ, (a, b) ↦ (−b, a), with and without reduction | 1.7e-10 to 1.8e-10 | 1.7e-10 to 1.8e-10 | 2.3e-10 to 2.7e-10 exactly; **0.68 to 0.97** with the reduction |
| w ↦ w + 1 | 5.3e-15 to 5.9e-15 | 5.3e-15 to 6.1e-15 | **1.2** |
| w ↦ w + τ (r2 alone, post hoc 1) | 7.3e-15 to 1.1e-14 | 6.0e-15 to 8.2e-15 | **1.4 to 2.4** |
| E: frame C's kernel at the charges q′ = q − c·q_H/2 | 5.1e-15 to 7.8e-15 | 1.2e-15 to 2.0e-15 | 1.8e-15 to 3.1e-15 |
| R: reading S at h against S̃ at −h | above 1e-3 | | |

- **U0** holds.
- **U1** (c = ±2 covariant under T, S and both periodicities) is not met as written. Its one failure was the w ↦ w + τ
  test, which compared σ₁ as well as σ₂/σ₁.
  - σ₁ carries the thetas' quasi-periodicity multiplier, a common factor of the whole coupling, so it is not expected to
    be invariant.
  - On σ₂/σ₁ alone (post hoc 1, not blind) c = ±2 is periodic to 1e-14. With that, c = ±2 passes every test.
- **U2** holds: c = ±1 is covariant only without reduction, and it is not periodic in w. Its effective charges are
  half-integers.
- **U3** holds: at c = −2 the shifted charges are (−q_R, −q_L).
- **U4** holds.
- **The plant** holds: the S-test with h not transported fails.

## 2. What it means

- **Frame D1, with the Higgs's twist in its own Szegő factor, is frame C at shifted charges.** At residue level the
  coupling equals frame C's at q′_L = q_L − c·q_H/2, q′_R = q_R − c·q_H/2, to 1e-14.
  - At residue level E is an identity for every c: the residue sees the matter doublets only at the pole.
  - So the covariance at c = ±2 is frame C's covariance at the shifted charges, and the only condition is that those
    charges be integers (c·q_H even).
  - **c = −2** gives (q_L + q_H, q_R + q_H) = (−q_R, −q_L). Frame C at those charges is frame C's coupling transposed,
    sector by sector: the legs exchanged, to 3e-15 (computed once by the second referee read, at residue level, and for
    frame C itself also with norms). So for the singular values D1 adds nothing. For the mixing it is frame C read with
    right singular vectors in place of left: at residue level the massive block of |V| differs from frame C's by up to
    0.84.
  - **c = +2** gives (q_L − q_H, q_R − q_H) = (2q_L + q_R, q_L + 2q_R): up (−2, −7), down (4, 5), leptons (0, 9) in 6Y.
    This is the one new covariant candidate. Its pole sits at u₀ = −2q_H·w = 2(q_L + q_R)·w. That is where matter's own
    rule puts a field of charge q_H: a leg of charge q has its argument shifted by 2qw, so its zeros move by −2qw. The
    three shifts 2q_L·w, 2q_R·w and 2q_H·w then sum to zero. At c = −2 the pole sits instead at the sum of the legs'
    zero locations, −2(q_L + q_R)·w.
  - **c = ±1** is excluded by periodicity in the Higgs's point.
- **Which sign of c is the charge-conserving one is a convention:** where the Higgs's point is put. Main should decide it.
  This seat's reading is that c = +2, the Higgs placed by matter's rule at its own charge, is the overlap's own. On that
  reading, c = −2 is frame C's bookkeeping with the legs exchanged.
- **The reading is still chosen by hand in this placement.** The Higgs's sign does not act as the reading (R). So this
  form does not realise W-B1's outline that D1 has no reading to choose.
- **The leptons, from B1934's law (a reading, not computed).**
  - Mod 5, the c = +2 charges are down (4, 0) and leptons (0, 4): transposed.
  - So at the points of order 5 the leptons again copy the down rows transposed. This holds at residue level, through
    E; the second referee read computed it once (1.4e-14 at the 24 points, and not at (1/7, 3/7)).
  - They would separate only through a line or level with another prime, as in frame C.
- **B1947's failure is recomputed.** The twisted triplet (K1, K3) is not covariant under τ ↦ τ + 1 (stage 1's post hoc 1:
  0.6 to 7.2; K3 there used the first, flawed kernel). With the corrected kernel and B1947's triplet, the second referee
  read finds 0.58 to 7.3, so it stands.
- **Next, if main wants it.** M34's mixing stage for c = +2: which reading pair, and |V| at the 24 points and the two
  heights, with the norms. That is frame C's machinery at the charges above, if the identity E extends from the residues
  to the norms (to be checked first). As built it will not: off the pole, M_alt(u − h) is frame C at q′ times a scalar
  of modulus e^(k·Im u), with k about −15 for up at the mark (the second referee read). The norm-level placement has to
  be fixed first.

## 3. Typed

| statement | how checked |
|---|---|
| the factorisation of frame C's bilinear | computed once (U0); found by the referee of the first note |
| the corrected placement is T- and S-covariant and periodic in w at c = ±2 | computed once (stage 3 and its post hoc 1; not blind); first computed, unsealed, by the referee; recomputed independently (the second referee read: its own thetas, main's q-series triplet, an analytic residue; to 6e-15) |
| it equals frame C at q − c·q_H/2 (residue level) | computed once (E) |
| c = −2 is frame C transposed (the same singular values, left and right vectors exchanged); c = +2 is new (up to 2.4 from frame C in σ₂/σ₁) | computed once by the second referee read (residue level; frame C's transposition also with norms) |
| B1947's triplet twist is not T-covariant | computed once (stage 1's post hoc 1); recomputes B1947 |
| the Higgs's sign does not act as the reading | computed once (stages 2 and 3) |
| the leptons copy the down rows transposed at order 5 for c = +2 | a reading (B1934's law applied to the shifted charges); at residue level computed once by the second referee read |

## 4. Files

`relays/chat1_2026-11-15_wb2/`: `wb2_stage3.py` (sealed), `wb2_stage3_posthoc1.py`, their outputs and warnings files
(empty), and `SCRIPT_SHA256.txt`.

This note was pushed before its second referee read finished (the first read found the first note NOT READY), following the author's word of 2026-11-15 on untracked notes. The second read's corrections are applied in a later commit (b8a394419 said so before they were; this commit applies them).

0 of 19.

## Addendum (stage 4, M36's data-free check): E does not reach the norms as this seat re-centred them; with the metric that absorbs the off-pole scalar, it does

**The check.** Stage 4 (`wb2_stage4.py`) was sealed (5004626b2) before its run. It is not blind: the second referee read
had found, unsealed, that off the pole M_alt is frame C at q′ times a scalar of varying modulus.
- **The construction.** Frame D1's full frame uses B1656's quadrature norms, re-centred on the moved pole:
  - the flat |P_s/R_s|² over the cell {−h + x + yτ : |x|, |y| ≤ ½}, with the ε cut-off and a0 taken about −h;
  - Theorem 90's weight and a bounded end, L₂ = 0.9.
  It is compared with frame C at q′ = q − c·q_H/2, with the same end.
- **Where.** In reading S, every sector, at the mark and the twin, at three bulk moduli (0.13 + 1.7i, −0.31 + 1.25i,
  0.4 + 1.2i).
- **The control N3 failed as written, on stage 1's harness flaw.** At unit weights the coupling has rank 2, so σ₃/σ₁ is
  rounding noise, and its relative difference (1.29, 1.94) means nothing.
- **Post hoc 1** (`wb2_stage4_posthoc1.py`, committed before its run, not blind) reports σ₂/σ₁ and σ₃/σ₁ separately.

| largest relative difference from frame C at q′ (3 sectors, 2 points, 3 moduli) | σ₂/σ₁ | σ₃/σ₁ |
|---|---|---|
| c = +2, with norms | **0.54** | 1.26 |
| c = −2, with norms | **0.70** | 1.66 |
| c = +2, unit weights (the control) | 5.3e-15 | (rank 2: noise) |
| c = −2, unit weights (the control) | 1.1e-15 | (rank 2: noise) |

- **E holds at residue level and fails with these norms**, by order one, for both signs of c.
- **How far that reaches** (the referee read, on its own code):
  - **The flat norm depends on where the cell is cut.**
    - Off the pole, |K_D1|² is |K_C′|² times e^(2k·Im z), with k = −2π·c·q_H·a. That factor is not periodic.
    - D1's norms come out at 1e3 to 7e10, against −2.9 to 21 for frame C at q′.
    - Over the fixed cell about u = 0 the differences change again: 0.009 to 3.3 at τ = 0.13 + 1.7i.
  - **This construction is not periodic in the Higgs's point.** Under w ↦ w + τ, at τ = 0.13 + 1.7i, σ₂/σ₁ moves by 0.004
    to 0.040 and σ₃/σ₁ by up to 0.57. Frame C at q′ holds to 1e-11.
  - **With the bundle's flat unitary metric E does reach the norms.** That metric is e^(4π·Im h·Im z/Im τ), fixed to 1 at
    the pole. With it, |K_D1|² is frame C's at q′ pointwise. The ratios then agree to 3e-8, and c = −2 stays frame C
    transposed.
- **So the answer depends on the norm.**
  - With the flat norm over the cell about the moved pole, frame D1 is a different object from frame C at shifted
    charges, and c = −2 is no longer frame C transposed.
  - With the flat unitary metric, D1 is frame C at shifted charges with the norms too.
- **[J] The fork.**
  - Either the flat norm over a cell, which depends on the cut and is not periodic in the Higgs's point;
  - or the flat unitary metric, under which D1 adds nothing beyond frame C at q′.
  That has to be fixed by a principle before D1's mixing stage, which M36 holds anyway. This seat's reading is that
  periodicity in the Higgs's point decides it for the unitary metric. On that reading D1, at the norm level too, is frame
  C at shifted charges.

| statement | how checked |
|---|---|
| E fails with the flat norm over the cell about the moved pole (c = ±2) | computed once (stage 4 and its post hoc 1; not blind); expectations committed first (N1 met; N3 failed as written, on rank-2 noise, re-run on σ₂/σ₁ alone post hoc); recomputed independently (the referee read: its own thetas, analytic residues, another quadrature; τ = 0.13 + 1.7i, every sector, both points, to four digits) |
| that construction is not periodic under w ↦ w + τ | computed once by the referee read (its code and the seat's agree to four digits) |
| with the flat unitary metric E reaches the norms (to 3e-8) | computed once by the referee read; the metric's uniqueness is a reading |

Files: `wb2_stage4.py` (sealed, 5004626b2), `wb2_stage4_posthoc1.py` (c38bec3b8), their outputs and warnings files
(empty); SHA256s in `SCRIPT_SHA256.txt`.

This addendum was pushed before its referee read finished, following the author's word of 2026-11-15 on untracked notes;
the read's corrections are applied in this version.

0 of 19.
