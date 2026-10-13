# B1637 — PREREGISTRATION: DOES ANY MODULAR STRUCTURE ON THE RULED BRANCH FIT THE CHARGED FERMIONS WITH ONE τ? (main's check of the SM seat's W53, and its open question)

cc (main), 2026-10-13. **Sealed before `fits_on_the_ruled_branch.py` runs.** Data: charged-fermion masses and the CKM
(value contact, reopened by the owner on 2026-10-08; the checklist below). 0 of 19.

**Why it matters.** On the ruled branch τ breaks the weave's group, so the Yukawas are values of modular forms at one τ
(B1634, B1635). The SM seat's W53 fitted the one structure on record that both fits and predicts (T ⊗ T at weight 3 in
every sector, 11 parameters for 13 numbers) and found it excluded: χ²_min 1887 on the 13, and 163 on the 9 masses
alone. Its cause, predicted beforehand, is that each sector reaches its hierarchy at its own Im τ, and the weave gives
one τ. If that holds, every structure that predicts a flavour relation is excluded, and all 13 flavour numbers are
free on this branch. The seat left open whether any structure fits at all. The owner's rule says a negative is
audited before anything is built on it. This arc re-derives the negative with main's own forms, code and optimizer, and
asks the open question.

## Seen first

`VERDICT topic-sweep /fit|chi2|Huang|running mass|one tau|weight assignment/: 50 of 1408 arcs on main match (NEGATIVE 11, OPEN 4, PROVED 35)` — the SM seat's W52 and W53 and its relay §57–§58 (read, with its numbers); B1612 (the CKM data on
main), B1634, B1635 (main's forms), B1636 (the sum rule). **Literature:** Huang and Zhou 2021 (the masses); PDG 2025
(the CKM); modular flavour models' fits (Feruglio 2017 and its sequels), for the shape of the question.

## Disclosed

- **Not blind.** W53's χ² values and per-sector best y were read before this seal, and the predictions use them.
- **The inputs were checked against the source before the seal.**
  - The masses are Huang and Zhou 2021 (arXiv:2009.04851v2), Tables 2 and 3, the row "M_Z, Full SM".
  - The PDF was fetched again on 2026-10-13. Its sha256 is baeddc97…, identical to the seat's record, and both rows
    match the seat's transcription digit for digit. The transcription is copied to `received/`.
  - The CKM values are main's own B1612 copy of PDG 2025 eq. (12.27), equal to the seat's.
- **Main's route and the seat's conventions.**
  - The forms are B1635's: polynomials in θ², with η¹⁸ cleared and the cusp condition.
  - The theta series, the optimizer (scipy least squares, multi-start over the fundamental domain with Im τ ≤ 10) and
    all the code are main's.
  - The observables, the log-scale χ² with its 10% running allowance and the profiled scales follow W53, because W53 is
    what is being checked.
- **Smoke test before the seal.** The forms were built (dimensions 2, 4 and 5 at weights 3, 5 and 7) and one residual
  was evaluated at an arbitrary point (13 finite numbers). No fit was run.
- **An optimizer's minimum is an upper bound.** "Fails" means that no start found a lower χ². A failure is a statement
  about this search, not a proof of exclusion, and it will be reported that way.
- **The value-contact checklist.**
  - Kind: a fit of a structure, not a value derived.
  - Sources: cited, hashed and checked.
  - Scale: M_Z, with a stated running allowance.
  - Tolerance: fixed above.
  - The data were read before this seal, which is disclosed.

## Cells, predictions, priors

P is the structure's number of real parameters, 2 + Σ_s (2 d(k_s) − 1): τ, plus the coefficients modulo one phase per
sector, including the three scales.

| | prediction | prior |
|---|---|---|
| **F2** | (3, 3, 3), P = 11, a = 0.10: χ²_min ≥ 100 on the 9 masses and ≥ 1000 on all 13 (the seat: 163, 1887); the verdict the same at a = 0.05 and 0.20 | 80% |
| **F3** | (3, 3, 3), each sector alone with its own τ: χ²_min small (< 3) for each, and the best Im τ of the three sectors spread by more than 1 | 70% |
| **F4** | over (k_u, k_d, k_e) ∈ {3, 5, 7}³ (P from 11 to 29), every assignment with u and d both at weight 3 has χ²_min > 13 on all 13 | 75% |
| **F5** | some assignment fits all 13 at χ²_min ≤ 13, and every one that does has P ≥ 15 > 13 (it predicts no flavour relation) | 55% |

**The reading, written before the run (the cells can only lower it).**
- **If F2 and F3 hold,** W53's negative is verified on main by an independent route, and its cause is confirmed: one τ
  cannot set three hierarchies that each want their own.
- **If F5 holds,** the modular structure on the ruled branch can fit the charged fermions only with at least as many
  parameters as observables. So the principle, read this way, leaves all 13 flavour numbers free (all 19 with the
  rest, given Λ). That is the honest answer to "how many free numbers": all of them, on this branch.
- **If no assignment fits** (F5 fails that way), the modular structure with one τ is excluded as the Yukawas' source
  on the ruled branch, within this search.

## Instruments

`verification/fits_on_the_ruled_branch.py`; data `received/HZ2021_running_masses_MZ.json` (and B1612's
`data.json`); hashes in `ARTIFACT_HASHES.txt`.
