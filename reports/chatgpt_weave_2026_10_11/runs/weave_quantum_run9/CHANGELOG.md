# Integrity notes

- Source materials were read before this run. No prior executable verification code was imported.
- The plan was written after source reading and exploratory reasoning, then locally hashed. No blind or externally timestamped preregistration is claimed.
- `verify_exact.py` initially had 37 checks. Three additional diagnostics of a hypothetical parallel colour-to-flavour reference field were added after the first successful run; the final 40-check script was rerun.
- The first Clifford script contained an incorrect test of separated-point antisymmetry at a finite Fourier cutoff. All 25 paired Clifford traces matched the finite mode formula; the separate antisymmetry assertion failed because a finite cutoff retains the truncated contact anticommutator. The check now tests that contact term exactly. The original source and failure log remain in `history/`.
- Meromorphic antisymmetry is separately verified for the analytically continued complete theta kernel, not inferred by discarding a cutoff contact term.
- Both 55-digit and 85-digit numerical runs completed with all 116 comparisons passing. Strict identities and finite-distance limits are reported separately.
- No input PDF, previous report or repository was modified. New files are confined to this run's output directory and archive.
