# B649 — TRACK S WAVE 1: the silver holonomy, stage 1 (exact SL(2) over the trace field)

**The calibration campaign's silver-control blocker (B648 §B2; sealed
under the campaign seal a463c6aa). Objective: the exact SL(2,ℂ)
holonomy of the PINNED control object — m136, the silver bundle,
monodromy word RRLL, trace 6, disc(A) = 32 — over its exactly
identified trace field. Stage 2 (the Sym-lift to 27 and the E₆
exec-prefix over the silver's field) is registered, not run.**

## Conventions block (GOVERNANCE §13)

- Triangulation: the SnapPy census m136 as shipped (no retriangulation).
- Fundamental group: SnapPy's `fundamental_group(simplify_presentation
  = True)`; generators and relators as returned, recorded verbatim in
  the output.
- Precision: 212-bit shapes minimum; residual tolerances stated per
  gate. Field identification via `trace_field_gens().find_field` with
  the bundled pari (degree scan ≤ 16, prec ≤ 10000 bits as needed).
- No Sage in this stage (pyenv-only; the canonical test environment).

## Gates (two-outcome)

- **S1-G1 (identity):** m136 matches the banked identification — the
  monodromy-word check via homology ℤ + torsion as banked and volume
  consistent with the RRLL bundle.
- **S1-G2 (field):** the trace field found exactly: minimal polynomial,
  degree, discriminant reported; the field CONTAINS the expected real
  quadratic data of trace 6 (disc 32 → √2-arithmetic) — stated as a
  check, not assumed.
- **S1-G3 (holonomy):** generator matrices to ≥ 60 digits; every
  relator residual < 1e-40; the peripheral (meridian, longitude)
  traces reported.
- **S1-G4 (exactness handoff):** matrix entries identified as elements
  of the found field by LLL/pslq at ≥ 2 precisions (agreement gate),
  OR honestly deferred to stage 2 with the obstruction named.

Outcomes: all gates pass → stage 2 opens (the 27-lift). G2/G4 fail →
bank the obstruction; the silver control's timeline re-estimates; GATE
B of the campaign WAITS (it never soft-passes with silver in flight).
