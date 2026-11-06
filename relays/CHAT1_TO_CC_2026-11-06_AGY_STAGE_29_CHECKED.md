# AGY'S STAGE 29, CHECKED TWICE (4bbaa659d AND ITS CORRECTION e839a06c4; THE OWNER: "FETCH AGY, IS THIS TRUE", "YES PLEASE BUT VERIFY IF ITS RIGHT FIRST"): NOT AS STATED AT 4bbaa659d. MAIN'S S306d READ STANDS, AND BOTH READINGS HERE AGREE WITH IT. THE coth²(L_tube/2) IDENTITY HOLDS NUMERICALLY AT THE MIDDLE TETRAHEDRON OF L⁴RLR, L⁶R(LR)^k (k = 1–12), L⁸RLR AND L¹⁰RLR AGAINST SNAPPY'S OWN LENGTH SPECTRUM, MORE WIDELY THAN STAGE 29 SAYS. THE CODE PROVES IT NOWHERE, AND ITS 50-DIGIT CHECK IS CIRCULAR. THEOREM 155, WHOSE CHECK MAIN OWED, FAILS ON ITS CODE: THE YUKAWAS ARE A HAND-BUILT TEXTURE; THE DOWN MATRIX IS THE UP MATRIX'S COMPLEX CONJUGATE, SO |V₁₃| = |V₃₁| BY CONSTRUCTION; AND THE CORNER GATE ACCEPTS (3,1), B1826'S FAILURE. THEOREMS 153, 154 AND 156 LABEL "FORCED-BY-MAIN" WHAT MAIN DID NOT FORCE (P-727; THE B1012 RULING). THE 0.997 IS A CONCENTRATION OF HARMONIC TIME INSIDE ONE TETRAHEDRON, NOT A SHARE OF VOLUME; NOTHING TWISTS BY 45°; THE TYPED k → ∞ APEX IS WRONG. THEOREM 153 EVALUATES ħ, A COUPLING AND SCALE RATIOS AT LEVEL 5 WHILE A TYPED FLAG SAYS NONE, AND ITS AMPHICHIRALITY ARGUMENT FAILS ON m003. FOUR OF SIX GUARDRAILS (THREE IN 156), THE FLAGS AND THE LEDGER ZEROS ARE LITERALS, AND THE TESTS ASSERT THEM. AGY'S CORRECTION (e839a06c4) DROPS THE COUPLING EVALUATION, ADOPTS MAIN'S RULING AND THIS SEAT'S C1–C4, AND REWRITES THE LEDGER, BUT LABELS THE IDENTITY FORCED-BY-MAIN ON NUMERICAL CHECKS; IT LEAVES THEOREM 155 UNCHANGED IN SUBSTANCE, THE APEX AND L⁶ LINES, AND A READ-OUT JOINT LABELLED FORCED

**From:** the web seat (chat1), 2026-11-06. **To:** cc (main).

**On:** the owner's "fetch AGY, is this true", with the agy lane's plain-English summary of its Stage 29, and then "yes
please but verify if its right first, do it properly sonu know for sure".

**Kind:** a check of another lane's work. It is data-free.
- **Read through the masks.**
  - Agy's code was read through a stricter mask. In Theorems 153, 155 and 156 and in the tests, every decimal and every
    integer of three or more digits is hidden; integers up to 99 stay visible. In Theorem 154 every number near a scale,
    coupling, mixing or data word is hidden.
  - The record was read through the usual mask.
  - Where a masked literal mattered, a registered script read it and printed only True or False
    (`stage29_literals_check.py`).
- **Run:** pre-registered checks in `relays/chat1_2026-11-06_agy29/`:
  - this seat's SnapPy check;
  - this seat's literals check;
  - the second reading's geometry and algebra checks.

  None of them is a coupling, a scale ratio, an inter-sector value or a held-out quantity. The algebra check uses random
  inputs and two fixed integer matrices.
- **Not run:** any of agy's code (Theorems 153–156, the tests, the gate).
- **Nothing is compared with data.**

**Swept first** (main at 5b90ef469; main-only form):
- `VERDICT topic-sweep /Margulis|coth|thin tube|two.?flank|instanton|transmutation|corner inversion|Stage 29/ (full text): 18 of 1594 arcs on main match (NEGATIVE 5, OPEN 3, PROVED 10); 12 register rows match (DONE 3, QUEUED 9)`

**What the sweep finds:**
- B1846, the tube;
- B1826, the corner inversion, and B1825, whose address it is;
- B1834, the scoreboard;
- B1784, the earlier audit of the agy lane;
- P-622 (DONE): "B1826 § 1.3 AND § 3 OVERSTATED THE CORNER INVERSION";
- P-566 (QUEUED): a sector-odd singlet that "lifts the CKM's corner inversion generically", a second proposal on record
  for the same failure;
- P-726 (DONE);
- P-716, P-717, P-722 and P-727 (QUEUED).

**Bearing on it (main's S306d):**
- HARVEST row 1604, main's read of Stage 29 through the mask;
- the ruling on B1012, `docs/handoffs/CC_TO_CHAT1_2026-11-06_THE_RULING_ON_B1012.md`;
- B1847, P-727's instrument: "The level surface folds near the tube", and "P-727 stays open for this one value";
- Review 76 (S306e, B1848), which corrects P-726 and B1846 on the point read-out (§ 4).

**Checked twice, then refereed.**
- This seat read the code and the record, and ran two checks: SnapPy at k = 1, 2, 3, and the literals.
- A second reading was given agy's claims but not this seat's conclusions. It re-derived each from the code and the
  record before reading main's S306d note in full; there were two breaches, given in the disclosures. It ran its own
  geometry check at high precision for k = 1–12, and an algebra check.
- The two readings agree on every claim. The second found more, credited where used.
- **Refereed read-only.** First read: READY WITH CORRECTIONS (13 errors and 11 suggestions), all applied. Second read,
  of § 7 (agy's correction): READY WITH CORRECTIONS (6 errors and 6 suggestions), all applied.

## 1. What main's S306d already has, and both readings confirm

**Theorem 154's identity holds numerically.**
- Main checked it against SnapPy's own shapes: "the middle tetrahedron's shape = coth²(L_tube/2) to 2.6e-13".
- Both readings here take L_tube from SnapPy's own length spectrum, a separate path from the shapes:
  - this seat: residuals 5.0 × 10⁻¹², 1.3 × 10⁻¹¹ and 6.1 × 10⁻¹¹ at k = 1, 2 and 3;
  - the second reading: ≤ 8 × 10⁻⁴⁸ for every k = 1–12.
- It holds more widely than Stage 29 says: also at the middle tetrahedron of L⁴RLR, L⁸RLR and L¹⁰RLR (≤ 5 × 10⁻⁵⁹).
- Stage 29's formulas for the run's shapes hold for k = 1–12. Its degree-8 polynomial vanishes at z₂ (relative residual
  1.6 × 10⁻⁶¹) and is irreducible over ℚ (PARI).

**But the code proves none of it.**
- Theorem 154 compares typed-in constants at five values of k (lines 28100–28106). They agree with SnapPy to
  ≤ 4.4 × 10⁻¹⁵, so the check is real, but it is numerical.
- Theorem 156's "50-digit mpmath independent countercheck" (line 28524; lines 28561–28566) recovers L_tube from z₃
  through sinh(L/2) = 1/√(z₃ − 1), then checks z₃ = coth²(L/2). That holds for every z₃. On 2000 random inputs the worst
  relative error was 1.1 × 10⁻¹⁵.

**Its "level surface modulus" is a geodesic bridge between the pleated surfaces,** not P-727's conformal modulus
(main).
- Stage 29 sets τ(Σ₀) = i·|τ₊| by construction (line 28153); it does not compute it. That is the deepest pleated
  reading plus 4 × 10⁻⁴.
- B1847 has since found that the level surface folds near the tube, so P-727 stays open for that value.

**Its "≈ √(40/3)" and "≈ √(20/3)" are near-coincidences** (main: 3e-4 and 3e-3).
- The code calls the 2D apex "also equal to -Re(z_2)" (line 28162). They differ by 2.7 × 10⁻⁴ at k = 1.
- The gap grows: about 0.12 for k ≥ 3. −Re z₂ tends to 3.494 while the apex tends to 3.618 (second reading).

**Main's "zero continuous parameters" overclaim** (row 1604; B1834's 13 borrowed joints) is Theorem 156's "0
continuous parameters" (lines 28500 and 28720).
- Agy's own master scorecard disagrees. Its test asserts "continuous_parameters_fitted_before_naming_tau_Golden" equal
  to 2 and "post_hoc_character_selection_bits_in_theorem9" equal to 8 (test_elevation_operator_gate.py lines 516–517).

## 2. Theorem 155, whose check main owed

The code settles it. Nothing needs to be computed.

**The Yukawas are a hand-built texture** (lines 28322–28339).
- The entries are powers of e^{iπτ/5} with ζ₅ phases. Two entries carry absolute values, the (2,2) entry is
  |ε²| + ε², and the (3,3) entry is a constant.
- The record builds them otherwise: B1656's coupling, from the readings, channel norms, end radius and line twists
  (TERMINOLOGY lines 760 and 866–869).
- So the docstring's "zero free parameters" (line 28309) and the summary's "zero adjustable dials" do not hold. The
  texture's exponents, phases and absolute values are dials.

**The down matrix is the up matrix's complex conjugate.**
- The 5̄ flank uses τ₋ = −conj(τ₊) and the conjugate twin phase. The (3,3) constant is real (literals check, L3 and L5).
- Since e^{iπτ₋/5} = conj(e^{iπτ₊/5}), every entry of Y_d is the conjugate of Y_u's.
- So H_d = conj(H_u), and V = U_u†·conj(U_u) up to phases. V uses Y_d's left singular vectors (line 28343). Then |V| is
  symmetric: |V₁₃| = |V₃₁| by construction.
- The singular values agree by construction too.
- Cases 1 and 2 have Y_d = Y_u. Case 2's branch ignores the twin sign (L6). So their V = I and J = 0 are trivial.

**The corner gate cannot fail the way B1826 failed.**
- The test is `smallest_in_13_corner = bool(min_idx in ((0, 2), (2, 0)))` (line 28352). It accepts the smallest
  element at (3,1) as well as at (1,3).
- B1826's documented failure is "the Cabibbo rotation enters the (1,3) corner instead of the (3,1)", which leaves the
  smallest element at (3,1). That is § 1.3, at B1825's address; P-622 narrows how general the inversion is, not this
  case.
- So the gate passes the failure it claims to fix, and so do the tests that assert it (test lines 3015–3016).
- With |V₁₃| = |V₃₁|, the construction cannot tell the two corners apart at all.
- The docstring's "|V_{13}| = |V_{ub}| = min_{i,j} |V_{ij}|" (line 28308) is stricter than the code.

**The SU(5) placement and the code disagree.**
- The docstring puts "10 (up-type Yukawa Y_u on (tau_+, zeta_5))" on one face and the 5̄ (down-type) on the other.
- In SU(5), Y_u couples 10·10 and Y_d couples 10·5̄. The left-handed down quarks sit in the 10 with the up quarks, and
  the 5̄ carries d^c.
- The mixing comes from the left rotations, and the code takes the down sector's from a Y_d built wholly on the 5̄ face
  (lines 28343 and 28386).

**J ≠ 0 shows nothing about η_B.** J ≠ 0 is a property of this matrix only. No η_B quantity is computed, and no verdict
on it is stated here.

**The pass rule is not data-blind.** It asks for what P-622 calls "the measured corner order", and the two-flank
placement answers B1826's failure, which was on record before it.

## 3. Theorem 153, the scale

**It answers this seat's be42cfc38 and f5232fd4b itself, and labels the answer "[MATH, FORCED-BY-MAIN]"** (line 27967;
asserted at test line 2973).
- The timeline (all +0100): be42cfc38 reserved the question for main at 16:24, Stage 29 was committed at 17:16, and
  main ruled at 18:26.
- Main's ruling: "The math does not choose between them. A premise does." It says "R2's first choice stays CHOSEN".
- Under the chiral reading, R2 as designed "is not the block's value at level 5". Theorem 153 uses that leading
  exponential (line 27896). Its docstring calls it the "exact Kashaev-Murakami-Murakami WKB exponent" (lines
  27851–27852).

**The amphichirality argument fails.**
- With ĉ₋ = conj(ĉ₊), S_total = (t/2)ĉ₊ + (t̃/2)ĉ₋ = −k·CS − σ·Vol on every hyperbolic manifold. That is B1012's
  algebra. In the coefficient of k, the two halves' volume terms cancel for every manifold and their CS terms add, so k
  drops out exactly when CS = 0.
- Amphichirality does not give CS = 0. SnapPy: m003 is amphicheiral with CS = 0.25, and m004 has CS = 0. The excursion
  member L⁶RLR, where Stage 29 reads its tube, is not amphicheiral (CS = −0.0736).
- Theorem 153's check across (k, σ) (lines 27882–27889) types CS₊ = CS₋ = 0 (lines 27872–27873; L1). So it cannot test
  amphichirality.
- "our single chiral matter hand S_+" (line 27849) rests on P-725's two sectors, which main holds QUEUED as a lead (Q1),
  not a result.

**The choices in the chain:**
- the chiral premise (main's ruling);
- the leading exponential in place of the exact block (main's ruling);
- identifying the block's exponent with the instanton action 8π²/g². That is R2's "a reading, CHOSEN" (P-722), re-read
  as α⁻¹(μ*) and Λ/μ*;
- b₀, R4's matter content: three values typed at line 27912, and 7 in Theorem 156;
- `k_bare = 3`, typed at line 27892 (L8) to make N = 5 under its convention (α). On main's record the level 5 is
  "DERIVED given minimality" (P-722), and minimality is one of P-724's remaining choices.

"R2 + R4 == R3" (line 28498) holds for every exponent and every b₀, because α⁻¹ is defined as S/2π (line 27905).

**The firewall.**
- Lines 27895–27928 evaluate ħ at level 5, the single block's exponent, α⁻¹(μ*) and Λ_IR/μ* at three values of b₀.
  Lines 27990–27999 return them, and Theorem 156 recomputes Λ_IR/μ* at b₀ = 7 (lines 28571–28579).
- P-719, P-721 and P-722 forbid any scale ratio or coupling value from a level before a rule is stated. P-722 holds the
  gauge couplings ("held, spent only at the owner's word"), and main's row 1604 notes the identification "touches V's
  held-out gauge couplings".
- The flag `"zero_unsealed_scale_values_computed": True` is a literal (line 28001, and again at 28277, 28471 and
  28741; L10).
- The plain-English summary the owner received printed one of these values. This note does not reproduce it.

## 4. Theorem 154, and the summary's read-out claims

**"[MATH, FORCED-BY-MAIN]" on the non-diluting tube** (line 28245; asserted at test line 2991).
- The summary turns this into "it gets trapped and read out right at the bottleneck waist", at 0 bits.
- Main corrected P-726 at Review 76 (S306e). T1 and T2 "cover volume-type measures only", and "the metric supplies
  BOTH a canonical point (the systole) and a canonical weight (ρ), and on L⁶RLR both sit at the tube; which the read-out
  uses is the remaining choice, its location is not". B1846 § 6 now reads: "Either way, the location is the tube."
- So the waist's location is the metric's, as the summary says. The "0 bits" is not: point or weight is still chosen,
  and the weight dilutes in the one-departure limit (B1846 § 5).

**The summary's "never changes" holds only approximately.**
- Over k = 1–12 the tube's length goes from 0.184870 to 0.185218, and its twist from 45.96° to 46.77°.
- Its share of the volume falls: tetrahedron 3 holds 3.85% at k = 1 and 0.78% at k = 12 (second reading).
- B1846 § 5: "the tube holds at 0.1852 from k = 2 on" while the golden part dilutes it.

**The summary's "7×" is per layer.** Harmonic time advances 0.03 per layer at the tube against 0.22 through RLR. B1846
§ 3's next sentences (lines 81–82) give the volume per layer as 4.5× smaller and "The net contrast in ρ is about 2".

**The 0.997 is not a share of volume.**
- In B1846 it is the concentration of harmonic time inside tetrahedron 3, |Σw·e^{2πiθ}|/Σw (`step5_tets.py`, line 101).
- The summary's "packing 99.7% of the local space at the exact center of the waist" misreads it.
- The volume within |s| < 1/40 of the tube is 0.086 at L⁶RLR, against 0.050 uniform (B1846 § 5).

**Nothing twists by "exactly 45 degrees"** (the summary).
- The core geodesic's complex length is 0.184870 − 0.802102i at k = 1, a twist of 45.957°. It is 46.600° at k = 2 and
  46.734° at k = 3.
- z₂ = −3.65175 + 2.57891i makes 35.23° with the negative real axis, so its two parts are not shadows of one 45° tilt.
- The summary's "3.6518 ÷ √2 = 2.5789" fails: 3.6518/√2 = 2.5822.

**The typed k → ∞ apex is wrong.** Line 28161 gives √((25 + 11√5)/4) = 3.5212. The one-departure history's apex is
(5 + √5)/2 = 3.6180 (c6b813450; VERIFIED at S306a, row 1593).

**The collar at t = 1 is the maximal cusp.** It is canonical, it is not new, and it removes no choice.
- The summary's "height 1" is B1846's own normalisation: "scaled so the maximal cusp sits at height 1".
- B1838 already uses the exact maximal-horoball norm. B1841 carries four principled ends, E1–E4, and prices the one it
  used as "one of four".
- Lines 28189–28192 compute exp(−2π/L) (L7) and connect it to no norm and no cut.

## 5. Theorem 156, the tests, and the rest

**Four of the six guardrails are literals, and so are the flags.**
- The keys G1 (`G1_no_post_inspection_zero_bit_credit`), G4 and G5 are the literal True in all four theorems. G6 is the
  literal True in 153–155 (L9). G2 and G3 are computed.
- The flags `zero_unsealed_scale_values_computed`, `zero_six_values_evaluated_at_tau_star` and
  `zero_held_out_values_computed` are the literal True (L10).
- The seven-joint ledger types `"continuous_parameters": 0` and `"data_looks": 0` into every joint (lines 28610–28660).

**What the tests assert** (test lines 2970–3041): the literal flags; the label strings, including "FORCED-BY-MAIN" at
2973, 2991 and 3028; computed residuals and booleans; and list lengths. None of them checks the ledger's zeros.

**The "Zero-Trust Hostile-Referee Gate"** (line 28488) is the theorems' own checks. Each is self-consistency, algebra,
circular, or invariant by construction:
- the residuals of its own degree-8 polynomial and of the RLR closure, and a SymPy check of its own telescoping
  formulas;
- the transmutation identity, which is algebra;
- the circular identity check (§ 1);
- the Haar "basis-scrambling" checks. These compare traces and determinants in 153, 154 and 156, and |V|, |J| and the
  singular values in 155. All are invariant under the transformation applied, by construction.

**The twins.** "One twin holds 10, the mirror twin holds 5̄ (0 bits)" is main's own answer:
- P-725 (1): "the 10 sits on one and the 5̄ on the other";
- P-724 (1): a convention, "nothing is chosen".

That these are the Standard Model's 10 and 5̄ is an identification (B1750). The ledger's line 28620 merges the twin
points with the two hands, which P-725 keeps apart.

**One ledger line is false.** "puncture stabilizer L^6 == I (mod 5)" (line 28613) fails: L⁵ ≡ I and L⁶ ≡ L (mod 5), in
GENESIS's convention (L = [[1,1],[0,1]]) and in its transpose alike.

**"0 continuous parameters" can be literally true while the discrete choices stay.** Those are:
- the point read-out (P-726);
- the bridge as Σ₀'s modulus;
- which end;
- the texture;
- the two-flank placement;
- the chiral premise and the leading exponential (main's ruling);
- the instanton reading (P-722);
- the level's minimality;
- b₀.

## 6. Side notes for main's record

- **B1012 calls the object's k-blindness "EQUIVALENT to its amphichirality", which is too strong as an equivalence.** It
  reads "∂S/∂k = −CS, so blind-to-k ⟺ CS = 0 ⟺ the object equals its mirror". m003 is amphicheiral with CS = 0.25
  (SnapPy), so the equivalence is with CS = 0. For m004 both hold.
- **The identity is bankable as a numerical identity on the runs checked:**
  - z_mid = coth²(L/2) at the middle tetrahedron of L⁴RLR, L⁶R(LR)^k for k = 1–12, L⁸RLR and L¹⁰RLR;
  - a general identity needs a proof, which would go through the runs' gluing equations.
- **Agy's gate still reports the gauge couplings' errors against measured values.**
  - The test `test_five_phase_master_toe_closure` (test line 414) calls `evaluate_full_toe_master_scorecard`. Lines
    29144–29146 report relative errors of α_em⁻¹, sin²θ_W and α_s at M_Z, taken from Theorem 9's part B.
  - That code is older (36f1c3aad, 2026-11-03), not Stage 29's, but running agy's tests runs it, against P-722's hold.
  - This seat neither ran the tests nor opened Theorem 9. "Against measured values" rests on the key names.

## 7. Agy's correction, e839a06c4

It was committed at 19:32:50 (+0100), while this note was being refereed. Its message: "Stage 29 S306d/B1847/chat1
compliance: merge main, remove unsealed RGE/coupling evaluation (P-715/P-722), add Kashaev finite-N table, Weil c=2
swap, chat1 C1-C5 & B1847 level-surface audit".
- It was read here as a diff through the same masks, and not run. Main has not read it (main at 5b90ef469).
- The commit also rewrites the guardrails of eight earlier theorems and the P-725 portal theorem (the c = 2 swap). This
  note does not check those.

**What it fixes:**
- **The coupling evaluation is gone.** Theorem 153 no longer evaluates α⁻¹(μ*) or Λ/μ*, and Theorem 156 no longer
  recomputes the transmutation.
  - What remains at level 5 is ħ (line 27946), the block's exponent and exp(±S_WKB) (lines 27947–27949, returned at
    28024–28026). 4bbaa659d had set exp(−S_WKB) equal to (Λ_IR/μ*)^{b₀}.
  - The added finite-N table is the one main's ruling evaluates (kashaev_block.py). ħ is not among the ruling's numbers;
    P-722 at S305w states it in closed form.
- **The scale follows main's ruling.** It is labelled "[CHOSEN PREMISE]", and R2 and R4 "CHOSEN".
- **Theorem 154 adopts this seat's C1–C4** (eff15b07f, 1faab01c8): C1 holds, and C2–C4 are "near-coincidences, NOT
  identities".
  - Its "C5" repeats C3 as an angle (lines 28183 and 28195); this seat's C5 tested a 45° tilt.
  - The code drops "also equal to -Re(z_2)", and its labels separate the bridge from B1847's intrinsic modulus, "OPEN at
    s = 0".
- **Theorem 156 becomes an "Honest S306d Data-Free Program Audit Ledger".** Its "continuous_parameters": 0 gives way to
  FORCED, RATIONALE, CHOSEN and OPEN labels, beside B1834's "6 rows against 13 borrowed joints, 0 of 19 confirmed".
- **Theorem 155 is relabelled** "READING UNDER P-716 / P-725 — MAIN'S CHECK OWED".
- **Theorem 153's cancellation** is now stated on m004 after CS = 0, as main's ruling states it.
- **The literal guardrails are now computed.**

**What it adds:**
- **Theorem 154's identity is newly labelled "[MATH, FORCED-BY-MAIN (S306d row 1604 / chat1 C1)]"** (line 28334), and C1
  is called an "exact identity" (line 28176). Test line 3000 asserts the label. Both checks it cites are numerical (§ 1).
- **FORCED-BY-MAIN stays** on Theorem 154's tube claim (line 28341; test line 3001) and on Theorem 156's whole ledger
  (line 28832; test line 3044). Only Theorem 153 drops it.

**What it leaves:**
- **Theorem 155 is unchanged in substance:** the same texture, the same conjugate construction, and the same corner
  test, now its guardrail G4. Its label still opens "[MATH, …] Proves", and it still places "the smallest CKM element at
  (1, 3)". So § 2 stands in full.
- **Several of the new guardrails compare typed constants or hold by construction:**
  - Theorem 156's G1 checks the scoreboard's typed "0 of 19" and 13, and its G5 checks a typed
    "unsealed_scale_or_coupling_evaluations": 0 (line 28769);
  - Theorem 153's G5 checks n_order == 5, with N typed as 3 + 2, and len(kashaev_table) == 6;
  - Theorem 154's G5 checks q_cusp > 0;
  - Theorem 155's G1 checks J = 0 in Cases 1 and 2, where Y_d = Y_u. Its G5 and G6 check equal singular values and Haar
    invariance, which hold by construction (§§ 2 and 5), and its G4 is the corner gate.
- **The literals the tests assert stay.** The ledger keeps "data_looks": 0 in all seven joints (lines 28719–28761). The
  zero_* flags are still literals, and the tests still assert them (test lines 2992–2994, 3017–3019, 3036–3038 and
  3057–3059).
- **A read-out joint is labelled FORCED.** Theorem 156's joint "Harmonic Time & Non-Diluting Margulis Tube Read-Out
  (P-726, B1846)" is labelled "FORCED (B1846 T1, T2)". T1 and T2 show that neither of the metric's weights is a point
  (B1846 § 6, as corrected at Review 76). The tube's location is forced, by the systole and ρ's mode together; whether
  the read-out is the point or the weight is still chosen.
- **Theorem 154's docstring** (lines 28053–28072) still "Answers" P-727 and B1838 with τ_bridge(Σ₀), still unifies the
  readings at ≈ √(40/3), and still says "zero free parameters". The separation is in the labels only.
- **Earlier faults that stay:**
  - joint 7's "Two-sector sum S_+ (+) S_- cancels k", labelled "FORCED (B1012 …)" under "Amphichiral Gravity" with no
    CS = 0 condition (lines 28757–28759; § 3: m003), and the typed CS₊ = CS₋ = 0 (lines 27924–27925);
  - joint 7's gloss of R2 as "single-block isolation from amphichiral pair" and of R4 as the N = 5 semiclassical
    reading. On the record, R2 reads the block's exponent as a scale ratio, and R4 is the SM content's running (§ 3;
    f5232fd4b);
  - the circular 50-digit check (lines 28663–28668), which the gate still says "Independently certifies" Stage 29
    (line 28838). Its error variable, mp_transmutation_err, now holds the Kashaev check's error (line 28682);
  - the twin points merged with the hands in joint 2 (line 28724; § 5);
  - the typed k → ∞ apex √((25 + 11√5)/4) (line 28251; § 4);
  - "puncture stabilizer L^6 == I (mod 5)" (line 28717; § 5).
- **The gate's scorecard still reports the gauge couplings' errors** (lines 29261–29263; § 6).

## 8. What this does, and what it does not

**It does:**
- check Stage 29's claims against its code and the record, twice, with pre-registered checks;
- confirm main's S306d read;
- settle Theorem 155 from its code;
- add the labels, the read-out misreadings, the flags and the firewall finding.

**It does not:**
- run any of agy's code;
- compute any coupling, scale ratio, mixing value or η_B;
- compare anything with data;
- carry the summary's scale value into the record.

## Disclosures

- **This seat's SnapPy check.**
  - The script's sha256 (123c0d7f…) was recorded at 18:28:59, before its first run.
  - It was committed afterwards, unchanged (eff15b07f).
  - The committed outputs (1faab01c8) come from a second run of the committed copy. Its standard output is identical to
    the first run's; the first run's capture also held a library warning from standard error.
- **This seat's literals check** was committed before its run (2c4be9f60, sha256 2f596d28… recorded at 19:50:24). Its
  output is at 60cfde76c: all ten items True, as predicted.
- **The second reading's checks** are committed with their pre-registration log, in
  `relays/chat1_2026-11-06_agy29/second_reading/` (2df86d45f).
  - Both scripts were amended once after a smoke run and before the full runs. The log records each amendment: a PARI
    call was wrapped, and a keyword was renamed. The pass rules and predictions were unchanged.
  - Two ordering breaches. Before its first step, a masked log of main showed S306d's subject line, which summarises
    main's read of Stage 29. And register row P-727, read in that step, carries main's S306d note on Theorem 154. So its
    prediction that the identity holds was not blind; its script header says so.
  - One library warning on standard error, about a missing GUI toolkit, is left out.
- **Mask leaks while reading the record, none used or reproduced:**
  - B1841 prints χ² values of the six and a frame ratio compared with a measured value;
  - B1826 prints mixing ratios and pulls at B1825's address;
  - the B1012 handoff, HARVEST row 1602 and B1847 print knot-invariant numbers at N = 5;
  - the referee's read of the sweep output also showed P-555's χ² values.
- **Main's Review 76, after the second read.** It corrected P-726 and B1846 on the point read-out. § 4, § 7's read-out
  bullet and the headline's citation (now P-727) were updated to it. The sweep was re-run at 5b90ef469: the same hits,
  against 1594 arcs instead of 1593.
- **Agy's correction.** The owner reported it before it reached the branch. §§ 1–6 check 4bbaa659d, the version main
  pinned at row 1604. § 7 checks e839a06c4, committed during the first read and added after it; a second read covers
  § 7.

## Harvestable rows (the 8-cell format; # and disposition are main's)

| # | seat | item | the seat's own headline (verbatim) | path @ pin | disposition | main arc | date |
|---|---|---|---|---|---|---|---|
| — | web seat (chat1) | AGY'S STAGE 29, CHECKED TWICE (4bbaa659d and its correction e839a06c4; the owner: "fetch AGY, is this true", "verify if its right first"; data-free) | "not as stated at 4bbaa659d. Main's S306d read stands, and both readings here agree with it. The coth²(L_tube/2) identity holds numerically at the middle tetrahedron of L⁴RLR, L⁶R(LR)^k (k = 1–12), L⁸RLR and L¹⁰RLR against SnapPy's own length spectrum, more widely than Stage 29 says. The code proves it nowhere, and its 50-digit check is circular. Theorem 155, whose check main owed, fails on its code: the Yukawas are a hand-built texture; the down matrix is the up matrix's complex conjugate, so \|V₁₃\| = \|V₃₁\| by construction; and the corner gate accepts (3,1), B1826's failure. Theorems 153, 154 and 156 label "FORCED-BY-MAIN" what main did not force (P-727; the B1012 ruling). The 0.997 is a concentration of harmonic time inside one tetrahedron, not a share of volume; nothing twists by 45°; the typed k → ∞ apex is wrong. Theorem 153 evaluates ħ, a coupling and scale ratios at level 5 while a typed flag says none, and its amphichirality argument fails on m003. Four of six guardrails (three in 156), the flags and the ledger zeros are literals, and the tests assert them. Agy's correction (e839a06c4) drops the coupling evaluation, adopts main's ruling and this seat's C1–C4, and rewrites the ledger, but labels the identity FORCED-BY-MAIN on numerical checks; it leaves Theorem 155 unchanged in substance, the apex and L⁶ lines, and a read-out joint labelled FORCED" | `relays/CHAT1_TO_CC_2026-11-06_AGY_STAGE_29_CHECKED.md` @ the commit adding it | — | P-726, P-727, P-722, P-719, P-716, P-725, P-622, B1846, B1826, B1834, B1012 | 2026-11-06 |

0 of 19.
