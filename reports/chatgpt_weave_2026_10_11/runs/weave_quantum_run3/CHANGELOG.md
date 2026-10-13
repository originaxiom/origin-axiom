# Integrity and corrections

## 2026-10-10 — Run 3

The analytic hypotheses were explored before the plan was written. PLAN.md was
then locally hashed before executing the formal scripts. This was not a blind,
externally timestamped or independently preregistered prediction.

1. **Exact simplification.** The initial equality check for exponential/root
   constants in the rotation-factorization test was not simplified to zero by
   SymPy. The zero predicate was changed to simplify after `expand_complex`.
   No matrix, target, representation or claimed result was changed. All exact
   checks were rerun.
2. **OPE branch approach.** The initial degeneration approached with positive
   real epsilon, putting -epsilon exactly on the principal-root branch cut.
   Tiny rounding imaginary parts selected opposite fractional roots. The
   approach was changed to epsilon=10^(-dps/2)*(1+i/5), off the cut, with the
   same OPE formula. Both complete numerical runs were repeated.
3. **Exploratory precision.** The early explore.py file uses ordinary floating
   inputs. It was moved to exploratory/ and is not evidence for 80/100-digit
   accuracy. Formal scripts use decimal-string and exact rational inputs.

Only final successful log files are retained; the earlier failing console
outputs were not saved as separate logs. The corrections are described here
rather than pretending those attempts never occurred.

The quantum-field-theory and branch prescriptions remain assumptions. The
calculation derives a holomorphic amplitude and its modular multipliers in the
specified oscillator/OPE normalization, not a full Quillen connection or a
regularization-independent global anomaly. The distinction is explicit in the
plan, code comments, report and user-facing summary.

No original PDF or external project repository files were changed.
