# W-B2, corrected: with the Szegő zero alone moved to the Higgs's point h = c·q_H·w, frame D1's coupling is covariant under τ ↦ τ + 1 and τ ↦ −1/τ, and periodic in w, at c = ±2. At c = −2 it is exactly frame C; at c = +2 it is frame C at the charges (2q_L + q_R, q_L + 2q_R). B1947's twisted triplet stays non-covariant, and the Higgs's sign does not act as the reading. No mixing computed

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
  - **c = −2** gives (q_L + q_H, q_R + q_H) = (−q_R, −q_L). That is frame C again: D1 adds nothing.
  - **c = +2** gives (q_L − q_H, q_R − q_H) = (2q_L + q_R, q_L + 2q_R): up (−2, −7), down (4, 5), leptons (0, 9) in 6Y.
    This is the one new covariant candidate. Its pole sits at u₀ = −2q_H·w = 2(q_L + q_R)·w, the sum of the matter
    legs' twist points.
  - **c = ±1** is excluded by periodicity in the Higgs's point.
- **Which sign of c is the charge-conserving one is a convention:** where the Higgs's point is put. Main should decide it.
  This seat's reading is that c = +2, the pole at the sum of the legs' points, is the overlap's own. On that reading,
  c = −2 is frame C's own bookkeeping.
- **The reading is still chosen by hand in this placement.** The Higgs's sign does not act as the reading (R). So this
  form does not realise W-B1's outline that D1 has no reading to choose.
- **The leptons, from B1934's law (a reading, not computed).**
  - Mod 5, the c = +2 charges are down (4, 0) and leptons (0, 4): transposed.
  - So at the points of order 5 the leptons again copy the down rows transposed.
  - They would separate only through a line or level with another prime, as in frame C.
- **B1947's failure is recomputed.** The twisted triplet (K1, K3) is not covariant under τ ↦ τ + 1 (stage 1's post hoc 1:
  0.6 to 7.2). That stands.
- **Next, if main wants it.** M34's mixing stage for c = +2: which reading pair, and |V| at the 24 points and the two
  heights, with the norms. That is frame C's machinery at the charges above, if the identity E extends from the residues
  to the norms (to be checked first).

## 3. Typed

| statement | how checked |
|---|---|
| the factorisation of frame C's bilinear | computed once (U0); found by the referee of the first note |
| the corrected placement is T- and S-covariant and periodic in w at c = ±2 | computed once (stage 3 and its post hoc 1; not blind); first computed, unsealed, by the referee |
| it equals frame C at q − c·q_H/2 (residue level) | computed once (E) |
| c = −2 is frame C; c = +2 is new | a reading of E |
| B1947's triplet twist is not T-covariant | computed once (stage 1's post hoc 1); recomputes B1947 |
| the Higgs's sign does not act as the reading | computed once (stages 2 and 3) |
| the leptons copy the down rows transposed at order 5 for c = +2 | a reading (B1934's law applied to the shifted charges) |

## 4. Files

`relays/chat1_2026-11-15_wb2/`: `wb2_stage3.py` (sealed), `wb2_stage3_posthoc1.py`, their outputs and warnings files
(empty), and `SCRIPT_SHA256.txt`.

This note was pushed before its second referee read finished (the first read found the first note NOT READY), following the author's word of 2026-11-15 on untracked notes. The read's corrections follow in a later commit.

0 of 19.
