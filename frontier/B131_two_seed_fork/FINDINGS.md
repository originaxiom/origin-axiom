# B131 — Two-seed gluing creates an internal discrete fork: heterogeneity makes a choice (answers S032-B, V120)

The arc *after* B130. B130 located the question precisely: a single metallic seed is **internally fork-free** (the
Fricke–Vogt invariant `κ` is free/continuous on the fixed locus; the substitution word is the unique deterministic
fixed point) — the only discrete fork is the **external seed label** `m`. The open question (`S032-B`, the precise form
of the standing "minimal multiplicity to become more" intuition): **does combining two distinct seeds create an
*internal* discrete fork neither had alone?** Pushed into the amalgam (the cusp-gluing). Re-derived in-sandbox
(verify-don't-trust).

**One-line result.** **Yes — and it is *heterogeneity*, not multiplicity, that does it.** Gluing two metallic bundles
along their boundary tori (shared suspension) matches their A-polynomial curves in the 2-dim boundary-torus character
space; **two distinct seeds = two distinct curves → a 0-dimensional (discrete) intersection** → the previously-free `κ`
collapses to a **finite set** (a fork). The **same seed** glued to itself = the **same curve** → the intersection is
the whole curve → `κ` stays **continuous** (no fork). So the minimal multiplicity for an internal discrete fork is
**two distinct seeds**. This is aperiodic-order / 3-manifold **mathematics**, **not** a physics bridge. MATH and
physics in different tiers. Nothing to `CLAIMS.md`; P1–P16, the functorial `Sym(W)→trace-ring` wall (B85), and the
merged B124–B130 untouched.

## The mechanism (proven)

Each seed's fixed locus `X(M_m)` is a 1-dim curve; its boundary holonomy data `(κ = tr[A,B], P = tr(t))` (the
meridian/longitude and suspension traces) traces an **A-polynomial curve** in the 2-dim boundary-torus character
variety. Gluing two bundles (shared suspension `t`) matches `(κ, P)`. Two curves in a 2-dim space:

| combination | curves | intersection | κ |
|---|---|---|---|
| single seed | — | — | **free** (B130) |
| same seed (1,1),(2,2) | identical | the whole curve | **free** (continuum) |
| **distinct seeds** | **distinct** | **finitely many points** (Bézout) | **discrete (a fork)** |

## The A-polynomial curves κ = P_m(trT), validated two independent ways

- **m=1:** `κ = trT⁴ − 5·trT² + 2` — **exactly B67's figure-eight identity**. (`tr(t)²(x) = (x²+x−1)/(x−1)`.)
- **m=2:** `κ = trT² − 6` — **exactly B69/V33's m=2 framing**. (`tr(t)²(x) = x⁴/(x²−2)`, matching B69 exactly.)
- **m=3:** `tr(t)²(x)` is **not rational** — B69's "irrational double cover" — so its `(κ,trT)` curve is higher/irrational.

Both m=1,2 relations were *also* re-derived here from explicit SL(2,ℂ) matrices (residual ~1e-14), an independent
in-sandbox check on top of the B67/B69 agreement.

## The forks (matched κ on the glued character variety; identity gluing)

| pair | matched κ (non-reducible) | type |
|---|---|---|
| **(1,2)** | **{−4, −2}** | **exact** ( `(trT²−2)(trT²−4)=0` ) |
| (1,3) | {−3.920, −2, −1.845±2.229i, −0.689, 2.299} | numerical (6 values) |
| (2,3) | {−4.397, −2, −1.427, 3.824} | numerical (4 values) |

**Every matched value has κ≠2, hence every fork point is an irreducible rep** (reducible ⟺ tr[A,B]=2). `κ=−2`
(parabolic longitude = the shared **complete-cusp** configuration) appears in every pair; the **other** values are
genuine new gluings. The number of fork values is the intersection number (grows with seed complexity / curve degree).

## Resolving choice-vs-determined (the B130-discipline question)

By B130's forced-choice definition (invariant + discretely-multivalued + unsymmetrizable): the glued system's `κ`
takes a **finite set** of values, all irreducible, none related by symmetry (`κ` is preserved by the relevant
symmetries, so distinct κ are unsymmetrizable). So a **forced choice exists** in the glued two-seed system. The
richer pairs (1,3),(2,3) give an unambiguous **multi-way** choice (≥2 genuine non-cusp values); the minimal pair
(1,2) gives `{−4,−2}` — two values at face value, or, if one reads `κ=−2` as the always-present complete-cusp
configuration, a single genuine new gluing `κ=−4` (a forced **value**). Either reading agrees on the robust,
gluing-map-independent core: **distinct seeds discretize the continuum** (continuum → finite), and a single seed (or
same-seed multiplicity) does not.

## The reading (tier: MATH; firewall POSTULATED)

B130: a single seed is a **moduli space** — it parametrizes, it does not choose. B131: gluing two **distinct** seeds
creates **discreteness** — a choice born from **heterogeneity**, not from multiplicity (same-seed stays a continuum).
So the precise form of "minimal multiplicity to become more" is: **two distinct seeds**. This is emergent
aperiodic-order / 3-manifold mathematics — *not* the Standard Model's vacuum selection (the honest `S032-B`
expectation: even a "yes" is a discovery about emergence in this mathematics, not a physics bridge).

## Honest scope (verify-don't-trust)

- **(1,2) is exact** and doubly-validated (B67 for m=1, B69/V33 for m=2, plus a matrix re-derivation here). The
  general **mechanism** (distinct curves → discrete; same curve → continuum) is a Bézout fact, gluing-map-independent.
- **(1,3),(2,3) are numerical** (Newton root-finding in ℂ²; m=3's curve is irrational so no closed form was extracted).
  They confirm the qualitative result (discrete forks) across distinct pairs.
- The exact discrete set depends on the **gluing map** (identity gluing used here) and on counting the shared
  complete-cusp `κ=−2`; the **qualitative** continuum→discrete transition does not.
- Tier: MATH (character varieties of graph-manifold gluings). The physics reading stays POSTULATED.

## Reproduce

```
python frontier/B131_two_seed_fork/probe.py
python -m pytest tests/test_b131_two_seed_fork.py -q
```

The exact (1,2) fork, the same-seed continuum, and irreducibility run unconditionally (sympy); the matrix
re-derivation of the m=1,2 A-polynomials is numpy-guarded.

**Tier.** MATH + a firewalled reading (POSTULATED). Resolves `speculations/S032` Target B (YES — heterogeneity makes a
choice; minimal multiplicity = two distinct seeds). Nothing to `CLAIMS.md`; P1–P16, B85, B124–B130 untouched. Ledger
**V120**.

**Anchors:** B130 (`K013`/`S032`, the question this answers — single-seed fork-freeness), B67 (`K004`, the m=1
A-polynomial identity), B69 (the metallic A-poly family / V33 m=2 framing), B128 (`K011`, why word-concatenation was
the *wrong* construction — its only fork chirality symmetrizes away). External: A-polynomials of once-punctured-torus
bundles; character varieties of torus gluings.
