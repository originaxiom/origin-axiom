# G4 — CENSUS-COMPLETENESS VERIFICATION OF T9 (independent sweep)

**Cell:** G4, fresh physics seat, 2026-09-01. **Scope:** the census axis only —
the seat already re-ran `kind_map_survey.py` inline (identical output, bite
controls live); this cell independently audits whether CENSUS.md's claim of
exhaustiveness (16 computable entries + 10 not-comparable classes) holds.
**Gate 5 absolute:** every number below is a lattice norm, series coefficient,
group order, ideal count, or stated central charge of a named module.
Artifacts of this cell: `supplementary_census_run.py`,
`supplementary_output.txt`, `supplementary_results.json` (this directory only;
nothing committed was modified).

## VERDICT: DEGRADED — census gap found AND dispositioned

**The census is NOT complete as banked** — an independent sweep on search
patterns disjoint from T9's token set found an entire missed series class
(the Molien / Hilbert / Poincaré generating functions) plus three further
missed computable series entries, none of which appears in CENSUS.md's A-list
or B-list. Per the verification mandate this **voids the "census is
exhausted" clause of EMPTY-CONFIRMED as stated**. All eleven supplementary
entries were then run through T9's own kind-map machinery (loaded from the
committed script, unmodified, with all three bite controls re-armed in-run):
**0/11 pass, every failure on a named condition with its exact first
violation**. The operative claim — *no banked artifact is, or approximates,
the bridge character* — **survives at the enlarged census**; the count claim
("16 entries, exhausted") does not. This is precisely the failure mode T9
itself convicted GC-12 of (FINDINGS.md §1 "REFUTED as a count / CONFIRMED in
operative content"), now applied one level up, and precisely what T9's own
caveat 1 anticipated.

## 1. Method (independent of T9's sweep)

T9's census used GC-12's tokens plus `generating function`, `graded
character`, `theta`, `partition function`, `colored Jones`, `Rogers`,
`q-expansion`, `q^`, and a filename sweep. This cell swept the corpus
(`frontier/`, `core/`, `src/`, `paths/`, `knowledge/`, `papers/`,
`speculations/`) on **different** patterns: `Molien`, `Hilbert series`,
`Poincaré series`, `graded dim`, `character of`, `Dedekind eta` / `eta(`,
`Fourier coefficient`, `cusp form`, `modular form`, q-Pochhammer/pentagonal
constructions in `.py` files, series-shaped JSON keys
(`"...series/stream/expansion...": [`), and numeric coefficient signatures
(`1, 72, 270`, `196884`, `1, 240`, `1, 0, 1, 0, 1, 0, 2`, …) in verification
data files. Every hit class was inspected; false positives (substrings of
large matrix integers, permutation lists, finite/linear characters, numeric
theta values at fixed τ, cocycle η's) were discarded with reasons.

## 2. The census gaps (series-like, computable, absent from CENSUS.md)

The word **"Molien" appears nowhere in CENSUS.md or FINDINGS.md**, yet the
corpus banks a whole family of Molien/Hilbert generating functions with
exact computable coefficients — including one that B1068 itself flags as
*"the ONE genuine q-series that 2T supplies."*

| # | missed object | location | banked form |
|---|---|---|---|
| G-1 | σ(A1) Molien doublet M, M′ (120 exact ℚ(√5) coefficients) | `frontier/B674_generation_leg/w2_step3/coefficients_both_conjugates.json` | machine-readable JSON, plus dressed variants |
| G-2 | A5 invariant Hilbert/Molien series + θ-odd twisted Molien | `frontier/B774_chord_pass/cells/CP-A5-molien/` | closed forms + coefficient tables in output.txt/results.json |
| G-3 | 2T Molien series (1+t¹²)/((1−t⁶)(1−t⁸)); Hilbert series 1/(1−t³) | `frontier/B267_e6_coherence/FINDINGS.md`; `frontier/B1068_descent_inventory/w2_full_results.json` | closed forms, computed exactly there |
| G-4 | Lee-Yang/(2,5) characters χ₁ = q^{...}G(q), χ_τ = q^{...}H(q), **with banked (c, h) in two conventions** (c = −22/5 and c = 14/5) | `frontier/B677_morning_packet/generation_leg/g1_tube/g1_run_log.txt` | stage-side characters as corpus artifacts — the exact analog of census class A4, absent from it |
| G-5 | divided-power series (q;q)_∞^{−3/5} (theorem cell: v₅(den cₙ) = n + v₅(n!)) | `frontier/B683_arithmetic_ledger/verify_divided_power.py` | object-side rational q-series |
| G-6 | ℚ(√−3) ideal-count series Σ #ideals(n)·qⁿ (verified there to n = 1500) | `frontier/B739_character_rigidity/b739_probe_out.txt` | weight-1 theta-type series of the object's trace field |

Minor location-level gaps in the NOT-COMPARABLE classes (kind already listed,
location not): B462's Masbaum twist-knot colored-Jones tower, B787
`D6_habiro_fib` Habiro cₙ, B771 W5-204 (u = q−1 Habiro expansion), B924's
colored-Jones vector. These add locations, not kinds; no disposition needed
beyond the existing class rows.

## 3. Disposition — all gaps run through T9's own instrument

`supplementary_census_run.py` exec's the machinery head of the committed
`kind_map_survey.py` (series engine, `c_eff_fit`, `kind_map`, `report`)
without editing it, re-arms the three MB12 controls **in this run** (plant-
valid PASSES with c_eff = 5.996; one-boson FAILS in the ONE-UNIT band at
0.999; seeded random PASSES K-ii and FAILS K-iv — bite = True), and
adjudicates eleven supplementary entries. Convention notes (E23): the raw
B674 Molien M has coefficient 3/2 + √5/2 ∉ ℚ at n = 0 (fails K-ii by
inspection, recorded in the log); its two faithful rational avatars M+M′ and
(M−M′)/√5 are what enter the kind-map. The B774 series were recomputed
exactly in ℚ(√5) from the banked closed forms (heads match the committed
cell 16/16 both). Provenance was read *generously toward the candidate*
where arguable (2T, B683, B739 as object-side), so kills land on computed
clauses, not on K-v alone.

**Result: 0/11 pass.**

| entry | first failed | exact violation |
|---|---|---|
| Lee-Yang χ₁, χ_τ (YL, c = −22/5) | K-iii | banked c = −22/5 ≠ 6 (K-iv also: c_eff ≈ 0.400; K-v: imported) |
| Fibonacci χ₁ (FIB, c = 14/5) | K-iii | banked c = 14/5 ≠ 6 (same K-iv/K-v) |
| B674 M+M′ | K-ii | n=1 coefficient **−4** |
| B674 (M−M′)/√5 | K-ii | n=1 coefficient **−2** |
| A5 Hilbert series | K-iii | untyped; K-iv c_eff ≈ 0.000 (polynomial growth) |
| A5 θ-odd twisted Molien | K-iii | untyped; K-iv c_eff ≈ 0.000 |
| 2T Molien | K-iii | untyped; K-iv c_eff ≈ 0.000 |
| 1/(1−t³) | K-iii | untyped; K-iv c_eff ≈ 0.000 |
| B683 (q;q)^{−3/5} | K-ii | n=1 coefficient **3/5** (non-integer) |
| B739 ideal-count series | K-iii | untyped; K-iv c_eff ≈ 0.004 |

No supplementary entry is, or approximates, a c = 6 boundary character.
The Lee-Yang rows are the sharpest addition: they are the corpus's ONLY
banked series besides (E6)₁ that carry a stated (c, h) — and both banked
conventions put c far from 6 with c_eff ≈ 2/5.

## 4. Independent (E6)₁ planted-character check (mandated)

Fresh code (not copied from the committed cell): E6 Gram = Cartan (own
labeling), direct 6-dim enumeration with saturation control (boxes ±6/±7
agree on norms 0..9; a first attempt at ±5/±6 saturated only to norm 5 —
confirming T9's clipping warning is real and the control bites), root count
72, Θ head [1, 72, 270, 720, 936]; χ = Θ/(q;q)⁶ head computed by own
convolution:

**[1, 78, 729, 4382, 19917] — CONFIRMED**, matching the committed
`survey_output.txt` line 16 exactly; anchors: 78 = dim E6,
729 = 270 + 72·6 + 27 verified by hand-decomposition of the convolution.

## 5. What this changes in T9's banked verdict

- **"EMPTY-CONFIRMED — census exhausted at 16 + 10"**: the count and the
  exhaustiveness clause are **REFUTED** (≥ 11 additional computable series
  entries across ≥ 6 missed objects/classes; the Molien class was invisible
  to both GC-12's and T9's token sets).
- **The operative emptiness** (no banked artifact passes the kind-map; σ's
  anchor status; the K-v-only status of the (E6)₁ character): **CONFIRMED
  and hardened** — it now holds at 27 computable entries (16 + 11), with
  controls biting in both the committed run and this one.
- T9's caveat 1 should be read as having FIRED, not merely as residual risk:
  the honest statement of the survey's result is operative emptiness under
  an open-ended census, not a closed count.
- Residual caveat (inherited, narrower again): a series artifact named by
  neither T9's tokens nor this cell's patterns could still exist; two
  disjoint sweeps now bound that risk from two directions.

## Reproduce

`python3 supplementary_census_run.py` from this directory (~3 min; numpy;
reads only the committed `kind_map_survey.py` head and the two banked JSONs
named above; writes `supplementary_output.txt`, `supplementary_results.json`
here). All gates assert; controls must bite or the run aborts.
