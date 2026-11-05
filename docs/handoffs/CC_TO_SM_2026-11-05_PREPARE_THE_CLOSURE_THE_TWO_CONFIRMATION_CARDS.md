# cc → the SM seat: preparing the closure — the physics of the two confirmation cards (2026-11-05)

*Direct, from main, at the owner's word (2026-11-05: "what else can we do to prepare, you can hire SM and Chat1 for
dividing tasks. its important that were prepared for a closure"). Recorded in docs/RELAY_LEDGER.md; P-686.*

## Where things stand

- **The record's one candidate** is THE SIX ON THE STRIP (B1829). It passes GENESIS v1.61's level-1 screen under B1798's
  matched null. It is not yet a result: a result needs a held-out confirmation, at least two quantities that are not
  functions of one another (GAP1, v1.60).
- **Its pass rests on an ansatz end** (B1838). THE END CARD, B1839 (sealed at c70b356f0, running today), decides whether it
  survives with a geometric end. The cut level would then be one fitted number, δ*.
  - **If it survives,** the candidate is frozen at its best row: apex, line, reading, c and δ*. Two level-2 cards are then
    sealed there.
  - **If it does not,** neither card runs. Your work below then serves the next candidate unchanged.
- **The two targets, fixed by the owner's rulings:**
  - **y_b/y_t (P-585).** The cleanest, never computed by main. Two unsealed seat exposures are counted in m_V.
  - **r = Δm²₂₁/Δm²₃₁ (P-638).** The owner ruled on P-665 (2026-11-05) that the PMNS card earns I-33's mass half only. The
    angles and the phase are not graded, and no held-out target may be scanned against data before its card (D11).

## The ask: four pieces, all data-free on the frame's side

- **S1. The y_b/y_t card's physics.**
  - **The reading.** B1832's S300 section: in any two-Higgs reading tan β absorbs y_b/y_t, so the ratio is held out only
    in a declared one-Higgs reading with shared normalisation. State that reading for the frame: (S̃, S, S), FR-FIB at
    a₀ = 0, or FR-COV with a₀ = ∓b₁₀, and write the normalisation condition that makes σ_max(down)/σ_max(up) the frame's
    y_b/y_t.
  - **The scale (P-574).** At what scale and in what scheme the frame's ratio is compared. The six are compared in B1741's
    data file (`frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json` through B1741's
    `compare.py`). Say whether y_b/y_t must use the same file and scale, and why.
  - **The theory error σ_th (P-575).** Which of the frozen row's fitted or chosen inputs propagate into the prediction: τ,
    c, δ* and the reading. Give the propagation rule, never its value at the row.
- **S2. The r card's physics.**
  - The neutrino reading: Dirac with B1799's pairing, against type-I or Weinberg. Main's draft is
    `audit/p638/DESIGN_DRAFT.md` § 2, summarised in B1835's FINDINGS § 2; a summary is in the relay ledger row.
  - σ_th for the ν sector, by the same rule as S1.
- **S3. GAP1 condition 4: are the two targets independent?** At the candidate's address, is r a function of y_b/y_t?
  - B1835 says r is independent of y_b/y_t by structure, but tied at leading order to the lepton hierarchy: the neutrino's
    within-sector gap is 1/20 on slope 2/5.
  - Write the argument, or the obstruction, with the frame's equations (B1656, B1799), not with numbers.
- **S4. The target data file.**
  - **Contents:** for each target, the measured value and its uncertainty, with provenance (source and version, scale,
    scheme), as a JSON committed on your branch.
  - **Pinning:** announce its sha256 in the relay. Main will not open it until its card runs, and the card will assert the
    hash.
  - **Never compare** any frame value with it.

## Firewall (binding)

- Do not compute the frame's y_b/y_t, y_τ/y_b, tan β, PMNS angles or phase, neutrino masses or splittings, or r, at any
  row or any τ.
- Nothing that compares such a frame value with data may reach the shared remote.
- If a check needs a frame quantity of that kind, describe it, and main computes it unread inside the sealed card.

## Timing

S1–S3 are wanted before B1839's verdict (expected 2026-11-05 afternoon), so the cards can be sealed the same day if the
candidate survives. S4 can follow.

*Nothing in this relay contains or implies a value of any held-out target.*
