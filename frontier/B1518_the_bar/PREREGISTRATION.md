# B1518 PREREGISTRATION — THE BAR: a selection rule and a null model for a positive on a generated state, run first on main's class-index census. Does anything cheap decide which states carry a generation at their own level?

**Sealed 2026-10-02, before any cross-tabulation of main's own-level or level hits with the fibre torsion group, the sign, the
symmetry order or the reversal class is computed, and before any stratum rate, AUC or conditional test. Seat: cc (the
SM-derivation branch). Occasion: the owner's "continue with the next arc" after B1517, which is OPEN_LEADS sL-9 item 1 (GENESIS
GAP4, fork FK9). Under the owner's rules NO NEGATIVE FROM A BUG and SEE THE REPO FIRST, THEN THE LITERATURE (WORKING_RULES), the
instrument's and the run's planted controls are in §2, and the sweep is in §5.**

## 0. The question

GENESIS GAP4 (GENESIS.md:249–251): with hundreds of states, four frames, many levels and several end conditions, a
Standard-Model-like feature somewhere is expected by chance, so a selection rule and a null model must be fixed before a match
counts. sL-9 item 1 (OPEN_LEADS:3712–3720) puts this first, and B1517 added that a rate names its unit.

The record already holds the pieces. They are §5's first list: the emergence bar (FORCED, UNSOUGHT, EXACT, CONTROLLED),
WHAT_WOULD_COUNT's three grades, B614's look-elsewhere gate, INPUT_COMPLETENESS rows 7–8, E20 and E61. They were written for value
matches and for single structures. None says what a positive on one generated state must beat. None has been run on a census of
generated states.

This arc does three things:
1. **States the bar** for a positive on a generated state (§3). It is sealed here, so the run cannot shape it.
2. **Runs its null model on the one frame with a population:** main's class-index census (B1439), at the own level and by level.
3. **Grades the record's positives** under the bar (§6.1, decided at design time).

It asks of main's census (main's L229 (i), "the own-level law"):
- **Q1.** Is a state's own-level firing determined by its fibre torsion with the monodromy's action? Or by that plus the symmetry
  order?
- **Q2.** Does the fibre torsion group predict firing beyond chance?
- **Q3.** Does reversal symmetry predict firing beyond the fibre torsion and the sign?

## 1. Setting and notation

- **The population.** GENESIS §3's census: the 758 signed word states ±w, w a primitive word in L and R of length 2 to 12 with
  both letters, up to rotation and the swap L ↔ R. They are **536 manifolds**: a word and its reverse are one oriented manifold
  (B1517).
- **The unit.** The **manifold** is the primary unit; word-state rates are reported beside it. A level k of a state is the bundle
  of (εA)ᵏ. So (+w)ᵏ and (−w)ᵏ are one manifold for even k, and a reversal pair stays one manifold at every k. Main's 988 level
  records are **659 level-manifolds** (k = 1 to 7: 536, 79, 32, 5, 4, 1, 2).
  - Main keeps both rows of an even level "because the decks differ" (main B1434 FINDINGS:96). Its record unit is (state, k)
    with its deck. The manifold unit here is for manifold-level statements; it does not replace main's.
- **The hit** is main's, read from main's records:
  - a level carries a **generation-shaped background** when its five charged sectors (Q, u^c, e^c, d^c, L) have equal non-zero
    class index (B1434 PREREGISTRATION:34; B1439 PREREGISTRATION:9–13; main's B1297 index);
  - a state **fires at its own level** when its k = 1 level carries one.
- **Covariates** (own code; none reads an outcome):
  - **G** = coker(εA − I), the fibre torsion group, with Smith invariant factors d1 | d2. |G| = |2 − t|, t the signed trace, and
    the exponent is d2.
  - the sign ε, the trace and the word length;
  - the **reversal class**: closed (the reverse word is the same state up to rotation and swap) or paired;
  - the **symmetry order** and **amphichirality**, from SnapPy 3.3.2 `symmetry_group()` (the detector E52 #7 fixed).
- **Strata:**
  - **S1** = (d1, d2), the fibre torsion group.
  - **S2** = (d1, d2, ε), the fibre torsion with the monodromy's action. εA acts on G as the identity, so A acts as ε. S2 also
    fixes tr A (F2 below).
  - **S3** = (d1, d2, ε, symmetry order).

## 2. Computed or seen before the seal (disclosed)

### 2.1 Main's records, read for this arc (main @ 637561d3)

- **B1439 FINDINGS:**
  - 95 of 758 states fire at their own level: 49 of sign + and 46 of sign −.
  - By word length, firing over all states for lengths 2 to 12: 0/2, 0/2, 0/4, 1/6, 1/10, 3/18, 5/32, 10/56, 16/102, 27/186,
    32/340.
  - The level table by records (:14–22). For k = 1 to 7: 95/758, 100/180, 25/32, 10/10, 3/4, 2/2, 2/2.
  - "No criterion found" (:53–56): torsion divisible by 3 holds for 71 of the 95 and for 209 of the 663 silent states. Non-cyclic
    fibre torsion holds for 54 of the 95, against 194 of the 758.
  - The fourteen complete states.
  - The five silent new three-fold levels (:61).
  - The root's level seven: 3 136 backgrounds (:63).
  - E1–E8 and the fence (:98).
- **B1434 FINDINGS:**
  - m369 = −LLRLR and s639 = −LLLRLR fire at their own level.
  - Ten of twelve three-fold levels carry orbits of three. The root's three-fold level carries 48 backgrounds.
  - §3 (:73–80): "nothing in this census selects m369 or s639"; "Nothing in the census distinguishes the root except that it is
    the state with nothing at its own level".
  - Caveats 3–4 (:95–96).
- **B1438** (the slope law), **B1442** (the exponent-two lemma), **B1414 row 5** (main's base rates).
- **Main's records, quoted into this arc:**
  - census_summary.json's 93-state list → `verification/main_B1439_firing_own_states.json` (B1517 C5);
  - the 988 level records' fields (state, k, N, torsion, characters, firing, generation_backgrounds, lifted) →
    `verification/main_B1439_levels.json`. These were extracted for this arc. No count was taken from them beyond main's
    published table.

### 2.2 Own, banked (B1517)

- Main's list splits no reversal pair at the own level, and the rate is **87 of 536 manifolds**.
- At lengths 7 to 12, reversal-closed states fire 77 of 290 times and paired states 16 of 444 times (8 manifolds).
- **Derivable from the above, so not open here:**
  - the manifold rate 87/536;
  - the unconditional reversal split by manifold: 79 of 314 closed against 8 of 222 paired (pairs begin at length 7, B1517 C2);
  - D3 (§6.1).

### 2.3 Own, computed at design time (covariates only; no outcome field read)

- **`covariates.py` → `covariates.json`.** Its controls passed:
  - 758 states and 536 manifolds;
  - |G| equals main's torsion on all 93 listed states;
  - m369 has G = ℤ/12, s639 has ℤ/15, m004 has trivial G and m003 has ℤ/5.

  By state: 194 non-cyclic; 314 reversal-closed (272 palindromic, 64 antipalindromic, 22 both); symmetry orders
  {2: 440, 4: 296, 8: 22}; 68 amphichiral; 286 groups G.
- **`level_covariates.py` → `level_covariates.json`.**
  - |G| and its exponent agree with main's torsion and N on all 988 records.
  - The records form 659 level-manifolds.
  - The root's tower has G at k = 1 to 7 of (1, 1), (1, 5), (4, 4), (3, 15), (11, 11), (8, 40), (29, 29).
- **`design_checks.py` → `design_checks.json`:**
  - **F1.**
    - Every odd-length state has even |G|: 268 of 268. Mod 2, L and R are the two transpositions of SL(2, F₂) ≅ S₃. An odd word
      is a transposition, so its trace is 0 mod 2. This is the literature sweep's check, proved here.
    - At even length, |G| is even exactly when A ≡ I mod 2: 164 of 490.
  - **F2.** (|G|, ε) fixes tr A on every state: tr A = |G| + 2 for sign + and |G| − 2 for sign −.
  - **F3, by manifold.**
    - S1 has 286 strata, with 406 manifolds in strata of two or more.
    - S2 has 422 strata, with 210 such manifolds.
    - S3 has 461 strata, with 140 such manifolds.
  - **F4.**
    - (reversal-closed, symmetry order) over the 536 manifolds: (no, 2) 220, (no, 4) 2, (yes, 4) 292, (yes, 8) 22. Reversal
      symmetry is almost the same thing as symmetry order 4 or more.
    - Amphichiral: 66 manifolds, 64 of them reversal-closed.
  - **F5.** Three own-level manifolds have exponent at most 2, and the census has no other level-manifold with exponent at most 2.
  - **F6, the conditional tests' power.**
    - Given S2, 32 strata hold both reversal classes: 70 manifolds, 36 of them closed.
    - Given S2 and the reversal class, 6 strata hold both amphichiral and chiral manifolds: 13 manifolds. So amphichirality is
      reported descriptively (R5) and is not tested.
- **`null_model.py --selftest`.** Ten planted controls pass, in both directions:
  - determinism and the AUC on a planted law;
  - no conditional effect where none was planted, and the planted one found;
  - a split manifold reported;
  - the exact interval and Šidák against their formulas;
  - the rank AUC equal to the pairwise definition;
  - the AUC permutation test finding a planted stratum effect and finding none where none was planted;
  - a lone unit scored at the population rate.
- **`bar_run.py --dry`.** Eight planted controls on synthetic hits drawn from covariates only, with no outcome field read. All
  pass:
  - a law of G leaves no mixed S2 stratum and is predicted beyond chance;
  - a planted reversal effect is found;
  - a covariate-free hit is predicted by nothing.

### 2.4 Not computed, not seen

- Any cross-tabulation of a hit with G, (G, ε), symmetry order, the reversal class given G, or amphichirality.
- Any stratum rate.
- The AUC, and the conditional reversal tests.
- The by-manifold length table, and the level-manifold rates (R3).
- D1's count, and the bar's strata table (R6).

## 3. THE BAR (the protocol this arc proposes; sealed with this file)

A **positive** reads: frame F, on state s (level k, end condition e), shows feature X. X is a Standard-Model-shaped feature with
an exact definition.

1. **The card.** State:
   - F, and X with its defining line;
   - the population P, a census of generated states (GENESIS §3) to a stated length;
   - the unit: word state, manifold or level-manifold (B1517);
   - how s was chosen: by a rule fixed before computing (the emergence bar's FORCED), or found by its outcome (scanned).
2. **The base rate.** The rate of X in P, in the unit, with its exact 95% interval (Clopper–Pearson). If F has not been run on a
   population, the positive is **UNJUDGED**: no credit and no refutation. The card names the population run that would judge it.
3. **The comparable objects** (E20, "only content a comparable object does NOT share is object-specific"; E61, "the widest
   population of the same type").
   - r is the **upper end of the exact 95% interval** for X's rate among the other units of s's stratum. A small stratum gives a
     wide interval, so it earns little credit, and no stratum-size threshold is set. A unit alone in its stratum gets r = 1.
   - For main's class-index frame the stratum is fixed now: (d1, d2, ε, reversal class), whatever P1–P4 read. An invariant that
     predicts nothing only widens the interval.
4. **Selection and trials.**
   - If s was chosen by a fixed rule, p = r.
   - If s was found by scanning n units, p = 1 − (1 − r_P)ⁿ, with r_P the population rate: the chance that the scan finds one.
   - Then every look the claim's arc made counts (Šidák over m looks): every frame, level, end condition and variant examined
     (INPUT_COMPLETENESS row 7; CROSSING_REQUIREMENTS R7; Gross–Vitells's trial factor).
5. **The gate.** The positive counts only if p < 0.01 after step 4. This is B614's G3 gate, the record's standing threshold. It
   is not a prior (PRACTICES, "a bar set from a prior is a bar set at the prior's error").

**The grades** are WHAT_WOULD_COUNT §3's three, plus one for a frame with no population:
- **DERIVED:** chosen by a fixed rule, and passes step 5.
- **REPRODUCED:** comparable objects show X at a rate that makes it unremarkable (step 5 fails). Zero credit, and labelled.
- **FITTED:** s was found by its outcome, and step 5 fails after the scan's trials. Negative credit: it spends look-elsewhere
  budget.
  - A census that reports its carriers is a base rate, not a positive. FITTED applies only to a claim that presents a scanned
    carrier as evidence.
- **UNJUDGED:** F has no base rate in any population.

## 4. BANKED IDENTITY:

The run reproduces the following before any test is computed.
- **C1.** Main's two records agree. The 93 listed own-level carriers, plus B1434's two (m369, s639), are exactly the k = 1
  records with a generation-shaped background: 95, B1439's count.
- **C2a.** No own-level manifold is split. This is B1517 C5, reproduced from the level records.
- **C2b.** No level-manifold at k ≥ 2 is split: a manifold's background count does not depend on which deck labels it (B1434 (d)
  and caveat 4).
- **C3.** The instrument's ten planted controls.
- **C4.** The covariate controls (§2.3).
- **C5.** The dry run's eight planted controls.

If C1, C2a, C3, C4 or C5 fails, the run stops before any test is computed. If C2b fails, R3 and D3 are withheld and nothing else
changes.

## 5. PRIOR ART:

### 5.1 The repository

Fetched 2026-10-02 with `git fetch --all`: main @ 637561d3, the audit lane @ e4bb7f68, this branch @ f1a2308a.

**This branch: the bar's pieces.**
- **The emergence bar,** `philosophy/THE_ORIGIN_POSTULATE.md:21–28`: FORCED, UNSOUGHT, EXACT, and CONTROLLED ("a generic or
  wrong object *fails* the same test").
- **`docs/WHAT_WOULD_COUNT.md`:**
  - §3 (:66–79): DERIVED, REPRODUCED ("so does any theory in its class"), FITTED ("it consumes look-elsewhere budget");
  - Tier 2 (:104–107): "no class-sibling shares" and "a global look-elsewhere budget".
- **`frontier/B614_null_model/NULL_MODEL_DESIGN.md:90–96`:** the Šidák-combined look-elsewhere correction and the G3 gate,
  p < 0.01.
- **`frontier/B511_physics_verdict/D0_GATES.md:7–9`:**
  - UNSOUGHT;
  - CONTROL: two foreign controls or more;
  - STATISTICS: "the match beats the committed base rate … denominators fixed BEFORE the census/scan runs; no post-hoc
    selection".
- **`docs/INPUT_COMPLETENESS_LEDGER.md:15–16`:** row 7, look-elsewhere over everything examined; row 8, the matched null ("the
  same measure the match criterion uses"). The unit is this row's question.
- **`docs/CROSSING_REQUIREMENTS.md:56`,** R7: every designer freedom priced.
- **`docs/ERROR_LEDGER.md`:**
  - E20 (:38), comparable objects and base rates;
  - E29 (:55), post-hoc analysis-model selection: the primary model is named here;
  - E52 (:81), two-sided and bite controls;
  - E61 (:100), the widest population of the same type;
  - E62 (:101), a closed form tested on its own examples.
- **`docs/PRACTICES.md:186–194`:** thresholds from an external source; "calibration on outcomes is not calibration on
  instruments".
- **`frontier/B855_wrong_null_audit/FINDINGS.md:9`:** "A genericity verdict is only as good as its null".
- **`frontier/B1234_a6_built_the_walls/FINDINGS.md:25–30`:**
  - 40 of 40 orientation double covers are amphichiral, by construction, against a control rate of 6 of 200;
  - main's B1414 later measured 181 of 203 123 census-wide.

  The population chosen fixes the rate.
- **B1517 C5 and sL-9 item 1,** this arc's occasion; **GENESIS** GAP4 (:249–251) and FK9 (:269).

**Main.**
- **B1439:**
  - the census, the hit and the level table;
  - "No criterion found … The list is the datum" (FINDINGS:53–56);
  - the fence "nothing selects a state" (:98).

  This arc's Q1–Q3 extend main's two-covariate look to strata, with a null model.
- **B1434:**
  - (a) the two own-level carriers;
  - (b) and §3, "orbits of three … not a property of the root": main's own comparable-object reading, which D3 reproduces by
    manifold;
  - caveat 4, the deck unit;
  - §6, the own-level law as a lead (:102).
- **Main's OPEN_LEADS L229** (:2985): (i) the own-level law, "the list is the datum and the law is open"; (iv) "what singles out
  a state".
- **B1438**, the slope law. Firing is read from slope coincidences of the fibre's torsion characters (Theorem A, :25). The slopes
  are sums over the word's letters (Theorem D, :53). So the word, not only G, enters: this is the reason for P1's prior.
- **B1442's lemma** (:23–31): a character group of exponent two forces I(Q) = −I(L), so no generation-shaped background. This is
  D1.
- **B1414 row 5** (FINDINGS:16): base rates on the census of SnapPy's one-cusped manifolds (chirality 0.089 %, the 2T door
  33.92 %, the count of three 0.050 %), reproduced from the outside bench. The base-rate step is practised on main, on a census
  population, not on the generated states.
- **S37's rule** of the same day: `topic_sweep.py` and the gate "seen-first". It is this seat's rule's counterpart, to reconcile
  in the next arc.

**The audit lane.**
- `GENESIS_RECONCILIATION_PLAN_2026_10_02.md:40` states the selection functional separately from the grammar. It is a plan, with
  no null model.
- R78 and R79 (signed levels; peripheral marking) bear on the unit at k ≥ 2: a level-manifold here forgets the peripheral marking
  (R79's question). C2b checks that main's counts do not depend on it.

**Sweeps.** `scripts/checks/prior_work.py` over 9 heads, deleted history and the working tree, 2026-10-02:
- "trials factor" is ABSENT.
- "Mantel" appears only in this arc's files.
- "own-level law" and "no criterion" are main's B1434 and B1439, read above.
- "what singles out a state" is main's L229 (iv) and its logs.
- "reversal-closed" is B1517, plus other senses: main's B1095 and B1085 (Fibonacci windows) and B128 (subshifts). These were
  read and do not bear.
- "null model", "base rate", "selection rule" and "look-elsewhere" are the arcs and docs above, plus older value-match arcs (B402,
  B467, B539, B608, B609 and others). None runs a null model on generated states.

### 5.2 The literature

Read 2026-10-02 by the seat's literature sweep; locations as read.
- **Look-elsewhere:**
  - Gross & Vitells, *Trial factors for the look elsewhere effect in high energy physics*, EPJC 70 (2010) 525, arXiv:1005.1891.
    Sec. 2.1, Eqs. 8–12: the trial factor ≈ 1 + √(π/2)·N·Z_fix. Sec. 1: background-only Monte Carlo "gives the correct answer".
  - Benjamini & Hochberg, JRSS B 57 (1995) 289, §3.1 Theorem 1 (FDR).
  - Benjamini & Yekutieli, Ann. Statist. 29 (2001) 1165, Theorems 1.2–1.3 (FDR under dependence).

  The bar keeps B614's family-wise Šidák gate, which is stricter than FDR control.
- **Base rates of Standard-Model features in ensembles of constructions:**
  - Douglas, *The statistics of string/M theory vacua*, JHEP 05 (2003) 046, §1 and §5: without a selection principle, no testable
    prediction.
  - Gmeiner, Blumenhagen, Honecker, Lüst & Weigand, *One in a billion: MSSM-like D-brane statistics*, JHEP 01 (2006) 004:
    - §4.3: no three-generation model among about 1.66 × 10⁸;
    - §5, Eq. 34–35 and Table 4: the product of suppression factors, about 1.3 × 10⁻⁹, after checking that the constraints are
      near-independent.
  - Blumenhagen, Gmeiner, Honecker, Lüst & Weigand, NPB 713 (2005) 83, §5.5: chirality has number-theoretic effects.
  - Douglas & Taylor, JHEP 01 (2007) 031:
    - §1: complete enumeration, "to be able to do unbiased random sampling";
    - §3: generation numbers favour composites and disfavour primes.
  - The heterotic scans impose three families as a filter, so none reports its base rate:
    - Anderson, Gray, He & Lukas, JHEP 02 (2010) 054;
    - Anderson, Gray, Lukas & Palti, PRD 84 (2011) 106005 and JHEP 06 (2012) 113;
    - Anderson, Constantin, Gray, Lukas & Palti, JHEP 01 (2014) 047;
    - Constantin, He & Lukas, PLB 792 (2019) 258.
  - Lebedev et al., PLB 645 (2007) 88, Table 1: a filter cascade, about 1 % overall, a patch "unusually fertile".
  - **Dienes & Lennek**, *Fighting the floating correlations*, PRD 75 (2007) 026008, §§1, 3, 6: generators sample models
    unequally, so correlations move with the sample, and there is a "lamppost effect". This is the literature's form of B1517's
    unit point.
- **Torsion statistics:**
  - Dunfield & Thurston, Invent. Math. 166 (2006) 457, §8, Theorem 8.4 and §9 Theorem 9.1. The base rates depend on the ensemble.
  - Sawin & Wood, *Finite quotients of 3-manifold groups*, Invent. Math. (2024), Proposition 9.3: a Cohen–Lenstra-type law for
    H₁ with its linking form.
  - Rivin, *Statistics of random 3-manifolds occasionally fibering over the circle*, arXiv:1401.5736:
    - §2.1, Corollaries 2.2–2.4: H₁(M_φ) ≅ coker(φ_* − I) ⊕ ℤ, and |tors| = |det(φ_* − I)|;
    - Theorem 2.5: every ℤ/r ⊕ ℤ/rs is realised.

    This is G here.
- **The census itself:**
  - OEIS A386200: PSL(2, ℤ) classes of trace n, counted as cyclic words in the matrices this repository calls L and R;
  - Latimer–MacDuffee, read in K. Conrad's notes, Theorem 2.1 and Remark 2.7: same-trace classes are ideal classes. These are
    what an S2 stratum holds.
  - Guéritaud, Geom. Topol. 10 (2006) 1239, Proposition 2.1. His R is this repository's L.
- **Forking paths:**
  - Gelman & Loken, *The garden of forking paths* (2013), §1.2 and §§4.3–4.4;
  - Nosek et al., PNAS 115 (2018) 2600, the abstract: preregistration on data that already exist. Main's census exists, and §2
    is the remedy.
- **Not opened, and cited only through the sources above:** Fox 1956, Latimer–MacDuffee 1933, Friedman–Washington 1989, Davies
  1987, Sarnak 1982 (full text).

**Standing (planned):** EXTENDS. The bar assembles the record's pieces into one rule for positives on generated states. The null
model on generated states, the manifold unit and the strata tests have no counterpart in the sweep.

## 6. What the sealed run reads

### 6.1 Decided at design time (computed as checks)

- **D1** (main's B1442 lemma). No level-manifold of exponent at most 2 carries a background: three own-level manifolds (F5).
- **D2** (main B1434 (a)). The root's own level is silent: torsion 1, no character.
- **D3 (the root's tower is REPRODUCED at k = 3 to 7).** Wherever the root's level fires and two or more other level-manifolds
  exist at that k, half or more of them fire.
  - This is decided by main's level table:
    - k = 3: 32 records are 32 level-manifolds, and 25 fire;
    - k = 4: all 10 records fire;
    - k = 5: 3 of 4 fire;
    - k = 6 and 7 have fewer than two others.
  - Main argued it at k = 3 (B1434 (b) and §3).
  - k = 2 is reported, not decided.
- **D4 (the record's positives, graded by §3).**
  - **The root's tower at k ≥ 3** (B1427, B1434, B1439): the root is chosen by a fixed rule (T-ROOT), and the positive is
    REPRODUCED (D3).
  - **m369 and s639** (B1434), **the 87 own-level carrier manifolds** and **the fourteen complete states** (B1439) were all found
    by scanning. Presented as evidence that the genesis selects them, each would be FITTED. R4 gives the chance that a scan finds
    a carrier at the census rate.
  - Main's fences claim none of them ("nothing in this census selects m369 or s639", B1434:75; "nothing selects a state",
    B1439:98). The census is the frame's base rate.
  - **The harmonic frame's counts** (B1509–B1515 on m004's family; the audit lane's R40 on m010) are UNJUDGED: the frame has not
    been run on a population.
- **D5.** The base rates by unit (R1), the length table (R2), the level-manifold table (R3), the scan chances (R4), amphichirality
  (R5) and the bar's strata table (R6) are readings, not tests.

### 6.2 Sealed predictions (open)

| | prediction | prior |
|---|---|---|
| P1 | the own-level hit is **not determined by the fibre torsion with the monodromy's action**: some S2 stratum holds a firing and a silent manifold | 85% |
| P2 | nor by G, sign and symmetry order: some S3 stratum is mixed | 75% |
| P3 | **G predicts the hit beyond chance**: the leave-one-out AUC under S1 beats its permutation null (hits permuted across the 536 manifolds, 2 000 permutations), Šidák-corrected p < 0.01 | 85% |
| P4 | **reversal symmetry predicts the hit beyond G and sign**: the Mantel–Haenszel odds ratio given S2 exceeds 1, and the conditional permutation's one-sided p (the reversal class permuted inside each S2 stratum, 20 000 permutations), Šidák-corrected, is below 0.01 | 45% |

**On the priors.**
- P1: B1438 Theorem D puts the word, letter by letter, into every slope. Two words with one G and one sign are different
  same-trace classes (F2; Latimer–MacDuffee).
- P3 is near-implied by main's disclosed enrichments (3 | torsion; non-cyclic). It is labelled so: per PRACTICES, a right answer
  here measures the record, not the seat.
- P4: the unconditional split (79 of 314 against 8 of 222) is disclosed. Only 32 S2 strata, holding 70 manifolds, contain both
  classes (F6), so the test may lack the power to see a real effect.

**The trials factor.** Two tests carry a significance claim: T2's permutation test and T3's conditional test. Each p is
Šidák-corrected for two (1 − (1 − p)²) and read against B614's gate, 0.01. T1 is exact. The readings and the decided items carry
no significance claim. The permutation seed is 12345.

**Reading rules.**
- `bar_run.py`'s `read()` reads P1–P4 mechanically.
- If **P1 fails**, the own-level hit is a function of (G, ε) on the census. Main's L229 (i) then has a criterion, stated by its
  strata. That is the headline.
- If **P1 holds**, no criterion in the fibre torsion, as a group with the monodromy's action, decides own-level firing on the
  census. Main's "no criterion found" becomes "none exists" for every such criterion. The mixed strata are the witnesses, listed.
- **P3 and P4** say what the null model must condition on. The bar's strata (§3, step 3) are fixed and do not move with them.
- If C1, C2a, C3, C4 or C5 fails, nothing is read and the failure is logged (NO NEGATIVE FROM A BUG). A failed prediction is not a
  failed control.

## 7. The instruments

- **Design time** (disclosed in §2):
  - `verification/covariates.py`, `level_covariates.py` and `design_checks.py`;
  - their records `covariates.json`, `level_covariates.json` and `design_checks.json`.
- **The instrument:** `verification/null_model.py`, with its self-test.
- **The sealed run:** `verification/bar_run.py --write` → `verification/bar_run.json`. This includes the dry run (C5) and the
  controls before any test.
- **Main's records, quoted:** `verification/main_B1439_firing_own_states.json` and `verification/main_B1439_levels.json`, each
  with its source and sha.

## 8. What this arc will and will not claim

- **It will not claim:**
  - that any state is physical, or any physics;
  - that the bar is complete for other frames (it is run here on one frame);
  - anything about a frame without a population run.
- **The bar is this seat's proposal; the owner may amend it.** GENESIS GAP4 and FK9 point to it after the run. A frame's later
  population run fills in its strata.
- **0 of 19 stays 0.**
