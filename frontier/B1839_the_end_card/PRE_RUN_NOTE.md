# B1839 — PRE-RUN NOTE: provenance corrected, one voidness rule, the frozen row settled (before `look.py` runs)

cc (main), 2026-11-05, before `look.py` has run (B1839's census still running). Credit: the web seat's verification of the
seal, `relays/CHAT1_TO_CC_2026-11-05_THE_OVERNIGHT_VERIFIED.md` § 4 (1a7861df3), each item re-checked by main. Nothing here
changes a cell, a threshold, a prior or an instrument; the sealed PREREGISTRATION (dc05a5c4…) and instruments stand.

## Provenance, corrected

1. **The web seat's E2 pin.**
   - `ARTIFACT_HASHES.txt` and `look.py`'s comment give the sha256 7f1502d9… for
     `relays/chat1_2026-10-28_exact_end/exact_end_look.json @ 4aa66ca45`. That hash belongs to main's re-run copy (P-595):
     the re-run in the seat's worktree overwrote the file, and the copy was never committed.
   - The sealed file is f4cb6a98…, recomputed by main from `git show 4aa66ca45:…`.
   - Its four E2 values equal `look.py`'s constants to ≤ 2.9 × 10⁻¹² relative (3.8 × 10⁻¹³, 5.3 × 10⁻¹³, 1.9 × 10⁻¹²,
     2.9 × 10⁻¹²), and its τ are identical. C0's tolerance is 10⁻⁶, so no cell is affected.
2. **The measured inputs, now pinned before the run.** `look.py` reads B1741 `compare.py`'s two data files and never calls
   `_load()`, where compare.py asserts their hashes.
   - Their sha256 today: `frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json` is 63450365…,
     and `frontier/B1612_the_mixing_patterns_the_weave_fixes/verification/data.json` is 61ea1565….
   - Both equal compare.py's own constants. The landing re-checks them.
3. **Output names.** The sealed text names `accessory.json` and `norms.jsonl.gz`. The code writes `accessory.jsonl`,
   `norms.npz`, `norms_index.json` and `census_controls.json`. The content is as described.
4. **A wording slip in the model.** "The sector charges sum to −Y_H" holds for up, (1, −4). Down (1, 2) and the leptons
   (−3, 6) sum to +Y_H. The law is stated in ±3w, so nothing that uses it changes.

## One voidness rule (stricter than the sealed text)

If any of the 1 364 302 rows' features, or the data's minimum in any mode, is not finite, the look is **void**, a control
failure, whatever the cells print.

**Why:** a non-finite minimum makes P1 print FAILS and can make D print HOLDS, because the screen's radius becomes
undefined and no target becomes a candidate.

**How it is checked:** from `look_run.txt`'s "all finite" line and the printed minima, before any cell is read.

## The frozen row, if D holds (settled before the run)

- **The mode is c continuous,** the decisive one. The row is frozen with the bounded-optimal c printed for the best row.
- **The best row is frozen wherever it lies,** on THE SIX ON THE STRIP's lines or off them. The record says which, and the
  family's name follows the row, not the reverse.
- **If δ* = ∞ (the cusp limit),** the end carries no continuous number. A07 is then re-typed CHOSEN (a discrete principled
  end), not FITTED.
- **If δ* is finite,** A07 is FITTED (one number). B1840's card then asks whether δ* coincides with one of E1–E4.

## Notes (none changes a result)

- **C0** runs through the split quadrature with the down sector's twists, the class cache's route. It does not use the
  cache itself or the `Measure` class; C1 and C3 cover those.
- **No control tests a reduced apex against its unreduced original.** That rests on B1836's T-law (8 × 10⁻¹³).
- **Not priced, as in B1798:** the apex band Im τ ∈ [2.0, 3.6] of B1753's rule.
- **Missed in the seen-first:** LAW_MAP's B1744 row (the Higgs's own twist is even, T0(3w) = T0(−3w)) is the nearest
  earlier record of the Higgs-twist law.
- **B1838 § 2b's "the norm of no geometric cut" overstates what was shown.** Single horoball levels were tested at two
  rows, so "no single horoball level reproduces the weights" is the result. B1838's dated note corrects it, and this card's
  "Why" inherits that wording.

## Addendum (S305d, still before `look.py` runs): what a pass would let the confirmation claim, fixed now

Credit: the SM seat's §349 (65bdcb637, on the SM seat's own branch), read by main and adopted,
because the math settles each point. These fix the scope of the level-2 cards before the frozen row is known; they change
nothing in B1839's cells.

- **The reading triple decides whether y_b/y_t is held out.**
  - With one Higgs doublet of definite hypercharge (I-35, UNEARNED), the pairs whose 6Y sums are −3, (Q, u^c) and (L, ν^c),
    read one section, and the pairs whose sums are +3, (Q, d^c) and (L, e^c), read the other.
  - So **(S̃, S, S)** is the one-Higgs reading: if the frozen row has it, y_b/y_t is a held-out target of the candidate.
  - **(S̃, S̃, S̃)** has up and down reading the same section, which no single doublet can do. It is a two-doublet reading
    whose free v_d/v_u absorbs y_b/y_t (B1832, S300). If the frozen row has it, y_b/y_t is **not** a held-out target, and
    declaring tan β = 1 to rescue it would choose the very parameter that absorbs the target.
  - The card would then have r alone, short of GAP1's two (v1.60), and the candidate's confirmation would stay one target
    short (P-597).
- **The y_b/y_t card's normalisation:** H = I for every field, generation by generation (B1822, CHOSEN), and no field
  carries a scalar or Kähler weight. In particular there is no modular weight (2 Im τ)^(−k_f). Such a factor multiplies
  y_b/y_t by a per-sector constant that the six cannot see, so it is fixed now, not left to the card.
- **The scale and the scheme:** μ = M_Z, full-SM MS-bar, the six's own file (HZ2021, the row "MZ, Full SM"). In it
  m_b/m_t ≡ y_b/y_t exactly, and the frozen row is the screen's fit at that scale. No running is applied.
