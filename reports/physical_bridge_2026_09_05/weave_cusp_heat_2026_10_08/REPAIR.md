# Special function checker correction

The first native execution under pushed seal1a9c71b1d exited1:
28 of29 predicates passed. The sole false predicate was
continuum_plus_index_is_erf. Reference execution and focused collection
had not begun because custody stops at the first failed job.

The residual was (1-erfc(x)-erf(x))/2. By the defining identity
erfc(x)=1-erf(x), it is zero. The instrument used simplify without
asking for a common special-function basis. The revised checker first
rewrites erfc in terms of erf, then simplifies the SAME residual to
zero. No target, sign, tolerance, physical claim or acceptance criterion
changes. This is a post-execution instrument repair, not a first-pass
success. The full failed output, exit receipt, server receipt and old
manifest are preserved byte-for-byte. The old code remains at its
immutable seal commit. The corrected code and new manifest must be
pushed and server-confirmed before the second attempt.

The other28 native predicates, including the exact color cubic moment,
actual scattering sign and IR anomalies, passed in that failed run;
this does not override the run's failed status or certify global analysis.
