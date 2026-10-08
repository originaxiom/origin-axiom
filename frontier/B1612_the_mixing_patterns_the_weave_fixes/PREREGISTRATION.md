# B1612 — PREREGISTRATION: THE MIXING PATTERNS THE WEAVE FIXES — every mixing pattern the weave's own group fixes by residual symmetries (no free parameter), and their contact with the leptonic and quark mixing data

cc (main), 2026-10-08, after S90. The first value-contact arc under the owner's reopening of 2026-10-08 (`docs/KIND_TABLE.md`,
"The reopening"). A weave arc: exact finite-group computations on the weave's flavour group on the matter triplet T, then
one sealed comparison. **Sealed before `mixing_on_the_weave.py` computes any cell and before any data is read.** The
patterns are |U|²-type (probability kind): admissible against the moduli of the mixing matrices (KIND_TABLE). 0 of 19.

## Seen first

`VERDICT topic-sweep /PMNS|tri-?bimaximal|TM1|TM2|CKM|Cabibbo|NuFIT|residual symmetr|mixing pattern/: 21 of 1383 arcs on main match (NEGATIVE 8, PROVED 13)`
— on one thread (m004): B342 (its ℤ/3 gives TM2, θ₁₂ = 35.7°, disfavoured relative to TM1), B343 (its deck ℤ/3 on the
Klein 2-torsion forces exact TBM, θ₁₃ = 0), B467 (a CKM scan's earned zero), B631, B861; the value campaign's NEGATIVEs
(B1063, B1066: both golden relations excluded by NuFIT 6.1, Nov 2025; B398: a PMNS formula ensemble banked as
numerology). The SM seat's §3 (READING): with the golden 3-cycle the swap fixes the TM1 column, the sign or a fibre
translation TM2, a single shear the third column (0, ½, ½) — with the swap among its generators, which B1610/B1611 put
outside the chiral weave. B1611 (the weave's group, its 96 automorphisms; CP is the swap); W33 (lane `bc4ea1303`). Nothing
on main computes the full set of patterns the weave's group fixes. **Literature:** C. S. Lam (2008), the residual-symmetry
rule; the classical patterns (TBM: Harrison–Perkins–Scott; TM1/TM2 families) — cited from the reviewer's knowledge.

## Disclosed

- The instrument computes the predictions; the comparison script is sealed with it, so the predicted set is fixed by
  the seal before any data is read. No cell has been computed (both scripts only compiled).
- **The data, named before reading:** NuFIT, the newest release on nu-fit.org at fetch time (6.1 or later): the 3σ
  ranges of the moduli |U_ij| for normal and inverted ordering (the release's |U| matrix, with the Super-Kamiokande
  atmospheric data where the release offers both). PDG, the newest Review of Particle Physics, section "CKM
  quark-mixing matrix": the global-fit moduli |V_ij| with their uncertainties. Transcribed into `data.json` after the
  seal, with URLs, release names and fetch dates; the transcription disclosed.
- The flavour group is G's image on T; the swap is not in G (B1611). Residual symmetries are taken as Lam's rule
  states; Majorana or Dirac nature is not distinguished (a two-generated subgroup covers the Klein case).

## Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **M1** | G acts faithfully on T (image of order 96) | 70% |
| **M2–M3** | a finite set of fully fixed patterns; the tri-bimaximal pattern (θ₁₃ = 0) among them | 75% |
| **M4** | the one-column patterns include the TM2 column (⅓, ⅓, ⅓) | 70% |
| **M4′** | they include the TM1 column (⅔, ⅙, ⅙) | 50% |
| **D1** | no fully fixed pattern lies inside NuFIT's 3σ ranges on all nine |U_ij|, in either ordering | 85% |
| **D2** | no fully fixed pattern, nor the identity, lies within 3σ of PDG's |V_ij| | 97% |
| **D3** | at least one fixed column lies inside NuFIT's 3σ ranges for some column of U | 60% |

**The reading, written before the run (the cells can only lower it).** If D1 and D2 hold: the weave's group, through
residual symmetries alone, cannot produce the observed mixings without a free parameter; like the CP phase (B1611), the
mixing angles live in the couplings. If D3 holds: the weave fixes one column of the leptonic mixing matrix — a
one-parameter relation, not a parameter-free value — graded a READING (which sector is the leptons is FK11's
dictionary, unearned). If a fully fixed pattern survived D1 or D2, it would be a parameter-free prediction of mixing
angles, graded a READING for the same reason, with the look-elsewhere count (M5) stated beside it. **The imported
expectation, stated separately:** the measured mixings — large leptonic angles with θ₁₃ ≈ 8.5°, small quark angles with
|V_us| ≈ 0.22 — are known to the reviewer; the priors above are informed by them.

## Instruments

`verification/mixing_on_the_weave.py` (the patterns; no data), `verification/compare.py` (the comparison, run once on
`data.json`); hashes in `ARTIFACT_HASHES.txt`.
