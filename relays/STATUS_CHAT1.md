seat: chat1
read: M45 (every file of this seat in the register read in full at d36b2a0ec and settled: 1,850 statements, none pending; § 5.3's items answered on main; the eight earlier notes of § 1d settled; W-H1's four asks paid; asked: whether main's record states this seat's work rightly, what is missing or understated, and HARVEST COMPLETE only if nothing is; no card). Before it, M44 (section 5 read; § 3.3's remainder mended; § 5.2's items and W-B2's stage 3 recomputed) and M43 (the review and W-H1 read; § 3's corrections taken)
state: HARVEST REVIEW FOR MAIN: M45 answered in § 7 below. Within the register main's record states this seat's work rightly but for ten small items (§ 7.2); outside it, this seat's older rows are owed by main's own record (§ 7.3). HARVEST COMPLETE not written
on: the harvest review (M42 to M45). Earlier: W-A3 (the author's card, = M39): the dihedral cover supplies the Heisenberg module (shifts as deck over M₂, clocks as twists by the act's fixed line) and the parity with no flux, not the act's Weil action; the frame's lines carry no class (End(W)'s trace signature), the object carries both classes (the knot's q = x²/5; the act through the cover, b(x, x) = 2x²/5, B1951's); the top-degree wedge is invariant in both classes (det ρ = 1), so up closes at level 5 in the Fock reading; frame C's 25th roots come from charge in the characteristic; nothing of level 25 in the object. W-H1 (the author's ask): the harvest checked with main's own instrument; four gaps (114 relays without a relay-ledger row, 38 not named by file; one physical-seat relay not named on main (its package is); two unwatched review lanes; the hostile seat unreachable here). Delivered: W-F17 (m = 1-6) to W-F26, W-B1, W-B2, W-V1, W-A1, W-L1, W-A2, W-Z1, W-A3, W-H1
needs: main to take or answer § 7.2's ten items; main or the author to decide the older rows (§ 7.3); main to choose the class (the knot's q, x²/5, or the act through the cover, 2x²/5 = B1951's); W-B2's sign convention; part F at S, on the up sector and for S̃ (main's, open per M38); the flux bit and the couplings as overlaps (P-863); the SM seat to re-run W-L1; W-F26's fork; the S* one-turn premise in A7 (W-F22) and N8 (W-F23); W-F21's N1 to N6
next push: on main's next message

## HARVEST REVIEW FOR MAIN

The answer to M42, 2026-11-17. **What was read**, through the mask:
- B1957's FINDINGS, its REGISTER and its records web-wa1-00 to -10;
- harvest rows 1843 to 1881 (this seat's: 1845 to 1848, 1852, 1866, 1867, 1878; and 1856, the physical lane's review);
- B1951 to B1956, and `docs/THE_PICTURE_AFTER_THE_HARVEST_2026-11-17.md`, at main 55fcbe008.

**The register's window** for this seat runs from b1727da04 to 401c9bd7e. Recounted here from `UNITS.json`, it holds
15 files and 955 statements, the same as the register. 828 are pending.

**This seat's notes are not edited.** The corrections below are stated here, dated, so that the register's units keep
their text at 401c9bd7e. Main may record the affected units as superseded by this section.

### 1. What the register does not cover

**1a. Results computed only by a referee read, whose code was not kept.** This seat's files hold no script for them.
"Covered" marks those main has since recomputed on its own code. The others are owed, or should be typed "computed
once, no file".
- **W-A1** (`relays/CHAT1_TO_CC_2026-11-15_W-A1_THE_ATTACK_ON_SELECTION_AND_THE_DICTIONARY.md`):
  - line 116: frame C is covariant under the mirror τ ↦ −τ̄, (a, b) ↦ (a, −b). The two crossings' agreement rests on
    it. **Covered**: B1957's `checks/web_wa1_rest.py`, item 4 (3.3e-16 at three τ and four lines; record web-wa1-02).
  - lines 50 to 53: the Frobenius–Schur indicators, SU(3)³, and the doublet count. **Covered**: the same script, items
    2 and 3 (record web-wa1-01).
  - line 167: the triplet's S-law, and a₃(i) = 0 at 40 digits. **Covered**: the same script, item 6 (record
    web-wa1-02).
  - line 119: the figure 0.76. Withdrawn (§ 3.2).
- **W-A2** (`relays/CHAT1_TO_CC_2026-11-17_W-A2_POSTULATE_D_FROM_THE_GROUND.md`):
  - line 26: three identifications, diag(1, 4) (the conjugate ρ), diag(1, 2) (the other class), and the swap (Z^a X^b).
    - **The T half of the first two is covered:** B1955's `class_is_a_choice.py`, item 2, computes ρ_c(T)'s shear for
      c = 1 to 4.
    - The S half and the swap are not on main.
    - This seat's referee read has since confirmed all three, each unique up to a scalar, by pure algebra.
  - line 59: the flux-5 modes realise the non-residue class.
    - The T² coefficient is now in a committed script of this seat's own (W-A3 post hoc 1, part D(F):
      `relays/chat1_2026-11-17_wa3/wa3_posthoc_word_out.txt`, line 20). That is not a recomputation by main.
    - The S kernel ψ(−jk)/√5 is in no committed script.
- **W-A3** (`relays/CHAT1_TO_CC_2026-11-17_W-A3_THE_COVER_THE_CLASS_AND_THE_UP_SECTOR.md`):
  - lines 74 to 75: |tr ρ_c(g)|² is the number of points of 𝔽₅² that g fixes. This came from the referee's correction
    (3c50b6d63). **Covered**: `class_is_a_choice.py`, item 1 (row 1878).
    - The note's typing at line 169 is wrong: `wa3_posthoc_wedge.py` computes the trace signature only, not this.
  - lines 76 to 77: one relabelling by ζ^(ab) removes both of B1953's down phases. This seat finds no recomputation on
    main.
  - lines 100 to 106: the act through the cover gives 2x²/5. **Covered**: `class_is_a_choice.py`, item 2.
- **W-B2's stage 3** (`relays/CHAT1_TO_CC_2026-11-15_W-B2_FRAME_D1_IS_FRAME_C_AT_SHIFTED_CHARGES.md`). These entered the
  window in 52bc4f053. Row 1842 checked E only, by hand reduction. Owed:
  - lines 57 to 61: c = −2 is frame C transposed (3e-15), and at residue level the massive block of |V| differs from
    frame C's by up to 0.84;
  - lines 74 to 76: the leptons copy the down rows at order 5 (1.4e-14);
  - lines 78 to 80: B1947's failure recomputed with the corrected kernel (0.58 to 7.3);
  - lines 83 to 84: the off-pole scalar, with k about −15;
  - line 94: c = +2 is new (up to 2.4 from frame C in σ₂/σ₁).
- **W-B2's stage 4** (the same note, lines 130 to 155). None of it is recomputed on main, since row 1848 is not read:
  - the cell's cut moves the differences (0.009 to 3.3);
  - D1 is not periodic under w ↦ w + τ (σ₂/σ₁ moves by 0.004 to 0.040, σ₃/σ₁ by up to 0.57);
  - E reaches the norms under the flat unitary metric, to 3e-8.
- **W-L1** (`relays/CHAT1_TO_CC_2026-11-15_W-L1_THE_LOOK_AT_TAU_I_FAILS.md`, line 47): the calibration of one row.
- **W-Z1** (`relays/CHAT1_TO_CC_2026-11-17_W-Z1_WHERE_ZETA_SITS_IN_THE_OBJECT.md`, lines 76 to 82): Hecke's period at
  discriminants 12 and 40. Not recomputed: B1955 takes G3 as a standing check.

**1b. A result in a committed output and in no note.**
- `relays/chat1_2026-11-17_wa3/wa3_posthoc_word_out.txt`, lines 29 to 32: under the card's cusp-degree reading, main's
  assignment (2, 2, 1) closes for down and for leptons in both models. The note gives only up. It is a by-product, and
  it bears on nothing now.
- A definition, not a result: the measure behind W-A1's H2 is given only in
  `relays/chat1_2026-11-15_wa1/wa1_tau_i_posthoc1.py`, lines 7 to 10. It is defined under H1, and H2 inherits it: the
  ratios' largest relative deviation, and |V|'s absolute deviation (§ 3.2).

**1c. After the window.** Three commits come after 401c9bd7e:
- f42770e18: a status update, "read M41";
- bbba03913 and 5432adc71: W-H1, the harvest checked from outside
  (`relays/CHAT1_TO_CC_2026-11-17_W-H1_THE_HARVEST_CHECKED_FROM_OUTSIDE.md`, `relays/chat1_2026-11-17_wh1/`).

W-H1 is bookkeeping, and its four asks are main's. This review comes after them too.

**1d. Earlier work main registered and has not read.** None of it has a later row that reads it:
- **W-F24's note** (rows 1833 and 1838, "its note owed"):
  `relays/CHAT1_TO_CC_2026-11-15_W-F24_WHERE_FRAME_CS_READ_OUT_LOSES_THE_HIERARCHY.md`, `relays/chat1_2026-11-15_wf24/`.
- **W-F25's note** (row 1838; its outputs were compared at row 1834):
  `relays/CHAT1_TO_CC_2026-11-15_W-F25_FRAME_CS_CUSP_EXPONENTS.md`.
- **W-F17's addendum 2, m = 5 by a second method** (row 1822): `relays/CHAT1_TO_CC_2026-11-14_W-F17_SECOND_COMPUTATIONS_FOR_COMPUTED_NOWHERE.md`
  from line 224, and `relays/chat1_2026-11-14_wf17/` (`wf17_posthoc2.py`).
- **W-C4** (row 1740, "registered by file name, not read"): `relays/CHAT1_TO_CC_2026-11-12_W-C4_THE_AGY_LANES_THEOREMS_C_D_E.md`,
  `relays/chat1_2026-11-12_wc4/`. Its Theorem C is the one main verified on its own code (M15).
- **The W-C2 and W-C3 notes and their outputs** (row 1708, "not yet"):
  - `relays/CHAT1_TO_CC_2026-11-11_W-C2_THE_AGY-EXP_SEATS_FOUR_THEOREMS.md`;
  - `relays/CHAT1_TO_CC_2026-11-11_W-C3_THE_SM_SEATS_ITEMS_UNDER_BANKED_ARCS.md`;
  - `relays/chat1_2026-11-11_wc2/` and `relays/chat1_2026-11-11_wc3/`.

  Row 1719 reads agy-exp's answers on W-C2's two counts, not the notes.
- **P-783, the golden state** (row 1713, "its head read", main's computation owed):
  `relays/CHAT1_TO_CC_2026-11-11_P-783_THE_GOLDEN_STATE_IS_THE_LOWEST_AND_SIMPLE.md`, `relays/chat1_2026-11-11_p783/`.
- **The content, asked in weave form** (row 1641, "headline only … to be read in full"):
  `relays/CHAT1_TO_CC_2026-11-10_THE_CONTENT_IN_WEAVE_FORM.md`.

Summaries written for the author outside the repository are not seat results and are not offered for the harvest.

### 2. This seat's results, in its own order of importance

The order is by how much of main's present picture rests on each result. Each result gives the one computation main
should repeat, its premises, and main's state.

1. **Level 5's Weil centre gives S(U(3) × U(2)) and one generation's hypercharges, only at p = 5** (W-A1 Part 1;
   B1951).
   - **Computation:** the commutant of ρ (ρ(T) = diag(ψ(2x²)), ρ(S) = −F) on ℂ⁵ is span{I, P}, and Λ^even(ℂ⁵) under
     6Y = (I − 5P)/2 carries D5's content (`relays/chat1_2026-11-15_wa1/wa1_weil.py`).
   - **Premises:**
     - SE3, the level is the act's discriminant;
     - postulate D's bits (B1952), with the flux bit now the cover (B1955).
   - **Main:** verified, three checks. It is standard group theory once the level is given.
2. **The figure-eight's dihedral cover supplies W and the parity, with no flux** (W-A3 Part 1.1; B1955 § 1).
   - **Computation:** the deck group of the 5-sheeted cover is trivial over m004 and C₅ over M₂ = ker(t ↦ −1), and t
     acts on ⟨X, Z⟩ by inversion (`relays/chat1_2026-11-17_wa3/wa3_posthoc_word.py`, parts A and B).
   - **Premises:**
     - m004 as the mapping torus with monodromy LR;
     - W read as the functions on the sheets.
     - Three limits: the shifts are deck transformations over M₂ only, the clocks are twists there only, and the act's
       unipotent part is not supplied.
   - **Main:** recomputed.
3. **Frame C at (i, the mark) fails the big run's statistic** (W-L1; row 1847).
   - **Computation:** `relays/chat1_2026-11-15_wl1/wl1_values.py`, checked against `LOOK_VALUES.json`'s sha256; then
     `wl1_look.py` on those values.
   - **Premises:**
     - the rule committed first (card W-L1, 82c94361d);
     - frame C as built;
     - the canonical end.
   - **Main:** NEGATIVE as sealed and provisional. The SM seat's re-run is the computation owed.
4. **The frame's lines carry no Weil class, and the object carries both** (W-A3 Parts 1.2 and 1.3; B1955 § 2).
   - **Computation:** |tr ρ_c(g)|² against the number of points of 𝔽₅² that g fixes, on all 120 g, for c = 1 and 2.
     This is main's `class_is_a_choice.py`, item 1; this seat has no script for it. The discriminant form of V + Vᵀ,
     with V = [[−1, 1], [0, 1]], is in `wa3_posthoc_word.py`, part D(K).
   - **Premises:**
     - the lines move by the record's transport (B1724);
     - the act's class 2x²/5 rests on labelling the clocks by Poincaré duality under the fibre's intersection form
       (W-A3, lines 101 to 106).
   - **Main:** recomputed, and corrected the same day.
5. **The record's lines of order 5 are W's Weyl operators, moved by the record's transport, and the flux-5 zero modes
   carry W, split 3 + 2** (W-A2; B1952).
   - **Computation:** conjugating X^a Z^b by B1951's ρ gives M_T = [[1, 0], [4, 1]] and M_S = [[0, 4], [1, 0]]
     (`relays/chat1_2026-11-17_wa2/wa2_checks.py`, part B).
   - **Premises:**
     - an identification of 𝔽₅² (the identity in W-A1's conventions);
     - for the modes, flux 5 on the filled fibre (§ 3.6).
   - **Main:** recomputed. "D becomes four counted bits" is a reading.
6. **At τ = i frame C's binaries settle: mark and twin agree, S̃ = S at all 24 points, and the two crossings agree**
   (W-A1 Part 3).
   - **Computation:** S̃ against S at τ = i on all 24 points (`wa1_tau_i_posthoc1.py`, H1 and H3). The cause is the
     triplet's S-law, which forces a₃(i) = 0.
   - **Premises:**
     - frame C as built (B1724, B1924, B1932, B1691);
     - B1927's end, with P-864's caution;
     - the mirror covariance behind the crossings, now recomputed on main (§ 1a).
   - **Main:** verified in B1957 (record web-wa1-02: I1 to I4, the plant, H1, H3, H4, G1 and the outputs at (i, mark)).
     H2 is PARTIAL (web-wa1-03; § 3.2).
7. **Frame D1, with only the Szegő zero moved, is frame C at shifted charges at residue level. At the norm level the
   answer depends on the metric** (W-B2, stages 3 and 4).
   - **Computation:** `relays/chat1_2026-11-15_wb2/wb2_stage4_posthoc1.py`: D1's σ₂/σ₁ with B1656's flat cell norms,
     against frame C at q′ = q − c·q_H/2 (0.54 at c = +2, 0.70 at c = −2). Then the same with the flat unitary metric
     e^(4π·Im h·Im z/Im τ), which only the referee read computed.
   - **Premises:**
     - B1656's quadrature norms;
     - the metric, which is the fork.
   - **Main:** the residue level was checked against main's hand reduction (row 1842). Stage 4 is not read (row 1848).
8. **The up coupling, as the top wedge, closes at level 5. Frame C's 25th roots come from putting the charge into the
   characteristic. Nothing computed in the object is of level 25** (W-A3 Part 2).
   - **Computation:** det ρ_c(g) = 1 on all 120 g, for c = 1 and 2 (`wa3_posthoc_wedge.py`, W1).
   - **Premises:**
     - the Fock-space reading;
     - the top wedge as the up coupling.
     - The closure is generic (§ 3.3).
   - **Main:** recomputed.
9. **Hecke's period along the act's geodesic is 5^(s/2)·Γ(s/2)²/Γ(s)·ζ(s)L(s, χ₅)/ζ(2s), and m004's group is
   congruence of level 4** (W-Z1).
   - **Computation:** `relays/chat1_2026-11-17_wz1/c1_hecke_period.py` at s = 1.7 + 3i and at the first zero,
     1/2 + 14.1347i. Main checked one real value, s = 2.
   - **Premises:** none from the record.
   - **Main:** Hecke's period checked at one value. The congruence level is B794's, on record and not recomputed by
     main. (Main's second checked identity, m004's volume, is outside this item.)
10. **Readings with no computation:** the choices audit (W-A1 Part 2) and the view (W-V1). Each bin names its source.

**Earlier results that main's picture leans on,** outside the register:
- W-F25, frame C's cusp exponents (row 1834; B1945, B1946);
- W-F24, the average loses the hierarchy (its note is owed, § 1d);
- W-F26, the cusp's mixing in every option (row 1839).

Each note names its computation.

### 3. Where main's record states this seat's work wrongly or too weakly

**3.1. Row 1848, W-B2's stage 4: too weak, and half stated.**
- The row records that E reaches the norms under the flat unitary metric, and that the claim was narrowed to the flat
  cell norm.
- The addendum (lines 108 to 164 of the W-B2 note named in § 1a, which the row does not name) says three things:
  - With the flat norm over the cell about the moved pole, E fails by order one (σ₂/σ₁ by 0.54 and 0.70).
  - That construction depends on where the cell is cut, and it is not periodic in the Higgs's point.
  - With the flat unitary metric, E holds (3e-8, the referee read only), and D1 then adds nothing beyond frame C at q′.
- The choice between the two is a fork, to be fixed before D1's mixing stage.
- What the row lacks: that E fails by order one under the flat cell norm, that the result depends on where the cell is
  cut, and the fork.

**3.2. B1957's records web-wa1-03 and web-wa1-09.**
- Main's PARTIAL is right for W-A1's lines 155 and 119. Those two figures are this seat's fault.
- For lines 32 to 33 the count reproduces, over the list now named. The fault was not naming the list.
- **"0.17 to 0.72"** (W-A1, line 155) mixes two measures. Here they are separately (`wa1_tau_i_posthoc1_out.txt`,
  lines 2 to 5):
  - the ratios' largest relative deviation: 0.165 to 0.701;
  - |V|'s absolute deviation: 0.415 to 0.724.

  Main's 0.41 to 0.72 in |V| is the same figure. Main's 0.07 to 0.43 is the absolute measure on the ratios, which this
  seat did not compute.
- **"Two candidates out of 32"** (W-A1, lines 32 to 33).
  - The 32 are ρ(T) = diag(ψ(kx²)) and ρ(S) = cF_s, with k in 𝔽₅*, s = ±1 and c in {1, −1, i, −i} (`wa1_weil.py`,
    lines 6 to 7, and `find_reps`, lines 69 to 79).
  - The two that pass are (2, 1, −1) and (3, −1, −1) (`wa1_weil_out.txt`, line 1).
  - This seat's referee read recounted 2 of 32. Running `find_reps` over those 32 should let main type lines 32 to 33
    VERIFIED.
- **"In S* the crossings differ (0.76)"** (W-A1, line 119). The 0.76 is in no committed file of this seat; it came from
  the referee read. **Withdrawn.** Main's figures stand in its place (web-wa1-09):
  - each crossing read at its own τ: 3.24 relative and 0.33 absolute in the ratios, and 0.30 in |V|;
  - read at one τ with the transported point, the two crossings agree in S*.

**3.3. The top wedge, stated without its caveat.**
- Where: B1955 § 3, B1953's dated note, and the picture's § 1 (the couplings).
- What W-A3 says (lines 131 to 133): the closure holds for any coupling into Λ⁵(W), because every representation of
  SL(2, 𝔽₅) has determinant 1. So it does not test the up sector's charges.
- Its answer is also conditional on the Fock-space reading (line 144).
- Row 1878 records "generic", but the arc and the picture list the closure as a gain.
- It should be typed generic and conditional, and not counted among the week's gains.

**3.4. The picture's § 1, "The knot supplies that space itself, with no flux".**
- It omits the three limits that B1955 § 1 states:
  - the shifts are deck transformations over the double cover only;
  - the clocks are twists there only;
  - the act's unipotent part is not supplied.
- § 1 should carry them, and also that the Fock-space reading has no source in the cover. The picture's § 5, item 3,
  already says that nothing explains the exterior algebra once the cover replaces the flux.

**3.5. "The recent results on ζ do not touch the object"** (row 1867; B1955's W-Z1 section; the picture's § 4). This
repeats this seat's own judgement in W-Z1, line 37, which was too strong.
- **The 11/12 bound covers both places.** W-Z1, line 31, says the bound holds for every Dirichlet L-function, ζ and
  L(s, χ₅) included. Those zeros are the zeros of Hecke's period along the act's geodesic (W-Z1, line 90).
- **The two-thirds result** is also about ζ's zeros.
- **So do the other claims.** G2 (lines 53 to 61) says the quasi-RH preprints' field is m004's trace field. If they are
  right, they bound the zeros that govern m004's cusp scattering.
- **Corrected:** if right, they bound zeros at both places G1 names, the act's geodesic and m004's cusp. Nothing on
  record uses those zeros, and they give no leverage on any open item.

**3.6. The flux bit as "a line bundle of degree 5 on the fibre"** (B1952's table and its open items). This repeats this
seat's imprecision ("it needs no puncture", W-A2, lines 63 to 64).
- W-A2's part C computed on the closed torus.
- m004's fibre is punctured, and there H² vanishes, so a degree survives only as relative data with a boundary
  trivialisation (the physical lane; B1954).
- It should read "on the filled fibre". B1955 replaces the flux by the cover, so this changes only how the replaced bit
  is stated.

**3.7. Nothing else found.** The other rows (1845, 1846, 1847, 1852, 1866 and 1878) and B1951 to B1953 were read
against the notes. Row 1866's first-version readings are corrected by row 1878 and by B1955.

**3.8. One more of this seat's own typing errors.** W-A3's table line 169 types "End(W) is the same in both classes,
and the down lines are its permutation form" as computed once by post hoc 2. Post hoc 2 computes only the trace
signature. The other two were computed by the referee read and have since been recomputed on main (§ 1a).

This section was pushed before its referee read finished, following the author's word of 2026-11-15 on untracked
notes. The read's corrections are applied in this version. Three claims of the first version were wrong:
- § 1d listed rows 11, 19, 530 and 899 as not read, but main had read them. It missed rows 1641, 1708 and 1713.
- § 1a missed main's B1957 recomputations of W-A1's referee-only results, and W-B2's stage 3 results.
- § 3.5's correction was too narrow: the bound reaches the act's geodesic too.

### 4. HARVEST COMPLETE

Not written. Lists 1 to 3 are not empty, and the register shows 828 of this seat's statements pending.

### 5. After M43 (2026-11-17, later)

**What was read**, through the mask, at main df0ce17a5:
- main's M43;
- B1957's records web-rv-01 to -07, web-wa1-03, -09 and -11, and `checks/web_review.py` with its run;
- harvest rows 1848, 1867, 1882 and 1883;
- the dated corrections in B1952, B1953 and B1955, and the picture's new § 7.

§ 1 to § 4 are left as main registered them at 9a5aafe40. This section is the state now, and replaces § 4's count.

**5.1. Taken on main.** Each was checked here against its source.
- **§ 3.1:** row 1848 now carries what it lacked, as a dated note. The stage's results are still owed (§ 5.3).
- **§ 3.2:**
  - W-A1's lines 32 to 33 are VERIFIED by main's own search (web-wa1-11).
  - Lines 155 and 119 are SUPERSEDED by § 3.2. Both measures are reproduced to three digits (web-wa1-03), and main's
    figures stand in place of 0.76 (web-wa1-09).
- **§ 3.3, in part:** B1955 § 3 and the picture's § 7 now type the top wedge's closure as generic and conditional
  (web-rv-06). Two places that § 3.3 named still state it unqualified (§ 5.4):
  - B1953's dated note, "Added 2026-11-17 (B1955; …)": "the up sector's specification is answered … an invariant at
    level 5";
  - B1955's one-line claim in `arc_verdict.json`: "the up coupling as the top wedge is invariant at level 5", under
    PROVED, with neither "generic" nor "conditional". Its scope does say that the Fock-space reading is not derived.
- **§ 3.4 to § 3.6:** taken as asked (web-rv-06).
  - § 3.4 is in the picture's § 7, which the page's head says to read with § 1; § 1 is kept as written.
  - § 3.5 is in B1955 and row 1867, and § 3.6 in B1952.
- **§ 1a, now covered** by main's `checks/web_review.py`:
  - W-A2 line 26's S half and the swap (R2);
  - W-A2 line 59's S kernel (R3);
  - W-A3 lines 76 to 77 (R4).
- **The register,** recounted here from `UNITS.json` and the records at df0ce17a5: 16 files and 1167 statements of this
  seat. 156 are verified, 5 superseded, 85 noted and 921 pending, the same as M43.

**5.2. Checked here against main's recomputations.**
- **R2's diag(1, 3) and W-A2's diag(1, 2) are one identification, read in opposite directions.**
  - `wa2_checks.py`, part B, solves φ M_g φ⁻¹ = R_g, from a representation's labels to the record's. Main's R2 solves
    D·M_ref = M′·D, from the record's labels to the representation's. So D = φ⁻¹.
  - By hand, for main's class 1 (W-A2's k = 1): M′_T = [[1, 0], [2, 1]] and M′_S = [[0, 3], [3, 0]].
    - φ = diag(1, 2) gives φ M′_T φ⁻¹ = [[1, 0], [4, 1]] and φ M′_S φ⁻¹ = [[0, 4], [1, 0]].
    - These are the record's transport.
  - Main's record (web-rv-02) is right.
- **The relabelling's sign: W-A3's lines 76 and 86 hold only when read backwards.** This corrects this seat's own text.
  - B1953 writes its law as Y(gτ, w) = c φ(g, w) U_L Y(τ, w g) U_R†. In that convention:
    - Y′(a, b) = ζ^(−ab) Y(a, b) removes both down phases, as main's R4 says;
    - for leptons the relabelling is Y′(a, b) = ζ^(+ab) Y(a, b).
  - Line 76 says "by ζ^(ab)", and line 86 says "m = 1 for down, −1 for lepton". Both hold only when read as
    Y(a, b) = ζ^(m·ab) Y′(a, b). The note does not say which way it is read.
  - **The check:** `relays/chat1_2026-11-17_rv/rv_relabel_sign.py`, run on main's `weyl_operator.py` as it is.
    - It used R4's base point, 0.13 + 1.7i (the first of B1953's two), both readings, and both generators, T and S.
    - After the right sign, the phases vary by at most 9.6e-17 (down) and 6.8e-17 (lepton).
    - After the wrong sign, they vary by 0.4 of a turn.
  - **Label:** computed once; expectations committed first. The script and its expectations are at 4aa024eb7, the
    output at 81f8bde53.
- **A by-product: the lepton lines move as a permutation too.**
  - The same run shows that one relabelling removes both lepton phases, under T and under S.
  - W-A3 states this for down, and for leptons under T only (line 86).
  - Computed once, at one base point. Lepton under S was not among the committed expectations. Not recomputed on main.

**5.3. Still owed, all of it main's.**
- **M43's list, pending in the register:**
  - W-B2's stages 3 and 4 (§ 1a);
  - W-L1's calibration of one row (§ 1a);
  - W-Z1 at discriminants 12 and 40 (§ 1a);
  - the result that is only in an output (§ 1b).
- **The 921 pending statements.**
- **Outside the register:**
  - the earlier notes of § 1d, outside its window, which M43 says will be added to it;
  - W-H1's four asks, which are debts under P-865, not register statements;
  - § 5.2's two new items: the relabelling's sign at W-A3's lines 76 and 86, and the lepton by-product. They are on
    this page after 9a5aafe40;
  - § 3.3's remainder (§ 5.4).

**5.4. List 3 has one remainder: § 3.3, at B1953's dated note and B1955's one-line claim** (§ 5.1). Main's record
states the rest of this seat's work rightly. The other wrong statement found since is this seat's own (§ 5.2).

**5.5. HARVEST COMPLETE** is not written:
- the computations in lists 1 and 2 that are marked owed are not yet repeated by main;
- list 3 has one remainder;
- 921 statements are pending.

This section was pushed before its referee read finished, following the author's word of 2026-11-15 on untracked
notes. The read's corrections are applied in this version. The first version made two claims that were wrong:
- list 3 was empty: two places that § 3.3 named still state the closure unqualified;
- § 5.3's whole list was M43's and in the register: § 1d's notes and W-H1's asks are outside it, and so are § 5.2's
  items.

### 6. After M44 (2026-11-17, late)

**What was read**, through the mask, at main d44ed1564:
- main's M44;
- B1957's records web-st5-01 to -04, web-wb2-s3-01 and web-read-02;
- `checks/wb2_stage3_on_main.py` and `checks/web_review.py`, with their runs;
- the new dated corrections in B1953's FINDINGS and in B1955's FINDINGS and `arc_verdict.json`.

**6.1. Taken on main, and checked here against the source.**
- **§ 3.3's remainder is mended.** B1953's dated note and B1955's one-line claim each carry a dated correction: the top
  wedge's invariance is generic and conditional on the Fock-space reading, it is not a gain, and the up sector's
  specification stays open. So list 3 is empty.
- **§ 5.2's two items are recomputed** (R4 and R5, web-st5-03): in B1953's convention ζ^(−ab) for down and ζ^(+ab) for
  leptons, both readings, both generators; the other sign leaves 0.40 of a turn in every case. Main's figures agree with
  this seat's run.
- **W-B2's stage 3 is recomputed on main's frame** (web-wb2-s3-01), at 0.13 + 1.7i and at residue level unless said:
  - c = −2 is frame C transposed: exactly, against the note's 3e-15, also with the norms;
  - the mixing read with right vectors differs from frame C's by up to 0.84, the note's figure;
  - the c = +2 charges are the note's; the leptons are the down coupling transposed at all 24 points of order 5 (3e-16,
    against the note's 1.4e-14), and not at (1/7, 3/7), where the singular-value ratios differ by 0.09;
  - c = +2 differs from frame C by up to 2.35 in σ₂/σ₁, the note's "up to 2.4".
  - Main takes the identity E from its own hand reduction (row 1842), as the note's stage 3 rests on it.

**6.2. The register,** recounted here from `UNITS.json` and the records at d44ed1564. Its window for this seat is at
d36b2a0ec: 16 files and 1228 statements. 205 are verified, 5 superseded, 110 noted and 908 pending.

**6.3. Still owed, all of it main's,** in M44's order:
- W-Z1 at discriminants 12 and 40 (§ 1a);
- W-L1's calibration of one row (§ 1a);
- the result that is only in an output (§ 1b);
- stage 3's two leftovers, B1947's failure with the corrected kernel (0.58 to 7.3) and the off-pole scalar (k about
  −15), and stage 4 (§ 1a);
- the earlier notes of § 1d;
- W-H1's four asks (P-865);
- the 908 pending statements.

**6.4. HARVEST COMPLETE** is not written. List 3 is empty, but lists 1 and 2 still hold computations main has not
repeated (§ 6.3), and 908 statements are pending.

### 7. After M45 (2026-11-18)

**What was read**, at main 7022a9dae:
- main's M45, through the mask;
- all 126 of B1957's records for this seat (verdict, reason and note of each) and `UNITS.json`;
- main's eight new check scripts for this seat's notes, as text;
- through the mask: the 116 new rows of `docs/RELAY_LEDGER.md` (counted, not read one by one), the instrument's two
  dated notes, and the new dated notes on harvest row 1641 and P-380;
- `checks/custody.py` and its output for this seat.

**7.1. Checked here.**
- **The register,** recounted from `UNITS.json` and the records: 24 files at d36b2a0ec and 1,850 statements. 791 are
  verified, 144 partial, 22 superseded and 893 noted; none is pending. These are M45's figures.
- **Main's eight checks, rerun** on a clean checkout of main at 7022a9dae (`relays/chat1_2026-11-18_rv45/`, G2):
  - six give their committed runs byte for byte: the post hoc closure, W-F17, Theorem C, W-F24 with W-F25, W-C2, and
    P-783;
  - in the other two, W-Z1 at discriminants 12 and 40 and W-B2's frame D1, only residuals below 1e-13 differ.
  - The outputs were compared as files and their text was not read. Main's eight results: reproduced. G2 itself, the
    comparison, is this seat's script: computed once, post hoc.
- **Main's figures against this seat's notes, item by item.** Each is as the note has it:
  - W-B2: k = −15.08 against "about −15", and the note's 3e-8, 0.54 and 0.70, 1e3 to 7e10, 0.009 to 3.3, 0.004 to
    0.040;
  - W-Z1's two periods, in the note's own formulas;
  - W-F17: the eighteen counts, the quotients 2; 4, 2, 4; 4 and 8; the components 1, 2, 2, 4, 3, 6; 308, 12 and 16;
    17 and 134; the lines at m = 4 and 8;
  - W-C2: 285, 228, 124, 20/70/34, the three volumes, +3 and −1 on 16 and 48 roots, 1350 with 1020 in the band;
  - W-C3: 8 798, 3 822, 40 and 36, 13 344, 1 601 280, 248, 55 of 745;
  - P-783: the values and their classes;
  - the weave note: sixteen errors removed by two referee reads (11 and 5);
  - W-F24's height shares and W-F25's eight cells.
- **W-F24's height law is one figure read two ways.** Main has 5.6 to 21.0 and the note 5.6 to 20.5:
  - main reads Re τ = 0;
  - the note's script averages over its eleven columns, Re τ = −0.5 to 0.5 (X1 in `wf24_run.py`).
  - This seat's committed grid gives 5.56 to 21.00 at Re τ = 0, and 5.62 to 20.47 as the mean over the columns (G1,
    computed once, post hoc).
  - The note's line 36 does not say "mean over the columns". That omission is this seat's. Main may carry the
    reading in web-wf24-02.
- **The result that stood only in an output: main's qualification is right,** and § 1b above was incomplete.
  - `wa3_posthoc_word_out.txt`, lines 27 to 32: (2, 2, 1) closes for down and for leptons only with the Higgs's charge
    0.
  - With the charge that conserves 6Y (−3 for both), it closes in neither model, and for up it closes at no charge.
- **W-H1's four asks are paid,** as M45 says:
  - 116 new rows (14 BANKED, 102 OPEN), the harmonic-transport relay's among them;
  - the two dated notes in the instrument.
  - The instrument, run here in strict mode at 7022a9dae on a fresh fetch of every branch, exits 0 with no relay
    without a row: 848 ids; the hostile seat is skipped on this clone, as its new note says.
- **Commits.** W-L1's rule 82c94361d (13:47:47), values 4a9b788d6 (13:48:09) and output ab41df26b (13:48:57) are on
  the branch in that order, as web-wl1-01 says. The look script's own commit, e364209e7 (13:48:54), falls between the
  values and the output, as the note says. b8a394419, 5004626b2, c38bec3b8 and e382e5eae are on the branch.

**7.2. Where main's record is still short, or too strong.** Ten small items. None changes an outcome.
1. **W-L1's values are verified on main already, and the record does not say so.**
   - web-wl1-01 rightly declines the comparison with data.
   - But it does not point to web-wa1-02, where the values that entered the comparison are verified: the governing
     option's seven values in `LOOK_VALUES.json` equal main's own outputs at (i, mark) at every printed digit
     (`checks/web_wa1_part3_run.txt`, line 11).
2. **W-Z1's congruence level** (web-wz1-05) is a computation, and the record files it as NOTED.
   - It agrees with B794 on both indices that make the level exactly 4: 12 modulo 4, so the group contains Γ(4); and 6
     modulo 2, so it does not contain Γ(2).
   - Main filed this seat's reproductions of banked arcs as VERIFIED in web-wc3-01. The same verdict here, VERIFIED by
     B794 for the level and partial for the indices at N = 3, 6, 7, 8 and 12, would state it.
3. **The norm fork** (web-wb2-d1-05). Main's reading is this seat's own reading of it, at lines 147 to 149 of the
   corrected W-B2 note: periodicity in the Higgs's point decides for the bundle's metric. The two agree. The record
   gives the reading as main's alone.
4. **Nine VERIFIED records say in their own notes that a figure in their statements was not recomputed:**
   - web-wa3-02: the regular cover's ℤ⁵, and u = 2ω(v, ·);
   - web-wa3-07: no D₂₅, and no ℤ/25 in the covers' homology;
   - web-wb2-d1-04: 0.58 to 7.3;
   - web-wb2-first-02: 2.2 to 7.2, and 2.3 to 2.8;
   - web-wc2-02: the 745 without the condition, and the other three conventions;
   - web-wc2-03: the 240 roots, the nine pairs, and the grading's weights;
   - web-wc3-01: the extensions in W107, W109 (iii) and W110;
   - web-wf17-04: the degrees, the point counts on κ = 2, κ varying, and completeness ("partial in its completeness");
   - web-p783-06: the dips near 6.66.
   The notes are right. But the tally of 791 counts those statements as verified, and in those figures they are partial.
5. **One of the 22 superseded statements is not a withdrawal.** In the first W-B2 note, line 55 (stage 1's plant
   holds) was not withdrawn and stands. Line 53, superseded whole, also carries V0, V1 and V3, which stand and are
   verified at lines 48, 49 and 51. Nothing is lost.
6. **The weave note's asks are done in part** (web-weave-03).
   - Ask 1 named FK11, P-380 and P-629. Ask 2 named W154's row 1388 and P-380.
   - Done: row 1641 now says the note is read, and P-380 carries the dated note. Row 1641's pointer cell has named
     P-629 and P-380 since 2026-11-10.
   - Not done:
     - the foundation's FK11 carries nothing from the note;
     - P-629's row, whose card asks which coefficients the weave forces, is last dated 2026-11-04;
     - row 1388 is last dated 2026-10-24.
   - If main judges P-380 enough, the record should say the asks were answered there alone.
7. **Three records describe a state that has since moved:**
   - web-rv-04: "not yet read";
   - web-rv-07: "not yet recomputed on main … pending under § 1a";
   - web-st5-04: "still owed by main".
   What they name is now settled or answered (web-st-1d; web-wb2-d1-05 and -06; web-wz1-02; web-wh1-01 to -03;
   web-st-lists-01 to -04). Stage 4's figures stay partial, and W-L1's calibration is left to the SM seat's re-run. A
   dated pointer would keep the three records right.
8. **The custody file records 0 commits** for W-L1, W-Z1 and the corrected W-B2 note (`checks/custody_chat1_web_seat.json`).
   - The cause: `custody.py` looks only for commit ids in backticks, and these notes give them in plain text.
   - No record cites the file, and the records' own commit checks are right (§ 7.1). But read alone, the file says that
     nothing was checked.
   - This is about main's instrument, as P-783's finding was.
9. **W-F17's statements are filed under the wrong records** (the referee read's finding, checked here against the
   note's lines).
   - web-wf17-06 (VERIFIED, E18 and E19 by Q4) holds lines 138, 139, 141 and 144. Those lines are the note's
     comparison of its projections with agy-exp's, which web-wf17-04 verifies.
   - E18 and E19's own lines, 149 to 156, sit in web-wf17-05, which is PARTIAL for T5 to T7.
   - Line 173 (the two lines at m ≡ 0 mod 4, verified by web-wf17-07) sits in web-wf17-03, the class-index record.
   - So about six statements main verified are counted as partial.
10. **Two references are off.**
    - Row 1641's dated note cites "records web-weave-01 to -04". Only -01 to -03 exist.
    - web-st-lists-02 gives the charge that conserves 6Y as −3 for every sector. For up it is +3 (the output's
      line 27). The conclusion holds.

**7.3. Outside the register.** Main's own record says that this seat's older deliveries are owed a reading in full:
- web-st-log names "the reviews' readings, W-C1, W-C5, W-F18, W-F19, the cold read, W-F3 to W-F16";
- P-865 lists the older rows in its order of work.

§ 1d above listed only the eight rows that said "not read". It took rows marked RECEIVED as read, so it undercounted.

The harvest ledger's rows for this seat, counted through the mask by main's instrument's rule
(`relays/chat1_2026-11-18_rv45/rv45_counts.py`, computed once, post hoc):
- this seat has 305 rows;
- 285 of them come before 2026-11-15: 278 dated before it, and seven six-cell rows of 2026-10-06 that carry no date;
- apart from the eight notes of § 1d, what those rows hold is outside the register;
- among the 278 dated rows, the dispositions open with:
  - RECEIVED: 31, of them 5 "read in full";
  - REGISTERED: 16;
  - UNREAD: 4 (later rows read those four);
  - and 5 rows were read only at their head.

The deliveries outside main's list fall into two groups:
- **Received and not marked read in full:** W-F1, W-F2, W-C6's part 1, W-C7, W-C8's parts 3 to 5, and the dated note
  on TICK_LINE_HIGGS's two post hoc fits.
- **Read in full at the time but outside the register:** W-F20 to W-F23, W-F26 and W-B1.

The second round for Review 79 (two of its sections read) and the addition to Review 80 (not checked) come under main's
"the reviews' readings".

Whether the harvest takes in the older rows is for main or the author to decide.

**7.4. HARVEST COMPLETE** is not written.
- **Within the register,** main's record states this seat's work rightly, except for § 7.2's ten items.
- **Outside it,** the older rows are owed by main's own record (§ 7.3).

It will be written when both of these hold:
- main has taken or answered each item of § 7.2;
- the older rows are either read into the register, or ruled outside the harvest by main or the author, with the ruling
  dated.

This page's §§ 6 and 7 come after the register's window (pin d36b2a0ec). § 7 rests on readings of main's record and on
four runs:
- committed in `relays/chat1_2026-11-18_rv45/`, each computed once and post hoc:
  - G1, the height law from this seat's grid;
  - G2, the comparison of main's eight reruns with main's committed outputs;
  - the row counts of § 7.3.
- not committed here: the eight reruns' own outputs, which are main's scripts' outputs and are compared by G2, and main's
  instrument in strict mode, computed once.

This section was pushed before its referee read finished, following the author's word of 2026-11-15 on untracked
notes; the read's corrections are applied in this version. Six claims of the first version were wrong:
- 7.3's counts (280 rows and 52);
- 7.3's list, which mixed rows read in full with rows not read;
- item 4's count of six records;
- item 7, which overstated what is paid;
- item 5, which left out V0;
- the header's "done", where W-L1's calibration was answered and not recomputed.
The referee read also added items 9 and 10 to § 7.2.

## Notes

- **The author's ruling, 2026-11-15, afternoon (the look).** The author answered in main's place that the τ = i read-out is to be tested against data, and that this seat runs the look (card W-L1): it may open the two data files the big run pins and compare W-A1's read-out with them under W-L1's rule. This seat is no longer blind to those data. Every other firewall line stands.

- **The author's ruling, 2026-11-15, early afternoon (frame C at τ = i).** The seat may evaluate frame C at τ = i and near it on the act's axis, and print the outputs; nothing is compared with data or with any value on record. Every other firewall line stands.

- **The author's ruling, 2026-11-15 morning (frame C's outputs).** To investigate the big run's negative and test a solution of the seat's own, the seat may compute and print frame C's outputs (its mass-ratio and mixing read-outs) anywhere on the surface. It may not open the data or compare any output with data; main does any comparison. This seat is no longer blind to frame C's outputs, so checks of the big run that touch data go to the SM seat or agy. Every other firewall line stands.

- **Disclosed, 2026-11-15.** Main's commit log, read through the mask to answer a question of the author, showed in words the headline of B1944 (the big run's outcome) and of its reading; the mask hides digits, not those words. No output, values file or B1944 page was opened. This seat does not compare or use it.

- **W-F17 and W-F19 delivered.** W-F17: agy-exp's quotient counts and E18-E19 reproduced; the class-index frame on m369 and s639 (40 and 72 modules with I != 0, against agy-exp's 8 and 16, whose definition is not read here); the metallic trace maps' fixed loci at m = 1-4 and 6 have no isolated point and kappa varies on every component, so B130's no-forced-choice holds component by component; T4's line count missed two lines at m = 4. W-F19: the class index is zero on every doublet at every odd level, proved by hand from a duality formula and the Klein bottle's twisted duality; blind predictions at silver and bronze odd levels all met. Both read by one session that recomputed them on its own code.

- **M27 read; W-F18 delivered.** Main ran W-F16's named test: in frame C, D∘C is not a symmetry (main's `dc_run`), and C alone is not one either (M24; B1932). So the second block keeps one free bit in frame C: H3's second row (symmetries J, K, D; relations h + o + e and q + y) gives 1. The bit is the Higgs world, which B1932 now carries as a declared input, both values run as options. The author's thesis holds for the hand, arrow and parity block; for the Higgs pair it fails in frame C, and the counterexample turns the bit into a declared input instead of a hidden choice. What could still settle it from inside is a relation that fixes the reading itself: P-847's named test (the Higgs's own twist added to the coupling, then covariance or periodicity along threads). That test is main's. W-F18 (`relays/CHAT1_TO_CC_2026-11-14_W-F18_A_COLD_READ_OF_THE_BIG_RUNS_RULE.md`, ded0292cd) answers M27's request for a cold read; it discloses a firewall slip (the mask passed the values file's numeric lines; nothing computed or quoted; this seat is no longer blind to frame C's values).

- **W-C5 delivered.** B1914 and B1915 recomputed independently (post hoc 1, after the sealed run stopped at its limit
  with no output); the cusp statement derived with the integral written out. One expectation not met: across the two
  sides, with this seat's basis of D A D's line, an orientation-keeping map swaps the twin label; the counts do not
  depend on it. Main's page names no basis for that line. Files in `relays/chat1_2026-11-13_wc5/`.
- **M15 and M16 read.** Main answered both questions: this seat computes neither Theorem D nor E (main verified A, C and
  E on its own code; D is held); P-747's note was about agy-exp's four theorems and is corrected in its row. W-C4 closes
  with its note at a1620b623. Card W-C5 proposed; M16 says to run it now, on the owner's word. Five findings of W-R81
  received; main answers them with Review 81's entry.
- **W-R81 delivered:** `relays/REVIEW_81_CHAT1.md`. Five findings (kinds 2, 7, 2, 5, 7); the six moved rows read, P-670's number
  wrong and P-694's draft not on record. Files in `relays/chat1_2026-11-13_r81/` (checks sealed at 9dad87387). Read by one
  session before it was pushed; its corrections applied but one: the closing count stays, as on every relay of this seat.
- **M14 read.** Review 81 is opened; this seat and the SM seat read first. Card W-R81 committed. The window is read
  as differences from c40446392 to the read branch, which holds planted faults whose list is sealed.
- **M13 read.** Main reports that findings 10 and 11 of Review 80's second addition hold. Finding 10, on main's own
  run: at period 5 the eliminant's factors have degrees 1 and 5, so neither loop over quadratic factors in
  `tests/test_b448.py` runs; the test is to hold that list of degrees. Both go to the builder's second series, with
  this seat's note on the answers file's header. The nine asserts in scripts get their register row in the review's
  entry. The number main gives for the quintic's discriminant is not checked here. M13 proposes no card.
- **W-C4 delivered:** `relays/CHAT1_TO_CC_2026-11-12_W-C4_THE_AGY_LANES_THEOREMS_C_D_E.md`. Theorem C of the agy lane's
  relay of 2026-11-07 is the same on this seat's own code (sealed at dc7399130; output 997332dd7; recomputed
  independently, expectations committed first). Theorems D and E are not independently checked: held by the firewall.
  Two questions to main are under `needs`.
- **M9 answered:** `relays/REVIEW_80_CHAT1.md`. Seven findings: asserts of the form `or True` read by no class, seven of
  them in main's locks; the sweep's cue word read anywhere on the line; a held file described as a held line; controls
  that skip at import under an `if` or `except`; the vacuity gate's request to shorten its table lost when all 26 are
  mended; B1891's lock missing the fourth old form; B1894 § 5's reading against the foundation's quotations. B1884
  (which verifies this seat's card) and B1889's lines on this seat left. Files in `relays/chat1_2026-11-12_r80/`.
- **M6 answered:** `relays/REVIEW_79B_CHAT1.md`. Of the ten, seven are right and complete. Three stay open: W1, W7
  and W8. The corrections reached B1882's § 1 and B1726's and B1753's notes, but not the programme's row V1, B1882's
  § 4 and § 5, its verdict line, or the law map's row. Five findings: B1861 once, B1882 three times (the bottom end
  with no menu; the audit's figure still "reproduced"; a lock line that cannot fail for one string), and B1862's
  tripwire, which accepts an unrelated "only", "parity" or "at most 20". Notes on query.py, global_form.py and B1879;
  listen.py read, no fault found. B1881 and B1885 left. Files in `relays/chat1_2026-11-12_r79b/`.
- **W-C1 delivered:** `relays/CHAT1_TO_CC_2026-11-11_W-C1_REAUDIT_OF_E7_AND_E2.md`. E2 accepted; E7 partly (six pages
  still state the zero, in the walk's own words, with no correction). Files in `relays/chat1_2026-11-11_wc1/`. The
  delivery's commit message (3dc33c6e3) says "37 planted cases"; there were 25, with two read-outs and a post hoc one.
- **M2 read.** Batch R1 is E2's line only, and E7 no longer needs this seat. W-C1 was delivered before M2 reached
  it; its E7 part is left as information for main: six pages that main's lock reads still state the zero, in the
  walk's own words, and the advisor seat's re-audit 7 did not see them. The four theorems of V1 are agy-exp's.
- **W-C2 delivered:** `relays/CHAT1_TO_CC_2026-11-11_W-C2_THE_AGY-EXP_SEATS_FOUR_THEOREMS.md`. Theorems A, B, C.2,
  C.4 and D reproduced where they use no data; C.3's count differs (1350, not 1020); A3's "two such involutions"
  differs (one); everything on overlaps held. Files in `relays/chat1_2026-11-11_wc2/`. The commit message of
  ce67c1a6c says "no cutoff of the A4 count gives 1020"; the band 6 < k ≤ 12 does.
- **W-C3 delivered:** `relays/CHAT1_TO_CC_2026-11-11_W-C3_THE_SM_SEATS_ITEMS_UNDER_BANKED_ARCS.md`. Seven items
  reproduced here (W34, W107, W108, W109 in part, W110 by census, W76's census, W83); seven held by the firewall (W59,
  W60, W62, W79, W87, W90, W101); ten arcs, sm:B1369 and B1652's W22 and W82 left to agy-exp, as M1 allows. The
  card's triage was corrected after its read: B1435 and B1652's W22 and W82 moved from held to agy-exp.
- **M6 read.** Review 79 entered (B1892); this seat's ten findings held. agy-exp answered both W-C2 questions: 1020
  counts the upper band; one involution negates the mark (its answers on its branch at a21bea23). The questions are
  closed. Card W-R79b committed.
- **M5 answered:** `relays/REVIEW_79_CHAT1.md` § 4 (the governing pages and fifteen arcs changed and not added): four
  findings (B1726 twice; GENESIS.md and WORKING_RULES.md count the suppositions against their source), a
  qualification of § 1's ROADMAP row, notes; B1853 and B1872 left, as they judge this seat's work.
- **M4 answered:** `relays/CHAT1_TO_CC_2026-11-11_M4_THE_PLANTED_CASES_AGAIN.md` (E2's lock 10 of 11, E7's 11 of 13)
  and `relays/REVIEW_79_CHAT1.md` (six findings in B1882, B1886 and B1888; B1878 and B1880 nothing found; B1889
  left, as it judges this seat's work).
- **M4 read.** W-C1 to W-C3 received; the questions to agy-exp passed on; the planted cases to be run again against
  both locks at main 323f92327; card W-R79. The owner's ruling of 2026-11-11 (P-805): a review is read by sessions
  that built none of what they read. B1889 judges this seat's work and is left, by § 13.
- **The cold read delivered:** `relays/CHAT1_TO_CC_2026-11-11_A_COLD_READ_OF_THE_THREE_PART_STRUCTURE.md` (no
  computation).
- **M3 read.** Two rulings of the owner, 2026-11-11: his messages are private and none is quoted (register row
  P-796); a check is named by its method, in the words of the protocol's § 12 (P-797). The results of W-C1 to W-C3
  in those words are on one page, sent next.
- **P-783 delivered:** `relays/CHAT1_TO_CC_2026-11-11_P-783_THE_GOLDEN_STATE_IS_THE_LOWEST_AND_SIMPLE.md`. The golden
  state is the lowest twin-odd state in all four classes and simple, by a scan to R = 11 (computed once; expectations
  committed first). 27 states in 15 values; neither of the lane's two values is a state.

- **Listener.** Main's `scripts/seats/listen.py --seat chat1` runs in the background from this seat's clone, as the
  protocol asks (main at 2f3984d27). It is silent while the page is unchanged. M1 was shown once and is read.
- **Order of work, as M1 gives it:** W-C1, then W-C2, then W-C3; then the sealed card of P-783 and the cold read of the
  three-part structure, which wait behind them.
- **The owner, 2026-11-11, in plain words:** the seat is to continue by main's recommendations and to run a silent
  listener.
- **What this seat had sent before M1** is listed on main (harvest rows to 1696). The last three relays of the day
  are verified on main (B1884, B1885, B1887).
- 2026-11-13, the author's ruling to this seat (topic: the foundation's inputs): this seat may read the agy lanes' committed work on whether the root's inputs reduce further. Read through the mask on that question only; none of their code run.
- 2026-11-14, the author's ruling to this seat (topic: the foundations): the foundations are this seat's main task; it computes the checks other seats proposed itself rather than relaying them. Card W-F1 is the first.
- **M26 read.** W-F13 and W-F14 received and entered on P-847; main's added lead: the global bit may be W-F9's order at the scar. The analyticity question under needs stays open.
- **M25 read.** Main's reading of P-847 by charge, to test or refute; W-F14 answers what can be said without the overlap. The overlap step itself is Yukawa-overlap work, which this seat's firewall holds.
- **M24 read.** Main gave P-847's two readings in words (S holomorphic; S̃ = εS*εᵀ, ε = j) and received W-F5 to W-F12; W-F13 (a reading, no values) is the answer.
- **M23 read.** Main fixes the end by analyticity (B1927) and gives τ a proof sketch (B1928, OPEN); B1924 orders histories by the letter-count measure, so this seat's Kronecker-limit growth bears only on the area version, which was not run. The ledger's rows for the end and τ (W-F10, § 2) are superseded by main's word; not checked here. P-847 (the Higgs reading) is offered as a W-F card; its definitions are asked for under needs.
- **M22 read.** Main answered the four needs and received W-C8 (complete), W-F3, W-F4 and the P-316 note; the W-F series runs on.
- 2026-11-14, morning, the author's ruling to this seat (topic: the two-way choices): the author approved card W-F16 and the cards that follow from it. The thesis to test: the surviving choices are all of one kind (a pair exchanged by an involution), and two such choices settle each other, needing no intervention from inside or outside the structure.
- 2026-11-14, later, the author's ruling to this seat (topic: the foundations' goal): the seat works on the foundations without stopping until each input of the candidate system is either derived or shown to be irreducible. A counterexample to an opposite counts as a strengthening and may justify a choice. The goal, as this seat states it: each input ends typed as derived, conditional (its opposite dies under a stated requirement) or irreducible (its opposite is alive, with the counterexample named).
- 2026-11-14, afternoon, the author's ruling to this seat (topic: the firewall, for W-B1): for main's problem W-B1 (frame D, M29) this seat may do the overlap step M25 kept with main, putting the Higgs's hypercharge twist inside the coupling, and may use B1922's definitions of S and S~ to build frame D. Every other firewall line stands: no value of a held target, no comparison with data, no CKM or J value, no frame evaluated at a named tau point or at the candidate family's addresses, no inter-sector value there.
- 2026-11-14, evening, the author's ruling to this seat (topic: the firewall, for W-F22): for the second computation of B1922's negative half (M31), this seat may evaluate the frame along the golden thread, at the frame's own line and at the lines it compares, computing the frame's outputs internally and printing only their deviations. Every other firewall line stands: no output value printed or kept, no comparison with data.
