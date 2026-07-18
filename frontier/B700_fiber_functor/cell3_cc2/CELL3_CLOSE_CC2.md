# B700 cell 3 — CLOSE (cc2): the CGN modular-data Galois action realizes the golden torsor

*Seat cc2, 2026-07-19. Prereg PREREG_CELL3_CC2.md sha256 f6d54fd6… (sealed
before compute). Compute agent FINDINGS_CC2.md sha256 ebb78309…. This CLOSE
records the verdict + this seat's INDEPENDENT verification + one honest
refinement for the theorem push. Advisory only; cc banks. Gate 5 throughout.*

## VERDICT: REALIZED — golden stage two-sided complete (with cell 3a).

The single nontrivial field automorphism σ ∈ Gal(ℚ(√5)/ℚ), σ: √5↦−√5 (φ↦−1/φ),
is simultaneously and exactly:
- (a) the Coste–Gannon–Ng Galois action on the golden (Fibonacci) modular data;
- (b) the swap of 2I=SL(2,5)'s two golden 2-dim irreps (cell 1, simply transitive,
  no fixed point);
- (c) the trace-tower weld map Wᵏ↦W³ᵏ (cell 3a; unit power {3,7} mod 10), NOT
  the square Wᵏ↦W²ᵏ.

So the modular-data half (this cell) and the trace-tower half (cc's cell 3a)
close the golden-stage realization on both sides.

## Independent verification (this seat, NOT trusting the agent's path)
- Field: D=2cos(π/10), D²=2+φ, minpoly(D)=x⁴−5x²+5 (deg 4, totally real
  ℚ(ζ20)⁺); ratio field ⟨1,φ,−1/φ⟩ = ℚ(√5) (deg 2, minpoly x²−x−1). CGN action
  lives on the ratio field, N=ord(T)=5. Reproduced exactly (sympy).
- Weld: trace tower (−1/φ,−φ,φ,1/φ,−2,1/φ,φ,−φ,−1/φ,2); σ(−1/φ)=φ=tr(W³)=tr(W⁷),
  tr(W²)=−φ. Unit-power correction confirmed; units mod 10 = {1,3,7,9}, gcd(2,10)=2.
- 2I via ICOSIAN QUATERNIONS (independent of the agent's GAP): BFS closure of the
  unit icosians = order 120 exactly; golden-irrep character (=2·scalar part)
  multiset sums to 120 with both −1/φ and φ present (order-10 classes, size 12
  each), Galois-swapped; character field ℚ(√5). The two golden 2-dim irreps are
  the Galois-conjugate pair. Confirms cell 1 + the swap without GAP.

## The honest nuance (agent flagged it; I confirm and sharpen it)
For rank-2 golden data the *naive* CGN "label-permutation + (±1) sign"
decomposition does NOT apply verbatim: the label permutation is forced trivial
(no room in rank 2) and σ(φ)/φ = −1/φ² ≈ −0.382 is not ±1. The ℤ/2 is carried
entirely by the value map φ↦−1/φ, i.e. σ sends the *unitary* Fibonacci datum
[[1,φ],[φ,−1]] to the *non-unitary* Galois-conjugate **Yang–Lee** datum
[[1,−1/φ],[−1/φ,−1]]. This is standard Fibonacci↔Yang-Lee Galois conjugation,
verified exactly here — a genuine fact, not a computational gap. The verdict is
unaffected: all three legs use the same σ on the ℚ(√5) ratio level.

## Refinement for the theorem push (a cell-2-flavored question, flagged to cc)
The two pictures act on DIFFERENT underlying 2-element sets:
- cell 1: {irrep A, irrep B} — two objects *within one category* Rep(2I);
- cell 3: {Fibonacci, Yang–Lee} — two *Galois forms of the golden MTC* (one
  unitary, one not).
Both are ℤ/2-torsors under the SAME Gal(ℚ(√5)/ℚ)=⟨σ⟩, and are identified via σ.
Whether this identification is CANONICAL (a distinguished torsor isomorphism) or
merely "both are ℤ/2-torsors under the same group" is exactly the cell-2 flavor
of question (canonical vs isomorphic). For the K020-in-ear PLACEMENT→THEOREM
claim, the canonical identification is what a clean theorem wants; this cell
delivers the same-σ realization, not (yet) a canonical torsor-iso. Recommend cc
weigh this when writing the theorem statement — it is the precise remaining gap,
and it is honest to state it rather than let "realized" over-read as "canonical."

## Program status (this cell's contribution)
K020-in-ear PLACEMENT: golden stage now realized both sides (3a trace-tower +
3 modular-data). Cell 4 (cc, second stage E₆ level 2 / PSL(2,7)) is the
stage-uniformity lever. Cell 3 alone does NOT claim the theorem; the theorem
needs (i) stage-uniformity (cell 4) and (ii) the canonical torsor-iso above.

## Firewall
Gate 5. Pure modular data / finite-group rep theory / Galois. "Measurement" =
fusion-category fiber functor, not physical measurement. Nothing to CLAIMS.
