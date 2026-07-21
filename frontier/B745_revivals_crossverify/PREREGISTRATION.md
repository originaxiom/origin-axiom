# PREREG — B745: cross-verify of B742's two revivals (B58, B225) (SEALED)

cc banking seat, 2026-07-21. Number reserved pre-use. Reassigned from cc2 on seat closure (R27-4).
cc3's design: correction headers on the original arcs WAIT on this independent cross-verify. My
protocol per revival: (1) re-execute cc3's recompute.py in THIS seat (different machine-context
than the audit seat); (2) at least one INDEPENDENT exact check of my own not present in cc3's
artifacts; (3) two-outcome: CONFIRMED (headers applied, B742 pending-status resolved, shortlist
re-ranked) or REFUTED (the revival dies, B742 gets an erratum). Base-rate discipline applies to
revivals exactly as to kills (E20; the pathfinder's rule).

- **B58** (claim: the kill's headline "the SL(4) tower prediction cannot be tested numerically" is
  NEGATED — the ε-pinv route computes the ambient 15×15 Jacobian, validated vs the exact SL(3)
  anchor and B65's exact J(1); the at-the-identity degeneracy survives as necessary-only). My
  independent checks: the exact SL(3) anchor charpoly via sympy from B54 conventions; the C2b′
  identity charpoly(B65 J(1)) == char(M⁻¹)char(M)char(M²)char(M³)char(M⁴)char(−M²)(t−1)²(t+1) via
  sympy against the banked B65 J(m); the closure lemma (min dist of any char(M^k)/parity root to
  −φ² = 1 exactly, at −φ).
- **B225** (claim: the octahedral-parent kill rested on a disc≡a² mod 2 criterion that is a
  TAUTOLOGY — vacuous, MB12 class — so the kill reopens OPEN; the golden half stands). My
  independent check: prove/refute the vacuity of the criterion itself in sympy (can it ever fail?).
