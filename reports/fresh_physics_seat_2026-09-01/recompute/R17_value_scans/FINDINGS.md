# R17 — B1126 / B1137 value-disjointness scans (committed-instrument re-run + value-free instrument audit)

Cell: `reports/fresh_physics_seat_2026-09-01/recompute/R17_value_scans/` — Ring R2, 2026-09-01.
Gate-5 exception invoked exactly as chartered: the committed instruments already contain the
sealed SM targets; they were re-run byte-faithfully (no new measured value, no new pairing
introduced anywhere in this cell; the planted controls are pure object-side regulator
combinations and synthetic numbers).

## Reading discipline (what was read when)

- BEFORE any code: `frontier/B1126_identification/FINDINGS.md` (head, claims + banked numbers)
  and `frontier/B1137_regulator_probe/FINDINGS.md` (head, same).
- This is a committed-instrument re-run cell, so the instruments themselves
  (`b1126_compare.py`; `pslq_probe.py`/`basis.py`/`verify.py`/`surrogates.py`/`targets.py`/
  `aggregate.py`) were then read as the object of the re-run and audit — the cell's mandate,
  not a blind-first breach. My own audit code (`b1126_audit.py`, `b1137_planted.py`) was
  written after reading the instruments, before reading any of the arcs' tests or NOTES
  beyond the FINDINGS heads. `B1137/PREREG.md` §E (outcome grammar) was read AFTER the
  planted control had already produced its result.

## Part 1 — byte-faithful re-runs

### B1126 (V-3): verdict MATCH

- Ran the committed `b1126_compare.py` unmodified (cwd = `b1126_rerun/`).
- Output `V3_results.json` is **JSON-identical to the banked `b1126_results.json`** (full
  dict equality including the 352-row table).
- Banked numbers reproduce exactly: 16 sealed periods x 22 targets = 352 pairs; sig-fig
  histogram {0: 344, 1: 7, 3: 1} → **351 below 2 sig figs**; the single ≥3-sig-fig pair is
  C1/C0 = 11π/(36√3) vs sin(θ12 PMNS), rel_diff = 2.53874e-4; look-elsewhere p = 0.1637
  (banked "≈16.4%"); expected-by-chance 3.52 @≥2sf (observed 1 cumulative, 0 at exactly
  2sf), 0.352 @≥3sf (observed 1). Final verdict string identical.

### B1137 (regulator probe)

- Ran the committed pipeline unmodified from `b1137_rerun/`: `pslq_probe.py real`
  (216 cells), `pslq_probe.py null --n-surrogates 100 --seed 17` (400 cells), `aggregate.py`.
- Diff vs banked `results/final_report.json`: recorded in the appendix below.
- **Prose/artifact discrepancy inside the banked arc (pre-existing):** FINDINGS.md and
  arc_verdict.json say "384-cell matched null (96 per H)"; the committed
  `results/final_report.json` says n=100 per H → **400 null cells**. Verdict-irrelevant
  (rates 0.0 either way) but banked prose does not match the banked artifact.
- Controls re-run independently: 9√3·ζ_K(2)/π² = 2.029883212819307250042405... = Vol(m004)
  (≥50 digits); 2√5·L(1,χ₅) = 4·log φ to ≥97 digits. MATCH.

## Part 2 — value-free instrument audits

### (a) B1126 — comparator power and dismissal mechanics: SOUND, with one hardcoding note

- `sig_figs_agree` (replicated verbatim, synthetic inputs only): rollover pair
  1.99999995 vs 2.00000001 → 7 sig figs (the arc's own fixed-bug case; no rollover
  collapse); planted 1e-4 / 1e-6 pairs → 4 / 6; far pair → 0. The comparator has power at
  and beyond the 3-sig-fig escalation bar.
- **Planted positive through the verdict branch** (the exclusion-control this cell owes):
  the top-level verdict flips mechanically on `look_elsewhere_verdict.startswith('NOTABLE')`,
  i.e. on the computed p_LE = 1−(1−2·rel)^352 vs the 0.02 threshold. A synthetic survivor at
  rel = 1e-5 (p_LE = 0.0070) or 1e-6 (p_LE = 0.00070) → **NEEDS-INSTRUMENT**: the banked
  negative COULD have failed. Break-even rel ≈ 2.9e-5 (~4.5 sig figs). Honest corollary: any
  hit in the 3–4-sig-fig band is dismissed by look-elsewhere in a grid this size by
  construction; the scan has claiming-power only from ~4.5 sig figs up — defensible, and
  pre-stated by the seal.
- Dismissal of the near-miss: ground 1 (look-elsewhere) is **computed** and gates the
  verdict — mechanical as claimed. Ground 3 (pre-commitment) is hardcoded `False`, true by
  construction for an exhaustive scan. Ground 2 (instrument-existence) is a **hardcoded
  `False`** backed by a grep the script does not itself run; re-ran it this bench: no
  tracked-.md line co-locates Kashaev vocabulary with neutrino/PMNS/θ12 vocabulary
  (file-level co-occurrences exist but are B1126's own writeups / unrelated sections).
  Ground 2 stands, but it is an assertion-in-code, not an executed check.
- Cosmetic defect: each survivor's `final_disposition` string is a constant ("fails all
  three grounds") independent of the computed flags — had a survivor passed look-elsewhere,
  the per-pair text would still read "fails look-elsewhere" even as the top-level verdict
  correctly flipped. Verdict-safe (the top-level branch is computed) but worth knowing.

### (b) B1137 — planted positive: THE INSTRUMENT COULD NOT HAVE FOUND A RELATION → VACUITY

Planted the true relation **5V − 3·L(1,χ₋₃) − 2π = 0** (object-side only, coefficient
height 5, two basis elements involved) and fed V through the committed `run_cell` unmodified
(`b1137_planted.py`, results in `b1137_planted_results.json`):

| digits budget | D,H | PSLQ found? | gates | outcome |
|---|---|---|---|---|
| 250 | 1, 100 | YES — exact planted coeffs [0,−5,3,…,2(π)…] | involves_V ok, involves_regulator ok, height ok (slack 112.6) | **exact_stable FALSE** (resid_hi 141.8 digits < required 116+60) → rejected |
| 250 | 1, 1e6 | NO (tol 1e-257 below the truncation/parse floor) | — | not found |
| 60 (prereg floor) | 1, 100 / 1, 1e6 | NO | — | not found |
| 10 (= best real target, m_p/m_e) | 1, 100 / 1, 1e6 | NO | — | not found |

Structural reading (confirmed in code): `run_cell` parses V at mp.dps = dps+25, while
`exact_reverify` demands the residual shrink past dps + BOOST/2 = dps+60 — so a genuine
relation involving any (irrational) regulator can NEVER pass the stability gate for a
truncated-decimal V: the residual is pinned at the truncation floor (≤ digits budget, itself
capped at dps+25 < dps+60). For the real targets (digit budgets 0–10) a regulator-involving
candidate cannot even be FOUND (its residual ~1e-10 vs tol ~1e-106..1e-257). The only
findable relations are the V-alone rational tautologies, which the `involves_regulator` gate
then rejects — exactly what the banked grid shows (10/18 targets found=12, all invReg=0).

**Therefore the positive terminus (ADMITTED / HIT-CANDIDATE) is unreachable for every
physically measured target at every one of the 216 cells, and the matched null's 0.0 base
rate is guaranteed by the same mechanism** (surrogates are truncated to the same digit
classes — the arc's own surrogates.py docstring says truncation "destroys the exact planted
relation"). The banked DISJOINT is TRUE and reproduces, but the check could not have failed:
**VACUITY** by this seat's definition. By the arc's own sealed outcome grammar (§E, read
after the control ran), the honest verdict was arguably **FLOOR** ("the decisive (D,H) or
precision is out of reach") — for every target: the decisive precision is ~(dps_search+60)
exact digits of the SM value (≥176), vs a best physical budget of 10 (m_p/m_e).

What survives of B1137 unconditionally: the regulator machinery is correct (controls to
50/97 digits); the V-alone-tautology hygiene works as documented (δ_CP→4, m_s/m_d→20
caught); and the literal statement "no exact bounded-height relation exists for the
truncated decimals" is true — but that statement is decidable a priori (a rational V cannot
lie in a ℚ-lattice over irrational, ℚ-independent regulators with nonzero coefficient), so
the 216-cell scan adds no evidence about the SM values themselves.

## Verdicts

- **B1126 (V-3): MATCH.** Byte-identical re-run; all banked numbers reproduce; the
  exclusion has a working planted-positive escape path (verdict flips at rel ≲ 2.9e-5);
  dismissal grounds verified (one hardcoded-but-externally-true, noted).
- **B1137: MATCH on bytes, VACUITY on substance.** The committed pipeline reproduces its
  banked outputs, but a planted true regulator relation is rejected (or unfindable) at every
  digit budget a physical measurement can supply — an instrument that could not have found a
  relation. The banked DISJOINT should be read as FLOOR (per the arc's own §E) with respect
  to the physical question. Also: banked prose says 384 null cells, banked artifact says 400.
- **Cell verdict: PARTIAL** (one MATCH, one VACUITY).

## Appendix — B1137 re-run diff

(completed)

Completed 2026-09-01, this bench (4 workers; real 216 cells in 834 s, null 400 cells in ~24 min).

- `b1137_rerun/results/final_report.json` vs banked
  `frontier/B1137_regulator_probe/results/final_report.json`: **DICT-IDENTICAL** (every field:
  M_grid_cells=216, alpha_cell=2.3744e-4, all four null rates 0.0 at n=100, all 18 per-target
  rows, overall_verdict=DISJOINT, dps_by_H={100:116, 1000:154, 10000:191, 1000000:267}).
- Re-run real grid intermediate: 216 rows, found=117, involves_V=117, involves_regulator=0;
  found distribution: alpha_s 12, |Vus| 12, |Vcb| 12, |Vub| 9, sin^2(th12) 12, sin^2(th23) 12,
  sin^2(th13) 12, delta_CP 12, m_c/m_b 12, m_s/m_d 12 — matches the banked per_target table
  exactly (and the arc's own "117 found cells" note in pslq_probe.py).
- Second prose/artifact mismatch noted for the record: banked FINDINGS says "Only delta_CP and
  m_s/m_d produced any stable, height-legal, within-1sigma relation"; the committed report
  shows TEN targets with found=12 V-alone relations, and NONE of them (delta_CP and m_s/m_d
  included) marked height-legal/stable/within-1sigma — the gate short-circuits at
  involves_regulator before those checks run. Verdict-irrelevant; narrative imprecision only.
