# B174 — the GL(2,ℤ) gluing-map landscape (H5): the character-variety face of interaction-born structure

**Date:** 2026-06-18. **Status:** the cusp-gluing lane (OPEN_LEADS **H5**) — the **character-variety companion** to
the spectral multi-seed arc (B171–B173). Maps the discrete-vs-continuum structure of two metallic once-punctured-torus
bundles glued along their cusp tori, across the **gluing map** φ ∈ GL(2,ℤ); extends B131 (identity gluing only) and
B134 (one swap) to the landscape, and **closes H5 → CHARACTERIZED**. **Firewall-side**: low-dim-topology /
character-variety math (emergent, `K010` boundary); no scale/Λ; **nothing to `../../CLAIMS.md`**; P1–P16 frozen.
Ledger V168. Reproducer `gluing_landscape.py` (`ALL CHECKS PASS`).

## Setup

Each once-punctured-torus bundle has **one cusp**; gluing two of them along their cusp tori gives a closed graph
manifold (so the gluing is **pairwise** — see Scope). The boundary holonomy is the trace ring of the **abelian**
peripheral `ℤ² = ⟨μ,λ⟩`: coordinates `(p,q,r) = (tr μ, tr λ, tr μλ)` with the commuting relation
`r² − p q r + p² + q² − 4 = 0`. The bundle's A-polynomial curve is `C = {q = f(p)}` (figure-eight, B67:
`f(p)=p⁴−5p²+2`). The mapping-class group acts on `(p,q,r)`:
`S` (swap `μ↔λ`): `(p,q,r)→(q,p,r)`; `T` (Dehn twist `λ→λμ`): `(p,q,r)→(p, r, pr−q)`.
The glued character variety under gluing map φ is `C ∩ φ(C)`; its dimension (continuum vs discrete) and the discrete
**count** measure the interaction-born structure.

## Validation (reproduces the banked results exactly)

- **V1 [B131]:** identity gluing — `(1,1)` same-seed → **CONTINUUM** (same curve, κ free); distinct `(1,2)` →
  **discrete `{−4,−2}`** (exact, the `(trT²−2)(trT²−4)=0` fork).
- **V2 [B134]:** swap (`S`) gluing of the figure-eight to itself → the condition `p = f(f(p))`, **degree 16** →
  discrete *even for the same seed* (the gluing map alone forks; Kitano–Nozaki).

## The landscape (new)

| gluing map φ | fork size (|discrete κ-set|) |
|---|---|
| identity | **CONTINUUM** |
| `T` (twist) | 9 |
| `T²` | 10 |
| `S` (swap) | 16 |
| `ST`, `TS`, `STS` | 32 |

**The characterization.** The glue is a **CONTINUUM** *only* on the **measure-zero curve-aligned locus** — φ that
map the curve `C` onto itself (the identity for a same-seed glue). For **every other** gluing map the glued variety is
**0-dimensional (discrete)** — a forced fork. The fork **size is φ-dependent, not simply monotone in word length**:
it **multiplies under swaps** (`S→16=4²`, `ST→32`) — a swap composes `f` with itself — and **grows slowly under
twists** (`T→9`, `T²→10` — `T` factors as `(2−p)(f(p)²−(p+2))=0`, i.e. `p=2` plus a degree-8 piece). The finiteness
for *every* nontrivial φ is the **Kitano–Nozaki Bézout** fact (distinct A-poly curves intersect in `gcd=1 ⟹` finitely
many points), here made explicit across the gluing-map family.

## The cross-face agreement (why this matters)

This is the **character-variety face of the same principle the spectral arc (B171–B173) found**: *interaction of
distinct units forces structure no single unit has.* On the **spectral** side, weaving two distinct metallic chains
produced an interaction-born **combination gap** (a rank-3 gap-label absent from either pure chain). On the
**character-variety** side, gluing two bundles with any non-aligning map produces an interaction-born **discrete
κ-fork** (absent from the single-seed continuum). Both faces: the lone unit is a moduli space (continuum, K013); the
choice/structure appears only with the interaction (K014, B131). B174 adds that the *amount* of forced structure
scales with the interaction map (the fork size; the spectral combination-label complexity).

## Scope / honesty (what this is NOT)

- **Pairwise only.** The once-punctured-torus bundle has one cusp, so this glues two pieces into a closed manifold.
  **Literal large-N** (a chain of N pieces) needs **multi-cusp** building blocks (twice-punctured-torus bundles /
  metallic chain-link analogues) — a genuine generalization, **NEEDS-SPECIALIST**.
- **The all-φ theorem** (a closed classification of the fork size as a function of φ ∈ GL(2,ℤ), and the exact
  continuum locus) is the **Kitano–Nozaki Bézout** result in general — cited, not re-proved; a uniform formula is
  NEEDS-SPECIALIST. The table is a computed slice, not a theorem.
- Low-dim-topology / character-variety math (`K010` boundary). No scale, Λ, mass, or constant; nothing supports a
  physics claim.

## Firewall
Emergent character-variety / 3-manifold mathematics; no physical-magnitude claim; **nothing to `../../CLAIMS.md`**;
P1–P16 untouched.

## Anchors
`B131`/V120 + `K014` (the identity-gluing two-seed fork — extended here), `B134` (the swap example + the Kitano–Nozaki
qualification), `K013` (single seed = continuum/moduli space), `K001`/`B67` (the Fricke trace map + the figure-eight
A-poly curve `f`), **B171–B173/V165–V167** (the spectral face this agrees with), `../../speculations/S035` (the
">1 building block" reframe). External: Kitano–Nozaki 2020 (arXiv:1904.02559, the splice A-poly Bézout finiteness);
Culler–Shalen (character varieties of glued manifolds).

## Reproduction
`python frontier/B174_gluing_map_landscape/gluing_landscape.py` — V1 the identity fork (B131); V2 the swap degree-16
(B134); L1 the gluing-map landscape (fork size vs φ); V3 the once-cusp scope + cross-face agreement. Prints
`ALL CHECKS PASS`.
