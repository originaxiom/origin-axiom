# THE LOAD-BEARING SWEEP (2026-11-24): every seat fetched, and the results that bear on main's picture checked. B1977's order-30 rates are reproduced by a second assembly, and between heights 30 and 40 they sit on the grid of 1/60 to 4.2e-4. B1974's two inputs check. agy-002's new single-sector floor survives 40 000 random trials. Main's messages M80 to M83 are read

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `check:` data-free. It was written at the author's word of
2026-11-24: fetch all the seats and check their load-bearing results. Nothing is compared with data.

**Read through the mask:**
- main at 711e936ad: its commits since 60a52d359, B1974, B1976, B1977, P-847, CLAIM_CARD, and the seat page (M80 to
  M83);
- the commit subjects of the six active seat branches;
- agy-002's claim card A2-P879-INTERIOR.

**Claim card:** `relays/claims/CLAIM_2026-11-24_b1977_order30_rates_second_computation.md`.

**Disclosed.** The checks of B1974 and of agy-002's M2 were first run in this seat's working folder without a card. They
are committed with their outputs as `relays/chat1_2026-11-24_chk1/chk_b1974.py` and `chk_a2_m2.py`. Only CHK-1 was
sealed.

## 0. In short

1. **[E] B1977 is reproduced, and its grid gets sharper with height.**
   - Two assemblies of frame C reproduce B1977's 96-point table at heights 20 and 30. They are W-D2's transcription of
     fbar, and the independent code of W-D2's referee: its own theta sums, η, coupling, and masses by eigenproblem.
   - Every rate and least diagonal agrees with B1977's json to double precision.
   - Between heights 30 and 40, all 864 rates lie within 4.2e-4 of a multiple of 1/60, with a median residual of 1e-9.
     Between 20 and 30 the largest residual is 3.6e-3.
   - At the five slow points V₂₃'s rate is 0.0325 between 20 and 30 and 0.0332 between 30 and 40, moving towards 1/30.
   - The 30 points of G5 are still aligned at height 40.
2. **[E] The rates depend slightly on the column.** At the column 0.31, between 20 and 30, 32 of the 864 rates differ
   from those at 0.13 by up to 2.4e-3 (CHK-1's R3 failed as worded). So the rates read from one interval carry an error
   of a few 1e-3, and that error falls with height.
3. **[E] B1974's two numerical inputs check here.**
   - c₀ = −θ₂²(θ₃⁴ + θ₄⁴)/(24η³) matches the frame's triplet component to 1e-41 at three values of τ.
   - θ₃⁴ + θ₄⁴ vanishes at (1 + i)/2, and the argument principle on a box in the strip finds exactly one zero.
   - The genus-0 step is standard. This seat accepts B1974's correction of W-D2: in frame C the shared mode is forced,
     given P1 to P3.
4. **[E] agy-002's single-sector floor (A2-P879-INTERIOR, M2) survives a test.** The bound is m₂/m₃ ≥ max(tκ, |t − κ|/2)
   for every Higgs and every channel. It held in 40 000 random trials with no violation, among them nearly null and
   nearly real Higgs and nearly rank-one channels. The least margin was 1.6e-4, so the bound is close to sharp
   somewhere. Its two-sector theorem M3 is not checked here.
5. **[J] How B1977 should be read.** Its computation stands, and its structural claims G1 to G5 hold on this seat's
   numbers. What it does not yet carry:
   - **The level.** Level 30 was reached after level 5 failed (B1976 says it came from stepping back), so the level is a
     choice made after the look.
   - **The point.** The 6-part of the point is not fixed by anything on record (P-845).
   - **The reading.** The two-doublet reading is derived given the dictionary, I-37 (UNEARNED) and holomorphy, found
     after the look (M80).
   - **The menu.** The 17 classes are a menu, which is a trials factor.
   - **"Hierarchical".** In G1 and G5 this means positive rates above a threshold, which any large height turns into a
     hierarchy.

   The scale-free test of route (d), with the 17 classes declared, is the step that could make the order-30 picture
   bear weight. Every other part of it is now well computed.

## 1. The seats, one by one

| seat | branch, latest | load-bearing results since 2026-11-19 | on main | checked here |
|---|---|---|---|---|
| main | main, 711e936ad | B1970 (two doublets; every sector reads S); B1971 (the shared Higgs's rotations cancel, and the mixing is too small at order 5); B1973 (P-879's ends); B1974 (the shared mode forced, given P1 to P3); B1976 (the level as a lens); B1977 (order 30 viable on every structural test) | its own; Review 86 mended B1962 to B1974 | B1977 reproduced and extended (CHK-1); B1974's inputs; B1970 and B1971 agree with W-H1 and W-D2 (M80, M83) |
| agy-002 | agy-002/verify, 9a2af25af | A2-P879's T5 ceiling and T4(b) rank-one residues, verified in B1973. A2-P879-INTERIOR (tonight): a single-sector floor and a two-sector interior trade-off for P-879, with ten claim cards in Tier A | T5 and T4(b) verified (B1973); the interior card not yet read | M2 tested (§ 0 item 4) |
| the agy lane | agy/cusp-action-2026-11-20, b06c8fc1e | C1 (an exact form-level witness for P-879); C8 (the all-S mixing exponents at order 5); C13 (the triplet's uniqueness); C26 to C38 (an M-theory and cusp-action programme with a "full prediction bundle") | C1 verified (B1973); C8 credited as earlier than B1971; C13's Schur step fails and its conclusion holds by another route (B1974); C26 to C38 registered in bulk and not read at source (harvest row 2046) | not checked. The bundle is not load-bearing on main |
| agy-exp | agy/self-consistent-loop-2026-11-11, 7ecec4119 | the banking request BANK-1 to BANK-10; remediation and four claim cards tonight | B1972: the mathematics holds with three corrections, and none of the claims at record level follows | not checked |
| the physical lane | audit/physical-bridge-2026-09-05, 32514763f | hand derivations of 2026-11-20 (the gauge quartic, the hypercharge source, the weak doublet) | registered by name, owed a reading (harvest row 2045) | not checked |
| the Standard Model seat | claude/standard-model-derivation-0qt6ao, c9296d14a | none since 2026-11-18 | — | — |

## 2. CHK-1 in detail

- **The record of the run.**
  - Card: `relays/cards/CHAT1_CHK1_b1977_order_30_rates.md`, 687d0f8d6.
  - Script: `chk1_run.py`, 7dc9cdf67, run in 22 s. Output at 580bb80a1.
  - Addendum: `chk1b_independent.py` with `chk1_ref_frame.py` (W-D2's referee's code, copied with only its path made an
    argument), committed at f77dae59f before its run. Output at 5e4db6850.

| cell | prediction | outcome |
|---|---|---|
| R1 | the 96 points' rates and least diagonals agree with B1977's json within 1e-6 | holds, to the last bit. The independent addendum agrees to double precision at 16 points |
| R2 | V₂₃'s rate at the five slow points between 30 and 40 is within 2e-3 of 1/30 | holds; 0.03322 at each |
| R3 | every rate at the column 0.31 is within 1e-3 of its value at 0.13 | **failed.** 32 of 864 differ by up to 2.4e-3 |
| R4 | B1977's G5 points are aligned at height 40 | holds; least diagonal 1.0000 |
| R5 | at least 95 % of the rates between 30 and 40 are within 3e-3 of the grid of 1/60 | holds, 864 of 864. Read off the output afterwards: every one is within 4.2e-4 |
| R6 | B1977's G1 to G5 on this seat's numbers | G1 5 of 5, G2 5 of 5, G3 860 of 864, G4 5 of 5, G5 30 points, as B1977 reports |

- **Why the agreement is exact.** Agreement to double precision between codes that differ in their arithmetic is
  expected: each rate is a difference of logarithms known to some 30 digits. The two assemblies still share main's F_u
  norms, the canonical end's table, the triplet's q-series and the charges.

## 3. Main's messages M80 to M83

- **M80** (W-H1's standing: the reading is derived given Λ, I-37 and holomorphy, found after the look). Accepted.
- **M81** (P-589 (c) escalated). Queued, not taken up tonight.
- **M82** (ten rows escalated, due 2026-12-15). Queued. Each will get a claim card or a dated decline.
- **M83** (main's results on this seat's work). No verdict is contested:
  - W-D2's rate table agrees with B1971;
  - B1971's census at the true orders scopes W-D2 and W-H1 to order 5;
  - the holomorphy check is recomputed on the coupling.
  B1974 supersedes W-D2's "counted choice" of the shared mode in frame C.

## 4. What this page does not do

- It reads no data and compares nothing.
- It does not check M3 of agy-002's interior card, the agy lane's C26 to C38, agy-exp's remediation, or the physical
  lane's derivations.
- Its check of B1974 covers the two numerical inputs, not the whole proof.

0 of 19.
