# B1811 — PREREGISTRATION: THE SYMMETRY-SELECTION VALUES AGAINST THE SIX (P-432's second half). The frame's outputs at the four configurations the object's symmetry fixes (B1810), for B1810's 13 directions, scored by B1741's sealed measure exactly

## Why

- **The owner's ruling (2026-10-29):** P-432 is to be run as a sealed test.
- **What it tests.** B1810 tabulated the only outputs of B1656's frame that need no continuous input. They come from:
  - the four configurations the object's symmetry fixes (B1809 § 2);
  - the record's parameter-free Higgs directions;
  - B1667's canonical radii;
  - the readings.

  This test asks whether any of them reaches the measured mass ratios ("the six") specifically.
- **What it is not.** It is not a search over τ; τ is fixed by the symmetry. It scores a finite menu fixed in advance.

## The frame card (WORKING_RULES, the rule of 2026-10-29; B1810's card, with the null filled)

| item | value | label |
|---|---|---|
| frame | B1656's flat fibre frame (FR-FIB): B1740's sealed census module, compute() exactly | CHOSEN (the frame) |
| configurations | (i, 0), (ω, 0), (i, (½, ½)), (ω, (⅓, ⅔)) in line_w's convention ((⅓, ⅓) in compute()'s w = aτ + b, the reviewer's check: the unconverted line changes DR's spectrum); ω = e^{iπ/3} | FORCED given the frame (B1809 § 2) |
| radii | B1667's exact L_max, L₂ at each point | FORCED (canonical construction) |
| horocycle | max, 2 | CHOSEN |
| readings | the seat's two reading triples (B1741's menus); the seat's reading rule was informed by data (the web seat's readings_scan, LOOK_LEDGER) | CHOSEN |
| directions | DR, a₀, R, t = −5/288 (B1809's Table T, untwisted, outside PF1-W) ∪ B1730's zero-free F_a at n = 1, a ∈ {−10, −6, −2, 6, 10, 14, 18, 22, 26} (B1730's `the_zero_free_lines.json`: {−10, 2, 14, 26}, {−6, 6, 18}, {−2, 10, 22}; F₂ = R) | CHOSEN: n = 1 (B1700's unit; n = 0 would be R alone; n = 2 not run); the union of the untwisted and twisted families; one Higgs for all sectors (B1742's two-Higgs pairs not in the menu) |
| outputs | the six (and the nine as read-outs) | — |
| **the null** | B1741's log-uniform random hierarchies, each scored against all 52 rows × 2 horocycles × the seat's two reading triples × c ∈ {1, 3}: the null chooses direction, configuration, horocycle, reading and c as freely as the arc | — |

**The effective menu** (the reviewer's count, foreknown from B1810): under the seat's readings only 22 (configuration,
direction, horocycle) cells are non-degenerate, all at τ = i. They are the 10 non-degenerate directions at (i, 0) and DR
at (i, (½, ½)), each at both horocycles. **The ω configurations cannot carry P1:** their rows are rank one or (0, 1).

## The model (no data)

- **The census** (`verification/census.py`): 13 directions × 4 configurations = 52 rows. Each row carries 2 horocycles,
  the sectors in S and S̃, and the CKM for each (up, down) reading pair. B1740's census.py is loaded unchanged (sha256
  asserted before execution), with its Higgs function extended to the 13 directions.
- **The measure** (`verification/compare.py`): B1741's `compare.py`, loaded unchanged (sha256 asserted before
  execution). It is re-pointed only to this census, the seeds 1811–1830 and the row count 52 (B1753's wrapper). Its
  menus, features, sigmas, null and χ² are B1741's. Finiteness is asserted on the loaded arrays.

## Cells

| cell | prediction | prior |
|---|---|---|
| **THE DECISIVE CELL: P1 AND P2** | the seat's menu: some row below 16.75 (P1), and at most 0.1% of random hierarchies reach as low a χ²_six (P2, mean over 20 seeds). **P2 without P1 is not a pass.** | 1% |
| C1, control | (a) the extended Higgs function gives B1740's F₋₂ to 10⁻¹²; (b) B1740's first committed census row is reproduced to 10⁻⁹; (c) every sector, reading and radius of the census, and the CKM wherever B1810 marks V defined, reproduce B1810's table to 10⁻⁴ relative (floor 10⁻²) | 97% |
| C2, control | B1735's 3.0945633 is reproduced on B1726's census | 99% |

**Read-outs, not looks:**
- P1 alone; P2 alone; P2 at 1%;
- the covariant menu (P2c); the factor free;
- R1, R2, R5 and R7;
- the best rows, decoded from the census's direction and configuration keys;
- the nine (P3, P4), foreknown to fail structurally: J = 0, and V a permutation except one angle of order 1/L (B1810).
  R6 (J at the best nine-row) is omitted: J = 0.

**THE_BAR, fixed now.**
- **m = 47.** That is 46 prior looks by the joint look ledger, counted at the seal: B1753's 39, plus B1755, B1786,
  B1792, W162, W166 and W170's two (B1795 is data-free, not a look). This test is the 47th.
- **PASSED needs r < 0.01/47 ≈ 2.1 × 10⁻⁴**, after the third opinion.
- **2.1 × 10⁻⁴ ≤ r ≤ 10⁻³, with P1, reads "specific as sealed, not PASSED"** (B1755's precedent).
- This test's row is added to LOOK_LEDGER at its landing. The seal commit carries only the seal.

**The reading, written before the run.**
- **The decisive cell holds.** A value the object's symmetry fixes reaches the six specifically: a candidate for THE_BAR
  as graded above. It is still a READING: the reading and the horocycle are chosen, and the direction is taken from a
  family. It is weaker if P2c (the covariant menu) fails. The nine fail by structure.
- **P1 holds, P2 fails.** Some symmetry-fixed value fits, but no more specifically than random hierarchies fit the same
  menu.
- **P1 fails (expected).** The parameter-free values do not reach the six. This closes P-432 for this frame.
- **A control failing** stops the reading until it is resolved post hoc, labelled.

## The input-completeness ledger (docs/INPUT_COMPLETENESS_LEDGER.md, its 12 rows)

1. **Scheme.** Inherited from B1741 unchanged: running masses at M_Z (HZ2021), ratios within a sector.
2. **Scale.** One scale, M_Z: a convention. The object supplies none.
3. **Uncertainties.** B1741's sigmas, unchanged.
4. **Multi-modal fits.** None for the masses. The CKM appears only in read-outs.
5. **Convention constants.** None drives a verdict. J_PDG and the P-094 target appear only in read-outs.
6. **Fit against direct.** Inherited (B1612's CKM data); read-outs only.
7. **Look-elsewhere.** The null scores the same menu (it chooses its best cell). THE_BAR's m = 47 is stated above.
8. **The matched null.** B1741's log-uniform random hierarchies against the same menu.
9. **The grep.** The sweep's VERDICT line (Seen first).
10. **The firewall question.** Yes, this asks for values. The stage assumption under test: the configurations the
    object's symmetry fixes select the state.
11. **Source freshness.** The archived, sha-asserted sources: B1637's HZ2021 JSON and B1612's data.json, fetched at those
    arcs and not re-fetched here.
12. **Sealing.** Inputs pinned by hash, instruments import-tested, outputs committed unread.

Note: B1726, B1741, B1749, B1753, B1755 and B1786 did not fill this ledger. A register row is proposed for that drift.

## Seen first

- **This arc's sweep (the reviewer's):** `VERDICT topic-sweep /symmetry.selection|configuration.fixed|fixed (point|configuration).{0,60}(six|mass ratio|χ²|chi2)|stabili[sz]er.{0,40}(six|mass)|P-432/ (full text): 5 of 1557 arcs on main match (PROVED 5); 2 register rows match (DONE 1, QUEUED 1)`.
- **The arcs.** B1667, B1697, B1700, B1703, B1726, B1730, B1740, B1741, B1742, B1753, B1798, B1807, B1809, B1810;
  LOOK_LEDGER.
- **The register.**
  - P-432;
  - P-153, P-312 (ω);
  - P-173 (the SM seat's W94, a prior sealed look at ω with the null Higgs R(ω));
  - P-224;
  - P-340.
- **Earlier data contact with the F_a family:** the web seat's ZERO_FREE_HOLOMORPHIC and its zero-free census
  (LOOK_LEDGER).
- **Literature.** Modular flavour models at fixed points (Novichkov–Penedo–Petcov; Feruglio et al.): exponents and
  patterns, not values. No published test of these configurations.

## Disclosed

- **Known before the seal: every frame value in the menu.** B1810 computed and read the whole table, and its structure
  is foreknown. Since the six's magnitudes are general knowledge, P1's outcome could be anticipated; the prior reflects
  that. The census reproduces B1810 (C1c).
- **No frame value was compared with any data before the seal.** The data files were not opened.
- **Data constants seen** (all on record):
  - compare.py's J_PDG and the P-094 target, seen by main while reading its interface;
  - the P-094 target, a measured (m_μ/m_τ)/(m_s/m_b) with its σ (P-173), and B1742's model-over-measured ratios, seen
    by the pre-seal reviewer in LOOK_LEDGER and the register.

  None enters P1 or P2.
- **The menu's provenance.** F₆ and F₂₂ first entered the record through B1742's data-informed fit. Here they enter only
  as n = 1 members, by B1730's rule.
- **The count of prior looks** is THE_BAR's m above. B1753's "twenty-ninth sealed test of this frame" counts one seat's
  tests; the ledger counts all seats' decisive cells.
- **The instruments were import-tested only.** Importing computes nothing. The census and the comparison were not run
  before the seal.
- **The pre-seal review** (hostile, read-only; `audit/review_b1811/`): GO WITH FIXES. All were applied:
  - the decisive cell is P1 AND P2;
  - finiteness asserts;
  - C1c covers the whole table;
  - THE_BAR's m and threshold;
  - the frame card;
  - the input-completeness rows;
  - the Seen first;
  - the disclosures;
  - the hash check before execution.

## Instruments

- `verification/census.py` → `census.jsonl`, `control.json`, `census_run.txt`.
- `verification/compare.py` → `comparison.json`, `compare_run.txt`.
- **Run:**
  `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 nice -n 10 python3 -B census.py`, then
  `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 nice -n 10 python3 -B compare.py --workers 8`.
- **`ARTIFACT_HASHES.txt` pins** both instruments, this preregistration, and, read in place:
  - B1740's census.py and census.jsonl (C1b);
  - B1741's compare.py;
  - B1726's census.jsonl (C2);
  - B1667's the_canonical_cusp.json;
  - B1810's symmetry_selection_table.json;
  - B1691's the_exponents.py and qseries.py;
  - B1723's b1656_funcs.py;
  - B1730's the_zero_free_lines.json.
