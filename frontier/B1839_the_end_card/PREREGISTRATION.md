# B1839 — PREREGISTRATION: THE END CARD (P-421) — with the end a geometric cut, does THE SIX ON THE STRIP stay a candidate?

**The question.** The end here is a geometric cut: the exact horoball norm of every channel at ONE level L_max(τ) + δ, with δ
free over a fixed grid and the cusp limit. The test asks whether the six charged-fermion ratios still single out the frame
at GENESIS v1.61's level-1 screen. The null is the matched one. It re-makes every choice read from the data: the apex, the
line from all 266, the reading, the lepton factor c (continuous in [1/3, 5]), and now δ.

cc (main), 2026-11-05, at the owner's agreement ("agreed", 2026-11-04, to main's plan: "one sealed card that re-reads the six
with the end's scale as a free, counted input, beside the matched null"). **Sealed before `verification/census.py` and
`verification/look.py` run.** P-421's deciding card (B1838 § 3). 0 of 19.

## Why

B1829 made THE SIX ON THE STRIP the record's one candidate family. It is graded at level 1 under B1798's null, which
re-chooses c and the line class (r ≈ 0.1–0.25%).

Every look of that family takes the end as the small-cut norm 2πL + c_s at L = L_max(Im τ) (B1726's `compute()`). B1838
showed three things about that end:
- **At the exact maximal-horoball norm the six fail:** χ²_six 26–54 at the web seat's four rows (P-595, reproduced on main).
- **The small-cut expansion is used where no disc fits.** At L_max, e^{−L_max} lies above the cell's inradius ½ at all 54
  of B1667's points.
- **No single horocycle reproduces the candidate's channel weights.** Each channel's weight is the exact norm at a
  different level: 0.81 for channels j and k, 0.91–0.95 for 1 and i.

So the end is an ANSATZ (the scoreboard's A07). The honest replacement is the end with its scale free and counted: one
geometric cut for every channel and sector, at a level read from the data and priced in the null.

- **If the candidate passes the screen with that end,** the end becomes one FITTED number, and the family's confirmation
  (P-585, P-638) is worth sealing.
- **If it fails,** the family's level-1 pass belonged to the ansatz, and the candidate dissolves before any held-out target
  is spent.

## The model (no data)

- **The points:** B1753's 223 apexes (its `census.py`'s `apexes()`, unchanged) × all 266 of B1713's lines (B1726's `lines()`).
  That is B1798's grid, 59 318 (apex, line) pairs.
  - Each apex is reduced to |Re τ| ≤ ½ by T⁻¹, as B1667's Dirichlet cell needs: (τ, (a, b)) → (τ − 1, (a, b + a mod 1)).
    T is a symmetry of the frame's outputs (B1836).
- **The end:** the exact norm of each channel's twisted kernel |P_s/R_s|² over B1667's Dirichlet cell minus the horoball at
  level L_h = L_max(τ) + δ.
  - This is the web seat's instrument (`frontier/B1838_the_end/verification/exact_end_web_seat.py`, byte-faithful) with B1667's
    geometry: the accessory parameter, the Frobenius series, the horocycle and the cell.
  - Its quadrature is used at (nth, ns) = (40, 28). Main's data-free check before the seal (Disclosed) found it equal to the
    instrument's (96, 64) to ≤ 8 × 10⁻¹² for δ up to 10.5.
- **One level, all channels and sectors.** δ is taken from the grid
  DELTAS = (0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50, 0.60, 0.70, 0.80, 1.0, 1.25, 1.5, 2.0, 2.5, 3.0, 4.0,
  6.0, 10.0), together with the cusp limit δ = ∞.
  - At the cusp limit every channel's weight is equal; there N_s → 2πL_h + const, and the ratios are scale-free.
  - That is 23 ends per (apex, line), and the grid is the family. No interpolation is used.
  - The lower edge, δ = 0, is the maximal horoball. B1667's L₂ lies inside the grid. Every embedded horoball is a geometric
    cut, so the grid runs past L₂ to the limit.
- **A data-free law the census uses, checked as control C1:** the exact norms depend on the line and sector only through
  the Higgs twist ±3w mod the lattice (w = aτ + b).
  - The reason: the sector charges sum to −Y_H. The pairs are (Q, u) = (1, −4), (Q, d) = (1, 2) and (L, e) = (−3, 6).
  - So each (apex, δ) needs one quadrature per class: 170 classes for the 266 lines, computed with the down sector's four
    channels. Each sector then zeroes the channels whose residue the instrument zeroes (|R_s| ≤ 10⁻¹²).
- **The ratios and the measure:**
  - **The ratios:** the instrument's `ratios()`, which takes the Higgs DR at τ and every sector in S and S̃.
  - **The measure:** B1741's `compare.py`, loaded unchanged with its sha256 asserted, through its DATA, `sigmas()`,
    `draws()` and SEAT.
  - **χ²_six:** cnull's (B1798, the referee). The four quark logs come from the row's readings, the two lepton logs take
    ±k with k = ln c, and the minimum runs over the rows and the two SEAT reading triples.
- **c, three ways:**
  - **decisive:** continuous in [1/3, 5], the range of the web seat's own c-scan, the most demanding of B1798's three c
    nulls;
  - **read-out:** the scan's nine values;
  - **read-out:** {1, 3}, the seat menu.

## Cells

| cell | prediction | prior |
|---|---|---|
| **D, THE DECISIVE CELL** | Under the matched null, with every choice above re-made by each target over the same 59 318 × 23 rows, the exact 97.5% upper end r of the fraction of random hierarchies whose minimum is ≤ the data's is below 0.01. The null is B1741's `draws()` on fresh seeds 31001–31250, 10⁶ targets, with c continuous. | 30% |
| P1, the support cell | Some row has χ²_six < 16.75 (c continuous). | 70% |
| C0, control | The web seat's sealed E2 (exact norms at L_max, the seat menu, its rows A–D at their τ) is reproduced through this card's code path (the split quadrature, the class cache, `ratios()`, the measure) to 10⁻⁶ relative. Rows A–D give 30.664, 39.149, 53.700 and 40.831. | 95% |
| C1, control (data-free) | The class cache equals the instrument's `twisted_norms()`, sector by sector, at 120 random (apex, line, sector, δ), to 10⁻¹² relative in every channel with a nonzero residue. | 95% |
| C2, control (data-free) | At 24 random (apex, class, δ), including δ = 6 and 10, the split quadrature equals the instrument's `twisted_norms()` at (40, 28) to 10⁻¹³, and (40, 28) equals (96, 64) to 10⁻⁹. | 93% |
| C3, control | The card's null code, run on B1798's committed small-cut census (its 59 318 × 2 rows), reproduces the referee's c-choosing hits on seeds 5001–5010 exactly: `cnull_b1753_all_5001_5010_c0.333_5.json`, both the bounded and the seat counts. | 95% |

**Read-outs, not looks:**
1. D with the nine c values and with {1, 3}.
2. δ = 0 alone (the maximal horoball, no end freedom): the data's minimum and its rate on seeds 31001–31050.
3. δ = ∞ alone (the cusp limit): the same.
4. B1753's 48 five-ality lines alone: the same.
5. The best rows: apex, line, δ, reading and c, and the δ of the data's minimum.
6. The distribution of δ among the null's hits.
7. The six's values at the best row against the data's, beside B1753's small-cut best (2.74).
8. C1's per-sector maximum.

**THE_BAR, fixed now (GENESIS v1.61, level 1):**
- **The screen:** p < 0.01 against the fully matched null, with every within-arc choice priced and no factor for the joint
  count.
- **Priced in the null:** the apex (223), the line (all 266, the class-choosing statistic), the reading (two SEAT triples),
  c (continuous) and δ (23 ends).
- **Not priced, as in every look of this frame:** the frame itself (FR-FIB with H = I), the construction of the readings,
  and B1667's geometry. The δ grid is fixed now and is data-free.
- **The count:** this is one look on the six. It is entered in docs/LOOK_LEDGER.md at the landing.

**The reading, written before the run.**
- **D and P1 hold:** the candidate survives level 1 with a geometric end.
  - The scoreboard's A07 is re-typed from ANSATZ to FITTED. It is one continuous number, the cut level δ*, read from the six
    and priced here; it is not derived.
  - The candidate is frozen at its best row with δ*. The level-2 cards (P-585's y_b/y_t and P-638's r, under P-665's
    ruling) are then sealed at that row and nowhere else.
- **P1 holds and D fails:** a geometric end reaches the six, but with its level free the frame reaches random hierarchies
  too often.
  - The family's level-1 pass belonged to the ansatz end. THE SIX ON THE STRIP stops being a candidate.
  - P-585's and P-638's cards are not run for it, and no held-out target is spent.
  - The small-cut weights stay on record as an ansatz that passes the screen. Any later end must be derived, not chosen.
- **P1 fails:** no geometric end reaches the six. The verdict is the same as the previous case, and stronger.
- **A control failing** stops the reading until it is resolved post hoc, labelled as such.

## Seen first

- `VERDICT topic-sweep /free cut|cut level|scale free|L free|end.{0,12}free|horoball norm|exact end|end card|Higgs twist/
  (full text): 15 of 1584 arcs on main match (NEGATIVE 2, OPEN 3, PROVED 10); 7 register rows match (DONE 4, QUEUED 3)`.
  The arcs that bear:
  - B1838 (the end; § 1, § 2b);
  - B1829 (GENESIS v1.61; the family);
  - B1667 (the canonical cusp);
  - B1712, B1620 (the weave; no end).

  The register rows:
  - P-421 (this card's question);
  - P-410 (the web seat's exact norms at L_max, DONE);
  - P-585 (the family's level 2);
  - P-445 (the web seat's looks counted);
  - P-589 (the correction class).
- **Also read for the design:**
  - B1753 (the apexes, the five-ality lines);
  - B1798 (the class-choosing null; the referee's `cnull.py`, `direct_null.py`; the three c nulls);
  - B1741 (the instrument and the measure);
  - B1726 (`compute()`; the lines);
  - B1728 (the 6Y mod N law, which the Higgs-twist law resembles: the frame sees charges mod N; here the norms see only the
    Higgs's);
  - P-402 (the small-cut L₂: χ²_six 30.6);
  - P-266 (look-elsewhere);
  - P-586 (the matched-null requirement).
- **LAW_MAP:** "THE CANONICAL CUSP" (B1667) and the two-ingredient rows (B1725, B1726, B1732, B1734, B1735, B1741). None
  states the end as a free geometric level, and none states the Higgs-twist law.
- **Literature:** none bears on the arithmetic. The regularisation scale of a cut zero-mode norm is an ordinary input in
  Kaluza–Klein normalisation.

## Disclosed

- **Known before the seal:**
  - the exact-end failure at L_max at the web seat's four rows (χ²_six 26–54; with τ refitted, 26–36);
  - the single-horocycle levels: per channel, the candidate's weights equal the exact norms at δ ≈ 0.16–0.30, so a single δ
    in that range is where a pass, if any, is expected;
  - the small-cut L₂ (30.6);
  - B1798's rates and the three c nulls;
  - B1753's best row, 2.74 at 0.3333 + 3.0368i on (2/5, 1/10).
- **Data-free design checks run and read before the seal** (`audit/p421_card/`; frame quantities only, no χ² computed):
  - **The quadrature:** (32, 24), (40, 28) and (48, 32) against (96, 64), ≤ 3 × 10⁻¹³ to δ = 3; (40, 28) ≤ 8 × 10⁻¹² to
    δ = 10.5. The norm's slope tends to 2π (6.283185) at deep cuts.
  - **The Higgs-twist law at six random apexes:** sectors agree to ≤ 1.2 × 10⁻¹⁴, and lines of one class to ≤ 6 × 10⁻¹⁵.
    The positive control holds: lines of different classes differ by 0.7–3.8.
  - **A cubic spline over 10 levels** missed direct values by up to 4.6 × 10⁻⁴, so the grid itself is the family.
  - **Timing:** 78% of a norm is the horocycle solve, which depends on (τ, L_h) only, hence the split.
  - **A calibration of the null, data-free:** on B1798's small-cut census, with random targets only (seeds 777001–777002) and
    synthetic thresholds in place of the data's minimum, the c-continuous rate is 0.21% at 3, 1.3% at 8 and 5.1% at 16.75.
    The card's rows are 11.5 times as many, so D can hold only if the data's minimum stays near the small-cut end's.
    The decisive prior was lowered from 40% to 30% on reading this.
  - **A dry run of both instruments** (`audit/p421_card/dry/`): 2 apexes, 4 levels, and the data's six replaced by one
    random hierarchy (seed 424242). It ran end to end, and C1 and C2 held on that grid. C0 and C3 failed there, as they must
    against a random target. It caught one defect (a JSON type), fixed before the seal. Census cost: about 13 s per
    (apex, level), so about 2.3 h on eight workers.
- **Not computed before the seal:** no χ²_six by main at any exact end other than the reproduction of the web seat's
  sealed E2 rows (P-595), and no frame value at an apex compared with data.
- **Limits:**
  - B1749's 125 apexes are not re-run. Its rates under B1798 were close to B1753's.
  - The decisive c null is the most demanding of B1798's three; the two others are read out.
  - The grid is finite. At δ = 10 the channel weights still differ by a few per cent ((N₁ − N_j)/N₁ ≈ 4.5% in the design
    checks, so about 2% in the weights); the cusp limit closes that gap, and the levels between are not sampled.

## Instruments

- `verification/census.py` (data-free).
  - It writes `accessory.json` (the accessory parameter and B1667's geometry at each reduced apex), `norms.jsonl.gz`
    (per apex: the 170 classes × 22 levels × 4 channels; the raw sha256 is in `census_run.txt`) and `census_run.txt`.
  - It runs C1 and C2 at its end.
- `verification/look.py`.
  - It builds the 59 318 × 23 rows' ratios from `norms.jsonl.gz` (data-free), then runs C0, C3, P1, D and the read-outs once.
  - It writes `look.json` and `look_run.txt`, which are committed unread and then read.
- Both are import-tested; importing computes nothing. They run with eight workers, niced, with single-threaded BLAS.
- `ARTIFACT_HASHES.txt` pins both instruments, the web seat's instrument, B1741's `compare.py`, B1753's and B1726's
  `census.py`, B1667's `the_canonical_cusp.py`, B1656's `b1656_funcs.py`, B1798's referee `cnull.py` and its
  `cnull_b1753_all_5001_5010_c0.333_5.json`, and the census files C3 reads.
