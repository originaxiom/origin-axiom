# B1637 — FITS ON THE RULED BRANCH: with one τ the modular structure fits the charged fermions only with 21 or more parameters for 13 numbers; W53's negative on all 13 holds on main's code, its masses-only number did not; W54's "every structure with a sector at weight 3 fails" is refuted at Im τ ≈ 6.8

> *Audited 2026-10-15 by main (P-152, B1655): STANDS ONLY AS SCOPED (P ≥ 25 in the reliable region; T ⊗ T, odd weights {3, 5, 7}³, Im τ ≤ 10, search-bounded). The grades, the corrected wording and the checks are in `frontier/B1655_main_audits_its_negatives/FINDINGS.md`.*

**Verdict: PROVED** for the question it was sealed for (F3, F4 and F5 hold as sealed). F2 fails as worded: on the nine
masses alone main's optimizer reaches χ² = 20.6, not ≥ 100, and on all 13 at the widest allowance 397, not ≥ 1000. The
structure stays excluded on all 13 at every allowance. cc (main), 2026-10-14. Sealed `3ef9c3f8f` before the run; the
run took about 17 hours (63 fits, 60 starts each). Data: the charged-fermion masses and the CKM (value contact, the
owner's reopening). **0 of 19.** POINT_REGISTER P-013–P-016, P-076.

## 0. Seen first, and what was read after the seal (P-076)

As sealed: `VERDICT topic-sweep /fit|chi2|Huang|running mass|one tau|weight assignment/: 50 of 1408 arcs on main match`.
The SM seat's W52, W53 and its relay §57–§58 were read before the seal (disclosed there).
**Literature:** Huang and Zhou 2021 (the running masses, arXiv:2009.04851); PDG 2025 (the CKM); modular-flavour fits
(Feruglio 2017 and its sequels; Novichkov, Penedo and Petcov 2021 near the cusp), for the shape of the question.
- **Read after the seal and before this grading:** the SM seat's W54 headline, that five rank-13 structures fit, all
  with every sector at weight 5 or 7, and that every structure with a sector at weight 3 fails. It was relayed to main
  while the fit ran.
- The cells were sealed before it and are graded as sealed. §3 reads the result against W54.

## 1. The sealed cells (`verification/fits_on_the_ruled_branch.py`, unchanged; `fits_on_the_ruled_branch.json`, `fits_run.txt`)

| cell | prediction | prior | result |
|---|---|---|---|
| **F2** | (3, 3, 3), P = 11, a = 0.10: χ²_min ≥ 100 on the 9 masses and ≥ 1000 on all 13; the verdict the same at a = 0.05 and 0.20 | 80% | **FAILS as worded.** The 9 masses: 66.3, 20.6 and 12.3 at a = 0.05, 0.10 and 0.20 (W53 reported 163 at 0.10). All 13: 2406, 1101 and 397. Excluded on all 13 at every allowance, but below both sealed thresholds where marked. |
| **F3** | (3, 3, 3), each sector alone with its own τ: χ² < 3 each, and the best Im τ spread by more than 1 | 70% | **HOLDS.** χ² 4·10⁻²³, 1·10⁻²⁹ and 1·10⁻³⁰; best Im τ 6.66 (up), 5.09 (down) and 5.85 (leptons), a spread of 1.58 |
| **F4** | every assignment with u and d both at weight 3 has χ² > 13 on all 13 | 75% | **HOLDS.** (3, 3, 3) 1101, (3, 3, 5) 1072, (3, 3, 7) 1072 |
| **F5** | some assignment fits all 13 at χ² ≤ 13, and every one that does has P ≥ 15 | 55% | **HOLDS.** Eight fit; the smallest P is 21 (table below) |

**Every assignment's best fit on all 13 (a = 0.10).** An optimizer's minimum is an upper bound: a fit found is real,
but a failure is a statement about this search.

| (k_u, k_d, k_e) | P | χ²_min | τ at the minimum |
|---|---|---|---|
| (5, 7, 3) | 21 | 1.86 | 0.36 + 6.79i |
| (3, 7, 7) | 23 | 6.72 | −0.09 + 6.63i |
| (5, 7, 5), (5, 7, 7), (7, 7, 5), (7, 7, 7) | 25–29 | below 10⁻¹⁵ | Im τ 3.40–3.45 |
| (7, 5, 5), (7, 5, 7) | 25, 27 | 1·10⁻¹⁰, 2·10⁻¹⁴ | Im τ 2.76, 2.62 |
| (7, 7, 3) | 23 | 14.7 | 0.30 + 5.51i |
| (3, 7, 5), (5, 5, 5), (5, 5, 7) | 21–25 | 27–35 | — |
| all others | 11–23 | 60 to 1101 | — |

## 2. What it says

- **W53's negative on all 13 holds on main's own forms, code and optimizer.** (3, 3, 3) is excluded at every
  allowance (χ² 397 to 2406 for 13 numbers with 11 parameters). Its cause is confirmed: each sector alone fits, but at
  its own Im τ, spread by 1.58.
- **W53's masses-only number was an overestimate.** Main reaches 20.6 where W53 reported 163, because main's search
  goes to Im τ = 10 and finds its minima near 7. The exclusion rests on the CKM, not on the masses alone.
- **On this branch the modular structure fits only by spending more parameters than it explains.** Every fit has
  P ≥ 21 for 13 numbers, so none predicts a flavour relation.
- **Scope (P-014, P-016).**
  - This is one ansatz, not the principle: holomorphic modular couplings at one τ, with three independent sectors.
    The Higgs content is beyond Λ and is assumed, not derived; one 27_H relating Y_u, Y_d and Y_e is a different test,
    best posed at the unification scale.
  - The weight assignments are chosen, not derived.
  - So the honest statement is: under this ansatz on the ruled branch, all 13 flavour numbers are free.
- **Where the fits sit (P-015).** At Im τ between 2.6 and 7. The exact fits sit near 3.4, where |q| = e^{−π Im τ} is
  about 2·10⁻⁵, and the weight-3 lepton fits near 6.8. That is deep toward the cusp. Under the weave's uniform measure
  the principle's dynamics puts no weight there (B1629, as scoped in B1648), and in the fibre frame τ runs there (the
  SM seat's W62). Neither selects a τ, and the fits do not either.

## 3. Read against W54 (P-076)

- **Agreement.**
  - Every exact fit has every sector at weight 5 or 7, as W54 found: (5, 7, 5), (5, 7, 7), (7, 7, 5) and (7, 7, 7) fit
    exactly in both searches.
  - Every fit has P ≥ 21, so W54's "none predicts anything" holds.
- **W54 refuted on one sentence.** W54 says every structure with a sector at weight 3 fails, with χ² ≥ 110 for the
  leptons at weight 3. Main finds two fits with a sector at weight 3, both at Im τ ≈ 6.7–6.8, which W54's 164-point grid
  likely did not resolve:
  - (5, 7, 3) at χ² = 1.86, below W54's own threshold of 5.99;
  - (3, 7, 7) at 6.72.

  So the geometry's weight is excluded only when it is the weight of the quark sectors, not of every sector.
- **W54 fits that main's optimizer missed.** W54 found (5, 5, 5) and (5, 5, 7) at 5.33, and (7, 5, 5) and (7, 5, 7)
  failing at 26 and 28. Main reaches 34.5 and 34.9 on the first two and exact fits on the last two. Both searches are
  local, and the union of their minima is the record's best.
- **The count is unchanged by either search:** all 13 flavour numbers are free under this ansatz.

## 4. Files

`verification/fits_on_the_ruled_branch.py` (sealed, unchanged), `fits_on_the_ruled_branch.json`, `fits_run.txt`;
`received/` (the inputs, hashed); the lock `tests/test_b1637_fits_on_the_ruled_branch.py`.

## Addendum (2026-10-21, Review 66; P-124, the reliance census)

> *Tagged 2026-10-21.* Review 66's reliance census found this arc relying on seat results that are not verified on main, and its `rests_on_seat` field does not declare them, so the gate seat-positive-verified could not see them. W62 (row 1115, headline, partial) is cited in an aside on where τ runs. They are the seat's, unverified (harvest rows named); the verifications are queued by consequence (P-229). The cells and numbers are unchanged.
