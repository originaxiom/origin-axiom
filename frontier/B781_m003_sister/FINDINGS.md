# B781 — THE m003 SISTER-DISTINCTION: the V4 residual, CLOSED

*2026-07-24. The B777 V4-genericity result left one named residual: m004 and m003 share
trace field Q(√−3), volume 2.029883, AND V4 — so V4 alone doesn't select the figure-eight.
This resolves it by direct computation. Phase-3; Gate 5-Q. RESOLVED-A.*

## The distinguishing mechanism (verified)
For a once-punctured torus bundle with monodromy M ∈ SL(2,ℤ),
**|H₁ torsion| = |det(M−I)| = |2 − tr(M)|.**

| | m004 (figure-eight) | m003 (sister) |
|---|---|---|
| H₁ (SnapPy) | **ℤ** (torsion-free) | **ℤ/5 + ℤ** |
| monodromy trace | **+3** (RL = [[2,1],[1,1]]) | **−3, COMPUTED** (B784 audit established m003's monodromy is −RL two ways; cc had only asserted −3 by convention, with the honest disjunction {−3,7} from \|2−tr\|=5) |
| char poly | x²−3x+1 (**golden φ²**) | x²+3x+1 |
| structure | **knot complement**, the σ-manifold | not a knot complement |

## The resolution
m004 is UNIQUELY the golden Fibonacci bundle: its monodromy has trace 3 (eigenvalue φ²)
and H₁ = ℤ. m003 fails BOTH conditions — trace ≠ 3 and H₁ = ℤ/5 + ℤ. The program's object
σ: a→ab is golden (incidence eigenvalue φ), and the figure-eight monodromy is its golden
square (φ², trace 3). **The downstream chain (Fibonacci / golden / trace-3 / H₁=ℤ) selects
m004 uniquely over its V4-sharing sister — the residual risk is CLOSED.**

## The structural beauty (recorded)
The golden **5** appears in BOTH sisters, differently: in m004 as the **field √5** (the
monodromy eigenvalue φ² ∈ ℚ(√5)); in m003 as **torsion ℤ/5** (H₁). The sister carries the
5 as torsion where the figure-eight carries it as the field — the same golden number in
two homological guises. This ties the sister-pair to the program's √5 spine.

## Consequence for the V4 chain (B777)
The V4 falsifier is now fully resolved: (1) V4 is NOT generic — amphicheirality-gated
(B777, verified); (2) among the amphicheiral V4 manifolds, the downstream chain selects
m004 UNIQUELY — m003 is excluded by the monodromy-trace/homology (B781, here). The
figure-eight's structural specificity is established; the #1 falsifier is fully defused.

Gate 5 / Gate 5-Q: structural topology. Nothing to CLAIMS.


---

## AUDIT UPGRADE (B784, 2026-07-24)
cc asserted m003's trace as −3 "by the sister convention" — only |2−tr|=5 was forced, leaving {−3, 7}. **The B784 audit COMPUTED it: m003's monodromy is −RL, trace −3, established two ways.** The conclusion (m004 uniquely trace-3, the sister excluded) was correct and survives, but it is now computed rather than assumed. The audit also confirms H₁(m004)=ℤ and H₁(m003)=ℤ/5+ℤ are genuinely computed and could have coincided.
