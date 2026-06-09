# K014 — Choice from heterogeneity: gluing distinct seeds discretizes the invariant

> **Explainer** (`GOVERNANCE.md`). Self-contained; standard material cited to the literature, the project's own use
> cited by `B`/`V` number (no re-proof). Nothing here promotes to `../CLAIMS.md`; never a premise in a proof. The
> bankable MATH of the two-seed-fork arc (B131/V120), the companion to `K013`.

## The question (answered)

`K013` (B130) showed a single metallic seed is **internally fork-free**: the Fricke–Vogt invariant `κ` is *free*
(continuous) on the fixed locus, the substitution word is the unique deterministic fixed point, and the only discrete
fork is the **external** seed label `m` — the structure is a moduli space, it parametrizes but does not choose. The
sharp follow-up (`../speculations/S032` Target B; the precise form of "minimal multiplicity to become more"): **does
combining two distinct seeds create an *internal* discrete fork neither had alone?**

## The answer: yes — and it is heterogeneity, not multiplicity

Glue two metallic bundles `M_{m₁}, M_{m₂}` along their boundary tori (shared suspension `t`). Each seed's fixed locus
`X(M_m)` is a 1-dim curve whose boundary holonomy data `(κ = tr[A,B], P = tr(t))` traces an **A-polynomial curve** in
the 2-dim boundary-torus character variety. Gluing matches `(κ, P)`:

| combination | curves | result |
|---|---|---|
| single seed / same seed glued | identical curve | `κ` **free** (continuum) — no fork |
| **two distinct seeds** | **distinct curves** | **0-dimensional intersection** (Bézout) — `κ` **discrete** = a fork |

So the minimal multiplicity for an internal discrete fork is **two distinct seeds**: it is the **heterogeneity** of the
seeds (distinct A-polynomial curves), not multiplicity per se, that creates the choice — gluing a seed to a *copy* of
itself keeps the continuum.

## The A-polynomial curves (validated)

`κ = P_m(trT)`, the meridian/longitude trace relation: **m=1** `κ = trT⁴ − 5·trT² + 2` (B67's figure-eight identity),
**m=2** `κ = trT² − 6` (B69/V33's m=2 framing); **m=3** has an irrational `tr(t)²(x)` (B69's double cover). The (1,2)
fork is exact: `(trT²−2)(trT²−4)=0 → κ ∈ {−4, −2}`, both **irreducible** (reducible ⟺ tr[A,B]=2, and −4,−2 ≠ 2). Pairs
(1,3),(2,3) give larger discrete forks (numerical); `κ=−2` (parabolic longitude = the shared complete-cusp
configuration) recurs, the other values being genuine new gluings.

## The reading

`K013`: a single seed is a **moduli space** — parametrizes, does not choose. `K014`: gluing two **distinct** seeds
creates **discreteness** — a choice born from heterogeneity. The two together: a single self-referential unit is rigid
(no internal fork), and **choice enters only with the interaction of *different* units**. This is emergent
aperiodic-order / 3-manifold mathematics (character varieties of torus/graph-manifold gluings) — **not** the Standard
Model's vacuum selection; the firewall (`../philosophy/P007`) is unchanged, and the only "this is physics" remains the
emergent `K010` naming.

## Scope

The (1,2) result is exact and doubly-validated (B67, B69/V33, plus an in-sandbox matrix re-derivation); the
distinct-curves → 0-dimensional-intersection step is a Bézout fact. Pairs (1,3),(2,3) are numerical (m=3's curve is
irrational). The full theorem-version (`S032` Target A) remains open.

> **Prior art + qualification (B134/V123 novelty audit).** This phenomenon is **known**: **Kitano–Nozaki 2020**
> (arXiv:1904.02559) prove finiteness of a splice's torsion image exactly via the two pieces' A-polynomial curves
> intersecting in the boundary-torus character variety (`gcd=1` ⟹ Bézout-finite). **Important qualification:** their
> evidence shows the discreteness is driven by the meridian↔longitude-**swapping splice** gluing, **not** by the
> pieces being distinct — a same-knot splice `Σ(K,K)` is *already* finite. So the **"heterogeneity makes the choice"**
> reading here is correct **only for the identity gluing** (under which distinct seeds → distinct curves → discrete,
> same seed → same curve → continuum); under the splice/swap gluing the **gluing map alone** forks even a same-seed
> glue (verified in B134: swap-glue fig8-to-fig8 → `P=f(f(P))`, degree 16, discrete). The honest general statement is
> *the gluing map determines continuum-vs-discrete*; distinctness suffices under the identity gluing. B131's math
> stands; this is a framing qualification. See `../docs/NOVELTY_AUDIT.md` (R2).

**Anchors:** B131/V120 (the result), B130/`K013` (single-seed fork-freeness — the question this answers), B67/`K004`
(the m=1 A-polynomial), B69 (the metallic A-poly family / V33), B128/`K011` (why word-concatenation was the wrong
construction — chirality symmetrizes away), `../speculations/S032` (the program), `K010` (`κ` = the Fricke–Vogt
invariant), **B134/`../docs/NOVELTY_AUDIT.md` (the Kitano–Nozaki prior art + the gluing-map qualification)**. External:
A-polynomials of once-punctured-torus bundles; **Kitano–Nozaki 2020 (arXiv:1904.02559)**; character varieties of torus
gluings (Culler–Shalen).
