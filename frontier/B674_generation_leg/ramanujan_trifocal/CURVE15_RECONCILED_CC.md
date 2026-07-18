# THE CONDUCTOR-15 CURVE — TWO SEATS, TWO MODELS, ONE ISOGENY CLASS
# (main seat, 2026-07-18; cc2's note as-received 8e86e428, verified +
# reconciled with my trifocal bank b9dccb0)

## The reconciliation (a subtlety worth stating exactly)

cc2 derived the elliptic curve from the banked Cooper–Long A-polynomial
by the m → 1/m palindromic quotient: Y² = (t+1)(t−2)(t+2)(t−3),
t = m+1/m. My trifocal bank used the direct discriminant curve (square
factors removed): Y² = (m²−3m+1)(m²+m+1). THESE ARE DIFFERENT CURVES —
j(cc2) = 13997521/225, j(mine) = −1/15 — but that is exactly the
signature of an ISOGENY, not a discrepancy: isogenous elliptic curves
share a_p (the L-function) and differ in j. The class 15a has EIGHT
curves with eight j-invariants; mine (j = −1/15) IS Cremona 15a8, cc2's
is another curve in the same class.

## THE DECISIVE CHECK (recomputed on THIS seat, three curves)

a_p = p+1−#E(F_p) at all twelve good primes p = 7..47, by direct
point-counting of (1) 15a8 in Weierstrass form y²+xy+y = x³+x², (2)
cc2's quartic, (3) my quartic:

  ALL THREE = [0,−4,−2,2,4,0,−2,0,−10,10,4,8]

— identical, and identical to cc2's stated sequence. So both elliptic
models are isogenous to the class 15a (Faltings-grade evidence at 12
primes, two independent models, two seats). The program claim rests on
the CLASS, which is now doubly established.

## The invariants + the bifocal branch locus (both confirmed)

15a8: c₄ = 1, c₆ = −161, Δ = −15 EXACTLY, j = −1/15, conductor 15 =
3·5 = the banked congruence level; modular avatar = the unique weight-2
level-15 newform. My trifocal bifocal-branch-locus claim SURVIVES cc2's
correct factorization: the full discriminant is (m−1)²(m+1)²(m²−3m+1)
(m²+m+1), and cc2's quartic factor (m⁴−m³−4m²−m+1) = (m+1)²(m²−3m+1)
EXACTLY (verified) — so the golden pair φ², φ⁻² (roots of m²−3m+1) and
the Eisenstein pair ω, ω̄ (roots of m²+m+1) are both genuinely in the
branch locus. Being and hearing are the branch points of the object's
own elliptic fibration, at the conductor that is the congruence level.

## Corrections adopted (from cc2)

- chat1's g₂ = −1/12, g₃ = 161/216 were garbled; correct scale
  c₄ = 1, c₆ = −161 (Δ = −15 was right). Adopted.
- PRIOR ART EXISTS for the elliptic identification (Borot–Eynard; the
  Kyoto paper) — NEEDS-SPECIALIST, NO novelty claimed for the curve.
  The program-level novelty is CONDUCTOR 15 = THE CONGRUENCE LEVEL,
  which is ours to state.

## Follow-ons (my lane)

Exact isogeny certification in pari/sage (12-prime evidence →
certificate); the Boyd/Mahler-measure bridge m(A_{4_1}) ↔ L′(E₁₅) —
the classical route connecting the banked hyperbolic volume 2.0299 to
the L-function ledger (queued in OPEN_LEADS as the L(E₁₅,s) lead).
