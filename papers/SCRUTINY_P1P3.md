# P1–P3 adversarial scrutiny — adjudication (2026-07-08)

**Nine-agent panel (correctness/novelty/hostile × P1/P2/P3). The correctness seats found
substantial real errors; the novelty/hostile seats flagged no blocking issues. Every finding
below was re-verified by CC before acceptance. VERDICT: P1, P2, P3 as drafted are NOT sound —
each needs revision before it reaches P4's standard. The errors are in the LaTeX PDFs already
sent. This is exactly why the panel exists.**

## P2 "The Inversion Law" — TWO FATALS (both CONFIRMED)
- **F1 [FATAL]: the figure-eight's field is ℚ(√−3), not ℚ(√5).** The paper's central
  "laundering" object is misidentified throughout (abstract, I1, §1, §5–6). The figure-eight's
  invariant TRACE field is ℚ(√−3) (Eisenstein, Bianchi PSL₂(O₃)); ℚ(√5) is the MONODROMY
  eigenvalue field — a different object. CONFIRMED (4₁ trace field x²−x+1, disc −3). Worse: the
  child 4₁(5,1) has trace field x⁴−x−1 (S₄, NO quadratic subfield), so the absence of ℚ(√5) is
  VACUOUS. The correct, non-vacuous statement — "the figure-eight's ℚ(√−3) is absent from the
  child" — is TRUE and survives; the paper states the wrong field and a vacuous absence. FIX:
  replace ℚ(√5)→ℚ(√−3) throughout; state the child has no quadratic subfield at all.
- **F2 [FATAL]: "every collision is orientation-reversing" is refuted by the paper's own
  triple.** The triple 4₁(1,2)=5₂(−1,1)=6₁(1,1) is orientation-PRESERVING (identical vol
  1.398509, H₁=0, and equal CS). So the inversion law's uniform "mirror signature" is false —
  the (5,1) collision is orientation-reversing but the triple is orientation-preserving. FIX:
  the orientation bit is not uniformly a mirror; state the (5,1) case and the triple separately;
  the "one bit survives" thesis needs the honest split (some collisions preserve, some reverse).

## P1 "The Seam Form" — 4 MAJOR (CONFIRMED)
- **M1: "five patterns = subfield lattice" is false.** The realized set is {full, ℚ(√5),
  ℚ(√−3), ℚ, **0**} — four lattice nodes + the zero stratum; **ℚ(√−15) is NEVER realized** (it's
  the absent node, "√−15 dies first"). 0 is not a subfield-lattice node. FIX: state it as a
  chain-with-fork + zero stratum; ℚ(√−15) absent is the real phenomenon.
- **M2: "44 distinct values" is a point-count, not a value-count.** 44 = seam-bearing points
  (44 of 49); the value set has **30** distinct values. FIX: "30 distinct values on 44 of the
  49 support points."
- **M3: two-tori conflation.** The values live on the 49-support (a,b) torus (ℤ/20×ℤ/12); the
  patterns/dark-locus/240-points/70-dark live on the Fourier-DUAL (x,y) torus, never introduced.
  FIX: introduce the Fourier step explicitly; separate the two objects.
- **M4: Lemma S5 has ∎ but §8 calls it the central open problem.** FIX: demote S5 to
  Observation/Conjecture (verified on 240), drop the ∎.
- MINOR: "parabolic pair" (the matrices are hyperbolic; only their commutator is parabolic —
  clarify); S10 verified 16/36 cells (state scope).

## P3 "The Forcing Chain and the Residue" — 3 MAJOR (CONFIRMED)
- **M1: "one ℤ/2" overstated for the determinant register.** det(Par·W(w)) = −ω^{#L−#R} is a
  6th-root-of-unity (cube-root × sign), NOT a pure sign; only balanced words give −1. FIX:
  state the residue is ℤ/2 for the norm/parity registers and −ω^{#L−#R} (ℤ/6-valued) for the
  determinant, agreeing at balance.
- **M2: Theorem F7's order-5 field.** Δ_d = τ²(τ²−8) is the SINGLE-τ disc (imaginary for d=5);
  the actual field ℚ(√41) is real, arising as the NORM over the two Galois-conjugate τ's. FIX:
  the closed form is per-τ; the field is ℚ(√(Δ_d over the conjugates)); state correctly.
- **M3: the quantifier "every divisor d≥3" vs the m∈{1,2,4} exception.** FIX: "every divisor
  d≥3 whose order-d cusp point is non-degenerate" (d=2,4 degenerate) — the B479 addendum's
  precise form; import it.

## Net
The mathematics UNDER each paper is largely real (the banked B-nodes reproduce), but the DRAFTS
mis-stated it in load-bearing ways — a wrong field, a false uniform law, a mislabeled lattice, a
point-vs-value confusion, an over-strong residue. All fixable; none fatal to the underlying
result. P1–P3 go back to revision (v2) with these corrections + re-verification, then re-panel.
P4 is unaffected (it cleared this same gauntlet). The scrutiny paid for itself: it caught a
FATAL field misidentification and a FATAL false law before they reached print.
