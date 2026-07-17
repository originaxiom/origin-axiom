# B590 — the revival remainders (Review-17 queue item 7) — prereg

**Date: 2026-07-14. Preregistered BEFORE the computations. Firewall: nothing to
CLAIMS.md; no SM quantities.**

## The four remainders, triaged

- **R1 — S031 sealing at bronze m=3 (B571-B2, under the CORRECTED framing).**
  B571's revival note claimed K₃ = ℚ(√13) (quadratic); B578-D6 retracted that
  same-day: K₃ is DEGREE 6 (ℚ(√13) is the scale field m²+4). The honest m=3
  question: do all irreducible off-sublocus SL(3) fixed points of the bronze
  trace map φ₃(A,B) = (A³B, A) have Lawton traces in the SL(2) trace field of
  the bronze bundle (b++R³L³), computed in-sandbox at high precision?
  Method: the B137 search (MB7 irreducibility filter) + mpmath polish of each
  converged point + pari `lindep` membership against the power basis of the
  trace field's primitive element, with BOTH controls: (i) known field
  elements must pass, random numbers must fail (height/residual gates);
  (ii) the m=1 pipeline-validation run must reproduce B129/B137 sealing in
  ℚ(√−3). Verdicts (registered): SEALED (0 irreducible escapes) /
  NOT-SEALED (≥1 verified escape — polish-stable, irreducible, lindep-fails)
  / UNSTABLE (report honestly).
- **R2 — B572-V3 (B299 orbits ↔ the three 16s).** Compute, at the weight
  level of the exact 27: (i) the trinification 9+9+9 blocks (B299's φ, the
  {1,ω,ω²} split — banked, test_b578_v3_reframe); (ii) the three
  D₅-decompositions 27 = 16 ⊕ 10 ⊕ 1 in the three triality frames (charge =
  the coweight of the deleted node, frames related by φ); (iii) the full
  intersection pattern |9_i ∩ 16_j| (and with the 10s and 1s). BLIND — no
  registered expectation; any exact pattern banks, including "no clean
  correspondence" (the honest negative). Note V3 lives on the Spin(10) side
  of the unpaid weld (B572) and B573 refuted principal-stability of the 16;
  nothing here claims the weld.
- **R3 — B572-V2 (H¹ = 6 by Fox calculus): DISCHARGED-BY-B575.** B575's exact
  pipeline computed per-block Fox-calculus cohomology dim H¹ = dim H² = 1 for
  each of the six blocks (gate G4), i.e. H¹ = 6 total by Fox calculus in
  exact ℚ(√−3) arithmetic — precisely the independent route V2 asked for.
  Deliverable: the reconciliation note in B572's FINDINGS + this file; no new
  computation (MB13: do not re-derive).
- **R4 — B572-V5 (global gap⟺chirality with Galois descent): DISCHARGED-BY-
  B578.** The banked duality item (descent obstruction Ĥ⁰(Gal, Z(G)) trivial
  for E₆; the biconditional unconditional; locks test_b578_duality).
  Deliverable: the reconciliation note; no new computation.

## Falsifiers / discipline

- R1: if the membership controls fail, the classifier is unusable — stop and
  report UNSTABLE rather than forcing a verdict (exploratory-numerics memory).
- R2: exactness gate — the three charges must give |16/10/1| = 16/10/1 in
  every frame, and φ must permute the frames; otherwise the frame setup is
  wrong — stop.
- MB13 sweep: B129/B137/B141 (the sealing program + MB7), B160 (the bronze
  map), B578-D6 (K₃ degree 6 — the corrected framing), B125 (the arithmetic
  table), B299 + test_b578_v3_reframe (the triality split), B573 (step-8
  refutation — scope guard), B575-G4 (V2's discharge), B578-duality (V5's
  discharge). Nothing rediscovered.
