# The minimal reading on deep threads, in ball arithmetic (exploration, unsealed; excluded orders only)

Files and what they show:
- **`saddle_check.py`, `saddle_check_run.txt`: the cusp criterion on single terms.** A term q^p q̄^p′ y^k grows on a
  deep thread like e^(4πR√(pp′)) only when p < 0 and p′ < 0; otherwise it grows at most polynomially. Five terms are
  checked at R = 4, 8 and 12, in mpmath at a precision set by the term.
- **`deep_cusp.py`: the instrument.** It computes the cells of W72 and THETA2 with B1656's twisted coupling vector in the
  minimal reading, with matter and Higgs modes untwisted.
  - It works in arb/acb ball arithmetic (python-flint) at 358–731 bits.
  - Every form is evaluated at the unreduced point of the thread's period, so no transport is needed.
  - That is sound where the period stays at y ≳ 1: the L·Rⁿ towers, where min |C| = 1. On other threads the period dips
    to y ≈ 1/|C|, which needs reduction or more terms.
  - It needs `forms.pkl`, which `../instrument/build_forms.py` writes. Run it as
    `python3 deep_cusp.py <forms.pkl> <theta2_completion.json> validate|deep`.
- **`validate_run.txt`, `deep_cusp_validate.json`: zero twist against THETA2 on L·Rⁿ, n = 1–7.** THETA2's stored values
  are double precision and admitted only for y ≤ 3.
- **`deep_run.txt`, `deep_cusp_deep.json`, `deep_summary.txt`, `summarize.py`: the towers.**
  - L·R^(9, 18, 27) at N = 3, L·R^(25, 50) at N = 5 and L·R⁴⁹ at N = 7.
  - The sectors are zero twist, up, down and leptons, on the line (0, 1)/N, all seven cells.
  - Each run is repeated at 1.25 times the points.
- **`deep_run_53bitparse.txt`, `deep_cusp_deep_53bitparse.json`: the first deep run, disclosed.**
  - It parsed the forms' coefficients at python-flint's default 53 bits.
  - Its singular values agree with the final run's to double precision, but its ball radii were meaningless. They were
    pessimistic bounds over 10⁻¹⁶ coefficient balls.
  - It was rerun with the coefficients parsed at 800 bits.

Every order here is excluded:
- at 3, up = down and the leptons are untwisted;
- at 5, down = leptons;
- at 7, up = leptons.
No N = 9, 11 or 12 quantity was computed.
