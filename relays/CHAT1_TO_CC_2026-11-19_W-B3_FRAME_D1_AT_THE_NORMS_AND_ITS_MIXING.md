# W-B3 (M78): identity E holds at the norms exactly, at every height, when D1's norm is taken with the flat unitary metric of the Higgs's twist and its a0 with that metric's connection (a short derivation, checked to 1e-87 at height 30). This seat's code, building D1 at its own pole, reproduces every class and number of B1962's that it could see: no reading pair aligned at height 30 under either sign (smallest diagonal 3.4e-5), at height 6 three pairs deranged and (S̃, S̃) partial (0.12525 and 0.12559), the leptons a transposed copy. B1962's NEGATIVE stands on a second computation

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` data-free. It answers M78 (on B1962) and closes
card W-B3 (`relays/cards/CHAT1_W-B3_frame_d1_at_the_norms_and_its_mixing.md`).

**The ruling it runs under.** The author's ruling of 2026-11-15: frame outputs are computed and printed. No data was
opened, and nothing here is set beside a measured number.

**Order of work.**
- The card, with Q1's derivation, every check and every expectation: 647429f10. Five lines in two places were
  rewrapped at e3be7373e, with no change of content.
- The script `relays/chat1_2026-11-19_wb3/wb3_run.py`: 89c491f47. Its output: fc1ff20f7, with a partial output
  committed unread mid-run (ac6bfeb6c). Both were committed before the output was read.
- The run stopped in the fork's variant (§ 2.4). The follow-up's condition was then added to the card (652cd48af), its
  script `wb3_followup.py` committed (5dcadd8d7), and its output committed before it was read (7a2961d85).
- **Smoke tests, before the script's commit.**
  - The functions were checked on control inputs: the thetas against W-F22's, the dual basis, the end's value.
  - main() was run once with one point and a random triplet, its printed output discarded. E4 uses neither the points
    nor the triplet, so that run computed E4 in full, unseen. X2's expectation had been fixed in the card before.
  - That run raised a division warning in E4's ratios, from a coupling that vanishes. Before the commit, the script was
    changed to count such cases instead of dropping them.

**Not blind.**
- M78 states B1962's outcome.
- Through the mask, B1962's output shows eight numbers at height 6. (The card says "four of its numbers" and lists
  eight.)
- Main's test file for B1962 also shows frame C's (S, S) at height 30, 1.000 and 6.277e-5 (the referee). This seat did
  not read it before the run, which gives 6.2770e-5.
- W-B2 stage 4 and its referee had shown E failing with the cell norm and holding, unsealed, with the unitary metric.

**Typing.** [E] marks what the run, the record or a standard result establishes; [J] marks this seat's judgement.

---

## 0. In short

1. **Q1, identity E at the norms: [E] it holds exactly, for one choice of norm.**
   - Off its pole, D1's kernel is frame C's at the shifted charges times e^(λz + μ), with λ = 2πi·c·q_H·a (the theta
     shift law; § 1).
   - So with the flat unitary metric of the Higgs's twist, normalised to 1 at the pole, the norm's integrand is frame
     C′'s pointwise. With that metric's connection, the constant term a0 is too.
   - Checked at heights 1.7, 6 and 30, for every sector, both signs and the 24 points: to 7e-32, 3e-40 and 1e-87.
   - Two other choices fail:
     - the flat norm over the cell (W-B2 stage 4; here 1.66);
     - the plain a0 (here up to 12, and in 30 of 36 bulk cases the coupling vanishes).
2. **Q2, the second computation: [E] it reproduces every class and number of B1962's that this seat could see.**
   - At height 30, no pair is aligned under either sign. The smallest diagonal |V| is 3.374e-5 for (S, S), the same
     under both signs, and 7.5e-41 to 1.8e-38 for the other pairs.
   - At height 6, three pairs are deranged and (S̃, S̃) is partial: 0.12525 (c = −2) and 0.12559 (c = +2), against
     B1962's 0.1252 and 0.1256.
   - The leptons copy the down sector transposed, to 1e-37 or better.
   - The frame-C control reproduces B1962's printed values at height 6.
3. **[J] What it means.**
   - B1962's NEGATIVE stands on a second computation.
   - Under the unitary metric, identity E at the norms is an identity, not an assumption. Whether that metric is D1's
     own is main's to rule. W-B2 stage 4's referee found it periodic in the Higgs's point, and the cell norm not.
   - The fork does not change the verdict: with the plain a0, every pair is deranged at both heights.

---

## 1. Q1: identity E at the norms

**The derivation** (the card's, written before computing).
- With T = 2τ, h = c·q_H·w and w = aτ + b, write z − h = z + pT + r, with p = −c·q_H·a/2 and r = −c·q_H·b.
- The shift law θ[α, β](u + pT + r, T) = e^(−iπTp² − 2πip(u + β + r)) θ[α + p, β + r](u, T) gives both components of
  v_x the same factor. The new characteristic is the twist of q′_L = q_L − c·q_H/2; likewise for y.
- Since θ₁(z − h + h) = θ₁(z), K_D1(z − h) = e^(λz + μ) K_C′(z), with λ = 2πi·c·q_H·a.
- **The residues** share the factor e^μ. That is W-B2 stage 3's E.
- **The norm.** |P_D1(z − h)/R_D1|²·m(z) = |P_C′(z)/R_C′|² with m(z) = e^(4π·Im h·Im z/Im τ). So every regularised
  norm over the same cell about the pole agrees.
- **The constant term.** The plain Laurent constant shifts by λ. The metric's Chern connection removes it, since
  ∂_z log m = −λ.

**The checks.**

| check | height 1.7 (33 digits) | height 6 (42 digits) | height 30 (90 digits) |
|---|---|---|---|
| E1: K_D1(z − h)·e^(−λz)/K_C′(z) one constant, 4 entries × 5 points z | 6.8e-32 | 2.7e-40 | 1.1e-87 |
| E2: R_D1/R_C′ one constant over the non-zero channels | 5.8e-32 | 4.4e-41 | 3.5e-88 |
| E3: a0_D1 (plain) − λ against a0_C′ | 5.3e-32 | 1.2e-41 | 1.3e-89 |
| zero channels that differ | 0 | 0 | 0 |

Each entry is the largest over the three sectors, both signs of c and the 24 points.

**E4, the integral itself, in double precision on this seat's quadrature.** This uses W-B2 stage 4's cases: three bulk
moduli, the mark and the twin, every sector, both signs, reading S, end 0.9. Each value is the largest relative
difference of σ₂/σ₁ and σ₃/σ₁ from frame C′.
- D1 with the metric in its quadrature norm and the covariant a0: **1.1e-11**.
- D1 with the metric and the plain a0: 12.2 over the 6 cases whose coupling survives, all at the twin with c = +2. In
  30 of the 36 cases every weight's argument is not positive, and the coupling vanishes.
  - The run printed 7 and 29. The referee found the seventh "survivor" false: at c = −2, up, the mark, τ = 0.4 + 1.2i,
    its only surviving channel is channel 1, which is identically zero there (its characteristic is ≡ (½, ½)).
  - In double precision that channel's residue is 9.4e-8 against 1e9 for the others, rounding noise, and it passed the
    absolute cut of 1e-12 carried over from W-B2 stage 4. The three real channels have plain arguments −163, −97 and
    −93. The card's follow-up section also says 29; it stays as written.
  - The 12.2 and X2 are unaffected. In the covariant construction that channel's weight is 1e-14 of the others'.
- Neither, which is W-B2 stage 4's construction: 1.66. That is stage 4's σ₃/σ₁ figure for c = −2.

**The answer to M78's first ask.** D1's norm equals frame C's at the shifted charges exactly, at every height, if it
is taken with the flat unitary metric of the Higgs's twist (normalised to 1 at the pole) and its a0 with that metric's
connection. That is the frame B1962 computed. With the flat norm over the cell it does not. With the metric but the
plain a0, the norm c_s agrees, and Theorem 90's weight does not.

## 2. Q2: the second computation

### 2.1 The build

The build is all in extended precision at 30 + 2·Im τ digits, at Re τ = 0.13.
- **Independent of main's code:**
  - the thetas, this seat's own series, with derivatives term by term;
  - D1's kernel and its residues, taken at D1's own pole −h, not as frame C at shifted charges, with a numerical test
    for the zero channels;
  - a0, the covariant Laurent constant n′(−h)/n(−h) − λ;
  - the triplet's route, W-F22's thetanull form with the τ-derivative taken term by term;
  - the dual basis of the channels.
- **Re-typed from main's code, line for line in effect:**
  - the norm, B1919's closed form (B1940's frame_mp), at frame C′'s channel characteristic, which § 1 justifies;
  - the map from channel to characteristic (frame_mp), on which that norm rests;
  - Theorem 90's weight and the coupling's contraction (frame_mp);
  - the unitary U, the left singular vectors by ascending singular value (B1945's cusp_mixing), and the same mp.svd_c;
  - the lepton measures (B1962's d1_mixing).
  - The closed form and the map are checked against this seat's quadrature and Kronecker's form (C1).
- **Shared data:** the end, B1927's and B1667's tables, interpolated by this seat's W-F24 code. L = 2.250512 at
  (0.13, 6), used at both heights.
- **The referee's recomputation used another route** for the parts re-typed here: mpmath's own thetas, the left
  singular vectors from the eigenvectors of Y·Yᴴ, the triplet by numerical differentiation and a Lambert series for E2.
  It reproduced every covariant up and down number at heights 6 and 30, for c = 0 and ±2, and every number of the
  fork. It also found the map holding at c ≠ 0 (to 1e-50 at height 6), where C1 tested it at c = 0 only, and the closed
  form agreeing with a quadrature at height 6 to 1e-11.

### 2.2 The controls

- **C0, frame C (c = 0) at height 6, against B1962's printed M0.** (S, S) gives 0.99324 and 0.11610, and (S̃, S̃)
  0.97516 and 0.22152: B1962's 0.9932, 0.1161, 0.9752 and 0.2215 to every printed digit.
- **C1, the closed form against this seat's quadrature:** within 6.3e-12 over 528 channels (heights 1.7 and 2.9). This
  seat's Laurent a0 against Kronecker's form: within 2.4e-32.
- **C2, the term-by-term triplet against W-F22's finite difference:** 2.1e-19.
- **C3, the numerical zero channels against the theta-constant rule:** no mismatch, in C1's cases and at every point of
  the run.
- **C4, two points at height 30 at 20 more digits** (the follow-up's F1): every |V| entry the same to its last double
  digit. The two points are (0, 1/5) and (0, 2/5), where a = 0 and λ = 0. The referee ran the same test at (2/5, 1/5)
  and (4/5, 3/5), c = ±2, with the same result.

Frame C's control also agrees with B1946 as B1962's card recalls it:
- (S, S) is aligned at both heights (1.0000 at height 30).
- (S̃, S̃) is aligned at height 6 and deranged at height 30.
- The mixed pairs are deranged at both heights.

### 2.3 The table

The table gives the smallest diagonal |V| and the largest off-diagonal |V| over the 24 points, classified by B1962's
thresholds. The run's output also prints frame C.

| c | height | (S, S) | (S̃, S̃) | (S̃, S) | (S, S̃) |
|---|---|---|---|---|---|
| −2 | 6 | 0.0564, 0.998: DERANGED | **0.12525, 0.99213: PARTIAL** | 2.6e-7: DERANGED | 1.3e-7: DERANGED |
| +2 | 6 | 0.0555, 0.998: DERANGED | **0.12559, 0.99208: PARTIAL** | 5.6e-5: DERANGED | 1.5e-6: DERANGED |
| −2 | 30 | 3.374e-5: DERANGED | 7.9e-39: DERANGED | 5.4e-40: DERANGED | 7.5e-41: DERANGED |
| +2 | 30 | 3.374e-5: DERANGED | 1.8e-38: DERANGED | 4.9e-40: DERANGED | 1.2e-39: DERANGED |

Where only one number is given, the largest off-diagonal is 1.0000.

- **Against M78 and B1962** (expectation X3, met):
  - No pair is aligned at height 30 under either sign, and every smallest diagonal is 3.4e-5 or less.
  - At height 6 three pairs are deranged and (S̃, S̃) is partial.
  - Both signs give the same classes.
  - The two (S̃, S̃) values agree with B1962's printed 0.1252 and 0.1256, with 0.9921, to three digits (X3). The
    referee's recomputation gives 0.1252469 and 0.1255883, with 0.9921256 and 0.9920824, so they agree to B1962's
    four.
- **The leptons** (X4, met) are a transposed copy of the down sector at both heights, both signs and both readings.
  The pattern distance is 5.8e-38 or less at height 6 and 3.6e-66 or less at height 30, and the spectra agree to
  1e-91. The plain copy is at 0.18 to 0.44 at height 6.

### 2.4 The run's stop, and the fork

**The stop.** The run stopped with a division by zero in the plain-a0 variant at c = +2, height 6. At that point all
three sectors' couplings had vanished; the division sat in the leptons' spectra. Every check of Q1, every covariant
table, C1 to C3 and the rows C0 reads had been printed; C0's verdict line had not. The
follow-up computed what was not reached: C4, the plain variant at both signs with the case guarded, and the run's
verdict lines, read off its output by the card's rules (C0, X3 and X4 all hold).

**The fork, the plain a0.**
- At c = +2 all three sectors' couplings vanish at the same 5 of the 24 points, at both heights: the points with
  a = 4/5 (the referee). At c = −2 none vanishes.
- Over the surviving points every pair is DERANGED, at both heights and both signs. (S̃, S̃) at height 6 is 1.9e-4
  (c = −2) and 0.093 (c = +2).
- The leptons are a transposed copy here too.
- So the fork changes one class at height 6, (S̃, S̃) from partial to deranged, and not the verdict.

## 3. What it means [J]

- **B1962's NEGATIVE stands on a second computation.** This seat's code builds D1 at its own pole, with its own
  thetas, a0, triplet and singular vectors. It reproduces every class and every number of B1962 that this seat could
  see.
- **P-861's owed item.** Under the flat unitary metric with its connection, identity E at the norms is an identity at
  every height, so B1962 computed D1 itself.
  - Whether that metric is D1's own is a choice, and it is main's to rule.
  - W-B2 stage 4's referee found it periodic in the Higgs's point, where the cell norm is not. That favours the metric
    over the cell norm.
  - Once the metric is chosen, the connection keeps every coupling in E4, where the plain a0 loses 30 of 36. That
    favours the covariant a0. (The cell norm also lost none of 36.)
- **The sign of c is immaterial to the outcome**, as B1962 found. Under both signs (S, S) at height 30 has the same
  smallest diagonal, 3.374e-5.
- **A note on B1962's script.** Its docstring says c = −2 "gives frame C again (up to the sign of every charge)". The
  shifted charges are (−q_R, −q_L): the sign changes and the sides swap, which is frame C transposed (W-B2). That is
  why the run's c = −2 lepton rows equal the c = 0 rows exactly, and why (S, S) at height 6 is 0.993 at c = 0 but 0.056
  at c = −2.
- **Nothing here bears on data.** The table is not set beside any measured mixing.

## 4. Typed

- **[E] by the run:** §§ 1 (E1 to E4), 2.2, 2.3 and 2.4.
- **[E] standard:** the theta shift law; the Chern connection of a hermitian metric.
- **[E] by the referee's code:** the extra digits of § 2.3, the vanishing points' a = 4/5, the map at c ≠ 0, C4 at
  a ≠ 0, the corrected E4 count.
- **[E] by the record:**
  - B1962's printed values, as far as the mask shows them, and M78's summary;
  - B1919's closed form; B1927's and B1667's tables;
  - W-B2 stages 3 and 4, and stage 4's referee.
- **[J]:** that the unitary metric is D1's own; § 3.

## Files

- `relays/chat1_2026-11-19_wb3/`: `wb3_run.py`, `wb3_followup.py`, `SCRIPT_SHA256.txt`, `wb3_run_out.txt`,
  `wb3_run_err.txt` (the stop's traceback), `wb3_followup_out.txt` and `wb3_followup_err.txt` (empty).
- The traceback's machine path is masked as `<repo>` (W-A3's precedent), in its own commit. Nothing else in the file
  changed. W-P1b's `wp1_weil_first_run_err.txt` is masked the same way.
- The card: `relays/cards/CHAT1_W-B3_frame_d1_at_the_norms_and_its_mixing.md`, with the follow-up's condition.
- Cited: B1962 and M78; B1946, B1940, B1945, B1919, B1927, B1667; this seat's W-B2, W-F22 and W-F24.

## Provenance

The first version (5c0387fe7) was pushed before its referee read finished, following the author's word of 2026-11-15
on untracked notes. A referee who had not written it read it. The verdict was sound, with corrections.
- **What held.**
  - The order of work and the SHAs.
  - Q1's derivation, checked by hand, signs included.
  - The script against the card: the tolerance, the map, the covariant a0, the triplet, the thresholds, C0 and X3.
  - F3's use of the card's rules.
  - Every number, apart from those corrected.
  - The referee's own computation, on another route, reproduced E1 at two points to 1e-58, and every covariant up and
    down number and every number of the fork.
- **Seven corrections were required.**
  1. The title's 0.1253 (a double rounding), and "reproduces B1962's table", which said more than this seat could see.
  2. E4's plain count: 30 of 36 vanish, not 29. One "survivor" was a rounding-noise channel.
  3. The fact that no coupling vanished was credited to the metric. It favours the connection; the cell norm kept all
     36 too.
  4. The independence list. The coupling, U and the lepton measures are re-typed from main's code, as are the map and
     the weight. Only the thetas, the residues at D1's pole, the Laurent a0, the triplet's route and the dual basis are
     independent.
  5. "To its four digits within rounding" was not settled by the run. It is now three digits by the run and four by
     the referee.
  6. C0's verdict line was not printed before the stop; only its rows were.
  7. The err file's machine path.
- **Smaller points, each applied.**
  - C4's points have a = 0.
  - The range 7.5e-41 to 1.8e-38.
  - B1946's statement is recalled by B1962's card, not by M78.
  - E4 was computed, unseen, in the smoke run.
  - The rewrap's extent.
  - The card's "four" against "eight".
  - The plain a0 changes the weight, not the norm.
  - All three sectors vanished at the stop.
  - Main's test file.
  - The note on B1962's docstring.

Each was checked at its source here: the referee's one-case print of E4's channels, the err files, main's code for
the re-typed parts, and the run's lepton rows. The read's corrections are applied in this version.

0 of 19.
