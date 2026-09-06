# B1268 — WHERE NET CHIRALITY CANNOT LIVE ON THE CUSPED OBJECT: the boundary bound −h⁰(∂M;V) ≤ N(V) ≤ h⁰(∂M;V̄), |N(27)| ≤ 1 near the geometric E₆ point, and the θ-odd point actually reached has N = 0

**Date:** 2026-09-06 · **Seat:** cc · **Status:** PROVED (the lemma and the bound, checked exactly on every row) + NEGATIVE (the count: no reachable θ-odd point on the cusped object carries net chirality, and three is excluded near the geometric point by a theorem) · **Price: unchanged at 14**

## The question — MAIN_GOAL JOIN 1 q1, in the frame the goal document says works

B1260 walled the closed assemblies (PD) and the cusped abelian sector (Alexander reciprocity), and named a
deciding computation on B71's non-self-dual SL(3) components W1/W2. That computation was run
(`scripts/external_verification/nonselfdual_w1w2.py`: nine generic points, six cusp-fixed-vector points, three
central twists — h¹(V) = h¹(V\*) in every row) and landed on B1260's *agree* branch, together with the twelve
PSL(2,7) classes and a non-semisimple extension (`scripts/external_verification/nonselfdual_psl27_extension.py`).
But MAIN_GOAL's frame is not SL(3): it is **the θ-odd deformation of the geometric E₆ holonomy** (B575/B576,
"the chirality is exactly the θ-odd motion"), and on the *cusped* object nobody had asked what a θ-odd E₆
representation of π₁(m004) does to `h¹(27) − h¹(27̄)`. This arc asks, first with a theorem, then with the
representation itself.

## 1. The lemma and the bound (theorem; checked exactly on every row of §2)

For M = m004 (χ(M) = 0, torus boundary) and V a representation of π₁(M), write `res_V: H¹(M;V) → H¹(∂M;V)`.
Poincaré–Lefschetz duality on the pair (M, ∂M) and the long exact sequence of the pair give

> **N(V) := h¹(M;V) − h¹(M;V\*) = rank(res_V) − h⁰(∂M;V)**  (the lemma; proof in
> `docs/EXTERNAL_VERIFICATION_2026-09-06.md` §3),

and the images of res_V and res_V\* are mutual annihilators under the cup pairing
H¹(∂M;V) × H¹(∂M;V\*) → ℂ, so **rank(res_V) + rank(res_V\*) = h¹(∂M;V) = h⁰(∂M;V) + h⁰(∂M;V\*)**. Hence

> **THE BOUND: −h⁰(∂M;V) ≤ N(V) ≤ h⁰(∂M;V\*).** Net chirality on the cusped object lives only where the cusp
> holonomy keeps fixed vectors, and is at most their number.

For a family V_s through the geometric point, cohomology dimensions are upper semicontinuous, so
h¹(M;27_s) ≤ h¹(M;27_0) = 3 for small s, whence rank(res) ≤ 3 and

> **N(27_s) ≤ min(3 − h⁰(∂M;27_s), h⁰(∂M;27̄_s)) ≤ 1** for **every** small deformation of the geometric E₆
> holonomy, θ-odd or θ-even. **Three is impossible on the cusped object anywhere near the geometric point.**

## 2. The lemma instantiated, exact (`verification/cusped_bound.py`, `SELFTEST: PASS`)

| row | h⁰(M) | h¹(M) | h⁰(∂M) | h¹(∂M) | rank(res) | lemma value | N = h¹(V) − h¹(V\*) |
|---|---|---|---|---|---|---|---|
| geometric point, principal 27 | 1 | 3 | 3 | 6 | 3 | 0 | **0** |
| its dual 27̄ | 1 | 3 | 3 | 6 | 3 | 0 | 0 |
| complementarity | | | | | 3 + 3 = 6 = h¹(∂M) ✓ | | |
| subregular 27 (B1257) and its dual | 0 | 3 | 3 | 6 | 3 | 0 | **0** |
| C_{−1}, C_ω and their duals (the abelian sector at non-roots) | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| the θ-odd block V₈ at the geometric point | 0 | **1** | | | | | the deformation class exists |

At the geometric point all three classes of the 27 are boundary-supported (rank(res) = 3 = h¹): the count
"3" of B1253 is the cusp's, not the interior's. The bound reads −3 ≤ N ≤ 3 there and self-duality makes it 0.

## 3. The θ-odd representation reached (`verification/cusped_theta_odd_hp.py`; run record `verification/cusped_theta_odd_hp_run.txt`)

The exact cocycle class in H¹(M; V₈) (the hv8 slot, h¹ = 1) is used as the tangent; Gauss–Newton with the
analytic Jacobian (the adjoint Fox operator) on the relator, in ball arithmetic at 600 bits, from
ρ(a) = exp(εZ_a)ρ₀(a), ρ(b) = exp(εZ_b)ρ₀(b), ε = 1/696464 (|εZ| ≈ 0.02 on the rescaled 27), converges to a
representation ρ_s: π₁(m004) → E₆(ℂ) with **relator residual 2.6·10⁻⁶³**. It is a genuine point off the
F₄ stratum:

| | |
|---|---|
| \|tr ρ_s(w) − tr ρ_s(w⁻¹)\| for w = a, b, ab, a²b, [a,b], ba² | 3.01, 3.01, 2.7·10³, 2.9·10⁶, ~0, 2.9·10⁶ — **not self-dual ⇒ θ-odd, closure e₆** (B576's dichotomy) |
| tr₂₇ ρ_s(a) | 27.7517… + 1.3039…i (27 at the geometric point) |
| the cusp holonomy (μ_s, λ_s), [μ_s, λ_s] | 6·10⁻⁵¹ (commute to working precision) |
| **h⁰(∂M; 27_s), h⁰(∂M; 27̄_s)** | **0, 0** (full-rank pivots 1.5·10⁻¹⁷ and 2.2·10⁻⁹ relative — solid) |
| h¹(∂M; 27_s) = h¹(∂M; 27̄_s) | 0 |
| rank(res) | 0 |
| h¹(M; 27_s), h¹(M; 27̄_s) | 0, 0 at the 10⁻³⁰ threshold (smallest accepted pivots 7·10⁻²⁸ and 4·10⁻²⁶: these two ranks are the only decisions near the threshold, and **N does not depend on them**: with no cusp invariants the bound forces N = 0 whatever h¹(M) is) |
| **N(27_s)** | **0** |

Off the geometric point the cusp holonomy has **no invariants at all**, so by the bound N = 0 identically along
the reachable θ-odd deformation — the boundary-supported classes of the geometric point disappear and nothing
replaces them. The only places |N| = 1 is still allowed are the loci where μ_s and λ_s keep a common fixed
vector; an augmented Gauss–Newton search for such a point (equations μv = v, λv = v added to the relator) was
started from the θ-odd point and had not converged when this arc was sealed — it is the **named remaining
computation**, bounded in advance: **|N| ≤ 1 there.**

## 4. What this settles for JOIN 1

- **q1 for the cusped object, in the θ-odd frame:** no reachable point carries net chirality; **three is
  excluded by a theorem** near the geometric point, in every direction.
- Together with B1260 (closed wall; abelian wall), B1267 (every cell of the spectrum law vector-like) and the
  W1/W2, PSL(2,7) and extension rows (`docs/EXTERNAL_VERIFICATION_2026-09-06.md` §3), **no h¹ of this
  manifold, on any representation the corpus supplies or this session could reach, is a net count of
  anything** — the generation count is not a twisted Betti number of m004.
- The lemma is the general instrument: it locates the only possible carriers of net chirality on any cusped
  object (cusp-fixed vectors of a non-self-dual system) and bounds their yield.

## Controls (MB12, both directions)

- The lemma is checked on rows where its ingredients are all nonzero (rank(res) = h⁰(∂M) = 3) and on rows
  where they vanish; complementarity 3 + 3 = 6 is checked, not assumed.
- The θ-odd point is certified off the F₄ stratum by six trace differences that could all have been zero
  (at the geometric point the same six are 0, 0, 10⁻¹⁷³, …).
- Every rank at the θ-odd point is decided at 60 digits from a representation with residual 10⁻⁶³, with the
  smallest accepted pivot printed; the two near-threshold decisions are identified and shown not to affect N.
- The bound's semicontinuity step is exhibited as arithmetic in the lock: min(3 − k, k) ≤ 1 for every
  admissible k, and a control (the −1 character) with no boundary invariants.

## Verification

`verification/cusped_bound.py` (exact, ~4 min, `SELFTEST: PASS`) and `verification/cusped_theta_odd_hp.py`
(python-flint + mpmath, ~40 min for stage (a); stage (b) open). Lock: `tests/test_b1268_cusped_bound.py`
(the geometric-point instances and the V₈ class fast; the exact selftest in the slow lane).

- **Feeds on:** B1260 (the walls and the named computation), B1267 (the instrument), B575/B576 (the θ-odd
  frame), B1253 (h¹ = 3), B1256/B1257 (the subregular row), B71/B102 (W1/W2), the two external-verification
  scripts named above.
- **Registers:** I-26 UNEARNED, unchanged; its cusped reading is now bounded (|N| ≤ 1 near the geometric
  point) and computed (N = 0 at the reachable θ-odd point).
