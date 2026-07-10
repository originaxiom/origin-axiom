# B509 — THE SQUARE-TIME CURVE: rank 0 PROVED; the curve is 40a3, ISOGENOUS to the program's 40a1
**Eleventh handoff verified by this seat (2026-07-11). Firewalled; the isogeny fact is FLAGGED, not
interpreted (handled per the 283-protocol: verify → convene → no interpretation first).**
- **Elimination exact (sympy):** δ(s)=c² ⟺ disc_s = (c²−1)(c²−5) ✓ (the handoff's chain).
- **E: Y² = X³−2X+1 = (X−1)(X²+X−1)** — disc 80 ✓, conductor 40, **j = +55296/5** (handoff's −55296/5
  sign-corrected — the session's fourth sign slip, caught by verification), torsion **ℤ/4** ✓.
- **RANK 0 OVER ℚ: PROVED (Sage descent).** THE RATIONALITY THEOREM IS NOW UNCONDITIONAL: the only
  rational points are the four torsion points ⇒ over ℚ, square (geometry-type) time on the evolution
  family exists ONLY at the Markov origin (s=0, δ=1). The bridge is closed over ℚ except at the seed;
  it opens over ℚ(√5) exactly at the entropy point (c²=5, d=0) and over ℚ(√−3) at the geometric point
  (c=2, d²=−3) — the three ends as fields of definition of one curve's special points.
- **THE FLAG (verified, unInterpreted):** E's Cremona label is **40a3**; it is **NOT isomorphic but
  ISOGENOUS to 40a1** — the program's banked character-variety curve. Same conductor (40), same
  isogeny class, same L-function. Banked as fact; interpretation awaits the convened seats + the
  number-field torsion/rank completion (Simon-descent crashed over ℚ(√5)/ℚ(√−3) — named tool gap,
  PARI ellrank or mwrank route priced). Lock: tests/test_b509.py.
