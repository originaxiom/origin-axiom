# Run 6 implementation record

- Source reading: the supplied Run 5 report and original PDF, with B1634 consulted read-only for the convention relating pullbacks to the target representation. Primary sources checked for current-current deformation and ordinary affine fusion.
- Exploratory exact cohomology calculations preceded PLAN.md. They found the diagonal untwisted cohomology characters and the line-times-rotation factorization. The plan therefore does not record blind predictions.
- Two exploratory SymPy convenience calls were unsuccessful: `charpoly` attempted to order non-real algebraic factors; `linsolve` encountered a number-field zero-divisor diagnostic while trying to find a 3-by-3 intertwiner. Neither call established a research claim. The formal calculation prints and directly checks a simple diagonal intertwiner, and finite representation multiplicities are computed by exact character sums rather than these solvers.
- After the first successful formal exact run, two alternate-gauge robustness checks were added (kill the b cocycle component instead of the a component). The exact script was rerun from the beginning; its final count is 140.
- Numerical scripts were run at 60 and 90 digits and passed all 80 checks at each precision. They use direct tau series, not fractional-nome roots.
- No failing formal research assertion was suppressed. The exploratory `explore_cohomology.py` is retained as an exploratory file, not needed for reproduction or counted among the verification evidence.
- Final claims distinguish internal local-operator symmetry, geometric local-system transport, and physical conformal-block transport. The first two are calculated; the third is not identified with them by assumption.
