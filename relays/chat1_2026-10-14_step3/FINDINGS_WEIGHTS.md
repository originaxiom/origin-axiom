# Step 3a — the weights cells: at rank three and given H-ORTH, no thread to length 8 splits the light pair as the up quarks and leptons need; the (3/2, 7/2) cell keeps the pair together, and the (−½, 7/2) cell has rank two on every thread

> **2026-10-15, after the owner's question and the audit of the negatives** (last two sections;
> `../chat1_2026-10-15_audit/AUDIT_OF_THE_NEGATIVES.md`).
> - **The substantive negative stands across the completions computed:** no completion splits the light pair at rank
>   3.
> - **The ring completion E4·F** is parameter-free and the same on every thread. Under it the (3/2, 7/2) cell has rank 2:
>   R's isotropy reaches it, and its first generation is massless on every thread. S2's inequality is then met only
>   trivially.
>   - That rank is a knife-edge: it needs the + mode's f-admixture to be exactly zero.
>   - The other parameter-free completion, ϑ², has admixture −4 and rank 3. Its split is not yet computed.
> - **In the (−½, 7/2) cell** the root gives 1 : 0.0184 : 0 under E4·F, far below its low-lying neighbours.
> - **Two sentences below are corrected:** "a completion other than H-ORTH, which would be a fit", and "right as made"
>   for "the root has no hierarchy".

chat1, 2026-10-15, after midnight. This is step 3 of the owner's plan of 2026-10-14 (23:30, agreed): before choosing a
thread, ask whether the thread frame can split the light pair at all.
- **Sealed** at `641ef8d94` (sha256 c332b494…), before main banked the tribunal.
- **The script** `weights_cells.py` was committed at `2852877a3`, after the seal. It ran once (1057 s), starting at
  00:33. That was after main banked THE FRAME TRIBUNAL at `c1e006b43` (S126, B1652), which was the seal's precondition.
- **Output** `weights_cells_run.txt` and `weights_cells.json` (`a8267245b`), committed before this read-out.
- **Refereed once,** read-only, by an agent of chat1's. It upheld the protocol, all six outcomes and the figures. Its
  corrections to the draft's readings are taken; see the last section.
- **0 of 19. No arc number claimed. Nothing to CLAIMS.md, GENESIS or the ledgers.**

## Scored

| | prediction | prior | outcome |
|---|---|---|---|
| Q0 | the controls hold | 88% | **HOLDS.**<br>(a) C1 reproduces `lagrange_law.json` to 8.2·10⁻¹⁶.<br>(b) Every recorded residual is below 6.5·10⁻⁴¹, and h at 5/2 equals W72's banked coefficients exactly.<br>(c) Every integrand of the three cells and the three norms is invariant to 8.7·10⁻¹⁴ under 20 moves, so no cell is void.<br>(d) On the root the completion does not depend on the particular solution, to 2.3·10⁻¹⁶.<br>(e) On LLRLRR the masses are unchanged under five changes of mode basis, to 1.5·10⁻¹¹ of m₃ |
| **S1** | C3 has rank 2 on every admitted thread | 97% | **HOLDS:** 59 admitted, m₁/m₃ below 2.3·10⁻¹⁷. The zero is exactly the F₊ = R row of Y |
| **S2** | some admitted C2 thread has m₁/m₂ ≤ 0.005 with m₂/m₃ in [0.002, 0.07] | 25% | **FAILS.** 18 admitted threads lie in the band, and none has m₁/m₂ below 0.769 |
| S3 | C2's least m₁/m₂ in the band is below C1's 0.0515 | 50% | **FAILS:** 0.769, on the mirror pair LLLRR and LLRRR |
| S4 | some admitted C3 thread has m₂/m₃ in [0.002, 0.07] | 70% | **HOLDS:** 32 of 59, the root among them (0.0215) |
| S5 | the root has C2's largest m₂/m₃ | 70% | **HOLDS:** 0.809. The next is LLRR's 0.126 |

**Admission.**
- The same 59 of 69 threads are admitted in every cell. The ten excluded all have y > 3; they are the Lagrange law's
  ten.
- The worst admitted agreement between N = 256 and N = 384 is 1.7·10⁻⁶ (C1), 3.0·10⁻⁷ (C2) and 8.5·10⁻⁹ (C3).

## The read-out

**The root in each cell** (m₃ = 1):

| cell | Higgs | masses | m₁/m₂ |
|---|---|---|---|
| C1 = (3/2, 3/2) | h at 5/2 | 1 : 0.369 : 0.0096 | 0.026 |
| C2 = (3/2, 7/2) | h at 9/2 | 1 : 0.809 : 0.618 | 0.764 |
| C3 = (−½, 7/2) | h at 5/2 | 1 : 0.0215 : 0 | 0 |

**C2: one heavy state against a pair that stays close together.**
- m₁/m₂ is between 0.41 (LLLLR) and 0.83 on every admitted thread, and between 0.769 and 0.823 in the band.
- Its m₂/m₃ still falls with height, from the root's 0.809 down. Spearman(y_max, ln m₂/m₃) is −0.996, as in C1. Mirror
  pairs break ties differently, so the fourth digit is not stable.
- The root's 0.8086 and 0.6179 are not φ/2 and 1/φ. Their relative differences are 5·10⁻⁴ and 1.5·10⁻⁴, while
  N = 256 and N = 384 agree to 5·10⁻¹⁴.
- The mechanism is not analysed.

**C3: rank two everywhere, and the root is its exception.**
- The left mode F₊ at −½ is R itself (Q0(b)'s identity), and G(R, F, R) = (R·R)F = 0 at every point. So no cycle
  integral can lift the zero: B1649's isotropy returns whenever R is a matter mode (S1).
- Its m₂/m₃ falls with height overall (Spearman −0.956), but the root lies far below its neighbours.
  - The root gives 0.0215.
  - The nine other distinct threads below y = 1.75 give 0.14–0.31 (LLRR 0.313, LLR 0.162).
- So in C3 the root is not the least hierarchical thread. The mechanism is not analysed.

**C1 under the invariant formula.** In the band its least m₁/m₂ is 0.0515, on LLRLRLR, as the seal quoted. Over all
admitted threads it is 0.0089, on the mirror pair LLLLRLR and LRLRRRR, where m₂/m₃ is 7·10⁻⁶.

**The nearest (thread, cell) to each sector.**
- A read-out only: no sector is assigned. It covers C1 and C2, since C3 has m₁ = 0.
- All three nearest points are in C1:
  - the down quarks: the mirror pair LLRLRLR and LRLRLRR, at log-distance 0.07;
  - the leptons: the same pair, at 1.69;
  - the up quarks: the pair LLLRLRLR and LRLRLRRR, at 2.43.
- The down-quark proximity is the post hoc coincidence the Lagrange law already reported
  (`../chat1_2026-10-14_selection/FINDINGS_LAGRANGE_LAW.md`).
  - "What it shows" 4 there gives p ≈ 0.02–0.05.
  - Its correction 5 notes that no script computed that figure. The referee's null gives 0.01–0.03 with threads to
    length 8 and 0.04–0.10 to length 12.
- C2 adds no nearer point for any sector.

**Reality on the reflection-symmetric threads.**
- On the 41 admitted reflection-symmetric threads, K_L and K_R are real to 4·10⁻¹⁸ in every cell.
- Y's imaginary part there is at most 1.2·10⁻⁵ (C2, LLLLLRRR). Whether that is quadrature error is not shown. No
  conclusion depends on it, since K is real.
- On the 18 other threads the matrices are complex, with |Im Y|/|Y| up to 4.3% in C2.

**H-ORTH.**
- The completed modes are orthogonal to f to 4·10⁻¹⁷.
- On the admitted threads the admixtures |c_b| run from 0.66 to 23.6. The excluded LRRRRR reaches 72. On the root they
  are 8.6, 2.4 and 4.0.

## What it shows

1. **At rank three and given H-ORTH, no admitted thread splits the light pair as the up quarks and leptons need.**
   **[SEALED for C2 (S2, S3); C1's figures are read-outs]**
   - The data need m₁/m₂ ≈ 0.002 (up quarks) and 0.0047 (charged leptons). The down quarks' is 0.050.
   - C1, the parameter-free cell, gives m₁/m₂ ≥ 0.0515 in the band, which is about the down quarks' value. Anywhere it
     gives at least 0.0089.
   - C2, the rank-3 alternative, keeps the pair together: at least 0.769 in the band and 0.41 anywhere.
   - The nearest value to the leptons' in the band is C1's 0.0515, a factor 11 above it.
2. **The cells have three shapes.** **[READING; no prior]**
   - C1: both ratios fall with height. In the band, m₁/m₂ stays at or above 0.0515.
   - C2: one heavy state against a pair that stays together.
   - C3: rank two, with the second generation in the band on 32 threads.
   - So in the two rank-3 cells computed, no admitted thread reaches m₁/m₂ ≤ 0.005 anywhere. The routes left are:
     - a lift of a rank-2 cell, the question main has taken as P-128;
     - the Higgs's locus;
     - another representation;
     - the (7/2, 7/2) cell;
     - a completion other than H-ORTH, which would be a fit;
     - longer threads.
3. **The zero survives integration when R is a matter mode.** **[SEALED S1, and a reading]**
   - Main's P-128 redesign says that what lifts the zero is a coupling that is not a point evaluation. Main labels that
     finding unbanked and firewalled until its arc is sealed and run.
   - Here the coupling is a cycle integral, and the zero returns on every thread, because G(R, F, R) vanishes pointwise.
   - So integration does not lift B1649's zero while R is among the matter modes. In C1 and C2, where R is not among
     them, the rank is 3. That is an observation, not a converse.
4. **"The root is the least hierarchical thread" is a statement about C1.** **[READING, given H-ORTH]**
   - The selection report and the relay say that at large c the action selects the root, "the least hierarchical
     thread", "not hierarchical enough".
   - B1652's F5 column carries this: "there it selects the root, which has no hierarchy". B1652 defines F5 by W72's
     integrands, which is C1. So both statements are right as made.
   - They do not carry over to other weights:
     - in C2 the root is again the least hierarchical (0.809);
     - in C3 it is not: it gives 1 : 0.0215 : 0, with a second generation in the band and a massless first generation
       that needs a lift, while LLRR gives 0.313.
   - So if F5 is extended beyond W72's weights, whether the classically selected vacuum carries a hierarchy depends on
     the matter's weights.
   - C3 rests on H-ORTH and has no lift, so this changes no grade.

## Fence

- **Hypotheses:**
  - H-thread;
  - H-ORTH, the minimal-norm completion of the 7/2 modes. Without it each 7/2 mode carries one free admixture of f,
    and the cell becomes a fit.
- **Object:** W72's framework:
  - matter in ρ_R at weights −½, 3/2 and 7/2;
  - the Higgs's holomorphic mode in ρ′ at 5/2 and 9/2;
  - B1644's coupling at the puncture;
  - Lyndon words to length 8 with y ≤ 3.

  Reach: *members*.
- **Not tested:**
  - H-ORTH's derivation;
  - the (7/2, 7/2) cell, whose Higgs is two-dimensional;
  - the half-period loci (B1651; main's by-hand Schur reading, P-142);
  - other representations;
  - the lift of C3's zero (P-128);
  - sectors, mixing and CP;
  - which thread.
- No value. **0 of 19.**

## Disclosed

- **Seen before the run.**
  - Everything the seal lists.
  - Between the seal (00:16) and the run (00:33), the labelled post hoc `post_hoc_invariant_masses` ran (00:17–00:23,
    output `ea0647ffc`). It computed C1, in both mass forms, on all 69 threads, including the seal's 0.0515 reference
    and the Q0(a) threads. It computed no C2 or C3 quantity.
  - Also before the run: main's S126 (B1652 banked; its relay; P-128's unbanked pre-seal finding that at a point no flat
    line lifts the zero).
  - None of these touches the instrument. The committed script ran unchanged.
- **During the run** (forms took 1047 s; no per-thread output existed before about 00:51), the dated mass-formula
  corrections were committed (`385ae39f2`).
- **One run.** No C2 or C3 number was computed before it.
- **Found in the read-out, after the run:** the C3 root's exception and the scope note in "What it shows" 4.
- **Seal against code, a nit.** The seal's Q0(b) asks for every solve's residual. For f, h at 5/2 and h at 9/2, the
  script records only the line it keeps. The plumbing disclosed in the seal showed residuals of about 10⁻⁴¹ on every
  line, so the outcome is unaffected.
- **The referee's corrections taken:**
  - item 2's conclusion was over-broad, since C1 reaches m₁/m₂ = 0.0089 out of the band;
  - the title and item 1 lacked the seal's qualifier;
  - the post hoc run above was not disclosed;
  - the base rate needed correction 5;
  - item 4 needed B1652's definition of F5;
  - a count (nine, not eight);
  - |c_b| needed scoping to admitted threads;
  - the bounds were rounded down;
  - the mirror pairs were not named;
  - "Y real to the quadrature's precision" was asserted, not shown.

## Post hoc (labelled), 2026-10-15: the completion decides the 7/2 cells

This was run at the owner's question (01:36: "are you sure about your math on all your negatives?") and after the
selection audit found the fence's "a completion other than H-ORTH, which would be a fit" wrong.
- **Script** `post_hoc_completions.py`, committed at `5073ffa9d` before its one run (864 s). Output at `735af4b8e`.
- No prediction. No sealed cell is re-graded.

**The structure.**
- Every one-unit 7/2 section on line l is E4·F_l + α f.
  - F_l is the unique one-unit −½ section.
  - E4 = 1 + 240q + … has weight 4 and leaves the unit's coefficient at 1.
  - f is the unique holomorphic 7/2 section.
- F₊ at −½ is R itself. So E4·R is isotropic, and G(X, E4·R, R) = E4·(R·R)X = 0.
- **The ring completion, H-E4, sets α = 0.** It is parameter-free and the same on every thread.
- **H-ORTH instead subtracts each thread's f-component.** That mixes f back into E4·R and gives the + mode a coupling.

**Controls.**
- The new integrands are invariant to 2.9·10⁻¹³ under 20 moves.
- H-ORTH computed from the E4 basis reproduces step 3a's sealed masses to 1.2·10⁻⁸ on every admitted thread (median
  8.2·10⁻¹²). It differs by up to 0.9% only on the ten unadmitted deep threads, where the quadrature has not converged.
- So E4·F_l lies in step 3a's 7/2 space, as the structure says.
- **The identities, checked by the referee (in scratch, with the same calls).** The script's own identity checks are
  void (below), so these come from the referee:
  - ϑ of the −½ section is s·F at 3/2, with s = e₀ + 1/24 (−5/6, −1/12, −7/12), to 2.7·10⁻¹⁶ in value.
  - Reading α and β off the one coefficient the particular sections zero, (e_i, 1/8):
    - step 3a's particular sections are E4·F_l + α_l f, with α = (−221, −4, −112);
    - ϑ²F_l, normalised, is E4·F_l + β_l f, with β = (−224, −4, −112);
    - both to 2·10⁻¹⁶.
  - So on the ± lines step 3a's particular sections are exactly ϑ²F. On e_i the two differ by 3f.

**The outcome.** Admission is the same 59 threads in every case.

| cell | completion | rank | the root | the root's place by m₂/m₃ | admitted threads in the band |
|---|---|---|---|---|---|
| C2 = (3/2, 7/2) | H-ORTH (sealed) | 3 | 1 : 0.809 : 0.618 | largest | 18 |
| C2 | H-E4 | 2 on all 59 | 1 : 0.485 : 0 | largest | 35 |
| C3 = (−½, 7/2) | H-ORTH (sealed) | 2 | 1 : 0.0215 : 0 | 36th of 59 | 32 |
| C3 | H-E4 | 2 on all 59 | 1 : 0.0184 : 0 | smallest of the 59 admitted | 5 |

- **The substantive negative stands under every completion computed: none splits the pair at rank 3.**
  - Under H-E4 the (3/2, 7/2) cell has rank 2. Its first generation is massless on every thread (m₁/m₃ below
    1.4·10⁻¹⁷), and its 2–3 ratio still falls with height (Spearman −0.997). S2's inequality is met only trivially.
- **The rank 2 is a knife-edge.**
  - In the E4 basis, the + column under any completion is c₊ times f's column. So the rank is 2 only at c₊ = 0.
  - Every completion computed with c₊ ≠ 0 gives the nearly degenerate pair: H-ORTH, and the two runs voided below, read
    as arbitrary fixed admixtures. All three have rank 3 on 59 of 59 threads, with m₁/m₂ ≥ 0.41 anywhere and ≥ 0.769
    in the band.
  - So the degenerate pair is not H-ORTH's alone.
  - ϑ², the other parameter-free completion, has c₊ = −4. It is rank 3 and not yet computed with its right admixture.
- **At leading order, then, the (3/2, 7/2) cell gives either a nearly degenerate pair (c₊ ≠ 0) or a massless first
  generation (c₊ = 0).** The (−½, 7/2) cell is massless under both completions.
  - A massless first generation is the record's own leading order (B1649).
  - Whether anything lifts it is P-128's open question (main's).
- **In C3 the root is far below its low-lying neighbours under both completions.**
  - Under H-E4 it gives 0.0184, the smallest of the 59 admitted threads, against 0.18–0.63 on the other admitted
    threads below y = 1.75.
  - Apart from the root, the lowest admitted values lie on the deepest threads: LLLLLRRR and LLLRRRRR at 0.0209 (y =
    2.8), then 0.053 and 0.072 (y = 2.8–3.0).
  - Five unadmitted deeper threads go lower. LLLLLR and LRRRRR give 0.0088 at y = 3.35, with the mirror pair agreeing
    to 4·10⁻⁴. Three others are not converged.
  - So the ratio still falls with depth, but weakly (Spearman −0.34; −0.41 without the root). The root breaks that
    trend.
  - The mechanism is not analysed.
- **For the record, not as a claim.**
  - The down quarks' m_s/m_b at M_Z is 0.0187 ± 0.0016 (HZ2021). C3's root sits 0.2σ from it under H-E4, and 1.7σ
    under H-ORTH.
  - The chance of landing within 1σ of some sector's m₂/m₃, for the five root values across cells and completions, is
    about 12–16%. That figure takes a log-uniform prior on [10⁻³, 1] or [10⁻⁴, 1], or the instrument's own 295
    admitted values (the referee). It rises to 28–35% if every ratio of the rank-3 roots counts.
  - C3's first generation is massless, while the down quarks' m_d/m_s = 0.050 is not small.
  - Nothing is assigned.
- **Void, through a defect of this script.**
  - The JSON's "identities" entries are void: I1, I2, I3, and the comparison of G(F_i, E4·R, R) by largest
    coefficients.
  - So are the completions "H-PART" and "H-THETA2" in "per thread" and "summary".
  - The cause: the fits weighted the q-coefficients by magnitude, so the highest exponents dominated. The collocation
    determines those exponents poorly; they agree to 10⁻¹⁹ through exponent 10 and are wrong at order one by exponent
    22.
  - For example I1's s on the + line came out 2.15 − 10.4i, where the structure requires −1/12. The isotropy
    comparison read 1.3·10⁻³ by coefficients; in value it is 2.7·10⁻⁴³.
  - The referee's identities (Controls, above) repair this with a one-coefficient read-out. So the right H-PART and ϑ²
    completions are a cheap rerun under their own label.

## Corrections (2026-10-15: the audit of the negatives)

1. **"A completion other than H-ORTH, which would be a fit"** (What it shows 2; Fence) **is wrong.**
   - E4·F and ϑ²F are completions with no free number, and each is the same on every thread.
   - Under E4·F the (3/2, 7/2) cell has rank two (previous section). Under every other admixture computed it keeps a
     nearly degenerate pair.
   - ϑ²F is still to be computed with its right admixture.
   - So the 7/2 cells stay hypothesis-bound: the choice of completion decides their rank.
2. **"So both statements are right as made"** (What it shows 4) **is too generous to "the root has no hierarchy".**
   - Even in C1 the root is 1 : 0.37 : 0.0096, a mild hierarchy, not none. FINDINGS_THREAD_FRAME's correction 3 said so
     the same evening.
   - The fair wording for B1652's F5 is: "in W72's cell the root's 2–3 ratio, 0.37, is 6–100 times too mild".
   - In C3 the root lies far below its low-lying neighbours: 0.0215 under H-ORTH, and 0.0184 under H-E4, where it is
     the smallest of the 59 admitted threads.
3. **Refereed.** A read-only referee checked this post hoc and its reading: the script, the controls, every quoted
   number and the void diagnosis. It found no arithmetic error. It corrected two readings of this draft before commit:
   - "S2's failure belongs to H-ORTH, not to the cell" repeated, in the positive direction, the error the audit names;
   - "most hierarchical overall" needed the y ≤ 3 qualifier.

   Its scripts are filed in `../chat1_2026-10-15_audit/auditors/post_hoc_referee/`.
