# The twisted-units comparison: chat1's side, prepared before any twisted unit exists

Nothing here is a result. No N = 9, 11 or 12 mass has been computed.

- **`DESIGN_DRAFT.md`: the comparison's design**, fixed before the SM seat's units exist and refereed twice. It is not a
  seal.
- **`units_cells.py`: the instrument** for delivered units.
  - Its input is one set of units per field, with any rational q-exponents, plus the Higgs modes and the coupling
    vector, through a `UnitSource`.
  - It covers the L·Rⁿ towers, evaluated at the unreduced point, in ball arithmetic.
  - It returns the seven cells per sector, the closure of every Y integrand over one period, and r_calc: the change
    from Npts to 1.25·Npts, and from full coefficients to coefficients rounded to 53 bits.
  - It generalises `../m003_exploration/deep_cusp/deep_cusp.py`. Left and right units come from different fields, and
    the sectors come from a charge assignment, so the null's assignments run the same way.
- **`units_cells_selftest.txt`: the self-test,** at excluded orders only.
  - It runs untwisted units for every field (the minimal reading) on L·R⁹ at N = 3 and L·R²⁵ at N = 5.
  - It reproduces `deep_cusp_deep.json` (`818db8b8d`) exactly, in double precision, in every rank-three cell.
  - Closure is 10⁻³⁶ over all three Y integrands. r_calc is 10⁻⁴³ or below.
- **`null_draws.py`, `null_draws_run.txt`, `null_draws.json`: the null's charge assignments,** by pure algebra with no
  mass.
  - They are the gauge-invariant integer 6Y assignments with every |q| ≤ 12.
  - Kept: eligible at N = 9, 11 and 12 on the SM's terms there.
  - Excluded: the SM, its negative, and every draw equal to k·SM mod N.
  - Shuffled with seed 20261015. 668 are eligible.
  - The SM's own status by order reproduces relay §126's table exactly:
    - N = 5: d = e, with the up quarks null;
    - N = 7: up = leptons;
    - N = 8 and 10: d = e;
    - N = 9: split, with the leptons null;
    - N = 11, 12 and 13: split, none null.

- **`units_cells.py`'s `PerFieldFactoredSource`: the per-field reading** (W92's z-form dressing, applied at each point;
  R neutral). It matches W92's dressed series to 2.5·10⁻⁴⁷. The towers exploration is in `exploration_per_field/`.
- **`tlow.py`: the low-thread instrument, stage 1, in double precision.**
  - It evaluates every form at the unreduced point of any thread's period. The untwisted forms are carried from the
    reduced point as integer-weight ratios X_c/R_c by R's monomial map, so no branch arises. The Higgs modes also carry
    χ_i(S) = χ_i(T) = i.
  - R, the dressing and the twisted coupling vector are evaluated directly, by explicit theta sums.
  - **Self-test (`tlow_selftest_run.txt`):**
    - pointwise invariance of K and Y at zero twist to 10⁻¹⁴;
    - THETA2's admitted threads to 10⁻¹²;
    - agreement with the ball-arithmetic instrument on L·Rⁿ towers to 10⁻¹¹ at y = 1.7.
  - **Its limit:** at y = 2.8–3.4 double precision loses the Y integrals, worst in the per-field reading (10⁻³ to order
    one). Stage 2 will be ball arithmetic.
- **`tlow_enum.py`, `tlow_configurations.json`: T-low's configurations,** by pure algebra with no mass.
  - They are the words up to length 12 at height ≤ 3, with lines of exact order N fixed up to sign and N² | Q_γ(w).
  - N = 9: 18 configurations on 3 words. N = 11: 40 on 8 words. N = 12: 32 on 10 words. Heights run 1.54–2.77.
  - LLRLLRRLRR has 6 lines up to sign and LLLLRLRRRLRR 5, as relay §127 counted.

**Delivered since:** W91, the twisted coupling vector (§131), and W92, the per-field units (§134). Both readings'
pieces now exist.
