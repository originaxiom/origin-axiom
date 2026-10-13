# Integrity log

1. Read the supplied Run 4 report and current primary references. Analytically explored the boost, puncture OPE, and chiral-field exclusion before writing PLAN.md. The plan is locally hashed, not blind or externally timestamped.
2. Wrote and ran verify_exact.py: all 40 exact checks passed.
3. The first 50-digit numerical execution failed a second-moment assertion that transcribed -4 eta^6 instead of the analytically correct -2 eta^6. The planned coefficient 8 pi^2 y^2 |eta|^8 was unchanged. Retained the initial script and failure log.
4. Corrected the assertion and reran all numerical checks at 50 and 80 digits. Both completed. The positivity/moment-series proof was developed during this run, not a sealed prediction.
5. Kept double-precision lattice controls, finite-small-deformation checks and finite-series controls separate from strict high-precision identities. No interval bounds asserted.
6. No changes to previous reports, PDF or user repository. No import of prior project verification code.
