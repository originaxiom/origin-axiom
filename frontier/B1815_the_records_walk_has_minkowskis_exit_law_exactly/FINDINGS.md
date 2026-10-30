# B1815 — THE RECORD'S WALK HAS MINKOWSKI'S EXIT LAW, EXACTLY (the owner-approved clock plan, T1–T4; data-free): THE WALK MODEL OF B1662 AND B1663 (L, R AT (1−p)/2, L⁻¹, R⁻¹ AT p/2, A FIREWALLED READING) HAS ENDPOINT LAW ν_p = (1−p)·M + p·F₊M AT EVERY p — MINKOWSKI'S MEASURE AND ITS MIRROR, SINGULAR TO AREA, P(ξ > 0) = 1 − p EXACTLY — SO, WITH τ PLACED BY ARCLENGTH ALONG THE RAY (CHOSEN), ITS AVERAGES ARE B1813's MOVE CLOCK'S. THE OBJECT'S DISCRETE SYMMETRY CANNOT DECIDE THE CLOCK; THE FRAME THAT COMPUTES THE MASSES NEVER SEES WORD LENGTH; NOTHING ON RECORD GENERATES A CONTINUOUS HOROCYCLE ACTION; THE RECORD'S ESTABLISHED RESULTS ARE CONSISTENT WITH BOTH CLOCKS. THE CLOCK STAYS CHOSEN

**Verdict: PROVED.**
- **The exit-law theorem.** Two proofs, the first checked line by line on main. An exact rational test (the
  stationarity defect is identically 0 at seven values of p) and two independent simulations, regenerated on main.
- **T2's computation:** main's.
- **T1 and T3:** a census and a reading, their load-bearing checks regenerated on main.
- **The referee:** refereed hostile (PASS WITH CORRECTIONS); its checks regenerated on main; every correction applied
  (§ 8).
- **Data-free.** cc (main), 2026-10-29, at the owner's approval of the plan in
  `docs/THE_CLOCK_AND_THE_NEXT_ATTACK_2026-10-29.md` § 8 ("they should either stand or fall by the math"; "please always
  verify").
- **0 of 19.**

## 1. The question

- **The clock.** B1813 found the weave's own measure on τ depends on the counting rule: by moves (Minkowski's measure,
  the thick phase) or by geometric length (hyperbolic area, the critical point).
- **The data cannot decide it.** B1814 had about 19% power, and one world carries about one nat.
- **The owner's ruling.** The fork must stand or fall by the mathematics.
- **The plan's four tests:**
  - T1: which established results presuppose which clock;
  - T2: which symmetry fixes "typical";
  - T3: door A, horocycle invariance;
  - T4: door B, the walk theorems.

## 2. T4 — the walk's exit law, in closed form (the headline)

**The walk.** B1663's code: L, R each with probability (1−p)/2, and L⁻¹, R⁻¹ each with p/2, i.i.d., right-multiplied.
The limit point ξ = lim X_n(∞) is a sample of the μ_p-stationary measure.
- The reversed walk has the step law μ_{1−p}. It would give P(ξ > 0) = p, and every simulation gives 1 − p.
- The walk is a model on record, not the record's adopted dynamics. GM5b adopts that inverse moves are legal; it fixes no
  walk and no weights. B1663 § 3 firewalls "the walk is the physical motion".

**The claim.** At every p ∈ [0, 1], **ν_p = (1−p)·M + p·F₊M**, with F(x) = −x and M the positive walk's exit law.
- M is Minkowski's measure on [0, ∞], the law of [a₀; a₁, a₂, …], where a₀ + 1 and a₁, a₂, … are i.i.d. Geometric(½)
  on {1, 2, …}. So a₀ can be 0.
- On (0, 1), the normalised M is d?.

**Proof** (the reader's; checked line by line on main and by the referee).
1. **The positive walk.** M = ½L₊M + ½R₊M. Since F L F = L⁻¹ and F R F = R⁻¹ exactly, as Möbius maps,
   F₊M = ½L⁻¹₊F₊M + ½R⁻¹₊F₊M.
2. **The reduction.** μ_p ∗ ν_p − ν_p = p(1−p)·[½(L₊ + R₊)F₊M + ½(L⁻¹₊ + R⁻¹₊)M − M − F₊M].
   - The claim at any one p ∈ (0, 1) is equivalent to F₊M = L⁻¹₊(M∣[0,1]) + R⁻¹₊(M∣[1,∞]).
   - This uses M∣[1,∞] = ½L₊M and M∣[0,1] = ½R₊M.
3. **Applying F** gives two symmetries of Minkowski's measure:
   - x ↦ 1 − x on [0, 1], which is ?(1−x) = 1 − ?(x);
   - y ↦ 1/y on [0, ∞], in x = 1 + y. This is the L ↔ R swap, since R = P L P with P(y) = 1/y, and i.i.d. fair letters
     are invariant under it.
4. **Uniqueness.** At every p ∈ [0, 1] the support generates SL(2, ℤ) as a group, which is all Furstenberg's uniqueness
   of the stationary probability on ℝP¹ needs. ("As a semigroup" matters only for Gadre–Maher–Tiozzo.) ∎

**A second proof** is the reader's, via PSL(2, ℤ) = ℤ/2 ∗ ℤ/3 and Forghani–Kaimanovich's invariant measures (their
Remark 1.22; `verification/T3_T4_REPORT.md` § 1.5). The referee checked its letter identities and side equation.

**Verified.**
- **Exact (`verification/referee/exact_stationarity.py`, regenerated on main, identical).** The stationarity defect is
  identically 0 as a rational on 1 500 random rational intervals at p = 0, 1/10, 1/3, 1/2, 3/4, 9/10 and 1.
  - The control with the side weight moved by 0.1 gives 0.05.
  - **The shape control:** an unequal-within-pair walk (L 0.3, R 0.2, L⁻¹ 0.25, R⁻¹ 0.25) fits no side weight in
    [0.40, 0.60] (least maximal defect 0.0125).
  - The reduced identities ?(1−x) = 1 − ?(x) and M([1, x]) = M([x/(x−1), ∞]) hold exactly.
- **Main's simulation (`verification/exit_law_check.py`, `.json`).** 20 000 exit points per p, by composing the
  sampled word from the inside out.
  - p = 0.1, 0.25, 0.5, 0.75: the two-sample KS distance to samples of (1−p)M + p(−M) is 0.011, 0.008, 0.008 and 0.015.
  - The last exceeded the 5% critical value 0.0136 (p ≈ 0.02), so it was rerun (`exit_law_check_seed2.py`, `.json`:
    seed 7531, 40 000 samples): 0.006 against 0.0096.
  - The referee's reseed (seed 4242) gives 0.0093, 0.0079 and 0.0104 at p = 0.25, 0.75 and 0.9.
  - P(ξ > 0) = 0.901, 0.749, 0.501 and 0.251, against 1 − p.
- **The reader's stationarity check (`verification/stationarity_check.py`, regenerated on main).** |z| ≤ 1.8 at
  p = 0, 0.25 and 0.5. The moved-side control reaches 123. It tests the side, not the shape; the exact check above
  tests the shape.
- **The referee's exact-integer walk (`verification/referee/walk_exit_fixedK.py`).** Fixed digits per walk, p up to 1:
  - P(Im τ > 2) = 0.1666–0.1683 against 0.1676;
  - P(Im τ > 3) = 0.0343–0.0351 against 0.0346, at every p.

  Two estimators agree.

**What it gives.**
- **The walk's endpoint law is singular to area at every p.** Under M the digit mean tends to 2; under Lebesgue measure
  it diverges (Khinchin).
- **The walk gives an endpoint law, not a τ-law.** Every walk position X_n(i) is the same point Γi of the modular
  surface, so the walk never moves τ. With τ placed by arclength along the geodesic ray to ξ (B1663's instrument,
  CHOSEN), the ray's averages are the lifted Minkowski measure's: P(Im τ > 3) ≈ 0.0346, and B1663's averaged defect
  0.517. **With that placement, the walk is B1813's move clock exactly.**
- **B1663's T2 and T4(b) become theorems.**
  - P(ξ > 0) = 1 − p.
  - The shape does not depend on p, so "the pull-back's strength is idle" for the shape is exact.
  - T3's escape rates are not covered.
- **B1813's referee check 5 is explained.** That check measured the closed geodesic of X_n's conjugacy class, not the
  ray. The cyclically reduced word of X_n agrees with ξ's expansion up to O(1) letters at its ends, and the reversed walk
  has step law μ_{1−p}, so both axis endpoints are Minkowski-shaped.
- **Scope.**
  - The closed form holds for i.i.d. letters with equal weights within each pair (B1663's own scope).
  - Unequal weights give Denjoy exit laws: a continuum of singular clocks.
  - Singularity holds for any i.i.d. walk with finite first word moment whose support generates the group:
    Gadre–Maher–Tiozzo, NYJM 2015 = CMH 2017 Cor. 1.2; Deroin–Kleptsyn–Navas 2009; Bénard 2024; Blachère–Haïssinsky–
    Mathieu at p = ½ (read at source by the reader).
  - Infinite-moment walks can have the Lebesgue exit law (Furstenberg).

## 3. T2 — which symmetry fixes "typical"

**(a) Computed (`verification/minkowski_quasi_invariance.py`, `.json`).**
- Conjugated by Minkowski's ?, S becomes piecewise linear with six power-of-2 slopes (2 to 64) on [1/64, 63/64], and R
  has slope ½, stable at grid depths 6, 8 and 10.
  - T's slope 1 is built into the extension ?(x+1) = ?(x) + 1, so it is not a test.
  - S and T already generate the group.
- The rigorous global statement follows from § 2: ν_p (0 < p < 1) is stationary with symmetric support, so g₊ν_p ≪ ν_p
  for each generator, hence for all of SL(2, ℤ).
- A rational translation outside the group (x ↦ x + 1/3) becomes singular: 234 distinct slopes, down to 10⁻²¹.
- **So SL(2, ℤ) cannot decide the clock.** SL(2, ℝ) forces the Lebesgue class, and any element outside SL(2, ℤ) already
  excludes Minkowski's class. The referee's digit check: deep digits of x + 1/3 have frequency of 1 at 0.415 and mean
  5.54, against 0.500 and 2.00.

**(b) Read: what the frame rests on.**
- FR-FIB (B1656 through B1740's module) uses only τ, the line (α, b) and B1667's radius column. A thread enters only
  through its axis and the lines it fixes (its trace, B1733). Word length appears nowhere in the construction (checked
  in the code by the referee).
- B1667's canonical end is built from the fibre's hyperbolic uniformisation.
- The moduli of such fibres carry at least two canonical continuous metrics:
  - Teichmüller, whose volume is hyperbolic area;
  - Weil–Petersson, defined by the fibre's hyperbolic metric. Its height tail is ~ 1/Y²: Wolpert's boundary asymptotics,
    with the referee's estimate ℓ ≈ π/Im τ and ω_WP = ℓ dℓ ∧ d Re τ giving a density of about π²/Y³. To read at
    source (P-481).
    > *Sharpened 2026-10-29 (B1816): read at source and computed on B1667's instrument — g_WP = (π²/2)∣dτ∣²/(Im τ)³ near the
    > cusp in Wolpert's normalisation (π² in ω = dℓ∧dt), volume π²/12, tail ≈ 3/(Y + 4 ln 2/π)²; the accessory parameter
    > is its primitive on the gated branch. Nothing ranks area against WP.*
- **Within FR-FIB the move clock is not frame-native.** This is a statement about naturality, not a theorem about the
  world.
- **The brane reading fails.**
  - In B1812's convention K_[0,1] = R and K_[1,0] = L⁻¹.
  - L is conjugate to no 7-brane monodromy: every K_[p,q] is conjugate to K_[1,0] = L⁻¹. No K_[p,q] equals L for
    |p|, |q| ≤ 20, and none is conjugate to L within entries up to 6 (main's check). L is conjugate to R⁻¹.
  - A positive word mixes a brane letter with an inverse-brane letter, so its length does not count branes. B1812
    identifies the word LR with the total monodromy of the E₁₀ configuration, on twelve branes (A⁹BCC)
    *["ten-brane" corrected 2026-10-30, Review 73]*.
  - The move clock has no shown home in the brane layer. P-482, raised as main's reading, is refuted.

## 4. T3 — door A: horocycle invariance

- **Dani 1978, Theorem A** (read at source by the reader; checked by the referee). On SL(2, ℝ)/SL(2, ℤ), every finite
  ergodic horocycle-invariant measure is Haar or uniform on one closed horocycle. Horocycle and geodesic invariance
  together force Haar, i.e. area.
- **The record has only discrete steps:**
  - T and S as relabellings (B1724, B1733);
  - L and R as updates and records (GM2, W34);
  - the geodesic flow through its threads.
- **The sweeps.**
  - The reader's wide sweep matched 185 arcs.
  - `VERDICT topic-sweep /horocycle flow|continuous shear|unipotent (flow|action)|shear flow|τ ?→ ?τ ?\+ ?t\b/ (full text): 0 of 1561 arcs on main match (none); 1 register rows match (QUEUED 1)`
    matches only P-472.
  - The referee's sweep (isomonodromy, Painlevé, earthquake, Fenchel, twist flow, axion, shift symmetry) matched 11
    arcs, none a horocycle action.
- **Continuous flows on record.** B169's isomonodromy (Painlevé VI) flow, which GENESIS GAP5 calls "a
  monodromy-preserving flow", and B944.
  - B169's time is the modulus itself. It is not a symmetry τ → τ + t of a measure.
  - The hyperbolic shear natural to B1667's fibre (the Fenchel–Nielsen twist, or earthquake flow) preserves the
    Weil–Petersson form, not area (Wolpert; the referee's recollection, to read at source).
- **B1667's Re τ = ¼ column is an interpolation, not a symmetry.** L_max varies over Re τ by 0.49% at Im τ = 1 and by
  ≤ 10⁻⁵ from Im τ = 2.
- **Door A is a CHOSEN door, not a forced one.** The flat horocycle flow would have to be added as a symmetry of the
  measure.

## 5. T1 — the record's established results are consistent with both clocks

The census is the reader's (`verification/T1_consistency_census.md`).

- Every established result whose conclusion changes with the clock names its ordering in its own claim: B1666 by trace,
  B1629 and B1663 by the walk or uniform words, B1722 by "the record's own measures".
- The conclusions other results build on are clock-neutral: B1633's scalar and B1676's mod-8 law (the reader's checks).
- Seat items that need the geometric clock are not established: § 320 READ, W57 REGISTERED.

**Regenerated on main.**
- **The quarter.** The share of threads with #L ≡ #R (mod 4) is 0.248 by trace ≤ 400 (0.252 at ≤ 200).
  - By word length it has no limit; it alternates with the parity of the length cut: 0.324 at cuts 14 and 16, 0.172 and
    0.174 at cuts 13 and 15.
  - The referee's enumeration agrees: even cuts 0.318–0.327, odd cuts 0.172–0.176.
- **B1666's per-thread quantity,** by its own function: 0.504, 0.507 and 0.508 by word length 10, 12 and 14 (0.517–0.518
  length-weighted), against 0.319 by trace ≤ 200.

**So the walk model could be the programme's whole dynamics without contradicting any established result.** Nothing
forces it either. The costs and the one contradiction, if it were:
- **P-180's ruled reason,** "Primitive threads of one length are equal time in the motion", is false of the walk, where
  equal steps are equal time. It is a ruling's reason, not a result.
- **THE_WEAVE's gloss** "the weave side meeting the wave side's constant" (B1666) would become a CHOSEN ordering: the
  move ordering gives 0.517.
- **The SM seat's § 320 and W57** would be relabelled CHOSEN (the census, § 4.3).

## 6. What it means (a reading)

- **The clock stays CHOSEN.** The plan's four tests narrowed where it can be decided:
  - the object's discrete symmetry cannot decide it (§ 3a);
  - the frame that computes the masses is native to continuous clocks and never sees word length (§ 3b);
  - the walk model, with equal weights within each pair, gives the move clock exactly (§ 2);
  - nothing on record generates the continuous symmetry that would force area (§ 4);
  - nothing established depends on either (§ 5).

  Other clocks stay open: B1813's s-family, the unequal-weight walks' Denjoy laws, Weil–Petersson.
- **A reading, not a computation.** The record's one computed τ-dynamics, the one-loop potential of W62's frame on the
  half-period line (B1686, B1704), runs to the cusp for every content on record: every cusp total is positive.
  - Holding τ at i or on the unit arc takes three or more trivial-sector Weyl fermions, where there is no hierarchy.
  - Holding τ in the hierarchy band needs a fine-tuned bosonic content: 89–95 scalars in ρ_Q without the gauge fields,
    595–672 with them, 689–780 with the graviton.
  - So the question of which measure the world is drawn from, and the record's "what holds τ" (P-251), meet at the same
    missing ingredient: a dynamics for τ in the frame that neither runs away nor is put in by hand.
  - This is a reading. The briefing's T6 was not computed. A runaway brackets every normalisable measure and selects
    none.
- **Our depth.** The strip, Im τ ≈ 3, comes from the earlier frame arcs (P-373). It is a 3.5% tail under the move clock
  and ordinary under area; neither picks it.
- **0 of 19.**

## 7. Corrections this reading found, applied at landing

- **THE_WEAVE's "the quarter of threads"** (B1666's entry) is a by-trace number. By word length the share alternates
  with the cut's parity (0.17–0.32). A dated scope note.
- **B1637 § 2's "no weight there"** under the uniform word measure: the move clock puts 3.5% above Im τ = 3 (B1813). A
  dated sharpening.
- **B1663's Guivarc'h–Le Jan citations** (§ 0; its sealed instrument's docstring, T4(c)).
  - The 1993 paper and the 1996 note contain no random-walk theorem.
  - The singularity corollary is attributed by Blachère–Haïssinsky–Mathieu (Theorem 1.10) to the 1990 C. R. note, which
    was not read.
  - The citation should rest on Gadre–Maher–Tiozzo, Deroin–Kleptsyn–Navas, Blachère–Haïssinsky–Mathieu and Bénard.
- **B1663's length bias.** Its post-seal digit frequencies, and its ray averages too, carry a small length bias from
  pooling walks stopped at a size cap (the referee: about −0.35% in P(Im τ > 2)). B1663's 0.5157 against the
  length-weighted 0.5176 is consistent with it. No verdict changes.
- **B1813's Seen first omits B1666** (P-470). A dated note.

## 8. The referee (hostile, read-only; `verification/referee/`)

**PASS WITH CORRECTIONS.** The mathematics of § 2 is correct. It was checked line by line, by an exact rational test,
and by an independent exact-integer simulation up to p = 1.

**Required corrections, all applied:**
1. The walk is a firewalled model, not the record's adopted dynamics.
2. The walk gives an endpoint law; the τ-law needs the arclength placement, which is CHOSEN.
3. "No longer a continuum of options" was false: Denjoy walks and the s-family remain.
4. The bracket:
   - B1704's numbers were misused;
   - "only the continuous measures sit between" was false;
   - it is labelled a READING.
5. The brane reading fails (L is not a brane monodromy).
6. The quarter by word length alternates with the cut's parity.
7. The KS rerun's provenance.
8. § 5 carries P-180's contradiction, THE_WEAVE's gloss and the costs.

**Recommended, applied:**
- the uniqueness wording;
- M's digits;
- the shape control;
- the scope of "theorems";
- check 5's bridge;
- T2(a)'s wording;
- T3's sweeps and B169;
- "at least two" metrics;
- the Seen-first additions;
- the source of "our depth";
- the attribution wording;
- the length bias in B1663's ray averages.

**Main's verification:** the referee's exact check regenerated on main identically
(`verification/referee/main_rerun/`). The brane and parity refutations were recomputed by main.

## Seen first

- `VERDICT topic-sweep /exit law|harmonic measure|stationary measure|Minkowski|question.mark|horocycle|Dani|quasi.invariant/ (full text): 49 of 1561 arcs on main match (NEGATIVE 20, PROVED 29); 26 register rows match (DECLINED 1, DONE 10, QUEUED 15)`
  - "horocycle" mostly matches the canonical end's horocycles.
- `VERDICT topic-sweep /exit law|harmonic measure|stationary measure|Minkowski|question.mark/ (full text): 16 of 1561 arcs on main match`
  - No arc gives the walk's exit law in closed form.
  - B1663 has it empirically.
  - B1813 has Minkowski's measure for uniform words, not for the walk.
- **Bearing on it:**
  - arcs: B21 (the Goldman/Weil–Petersson bracket), B97, B169, B944, B1629, B1633, B1637, B1662, B1663, B1666, B1667,
    B1676, B1686, B1704, B1812, B1813, B1814;
  - GENESIS GM1–GM4 and GM5a–GM5d, § 3, GAP5;
  - P-180;
  - register rows P-438–P-441, P-469 (settled here: the walk's averages are 0.517, not 0.315), P-472, P-473, P-474,
    P-477, P-480, P-481, P-482.
- **Literature (read at source by the reader unless marked):**
  - Gadre–Maher–Tiozzo (2015/2017);
  - Deroin–Kleptsyn–Navas (2009);
  - Blachère–Haïssinsky–Mathieu (2011);
  - Bénard (2024);
  - Forghani–Kaimanovich (2025, Remarks 1.21–1.22);
  - Dani (1978, Theorem A, scanned original);
  - Strömbergsson (2004);
  - Furstenberg; Khinchin;
  - Minkowski's ? (Denjoy, Salem; not read);
  - Wolpert (not read; to read at source).
