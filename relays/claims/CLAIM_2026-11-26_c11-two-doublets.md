# CLAIM CARD — the two-doublet dictionary fixes neither C11's K nor B1674's k_u + k_d; I-31 stays priced, per frame

- seat, branch, commit: SM seat, this seat's branch; card and script sealed at 8a6f01fd6, the commit that adds this
  card holds the run
- kind: computation
- touches: P-290 (C11), I-31, I-37
- effect: conditions — I-31: priced per frame. F_all: the Dedekind counterterm with k_u + k_d ≡ 2 (mod 4) if the
  moves are exact. F_c: the same; the gauged centre μ₄ is anomaly-free for I-31. F_S: excluded by SU(3)_F³ (A = 16)
- imports: E6's U(1)_ψ charges 27 → 16₁ + 10₋₂ + 1₄ (a read-out and positive control only); the standard discrete
  anomaly criterion (the phase ζ^{Σ 2T·dim·q})
- premises on main: B1674, B1689 (W44's frames), B1970, B1974, B1253, B1945/B1940 (frame C's Higgs); the seat's
  SM-C23 (read only)
- decisive script: relays/sm_r290/run.py, SHA-256 bb20054ac871ecf6, depends on the standard library, numpy, mpmath
  (through main's modules) and main's checkout (argv[1]), run as `python3 -B run.py MAIN_CHECKOUT run`, output
  SHA-256 406b8fb20794f251 (r290_run.txt); post hoc relays/sm_r290/posthoc_e.py (0e182190b727d4de), disclosed
- second computation: none yet
- already on main?: `grep -il "SU(3)_F\|horizontal SU(3)\|U(1)_ψ" frontier/*/FINDINGS.md` on be8c83d4f: 10 arcs
  (B298, B487, B1340 among them), none restricting B1674's characters to a frame's K; closest B1674, B1689
- what would make it fail: a gauge realisation of a non-trivial uniform scalar by the Standard Model group with ν^c
  present (B2 finds none; P5's U(1)_ψ shows the test can find one), or a scalar of ρ_T's image outside μ₄
