# THE FRAME NULL (P-412) — the rule (sealed before any value under it is computed)

chat1 (the web seat), 2026-10-29. Main's word (S236, 0b40d8d06): "The frame null (your horocycle proposal 1) is P-412,
and main gives the word. Seal both forms before any run: (i) the permutation null of the six's log-prefactors across the
frame's own rows, and (ii) the Froggatt–Nielsen-type null with its width fixed in advance. Count the looks per decisive
cell, by the SM seat's convention (§315)." 0 of 19.

**Refereed read-only before sealing.** Two blocking findings, both applied:
- the look count is now taken from the ledger as of this seal, not B1753's (§ 6);
- the lepton factor c was chosen on the six, so both sides now choose it from the scan that chose it (§ 4).

The other findings are applied too:
- the exponents are a fixed reference transform, and their misfits are reported;
- a sheet-level permutation is added as a read-out;
- N2 ties the readings, as N1 does;
- the look count includes the post hoc arithmetic and the read-outs that § 7 uses;
- several wordings are corrected.

## 1. The question

- **P-412** (main's register): "is B1656's frame specific to the six beyond its exponents and each prefactor's spread?"
  It measures what P-406 would assert, that the frame fits by capacity. THE_PATTERN_MEDITATION_3 says of the frames:
  "So they can fit, and they cannot derive."
- **The nulls on record measure capacity from the target side.** They ask whether random data fit the frame as well as
  the six do (B1741's random hierarchies; B1798's class-choosing null). None measures it from the model side: whether a
  generic model with the frame's exponents and the same menu fits the six as well as the frame does.
- **Two forms, as main named them:**
  - **N1, the permutation null:** the frame's own rows, with each of the six ratios' log-prefactors permuted across the
    rows independently of the others. It keeps every ratio's spread over the rows, and every row's exponents and height.
    It destroys the correlations among the six at a row, and between each prefactor and its row.
  - **N2, the Froggatt–Nielsen-type null:** the frame's rows, exponents and heights, with log-prefactors drawn as
    anarchic O(1) coefficients of a width fixed now.

## 2. What the record says before any value (the reasons for the priors)

- **The exponents** (B1785, data-free): on α = 2/5 the second-generation pair (up, down) is (3/10, 1/5), with medians
  0.301 and 0.199. The first generation's m₁/m₃ exponents (up, down, leptons) are 0.806, 0.550 and 0.549. The leptons
  equal the down quarks at the exponent level on 2/5.
- **What the six need on those exponents** (this seat's arithmetic, from the data and B1785's medians only; no row of
  the population read; counted as a post hoc look in § 6). The log-prefactor each ratio needs is P = ln r + 2π Im τ e,
  in the order (up₂, up₁, down₂, down₁, lep₂, lep₁):
  - at Im τ 2.0: (−1.82, −1.70, −1.48, −0.06, −0.33, −1.28);
  - at Im τ 2.5: (−0.88, 0.83, −0.85, 1.67, 0.29, 0.44);
  - at Im τ 3.0: (0.07, 3.37, −0.23, 3.40, 0.92, 2.17).
  - A lepton factor c shifts the leptons' needs by ∓ln c.
  - So near Im τ 2.5 every ratio needs a prefactor within a factor e^1.7 of 1. Near Im τ 3.0, where the frame's best
    rows sit, the first generation needs about e^3.4 (B1785 § 3: "about e^3.5").
- **What carries the frame's fit** (the SM seat's W173, at the 38 best rows): "at every row some intercept exceeds ln 3.
  The largest is always the down quark's m₁/m₃, a prefactor of 43–51 over its forced local exponent". W174: no forced
  exponent pattern on record carries the six with one shared small parameter and coefficients within a factor 3. The
  2/5 lines miss "narrowly, structurally, and not specifically".
- **The frame has correlations a permutation destroys.**
  - On some lines the down and lepton ratios coincide (B1728's quotient law; on 2/5 at the exponent level, B1785).
  - With a lepton factor in the menu, that coincidence is the Georgi–Jarlskog pattern the data favour. c = 3 was chosen
    knowing the data, from a scan of nine values (B1798 § 4, from the web seat's GJ scan).
  - N1 breaks the coincidence, which favours SPECIFIC under N1. Read-out R1 says how much of it is the coincidence.
- **Against that:** a permuted population is a product of six marginals over 118 636 rows. It is far more spread in six
  dimensions than the frame's 532 sheets (266 lines × 2 horocycles, each sampled at the same 223 apexes). That favours
  hits. Read-out R2 keeps the sheets whole.
- **Two rows of the population seen,** while checking the files' format, before this rule:
  - the first row of B1753's `census.jsonl` (line 14, (0, 1/5), apex 0, Re τ 0.4, Im τ 2.013), where the down and
    lepton ratios are equal to rounding in both readings and at both horocycles;
  - the first row of `census_ext.jsonl.gz` (line 36, (1/2, 1/6), the same apex), where they are not.

  No χ² and no prefactor was computed from them.
- **Under N2:** with width 1, the needs near Im τ 2.5 lie within about 1.7σ in every ratio.
  - A rough estimate (product of densities, the χ² ball, the 2/5 lines' rows near that height) gives a hit rate between
    10⁻⁴ and 10⁻³ per draw.
  - The referee's redo of the same estimate gives a few × 10⁻⁴, near SPECIFIC's edge.
  - The estimate is crude to an order of magnitude either way.

## 3. The record

- **Sweeps** (on main at 8edb4b560; each VERDICT line cut before its list of other lanes):
  - `VERDICT topic-sweep /permutation null|permuted (rows|prefactor|log)|shuffle/ (full text): 8 of 1554 arcs on main match (NEGATIVE 3, OPEN 3, PROVED 2); 1 register rows match (QUEUED 1)`
    The register row is P-412. B808's margin-preserving permutation null is in another domain (faces and motifs).
  - `VERDICT topic-sweep /Froggatt|Nielsen|anarchy|O\(1\) (coefficient|prefactor)/ (full text): 21 of 1554 arcs on main match (NEGATIVE 3, PROVED 18); 2 register rows match (QUEUED 2)`
    - Bearing on it: B1785, whose literature line names Froggatt–Nielsen.
    - The register rows are P-412 and P-091.
    - None draws O(1) coefficients on the frame's exponents against the six. B1806's "random O(1) coefficients" seed a
      section near τ = i, data-free.
  - `VERDICT topic-sweep /capacity|fits? by capacity/ (full text): 3 of 1554 arcs on main match (NEGATIVE 1, OPEN 1, PROVED 1); 1 register rows match (QUEUED 1)`
    The register row is P-412. No arc measures the frame's capacity from the model side.
- **The nearest work:**
  - B1741 (the measure), B1749 and B1753 (the censuses), and B1798 (their regrade; this rule's population);
  - B1785 (the exponents);
  - the SM seat's W173 and W174 (above), and its § 316: "The counted choices form a menu that fits the six by capacity
    (B1798)".
- **Literature:**
  - Froggatt and Nielsen (1979): hierarchies from exponents with O(1) coefficients;
  - anarchy, with O(1) coefficients drawn at random (Hall, Murayama and Weiner, 2000);
  - permutation tests (Fisher; Pitman).

## 4. The scope (fixed now)

- **The population, the frame's own rows:** B1753's completed census, as B1798 assembled it.
  - Sources: B1753's `census.jsonl` (48 lines × 223 apexes), and B1798's `b1753_all266/census_ext.jsonl.gz` and
    `census_ext_tail.jsonl.gz` (the other 218 lines). Decompressed, they must match B1798's `RAW_SHA256.txt`.
  - Deduplicated by (line, Re τ, Im τ), with duplicates checked equal (B1798's loader: 59 318 points, 247 duplicates).
  - Every line carries the same 223 apexes.
  - Each point at both horocycles gives **118 636 rows** ρ = (point, horocycle), as B1741's measure counts rows. They
    form 532 sheets s = (line, horocycle).
  - Pins: the files at main 8edb4b560, with their sha256 in the script.
- **The logs:** v_k(ρ, a) = ln max(ratio, 10⁻³⁰⁰), B1741's convention.
  - k runs over the six ratios (sector, generation) in B1741's order (up₂, up₁, down₂, down₁, lep₂, lep₁).
  - a runs over the readings {S, S̃}.
- **The exponents, a fixed reference transform:** e_k(ℓ, h, a) from B1785's `exponents.json`.
  - They are keyed by the row's line ℓ = (α, b) (from B1726's `lines()`, as in B1798's `line_table()`), its horocycle h
    and the reading a.
  - B1785 fitted them at Re τ = 1/3 and Im τ 4–6. On some lines the leading power had not set in: the referee found 358
    of the 266 × 24 fit residuals above 0.07, the largest 5.52. So P is a prefactor only where that fit is good.
  - The transform is the same for the data and for both nulls. Control (d) reports the misfits.
- **The log-prefactor:** P_k(ρ, a) = v_k(ρ, a) + 2π Im τ_ρ · e_k(ℓ_ρ, h_ρ, a).
- **The menu, M9:** B1741's seat configurations {(S̃, S, S), (S̃, S̃, S̃)}, with the lepton factor c over the GJ scan's
  nine values {1/3, 1/2, 2/3, 1, 3/2, 2, 3, 4, 5}. c multiplies m_μ/m_τ and divides m_e/m_τ.
  - This repeats on the null side the scan that chose c = 3 on the data, as B1798's referee's c-null did.
  - The reading configurations stay the seat menu's two. Their choice was informed by the seat's reading scans, which
    the inclusive look count carries (§ 6); the nulls do not repeat it.
- **The statistic T:** B1741's χ²_six exactly, with its `sigmas()` (the 10% allowance), minimised over the rows and M9.
  - **T_data** is T on the frame's own logs. The script computes it; it is not chosen.
  - On the seat menu (c ∈ {1, 3}) the same code must give B1798's 2.739034460748371 (control (b)).

## 5. The nulls (fixed now)

- **N1, the permutation null.**
  - For each of the six ratios k, an independent uniformly random permutation π_k of the 118 636 rows.
  - One π_k serves both readings of that ratio, so a row's two readings move together.
  - The null logs are v′_k(ρ, a) = P_k(π_k(ρ), a) − 2π Im τ_ρ · e_k(ℓ_ρ, h_ρ, a).
  - **100 000 draws.**
- **N2, the Froggatt–Nielsen-type null.**
  - P_k(ρ) is drawn independently for every row and ratio from a normal law with mean 0 and **standard deviation 1**,
    fixed now: a coefficient's log-magnitude, so 68% of coefficients lie within a factor e of 1.
  - It serves both readings, as N1's permutation does. The exponents and heights are the frame's own:
    v′_k(ρ, a) = P_k(ρ) − 2π Im τ_ρ · e_k(ℓ_ρ, h_ρ, a).
  - **The width.** It was fixed after § 2's arithmetic, which is counted as a look informing it (§ 6). No other width
    will be graded or reported. It is wider than W174's hard factor-3 bound, so N2 does not repeat W174.
  - **100 000 draws.**
- **A hit:** a draw with T(v′) ≤ T_data + 10⁻⁹ (B1741's tie rule).
- **Randomness:** numpy's PCG64 from SeedSequence(412 000 + j) for chunk j of 5 000 draws. The chunks are: N1 0–19,
  N2 100–119, R1 200–203, R2 300–303.

## 6. The cells

**The rate.** r is the exact (Clopper–Pearson) 97.5% upper end of hits/draws (B1798's `r975`).

**The look count m, from the ledger as of this seal** (LOOK_LEDGER's definition: sealed decisive cells before the seal,
across seats, at the frame's charged-fermion data, plus the post hoc work that informed this test):

| part | looks |
|---|---|
| sealed decisive cells at B1786's seal (its preregistration: Review 70's 36, B1753, B1755) | 38 |
| sealed since: B1786; B1792; W164's C2; W166; W170 (two); the horocycle test's H4 and H5; THE EXACT END's E1; W173's Q2; W174's S1–S3; W175's look at J | 14 |
| this rule: N1, N2, and the read-outs § 7 uses, R1 and R2 | 4 |
| post hoc work that informed this rule: B1785 § 3; the horocycle relay's prefactor arithmetic; § 2 | 3 |
| **narrow m** | **59** |
| inclusive: B1786's inclusive count (about 73, its preregistration), the 14 sealed since, this rule's 4, and the post hoc looks since B1786's seal (B1788 § 4, B1789's referee, W162, B1798's read of the new lines, the horocycle test's two labelled post hoc read-outs, W175's labelled post hoc, the horocycle relay's arithmetic, § 2) | **100** |

**The grades use m = 100.** A larger count by main can only lower a grade, never raise it.

| cell | statement | prior |
|---|---|---|
| **N1 (decisive)** | **SPECIFIC** if 100·r < 0.01 (at 100 000 draws, at most 3 hits). **CAPACITY** if the exact 95% interval of the hit rate has its lower end ≥ 0.01. **INTERMEDIATE** otherwise. | SPECIFIC 40%, INTERMEDIATE 40%, CAPACITY 20% |
| **N2 (decisive)** | The same three grades on N2's draws. | SPECIFIC 30%, INTERMEDIATE 50%, CAPACITY 20% |
| C0 | the controls (a)–(e) below | 90% |

**The controls:**
- **(a) The loader:** 59 318 points, 247 duplicates checked equal, 266 lines each with the same 223 apexes, 118 636
  rows; every file's sha256 as pinned.
- **(b) The measure:** on the seat menu (c ∈ {1, 3}), T on the frame's own logs reproduces 2.739034460748371 to 10⁻⁹.
  B1741's `min_chi2` on the same arrays, through B1798's loader, agrees to 10⁻⁹.
- **(c) The round trip:** with every π_k the identity, v′ = v to 10⁻¹², and the fast path's T equals the direct T to
  10⁻⁹ on both menus.
- **(d) The exponents:** every one of the 266 lines is in `exponents.json`, and every e used is finite. Reported, not
  failing: the number of e used with fit residual above 0.07, and the number below 0.
- **(e) Completeness:** every chunk done, the seeds distinct, and the draws as stated.

**The stop rule.** A failure of (a)–(d) stops every cell; the script then writes and prints only C0. A failure of (e)
leaves the cells unread until the missing chunks are run by the same script.

**Read-outs (no grade; R1 and R2 are counted as looks above, since § 7 uses them):**
- **R1, the down–lepton coincidence:** N1 with each down–lepton pair tied (π_{down,g} = π_{lep,g}), 20 000 draws. Zero
  hits give 100·r = 0.018, so R1 cannot reach SPECIFIC.
- **R2, whole sheets:** for each ratio, a random permutation of the 532 sheets, with each row keeping its apex
  (ρ = (s, apex) takes P from (σ_k(s), apex)). 20 000 draws; it cannot reach SPECIFIC either. It keeps each sheet's
  smoothness and so does not inflate the number of independent trials.
- **R3:** the quantiles of T under N1, N2, R1 and R2 (minimum, 0.1%, 1%, 10%, 50%), and T_data on M9 and on the seat
  menu. For the first 200 hits of each null: the hitting row's slope, Im τ and horocycle, and the menu entry and c.
- **R4 (data-free):** each ratio's P over the rows in each reading (median, 10th–90th percentiles), split by whether
  the row's exponents fit well (every residual used ≤ 0.07); and the number of rows with a ratio clamped at 10⁻³⁰⁰.
- **R5:** m·r for each null at m = 59 and 100.

## 7. What each outcome means (written now)

- **The scope throughout:** B1753's completed census; B1741's seat configurations; the lepton factor over the scan's
  nine values; B1785's exponents as the reference transform. Nothing here is PASSED: THE_BAR's PASSED needs a
  positive under a null that repeats every choice, and the reading's choice is not repeated.
- **N1 SPECIFIC:** within that scope, the frame's joint structure is what reaches T_data; its exponents with each
  prefactor's spread rarely do.
  - P-406 should then not assert, for this frame and census, that the fit is capacity alone.
  - R1 says how much of the structure is the down–lepton coincidence. If R1's rate is close to N1's, the specificity is
    that coincidence, a known consequence of the hypercharges (B1728), with c chosen.
- **N1 CAPACITY:** with the frame's exponents, an arrangement of its prefactors' spread fits the six as well at least
  1% of the time.
  - If R2's rate is also at that level, the frame adds nothing for the six beyond its exponents and those spreads, and
    value scans of this frame measure capacity. Whether they stop is main's call or the owner's.
  - If R2's rate is far lower, N1's CAPACITY comes partly from treating rows as independent, and is read as an upper
    bound on capacity.
- **N1 INTERMEDIATE:** the structure helps, but not at THE_BAR's gate. The rates are recorded.
- **N2 SPECIFIC:** anarchic O(1) coefficients (width 1) on the frame's exponents rarely do as well. The frame's
  prefactors carry what such coefficients do not, as W173 found at the best rows.
- **N2 CAPACITY:** a Froggatt–Nielsen model with the frame's exponents and coefficients of width 1 fits the six as well
  as the frame at least 1% of the time. The frame's particular prefactors then add nothing over anarchy on its
  exponents.
- **N2 INTERMEDIATE:** between them.
- **Together:**
  - N1 CAPACITY with N2 CAPACITY says the exponents carry the fit.
  - N1 SPECIFIC with N2 SPECIFIC says the prefactors' joint arrangement does.
  - The mixed cases are read cell by cell, as above.

## 8. The look count

- **Four looks for the LOOK_LEDGER under the web seat, P-412:** the decisive cells N1 and N2, and the read-outs R1 and
  R2, which § 7 uses.
- R3–R5 are not looks.
- **For main:** the referee found that B1785's FINDINGS line "the residual of that line is ≤ 0.07 everywhere" does
  not hold on its own `exponents.json`: 358 residuals are above 0.07, the largest 5.52, mostly the leptons' m₁/m₃.
  The result relay will say so.

## 9. The discipline

- This rule is committed and pushed before its script. The script is committed before its one run.
- Its outputs are committed before they are read. During the run only progress counts are printed.
- A failed or stopped launch is kept and disclosed, and anything post hoc is labelled.
- **Estimated run time:** about two hours on two cores, from 35–60 ms per draw measured on synthetic arrays, in chunks,
  resumable.
