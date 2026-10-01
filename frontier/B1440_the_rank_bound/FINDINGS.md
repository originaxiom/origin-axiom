# B1440 — THE RANK BOUND: on a once-punctured-torus bundle no flat bundle of rank n has class index above ⌊n/2⌋, so a rank-five bundle carries at most two generations

cc, 2026-10-01. B1438 proved one count per background for the Standard-Model frame's rank-two sectors. The record
holds the larger parent that would evade it — E₈ ⊃ SU(5) × SU(5)_⊥ with a flat rank-five bundle W, tens from
H¹(W) and five-bars from H¹(Λ²W): built by the audit lane on m010 with I(W) = I(Λ²W) = +1 (its R40), carried by
the SM lane as an open lead (sL-4, "relative SL5 component search"), and searched by the web seat on M₆ in bounded
families with largest index 2 and "genuine nonsplit rank-five W of index 3: OPEN". **This arc closes that question
on every once-punctured-torus bundle, by a theorem that needs no census. Verdict: PROVED.**

## The theorem

Let M be a once-punctured-torus bundle, F its fibre group, λ the longitude (the boundary of the fibre), and V any
finite-dimensional module of π₁(M) with V^F = 0 and (V*)^F = 0. Let n = dim V and r = rank(ρ(λ) − 1). Then

    |I(V)| ≤ min(r, n − r) ≤ ⌊n/2⌋,

where I(V) = n(V) − n(V*) is main's class index (B1297) and n counts interior classes. Nothing is assumed about
the shape of V: reducible or irreducible, unipotent on the cusp or not.

*Proof.* (i) An interior class restricts on the cusp to a coboundary, hence on ∂F = ⟨λ⟩ to a coboundary, so its
restriction to the fibre lies in H¹_!(F; V) = ker(H¹(F; V) → H¹(∂F; V)). The restriction H¹(M; V) → H¹(F; V) is
injective because its kernel is H⁰(F; V) modulo the monodromy, which is zero. So n(V) ≤ dim H¹_!(F; V).
(ii) F is free of rank two and V^F = 0, so h¹(F; V) = n. H¹(∂F; V) = V/(ρ(λ) − 1)V has dimension n − r, and
H¹(F; V) → H¹(∂F; V) is onto because its cokernel lies in H²(F, ∂F; V) = V_F = 0. So dim H¹_!(F; V) = r, and the
same for V*. Hence I ≤ n(V) ≤ r and −I ≤ n(V*) ≤ r.
(iii) By B1297's identity, with no invariants, I(V) = t₀(V*) − r₁(V) ≤ t₀(V*), and t₀(V*) is the dimension of the
coinvariants of the peripheral group on V, at most n − r. Likewise −I ≤ t₀(V) ≤ n − r. ∎

## Consequences

- **Rank two: |I| ≤ 1.** B1438's Theorem B, without the slope.
- **Rank five: |I| ≤ 2.** No flat SL(5) bundle on a once-punctured-torus bundle has three net tens, whatever its
  shape — including the irreducible components the web seat's census and the SM lane's sL-4 left open. In E₈ the
  commutant of the Standard Model is SU(5)_⊥ × U(1)_Y and every sector of the ten is W twisted by a character, so
  **no E₈ vacuum on these manifolds has three net generations in this index.** Likewise SO(10) × SU(4)_⊥ gives at
  most two sixteens, E₆ × SU(3)_⊥ at most one twenty-seven.
- **Three needs rank six**, and rank six reaches it: three rank-two blocks (the M₆ triplet of sm:B1378, I = −3),
  and also genuinely triangular rank-six modules (below). The count of three on the record's one-cusped levels is
  always three rank-two sectors, that is three vacua of the rank-two frame.
- **A regular unipotent longitude gives |I| ≤ 1** (r = n − 1): uniserial modules never count more than one.
- **The bound is one cusp's.** With several cusps the right-hand side of (iii) is a sum over cusps and the fibre
  of (ii) has several punctures. The record's counts of three on two-cusped members (B1321) are not touched.

## Verified (`verification/rank_bound.py`, record `rank_bound.json`, `rank_bound_run.txt`)

Modules built over a prime field on four small levels of the architecture, index by main's B1427 code; each of the
four inequalities of the proof is checked separately on every module.

| family | ranks | modules | largest \|I\| by rank | bound attained |
|---|---|---|---|---|
| triangular, built one superdiagonal at a time (obstructed attempts discarded) | 2 – 6 | 1 182 | 1, 1, 2, 2, 3 | at every rank |
| direct sums of those | 4 – 8 | 289 | 1, 2, 1, 2, 3 | at every rank |
| exterior squares of rank-three and rank-four modules | 3, 6 | 267 | 1, 2 | yes |
| two-step modules against the formula n(W) = dim(D ∩ Im C) | 2 – 7 | 357 | 2 | — |

**No failure.** Modules with invariants fall outside the hypothesis and are counted separately, not tested.

**The two-step formula.** For W = (⊕ α_i) extended by (⊕ β_j) with classes c_ij, interior classes come only from the
socle, and n(W) = dim(D ∩ Im C) with C: k^b → (k²)^a the boundary vectors of the extension classes and
D = ⊕ k·(s(α_i), 1). So n(W) ≤ min(a, b): the web seat's two-step families could not have reached three on any
level.

## What it means, and the fence

- **The generation count per vacuum is bounded by half the rank, on these manifolds.** The frame is not what limits
  it; the fibre is. A fibre with one puncture gives each module r interior fibre classes and n − r boundary
  coinvariants, and the index is squeezed between them.
- **So the record's three is three vacua** — a deck orbit on a three-fold cover, or three blocks — and by B1438's
  Theorem E those do not mix. What would distinguish three generations is not a flat bundle of rank five or less on
  a once-punctured-torus bundle.
- **Where the bound does not reach:** manifolds with more cusps; rank six and above; a count other than main's
  class index. Each is a named place to look, not a claim.
- **The fence is unchanged:** main's class index on modules outside the reductive domain; an index is not a
  generation count; no physics reading of a non-semisimple background. 0 of 19.

## Corrections of scope this implies

- sm:sL-4 and sm:B1384 §3 ("relative SL5 static-flat chiral component — OPEN"): closed for index three on
  once-punctured-torus bundles. A relative SL(5) component may exist; it cannot count three.
- The web seat's P03/P04 status "genuine nonsplit rank-five W of index 3: OPEN": closed, on every level, not only
  on M₆.
- Main's B1427 remark that "h¹ = 1 bounds |I| ≤ 1 is not a proof as stated": the proof is (i)–(iii) with n = 2.

## Not verified here

The audit lane's R40 and the web seat's census are read (through a sweep of all lanes), not re-run. The bound for
several cusps is stated, not tested.

## Verification

`verification/modules.py` (the builder), `rank_bound.py`. Lock: `tests/test_b1440_rank_bound.py`.
