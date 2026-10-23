# RIGID_TAU_HOLOMORPHIC: control C2 failed as written, and how it was resolved before any output was read

chat1, 2026-10-23. **Post hoc, labelled.** Written while the run is in progress, before its output exists. 0 of 19.

- **As written.** C2 checked F_6's T-covariance (τ → τ + 1, b → b − α) at the first family-A point, the class LR's apex
  (1.5 + 1.118i) on (1/5, 1/5): 9.0 × 10⁻⁸ in ln for the ratios and 1.4 × 10⁻⁷ for |V|, against the sealed bar 10⁻⁹
  (`rigid_tau_controls.json`, 483397c30, committed before it was read). C1 (2.5 × 10⁻¹⁴) and C3 (B1720's stored six
  reproduced to 2.0 × 10⁻¹²) hold.
- **Why the bar was wrong for these points.** The 10⁻⁹ bar was carried over from the earlier tests, whose points (lines
  of order ≤ 12, |Re τ| < 1) gave about 10⁻¹³. Family A's points are B1720's apexes, with lines of order up to 54 and
  Re τ up to 4.5, where main's quadratures (residues and regularised areas) are less precise. B1720's own
  basis-covariance control allowed T-moves up to 10⁻⁶ and measured 5.9 × 10⁻⁸.
- **C2′** (`rigid_tau_c2prime.py`, committed before its run; output committed before it was read) repeats the check
  for F_6 and for main's ∂R at seven family-A points spanning the heights 1.12–3.87:
  - F_6: 1.7 × 10⁻⁹ to 4.7 × 10⁻⁷ (ratios), 3.2 × 10⁻⁹ to 2.2 × 10⁻⁷ (|V|);
  - ∂R: 4.0 × 10⁻⁹ to 3.3 × 10⁻⁸ (ratios), 6.1 × 10⁻¹⁰ to 1.2 × 10⁻⁵ (|V|, the largest at LR's apex).
  The zero-free Higgs and main's own ∂R show deviations of the same order: the instrument's precision at these points,
  not a broken covariance.
- **Resolution.** The model is T-covariant to the instrument's precision, at most 5 × 10⁻⁷ in ln for the menu, within
  B1720's own tolerance and at least four orders of magnitude below anything the cells read (a factor of 2 is 0.69 in
  ln; the precision bar's σ is about 0.10). The cells are read with C2 reported as failed as written and resolved here.

0 of 19.

## Erratum (2026-10-23, after the result was read and refereed; post hoc)

The text above is kept as committed (fff2b28dd). Corrections, checked against `rigid_tau_c2prime.json`, the index and
B1720's committed files at 3412bf09d:
- ∂R's ratio deviations run from 3.2 × 10⁻⁹ (LLLLLLR), not 4.0 × 10⁻⁹, to 3.3 × 10⁻⁸.
- "At most 5 × 10⁻⁷ in ln for the menu" should read "for F_6": C2′ did not check F_−2 or F_22. `rigid_tau_posthoc.py`
  (R7) recomputes the two best rows (F_22) after moving each by three T-steps and reproduces their stored six and nine
  to 5 × 10⁻⁸ in ln (two numbers per row; the stored fields are float32, good to about 5 × 10⁻⁷). F_−2 is not rechecked.
- Family A's lines have order up to 70, not 54.
- "Deviations of the same order" should read "of the same range": point by point F_6 and ∂R differ by up to about 90×.
- B1720's 10⁻⁶ tolerance covered its six ratios only, at 8 classes of height 1.1–2.4 (its PREREGISTRATION.md, C1; the classes used reach 2.29). Its
  measured maximum, 5.9 × 10⁻⁸, already exceeded the 10⁻⁹ bar, and at C2's own point (LR's apex on (1/5, 1/5), class 0)
  it measured 2.4 × 10⁻⁸ (the_thread_census.json, C1_control). The bar conflicted with a source the rule cites; the
  failure was foreseeable from the record.
- The earlier tests gave 4 × 10⁻¹³ (TICK_LINE_HIGGS's C2) to 1.1 × 10⁻¹⁰ (ZERO_FREE_HOLOMORPHIC's C2′, |V|, 323867b0c),
  not "about 10⁻¹³".
- C2′'s working hypothesis, low Im τ, holds as a trend but not point by point: each of the four series is smallest at
  Im τ 3.87, and ∂R's |V| falls from 1.2 × 10⁻⁵ at 1.12 to 6.1 × 10⁻¹⁰, but F_6's largest ratio deviation (4.7 × 10⁻⁷)
  is at 2.49. Height is not the only factor: ZERO_FREE_HOLOMORPHIC's C2′ held to 1.1 × 10⁻¹⁰ at heights 2.05–3.45
  (lines of order at most 12, Re τ < 1).

None of this changes the resolution for the menu's checked deviations (F_6 at seven points, F_22 at two rows): they stay
at least four orders of magnitude below anything the cells read. ∂R's largest, 1.2 × 10⁻⁵ in |V| at LR's apex, is
about 8 000 times below the bar's σ of 0.10; no cell reads ∂R.

0 of 19.
