# R2: MIXING NUMBER CROSS-CHECK — FINDINGS

cc3 audit seat, 2026-07-24. Gate 5-Q.

---

## Result

The mixing number p = 1/(φ·√5) from B753 (quantum topology, SU(3) level-2
Weil representation) and the torsion data (τ_geo = -3, τ_dyn = -5) from
B425 (classical topology, Fox calculus) are connected by six golden
identities. All six verified symbolically.

## The six identities

| # | Identity | Content |
|---|---|---|
| 1 | σ(p) = 1 − p | doubly stochastic = Galois symmetry |
| 2 | p · σ(p) = 1/5 = 1/\|τ_dyn\| | Galois norm = reciprocal dynamical torsion |
| 3 | \|τ_geo\| = φ² + φ⁻² = 3 | geometric torsion = monodromy trace |
| 4 | \|τ_geo\| · \|τ_dyn\| = 15 = \|disc Q(√-15)\| | torsion product = meeting discriminant |
| 5 | p = 1/(φ² + 1) | mixing = reciprocal of shifted trace |
| 6 | **p² + (1−p)² = 3/5 = \|τ_geo\|/\|τ_dyn\|** | squared sum = torsion ratio |

## Significance of Identity 6

The sum of squared Born weights in the mixing matrix equals the ratio of
geometric to dynamical torsion:

    p² + (1−p)² = |τ_geo| / |τ_dyn| = 3/5

This is the two-column law (Eisenstein/golden = being/hearing) appearing
*inside* the mixing matrix itself. The quantum-topological mixing (B753)
and the classical-topological torsion (B425) are not independent — they
share the same golden arithmetic, and the ratio that organizes the
character variety's two columns is the same ratio that organizes the
Born weights.

## The V4 discriminant chain

The three torsion values form a V4-consistent chain:

    Q(√-3):  disc = −3  = τ_geo    (Eisenstein column)
    Q(√5):   disc =  5  = |τ_dyn|  (golden column)
    Q(√-15): disc = −15 = τ_geo · τ_dyn  (meeting face)

The product relation disc(meeting) = disc(being) · disc(hearing) is the
field-theoretic content of the V4 group law: being · hearing = meeting.
The two torsions are not independent invariants — they are the two
generators of V4's discriminant lattice.

## Verdict

**CROSS-CHECK PASSED.** The mixing number is structurally consistent
with the torsion data. The consistency is not coincidental — it follows
from the V4 discriminant chain and the golden arithmetic that both
computations share. Identity 6 is the strongest confirmation: the
two-column law that organizes the character variety also organizes
the Born-weight mixing.
