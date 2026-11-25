# CLAIM CARD — frame C, with its canonical end, is covariant under SL(2, Z) acting on the modulus and the point together

- seat, branch, commit: SM seat, claude/standard-model-derivation-0qt6ao, the commit that adds this card
- kind: computation
- touches: P-845, P-860 (d); B1978's dated caveat (the orbit reading needs joint covariance first)
- effect: conditions — P-845's orbit reading: B1978's change of rate class under the act is a change of cusp
- imports: none (main's frame and B1927's covariance law of the end, both on main)
- premises on main: B1945 (`parts`, `U_of`), B1927 (L(gτ) = L(τ) + log|cτ + d|), B1733 (row convention), B1978
- decisive script: relays/sm_c23/run_c23.py, SHA-256 25bab0c1eb3064cc, depends on mpmath and main's checkout (argv[1],
  for B1945's frame), run as `python3 -B run_c23.py MAIN_CHECKOUT > c23_run.txt`, output SHA-256 95c8ed77ec233c7a
- second computation: none yet
- already on main?: `grep -il "joint covarian" frontier/*/FINDINGS.md` on be8c83d4f: B1978 and B1979, both name it as
  owed; closest arc B1978
- what would make it fail: S with the point unmoved, or with the end unshifted (both fail here, by 3.3 and by 0.07)
