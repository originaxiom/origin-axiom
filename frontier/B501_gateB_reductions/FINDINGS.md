# B501 — CL-3B: Gate B in-sandbox reductions — the chiral window collapses 70262 → 28, the {4,8} sector integrates at order 4, and the involution *is* θ on the tangent

**Status: banked (frontier). Pre-registered (docs/CLOSURE_CAMPAIGN_2026-07.md CL-3B + this
directory's README, enum committed per piece: REDUCED / NEGATIVE / TOOL-BLOCKED, CLOSED absent).
Firewalled; mathematics only; nothing to CLAIMS.md; firewall untouched.**

Three sub-pieces of Gate B (`T[4₁;E₆]`, docs/OPEN_PROBLEMS.md), each attacked with the declared
bounded method and run to completion in-sandbox. Reproducer: `probe.py` (piecewise CLI; parameters
logged in the three JSONs). Locks: `tests/test_b501_gateB_reductions.py`.

---

## Piece (i) — the σ-stability register (H103/H104): **REDUCED** (70262 → 28, not-found-in-bound)

**The declared bounded search.** A chiral (non-σ-stable) `2T↪E₆` is exactly one whose
27-restriction has *complex* character (B329/B356). The search space is B356's chirality window —
all faithful 27-dim assemblies with `(Sym³V)^G ≠ 0` and complex character (re-derived here and
gated: 71192 total / 70262 chiral for 2T; 1089/1028 for A₄) — sieved by three **exact necessary
conditions** any genuine embedding must satisfy:

- **C1 (cross map):** `Sym²(27) = 27̄ ⊕ 351′` ⇒ `V̄ ≼ Sym²V` as G-characters.
- **C3 (torsion realizability):** every `g` of order `n` maps to an order-`n` torsion element of
  simply-connected E₆; those are W-orbits on `(1/n)Q∨/Q∨`, so the **eigenvalue multiset of `g` on
  V** must be achievable by some `x ∈ (ℤ/n)⁶` acting on the 27 weights. Enumerated exhaustively
  per order (`n=2`: 3 achievable multisets, `n=3`: 7, `n=4`: 14, `n=6`: 47). This is the
  element-level "genuine conjugacy" test H103 asked for, run as a sieve.
- **C2 (adjoint fit):** `27⊗27̄ = 1 ⊕ 78 ⊕ 650` and `Sym³(27) = 1 ⊕ 650 ⊕ 3003`: a C3-matching
  torsion point determines candidate values `χ₇₈(g), χ₆₅₀(g)`; there must exist a choice of
  torsion profiles — one per maximal-cyclic class family, **consistent at shared power classes**
  (both order-6 families and the order-4 family of 2T meet at `−1`) — making the would-be `78|G`,
  `650|G` and `(Sym³V−1−650)|G` genuine characters (non-negative integer multiplicities), with
  `78|G` **orthogonally realizable** (finite ⊂ E₆(ℂ) is conjugate into the compact form, whose
  adjoint is real ⇒ quaternionic irreps in even multiplicity).

Every E₆ ingredient is **derived in-probe, exactly** (Fractions): the root system, the 27/78/650
weight systems by Freudenthal (gated by the Weyl dimension formula), and the three tensor
decompositions by greedy exact decomposition of the weight multisets (gated to zero remainder) —
no transcribed branching tables.

**Result (the attrition table; `b501_piece1.json`, 8 s):**

| population | input | pass C1 | pass C3 | pass C1∧C3 | pass C2 (all) |
|---|---|---|---|---|---|
| 2T chiral | **70262** | 68396 | 28 | 28 | **28** |
| 2T real (control population) | 930 | 930 | 17 | 17 | 17 |
| A₄ chiral | 1028 | 1028 | 2 | 2 | **2** |
| A₄ real | 61 | 61 | 3 | 3 | 3 |

**Controls.** The two *realized* canonical assemblies (B329: principal `3·1⊕3·1′⊕3·1″⊕6·3`,
trinification `9·1⊕3·1′⊕3·1″⊕3·2′⊕3·2″`) **pass every layer** (a sieve that rejected a realized
embedding would be broken — direction-of-error guard); the 2500× attrition of the chiral window
shows the sieve is nowhere near vacuous (MB12 bite check).

**Verdict: not-found-in-bound; REDUCED.** No chiral embedding was *found* (the bound is
character + torsion level; construction/exclusion of an actual homomorphism is beyond it), and the
escape did not close (28 candidates survive every exact necessary condition we can run). H103's
finite question sharpens from "any of 70262 ω-window assemblies" to **28 explicit survivors**
(14 conjugate pairs; full list in the JSON; extremes like `15·1′ ⊕ 6·2′` — pure ω-isotypic — and
near-balanced ones like `3·1⊕3·1′⊕2·1″⊕3·2⊕1·3⊕3·2′⊕2·2″`), all carrying the ω-twist in both the
1-dims and the 2-dims. The torsion sieve is the entire bite (C1 removes only 2.7%; C2 adds
nothing after C3 — banked as data). **Named next tool:** deciding realization of a specific
27-dim assembly needs invariant-theoretic Hom-space computation beyond character level
(nondegeneracy of the induced cubic + actual conjugacy — Gröbner-scale computation or a
finite-subgroups-of-E₆ classification), i.e. the specialist step H103 already names; what is new
is that it now has to be asked of only 28 explicit objects.

---

## Piece (ii) — third-order {4,8} integrability, one depth further: **REDUCED** (order 4 unobstructed)

**Method (B370's jet machinery, extended to `t⁴`; declared before running).** Deform
`ρ_t(g) = exp(t·z₁ + t²·z₂ + t³·z₃)ρ(g)` and expand `X_t(rel) = I + tP₁ + ... + t⁴P₄` (B352's
two-basis architecture, dps 100). Self-gating: `‖P₁‖,‖P₂‖,‖P₃‖ ≈ 0` gate the cocycle, the `z₂`
solve and the `z₃` solve *inside the same expansion*; `ad(q₄) = P₄` defines the order-4
obstruction (exact-Gram normal equations); classes are read per exponent block against B352's
coker functionals. **Gauge discipline:** `P₃`/`P₄` are affine-linear in `z₂`/`z₃` (the letter jets
carry no `B²`-at-`t³` or `C²`-at-`t⁴` terms), so unit finite differences are exact; the order-3
class is first killed *exactly* inside the `z₂`-indeterminacy span, and the corrected order-3
class must sit at the floor before order 4 is read. The order-4 verdict is taken modulo the
`z₃`-shift span (six unit cocycle shifts, full re-runs) with the MB12 random-vector control —
quotienting by a *sub*-span is logically safe for an "unobstructed" verdict. Controls: coboundary
(exact-tier zero) and `m=1` (the A-polynomial curve, integrable to all orders).

**Result (`b501_piece2.json`; dps 100; directions as declared):**

| direction | P₁ gate | P₂ gate | P₃ gate | order-3 class | ‖class(q₄)‖ | below own gate floor | span / MB12 |
|---|---|---|---|---|---|---|---|
| coboundary (control) | 1.2e-62 | 3.5e-64 | 1.2e-76 | 6.2e-87 | **1.1e-94** | 32 orders (exact tier) | — |
| m=1 (integrable control) | 1.4e-52 | 5.3e-52 | 1.4e-51 | 9.6e-62 | **2.6e-61** | 9.7 orders | rank 0; MB12 1.5–2.5 |
| m=4 (escape) | 2.2e-55 | 7.0e-53 | 8.4e-55 | 8.5e-63 | **1.02e-60** | 7.8 orders | rank 1; MB12 0.85–1.0 |
| m=8 (escape) | 2.5e-54 | 9.5e-47 | 2.4e-43 | 3.1e-54 → 1.5e-57 gauge-fixed | **2.19e-48** | 5.0 orders | span saturates ℂ⁶ (MB12 vacuous → absolute-floor verdict) |
| m=4+m=8 (mix) | 1.7e-54 | 3.1e-49 | 3.4e-44 | 4.2e-55 | **1.54e-49** | 5.3 orders | base mode (full-run log-harvest: 1.03e-48, 4.8 orders below its 5.9e-44 gate) |

**Verdict: REDUCED — the escape sector extends to FOURTH order.** Every direction's order-4
class sits ≥5 orders below its own expansion-floor gates, matching the integrable control's
signature; the coboundary control is exact-tier. With B347 (dim H¹ = 1 per exponent), B352
(order 2) and B370 (order 3), the `{4,8}` escape sector — including the polarization mix — now
carries integrability evidence at **orders 1–4**. The θ-parity signature confirms the derivation
`q₄ = [z₁,z₃]+[z₂,z₂]`-type is θ-**even** (odd `z₁,z₃`, even `z₂`): in every {4,8} direction the
{4,8}-block class components sit below the leading F₄-block component (e.g. m=8:
`8.8e-54/1.2e-51` vs `2.2e-48`). **Execution record (honesty):** the full treatment (gauge fix +
span, ~85 min/direction) is banked for coboundary/m=1/m=4/m=8; the mix48 full run completed but
lost its JSON to a file race with the staged base re-run (numbers harvested from `p2_mix48.log`
into the part JSON — same floor, same verdict). A staged base mode (minimal-norm defining
system, two bounded foreground stages per direction) was run for all five directions as a
cross-check and **reproduces the full-run classes at the same floors** (m=4: identical
`1.018e-60`; coboundary: identical `1.118e-94`; m=1: identical `2.612e-61`). Where the z₃-shift
span saturates ℂ⁶ (m=8, mix — deltas at q₄-scale against a floor-level class) MB12 goes vacuous
and the span readout is **not used**; the verdict there is the absolute criterion (class ≥3
orders below the direction's own gates), which is the conservative direction. Honest limits:
order ≥ 5 untested; the defining-system dependence is quotiented only where the quotient is
informative; no formality theorem exists for knot groups — this is evidence, not proof, of
smoothness.

---

## Piece (iii) — the geometric θ-identification: **REDUCED** (the involution *is* θ on the tangent, canonically)

Three tiers, two of them exact:

1. **Exact — θ is an automorphism of the π₁-module `𝔢₆_{Adρ}`.** B351's Jacobi-verified θ maps
   *every one of the 78 chain basis vectors* to `(−1)^{m+1}` times itself (checked with integer
   arithmetic, all 78). Since `Adρ` is block-diagonal in this basis and θ is the blockwise scalar
   `(−1)^{m+1}`, `[θ, Adρ(g)] = 0` *exactly* — θ fixes the geometric representation pointwise and
   therefore acts directly on `H¹(π₁(4₁), 𝔢₆)`, where it multiplies the line at exponent `m` by
   `(−1)^{m+1}`.
2. **Exact — the sl₂-commutant lemma.** Any linear map commuting with the principal sl₂ is
   blockwise scalar (the six `Sym^{2m}` are multiplicity-free; Schur). Bracket preservation forces
   `λ_m λ_{m'} = λ_{m''}` over the **46 exact block-coupling relations** of the chain brackets
   (each bracket expressed in the chain basis by exact Fraction solves). Smith normal form of the
   relation lattice: invariant factors `(1,1,1,1,1,2)`, free rank 0 ⇒ **exactly two solutions**:
   the identity and the pattern `(−1)^{m+1}` = θ. So the sl₂-commutant of `Aut(𝔢₆)` is `{1, θ}`,
   its inner part is trivial, and the involution's tangent action (whose intertwiner is only
   determined up to this commutant times the trivially-acting centre) is **canonical**.
3. **Numeric (dps 100) — the intertwining itself.** The hyperelliptic involution
   `σ: a→a⁻¹, b→b⁻¹` is realized *inner*: `ρ∘σ = D ρ D⁻¹` with `D ∈ SL(2)` (residual `1.4e-71`).
   Its pullback on each H¹ line equals θ's module action **at the cocycle level**:

   | m | 1 | 4 | 5 | 7 | 8 | 11 |
   |---|---|---|---|---|---|---|
   | `‖Ψz₀ − (−1)^{m+1} z₀ mod B¹‖` | 6.3e-71 | 5.4e-71 | 6.7e-71 | 1.5e-70 | 3.7e-70 | 7.2e-64 |
   | wrong-sign control | 2.0 | 2.0 | 2.0 | 2.0 | 2.0 | 2.0 |

   (`z₀` normalized, `‖z₀ mod B¹‖ = 1` — non-vacuity; the amphichiral involution re-derives as
   the antilinear real structure with `J² = +1` at floors `9e-71 … 3.6e-59` — it is *not* θ, and
   it commutes with θ exactly since θ is a real blockwise scalar.)

**Verdict: REDUCED — the identification holds, with its precise sense pinned.** The manifold's
orientation-preserving (hyperelliptic) involution induces **exactly θ** on the E₆ tangent
`H¹(4₁, 𝔢₆)`, and by the commutant lemma this statement is canonical, not convention. The
sharpening over B347/B351: at the *representation* level the involution does **not** realize the
outer class (`ρ∘σ` is inner-equivalent to ρ — `D` is an SL(2) element); rather θ itself fixes
`ρ_geo` pointwise, and the involution's canonical tangent action coincides with θ's module
action. "The involution induces θ" is a theorem *about the tangent*, with the two exact lemmas
carrying it; what stays open is the identification beyond the tangent germ (the higher-order jets
— piece (ii)'s territory: the depth-2 τ-defect already *sees* the θ-fold, B370 leg B).

---

## Honest tiers and limits

- **Exact:** the piece-1 lattice toolkit (root system, Freudenthal, Weyl dims, the three tensor
  decompositions — all gated), the window enumeration and sieve arithmetic (integer snaps at
  1e-6 off exact tables, values ≤ 27³ — B356's banked justification), piece-3 tiers 1–2.
- **Computer-assisted (dps 100):** piece 2 entirely (floor-level zeros are evidence of exactness,
  not proof; order ≥ 5 untested; the m=1 control calibrates but does not certify), piece-3 tier 3.
- **Piece 1 is a sieve of necessary conditions:** survival ≠ realization. The 28 survivors are
  *candidates*; no chiral embedding is constructed, and none is excluded beyond the bound. The
  conditions used are provably necessary for any embedding into simply-connected E₆(ℂ) acting on
  the 27 (the H103/H104 framing).
- Nothing promotes; no physics claim; the hierarchy/value firewall (B327/B329/B335–B338) is
  untouched by all three verdicts.

## The fence

`probe.py` (this directory; CLI per piece; all parameters logged in the JSONs) ·
`b501_piece1.json`, `b501_piece2.json` (+ per-worker parts), `b501_piece3.json` ·
`tests/test_b501_gateB_reductions.py` (always-on: full piece-1 re-derivation + banked locks;
OA_SLOW=1: piece-3 exact recompute + a piece-2 direction re-run). Machinery reused read-only:
B352 `cup_product.py` (loaded with declared dps), B370 `massey.py`, B356 `sigma_stability.py`,
B351 `exact_e6.py`, B347 `e6_tangent_gradings.py`.

**Provenance.** Pre-registration: `docs/CLOSURE_CAMPAIGN_2026-07.md` (CL-3B) + `README.md` here.
Method sources: B329/B327/B356 (piece i), B352/B370 (piece ii), B351/B347 (piece iii).
Hints: H103/H104 (`docs/HINT_LEDGER.md:183-184`). Gate: docs/OPEN_PROBLEMS.md §B.
Nothing to CLAIMS.md; firewall untouched.
