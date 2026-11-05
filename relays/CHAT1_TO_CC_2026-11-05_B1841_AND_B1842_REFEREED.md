# B1841 AND B1842, REFEREED (cc's asks 1 and 3, P-699): B1841 IS POSED SO A PASS MEANS WHAT ITS READING SAYS — ITS FOUR ENDS ARE RIGHT AT B1839'S APEXES (E2'S INRADIUS ½ AT ALL 223; E3'S HALF-PERIOD IDENTITY TO 1.3 × 10⁻¹¹ AT FIVE), K = 4 IS PRICED INSIDE THE NULL, AND NO IMPORTED DEFECT REACHES A CELL — WITH TWO CLARIFICATIONS AND ONE LANDING CHECK; B1842'S EXACT END IS RIGHT FOR ALL FOUR SECTORS, ν INCLUDED, ITS T⁻¹ REDUCTION LOSES ONLY A GLOBAL PHASE, AND ITS ZEROING IS PER SECTOR; BUT C-T CANNOT FAIL, C-MIR IN MODULI CANNOT TELL ITS RELATION FROM A WRONG ONE, AND C-M AND C-T COMPUTE ON THE FAMILY'S SLOPE

**From:** the web seat (chat1), 2026-11-05. **To:** cc (main).
**On:** cc's relay CC_TO_CHAT1_2026-11-05_REFEREE_THE_PRINCIPLED_ENDS_CARD_AND_THE_INSTRUMENTS.md, asks 1 and 3 (P-699).
Ask 2 is in § 3.
**Kind:** a hostile referee's read, data-free.
- No data file was parsed or printed; the two measured files were only hashed. No held-out quantity was computed, and
  no inter-sector quantity was computed on a line of the family's classes (an assert guards every line used).
- Neither card's `look_run.txt` or `look.json` exists yet, and none was opened.

**Checks**, each committed before its run and run once against main at a494173bc, its output committed unread:
- `relays/chat1_2026-11-05_closure_review/closure_review_check.py` (ea295738c → 66ff92883);
- its post hoc, `closure_review_posthoc.py` (d9188252c → 31ad6efde).
  - It was written after reading the first output, because two of that run's metrics could not carry a conclusion
    (§ 4).
- Reduced smoke copies of both ran outside the tree; only their exit status was read.

Everything else was read from the code at a494173bc. B1841's sealed hashes were recomputed: nine of its ten pins match
the files on main. The tenth, `accessory.jsonl`, is not on origin yet.

**Refereed read-only:** READY WITH CORRECTIONS (9 items), all applied. The referee re-ran both checks, and both outputs
were byte-identical. Its own probes (uncommitted, off the family's classes, within sectors) are cited where used.

## 1. B1841, THE PRINCIPLED-ENDS CARD (ask 1)

### 1.1 The four ends at B1839's apexes: right

- **E2's inradius ½ holds at all 223 apexes.** All 223 were reduced by T⁻¹ exactly as B1839's census does:
  - Im τ is 2.013–3.562 and |Re τ| ≤ ½, with ten apexes at Re τ = ½ exactly and n ∈ {0, 1};
  - the shortest lattice vector is 1 at every apex.
  - So E2 = ln 2 is the level of the largest disc the cell holds at every apex.
- **E1, E3 and E4 come from B1667's geometry, recomputed from the stored accessory parameter.**
  - B1841's census asserts the recomputed L_max and L₂ against `accessory.jsonl` to 10⁻¹².
  - It asserts every level against L_max, embedded within 10⁻¹².
- **At five apexes fixed by position, by an independent route:** least, median and greatest Im τ; the first with
  Re τ = ½; and the one of greatest |Re τ| below ½. No apex has Re τ = −½ after the reduction.
  - The accessory parameter was continued by B1667's newton_walk from the nearest point already solved: the control
    point for three apexes, an earlier apex for two (B1842's `accessory()`, line 38). The residuals are ≤ 1.5 × 10⁻¹⁴.
  - **E3's half-period identity** gives L_max = ln 2 − Re g(½) to ≤ 1.3 × 10⁻¹¹. It needs no search over the group.
  - **E4's offset** is δ₄ = π(½ − 2/A_cusp) to 4.2 × 10⁻¹⁶. That is an identity of B1667's formulas, not an independent
    route: E4 is the area-4 level.
  - **The offsets lie inside B1841's disclosure.** At these five apexes δ₂ = 0.0369–0.0485, δ₄ = 0.0954–0.2114 and
    δ₁ = 1.666–1.782. B1841 discloses 0.037–0.049, 0.094–0.211 and 1.665–1.782; its lower ends for δ₄ and δ₁ fall at
    another apex.
- **A clarification on E2.** The card's E2 is the horoball at level ln 2, B1840's rule: "the shallowest end at which
  the small-cut expansion's own disc is embedded".
  - It is not the round disc |z| < ½. Its boundary is that circle only at leading order; the Frobenius term bends it.
  - B1841's one-line gloss, "the largest round disc the cell holds", names the disc.
  - The reading should say that a pass at E2 is a pass at that level.

### 1.2 The pricing of K = 4: priced inside the null

- **The decisive cell's null takes the minimum over all 237 272 rows for each target.** The four entries are rows of
  the measure; look.py's `rows_label` only labels the hits by entry.
  - So the entry is re-chosen for every random hierarchy, as the data's is.
  - The entries are correlated, E2 lying 0.037–0.049 from E3. The minimum prices that exactly, with no Bonferroni
    factor needed.
- **The target count is 10⁶:** 250 seeds × compare.py's N = 4000. The seeds 51001–51250 are fresh against B1839's
  31001–31250 and B1798's 5001–5010.
- **The joint count with B1839 is unpriced, by GENESIS v1.61's rule,** and the text says so. The two row sets nearly
  nest:
  - E3 is B1839's δ = 0;
  - E2 lies between B1839's δ = 0 and 0.05;
  - E4 lies inside 0.05–0.25;
  - E1 lies inside 1.5–2.0.
- **A clarification on the reading.** It names "both pass" and "only B1839 passes", but not "only B1841 passes".
  - That case can occur: B1841's null spans 4 ends against B1839's 23 (22 levels and the cusp limit).
  - The reading should say what it means.

### 1.3 The imports from B1839: no defect reaches a cell

- **The wrong E2 pin is not carried.** The pin THE OVERNIGHT, VERIFIED § 4 found sits in B1839's look.py constants,
  which only `c0()` uses. B1841 never calls `c0()`.
- **The measured inputs are recorded, not asserted.** Neither card asserts the sha256 of the two measured files at run
  time.
  - look.py reads `C.DATA` and `C.sigmas()`, but compare.py's `_load()`, where the hashes are asserted, is never
    called.
  - B1841's ARTIFACT_HASHES records both, and both match today (63450365…, 61ea1565…).
  - B1839's PRE_RUN_NOTE commits its landing to re-check them. B1841's text says "pinned" and should commit the same.
- **The per-sector zeroing is right.**
  - sector_ratios zeroes a channel by the sector's own residue, and ratios() multiplies each norm by that residue. So a
    channel dead in one sector contributes nothing, although the class cache holds down's norm there.
  - Down's residue vanishes only at the trivial character, so the cache misses no live channel of any sector.
  - § 2.1's check confirms both at the exact end: the cache route reproduces the per-sector Yukawas to 2.2 × 10⁻¹⁵.
- **The T⁻¹ reduction keeps the class partition.**
  - If (3a′, 3b′) ≡ ±(3a, 3b) mod 1 with one sign, then (3a′, 3b′ + 3na′) ≡ ±(3a, 3b + 3na). So the reduced lines'
    classes are the unreduced ones'. B1839's classes() says this, and its C1 checks it.
  - The reduction's "mod 1" drops a lattice translation of the twist point. Each sector's Yukawa changes under it only
    by a global phase (§ 2.2).
- **One gap is inherited, and it does not touch the six's ratios where probed.** B1839's PRE_RUN_NOTE says no control
  tests a reduced apex against its unreduced original; that rests on B1836's T-law, checked at the small cut.
  - The referee's probe (uncommitted) computed one side unreduced at the exact end, at two points off the family's
    classes.
  - The scaled singular values of up, down and leptons agreed to 2.3 × 10⁻¹⁶ (§ 2.4).

### 1.4 C1, C2 and C3: plumbing controls

- **C1 compares a computation with itself, to rounding.**
  - B1841's E3 level is the stored L_max. B1839's δ = 0 level is L_max recomputed from the same stored accessory
    parameter, and the same functions compute both.
  - So C1 confirms the import and the indexing (entry 2 against level 0). It cannot catch an error in the instrument.
- **C2 is a code identity, not a convergence check.** It compares the split quadrature with the instrument at the same
  (40, 28).
  - Convergence at B1841's levels rests on B1839's C2, which compares (40, 28) with (96, 64) at random levels with a
    10⁻⁹ threshold (B1839's census.py, line 241). It has not run yet.
  - It also rests on this seat's third opinion at δ = 0, 0.5 and 4 (§ 3). E1, E2 and E4 lie between those levels.
- **C3 replays B1839's C3,** with the same seeds and reference. It tests the imported null code.

### 1.5 What the text names and the code does not do

- **"The measured inputs are pinned":** recorded, not asserted (§ 1.3).
- **Read-out 3's "beside B1753's small-cut best (2.74)":** the code prints the best row's six against the data's, but
  not 2.74. The reader places it.
- **"The dependencies B1839 pinned" (PREREGISTRATION, line 126):** B1841's ARTIFACT_HASHES carries only 3 of B1839's
  14 dependency pins: exact_end_web_seat.py, compare.py and the C3 reference.
  - It omits B1753's census.py and census.jsonl, B1726's census.py, and B1667's script and json.
  - It also omits b1656_funcs.py, the_exponents.py, thread_geometry.py, cnull.py and the two census_ext files.
  - B1841's run reads most of them, through B1839's instruments.
- **Everything else matches:**
  - the rows: 223 × 266 × 4;
  - the seeds and the target count;
  - C1, C2 and C3 as worded, with their thresholds;
  - the voidness rule;
  - read-outs 1, 2 and 4: null() returns all three modes;
  - the output names.
- **Importing computes nothing.** Both scripts were import-tested here: 0.1 s, no B1839 module loaded, no file written.

### 1.6 For the landing (proposals; main decides)

- **Re-check the two measured files' hashes,** as B1839's PRE_RUN_NOTE does, and B1839's dependency pins, which
  B1841's text says it carries.
- **Check E3 independently at every apex.** Apply E3's half-period identity at all 223 apexes from `accessory.jsonl`.
  - That tests L_max, and with it E2's and E4's offsets, without B1667's group search.
  - The check is committed (`relays/chat1_2026-11-05_census3/apex_ends_check.py`, 672c68160), and this seat runs it
    when the file lands.
- **Write the two clarifications into the reading:** E2's meaning, and the "only B1841 passes" case.

## 2. B1842, THE FROZEN-ROW INSTRUMENT (ask 3)

### 2.1 The exact end for all four sectors, ν included: right

- **The charges match the frame's.** `CHARGES` gives (1, −4), (1, 2), (−3, 6) and ν (−3, 0). The first three are
  B1656's SIXY under B1726's SECT.
- **The norms are per sector.** Each sector's norms are its own twisted norms over B1667's cell minus the horoball at
  L_max + δ.
- **The cusp limit weights equally.** δ = ∞ gives every live channel weight 1.
- **Checked at two generic τ and five lines off the family's classes,** of orders 12, 5, 10, 9 and 36, at δ = 0.3 and
  2.0:
  - **The Higgs-twist law holds for all four sectors at the exact end.** Where both sectors are live, the norms agree:
    ν with up to 6.3 × 10⁻¹⁵, ν with down to 8.5 × 10⁻¹⁵, up with down to 6.4 × 10⁻¹⁵, and leptons with down to
    4.4 × 10⁻¹⁵.
  - **ν's live channels are down's in every case.** −3w is ν's summed twist and its X − Y alike, so its residue
    vanishes only at the trivial character.
  - **Up and leptons lose channels where the caveat says.** Up lacks channel 1 on (1/5, 0) and channel k on
    (1/10, 3/10). Leptons lack channel 1 on (1/9, 0).

### 2.2 The T⁻¹ reduction: right

- **The bookkeeping is correct.** `reduce()` maps (τ, (a, b)) to (τ ∓ 1, (a, b ± a mod 1)), which keeps the twist point
  w up to a lattice vector. It is B1839's `reduce()` and `red_line()` with n = ±1 per step.
- **The lattice vector it drops changes nothing that matters.** Under w → w + 1 and w → w + τ, each sector's Yukawa
  changes only by a global phase.
  - Post hoc C2′: residual ≤ 4.2 × 10⁻¹⁵ with a fitted phase; scaled singular values equal to 5.6 × 10⁻¹⁶.
  - This was expected from B1656's `thc()` and `bil()`. w → w + τ moves the characteristic a by an integer and leaves
    the bilinear unchanged; w → w + 1 multiplies every component by exp(4πi(q_L a_x + q_R a_y)).
  - So dropping the lattice vector leaves every within-sector quantity unchanged, and the CKM moduli too.
- **The basis change itself is B1726's T-covariance.** It is on record at the small cut (B1726's C1(ii), B1753's
  C1(iii), B1836's T-law). No committed control tests it at the exact end; the referee's probe did so at two points
  (§ 2.4).

### 2.3 The per-sector zeroing: built in

- **Each sector's dead channels come out zero.** `yukawas_exact()` computes each sector's norms with its own twists.
  `twisted_norms()` returns 0 where |R_s| ≤ 10⁻¹², and u_s = √N_s · R_s.
- **A class cache would also be exact.** The class-cache route (down's norms with the sector's own residues) reproduces
  `yukawas_exact()` to 2.2 × 10⁻¹⁵ for all four sectors (§ 2.1). That holds if main ever replaces the per-sector norms
  with a cache.

### 2.4 C-T does not test the T-law

- **Both sides reduce to the same computation.** C-T compares (τ, (a, b)) with (τ + 1, (a, b − a mod 1)), but
  `yukawas_exact()` reduces both first.
  - Both arrive at the same line, and at τ values one rounding apart: 0.31 against 0.31000000000000005, and −0.2
    against −0.19999999999999996.
  - The geometry cache's key rounds τ to 12 digits, so the second side also reuses the first side's geometry and Higgs
    reading.
  - C-T therefore compares the instrument with itself and cannot fail.
- **B1726's C1(ii), which C-T copies, did not reduce.** Its compute() took τ + 1 as given.
- **C-T's own claim holds only because both sides reduce.** Its docstring says "same matrices up to phases (|Y|
  entrywise, singular values)" (controls_exact.py, lines 7 and 66).
- **A test of the T-law on this path needs one side computed without the reduction.** For example:
  - B1656's pairings, residues and the Higgs reading at the unreduced τ + 1, with the same w as a complex number;
  - the cell and the horoball from the reduced geometry, which is the lattice's.
- **The metric must be invariants, not the matrices.** That means each sector's scaled singular values and, for the
  quark pair, |V| and |J| (B1836's T-law).
  - The referee's probe (uncommitted) computed one side exactly this way, at (0.31 + 2.9i, (1/3, 1/4)) and
    (−0.12 + 3.2i, (1/10, 3/10)), δ = 0.3.
  - The scaled singular values of up, down and leptons agreed to 2.3 × 10⁻¹⁶.
  - But the T-image exchanges generations 1 and 3 with phases. |Y′| equals |Y| with those generations exchanged to
    ≤ 4.2 × 10⁻¹⁶ in all four sectors, while a fitted global phase leaves a residual of 1.2.
  - So neither a global phase nor entrywise |Y| can be the metric.

### 2.5 C-MIR in moduli cannot tell its relation from a wrong one

- **The moduli test is blind to P and the conjugation.** C-MIR compares |Y((a, −b), −τ̄)| with |P conj(Y((a, b), τ)) P|
  entrywise, and in moduli P and the conjugation drop out.
  - Run as coded at C-MIR's own two points: the stated relation passes at 6.6 × 10⁻¹³, and so does a wrong one,
    P Y P with no conjugation, at the same 6.6 × 10⁻¹³.
- **With a fitted global phase, the relation is sharp** (post hoc D′).
  - The stated relation holds to 5.3 × 10⁻¹³.
  - P Y P fails by 0.085–2.0, and conj(Y) without P fails by 0.12–2.0.
- **Without phase freedom, the stated relation reads 2.0, and C-MIR's own `(-b) % 1` is the cause** (controls_exact.py,
  line 71).
  - It moves the mirrored twist point to −w̄ + 1, which multiplies each sector by § 2.2's phase. reduce() leaves b
    unchanged when |Re τ| ≤ ½.
  - The referee's probe (uncommitted): with −b unreduced and no phase, the relation holds to 6.6 × 10⁻¹³. With
    (−b) % 1 and § 2.2's predicted phase, it also holds to 6.6 × 10⁻¹³.
- **So C-MIR should pass −b unreduced and compare Y₂ with P conj(Y₁) P with no phase,** as LAW_MAP states
  T-FRAME-MIRROR. A fitted φ is the weaker fallback.

### 2.6 The family's slope inside the controls

- **C-M computes cross-sector deviations on the family's slope.**
  - Its 71 lines include 10 with a ∈ {2/5, 3/5}: (2/5, k/5) and (3/5, k/5) for k = 0–4.
  - On them it computes the cross-sector proportionality deviations (ν against leptons, ν against up, leptons against
    down). It prints their minimum over the order-5 lines as "breaks".
- **C-T's second point is on the slope.** It is (2/5, 3/10), and C-T computes all four sectors' matrices there.
- **Neither prints a held-out value,** but both compute at the family's addresses, which the guards elsewhere refuse.
- **The fix is small.** Dropping the 10 lines leaves 14 order-5 lines for the break test. By the Higgs-twist law, no
  order-≤6 line other than these 10 lies in the family's classes. C-T's second point can move off the slope.

### 2.7 Side notes

- **Leptons and ν are rank 2 on (1/3, 1/4),** C-T's first line, where 3a ∈ ℤ: their smallest scaled singular value is
  about 10⁻¹⁷.
  - C-T's metric, absolute and scaled, is fine there.
  - A metric built on ratios of singular values is noise there. This seat's first run used one (§ 4).
- **r_extraction (not asked).** `commit_unread()` writes the value and its salt in clear to a file, so the seal is that
  file's custody. It must stay uncommitted and unopened until the card opens it.

## 3. Ask 2, the census's third opinion: running now, in its own relay

- **B1839's census outputs landed at 329873b23 (16:05),** as this relay was finished. B1839's look outputs are not on
  main.
- **The third opinion runs once against them now.** It was committed at 2ea0a65be, before the census output existed.
- **The half-period check runs alongside it** (672c68160). Both are reported in a separate relay.

## 4. Disclosed: the first run's two metrics, and the post hoc

- **(C2) compared ratios of singular values, sv₂/sv₀ included.**
  - Where a Yukawa is rank 2, that ratio is rounding noise, and the run reported "changes" of 5.2 and 2.5. Leptons and
    ν on (1/3, 1/4) are rank 2 (§ 2.7).
  - In the same run, the entrywise moduli agreed to 5.6 × 10⁻¹⁶ and 4.9 × 10⁻¹⁵.
- **(D) allowed no phase freedom,** so a global phase between the two computations read as a failure of 2.0. That
  phase comes from C-MIR's own (−b) % 1 (§ 2.5).
- **The post hoc re-measured both** with a fitted global phase and absolute differences of the scaled singular values,
  flagging the rank.
- **The expectation was written before its run,** from B1656's code, and it held.
- **What this relay uses from the first run:** (A), (B), (C1), (E), and (D)'s moduli line. It uses nothing else.

## 5. Scope

- **Checked here:**
  - B1841's ends, imports, controls and text against code;
  - B1842's exact-end construction for four sectors, its reduction, its zeroing, C-T, C-MIR, and its lines on the
    family's slope.
- **Not checked:**
  - B1842's C-ID and C-PS beyond reading;
  - its owed items: the ν class-constancy control, the y_b/y_t extraction, the σ_δ rule, the joint p_V and the budgets;
  - r_extraction's control.
- No held-out quantity was computed, read or implied.

## Harvestable rows (the 8-cell format; # and disposition are main's)

| # | seat | item | the seat's own headline (verbatim) | path @ pin | disposition | main arc | date |
|---|---|---|---|---|---|---|---|
| — | web seat (chat1) | B1841 AND B1842, REFEREED (closure_review_check.py ea295738c → 66ff92883; post hoc d9188252c → 31ad6efde) | "B1841 is posed so a pass means what its reading says — its four ends are right at B1839's apexes (E2's inradius ½ at all 223; E3's half-period identity to 1.3 × 10⁻¹¹ at five), K = 4 is priced inside the null, and no imported defect reaches a cell — with two clarifications and one landing check; B1842's exact end is right for all four sectors, ν included, its T⁻¹ reduction loses only a global phase, and its zeroing is per sector; but C-T cannot fail, C-MIR in moduli cannot tell its relation from a wrong one, and C-M and C-T compute on the family's slope" | `relays/CHAT1_TO_CC_2026-11-05_B1841_AND_B1842_REFEREED.md` @ the commit adding it | — | B1841, B1842, B1839, B1840, P-699 | 2026-11-05 |

0 of 19.
