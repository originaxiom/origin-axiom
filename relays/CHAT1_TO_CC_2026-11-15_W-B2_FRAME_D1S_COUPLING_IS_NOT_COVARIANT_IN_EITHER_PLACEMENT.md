> **WITHDRAWN IN PART (2026-11-15, the same day, from its referee read).** The headline is wrong, and so are § 2's
> "no placement in frame C's kernel gives a covariant D1", its level-mismatch hypothesis, and its "next step".
> - **The error.** This seat's K2 shifted more than the Szegő zero. Frame C's bilinear factorises as
>   v_x(u) v_y(u)ᵀ / θ₁(u), and the factors e^{−iπu} (in den) and e^{−2πiu} (inside θ₁(u + τ)) belong to the matter
>   doublets. bil_h moved them too. So its K2 is the correct placement conjugated by diag(1, e^{iπh}), which is not
>   unitary, and it is not even periodic in the Higgs's point (w ↦ w + τ changes it).
> - **What the referee computed (not sealed here).** The placement with the Szegő zero alone moved is covariant under
>   τ ↦ τ + 1 and τ ↦ −1/τ at c = ±2, to 1e-14. At c = −2 it reproduces frame C's singular values (its
>   coupling is frame C's transposed). At c = +2 it is a different
>   covariant object.
> - **What stands.** B1947's twisted triplet (K1) and K3 are not covariant, and the Higgs's sign does not act as the
>   reading in either build.
> - **§ 1's and § 3's K2 rows** (T-covariant for every c, S-covariant for none) describe the first build only. They are
>   not results about D1.
> - **What follows.** Stage 3 (sealed at 7339ec8a3) recomputes the corrected placement. The rewritten note is
>   `CHAT1_TO_CC_2026-11-15_W-B2_FRAME_D1_IS_FRAME_C_AT_SHIFTED_CHARGES.md` (b1727da04).

# W-B2, stages 1 and 2: frame D1's Higgs twist has no modular-covariant place in frame C's kernel. In the triplet (B1947's) it fails τ ↦ τ + 1. In the kernel's Szegő factor it passes τ ↦ τ + 1 for every shift tried and fails τ ↦ −1/τ for every one. As M34 asks, this is said before any mixing is computed: no mixing was computed

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` (data-free). It answers M34's condition ("show
covariance first"; "if you find it inconsistent with frame C's bilinear kernel, say so before computing anything") for
card W-B2 (`relays/cards/CHAT1_W-B2_frame_d1s_coupling_as_a_triple_overlap.md`, 7557aa1f5).

**Under the author's ruling of 2026-11-15** (outputs computed; no data, no comparison). **No mixing** was computed in any
stage.

**How it was checked.** Computed once; expectations committed first (with one harness failure, disclosed).
- **The kernel.** This seat's transcription of B1656's bilinear (W-F22), with one change: a shift h of its Szegő
  denominators, θ₁(u) ↦ θ₁(u + h) in all three, and the residue taken at u₀ = −h. With h = 0 it is frame C's kernel.
- **The Higgs's charge.** q_H = −(q_L + q_R) in 6Y (up +3, down and leptons −3), asserted in the script.
- **The test.** Residue level, with unit weights, so the norms do not enter.

**The stages.**

| stage | sealed | output | what it found |
|---|---|---|---|
| 1 (`wb2_stage1.py`) | 7557aa1f5 | af53b7f59 | **the control failed, on a harness flaw.** With unit weights the coupling has rank 2 (σ₃/σ₁ about 1e-16), so the σ₃/σ₁ test compared rounding noise. Frame C's full frame is covariant at the same points: this was checked in a debugging run, which was not sealed |
| 1, post hoc 1 (`wb2_stage1_posthoc1.py`) | committed before its run; not blind | committed before it was read | the same test on the two non-zero singular values: the control passes |
| 2 (`wb2_stage2.py`) | before its run; designed after post hoc 1 was read | committed before it was read | τ ↦ −1/τ, and the reading against the Higgs's sign |

## 1. Results

**Under τ ↦ τ + 1, with w ↦ (a, b − a)** (stage 1, post hoc 1). The test covers every sector, four points of order 5
and three bulk moduli; a deviation below 1e-8 counts as covariant.

| candidate | S | S̃ |
|---|---|---|
| K0, frame C (the control) | 3.3e-10 | 3.3e-10 |
| K1, B1947's twisted triplet (q_H a, q_H b), kernel untwisted | **2.2 to 7.2** | **0.6 to 0.9** |
| K2(c), the kernel's Szegő factor shifted by h = c·q_H·w, c = ±1, ±2, triplet untwisted | **2.9e-10 to 3.5e-10, every c** | the same |
| K3(c), K2 with K1's triplet | 1.6 to 7.0 | 1.6 to 7.0 |

- **V0** (the control) holds. **V1** (K1 is not covariant) holds, which recomputes B1947. **V2** holds: every c is
  covariant. **V3:** no K3 is covariant.
- **The plant** holds: the control with the line not moved fails.
- **Why every c passes.** The shift h = c·q_H·w is unchanged by the transport, because w is unchanged as a complex
  number. So τ ↦ τ + 1 does not see h.

**Under τ ↦ −1/τ, with (a, b) ↦ (−b, a), w ↦ w/τ and h ↦ h/τ** (stage 2). The moduli 0.3 + 0.97i, −0.2 + 1.0i and
0.1 + 1.1i keep both τ and −1/τ above height 0.85.

| candidate | S | S̃ |
|---|---|---|
| frame C's kernel, h = 0 (the control) | 1.7e-10 | 1.8e-10 |
| K2(c), c = +1, −1, +2, −2 | **0.82 to 0.97** | **0.80 to 0.95** |

- **W0** (the control) holds.
- **W1** holds: no c ≠ 0 is S-covariant. The expectation, that some c would pass and some fail, is met in its letter
  only, since none passes.
- **W2** (that the Higgs's sign acts as the reading) is not met. Reading S at h against S̃ at −h differs by a factor of
  2.3 to 2.7 in σ₂/σ₁, and against S̃ at +h by 2.3 to 2.8.
- The plant holds.

## 2. What it means

- **B1947's failure, recomputed: the triplet is the wrong place for the Higgs's twist.** Twisting the characteristics of
  B1691's theta constants breaks τ ↦ τ + 1 in every sector and in both readings.
- **The kernel's Szegő factor is the place B1938 points to, and it is not enough either.** Shifting its zero to the
  Higgs's point keeps τ ↦ τ + 1 trivially and breaks τ ↦ −1/τ, for each of ±q_H w and ±2q_H w.
- **So, of the placements frame C's kernel offers, none gives a modular-covariant D1.** This is the inconsistency M34
  asks to hear about before anything is computed.
  - A reading of why: the matter thetas are of level 2 (modulus 2τ), and the Higgs's Szegő factor and triplet are of
    level 1. A charge-conserving overlap in the sense of the magnetized-torus product formula needs its three factors on
    one lattice, so that their Gaussian factors under τ ↦ −1/τ combine. In frame C they do not.
- **The Higgs's sign does not act as the reading.** So frame D1, in this form, does not remove the reading, contrary to
  what W-B1's frame D promised in outline.
- **What would be next, if main wants it:**
  - rebuild the kernel with the Higgs as a level-2 theta doublet in the same u, so that the overlap is the product of
    three level-2 thetas over one Szegő factor;
  - test it under T and S at residue level before any norm or mixing.
  - This is a new construction, not a variant of frame C, so it needs its own card.

## 3. Typed

| statement | how checked |
|---|---|
| K1 (B1947's) is not T-covariant | computed once (post hoc 1, not blind); recomputes B1947 |
| K2 is T-covariant for every shift tried | computed once (post hoc 1, not blind) |
| K2 is not S-covariant for any shift tried | computed once; expectations committed first (stage 2, designed after post hoc 1) |
| the Higgs's sign does not act as the reading in K2 | computed once; expectations committed first (W2 not met) |
| no placement in frame C's kernel gives a covariant D1 | a reading (of the placements tried: the triplet, the Szegő factor, both) |
| the cause is the level mismatch | a hypothesis |

## 4. Files

`relays/chat1_2026-11-15_wb2/`: `wb2_stage1.py` (sealed), `wb2_stage1_posthoc1.py`, `wb2_stage2.py`,
`SCRIPT_SHA256.txt`, the three outputs and the three warnings files (with machine paths redacted to `<repo>/`).

This note was pushed before its referee read finished, following the author's word of 2026-11-15 on untracked notes. The
read's corrections follow in a later commit.

0 of 19.
