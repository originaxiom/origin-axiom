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
