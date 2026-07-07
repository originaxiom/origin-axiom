# B467 ADDENDUM — the 2026-07-07 registry processed: R2 verified, the collision census run, R4.2 closed

**Added on receipt of Chat-2's OA COMPUTE REGISTRY. Everything below computed/verified
in-session before writing. Firewalled.**

## Registry R2 (Chat-2's residue computation): VERIFIED EXACTLY

det(W₁) = 1, det(W₂) = 1, det(Par) = −1, det(Par·W₁·W₂) = −1 — exact (F_p at p = 61, 421,
the B465 engine). Chat-2's identification confirmed: sign(negation on ℤ/N) = (−1)^((N−1)/2)
= −1 for N = 15 ≡ 3 mod 4; the Weil operators are even; the uniform −1 is the level's class
mod 4. **Two-register convergence banked**: Chat-2's operator-determinant bit and B467-F2's
permutation-sign bit are the SAME residue seen quantum-side and classical-side — in both
registers everything orientation-preserving is even and the single odd object is the
negation/orientation character (classically carried by the det = −1 half-monodromy σ, the
B466 Gieseking bit). Uniform ⇒ not a chirality FIELD (Chat-2's caveat, endorsed): it
distinguishes nothing; it is a global signature. Their branch-permutation version stays
blocked on Chat-1's loop definitions (recorded).

## Registry R3 (the sharp question): the p = 5 collision is NOT isolated

`census.py` (parents 4₁, 5₂, 6₁ — the third TWIST-KNOT parent; the registry's "extend to
m=3" corrected again: metallic m=3 is a bundle, not a knot): slopes |p| ≤ 15, q ∈ {1,2},
buckets by (vol, H₁), isometry-certified (hyperbolic fillings only; the first census run
missed p=5 through an over-strict solution-type filter — corrected, documented):

| child | H₁ | parents (oriented statements from CS) |
|---|---|---|
| vol 0.9813689 | ℤ/5 | **5₂(5,1) = 4₁(−5,1)** (mirror of 4₁(5,1)) — the banked collision |
| vol 1.3985089 | **0** | **TRIPLE: 4₁(1,2) = 5₂(−1,1) = 6₁(1,1)** (CS −0.246607 all three; 4₁(−1,2) = its mirror) — an integral homology sphere with THREE distinct parents |
| vol 2.4075735 | 0 | 5₂(−1,2) = mirror of 6₁(−1,2) (CS ±0.075207) |

**Eight certified pairwise collisions in-window; three collision children; one triple.**
Mechanism candidate (named, lit-gated): all three parents are twist knots = fillings of one
component of the Whitehead link; the Whitehead link's component-exchange symmetry
systematically manufactures different-parents-same-child coincidences — the (±1,2)/(∓1,1)
slope pattern is exactly that shape. Literature class: Brakes/Livingston-type "manifolds
with multiple knot-surgery descriptions" — **NEEDS-LIT before any novelty word**; the
census stands as exact data regardless. Registry kill-condition NOT triggered (the wall's
merging is not "one banked coincidence" — it is a small family in-window), but the
mechanism candidate is a launder-shape: the collisions may all be Whitehead-symmetry
bookkeeping, which the lit-gate will decide.

## Registry R4.2 (V₁ ↔ V₂ under the outer symmetry): CLOSED by composition of banked facts

B444 banked the identification "V₀ geometric over ℚ(√−3); **W₁/W₂ over ℚ(√−7)**" — so the
D(3,3,4)/ℚ(√−7) pair IS the B71 Dehn-filling pair — and B466 computed **σ(W₁) = W₂
exactly** (the Gieseking half-monodromy exchanges them; the σ-fixed locus is the p=q line
in V₀ through the all-ones triple point). Answer: **YES, the outer symmetry exchanges the
pair.** The chirality-ledger payoff: exchanged-by-σ is the same ℤ/2 as everything else
tonight — the orientation bit.

## Registry bookkeeping corrections

- "torsion 121 = 11²" (registry R3 header): 121 is B437's ABELIAN-BOOK resultant
  |Res(Φ₅, Δ_{4₁})| = L₅² — a PARENT-side invariant. H₁(child) = ℤ/5 (parent-blind). Since
  the collision children are literally isometric, every intrinsic child invariant matches;
  121 lives upstream of the wall and would differ for 5₂'s book — worth noting as exactly
  the kind of data the wall forgets.
- Registry R1 is already run (B467-F1): earned negative, 886 expressions ⊇ the registry's
  class (arcsin/arccos of all three ratios also checked: nothing within 5% of any target,
  let alone 1e-3). The May lesson's null battery was attached; nothing to run again unless
  the class is widened by prereg.

## Reproduce
```
python3 census.py       # the collision census (isometry-certified)
python3 det_check.py    # registry-R2 determinants, exact at two primes
```
