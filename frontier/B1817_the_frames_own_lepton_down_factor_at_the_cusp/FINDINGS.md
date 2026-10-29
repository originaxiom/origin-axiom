# B1817 — THE FRAME'S OWN LEPTON/DOWN FACTOR AT THE CUSP (strand A's A1; P-397, P-294; data-free): ON THE SLOPES OF ORDER ≤ 30 WHERE B1788's CLOSED FORM GIVES THE DOWN QUARKS AND THE CHARGED LEPTONS THE SAME SECOND-GENERATION EXPONENT, EVERY CONVERGED LIMIT OF R₂ THAT IS INDEPENDENT OF THE OFFSET AND OF Re τ IS 1, 4 OR ¼ (BY READING) OR A NON-INTEGER LINE CONSTANT (3.43 ON 1/8); WITH THE ANOMALY-FIXED CHARGES OF N_c = 2, 4, 5 THE SAME 4 AND ¼ RECUR UNCHANGED — THE INTEGER DOES NOT MOVE WITH N_c (IT EQUALS N_c ONLY AT N_c = 4, BY COINCIDENCE), SO NO LIMIT TRACKS THE COLOUR COUNT AND NONE IS 3 AT N_c = 3; ON THE TORSION-DEGENERATE SLOPES R₂ IS A FUNCTION OF THE OFFSET b AND PASSES THROUGH 3 ON A CONTINUUM — A TUNED VALUE, NOT A FACTOR. THE TWIST-CHARGE ROUTE TO c = N_c IS CLOSED ON THE SLOPES TESTED

**Verdict: NEGATIVE as scoped** for "the frame's own twists supply c = N_c at the cusp".
- Refereed hostile: PASS WITH CORRECTIONS (§ 5). Its scans were regenerated on main.
- Data-free, exploratory, and not sealed. No line is selected by it.
- cc (main), 2026-10-29: strand A of the owner's final act (DESIGN.md § 1, A1, written before the run).

**0 of 19.**

## 1. Why this was the first test
- **The literature has no geometric source of an exact 3.** The strand A reader read it at source and main re-derived the
  algebra (`verification/STRAND_A_DESIGN.md` § 0; P-397's 2026-10-29 note).
- **Exactly 3 exists only as the B − L Clebsch diag(1, 1, 1, −3) = −N_c.**
- **On the frame's doublet leg the anomaly-fixed charges give L/Q = −N_c for every N_c.** On its singlet leg they give
  e^c/d^c = 2N_c/(N_c − 1), which equals 3 only at N_c = 3.
- **The frame already sees each leg's own charge**, through the exponents e(m₂/m₃) = ½ − (‖2q_Lα‖ + ‖2q_Rα‖)/2 (B1788).
  - Where the two sectors' exponents agree, R₂ = (m₂/m₃)_e/(m₂/m₃)_d tends to a constant: 1 on slope 2/5 and 4 on 1/10
    (B1789).
  - Whether any such constant is the colour count had never been mapped.

## 2. The computation (`verification/a1_cusp_map.py` → `.jsonl`, `_run.txt`, `_summary.json`)
- **The slopes:** every α = j/N with N ≤ 30 and 0 ≤ α ≤ ½ on which the two exponents are equal as exact rationals.
  There are 31 for N_c = 3, and 39, 39, 31 for N_c = 2, 4, 5.
- **The instrument:** B1726's `compute`, unchanged, at Re τ = ⅓ and Im τ 8, 10, 12.
  - L is clamped beyond B1667's column, as in B1785 and B1789.
  - Offsets b = 0.137 and 0.311.
  - Both readings, both horocycles. 840 rows, no errors, single-threaded.
- **The control:** the charges replaced by the anomaly-fixed 2N_c·Y: Q 1, u −(N_c+1), d N_c − 1, L −N_c, e 2N_c,
  H N_c. These give 6Y exactly at N_c = 3.
- **The b-independence of the limits:** median relative difference 6 × 10⁻⁶ between the two offsets at Im τ 12. The
  exceptions are α = 0 and ½ (degenerate twists) and two N_c = 5 slopes.
- **Results** (N_c = 3, reading S, L_max, Im τ 8 → 12):
  - **→ 4:** a family around α ≈ 1/10, from 2/21 to 3/25: 3.98 → 4.00 at 1/10, 4.003 → 4.001 at 3/29. Reading S̃ gives
    ¼.
  - **→ 1:** the family around 2/5, which is B1742's identity: 1.000 on 2/5 and 1/5, 1.001–1.014 on 11/29 … 11/28.
  - **A true line constant, independent of b and Re τ:** 3.4299 in reading S on 1/8 (0.2916 in S̃).
  - **Not constants (the referee's correction, regenerated on main).** On the torsion-degenerate slopes 1/12, 1/4,
    5/12 and their kin, R₂ is flat in Im τ but varies with the offset b and with Re τ:
    - 1/12, reading S, at Im τ 12: 1.39, 2.56, 1.28, 1.70, 1.05, 3.77 at b = 0.05, 0.137, 0.2, 0.311, 0.4, 0.6, and 0 at
      b = 0, 0.5, 0.75;
    - 5/12, reading S̃: 3.03 at b = 0.05;
    - so on these slopes R₂ is a function of a continuous offset, and 3 is reached on a continuum of b.
  - **Slowly converging:**
    - 1/11: 3.45 → 3.82, heading for 4;
    - 2/23 depends on Re τ. Along Im τ it gives 2.59, 2.88, 3.12, 3.31, 3.47, 3.50 at Im τ 10–20, passing through 3, and
      double precision fails by Im τ 24. Its S̃ runs 0.208 → 0.236, like the 4-family's ¼. A limit of 4 is plausible
      but not shown.
    - The 1-family's edges.
  - **The first generation fails wherever R₂ → 4:** R₁ runs to 0 in S and to ∞ in S̃, as B1789 found on 1/10.
- **The integer census:** limits b-independent to 10⁻³ and within 1% of n or 1/n, for n = 2…6, at Im τ 12, L_max.
  The b-filter excludes the torsion-degenerate slopes. Re τ-independence was checked by the referee on the integer
  cells (1/10, 1/9, 1/6, 2/5, 1/8: identical at Re τ 0.1, ⅓ and 0.6), not on every row.

  | N_c | rows hitting | values |
  |---|---|---|
  | 2 | 25 | 4, ¼ only |
  | 3 | 14 | 4, ¼ only |
  | 4 | 4 | 4, ¼ only |
  | 5 | 4 | 4, ¼ only |

  - The integer does not move with N_c: 4 and ¼ at every N_c. It equals the colour count only at N_c = 4, by coincidence
    (caught by this arc's own lock at landing; the referee had not flagged it). At N_c = 2, 3, 5 no slope gives N_c or
    1/N_c.
  - The line-specific constants change with N_c, with no N_c-proportional pattern. At α = 1/(4N_c), for example, they
    are 1.087, 2.557, 0.776 and 1.214 for N_c = 2, 3, 4, 5.

## 3. What it means
- **No converged, b- and Re τ-independent limit of the frame's lepton/down factor tracks N_c.** The integer 4 (¼) is
  the same at N_c = 2, 3, 4 and 5. It equals N_c only at N_c = 4, by coincidence, and none is 3 at N_c = 3. Where the factor is a genuine cusp limit it is 1, 4, ¼ or a non-integer line constant.
- **The recurring integer is 4 in reading S and ¼ in S̃, at every N_c.** This is consistent with a property of the theta
  structure rather than of the charges. It is observed, not derived. The swap between readings is consistent with S̃'s
  exchange of the off-diagonal entries (B1788 § 3).
- **Where R₂ reaches 3 it does so on a continuum.** On the torsion-degenerate slopes R₂ is a function of the continuous
  offset b, and of Re τ. A 3 there is a tuned value of a free parameter, not a factor.
- **The control's reach.** It changes only the twists' integer charges: compute reads the charges only through the
  sector twists. So it shows that integer multiples of the twist do not produce N_c. It does not test other
  colour-dependent structure.
- **What the earlier arcs settled, and what this adds:**
  - B1789 showed c is not derived on the six's slope family.
  - B1793 showed a zero-net curvature cannot supply it.
  - This arc closes the twist-charge route on the equal-exponent slopes tested.
- **What remains (P-397):**
  - a mechanism that generates an entry linearly in the doublet leg's charge, the GJ structure, which the frame as built
    does not have;
  - the B − L Clebsch channels, which the record's content lacks at tree level;
  - L250's non-abelian bundle (P-401, P-403).
- **No input removed. c stays one discrete input, not derived.** It is never set: P-488.

## 4. Scope
- B1656's frame through B1726's `compute` with the record's Higgs (DR).
- Slopes of order ≤ 30 with equal second-generation exponents.
- The cusp limit read at Im τ 8–12 (the referee: to 20) with L clamped. These are limits of the instrument, whose end
  radius is B1667's column extrapolated, not of a physical cusp. Double precision fails by Im τ ≈ 24.
- Re τ = ⅓. Two offsets.
- Off-equal-exponent slopes are not covered. There R₂ runs to 0 or ∞ with Im τ, so it has no finite limit to be a
  factor.
- Exploratory: it selects nothing and compares nothing measured.

## 5. The referee (hostile, read-only; `verification/referee/REPORT.md`; drivers `drv.py`, `drv2.py`; regenerated on main in `referee/main_rerun/`)

**Verdict: PASS WITH CORRECTIONS.** All corrections are applied.
1. **OK.** The integer limits were regenerated with an independent driver at Re τ 0.1, ⅓ and 0.6 and at Im τ 12 and 14.
2. **OK, applied as a wording change.** The charge patch is legitimate but tests only the twists.
3. **OK.** The equal-exponent selection is correct. An unequal slope (1/7) has no finite limit.
4. **CONFIRMED-PROBLEM, applied.** The draft's "line-specific constants" on 1/12, 1/4 and 5/12 depend on b and Re τ. 3
   is reached on a continuum there. 2/23 is unconverged.
5. **MINOR, applied.** The clamped L: these are the instrument's limits.
6. **Applied: three overclaims reworded.** The title's "nothing tracks N_c"; "a property of the theta structure"; and
   "closes the remaining frame-internal formulation".

## Seen first
`VERDICT topic-sweep /lepton factor|Georgi|Jarlskog|Clebsch|c = 3|factor 3|N_c|colour count|cusp limit|prefactor/ (full text)` is rerun at landing.

**Bearing on it:**
- B1788 (the closed form);
- B1789 (1/10's 4; 2/5's 1);
- B1793;
- B1742 (the 2/5 identity);
- B1656;
- P-294, P-397, P-355, P-488.

**Literature:** the strand A reader's LIT_ONE_LEG (audit; arXiv:1211.6529, 0907.4895 and the GJ literature at source),
summarised in `verification/STRAND_A_DESIGN.md`.

## Files
- `verification/a1_cusp_map.py`, `.jsonl`, `_run.txt`, `_summary.json`.
- `verification/STRAND_A_DESIGN.md`: the design, written before the run.
- `verification/referee/`.

The lock: `tests/test_b1817_the_frames_own_lepton_down_factor_at_the_cusp.py`.
