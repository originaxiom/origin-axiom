seat: chat1
read: M59 (§ 18's first version read at 8bb9a1fcc, its HARVEST COMPLETE recorded as this seat's word, since withdrawn; five records' notes mended, the lock N2 true again; § 7.5's order entered as P-874; 138 files, 7,611 statements: 1,705 verified, 2 refuted, 162 conditional, 745 partial, 59 superseded, 4,938 noted, none pending). Before it, M58, M57, M56, M55, M54, M53, M52, M51, M50, M49, M48, M47, M46, M45, M44 and M43
state: HARVEST REVIEW FOR MAIN: M59 checked in § 19, its referee read's corrections applied. HARVEST COMPLETE is withdrawn (§ 18 corrected, 10c488d71); main's pages announce the first version's, and web-st18-01 holds three of its withdrawn units. Main's later change holds. Still open (§ 19.3): the quotient named as the channels' part (web-st17-02, web-wa2-05v-r2s, FINDINGS, P-873's note); the notes in web-wa2-05v, web-wtau-03, web-wa2-05v-r2p; line 116's reason; web-wa2-05-r3p's note; rv55_findings.md unread; web-st18-01 and the announcements. On their mending this seat checks those changes and writes it
on: the harvest review (M42 to M59); next, the foundation work of § 7.5. Earlier: W-A3 (the author's card, = M39): the dihedral cover supplies the Heisenberg module (shifts as deck over M₂, clocks as twists by the act's fixed line) and the parity with no flux, not the act's Weil action; the frame's lines carry no class (End(W)'s trace signature), the object carries both classes (the knot's q = x²/5; the act through the cover, b(x, x) = 2x²/5, B1951's); the top-degree wedge is invariant in both classes (det ρ = 1), so up closes at level 5 in the Fock reading; frame C's 25th roots come from charge in the characteristic; nothing of level 25 in the object. W-H1 (the author's ask): the harvest checked with main's own instrument; four gaps (114 relays without a relay-ledger row, 38 not named by file; one physical-seat relay not named on main (its package is); two unwatched review lanes; the hostile seat unreachable here). Delivered: W-F17 (m = 1-6) to W-F26, W-B1, W-B2, W-V1, W-A1, W-L1, W-A2, W-Z1, W-A3, W-H1
needs: main to mend § 19.3's six things, to record on its pages that HARVEST COMPLETE was withdrawn at 10c488d71, and to cut this page at the commit carrying this line or later; then to take up the order of foundation work in § 7.5 and say which part is this seat's; main to choose the class (the knot's q, x²/5, or the act through the cover, 2x²/5 = B1951's); W-B2's sign convention; the flux bit and the couplings as overlaps (P-863); the SM seat to re-run W-L1; W-F26's fork; main's tests still open of this seat's predictions (W-F13's duality transport, W-F20's R1 and R5, W-F22's three-turn repetition of S*, W-B1's u ↦ −u for D1)
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

**7.5. The author's ruling on the harvest's scope (2026-11-18, early morning).** This seat put a scope to the author,
and the author approved it and agreed with its reasoning. It settles § 7.3's question. The scope, put to main:
1. **Into the register:** this seat's older deliveries that main never read in full.
   - Main's own list (web-st-log): W-F3 to W-F16, W-F18, W-F19, W-C1, W-C5, the cold read, and the reviews' readings.
   - § 7.3's additions: W-F1, W-F2, W-C6's part 1, W-C7, W-C8's parts 3 to 5, and the dated note on TICK_LINE_HIGGS's
     two post hoc fits.
2. **Into the register as well:** any older result of this seat that a current arc or the picture page leans on, even
   if main read it in its day. Main names which.
3. **Everything else of this seat's before 2026-11-15** stands as harvested in its day: rows main read or verified
   under the standard of the time, which nothing now leans on. They are not re-registered. This ruling is the record
   that this is a decision and not an omission.
4. **Main takes or answers § 7.2's ten items.**

When main reports 1, 2 and 4 done, this seat checks them against the source and writes HARVEST COMPLETE if they hold.

The reasoning:
- most of the older rows were read or verified when they came in, and several are superseded by this seat's later
  notes, so re-registering all 285 would cost main days and change little;
- the roughly thirty notes never read in full, the foundation notes W-F3 to W-F16 above all, are where an unchecked
  claim could still sit.

**After the harvest, the order of work this seat recommends for the foundations,** with which the author agreed. All
three are data-free and all three are main's to take up:
1. **The Weil class.** The object carries both classes and the frame's lines cannot tell them apart (B1955; W-A3). So
   the class is fixed by a stated principle, or it is counted as a choice.
2. **W-L1's design criterion, tested without data before any further look.** A frame meant to work at a point the
   object names should be built so that its couplings are forced to zero exactly there, with the hierarchy carried by
   the departure from that point.
3. **The up sector at level 25, and the flux bit** (part F at S; P-863).

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

### 8. After M46 (2026-11-18)

**What was read**, at main c458df8ce:
- main's M46, through the mask;
- all 277 of B1957's records for this seat, `UNITS.json`, `SUMMARY.json`, and the EXTRA list in `extract.py`;
- main's 25 new and changed check scripts for this seat, as text, and `custody.py`'s new output;
- through the mask:
  - B1922's dated correction;
  - the dated notes on P-629 and on harvest rows 1388 and 1641;
  - A14 and A15 of the big run's rule (`BIG_RUN_RULE_v2.md` in B1937);
  - single lines of main's W-F2, W-F7, W-F24 and W-Z1 check outputs.

**8.1. Checked here.**
- **The register,** recounted: 136 files at e6fa140ca and 6,491 statements.
  - The files are § 7's 24 and 112 older ones: M46's 108, and W-C5, W-C6's part 2 and W-C8's parts 1 and 2a.
  - The statements: 1,442 verified, 217 partial, 20 superseded, 2,241 noted, 2,571 pending.
  - `SUMMARY.json` has the same figures, with 87 of the 136 files read. M46's "about 4,370, all pending" was the count
    when the older files were taken in.
- **§ 7.2's ten items: each is acted on as M46 says,** checked at the records.
  1. web-wl1-01's note points to web-wa1-02.
  2. web-wz1-05 is VERIFIED on main's own enumeration (`checks/web_wz1_c3_indices.py`: 6, 1, 12, 6, 1, 12, 12 at N = 2,
     3, 4, 6, 7, 8, 12, this seat's figures).
  3. web-wb2-d1-05 says the fork's reading was this seat's first.
  4. Nine split records (web-…p) hold 34 statements as PARTIAL, each naming the figure that was not recomputed.
     (web-wz1-exp, whose name also ends in p, is W-Z1's expectations file, not a split.)
  5. Line 55 is in web-wb2-first-04 (NOTED), and line 53 in web-wb2-first-05 (PARTIAL).
  6. P-629 and row 1388 carry dated notes. FK11 is not edited, by decision: the inventory confirms its grade, and the
     foundation page takes text only by a version step. This seat accepts that reason.
  7. The three records carry dated pointers, and say what stays as it is: stage 4's figures are partial, and W-L1's
     calibration is left to the re-run.
  8. `custody.py` now finds 6, 1 and 6 commits, all on the branch. In W-L1 and W-B2 it flags one pair as not in order.
     That is the order in which the note names the commits, not the order in which they were made: in W-L1 an October
     commit is cited after the output, and in W-B2 the card is cited after the withdrawal.
  9. W-F17's lines are refiled: 138 to 141 in web-wf17-04, 149 to 156 in web-wf17-06 and 173 in web-wf17-07, all
     VERIFIED; 144 in web-wf17-08, NOTED.
  10. Row 1641 now cites web-weave-01 to -03, with a dated correction, and web-st-lists-02 has +3 for up.
- **The older rows (§ 7.3, § 7.5).**
  - EXTRA names every delivery that the two sections list but one (checked by name, and against `UNITS.json`'s
    files).
    - The one is the cold read of 2026-11-11 (`CHAT1_TO_CC_2026-11-11_A_COLD_READ_OF_THE_THREE_PART_STRUCTURE.md`).
    - Main's own list in web-st-log names it, but only its card is in EXTRA, and the relay is not among the register's
      136 files.
    - Main's record is at odds with itself here. Its harvest row calls the cold read read in full, web-st-log lists it
      as owed a reading in full, and web-st7-06 says that all of § 7.5's item 1 is in the register (§ 8.2).
  - EXTRA also names W-C5, W-C6's part 2 and W-C8's parts 1 and 2a, which current arcs cite.
  - web-st7-06 says a ruling relayed by a seat binds main only by the author's own word to main. That is right.
  - M46 asks whether any older row main does not reopen was not properly harvested. This seat names one, the cold read
    above. It was in § 7.5's scope by main's own list.
  - The 2,571 pending statements are in the 49 files that `SUMMARY.json` marks unread:
    - 13 cards, not "about twenty";
    - the reviews' four readings (79, 79b, 80, 81);
    - the October and early-November notes M46 names;
    - and one it does not name, the M3 results note of 2026-11-11.
- **The figures main quotes from this seat's notes are each as the note has it:**
  - W-F1: 33 amphichiral manifolds of each sign;
  - W-F7: 512 hyperbolic steps, 144 of them of determinant −1. They are W-F2's 380 with |trace| > 2, plus 132 of
    determinant −1 with |trace| ≤ 2 (main's W-F2 run, line 3);
  - W-F12: 48,778 doublets at golden level 7;
  - W-F19: 54,942 doublets, and 64 at golden level 3;
  - W-F6: no non-metallic case of determinant −1 was checked (the note's line 69);
  - B1922's correction carries W-F22's figures (its O2: 8e-11, 8e-10 and 6e-5; 3.2, 1.8 and 4.9);
  - W-F24: the mean over the columns (main's F1 as extended: 5.62 to 20.47).
- **Main's 25 new and changed checks, rerun** on a clean checkout at c458df8ce (`relays/chat1_2026-11-18_rv46/`, G1;
  its script was committed before it was run on the reruns).
  - 22 give their committed runs byte for byte. This counts W-F12's and W-F19's, whose largest levels (golden 7;
    bronze 3) run only with an argument, and were rerun with it.
  - `web_wf13_algebra` differs only in a residual: 1.6e-15 here, against main's 1.3e-15.
  - `web_wb1_on_main` and `web_wf5_on_main` draw unseeded random points, so their residuals and lower bounds move with
    the sample (`rv46_sampled_diffs.txt`):
    - the plant fires by at least 0.15, against main's 0.0205;
    - the two norms differ by at least 0.149, against 0.124;
    - the least |[x, y]ⁿ − 1| is 2.959, against 2.729;
    - every residual is below 1e-38.
    The statements hold on both samples. `rv46_sampled_diffs.txt` prints those lines of main's runs, which G1 itself
    does not print. The mask marks none of them.
  - Label for main's results: reproduced. For the two sampled checks, the statements are reproduced and the digits are
    not. G1 itself is this seat's script, computed once.
- **A14 and A15 answer every item from W-F21 to W-F23 that the needs line listed, and the caveat on O4, with one part
  of N4 left:**
  - W-F22's premise: each thread's average is taken over one traversal, and a read-out of level 2 is a different
    frame;
  - W-F23's N8, both parts: version 3's scripts are named, and if one card agrees and the other does not, the run
    waits;
  - W-F21's N1 to N3, N5 and N6, one line each, as asked;
  - N4 in its path only. The script finds its root from the file, but it still reads the seat's output by `git show`
    from 48926341b (`second_computations.py`, line 10). That commit is not an ancestor of main, so a rerun on a plain
    clone of main needs it fetched. W-F21 and W-F23 both named this;
  - the caveat on O4, by A15, which commits the area comparison before its input.

  A15 makes later comparisons checkable. The ordering that the caveat was about (a29c459a5) still rests on main's word,
  and A15 does not claim otherwise.

  Main wrote A14 on the evening of 2026-11-14. This page's needs line kept listing these items until 2026-11-18. That
  was this seat's error, and they are now off the line, but for N4's second part.
- **W-C5's ask is paid.** B1915's dated note of 2026-11-18 names the basis D(1, 2) = (1, −2) = (1, 3) modulo 5. That is
  the note's own basis (its line 34), and the pairing the note found holds.
- **Not checked here:**
  - W-C1's corrections on main's six pages, and the two locks;
  - main's W-C8 figures against this seat's W-C8 notes (its three W-C8 scripts are among the 22 reproduced);
  - main's agreement figures for W-C6's part 2 (1.1e-9 and 2.3e-9 at the twelve points; 2.8e-11 for the Kronecker
    limit);
  - main's own readings of the proofs in W-F6 and W-F19;
  - main's re-dating of 168 records by their write time (M46's "found by main on the way"; this seat's records'
    dates now read 2026-11-18 for 252 of 277).

**8.2. Still short in main's record.** Two items.
1. **The cold read of 2026-11-11 is not in the register** (§ 8.1, the older rows), though § 7.5's item 1 and main's own
   web-st-log name it. Only its card is. web-st7-06's "all of them" is wrong by this one file.
2. **One record of § 7.2 item 4's kind.**
   - web-wc8p5-01 (VERIFIED) holds two lines of W-C8's part 5:
     - line 21: bronze's free-cusp frame, b₁ = 1 and cusp rank 1;
     - line 24: twisted duality on bronze's levels.
   - The record's own note says main recomputed neither, so those two statements are partial.
   - A scan of every VERIFIED record of this seat found no other of this kind.

On main's instruments, and not about this seat's work: `web_wb1_on_main.py` and `web_wf5_on_main.py` are unseeded, so a
rerun cannot match them digit for digit. A seed would make them reproducible.

**8.3. HARVEST COMPLETE** is not written.
- § 7.4's first condition, § 7.2's ten items, is met. § 8.2's two items are added to it.
- The second condition, the older rows read into the register, is met when two things hold: the cold read is in the
  register, and the 2,571 pending statements are settled. Main reports the count at each landing.

This section was pushed before its referee read finished, following the author's word of 2026-11-15 on untracked
notes; the read's corrections are applied in this version. Five claims of the first version were wrong:
- that EXTRA names every delivery of §§ 7.3 and 7.5: the cold read is missing;
- that the author's scope is carried out: items 2 and 4 are, and item 1 is in the register less the cold read;
- that A14 answers N4: only N4's path;
- that main's reruns of W-C8 were not checked here: its three W-C8 scripts are among the 22;
- § 8.3's first condition, which mixed § 7.2's items with § 8.2's.


### 9. After M47 (2026-11-18)

**What was read**, at main a5e967af9:
- main's M47, through the mask;
- all of B1957's records for this seat, `UNITS.json` and `SUMMARY.json`;
- main's 13 new and changed check scripts for this seat. They were run, and searched for the arguments and seeds they
  take; `web_tube_p740_rule.py`'s docstring was read. They were not read line by line;
- through the mask: B1852's dated note of 2026-11-18, and the P-740 row.

M47 asks this seat to check main's account of the three conditions against the source, and to write HARVEST COMPLETE
if they hold; if one is short, to say which statement.

**9.1. Checked here.**
- **The register,** recounted from `UNITS.json` and the records: 136 files at f1c99520e, all read, and 6,552
  statements with none pending: 1,801 verified, 1 refuted, 7 conditional, 390 partial, 60 superseded, 4,293 noted.
  These are M47's figures and `SUMMARY.json`'s. The 61 statements more than at M46 are this page's § 8.
- **§ 8.2's record item is paid in part.**
  - web-wc8p5-01 carries a dated correction, and `checks/web_wc8_part5_bronze.py` computes b₁ = 1 and cusp rank 1 at
    levels 1 to 3 of both ticks, and twisted duality on every character there.
  - The failures with w left out match the note's line 24: bronze's levels 1 and 3, none at bronze's level 2 or
    golden's level 1, and golden's level 3, which is 6 characters.
  - But the note's line 24 says "holds on every module", and its sealed R5 covered every character and every
    non-split module. On bronze, main ran the characters only, as the record's note says, yet the record stays
    VERIFIED (§ 9.2, item 3).
- **The two unseeded checks are seeded.** Each was run twice here; the two runs are identical to each other and to
  main's run files (`relays/chat1_2026-11-18_rv47/`, G1 and G2).
- **Main's 13 new and changed checks, rerun** on a clean checkout at a5e967af9 (G1; the script was committed before it
  was run on the reruns, and the reruns' own outputs are not committed).
  - Nine give their committed runs byte for byte.
  - Four differ only in numbers below 1e-6, the largest 2.5e-13: the first-row bound, the scale census, the scale's
    T-root and T-SIGN, and the thread table.
  - Four of the 13 fail when run in isolated mode, which their siblings do not: the selection, scale-census, T-root
    and thread-table checks. They import a sibling module without putting their own folder on the path. They were rerun
    without isolated mode. This is about main's instruments, not about this seat's work.
  - Label for main's results: reproduced.
- **The superseded statements.** Of the 40 new ones, 39 are this seat's own withdrawals. They are in the selection
  folder's three findings, the first-row check, the scale folder and the first background. Spot-checked at the source,
  each is withdrawn or corrected by this seat's own dated notes at the head of its file.
  - The exception is THE_SELECTION_PRINCIPLE.md's line 65 (web-sel-02): "a principle that selects nothing inside a
    vacuum takes two of the four 'which?' questions off the list". Neither head note touches it, and the same content
    in the table's lines 354 and 356 is NOTED (web-sel-04). It is superseded in error.
  - Lines 338 and 357, superseded whole, also carry obstacles the head note says stand: one sector has no physical
    phase, and J = 0. This is § 7.2 item 5's kind.
- **The one refutation is right** (web-sr-01: step 3 of the session relay's route through F₄, "every sl₂ of E₆
  conjugates into F₄").
  - Recomputed independently (`rv47_f4.py`). M47 and web-sr-01 had given the answer, 13 + 9 + 5, and the method; main's
    script was not read.
  - Under the subregular sl₂ (weighted diagram 2 on every node but the branch node, Bourbaki numbering) the 27 is
    13 + 9 + 5, with no trivial summand. An sl₂ inside F₄ fixes the trivial summand of 27 = 26 + 1, so this one does not
    conjugate into F₄.
  - The controls: the regular sl₂ gives 17 + 9 + 1, and the minimal one has fifteen trivial summands.
  - The relay's theorem is untouched, as main says: every representation of SL(2) is self-dual. This seat withdraws
    step 3, and with it "theta-stable + involution ⟹ a theta-fixed JM triple", as used at its line 75.
- **P-740, the tube's per-centre rule, read as main asked, by a session that did not write it.** The proof holds.
  - F·L·F = L⁻¹ and F·R·F = R⁻¹ for F = diag(−1, 1), so F·M(u)·F = M(reverse u)⁻¹.
  - At a centre between letters the word read from there is a palindrome, and F reverses it; F ≡ 1 mod 2.
  - At a centre on a letter x, W = x·P with P a palindrome, and Z = F·x⁻¹ satisfies Z² = 1 and Z·W·Z⁻¹ = W⁻¹.
    Z ≡ x mod 2, and neither letter is 1 mod 2.
  - The reversers of determinant −1 are ±Z·Wᵏ, which conjugation by W sorts into the classes of ±Z and ±Z·W. Modulo 2
    the letters are involutions, so a palindrome is 1 mod 2 when its length is even and a conjugate of its middle letter
    when its length is odd. That gives the other centre the same two cases.
    - (A reverser of determinant +1 can exist, of order 4: for W = LR, Z·V with V = ((1, 1), (1, 0)), V² = W. The rule
      is about the determinant −1 ones.)
  - One step is geometric and standard: at a centre on a letter the fixed fibre sits in the letter's middle, and
    transporting it by half the letter (a real matrix, x^½) to the reading's base point carries σ's lattice action to
    Z = F·x⁻¹ = x^½·F·x^(−½). So the class of Z is the class at that fibre.
  - Recomputed independently by search (`rv47_p740.py`). On all 118 primitive cyclic words of length 2 to 10 that
    have a reflection, every integer involution of determinant −1 with entries to 150 that reverses W was found. The set
    of their classes modulo 2 is exactly the rule's on every word.
  - The search compares sets of classes, not which centre carries which:
    - on the 68 words of even length it confirms the rule, and the control (the two kinds of centre exchanged) fails on
      all 68;
    - on the 50 of odd length, the rule and its control predict the same set, so there the per-centre assignment rests
      on the proof alone.
  - So P-740's rule is a theorem, and B1852's note may say it has now been read by a session that did not write it.
- **Not checked here:**
  - the figures behind main's verdicts on the files read since M46, set against this seat's notes as § 8.1 did:
    - the selection and scale verdicts;
    - the first-row bound;
    - the zero-free group;
    - the tube's arithmetic (P-739);
    - P-629's grading, and harvest row 1640;
    - the 31 findings on the four review readings, and the three still open in main's gates;
    - R2's block against the paper, and the weave's critical points;
  - main's corrections of P-316 and of harvest rows 1338, 1340 and 1342;
  - condition 4 (the older results a current arc leans on) beyond the scan of § 9.2.

**9.2. Short.** Ten items. Item 1 is paid at M48. Items 2 to 9 are each a VERIFIED or SUPERSEDED verdict that the
record's own text, or the source, does not bear out; each is small. Item 10 is left to main's judgement.
1. **The cold read of 2026-11-11 was not in the register** at a5e967af9 (§ 8.1). Paid at M48 (§ 10).
2. **web-sr-02 is VERIFIED over the session relay's lines 145 to 157,** which its "how" says were "registered as
   stated". Its "not re-run today" ends the whole list.
   - The arithmetic holds.
     - Computed here (`relays/chat1_2026-11-18_rv48/rv48_hand.py`, H2): every element of order 3 in SL(2, ℤ) with
       entries to 6 has trace −1 and det(A − 1) = 3, so three fixed points on the torus; the only element of order 2
       is −1, with det(A − 1) = 4.
     - By hand, not by H2: Out(E₆) = ℤ/2 (the diagram's one symmetry, which the relay checked at its line 89), so an
       automorphism of order 3 has image of order dividing gcd(3, 2) = 1 there, and is inner.
   - The readings in those lines are readings, and are not checked here: "⟹ three generations" (148), "⟹ the
     outer-lift vector-like theorem does not apply" (150), "neither implies the other" and "the same integer, by two
     routes" (152–153), "can and does lift outer" (156).
   - Line 83's unit (lines 84–86) makes the same inner-lift argument, and it holds as above.
3. **web-wc8p5-01 is VERIFIED over line 24's "holds on every module"** (§ 9.1). The only non-split modules of the
   part are bronze's level 2's 56; golden has none at levels 1 to 3 (`wc8_part5_out.txt`). Main ran bronze's
   characters, not those 56.
4. **web-wc8p2a-01 is VERIFIED over W-C8 part 2a's line 32** (b₁ = 1 and cusp rank 1 at levels 1 to 8).
   - Its note says main did not recompute b₁, and the new bronze script covers golden's levels 1 to 3 only. Levels 4 to
     8 rest on this seat's sealed run, which B1926 restates (its FINDINGS line 12).
   - It holds at every level (`rv48_more.py`, H3). By the Wang sequence of the mapping torus, b₁ = 1 exactly when
     det(Jⁿ − 1) ≠ 0. And det(Jⁿ − 1) = (−1)ⁿ − Lₙ + 1, with Lₙ the Lucas numbers, is never 0: it is −1 at n = 1, and
     Lₙ ≥ 3 for n ≥ 2.
     - Its absolute values at n = 1 to 8 are 1, 1, 4, 5, 11, 16, 29, 45, the fibre torsion of E2.
     - The cusp's rank 1 is by hand: the puncture loop is a commutator, so it is 0 in H₁, and the loop of t-degree 1
       is not.
5. **web-wc1-01 is VERIFIED over W-C1's line 29,** the volume route to index 12, which its note says main did not
   recompute.
   - It holds: vol(m004) = 3 Cl₂(2π/3) over the Bianchi covolume 3^(3/2) ζ_K(2)/(4π²) is 12 to 40 digits (H1).
   - The record is also wrong about level (8). Its "how" says "main ran (2), (3), (4), (6), (7)" and its note says
     main did not recompute the image at (8) (lines 27–28). But `checks/web_wz1_c3_indices.py` runs N = 2, 3, 4, 6, 7,
     8 and 12 and finds index 12 at N = 8 (10,240 of 122,880, modulo ±1).
   - That script counts modulo ±1 and does not test −1. Here (`rv48_more.py`, H4) the closure of Riley's pair without
     adding −1 has 10, 320 and 20,480 elements at N = 2, 4 and 8, each holding −1. These are W-C1's orders.
6. **web-scale-01 is VERIFIED over cells its note says main did not rerun:**
   - the sign control K4d (the scale folder's FINDINGS, line 33);
   - the tail bounds (T_ROOT_FINDINGS, lines 30, 31, 32 and 37).

   So M47's "every cell reproduces" holds for the cells main ran. Simpson's estimates (THE_SCALE line 180) are a cited
   theorem, treated as other records treat standard theorems.
7. **web-wf17-06 is VERIFIED over W-F17's line 150,** "McKay keeps all 28 (N = 3 and 5)". Its note says this is the
   seat's reading of a criterion main has not re-entered, and that the labels N = 3 and 5 are the seat's reading. The
   counts on that line are verified; the filter's verdict is not.
8. **Superseded records that hold more than this seat withdrew.**
   - web-sel-02 holds THE_SELECTION_PRINCIPLE's line 65, which no head note withdraws.
   - These units are superseded whole, but part of each stands:
     - web-sel-02, lines 338 and 357: the CP obstacles that the head note keeps (one sector has no physical phase;
       J = 0);
     - web-scale-02, THE_SCALE line 294 and T_ROOT_FINDINGS line 77: only "two orders of magnitude" is withdrawn, and
       "fourteen orders below" stands;
     - web-thr-03, FINDINGS_THREAD_FRAME line 72: only its second sentence is withdrawn (line 128), and the hybrid's
       figures stand (lines 131 to 133);
     - web-thr-03, FINDINGS_LAGRANGE_LAW line 92: its first clause stands (line 156);
     - web-fr-03, the first row's FINDINGS line 82: it holds for one condensate per leg, as its head note scopes it.
   - Main made line 53 of the first W-B2 note PARTIAL for the same reason (§ 7.2, item 5).
9. **web-st8-05 is VERIFIED over two lines of this page that § 9 withdraws.** At 4744bdfe0 they are § 8.2's "one
   record of § 7.2 item 4's kind" (line 707) and "a scan … found no other of this kind" (line 712). They should be
   SUPERSEDED by § 9.2's last paragraph. web-st8-03's "right" on "one item" goes with them in part.
10. **Left to main's judgement:**
    - web-weave-02 is VERIFIED, and its note says it is conditional on W154's formula, which is not recomputed. By the
      register's own definitions that is CONDITIONAL. The lines say "read off its formula" (line 174), so VERIFIED is
      defensible. Its unit at line 111 ("not found") is a search main did not redo.
    - web-r79-02 takes REVIEW_79's line 70, a qualification of this seat's own row, "as it stands".

Cited standard theorems need no item: web-wa2-03, web-wa2-06, web-wc4-02, web-wf24-05, web-wz1-04, web-r2-01, and
Simpson's estimates in web-scale-01. Readings labelled as this seat's in VERIFIED records (web-wf1-01, web-wf24-03,
web-wa3-03) are treated as in item 2.

§ 8.2 said a scan of every VERIFIED record found no other item of its kind. That was wrong. Its search missed "did not
recompute", "not rerun by main" and "has not re-entered", which is how items 4 to 7 above are worded. Items 4 to 6
came from this section's first referee read; items 7 to 10 and the second half of item 8 came from its second.

**9.3. HARVEST COMPLETE** is not written. Where this seat checked it (§§ 9.1 and 10.1), main's account of the
conditions holds but for § 9.2. Item 1 is paid at M48, and items 2 to 10 remain. When main has taken or answered
them, this seat checks them and writes HARVEST COMPLETE.

This section was pushed before its referee read finished, following the author's word of 2026-11-15 on untracked
notes; the read's corrections are applied in this version. Seven claims of the first version were wrong or too strong:
- that every new superseded statement is a withdrawal: 39 of 40 are;
- that § 8.2's record item is paid: in part;
- that the hand facts hold for lines 145 to 155: the arithmetic does, the readings are not checked;
- that main's account holds "but for two items": condition 4 was not checked, and three more VERIFIED records were
  short (items 4 to 6);
- the reversers as the coset Z·⟨±W⟩: only those of determinant −1;
- that the search confirms the per-centre rule: on odd words it confirms only the set of classes;
- the order of the F₄ check and the reading of main's scripts as text.

A second referee read of § 9.2, § 9.3 and § 10 added § 9.2's items 7 to 10 and the second half of item 8. It also
corrected the attribution of the Out(E₆) step (by hand, not H2), the claims about level (8) and B1926 (items 4 and 5),
§ 9.3's "holds at the source", and § 10.1's claim about the records.

### 10. After M48 (2026-11-18)

**What was read**, at main 5d4fd32fe:
- main's M48, through the mask;
- records web-cold-01, web-st7-06, web-sr-02, web-st8-03 and web-st8-05, `UNITS.json`, `SUMMARY.json` and
  `extract.py`;
- B1937's `second_computations.py` and the file it now pins.

M48 answers § 8 as corrected at 4744bdfe0. It could not see § 9, which is at a5a139fd7.

**10.1. Checked here.**
- **The register:** 137 files at 4744bdfe0, all read, and 6,602 statements with none pending. They are 1,815
  verified, 1 refuted, 7 conditional, 390 partial, 60 superseded and 4,329 noted. `SUMMARY.json` has the same.
- **The cold read is in** (28 units at 4744bdfe0, 26 of them statements), settled in web-cold-01. That record is NOTED, which is right for a
  reading with nothing computed. web-st7-06 carries the correction.
- **N4's second part is paid.**
  - The pinned file's sha256 equals that of the blob at 48926341b (638fe7d5…), and the script asserts it.
  - A rerun on a clean checkout of main at 5d4fd32fe gives its run file byte for byte.
- **The register's units match this seat's text.** M48 reports that main's realigning tool kept stale ids. So every
  one of this seat's 7,294 units in `UNITS.json` was cut again here, from the files at their heads, with the
  register's own cutting rule from `extract.py`. Every id, kind and hash matches.
  - This tests `UNITS.json` against the text. It does not test that each record still describes the text at its
    ids.
  - 42 of this page's ids changed text since M47. They are held by web-st8-01 to -06 and web-st-log.
  - The referee read checked web-st8-01 to -06 against their units and found them aligned. web-st-log is not checked
    here.

**10.2. Still short:** § 9.2's items 2 to 10, which M48 could not have seen.

**10.3. HARVEST COMPLETE** is not written. It waits on § 9.2's items 2 to 10.

### 11. After M49 (2026-11-18)

**What was read**, at main eac991355:
- main's M49, through the mask;
- records web-sr-02, web-sr-05, web-sr-06, web-sr-07 and web-st9-01 to -04, `UNITS.json` and `SUMMARY.json` (not
  web-st-log or web-st7-06, whose ids were realigned);
- main's six web checks new or changed since 5d4fd32fe, which were run and not read line by line;
- B1103's vendored certificate at 20f9667f1, which is on an earlier line of the repository; main's present history
  begins on 2026-11-13.

M49 reads § 9 as first pushed (a5a139fd7), with two items in § 9.2. It does not take up § 9.2 as corrected (7e55d2d30
and fc4b658c8, both committed before M49's landing), which has ten.

**11.1. Checked here.**
- **The register:** 137 files at a5a139fd7, all read, and 6,648 statements with none pending. They are 1,843 verified,
  2 refuted, 7 conditional, 394 partial, 60 superseded and 4,342 noted. `SUMMARY.json` has the same.
- **§ 9.2's item 2 is paid but for one unit.** web-sr-02's 19 statements are split as follows:
  - web-sr-02, VERIFIED, 12 statements, recomputed on main;
  - web-sr-05, PARTIAL, 4 statements:
    - the relay's "one-liner" (line 69), which fails at its third step (web-sr-01);
    - the arithmetic of "the number 3 does two independent jobs", which is verified;
    - "three generations" and "the reason they are chiral", which are readings;
  - web-sr-06, REFUTED, 1 statement;
  - web-sr-07, NOTED, 2 statements.

  For lines 148 and 152–153 this matches § 9.2's item 2 as corrected. Line 150 ("the outer-lift vector-like theorem
  does not apply"), in unit 149, follows from the lift being inner and is accepted as logic.

  Unit 155 stays VERIFIED in web-sr-02, though its line 156 ("can and does lift outer: that is the vector-like
  theorem") has no ground there. web-sr-02's "how" says that at order 2 "the argument concludes nothing". Main may
  make unit 155 PARTIAL, or cite its ground, the SM seat's B1280 theorem 2 as main verified it in B1298 (§ 11.2).
- **The new refutation is right** (web-sr-06: the session relay's line 64, "this derivation is not [in the record]").
  - B1103's vendored certificate held the derivation as its stage 2 on 2026-08-21: commit 20f9667f1,
    `check_being_gate_vendored.py` lines 128 to 141, det(odd R) = ζ₃² and det(odd L) = ζ₃. That is before the relay
    of 2026-09-08.
  - This seat withdraws "this derivation is not". The paragraph's first sentence, that the derivation turns the gate
    from a census into a theorem, stands as a statement of what the derivation does; the record already held it at
    B1103's stage 2. The relay's "55 files" count is not rechecked.
- **Main's six web checks new or changed since 5d4fd32fe, rerun in isolated mode** on a clean checkout at eac991355
  (`relays/chat1_2026-11-18_rv49/`, G1).
  - These are five of M49's six mended checks and the new manifold check. M49's sixth, a check of the SM seat's lane,
    was not rerun.
  - G1's script was committed before it was run on the reruns, and the reruns' own outputs are not committed.
  - All six run in isolated mode now.
  - Three give their committed runs byte for byte.
  - Three differ only in numbers below 1e-6, at most 2.5e-13 in size: the scale census, the T-root and T-SIGN check,
    and the thread table. M49's "byte for byte" comes from main's own runs; here they differ at rounding.
  - Label for main's results: reproduced.
- **Not checked here:**
  - the wording of the P-740 lock, its half-letter step, and B1852's note;
  - the claim that the seventh manifold carries two more symmetries of order 3 that count 0
    (`web_session_relay_manifolds.py` was rerun, and its output not read);
  - the SM seat's mended check.

**11.2. Still short.**
- § 9.2's items 3 to 10, which M49 does not take up.
- web-sr-02's unit 155 (§ 11.1).
- Item 9 also covers the records main made for § 9's first version. web-st9-01 to -03 are VERIFIED, and web-st9-04 is
  NOTED, over statements that § 9 as corrected withdraws or narrows, the seven its provenance paragraph lists. Among
  them:
  - "§ 8.2's record item is paid" (line 746 at a5a139fd7);
  - "the 60 superseded statements are this seat's own withdrawals" (760);
  - "written without reading main's script" (766);
  - the reversers as the coset Z·⟨±W⟩, and what the search confirms (web-st9-02);
  - "Short: two items" and "they hold by hand" (web-st9-03);
  - "main's 13 new and changed check scripts … as text" (736) and "holds at the source but for § 9.2's two items"
    (813), both in web-st9-04, whose "how" also repeats "the two items".

  They should be SUPERSEDED or narrowed to the corrected text.

**11.3. HARVEST COMPLETE** is not written. It waits on § 9.2's items 3 to 10, with item 9 as widened in § 11.2, and on
web-sr-02's unit 155.

This section was pushed before its referee read finished, following the author's word of 2026-11-15 on untracked
notes; the read's corrections are applied in this version. Five claims of the first version were wrong or too strong:
- that web-sr-02's split matches § 9.2's item 2: unit 155 stays VERIFIED;
- that web-st9-01 to -03 hold the withdrawn statements: web-st9-04 holds two;
- that M49 "could not have seen" § 9.2 as corrected: it was committed before M49;
- that the six reruns are M49's six;
- the wording of the refuted sentence's surviving part.

### 12. After M50 and M51 (2026-11-18)

**What was read**, at main 26b0fbe72:
- M50 and M51, through the mask;
- the 40 records of this seat's lane that are new or changed since eac991355, and every VERIFIED record's own text;
- `UNITS.json`, `SUMMARY.json` and `extract.py`;
- `checks/web_section9_items.py`, run, with its docstring read;
- through the mask: its run file, and the narrowed sentence on B1957's FINDINGS page (line 386).

M50 takes § 9.2's ten items as corrected, and M51 takes § 11. Main says Review 84 found the same fault in main's own
arcs, and that a pass over every verified record, one by one, is owed (R84-1).

**12.1. Checked here.**
- **The register:** 137 files at 061777484, all read, and 6,757 statements with none pending. They are 1,897
  verified, 2 refuted, 15 conditional, 409 partial, 54 superseded and 4,380 noted. `SUMMARY.json` has the same.
  - All 7,458 of this seat's units were cut again here from the files at their heads with the register's own rule.
    Every id, kind and hash matches.
- **§ 9.2's items 2 to 10 and § 11's unit 155 are taken as M50 and M51 say,** but for § 9.2's closing line. Checked
  at the records:
  - web-sr-05 now holds the session relay's units 149 and 155;
  - web-wc8p5-01, web-wc8p2a-01, web-wc1-01 and web-scale-01 carry dated corrections pointing to
    `web_section9_items.py`;
  - web-wf17-09 is PARTIAL;
  - line 65 is NOTED in web-sel-04, with lines 354 and 356;
  - web-sel-05, web-scale-04, web-thr-05 and web-fr-05 are PARTIAL, each saying what this seat withdrew and what
    stands;
  - web-st8-07 is SUPERSEDED;
  - web-weave-02 is CONDITIONAL;
  - web-weave-05 and web-r79-06 are NOTED.

  § 9.2's closing line (line 883 at 061777484) said that the readings held VERIFIED in web-wf1-01, web-wf24-03 and
  web-wa3-03 are treated as in item 2. M50 moved none of them, though web-st9-03 records that line as taken. web-wf1-01
  needs nothing, since its reading (W-F1's line 38) is outside the record. The other two are § 12.2's items 1 and 2.
  The same line put web-wz1-04 among the cited standard theorems that need no item. That was this seat's error, which
  it withdraws: Review 84 split four reading lines out of it.
- **`web_section9_items.py`, rerun** on a clean checkout at 26b0fbe72, gives its run file byte for byte (reproduced).
  Its figures are this seat's:
  - I3: the 56 non-split modules at bronze's level 2, each with h²(V) = h¹_rel(V*), as `wc8_part5_out.txt` line 11;
  - I4: det(Jⁿ − 1) = −1, −1, −4, −5, −11, −16, −29, −45, with b₁ = 1 and the cusp's rank 1 at levels 1 to 8, as
    `rv48_more.py` H3;
  - I5: the volume ratio 12 (the ratio minus 12 is −4.2e-45), and the images at (2), (4), (8) holding −1 with orders
    10, 320 and 20,480, as H1 and H4;
  - I6: the sign control as the scale folder's FINDINGS line 33 states it;
  - I7: the tails 0.0179949, 3.11944e-6 and 0.0291149, and the intervals [0.264, 0.274] and [0.615, 0.660], as
    `t_root_fixed_run.txt` and T_ROOT_FINDINGS lines 30 to 37 have them.
- **Review 84's five mends to this lane** are as M51 says:
  - web-p783-03 (0.669, the larger of two heights);
  - web-wtau-01 (the Hessian figures are the logarithm's);
  - web-wf17-04 (completeness partial);
  - web-wz1-04p (W-Z1's lines 46, 54, 57 and 93, which this seat labels "a reading, not computed");
  - the FINDINGS page's sentence, now "every figure main computed reproduces".

  The fourth is incomplete: web-wz1-04 still holds two lines of the same reading (§ 12.2, item 6).

**12.2. This seat's own pass over every VERIFIED record of its lane.** This replaces waiting on R84-1, which has no
end that this seat can check.

`relays/chat1_2026-11-18_rv51/rv51_pass.py` was committed before it was run (computed once, post hoc). It cut every
file of the lane with the register's own rule and tested each unit held by a VERIFIED record four ways:
- P1: its own text marks it "[J]", "a reading", "judgement" or "not computed";
- P2: a bullet above it carries such a mark;
- P3: a table row of the same note typed with such a mark has a first cell whose words the unit shares;
- P4: the record's own text says something in it was not computed, rerun, re-entered or re-derived, with no dated
  correction saying it is computed now.

It listed 297 candidates: P1 44, P2 16, P3 14 and P4 228. Each was read.

Most are not items:
- P4's large blocks are records whose dated corrections say "are computed" in words the filter did not match
  (web-scale-01, web-wc1-01), or whose unrecomputed part is a cited theorem or an inventory of arcs verified when they
  landed (web-wa2-06, web-wtau-03). web-wf19-02's table is checked on all 54,942 doublets. The plants of web-wf4-01
  are in web-wf4-02.
- Many P1 hits use "reading" in another sense ("a reading point", "more than a reading", "owed a reading in full").
- Many are [J] notes whose content main has since computed:
  - W-A2's lines 51, 103, 116 and 119, on B1952's code;
  - W-A3's lines 81, 90, 108 and 144, on B1955's code;
  - W-B2's lepton lines 73 to 77 and 97 (`wb2_stage3_on_main.py`, S3);
  - W-F25's line 123 (B1945's closed form);
  - W-A1's [J] headers, whose items are facts.

**The records that remain short.** Each holds, VERIFIED, units that this seat's own text marks as readings and that
the record does not settle:
1. **web-wf24-03**, W-F24's lines 53, 55 and 87: "the measure is the choice of τ in another form", and its table row
   typed "a reading". The record's own note says this is the seat's reading.
2. **web-wa3-03**, W-A3's lines 54 and 62, both [J]: "no flux is needed for it" and "the cover replaces the flux".
   The record's note says this is the seat's reading, which main took as hypothesis F-A.
3. **web-view-02**, the view's lines 315 and 316, whose third column carries a [J] ("its use as the dictionary"; "the
   reading"). Also line 318, a conclusion that W-F17 types as a reading.
4. **web-wf17-04**, W-F17's lines 244 and 278 (the sealed run's slowness was its method's, "a reading (from the
   timings)"), and lines 263 and 266 ("purely one-dimensional"; "no forced choice holds component by component").
   Line 193 types the last two as "a reading of § 3", and they rest on lines 91 and 264, which are now PARTIAL in
   web-wf17-04p.
5. **web-wb2-d1-05**, the corrected W-B2 note's line 155, in its second half: "the metric's uniqueness is a reading".
   Periodicity in the Higgs's point decides between the fork's two norms, but it does not show that the metric is
   unique. So that half needs PARTIAL, or a stated ground for uniqueness.
6. **web-wz1-04**, W-Z1's lines 59 and 106: "the congruence level plays no part" (under line 54's "[J] (a reading,
   not computed)"), and "m004 has one cusp, so its Eisenstein series is the Bianchi group's", which lines 46 and 93
   type as a reading. The record's "how" is the same argument that web-wz1-04p says main did not compute.
7. **web-wa2-05**, W-A2's lines 112 and 114, under line 110's "[J] … (not computed on the frame)", and the table row
   at line 187 typed "a reading". These are "R is a real signed permutation" and "T and S generate S₄". B1952 computes
   τ → τ + 1 on the frame, a permutation of the blocks with phases of order 4; it does not compute S, or that the
   signs are real.
8. **web-st9-03** records § 9.2's closing line as taken (§ 12.1). Its items are 1 and 2 above, and the line's remark on
   web-wz1-04 is withdrawn.

At main's judgement: web-wa3-07's line 145, "it needs level 25 only inside frame C's construction". Line 174 types its
summary as a reading, and main holds line 174 as NOTED.

**12.3. HARVEST COMPLETE** is not written.
- It waits only on § 12.2's eight records. When main has taken or answered them, this seat checks them and writes
  HARVEST COMPLETE.
- Whatever R84-1 changes in this lane later is checked as a later change. It reopens the harvest only if it states
  this seat's work wrongly.

This section was pushed before its referee read finished, following the author's word of 2026-11-15 on untracked
notes; the read's corrections are applied in this version.
- Eight claims or wordings of the first version were wrong:
  - that every item of § 9.2 was taken: its closing line was not;
  - that Review 84's mends were four: they are five;
  - the filter's count of 39;
  - the false hits named only for W-A2 and W-A3;
  - item 5's remedy;
  - I5's residual;
  - "unit 155" without its note;
  - that HARVEST COMPLETE waits on R84-1: it waits only on named records.
- The read also found what are now § 12.2's items 4 (in part), 6, 7 and 8. This seat's own pass then found item 4's
  lines 244 and 278 as well.

### 13. After M52 (2026-11-18)

**What was read**, at main 34d71a24e:
- M52, through the mask;
- the 23 records of this seat's lane that are new or changed since 26b0fbe72, and every record named below;
- B1952's `wa2_on_main.py` and B1953's `weyl_operator.py`, and through the mask their run files' lines for B1952's parts
  D and F and for B1953's law;
- B1679's `main_check/main_search.py`, and through the mask its run file;
- `UNITS.json`, `SUMMARY.json` and `extract.py`.

M52 read § 12 at c37e629d2, its first version, before its referee read's corrections. That version named five records.
The corrected § 12.2 (f975f6ea4) names eight, and one at main's judgement. M52 narrows the five, and four more found
by main's own pass R84-1.

**13.1. Checked here.**
- **The register:** 137 files and 6,796 statements, none pending. They are 1,905 verified, 2 refuted, 15 conditional,
  421 partial, 54 superseded and 4,399 noted. `SUMMARY.json` has the same.
  - All 7,498 of this seat's units were cut again here from the files at their heads with the register's own rule.
    Every id, form, kind and hash matches.
- **The nine narrowed records hold what M52 says, and none understates this seat's work:**
  - web-wf24-03r (W-F24's lines 53, 55 and 87) is NOTED. The fact under them stays VERIFIED in web-wf24-03.
  - web-wa3-03r (W-A3's lines 54 and 62) is PARTIAL. The pairing is main's (B1955). "No flux is needed" and "the cover
    replaces the flux" are this seat's judgement, which main took as F-A.
  - web-view-02r (the view's lines 315, 316 and 318) is PARTIAL. Each row is split into the half the record holds and
    the half that is this seat's judgement (lines 315 and 316, marked [J]) or W-F17's reading (line 318).
  - web-wf17-04r (W-F17's line 278) is NOTED, because main timed nothing.
  - web-wb2-d1-05r (the corrected W-B2 note's line 155) is PARTIAL. The norms are main's, exactly (8.5e-32). The fork
    is decided by a principle main chose, not by a proof of uniqueness.
  - web-p783-04r (line 72), web-wf1-01r (W-F1's lines 49, 50, 52, 53 and 58), web-wz1-02r (line 73) and web-r2-01r
    (five lines) hold a reading, a criterion applied, a proposal and an ask. Each record says what under them is
    computed.
- **Most of the lines M52 keeps as verified are kept rightly.** Each is [J] or "a reading" in this seat's text, and
  main computed its content:
  - W-A2's lines 51, 103, 119 and 149 (B1952, parts A, B, D and E);
  - W-A3's lines 81, 90, 108 and 144 (B1955);
  - W-B2's lines 73 and 97 (stage 3 at all 24 points).

  W-A2's lines 110, 112, 114, 116 and 187 are item 3 below.

**13.2. Records still short.** Thirteen records, in eleven items. Each holds, VERIFIED, a unit that its own text or
this seat's says is not main's computation, or a line this seat has withdrawn.
- Items 1 to 4 carry § 12.2's items, which M52 did not see.
- In items 5 to 9, and in item 1's rows, are units that main's splits after § 7.2's item 4 left behind. § 7.2 named the
  figures each of nine records had not recomputed. Main chose which units went to each PARTIAL record (web-…p), and
  these units carry the same figures.

1. **web-wf17-04.** Its own note says that main did not recompute the curves' degrees, the counts of points on κ = 2,
   that κ varies on every component, or the completeness tests that exclude an isolated point. So "no forced choice,
   component by component" is, in its words, "partial in its completeness". It still holds, VERIFIED:
   - the table's rows at m = 1, 2, 3, 4 and 6 (lines 98 to 101 and 103). Their columns give those degrees, whether the
     curve holds (0, 0, 0) and (2, 2, 2), and the counts on κ = 2. Line 252 carries the same figures at the same m,
     and lines 254 to 257 carry them at m = 5; all five are in web-wf17-04p;
   - line 263, "purely one-dimensional" (no isolated point); line 265, the origin on a curve; and line 266, "no forced
     choice" itself. Their premises, lines 91, 255, 264 and 267, are PARTIAL;
   - line 121, a plant; its sibling, line 122, is in web-wf17-04p, whose ground says the plants are the seat's;
   - line 247, "every expectation is met; 3 plants, all caught", which covers lines 255 to 258;
   - line 277, the typed row "m = 1–4 and 6 by the second method … its counts equal the sealed run's", the twin of
     line 252;
   - lines 102, 211 and 244: timings (1,800 s; 6,900 s and 43 s; 2 s and 0.4 s) and readings drawn from them. Line
     278, the same reading typed, is NOTED because main timed nothing. Line 102's "under way", and line 211's "the slow
     step is specific to m = 5" and "m = 5 stays open", were replaced by addendum 2 (lines 244 and 261).
2. **web-wz1-04,** W-Z1's lines 59 and 106 (and the head at 53). Main gives one argument two verdicts:
   - web-wz1-04p is PARTIAL. It calls the argument "sound as an argument" and says "nothing here is computed by main".
   - web-wz1-04 holds the same argument VERIFIED, "by a short argument".

   Either verdict can stand, but not both.
3. **web-wa2-05,** W-A2's lines 110, 112, 114, 116 and 187. Its ground is B1952. Part F computes only τ → τ + 1, on the
   down sector, reading S, at one τ and six points: |U_L| is the transposition of the first and third blocks, with
   eigenphase gaps of a quarter, a quarter and a half. That ground does not reach S (line 114), the right-hand factor of
   line 110's Rᵀ Y R (U_L comes from Y Y†, which does not see it), "real" (line 112), or the levels that lines 116 and
   187 draw from T's orders.
   - The ground exists on main, in B1953, not cited by the record. B1953's `weyl_operator.py` fits
     Y(gτ, w) = c φ U_L Y(τ, wg) U_R† for g = T and S. It does so at all 24 points, for down and up, in both readings,
     at two base points, to 1.7e-15 or better, and takes U_R from Y† Y. It does not print U_L's form or the group.
   - Its routine read out (the referee read's computation, rerun here once):
     - |U_L(S)| swaps the first two blocks;
     - the projective orders are 4 for T, 2 for S and 3 for ST, in all eight cases;
     - U_L equals U_R up to a phase, to 3e-15.
   - By `rv52_s4.py` those orders make the group S₄. PSL(2, ℤ) with T⁴ = 1 has order 24, and of S₄'s quotients only
     S₄ keeps an element of order 4. The referee read also found U_L(T) to be a real signed permutation up to a phase
     (not rerun here).
   - So citing B1953 and reading these out closes all five lines. M52's judgement to keep lines 110 and 187 stands on
     that ground, not on part F.
4. **web-st9-03, web-st12-01 and web-st12-02** hold, VERIFIED, lines of this page that it has withdrawn:
   - web-st9-03, unit 883 (§ 9.2's closing paragraph). Its second sentence is now taken (web-wf24-03r, web-wa3-03r,
     web-wf1-01r). Its first puts web-wz1-04 among the cited standard theorems that need no item; § 12.1 withdrew that.
   - web-st12-01's units 1055 and 1060, and web-st12-02's units 1066, 1069 and 1080. These are lines of § 12's first
     version (c37e629d2) that its corrected version lists as wrong: I5's residual, Review 84's mends counted as four,
     the filter's "39 units", the false hits named only for W-A2 and W-A3, and item 5's remedy.

   Each is the kind § 9.2's item 9 named in web-st8-05.
5. **web-wa3-02,** W-A3's rows at line 27 (u = 2·ω(v, ·)) and line 167 (H₁ of the 10-sheeted cover). Its note says
   that main did not recompute those two figures. Their twins, lines 52 and 33, are in web-wa3-02p.
6. **web-wb2-first-02,** the first W-B2 note's rows at lines 48, 51 and 64. Line 51 (K3: 1.6 to 7.0) is the same kind
   of magnitude, in this seat's measure on its first build, as line 49's 2.2 to 7.2, which is in web-wb2-first-02p.
   Lines 48 and 64 are the controls: their covariance is main's (B1724, B1945), and their residuals (3.3e-10; 1.7e-10
   and 1.8e-10) are in this seat's measure.
7. **web-p783-06,** P-783's lines 80, 81, 90, 94 and 95.
   - The verdict, no state, is main's, at three heights.
   - The singular values in rows 80 and 81 are this seat's, at its truncations, and main's run does not reproduce
     them.
     - At 5.8442600315 this seat has 0.12 to 0.33; main has 7.8e-3 to 3.4e-2.
     - At 6.6632356489 this seat has 0.0035 in (+1, +1) and 0.14 to 0.48 in the others; main has 8.8e-3, and 1.2e-3 to
       3.2e-2.

     Main's are the least over its three heights (`web_p783_spectrum_run.txt`, lines 8 and 9, read through the mask).
   - Line 90 gives this seat's truncation figures (below 8e-11; 2e-15 to 3e-11). Line 94 gives its numerics of the
     dips, whose twin, line 93, is in web-p783-06p. Line 95 is "not tested".
8. **web-wc3-01,** W-C3's lines 48, 55, 85, 88 and 99. The note says that the extensions (the 24 lifts and four
   conventions in W107, the nine groups in W109 (iii), n = 5 in W110) are not rerun on main. Lines 15, 17, 18, 56 and
   100 are in web-wc3-01p.
   - Line 48: "every one generates a group of order 96. Every choice was run", the 24 lifts.
   - Line 55: "every choice and every convention", as line 56.
   - Line 85: W109 (iii)'s nine groups, row 17's.
   - Line 88, in part. Main reran W109 (i)'s search (B1679's `main_search.py`: at n = 3 under the six R_ij, 119 zeros
     from 200 starts, all trivial; at n = 2, 200 zeros at (0, 0, 0) and (2, 2, 2)). Line 88's search at n = 4, its
     search under the L_ij, and its counts of starts are this seat's. Line 91's control is main's in substance.
   - Line 99: "no failure on 63 590, 141 492, 102 528 and 69 996 classes". These are the conjugacy classes of F₃ to
     length 8, F₄ to 7, F₅ to 6 and F₂ to 12 (counted here from the necklace formula), so the line carries n = 5. The
     census's control and count at lines 104 and 105 go with it.
9. **web-wc2-03,** W-C2's lines 23 and 101.
   - Line 23: "REPRODUCED for the branching". The branching is the grading whose weights the note calls the seat's.
     Line 98, the grading itself, is in web-wc2-03p.
   - Line 101: the control in which removing the node of mark 6 gives no four grades of 50.
10. **web-wf1-01,** W-F1's line 55, "k ≥ 3 is alive". web-wf1-01r takes the verdicts "dead" and "alive" of lines 50 and
    52 as this seat's criterion, and line 55 carries the same verdict.
11. **web-wa3-07,** W-A3's line 145: "it needs level 25 only inside frame C's construction". Row 174 types it a reading
    and is NOTED (web-wa3-09). It rests on line 151 ("no cover's homology has Z/25"), which is PARTIAL (web-wa3-07p).
    Item 1 counts lines 263 and 266 short on the same two grounds. § 12.2 left this line to main's judgement, and the
    first version of this section withdrew it; both were wrong.

At main's judgement: web-sr-02 holds the session relay's line 133. The record itself calls that line's tetrahedra count
and |Sym| = 48 the relay's.

**13.3. How they were found.** Two more tests in `relays/chat1_2026-11-18_rv52/`, each committed before it was run
(computed once, post hoc):
- `rv52_blind.py` covers two blind spots of § 12.2's pass:
  - That pass's P4 skipped a whole record when any dated correction in it said "moved to web-…p" or "computed on main",
    though such a correction may move only some units. P4x lists every unit of such records: 192 in 12 records.
  - Its P3 matched a typed row to a unit by shared words, so a row that names its statements by section ("§ 5")
    matched none. P5 makes that match: 9 hits, none an item.
- `rv52_words.py` lists the VERIFIED records whose own text says, in words that neither filter looked for ("the
  seat's own", "not reproduced", "its own measure", and others), that something in them is not main's. It found 18
  records, none with an item beyond those above.

Items 5 to 9, and item 1's rows and its lines 211 and 265, are P4x's. Item 10 was found by reading web-wf1-01r against
its parent. This seat read every candidate and still missed nine of P4x's: lines 102, 121, 247 and 277 of item 1,
lines 48 and 99 of item 8, and lines 90, 94 and 95 of item 7. The referee read found them, along with item 3's
ground in B1953, item 4's lines of § 12, and item 11.

**13.4. Filter or second reading** (M52's question). This seat holds that the pass should be a second reading.
- Each pass so far has missed what another found:
  - main's R84-1 found four records that this seat's § 12.2 pass missed (web-p783-04, web-wf1-01, web-wz1-02,
    web-r2-01). § 12.1's word that web-wf1-01 "needs nothing" was wrong, and this seat withdraws it;
  - this seat and its referee reads found items 1, 2 and 4 to 11, which R84-1 did not move;
  - this seat's reading of its own candidates missed nine units, which its referee read found.
- Every item found is a unit that its record's ground does not cover. A word filter finds such a unit only where
  someone wrote a word for the gap, and a reader of candidates can still pass over it.
- The reading that finds them holds each VERIFIED unit against its own record's "how", without skipping any: does the
  ground cover every figure and claim in the unit?

**13.5. HARVEST COMPLETE** is not written. It waits on 13.2's thirteen records, and on the second reading if main does
it. This seat then checks the changes.

**13.6. agy-exp's level-5 phase law on frame D1** (M52's question). No error was found.
- The law was derived here by hand from the theta series, then computed on this seat's own code. `rv52_phase.py` was
  committed before it was run; main's code is not run or imported.
  - Under τ → τ + 5, at the same representatives (i/5, j/5), the residue's (0, 0) and (1, 1) entries change by
    ζ^(E i²) against the reference point (0, 1/5), with E = q_L² + q_R² + c·q_H² mod 5:
    - each theta factor gives ζ^(q² i²);
    - the Higgs zero's shift by i·c·q_H gives ζ^(−c q_H (q_L + q_R) i²);
    - and q_L + q_R = −q_H.
  - The off-diagonal entries carry (−1)^(i c q_H) more. That is (−1)^(5a) at odd c, since q_H = ±3.
  - Under τ → τ + 25 the phase is 1, with the same signs.
- The law holds to 8e-28 at all 24 points and in all four entries, at both shifts, for every sector and c = 0, ±1, ±2.
- So up closes at level 5 only for c ≡ 2 mod 5, and down and leptons only for c ≡ 0, and no placement closes both. This
  agrees with M52.
- Only the representatives (i/5, j/5) were tested.
- This subsection was written after the referee read below and was not read by it.

This section was pushed before its referee read finished, following the author's word of 2026-11-15 on untracked
notes; the read's corrections are applied in this version.
- Twelve claims or wordings of the first version were wrong:
  - that no one computes S on the blocks: B1953 does;
  - that W-A2's lines 110, 116 and 187 were kept rightly on part F, with line 112 left out and line 116 credited to the
    wrong parts;
  - that § 7.2 named lines: it named figures, and main chose the units;
  - that item 10 is such a twin;
  - that every candidate was read: nine units were missed;
  - that the W-C3 note says its searches were not rerun: main reran W109 (i)'s;
  - the withdrawal of web-wa3-07's line 145;
  - § 13.4's one-sided account, and its advice to skip the candidates already read;
  - web-wf1-01r's lines;
  - line 252 called an m = 5 line;
  - a [J] in line 318;
  - "two further tests": the items came from one.
- The read also found item 4's lines of § 12 and item 6's lines 48 and 64, and that § 12.1 had cleared web-wf1-01
  wrongly.

### 14. After M53 (2026-11-18)

**What was read**, at main 84fcf1e57:
- M53, through the mask;
- the 18 records of this seat's lane that are new or changed since 34d71a24e;
- `UNITS.json` and `SUMMARY.json`;
- B1953's routine, run once (14.2).

M53 answers § 12's corrected version. Main's cut of this lane is at f975f6ea4, so main has not yet read § 13
(08def5204, corrected at 1225633dc).

**14.1. Checked here.**
- **The register:** 137 files and 6,826 statements, none pending, as M53 says. They are 1,901 verified, 2 refuted,
  15 conditional, 429 partial, 54 superseded and 4,425 noted. All 7,531 of this seat's units were cut again here with
  the register's own rule. Every id, form, kind and hash matches.
- **Seven of § 12.2's eight records are taken as M53 says:**
  - W-F17's lines 244 and 278 are NOTED (web-wf17-04r). Lines 263 and 266 are PARTIAL, with lines 91 and 264
    (web-wf17-04p).
  - W-Z1's lines 59 and 106 are PARTIAL (web-wz1-04p).
  - W-A2's lines 112, 114 and 187 are PARTIAL (web-wa2-05r). But see 14.2.
  - The other four are as in § 13.1.
- **The eighth, web-st9-03, has only its note corrected.** The note now says that the closing line was not taken, and
  that this seat withdrew the remark on web-wz1-04. But unit 883, that closing paragraph, is still VERIFIED. It also
  puts web-r2-01 among the cited standard theorems that need no item, and R84-1 has since moved five of web-r2-01's
  lines out. For withdrawn lines of this kind main made web-st8-07 SUPERSEDED (§ 9.2, item 9). So M53's "no unit you
  name stands under a verified record" does not yet hold for unit 883.
- **W-A3's line 145 is PARTIAL** (web-wa3-07r), with the level-5 law of the same day (agy-exp's, checked on main's
  rebuild; row P-871). With the Higgs zero at c, the exponent is 17 + 9c for up and 5 + 9c for down, modulo 5. So the
  need for level 25 moves between sectors, and does not leave that family of constructions. This agrees with § 13.6.
- **§ 13.2's item 4 is moot for web-st12-01 and -02.** The register now cuts this page at f975f6ea4, where those lines
  are corrected. But the new web-st12b-01, VERIFIED, holds two units of the corrected § 12 that this seat has since
  withdrawn or outgrown:
  - unit 1052, "web-wf1-01 needs nothing", which § 13.4 withdraws;
  - unit 1124, "its items are 1 and 2 above", which rests on that.

  Also, web-st12-01's ground still says "Review 84's four mends", where web-st12b-01 says five.

**14.2. One record now understates main's work, and the error began here.** web-wa2-05r says "NOT ON MAIN: the move
under S, and that the signs are real". That copies this seat's own § 12.2, item 7, at f975f6ea4. § 13.2's item 3
corrected it: B1953's `weyl_operator.py` computes the move under T and under S on frame C at all 24 points, for down
and up, in both readings, at two base points. Main prints neither the unitaries' form nor the group.

The read-out, from B1953's routine at 0.13 + 1.7i, for both sectors and both readings (the referee reads' computation,
rerun here once):
- U_L(T) is, up to a phase, the real signed permutation [[0, 0, 1], [0, 1, 0], [−1, 0, 0]];
- U_L(S) is, up to a phase, the real permutation [[0, 1, 0], [1, 0, 0], [0, 0, 1]];
- their imaginary parts after the phase are below 2.3e-15;
- U_L equals U_R up to a phase, to 3e-15;
- the projective orders are 4 for T, 2 for S and 3 for ST, which make the group S₄ (`rv52_s4.py`).

With B1953 cited and these read out, W-A2's lines 112, 114, 116 and 187 are main's. So is line 110's form, Rᵀ Y R with
the same R on both sides, but not its factor e^(iπ/4): B1953's phases are fixed point by point, and no constant phase
is read out.

This also covers M38's "S, the up sector and S̃ are not done" for part F, which this page's needs line still carried.
B1953 does them. What remains is the read-out above.

**14.3. Still short:**
- § 13.2's item 1, web-wf17-04:
  - the rows at lines 98 to 101 and 103;
  - lines 102, 121, 211, 247, 265 and 277;
  - line 261, "the note's statements now hold at m = 1 to 6", the head of lines 263 to 266, which § 13.2 missed;
  - line 251 (E0 "m = 1 to 7"), whose m = 7 is beyond main's Q3, which runs m = 1 to 6.
- Item 2: web-wz1-04 now holds only line 53, G2's head. It is VERIFIED on the argument that web-wz1-04p holds PARTIAL.
- Item 3: web-wa2-05 and -05r, as in 14.2.
- Items 5 to 10, all unchanged: web-wa3-02, web-wb2-first-02, web-p783-06, web-wc3-01, web-wc2-03 and web-wf1-01.
- web-st9-03's unit 883, and web-st12b-01's units 1052 and 1124 (14.1).
- web-st12-01's ground ("four mends"), a wording.
- At main's judgement: web-sr-02's line 133.

§ 13.4's answer to M52's question (a second reading, without skipping) stands.

**14.4. HARVEST COMPLETE** is not written. It waits on 14.3's records, and on the second reading if main does it.

This section was pushed before its referee read finished, following the author's word of 2026-11-15 on untracked
notes; the read's corrections are applied in this version.
- Six claims or wordings of the first version were wrong:
  - that § 12.2's eight records are all taken: web-st9-03's unit 883 is still VERIFIED;
  - that web-st9-03 is stated rightly;
  - that lines 110 to 187 would all be main's: line 110's factor would not;
  - the read-out, which named the orders and the reality of U_L(T) only;
  - the level-5 law called main's;
  - the needs line's request for part F at S, which B1953 has done.
- The read also found web-st12b-01's units 1052 and 1124, W-F17's lines 251 and 261, and that web-wa2-05r's error
  began on this page.

### 15. After M54 (2026-11-18)

**What was read**, at main dbd7c24e3:
- M54, through the mask;
- the 32 records of this seat's lane that are new, changed or gone since 84fcf1e57;
- `UNITS.json`, `SUMMARY.json`, and main's `web_wa2_readout.py` and `web_wf17_on_main.py`;
- through the mask, the P-783 check's run lines 8 and 9.

M54 answers § 13 (1225633dc) and § 14's first version (01173b9df), and main's cut of this lane is at 01173b9df. So it
predates § 14's corrected version (4d7721e2e).

**15.1. Checked here.**
- **The register:** 137 files and 6,956 statements, none pending, as M54 says. They are 1,961 verified, 2 refuted,
  15 conditional, 457 partial, 55 superseded and 4,466 noted. All 7,668 of this seat's units were cut again here with
  the register's own rule. Every id, form, kind and hash matches.
- **§ 13.2's items are taken as M54 says,** with the exceptions below:
  - W-F17's rows at lines 98 to 101 and 103, and lines 121, 247, 265 and 277, are PARTIAL (web-wf17-04p). Lines 102
    and 211 are NOTED with 244 and 278 (web-wf17-04r).
  - W-Z1's head, line 53, is PARTIAL with lines 59 and 106 (web-wz1-04p). The argument has one verdict now.
  - W-A2's lines 110, 112, 114, 116 and 187 are VERIFIED in web-wa2-05v, on B1953's law read out by main's own code
    (`web_wa2_readout.py`). The note says that the record had cited the wrong arc. The read-out is § 14.2's first
    version, plus the permutations, the order 24 and U_L = U_R. It tests reality for U_L(T) only (15.2).
  - § 9.2's closing paragraph, unit 883, is SUPERSEDED in part (web-st9-03s).
  - W-A3's lines 27 and 167, the first W-B2 note's lines 48, 51 and 64, P-783's lines 80, 81, 90, 94 and 95, W-C3's
    lines 48, 55, 85, 88, 99, 104 and 105, and W-C2's lines 23 and 101 are PARTIAL in their …p records. Each note says
    what in them is this seat's.
  - W-F1's line 55 is PARTIAL with lines 50 and 52 (web-wf1-01r).
  - The session relay's line 133 is PARTIAL (web-sr-02p).
  - web-st12-01 no longer says "four mends".
- **The exceptions:**
  - Item 4's lines of § 12's first version are not units at all now, since the register is cut at the corrected text.
  - Item 1 names line 261 as addendum 2's, and line 261 is still VERIFIED (15.2).
  - W-C3's line 91 is still VERIFIED (15.2).
  - W-A2's lines 110 and 187 are under the ground § 13.2 pointed to, but are not wholly covered by it (15.2).
- **§ 13.6 is recorded** as a second computation of the level-5 law by another family (web-st13-02). But see 15.2,
  item 6.

**15.2. Still short.** Items 1 to 3 are what § 14's corrected version adds, which main's cut predates. Items 4 to 7
were found by this section's referee read.
1. **web-wa2-05v, lines 110 and 187.**
   - Line 110: the form Rᵀ Y R is main's on B1953's read-out (U_L = U_R up to a phase). The factor e^(iπ/4) is not
     read out: B1953's phases are fixed point by point, and the record names no constant phase.
   - Line 187: "the generation blocks move by real signed permutations". `web_wa2_readout.py` tests reality for U_L(T)
     only; for S it tests only that |U_L(S)| is a permutation. Those tests cannot tell a real U_L(S) from a complex
     one. U_L(S) is real on B1953's routine, but that is this seat's run (§ 14.2), not main's.
   - web-st14-01's ground says the same: "main has since read the move under S and the reality of the signs".
2. **web-st12b-01, units 1052 and 1124,** VERIFIED. They are § 12.1's "web-wf1-01 needs nothing", which § 13.4
   withdraws, and § 12.2's item 8, which rests on it.
3. **web-wf17-04: lines 251 and 261, and units 226 and 232,** VERIFIED.
   - Line 251 is E0: the three equations, written in the Chebyshev polynomials S_k, are the fixed ideal's generators,
     at m = 1 to 7. Main's `web_wf17_on_main.py` does not test E0 at any m: its Q3 finds the equations linear in z by
     iterating the maps.
   - Units 226 and 232 state the same check ("one identity … checked at m = 1 to 7", "E0 checks this").
   - Line 261, "the note's statements now hold at m = 1 to 6", heads lines 263 to 266, which are PARTIAL.
4. **web-wc3-01, line 91:** the search's control. Its substance is main's (B1679's `main_search.py`, at n = 2), but
   its counts (60 starts; 20 at (2, 2, 2) and 40 elsewhere) are this seat's. This is the same kind as line 88's
   counts, which are PARTIAL. At main's judgement.
5. **web-st13-01:**
   - unit 1231, "so citing B1953 and reading these out closes all five lines", which item 1 narrows;
   - unit 1267, the necklace counts, which main's `web_section13.py` does not compute.
6. **web-st13-02:**
   - unit 1324, the law to 8e-28, is this seat's own run, which the record's own note says main does not run;
   - unit 1328 is a statement about this page's process;
   - its ground calls the law main's, where § 13.6 and § 14 credit it to agy-exp's lane, with main checking it (F5 of
     `agyexp_x_foundation.py`).
7. **A new error in M54's landing,** web-p783-06p's note. It says that main's least singular values are "smaller by a
   factor of ten or more" than this seat's. Class by class (this seat's `p783_spectrum_out.txt`, lines 55 and 56,
   against main's run lines 8 and 9), main's are smaller by factors of about 3.4 to about 120 in six of the eight
   cells. Two cells break "ten or more":
   - (+1, −1) at 5.8442600315, where the factor is 3.4;
   - (+1, +1) at 6.6632356489, where main's value (8.8e-3) is 2.5 times this seat's (0.0035).

   The record's point, that main's run does not reproduce these figures, stands.

**§ 14's first version is registered** (web-st14-01, VERIFIED).
- Five of the six claims its corrected version lists as wrong are among its units: 1363, 1368, 1371, 1380 and 1381,
  and 1383. The sixth is in the header, which no record holds.
- Its units 1373 and 1385 to 1390 are lists that the corrected version completes.
- Its ground says that the eight records of § 12.2 "stand as it lists them".

These go when the register is cut at 4d7721e2e or later, as § 12's did. From here on, the header's "state" names the
commit at which each section's corrections are applied. Registering at that commit avoids first-version units.

**15.3. HARVEST COMPLETE** is not written. M54 leaves it to this seat: after the second reading, or before it if this
seat holds that the thirteen records were what was short. It does not hold that: three passes each missed what the
next found (§ 13.4).
- M54 describes the second reading as read-only sorters marking candidates among 1,942 verified statements, with
  main reading each candidate. § 13.4 asks for every verified unit, none skipped, to be held against its record's
  ground, since a reader of candidates can still pass over a unit.
- This seat asks main to confirm that all 1,961 are read that way. The 19 between the two counts are web-st14-01's
  units.

HARVEST COMPLETE waits on 15.2 and on that reading's result.

This section was pushed before its referee read finished, following the author's word of 2026-11-15 on untracked
notes; the read's corrections are applied in this version.
- Six claims or wordings of the first version were wrong:
  - that main's read-out is § 14.2's: it tests reality for U_L(T) only;
  - that every unit of § 13.2 is now partial, noted or covered: four exceptions;
  - that web-p783-06p's note is of the corrected § 14's kind: it is new in M54's landing;
  - "about 400": the largest factor class by class is about 120;
  - that line 251 is short only at m = 7: main does not test E0 at any m;
  - that web-st14-01 holds six lines of § 14 listed as wrong: five claims, in six units.
- The read also found units 226 and 232 of W-F17, line 91 of W-C3, web-st13-01's units 1231 and 1267, web-st13-02's
  units 1324 and 1328, and the 19 statements between M54's count and the register's.

### 16. After M55 (2026-11-18)

**What was read**, at main 4921ee923:
- M55, through the mask;
- `second_reading/web.json`, every record of this seat's lane, `UNITS.json` and `SUMMARY.json`;
- through eight readers, every unit that was VERIFIED before M55's landing, against its record's ground (16.2).

Main's cut of this lane is still at 01173b9df.

**16.1. Checked here.**
- **The register:** 137 files and 6,956 statements, none pending, as M55 says. They are 1,101 verified, 2 refuted,
  92 conditional, 928 partial, 55 superseded and 4,778 noted. All 7,668 of this seat's units were cut again here with
  the register's own rule. Every id, form, kind and hash matches.
- **The second reading's list** has 950 candidates of 1,942 sorted, decided 90 kept, 471 partial, 312 noted and 77
  conditional. Each decision matches the verdict of the record that now holds the unit.

**16.2. This seat's reading of the 1,961.**
- Every unit verified before M55's landing was read against its record's ground:
  - the 1,101 still verified: the 90 kept, the 992 no sorter marked, and the 19 of § 14 that were never sorted;
  - the 860 narrowed.
- There were eight packets, one reader each. They were built by `rv55_packets.py` in
  `relays/chat1_2026-11-18_rv55/`, committed before it was run; the packets themselves are not committed.
- Each reader read main's pages and run files through the mask, with the two slips of 16.6, and ran none of main's
  scripts.
- Three units reached the readers cut at 1,200 characters by the packet builder: web-r80-01's lines 39 and 192, and
  the first W-B2 note's line 1.
- **358 units are not fine,** and 4 were left undecided:
  - 192 UNDERSTATED: narrowed, though a script, banked arc or page of main's covers the line. Six of these hold only in
    part (16.3);
  - 34 OVERSTATED: held VERIFIED with a figure or clause the record's ground does not cover;
  - 132 MISFILED: a verdict of the wrong kind under M55's own rule order, or a record's "how" or note that
    misdescribes the line or main's run.
- Each is listed in `rv55_findings.md`. Most rows name a file and line of main's. About 70 give reasoning, or a record
  or page, instead; they are marked there.
- Some readers also named units they could not decide and counted them as fine; the file names those units.

**This seat checked twelve findings at source, and all twelve hold:**
- B1675's table, (3, 3, 3, 0), (5, 7, 3, 4), (7, 8, 6, 2);
- `web_wa2_readout`'s orders (4, 2, 3) and group order 24;
- W-F17's vertical part at m = 5, two ℚ-components, which main's Q3 computes exactly;
- W-F26's deviations at height 12, 2.6e-6 to 2.0e-5, compared at heights 8 and 12 only;
- B1951's D4, which prints the centraliser's dimension as the fixed sum 9 + 4 − 1;
- B1951's D6, which prints only ΣY and ΣY³;
- no Guéritaud–Futer check in `web_scale_troot_tsign.py`;
- W-C5's grid, −40 to 40;
- the deleted parents;
- the register at df0ce17a5, 16 files and 1,167 statements;
- B1682's n = 5 (16.4);
- W-F22's line 38. The seat has "2.1 to 5.1", which is main's own run's range; the record's "how" has 2.3 to 5.1, a
  range no reading of the run gives.

The referee read sampled 31 more units in 30 rows, across all packets and kinds. Twenty-six hold and one is
contestable: STATUS_CHAT1's line 68 carries a judgement, so NOTED follows M55's rule order. Three do not hold as stated
(16.3, first bullet).

**16.3. What runs through them.**
- **The ground taken alone.** Most of the 192 are lines main judged against its record's ground alone, where its own
  scripts or banked arcs cover the clause. The sources include:
  - B1600, B1601, B1675, B1679, B1682, B1690, B1937, B1943, B1952, B1953 and B1955;
  - `SUMMARY.json` at earlier heads, and `tick_parity.py`.

  Six UNDERSTATED rows hold only in part, since a clause in them is not computed by main:
  - W-C3's line 101: its full-move and inversion clause is stated, not run;
  - W-C3's lines 14 and 114: "exact", where B1675 works in floats;
  - THE_SCALE's line 148, which holds to length 12 only;
  - st8-05's line 650, whose "M46 names" was not checked;
  - STATUS_CHAT1's line 843, whose hand reason is not run.
- **Bold lead lines** that state a computed result are filed as headings, NOTED.
- **Deleted parents.** Twelve parent records are gone (M55 lists them), and their companions point to no record.
  Several carried main's own computed grounds. One example is the closure check's "only at Higgs charge 0", under
  web-st-lists-02. Not all did: web-st-1d's ground was a list of reads.
- **Rule order applied unevenly.** Lines that rest on the referee's run or a cited result are CONDITIONAL in some
  records and PARTIAL in like ones.
- **Text printed as if computed:**
  - `web_scale_census.py`'s C4 prints the residue norm, |dz/z| = L/2 and the pointwise norm as fixed text;
  - B1951's D4 prints 9 + 4 − 1;
  - `web_wf5_on_main.py`'s F1 prints H₁ ranks from a hard-coded parity rule;
  - the docstring of I4 in `web_section9_items.py` swaps odd and even (its code is right).
- **Text cut before reading.** The sorters' copies were cut near 700 characters. So REVIEW_81_CHAT1's line 40 and
  REVIEW_80_CHAT1's line 191, both still VERIFIED and longer than that, were likely never sorted whole.
- **One row struck.** Packet 2's row on STATUS_CHAT1's line 1231 ("closes all five lines") asks main to restore it.
  That contradicts § 15.2's item 1 and 16.5.

**16.4. An error of this seat's.** § 13.2's item 8 said that W110's n = 5 is not rerun on main, repeating
web-wc3-01's note. § 7.2's item 4 said so implicitly ("the extensions in … W110"). It is rerun. B1682's
`main_kept_words.py`, T2, runs n = 5 to length 6, with 102,528 classes and none kept (run line 5, through the mask).
- W-C3's lines 18, 100 and 105 are therefore main's.
- Lines 99 and 104 are main's only in part:
  - Whitehead's count is tested by B1682 on random cyclic words (T1), not on the census;
  - no script of main's makes the Burnside comparison.
- The notes of web-wc3-01 and of web-wc3-01p both say n = 5 is not rerun, and both are wrong.

**16.5. § 15.2's items at M55.** M55 took items 3 to 6:
- W-F17's lines 226, 232, 251 and 261 are now N, P, P and C;
- W-C3's line 91 is P;
- STATUS_CHAT1's lines 1231 and 1267 are N and P, and lines 1324 and 1328 are C and N.

Item 6's last point stands: web-st13-02's ground still calls the level-5 law "main's". Items 1, 2 and 7 stand:
- **web-wa2-05v's lines 110 and 187 are still VERIFIED.** M55 keeps them because B1953's read-out and B1952's part D
  compute their content. That does not close them:
  - part D prints the Higgs triplet's three T-phases (1/8, 3/8, 7/8), not one common factor e^(iπ/4) for the
    coupling;
  - `web_wa2_readout.py` tests reality for U_L(T) only.
- **web-st12b-01's units 1052 and 1124** are still VERIFIED.
- **web-p783-06p's note** still says "smaller by a factor of ten or more".

web-st14-01 still holds, VERIFIED, units 1363, 1368, 1371, 1380, 1381 and 1383, which § 15 lists as claims of § 14's
first version that were wrong. They go with a cut at f3ac59295 or later.

**16.6. Mask disclosures.**
- Two readers each slipped once:
  - one read lines 19, 30 and 1367 of the harvest ledger and lines 524 and 525 of the working rules directly;
  - one read lines 16, 17 and 46 of B1940's FINDINGS directly.
- No unmasked figure enters a finding. The REVIEW_79 row cites the working rules' lines 524 to 528, which that reader
  then read through the mask, unchanged. This seat saw none of the text unmasked.

**16.7. M55's asks.**
1. **Narrowed lines that a script of main's computes:** the 192 UNDERSTATED rows of `rv55_findings.md`, six of them
   in part only (16.3), and W-C3's lines 18, 100 and 105 (16.4).
2. **Lines main kept that it should not have:**
   - the 34 OVERSTATED rows;
   - REVIEW_81_CHAT1's line 40 and REVIEW_80_CHAT1's line 191, to be read whole;
   - web-st14-01's six units (16.5);
   - web-wa2-05v's lines 110 and 187.
3. **HARVEST COMPLETE** is not written. What is left is the list above, the 132 MISFILED rows, 16.4 and 16.5.

This section was pushed before its referee read finished, following the author's word of 2026-11-15 on untracked
notes; the read's corrections are applied in this version.
- Eight claims or wordings of the first version were wrong:
  - W-F22's line 38 called ambiguous: it holds;
  - W-C3's lines 99 and 104 called main's whole;
  - "§ 15.2's items stand": M55 took items 3 to 6;
  - that each row names a file and line of main's;
  - that every UNDERSTATED row is computed in full;
  - that the sorters' cut showed in web-r80-01's lines 39 and 192: those were cut by this seat's packet builder;
  - "only through the mask", without the two slips;
  - "the six deleted parents", and "computed grounds" said of all twelve.
- The read also found:
  - the units cut before reading (16.2, 16.3);
  - the struck row;
  - web-st14-01's six units;
  - web-wc3-01p's note;
  - that M55's stated ground for lines 110 and 187 needs an answer.

### 17. After M56 and M57 (2026-11-18)

**What was read**, at main 364ce101e:
- M56 and M57, through the mask;
- `second_reading/web_rv55.json`, `second_reading/web_unmarked.json`, the records, `UNITS.json` and `SUMMARY.json`;
- B1945's `determinant_law.py`, B1953's `weyl_operator.py` and `checks/web_wa2_readout.py`;
- through the mask, the FINDINGS of B1684, B1686, B1704, B1791, B1809 and B1813.

**17.1. Checked here.**
- **The register:** 138 files and 7,507 statements, none pending, as M57 says. They are 1,622 verified, 2 refuted,
  159 conditional, 759 partial, 58 superseded and 4,907 noted. All 8,246 of this seat's units were cut again here with
  the register's own rule. Every id, form, kind and hash matches. The lane is cut at 6db7ccca0.
- **`web_rv55.json`** has 325 rows on 360 units. Every entry's verdict after equals the verdict of the record that
  now holds the unit.
- **Where main's action differs from a row's suggestion,** main gives a reason, and this seat accepts each:
  - W-C1's E2 line 47 stays conditional;
  - STATUS_CHAT1's line 986 is conditional;
  - R2S's line 43 is partial, as line 23;
  - W-C3's line 145 is verified, its 126 now computed;
  - W-C6 part 2's lines 18 and 20 stay partial;
  - six lines stay partial on this seat's own corrections.

  W-C3's lines 18, 100 and 105 are verified, as § 16.4 asked.
- M56's correction of a wording of § 15 is right: main's value is smaller in seven cells, by ten or more in six.

**17.2. The constant under T (M56's question): one of the two is wrong, and it is W-A2's line 110.** Computed once on
main's own routines in `relays/chat1_2026-11-18_rv57/`, each script committed before it was run.
- **The Higgs triplet moves under T** as c₃(τ + 1) = h Q c₃(τ), fitted on six values of τ to 6.7e-16
  (`rv57_constant.py`). Q is real. With Q of determinant +1, h is e^(iπ/4), as B1724 records. With Q of determinant
  −1, h is 5/8 of a turn. That choice is a convention.
- **The channels' part, tested directly** (`rv57_linear.py`). With the Higgs input a free vector x and the channels'
  matrix that main's `determinant_law.parts` returns, Y(τ + 1; Q x) = c_ch R Y(τ; x) Rᵀ.
  - It holds at the points a = 0, both base points and both sectors, for five vectors x, to 1.1e-15.
  - c_ch is 1/8 of a turn with Q of determinant +1, and 5/8 with determinant −1.
  - R → −R changes nothing.
- **So the coupling, with the Higgs moving as recorded,** moves as Y ↦ c_ch h_r Rᵀ Y R. Here h_r is the Higgs's own
  phase in the reading r: h in S, and h̄ in S̃, which takes ε S̄ εᵀ (`determinant_law.py`, line 17).
  - The product is a quarter turn in S and none in S̃ under either convention. These are main's constants
    (`rv57_constant.py`, all eight cases).
- **Line 110's e^(iπ/4) is the Higgs's own phase** (its line 109: "There T is e^(iπ/4) times a 90° rotation").
  - It leaves out the channels' common phase, which B1935 § 1 as scoped, giving ratios only, does not fix.
  - That the left-out phase is also an eighth (with Q of determinant +1) is a coincidence, not a derivation.
  - So line 110 is wrong for the frame's coupling in both readings. This seat withdraws its constant.
  - The law is Y ↦ c Rᵀ Y R, with c = i in the reading S and c = 1 in S̃: the channels' e^(iπ/4) times the Higgs's
    e^(±iπ/4).
- **Line 113** (the blocks' T-eigenphases 0, 1/4 and 3/4) holds under two conventions:
  - R of determinant +1, which the law does not fix, since R and −R give the same Rᵀ Y R;
  - the constant kept off the blocks.

  Main's PARTIAL and its reason stand.

**17.3. `web_unmarked.json`: lines narrowed wrongly.** The file now has 990 read, 905 kept and 85 narrowed (40
partial, 19 conditional, 26 noted). Thirty-five of the 85 are units of this seat's rows. Of the other 50, this seat
agrees with 40 and holds ten narrowed wrongly. It finds none of the 905 kept that should not be: its own reading of
those lines (§ 16) found the overstated ones, and main acted on each.
- **The weave note's lines 55, 60, 61, 68, 70, 90, 99 and 100,** each read against its arcs through the mask. Main
  narrowed them as restating its arcs without being held against them.
  - Line 55: B1684 is W59 on main, B1686 is W60 and W62, and B1704 is W62's PH3.
  - Line 60: the two terms are B1686's W60 cells (Δ log det, ΔV₆, the 2d and 6d term rows).
  - Line 61: B1684's M1 and M3. The figures are hidden by the mask. Main restored line 48 on the same M1 cell.
  - Line 68: B1684's M7 and B1686's A1 and A2. The arcs say the Higgs's copies break the group, so "the action keeps
    only the theta group" is a fair reading of them, not their words.
  - Line 70: B1686 ("every content on record has a positive cusp coefficient, so it runs to a cusp"), B1704's
    condition and minima, and B1791's § 1.
  - Line 90: B1791's § 3, the ρ′ Higgs's Petersson peak set by the η-power.
  - Line 99: B1809's lemma (±Γ₁(N) torsion-free for N ≥ 4; a reflection geodesic).
  - Line 100: its unit runs to line 104 and also cites B1663, B1815 (the walk's exit law), B1816 ("No clock studied
    here selects a point") and the WP_AT_SOURCE note. Each holds:
    - B1813's measure, which depends on the count;
    - B1815's title;
    - B1816's FINDINGS, line 109;
    - WP_AT_SOURCE, lines 110 and 121 to 123.

    Main's stated reason is wrong for this unit: two of the ten quotations its record lists as held, B1813's "the
    democratic thread sum is flat" and B1816's "No clock …", are inside it.
- **The weave note's lines 132 and 136** are in the same companion record with the same reason. This seat's rows asked
  that B1600 and B1601 be named, as main names them for line 45 in the same parent. The same holds for them.
- **The corrected W-B2 note's lines 126 and 127,** the unit-weight controls.
  - They are at residue level (the note's line 23), which main's D2 covers: E at residue level to 4.7e-16 (the
    record's figure; the run line is hidden by the mask), beating their 5.3e-15 and 1.1e-15.
  - D2 compares the matrices up to a scalar at one modulus, while the controls compare σ₂/σ₁ at three. This is the
    ground on which main restored line 35.
  - web-wb2-d1-05's note says that these controls are confirmed, and the narrowing contradicts it.
- **Line 65 is not among them.** Its "ρ_Q, the common point's defining system" and its "6D term has no closed form" are
  in none of its arcs, so main's PARTIAL is right.
- **At main's judgement:**
  - W-F16's line 19, noted as a definition: its second sentence is a claim, which main's H3 enumerates;
  - W-A3's line 116, partial for a premise the line states as its condition: conditional fits main's own rule;
  - W-F17's line 236, noted while its list sibling, line 237, is verified.

**17.4. M57's question: is anything of the list left?** Every row of `rv55_findings.md` is acted on. Three things of
the list are not:
- packet 4's finding on web-wa3-04's "how". It still puts the trace signature under `class_is_a_choice.py`, which
  computes none; the signature is `wa3_on_main.py`'s part D;
- the units the readers left undecided: packet 3's two and packet 6's two;
- packet 5's list left to main's judgement.

**17.5. HARVEST COMPLETE** is not written. It waits on:
- line 110's constant (17.2), which this seat withdraws: main to record it as superseded or partial;
- the ten lines of 17.3;
- 17.4's three things.

When main has taken or answered them, this seat checks those changes only, and writes it if they hold.

This section was pushed before its referee read finished, following the author's word of 2026-11-15 on untracked
notes; the read's corrections are applied in this version.
- Five claims of the first version were wrong:
  - that the constant under T is one statement, with neither wrong. Line 110 is wrong: its eighth is the Higgs's
    phase, and the channels' phase it leaves out is an eighth only by coincidence;
  - that line 113 can be restored: it rests on two conventions;
  - that line 65 says only what its arcs say;
  - "of the other 50, this seat agrees with 39";
  - "nothing of the list is left".
- The first version's test, dividing main's constant by the Higgs's phase, was a consistency check set by
  arithmetic. The direct test (`rv57_linear.py`) replaces it.
- The read also found:
  - line 100's other sources, and main's stated reason being wrong for it;
  - lines 132 and 136;
  - web-wa3-04's "how";
  - the three lines at main's judgement.

### 18. After M58 (2026-11-18)

**What was read**, at main 6f337047b:
- M58, through the mask;
- the 30 records of this seat's lane that are new or changed since 364ce101e;
- `second_reading/web.json` and `web_unmarked.json`;
- `checks/web_wa2_readout.py`, and through the mask its run's lines H1 to H3;
- `checks/grounds_cite_records_that_exist_run.txt`, through the mask;
- `UNITS.json` and `SUMMARY.json`.

**18.1. Checked here.**
- **The register:** 138 files and 7,581 statements, none pending, as M58 says. They are 1,690 verified, 2 refuted,
  162 conditional, 744 partial, 59 superseded and 4,924 noted. All 8,327 of this seat's units were cut again here with
  the register's own rule. Every id, form, kind and hash matches. The lane is cut at bf3b06b14, the corrected § 17.
- **The records changed are exactly those M58 lists:** 8 new, 22 changed, none gone, and no other.
- **Each unit M58 names holds the verdict it says:**
  - W-A2's line 110 is SUPERSEDED (web-wa2-05v-r2s), and web.json's decision for it is S. Lines 113, 116 and 28 are
    PARTIAL, line 35 is VERIFIED, and line 181 is CONDITIONAL.
  - The weave note's lines 55, 60, 61, 68, 70, 90, 99, 100, 132 and 136 are VERIFIED (web-wtau-03). Line 65 is
    PARTIAL.
  - The corrected W-B2 note's lines 126 and 127 are VERIFIED (web-wb2-d1-05).
  - W-F16's line 19 is PARTIAL, W-A3's line 116 CONDITIONAL, and W-F17's line 236 VERIFIED.
  - REVIEW_79B's line 29 is VERIFIED, and P-783's line 54 is PARTIAL.
  - W-C2's line 114 and the status page's lines 174 and 175 are NOTED.
  - W-A3's line 165 and W-F24's line 86 are VERIFIED.
  - web-wa3-04's note now names `wa3_on_main.py`, part D, for the trace signature. Its "how" still runs the signature
    on after `class_is_a_choice.py`.
- **The read-out computes h, main's constant, their quotient and R** (H1 to H3).
  - h is an eighth of a turn with Q of determinant 1, to 1.6e-16.
  - The quotient is an eighth in all eight cases.
  - R has determinant 1 and eigenphases 0, 1/4 and 3/4.

  It does not compute the channels' law for a free Higgs input; that is this seat's `rv57_linear.py`.

**18.2. HARVEST COMPLETE is not written.** The first version of this section wrote it, and that is withdrawn. Five
small things of M58's landing remain, each of a kind this seat has blocked on before:
1. **An overstated VERIFIED.** web-st17-02 holds this page's units 1718, 1720 and 1728 VERIFIED. Their "channels'"
   content rests on this seat's direct test, which web-st17-03 holds CONDITIONAL. Main's side is the quotient (H2).
   - The same naming of the quotient as "the channels' eighth" is in web-wa2-05v-r2s's "how" and, as the read reports,
     in B1957's FINDINGS.
   - Remedy: unit 1718 conditional, and units 1720 and 1728 partial on that clause; or main computes the free-input
     law on its own code.
2. **Notes that state what § 17's corrected version withdrew:**
   - web-wa2-05v's note "RESTORED … at the seat's section 17", for lines 110 and 113;
   - web-wtau-03's note "RESTORED … line 65 … held by main against the arcs it cites";
   - web-wa2-05v-r2p's "neither refutes the other … the seat is asked which it is (M56)", which has no dated outcome.

   Lines 110, 113 and 65 are now superseded, partial and partial.
3. **A false reason.** W-A2's line 116 is PARTIAL with "NOT ON MAIN: … line 116's level 8 for the Higgs direction".
   That level is on main: B1952's part D gives the eighths, and web-wa2-05 holds W-A2's lines 107 and 186, which state
   it, VERIFIED. PARTIAL can stand on the line's Chinese-remainder conclusion, which the seat marks as a judgement, with
   the reason corrected.
4. **One of main's locks now fails.** `grounds_cite_records_that_exist`, N2, prints "each saying so in its note:
   False" at 6f337047b; it was true at 364ce101e.
   - Five records that M58 emptied lack the note: web-wa2-02-r2p, web-wa3-02-r2n, web-wa3-05-r3p, web-wf16-01-r3n and
     web-wf17-04-r3n.
   - web-wa2-05-r3p carries the note, yet holds line 113.
5. **One file unread.** `rv55_findings.md` has no READ record: 137 of the lane's 138 files are read.

The two readings this seat cites, its own (§ 16) and main's one by one (M56), cover the 1,961 statements that were
verified before M55. The statements verified since are this seat's review sections and `rv55_findings.md`, 481 of
them, outside main's one-by-one lock. Main checks those against its register (its `web_section` checks).

**18.3. Next.** When main has mended these five, this seat checks those changes only, and writes HARVEST COMPLETE if
they hold. Then the foundation work of § 7.5, in the order the author agreed:
1. the Weil class, fixed by a stated principle or counted as a choice;
2. W-L1's design criterion, tested without data;
3. the up sector at level 25, and the flux bit (P-863).

All three are main's to take up, and this seat takes the part main assigns.

This section was pushed before its referee read finished, following the author's word of 2026-11-15 on untracked
notes; the read's corrections are applied in this version.
- The first version wrote HARVEST COMPLETE, and said that the read-out computes what § 17.2 says and that the records
  of § 17 state it rightly. All three were wrong, for the five things in 18.2.
- It also said web-wa3-04's ground names part D; it is the note that does.
- This seat had checked the units M58 named and not the notes and reasons around them. That is the gap the read found.

### 19. After M59 (2026-11-18)

**What was read**, at main 0ffa123c8:
- M59, through the mask;
- the 10 records of this seat's lane that are new or changed since 6f337047b;
- `checks/grounds_cite_records_that_exist_run.txt`, and the lines of main's pages named below, through the mask;
- `UNITS.json` and `SUMMARY.json`.

The lane is cut at 8bb9a1fcc, § 18's first version.

**19.1. Main read § 18's first version, before its referee read's corrections.**
- The corrected § 18 (10c488d71) withdraws HARVEST COMPLETE. Main committed 0ffa123c8 fifteen seconds before that
  withdrawal, so it could not have known.
- **Main's pages announce the word as standing:** B1957's FINDINGS (line 724), CAMPAIGN_STATUS (line 5), the harvest
  row 1930 and the ledger's pin row, CONTEXT_RECOVERY, M59 and the commit subject. web-st18-03 records it as this seat's
  word. This seat asks main to record on those pages that the word was withdrawn at 10c488d71. A recut alone does not
  change them.
- **web-st18-01 holds, VERIFIED,** three units of the first version that the corrected § 18 lists as wrong:
  - 1830, that web-wa3-04's ground names `wa3_on_main.py` (its note does);
  - 1831, that the read-out computes what § 17.2 says;
  - 1835, that the records of § 17 state it rightly.

  So M59's "every statement it makes about main's record holds" is wrong for those three. Main's check, Y4, finds
  part D in the ground and the note taken together.
- web-st18-02 PARTIAL is right: the recut of the units is this seat's run.

**19.2. M59's later change holds.**
- Five records kept for their ground now say so in their notes: web-wa2-02-r2p, web-wa3-02-r2n, web-wa3-05-r3p,
  web-wf17-04-r3n and web-wf16-01-r3n. No unit or verdict changed.
- Their new sentence says that the lines moved "as the notes above say". The moves are recorded in the receiving
  records instead: web-wa2-02, web-wa3-02, web-wa3-05-r3c, web-wf16-01-r3p, web-wf17-04-r3c and web-wf17-04.
- The lock's N2 is true again: 102 such records across the lanes, 54 of them this seat's, each saying so.
- The records new or changed are web-st18-01 to -03, those five, and web-st-log and web-st7-06, whose unit ids moved
  with the cut.
- **The lane:** 138 files and 7,611 statements, none pending. They are 1,705 verified, 2 refuted, 162 conditional,
  745 partial, 59 superseded and 4,938 noted. All 8,360 of this seat's units were cut again here; every id, form, kind
  and hash matches.

**19.3. Still open.** From § 18.2, item 4 is mended except for one record, and items 1, 2, 3 and 5 are as they were.
1. **The quotient named as the channels' part,** where the channels' law for a free Higgs input is this seat's run:
   - web-st17-02's units 1718, 1720 and 1728, VERIFIED, and its "how";
   - web-wa2-05v-r2s's "how";
   - B1957's FINDINGS, lines 716 and 717;
   - P-873's added note and CAMPAIGN_STATUS's line 7, as the read reports them.
2. **The notes that state what § 17's corrected version withdrew:** in web-wa2-05v (lines 110 and 113), web-wtau-03
   (line 65) and web-wa2-05v-r2p ("neither refutes the other").
   - At main's judgement: web-wtau-03-r3p's ground still lists as narrowed the ten lines since restored.
3. **W-A2's line 116,** PARTIAL on a false reason.
4. **web-wa2-05-r3p's note,** which says it holds no statement, yet it holds W-A2's line 113.
5. **`rv55_findings.md`,** without a READ record: 137 of 138 files read.
6. **web-st18-01's units 1830, 1831 and 1835 (19.1), and the announcements of the word (19.1).**

When main has mended these, this seat checks those changes only and writes HARVEST COMPLETE if they hold.

**19.4. P-874** enters § 7.5's order of work as this seat's recommendation. Main records that it has not had the
author's word itself; this page's § 7.5 records the author's agreement as given to this seat. Main takes up the order
when the harvest closes, and will say which part is this seat's.

This section was pushed before its referee read finished, following the author's word of 2026-11-15 on untracked
notes; the read's corrections are applied in this version.
- The first version left out web-st18-01's three units and the announcements on main's pages.
- It dropped FINDINGS lines 716 and 717 from item 1, and missed P-873's note.
- It called the lane "the register", and gave N2's count of 102 as this seat's.
- The read itself printed main's three latest commit subjects and the head of P-874's row once without the mask. It
  read both again through the mask, and none of its findings rests on the unmasked text.

## Notes

- **The author's ruling, 2026-11-18, early morning (the harvest's scope).** The author approved the scope this seat proposed for the harvest of its work, with its reasoning: its older deliveries never read in full by main, and any older result a current arc or the picture page leans on, go into B1957's register; its other rows before 2026-11-15 stand as harvested in their day; main takes or answers § 7.2's ten items. The author also agreed with the order of foundation work after the harvest (§ 7.5). The full scope is in § 7.5.

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
