# ADDENDUM (2026-09-01, fresh physics seat) — DISJOINT byte-reproduces, but the gate is structurally unpassable at physical precision: the PREREG §E outcome type was FLOOR. Proposal, not a re-grade.

**Scope.** Ring R2 cell R17 re-ran this arc's committed pipeline byte-faithfully (real 216
cells, matched null, aggregate): the output is **dict-identical** to `results/final_report.json`
(DISJOINT; 0 regulator relations; null rates 0.0; α_cell 2.374e-4; controls to 50+/97+ digits).
This note records what the same re-run showed about the instrument. It proposes a
reclassification under the arc's own PREREG grammar; the grade change itself is the banking
seat's to make. Original FINDINGS.md / PREREG.md left unedited.

**The mechanism (read directly from the committed code).**
- `pslq_probe.py:38–45`: the target value V is **truncated to the target's own digit count**
  (`nstr(V_full, d_use)`) before the search; the working precision is `dps + 25`.
- `verify.py:52–60`: the stability gate recomputes the residual at `dps_search + BOOST` with
  BOOST = 120 and demands `resid_hi_digits > dps_search + 60`.
- A **true** relation involving a target known to d digits has residual pinned at ~10⁻ᵈ (the
  truncation), never at 10^−(dps+60). So for every physically measured target (best case 10
  digits, m_p/m_e) the ADMITTED/HIT terminus is unreachable **for any coefficient vector**,
  and the matched null's 0.0 is produced by the identical mechanism (surrogates truncated the
  same way).

**Planted-positive control run through the committed `run_cell` unmodified** (R17,
`reports/fresh_physics_seat_2026-09-01/recompute/R17_value_scans/`): the exact relation
5·V − 3·L(1,χ₋₃) − 2π = 0 (height 5, inside the searched box) is
- **found but rejected** at digits = 250 (PSLQ returns the exact coefficients; `exact_stable`
  fails because the residual sits at the parse floor dps+25 while the gate wants dps+60);
- **not found** at digits = 60 (the PREREG floor) and digits = 10 (best physical target):
  truncation residual ~1e-10…1e-60 against a tolerance of 1e-106…1e-257.

The instrument therefore has zero power on the question it was built to answer at every one of
the 216 cells; the decisive precision is ~176+ exact digits against a best physical budget of 10.

**Proposal.** By PREREG §E the honest outcome type is **FLOOR** ("the decisive (D,H) or
precision is out of reach → typed honest-open, with the reached bound stated"), with the reached
bound = "no relation of height ≤ 10⁶, degree ≤ 3, detectable at ≥ dps+60 stable digits — a
threshold no physical target can meet". DISJOINT as banked reads as a contentful negative; it
is not one. Either (a) reclassify to FLOOR, or (b) fix the gate (compare the boosted residual
against the *target's* digit count, not against dps+60) and re-run; (b) would make the
matched-null calibration meaningful for the first time.

**Two arc-internal mismatches found on the same pass (verdict-irrelevant, prose-level).**
(D7a) FINDINGS.md:37/42 and `arc_verdict.json` say a 384-cell matched null (96/H); the
committed `results/final_report.json` has 400 (100/H, seed 17, n = 100) and no committed
configuration reproduces 384. (D7b) FINDINGS says only δ_CP and m_s/m_d produced "stable,
height-legal, within-1σ" relations; the committed report shows ten targets with V-alone finds
(117 total) and **none** marked stable/height-legal — the gate short-circuits earlier.

**Assumption carried.** The pruned 25-element basis is taken to be ℚ-linearly independent with
1, as the arc asserts; `basis_hygiene_check.py` is not in the arc dir. The parse-cap-vs-gate
mismatch holds regardless.

Ledger: R2_REPORT V8 (seat: ENDORSED, code-structure confirmed), D7. Error-class E27/E40
(a check that cannot fail) — the load-bearing instance of the ring.
