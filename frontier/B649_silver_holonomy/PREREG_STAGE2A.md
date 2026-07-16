# B649 stage 2a — TRACK S WAVE 2: exact entry identification (campaign a463c6aa)

**Objective: identify every entry of the m136 holonomy generators as an
exact element of L = ℚ(s, i), where s = 2·Re tr(a) with s⁴−8s²−16 = 0
(stage 1's anchor; [ℚ(s):ℚ] = 4, √2 = (s²−4)/4 ∈ ℚ(s), so
ζ₈ ∈ L and [L:ℚ] = 8) — closing stage 1's deferred G4.**

## Conventions block

- The stage-1 presentation exactly (SnapPy m136, simplified, generators
  a,b,c; relators aBAbcc, aaCbcB; peripheral (CCB, caCA)).
- The field basis: {s^j · i^k : j = 0..3, k = 0,1} over ℚ; an entry's
  real/imag parts identified separately in ℚ(s) via mpmath.pslq on
  [x, 1, s, s², s³] at the source's ~64-digit precision; coefficient
  bound 10^8; acceptance = reconstruction residual < 1e-50.
- If direct identification fails (entries need not lie in the trace
  field for SnapPy's arbitrary conjugation), NORMALIZE first: conjugate
  the representation so the meridian is upper-triangular parabolic
  ([[1,*],[0,1]]) with a second generator's fixed point at 0 — the
  standard trace-field position — then re-identify; the normalization
  matrix recorded.
- Symbolic verification in L via an exact quotient-ring class
  (4-vectors over ℚ(i) mod s⁴−8s²−16).

## Gates

- **S2a-G1:** all 12 entries (3 generators) identified with residual
  < 1e-50 (direct or post-normalization, stated which).
- **S2a-G2 (exact):** both relators evaluate to ±I EXACTLY in L.
- **S2a-G3 (exact):** peripheral μ trace = 2 and λ trace = −2 exactly;
  tr(ac) = −√2−√2i and tr(abc) = −2√2i reproduced EXACTLY in L
  (stage 1's relations, now symbolic).
- Failure of G1 after normalization → bank the obstruction (entries in
  a quadratic extension; name it); GATE B keeps waiting.

Outcome: G1–G3 ⇒ stage 2b opens (the Sym-lift + the E₆ prefix over L).
