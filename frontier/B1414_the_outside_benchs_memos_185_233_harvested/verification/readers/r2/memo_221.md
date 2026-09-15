# Reader r2 — Memo 221 (MUELLER_ANSWERS_MEMO_210.md)

## 1. HEADLINE
"MEMO 210's TWO QUESTIONS ANSWERED: the linear coefficient is exact, and the constant is not a
constant." No cell-outcome grid (no seal — "verifies a banked computation against statements read
verbatim from two papers... supplied as PDFs by the owner on 2026-09-13"). Banked "1B,
2026-09-13" per `INDEX.md`.

## 2. CLAIMS
1. Memo 210 fitted `log|τ_m| = A·m² + B·m + C` on B581's **six exact torsions**, measuring
   `A/(Vol/π) = 1.000781734`, `B/(Vol/π) = 0.9861960956`, and left the linear coefficient and
   constant `C` unidentified (explicitly declined, citing B583's X2 PSLQ-overclaim precedent).
   Grade (memo 210's own): measured, not identified.
2. **Q1 answered YES for closed manifolds**: Müller's Corollary 1.2 gives only `O(m)` and does not
   pin the linear term, but his **sharp formula at the end of §8** (quoted verbatim) gives
   `log T_X(τ_{2m}) = log T_X(τ₄) + Σ_{k=3}^m log|R_{2k}(k)| − (1/π)·vol(Γ\H³)·(m(m+1)−6)`, i.e.
   the combination is **exactly `m(m+1)`** — the theorem makes `B/(Vol/π) = 1`, vs. memo 210's fit
   of 0.9862. MFP eq. (2) independently quotes the same combination. Grade: **PROVED, for closed
   hyperbolic 3-manifolds** (a citation, not a new derivation — but the quoted formula is checked
   against memo 210's own numbers below).
3. **Scope claim, load-bearing**: Müller's Theorem 1.1 explicitly requires X **closed**; MFP (who
   handle the cusped case) prove only the **leading term**
   `lim log|T_{2k+1}(M)|/(2k+1)² = −Vol(M)/4π`, not the `m(m+1)` refinement. The figure-eight
   complement is **cusped**. So the `m(m+1)` refinement is **NOT established for `4₁`** by either
   paper. Grade: documentary/scope, verified by direct quotation of both papers' stated hypotheses.
4. Interpretive: memo 210's six exact integers on a **cusped** manifold obey the closed-manifold
   refinement to a spread of **0.0123242** — read as "evidence for an extension neither paper
   proves," not as a verified theorem for `4₁`. Grade: interpretive, correctly labelled as such.
5. **Q2 answered: there is no constant.** Müller's formula names the residual as
   `log T(τ₄) + 6·Vol/π + Σ_k log|R_{2k}(k)|`, a **bounded, decaying** Ruelle sum (his Lemma 8.1).
   So memo 210's drift was never going to identify a constant — it was measuring that sum
   converging. Grade: structural, from the cited theorem.
6. Computed here: consecutive exponents extract Ruelle terms directly from B581's banked numbers —
   `log|R₁₀(5)| = R₅−R₄ = +0.0104577255`, `log|R₁₆(8)| = R₈−R₇ = −0.0002468702556`. Magnitude ratio
   across three steps: **42.361**, bracketed by `e^{3ℓ₀}=26.081` and `e^{3.5ℓ₀}=44.914` at systole
   `ℓ₀=1.087070144995739` (SnapPy) — i.e. decay rate between `e^{−ℓ₀}` and `e^{−1.3ℓ₀}` per step.
   **The sign flips** (−0.01046 → +0.0002469), consistent with oscillating geodesic terms carrying
   imaginary part `±1.7228i` at the systole — "a constant cannot change sign; a Ruelle sum must."
   Grade: **computed here, PASS** as a discriminating fact for claim 5.
7. R-values banked: `R_1=−0.19365150021, R_4=−0.451374208632, R_5=−0.461831934135,
   R_7=−0.463698384356, R_8=−0.4634515141, R_11=−0.463653214704`. Grade: raw data, restated from
   B581 (not independently re-derived in this memo — cited as "R values banked here").
8. Memo 210's refusal to identify `C` is **vindicated for a better reason than it knew**: there was
   never a constant to identify; any PSLQ hit would have fit the partial sum of a convergent series
   — "the exact failure mode B583's X2 was retracted for." Grade: interpretive, well-supported by
   claims 5–6.
9. Filed as a **correction by addendum, not a rewrite** — memo 210's cells, numbers, outcomes stand
   unchanged; only SS7's "neither claimed" successors are discharged.

## 3. CERTIFICATE
- **No seal** (explicitly stated, and appropriate — this memo verifies literature-derived formulas
  against an already-banked computation rather than pre-registering a new empirical branch).
- **Certificate:** `outside_bench/certificates/mueller_answers_memo210.py` — **exists**.
- **Output:** `outside_bench/outputs/mueller_answers_memo210.txt` — **exists**. Tail:
  ```
  Q1 'is the linear coefficient exactly Vol/pi?'
     ANSWERED YES FOR CLOSED hyperbolic 3-manifolds -- [Mul]'s exact m(m+1).
     For the CUSPED figure-eight it remains UNPROVED; ... spread of 0.01232.
  Q2 'what is the constant C?'
     IT IS NOT A CONSTANT. ...
  ```
  **Agrees exactly** with the memo's headline and claims 2–5 (same numbers: 0.01232 spread,
  the `m(m+1)` combination, the "not a constant" verdict).
- Ruelle-term numbers in the output file's body (`log|R_10(5)|`, `log|R_16(8)|`, the ratio 42.361,
  and `e^(3 l_0)=26.081088`, `e^(3.5 l_0)=44.913818`) match claim 6 verbatim, including the
  systole value to full precision. **No discrepancy found between memo prose and output file.**

## 4. ON MAIN ALREADY?
1. **B581 (the six exact torsions this memo builds on):** **(a) already on main** —
   `frontier/B581_six_torsions` exists as a tracked arc directory (confirmed via `find`).
2. **Memo 210 itself (the arc this memo answers):** lives in `outside_bench/memos/`, i.e. inside the
   merged outside_bench tree — present on main as a *file*, but **(c) NOT cross-cited** in
   `docs/HARVEST_LEDGER.md` or `docs/CAMPAIGN_STATUS.md` by name/number (`grep -n "Mueller"
   docs/HARVEST_LEDGER.md docs/CAMPAIGN_STATUS.md` → no hits; `grep -n "memo 210\|memo 221"` in
   either file → no hits). The Müller/MFP citation and the `m(m+1)` result do not appear anywhere
   in the tracked `frontier/` or `docs/` governance layer outside `outside_bench/`.
3. **The cusped-vs-closed scope caveat (claim 3), which is the single most important fact in this
   memo:** (c) NOT reflected anywhere on main outside this memo — there is no doc stating "the
   figure-eight's `m(m+1)` torsion growth is UNPROVED for the cusped case, only observed to 0.0123
   spread." This is exactly the kind of caveat that risks being flattened into an unqualified
   "verified theorem" claim if picked up loosely by a later summary; a verifier should specifically
   check that any future citation of this result on main (paper drafts, `docs/THE_LADDER.md`, etc.)
   carries the closed-vs-cusped distinction. As of this reading, no such citation exists yet, so
   there is nothing to catch it doing so incorrectly — but the risk is worth flagging for future
   harvesting.
4. **No contradiction found** anywhere on main against any of this memo's numbers or scope
   statements.

## 5. NEEDS COMPUTATION HERE
- **Claim 2 (the `m(m+1)` fit):** re-fit `log|τ_m| = A·m² + B·m + C` on B581's six exact torsions
  (values in `frontier/B581_six_torsions`) and confirm `B/(Vol/π)` sits at `0.9861960956` as memo
  210 reported, then separately confirm that forcing `B/(Vol/π)=1` (the theorem's value) changes
  the residual fit by the stated spread `0.0123242` at the outlier point — this is the single
  discriminating fact behind "six exact integers obey it to a spread of 0.0123."
- **Claim 6 (Ruelle-term decay/sign flip):** recompute `R_5−R_4` and `R_8−R_7` directly from the
  seven banked R-values (claim 7) and confirm the two increments equal `+0.0104577255` and
  `−0.0002468702556` to the stated precision, then recompute the systole `ℓ₀` via SnapPy on `4₁`
  (`M.length_spectrum()` at the shortest geodesic) and confirm `ℓ₀ = 1.087070144995739` and the
  imaginary part `±1.7228i`.
- **Documentary check:** confirm Müller's actual arXiv text (`1003.5168v1`) states Theorem 1.1 for
  **closed** manifolds only, and that the §8 sharp formula is exactly as quoted — this is a direct
  textual verification against a source PDF, not a numeric computation, but is the load-bearing
  citation for the entire memo and should be checked against the actual paper text if available.

## 6. SUPERSESSION
Not superseded — no later `outside_bench/INDEX.md` row references "memo 221" by number except a
routing note ("memo 221) and memo 204's E-question (memo 222)"), which is an index cross-reference,
not a correction. Memo 221 explicitly frames itself as correcting memo 210 by addendum (claim 9),
not the other way around — memo 210's own cells/numbers/outcomes are stated to stand unchanged.

## 7. GRADE PROPOSAL
**REPRODUCE-AND-BANK.** This is real, cheaply-checkable arithmetic (a linear fit re-derivation and
a systole/Ruelle-decay recomputation) built on an already-banked exact dataset (B581), reading a
genuine theorem correctly and — critically — stating the scope caveat (closed vs. cusped) that
keeps it from being over-claimed. It is not yet cited anywhere in `docs/` or `frontier/`'s
governance layer, so a verifier reproducing claims 2 and 6 and then filing a proper frontier arc
(with the cusped-vs-closed caveat carried forward explicitly, per this memo's own discipline) would
convert a sound outside-bench finding into a bankable main-line result.
