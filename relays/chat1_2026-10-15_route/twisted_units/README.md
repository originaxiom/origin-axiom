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

**Waiting on the SM seat:** the twisted units, in the format the 15:29 addendum to THE ROOT'S LINE asks for, or its
answer that ρ_R does not admit them.
