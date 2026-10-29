# chat1 → cc (main), 2026-10-29: THE SCOREBOARD'S SECOND ROW (P-418) — FR-FIB's two-Higgs branch (TWO_HIGGS; B1742) on the six: a lower χ²_six than the first row (1.19 against 2.74), with more inputs — 23.79 bits (17.40 searched on the data, 6.39 by hand) against 20.03, 3 identification sources against 2 (I-26 through the menu's generation count, this seat's reading), two tagged readings (PF1-W, holomorphy) for H-cov, three unpriced looks against one — and a relation among the six that the data exclude (D = 9, 14σ); 0 of 19 (a proposal; data-free; the menus recomputed from committed files)

chat1 (the web seat), at the owner's word (2026-10-29, "do them all in your order", after this seat proposed this row).
It is the second row of the scoreboard the owner adopted at S254, following THE SCOREBOARD'S FIRST ROW (4a4382949).
Data-free: no measured number is read. 0 of 19.

**How it was done.**
- **The sources:**
  - this seat's sealed TWO_HIGGS (rule 0b192e458; its result, with its "Limits");
  - its menu's rule (ZERO_FREE_FRAME_EXPLORATION §§ 1, 6, 7; B1730);
  - main's B1742, which verified it on main's B1740 instrument;
  - B1809 § 4, B1753, P-351, P-355 and the identification ledger.
- **The entry and its check.** The entry is `relays/chat1_2026-10-29_scoreboard/FR_FIB_TWO_HIGGS_ENTRY.json`; the check
  is `scoreboard_check_2.py`. They were first committed at e7fe5cc3f, before their first run.
  - The check reads main at 187855d48 and this branch at 27f4782fa with `git show`, and writes nothing there.
  - **Recomputed:**
    - the ten lines and the grid, from TWO_HIGGS's own definitions;
    - the 266 lines;
    - the Higgs menu, from its stated rule, with the members parsed from the text;
    - the 27 sector assignments and the 9 searched;
    - the horocycles, c's scan and the readings;
    - the unused UNEARNED rows, the sources and the bits.
  - **Typed:**
    - the end's scale as a binary;
    - the weight's count of seven, as in the first row;
    - the four readings seen, which is quoted.
  - Every other item is checked by quoting its own source.
- **The launches:**
  - **First:** all PASS, output 26a0978ab. It was superseded at the referee and kept as `*_run1.txt`.
  - **The corrections** were committed at 9aff77e4e.
  - **Second:** one quote FAILED, because its source wraps the sentence across lines. It is kept as `*_launch2.txt`
    (53e521f2f).
  - **Third,** after cutting that quote at the line end: exit 0, every check PASS (5e5b855b7). It is kept as
    `*_launch3.txt`.
  - **One provenance was then corrected** before the referee's re-read. TWO_HIGGS (2026-10-23) predates B1748's band
    (2026-10-24), so its Im τ window is the earlier fits' band (P-287's note). Two quotes were added.
  - **Fourth:** exit 0, empty stderr, every check PASS (K1–K5, 51 quotes), with the vector unchanged. Committed unread
    at 896681abf, then read.
- **Refereed read-only before the push: PASS WITH CORRECTIONS.**
  - **Three blocking findings, applied:**
    - the reading was chosen with four readings' results in view, so it is labelled on the data, as the first row labels
      its own;
    - "unpriced looks" now has one definition in both rows;
    - the reading of the comparison over-reached.
  - **Its thirteen other points are applied.**
  - **What it confirmed:**
    - it reproduced the check byte for byte;
    - B1266's own `sources.py` gives these edges.

**Seen first.** `VERDICT topic-sweep /two.higgs|H_u|H_d|two doublets|F_22|F₂₂|zero.free|holomorph/ (full text): 91 of 1561 arcs on main match (NEGATIVE 26, OPEN 7, PROVED 58); 50 register rows match (DONE 28, OWNER 1, QUEUED 21)`
(at 9fa41983c; cut before its list of other lanes).
- **Bearing on it:**
  - B1730 (the zero-free family);
  - B1740 (the non-null Higgs);
  - B1742;
  - B1743 (one free Higgs reaches χ²_nine 17.26, post hoc);
  - B1745 (the frame's locks);
  - B1747 (no one-Higgs direction carries the nine);
  - B1790 (the reading);
  - P-351 ("A READING");
  - P-355 (the lepton–down identity; owed: "a precision six on lines off it").
- No arc or row scores this branch's inputs.

## The frame card (the 2026-10-29 rule, item 1)

- **The frame:** FR-FIB (B1809 § 4).
- **The branch:**
  - H_u for the up quarks and H_d for the down quarks and the leptons;
  - each a zero-free direction F_a = (εθ₂^a, εθ₄^a, iθ₃^a), from the menu {F₆, F₋₂, F₂₂};
  - all read S, with c = 3;
  - on the ten lines (2/5, k/10), at both horocycles.
- **Best row:** χ²_six 1.188 at τ = 0.5625 + 2.6i on (2/5, 1/10), L₂, with H_u = F₆ and H_d = F₂₂ (B1742).
- **𝒦:** the coupling's covariance under Γ₄ (symmetry; B1736); the canonical end radius (canonical construction;
  B1667).
- **Outputs:** the six. This is an accounting, not a test.

## The vector (`scoreboard_check_2_out.txt`), beside the first row

| component | the two-Higgs branch | the first row (H-cov, shared ∂R) |
|---|---|---|
| best χ²_six | 1.188 (L₂, Im τ 2.6) | 2.74 (L_max, Im τ 3.04), at the small-cut norm, which at L_max lies 35–38% above the exact norms (P-421) |
| fitted continuous | 2 (Re τ, Im τ) | 2 |
| continuous, set by hand | 2 (h₀ = 0, M_Z) | 2 |
| discrete | 7: 5 chosen on the data, 2 by hand | 7: 4 on the data, 3 by hand |
| bits on the data / by hand / in all | 17.40 / 6.39 / 23.79 | 15.23 / 4.81 / 20.03 |
| identifications | 7 rows → 3 sources (I-13, I-26, I-31) | 5 rows → 2 sources (I-13, I-31) |
| tagged hypotheses | 5: PF1-W, holomorphy, Λ, the unit, GM5b | 4: H-cov, Λ, the unit, GM5b |
| unpriced looks (searches with the data in view that no bits price) | 3 | 1 |
| D at the best row | 9 (to rounding): a relation of the branch, excluded at 14σ by P-094's 10.58 ± 0.11 | 10.75 (1.6σ): a fitted output, 10.48–11.32 over the rows below the bar (B1753) |
| the nine (census minimum) | χ²_nine 154 | χ²_nine 183 (B1753) |
| bought | 0 of 19 | 0 of 19 |

## The items

**Continuous.**
- **Re τ, Im τ: FITTED** on the rule's grid (8 × 16 per line). ±0.02 moves χ²_six to 1.04–3.43 (B1742). All fourteen rows
  below the bar sit at Im τ 2.6 on L₂.
- **h₀ = 0: CHOSEN, by hand.** S = v · (QI, QJ, QK) is a pure vector.
- **The comparison scale M_Z: CHOSEN, by hand** (P-365).
  - TWO_HIGGS_RESULT's 2 × 10¹⁶ GeV figures (χ²_six 5.8 at the best row; m_c/m_t at 4.8σ) use the Standard Model's
    running.
  - For a holomorphic two-doublet structure the running "depends on tan β". That is a further continuous datum (the
    ratio of the two vevs), which the six at M_Z do not see and this row does not fix.

**Discrete.** Bits are log₂ of the count, computed by the check.

| item | value | label (scope: FR-FIB, this branch) | options | searched | the source's words |
|---|---|---|---|---|---|
| the line | (2/5, 1/10) | CHOSEN, on the data | open | 266 (8.06); 10 in the test | the rule: "This restriction is a choice made after those results" |
| the Higgs of each sector | up F₆; down and leptons F₂₂ | CHOSEN, on the data (the pair); the down = leptons tie by hand | 27 (4.75) | 9 (3.17) | B1742: "the pair is chosen by the data out of six" |
| the reading | S in every sector | CHOSEN, on the data (four seen); the rest of the eight by hand | 8 (3.00) | 4 (2.00) | the rule saw "the readings S, S̃ and the two mixed ones" before fixing "both read S (holomorphic)" |
| c | 3 | CHOSEN, on the data | open | 9 (3.17) | "With c = 1 the six is 3.20: the hand-set factor is essential." |
| the horocycle | L₂ | ADMITTED menu; the pick CHOSEN, on the data | 2 (1.00) | 2 (1.00) | every row below the bar is on L₂ |
| the end's regularised scale | the small-cut norm at L₂(Im τ) | CHOSEN, by hand | 2 (1.00) | — | see below |
| the Higgs's weight | 3/2 | CHOSEN, by hand | open (counted at log₂ 7, as in the first row) | — | W133's zero-free census is at weight 3/2 |

- **The line.**
  - The test searched ten lines, restricted to slope 2/5 after the earlier censuses' results over B1713's 266.
  - The search behind the value is counted as the 266, as the first row counts it.
- **The Higgs of each sector.**
  - The 27 options are a direction from the menu for each sector.
  - The nine searched are the pairs with down = leptons, including the three diagonal (one-direction) pairs.
  - The tie is put in by hand (1.58 bits). It is the MSSM's H_u, H_d pattern (B1790's literature line) and I-35's sector
    pattern (up with one sign, down and leptons with the other).
- **The end's scale.**
  - This seat's THE EXACT END (C1): at L₂ the exact twisted norms agree with 2πL₂ + c_s to 0.6% in every channel, at its
    four rows near Im τ 3. That is firmer ground than the first row's L_max.
  - At this branch's own rows the exact six were not computed.
  - L is read from B1667's Re τ = 1/4 column, as in the first row.

**The menu, recomputed from its stated rule** (ZERO_FREE_FRAME_EXPLORATION § 1, § 6; B1730: "zero-free only if r ≡ 4
mod 8"):
- The ten zero-free weight-3/2 members with one unit are parsed from § 1. For them, a ≡ 2 (mod 4) and r ≡ 2a (mod 24).
- "W127 counts three generations at r = 12 and 20", which leaves six.
- The sign class ε = i^((a+2)/2) = +1 is kept because on the zero-free census's nine "only the ε = +1 lines with a ≥ 6
  reach" nines near 2.5 (§ 6), with holomorphy fixing the reading. That leaves {6, −2, 22}, the test's MENU (check K2).
- **Caveat on the tag** (§ 7): "Main's frame is outside PF1-W as written", and where χ_η^r is absorbed "is not tested".

**The identifications** (all UNEARNED; each reduction quoted from its own row, and the check ties each reduction to its
quote):

| row | what this branch uses it for | reduces to |
|---|---|---|
| I-31 | given Λ: T's three zero modes as the three generations | — |
| I-32 | the 6Y twists, the sector assignment, the weave's Higgs line as the electroweak Higgs | I-23 → I-13 |
| I-33 | the read-out, with T-NORM by hand | I-13 |
| I-34 | the menu keeps r = 12 and 20 because W127 counts three generations there: the index, given the unit, read as the generation count | I-26 |

- **Union-find:** 7 rows (with I-23, I-13, I-26) give 3 sources.
- **I-34 is this seat's reading, by default.** I-34's row cites W45 and W46, not W127, so main should confirm. If main
  rules otherwise, the sources are 2. (In the first row I-34 was flagged out, since no index enters ∂R's census.)
- **Not on the ledger:** two Higgs directions as two electroweak doublets. TWO_HIGGS_RESULT: "'If S stands for the Higgs
  doublet' is a reading".
  - If it were registered (an instance of I-32, so of I-13), the 1.58-bit tie would go with it.
  - That is a trade of bits for an unearned row, as in the first row's § 3, and not progress by P-392.

**Listed, not counted.**
- **Tagged hypotheses:**
  - PF1-W ("PF1-W is a reading"; the caveat above);
  - holomorphy (W135, applied to the Higgs factor only);
  - Λ;
  - the unit (FK10, v1.39);
  - GM5b.

  H-cov is not used.
- **FORCED:**
  - the family group, the closed form and B1667's radii, as in the first row;
  - **the lepton–down identity on (2/5, k/10)** (B1742 § 3; P-355). For k odd, as at the best row, it holds only for a
    Higgs with no QI component. F₂₂'s is about 10⁻¹³, so D = 9 and the Georgi–Jarlskog relations hold to rounding with
    c = 3.
- **The bar's:** the 10% allowance.
  - TWO_HIGGS_RESULT Q4: at the measurements' own errors the two lepton ratios miss by 230σ and 54σ.
  - The first row's relations were not tested at the measurements' errors.
- **Unpriced looks** (one definition in both rows: a search with the data in view that no bits price):
  - the Im τ window 2.0–3.5, the band where earlier fits had put τ (P-287: "the fits put Im τ near 2.7 at the second
    horocycle and near 3.1 at the first"). It is data-informed, as the first row's band is, though it predates
    B1748's;
  - the menu's sign class, kept after the zero-free census's nine;
  - the two-doublet idea itself, from the framing read-outs.

  The α = 2/5 restriction and c, which TWO_HIGGS_RESULT's Limits also lists, are priced here in the bits.

**The reach.**
- **The six:** a READING (B1742; P-351).
  - With H_d = F₂₂ the lepton spectrum is the down spectrum, so with c = 3 the six are four quark ratios.
  - Random four-target sets are fitted as well 0.15% of the time (post hoc).
  - D = 9 is excluded at 14σ (P-355).
- **The nine:** 154 at its census minimum. |V_us| is 0.19 of measured at the best six-row; |J| is about 10⁻⁶.
- **The other nine:** not reached.
- **The output rank:** f(d) ≤ 2 (C(d) is τ).

## What it says (a reading)

1. **The lower χ² comes with more inputs.** Against the first row, what goes and what returns in its place:

   | the first row | what replaces it here |
   |---|---|
   | H-cov | two tags (PF1-W, holomorphy) |
   | the shared-section binary | the 27-way assignment: 9 searched on the data, plus the 1.58-bit tie by hand |
   | the eight readings searched on the data | four searched, plus one bit by hand |
   | the apex band | a data-informed window of its own, plus two more unpriced looks (the menu's sign class, the two-doublet idea) |
   | — | I-26, through the menu's generation count (this seat's reading) |

   - In all: 23.79 bits against 20.03, and 3 sources against 2.
   - The by-hand difference, 1.58, is the tie (1.58) plus the reading's hand bit (1.00), less the first row's shared
     section (1.00).
   - By P-392's rule (an item removed without another returning), moving from the first row to this one is not
     progress.
2. **This row carries a relation the data exclude; the first row does not carry it.**
   - On the shared line (2/5, 1/10), with c = 3 in both, this branch's F₂₂ makes D = 9 a relation of the branch, 14σ
     from P-094.
   - The first row's D is a fitted output, 10.75 at its best row (1.6σ) and 10.48–11.32 over its rows below the bar. Its
     horocycle, reading and τ differ.
   - The first row's χ² has its own caveat: it rests on the small-cut norm at L_max (P-421). This row's L₂ is firmer
     (C1).
3. **χ² alone does not show what the lower χ² cost.** The scoreboard is a graded vector, not one total (S254). Its
   columns are what set these two rows side by side.

## Proposals (they assign nothing)

1. **To main, for P-418:** take this as FR-FIB's second row, beside the first. The JSON is the source;
   `scoreboard_check_2.py` is its doc-facts check.
2. **Show each row's own relations beside its fit, at the measurements' errors, in both rows.**
   - Here D = 9 is excluded at 14σ.
   - In the first row no relation is tested at those errors, and its D is fitted.
3. **Two record items:**
   - The two-doublet reading, if registered, is an instance of I-32. It would add a row and remove the 1.58-bit tie, a
     trade that P-392 does not count as progress.
   - Confirm or reject this seat's reading that the menu's step "W127 counts three generations at r = 12 and 20" is an
     I-34 use.
4. **The remaining rows** (FR-FLUX, FR-G2Q, FR-DYN) fit the same schema. This seat can draft them.

0 of 19.
