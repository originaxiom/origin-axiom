# K019 — The collective (multibody) metallic spectrum: what interaction of distinct units builds

> **Explainer** (`GOVERNANCE.md`). Self-contained; standard material cited to the literature, the project's own use
> cited by `B`/`V` number (no re-proof). Nothing here promotes to `../CLAIMS.md`; never a premise in a proof. The
> textbook-layer consolidation of the **multi-seed / multibody arc** (B171–B176) — the companion to `K007`/`K010`
> (the *single*-chain metallic quasicrystal).

`K007`/`K010` named the object for **one** metallic unit: the metallic-mean Schrödinger cocycle / Fibonacci-type
quasicrystal, with its Fricke–Vogt invariant `κ` and its zero-measure Cantor spectrum. This explainer is the **many**
case — what happens when **distinct** metallic units interact. The one-line result: **a lone unit only parametrizes;
structure that no single unit has appears only with the interaction of *different* units — and that structure is
predictable.**

## The two faces of one principle

The project reached the same statement from two independent directions:

| face | the unit | what *interaction of distinct units* generates | where |
|---|---|---|---|
| **spectral** | a metallic chain | an **interaction-born combination gap** — a rank-3 gap-label `n₁α₁+n₂α₂` (both nonzero), absent from either pure chain | B171–B173, B175 |
| **character-variety** | a metallic bundle | an **interaction-born discrete `κ`-fork** — a continuum collapses to finitely many values | B131/`K014`, B174 |

A single seed is a moduli space (a continuum — `K013`); **choice/structure enters only with the interaction of
different units** (`K014`). K019 records *how much* and *how predictable* that structure is.

**Read precisely (B180):** "two faces" is **one hinge quantity + two analogous operations**, *not* a numerical
identity. The hinge `κ = tr[A,B]` genuinely lives on both faces — it is the character-variety boundary coordinate
*and* the conserved trace-map invariant whose value sets the spectral type (κ=2 full band → κ>2 Cantor) [a real link,
`K010`]. But the two *interaction operations* — **cusp-gluing** (match two bundles' `(κ,P)` → a discrete κ-fork) and
**potential-weaving** (add two metallic potentials → gap labels `n₁α₁+n₂α₂`) — are **distinct math with distinct
outputs** (trace values vs IDS fractions); they share only the *signature* single=continuum / distinct=structure. The
naive read "the κ-fork values equal the gap labels" is **false** — exactly the conflation the do-not-conflate boundary
(`B179`) guards against.

## The spectral face, made quantitative (B171–B176)

For a woven two-frequency chain `V_n = λ₁ g(α₁n+θ₁) + λ₂ g(α₂n+θ₂)` (`α_m = 1/`metallic-mean):

1. **Heights — exact, all couplings (a theorem).** Every gap sits at a **gap-labeling label** `n₁α₁+n₂α₂ mod 1`.
   The label group is the **rank-3 frequency module** `ℤ+ℤα₁+ℤα₂` — *product-free* — a citable consequence of the
   gap-labeling theorem (Johnson–Moser 1982; Bellissard; Damanik–Fillman 2022); the L16 rank formula
   `rank = 1 + #distinct quadratic fields` is confirmed (distinct fields → 3; same field → 2). The `√(dᵢdⱼ)` "product
   would raise the rank" worry is **dispelled** — products are a ℤ^d≥2 / 2D-tiling feature, not a 1D superposition
   (B173). So `(α₁,α₂)` → **every gap position, exactly.**
2. **Widths — the order-power law at weak coupling (`[num]`).** A combination gap of label `(n₁,n₂)` opens at
   perturbative **order `|n₁|+|n₂|`**, so `width ~ λ^{|n₁|+|n₂|}`: the gap's *label-complexity is its
   width-scaling exponent* (verified — order-2 slope ≈ 2, order-3 → 3; B175). So `(λ₁,λ₂)` → **every gap width**
   (perturbatively). **Bound:** the law is perturbative — widths **saturate** at strong coupling.
3. **The golden privilege (`[num]`).** The combination structure preferentially **dresses the golden (φ)
   resonance**: golden's satellite ladder dominates both silver's and bronze's (θ-averaged, both models), and not
   because golden has a wider bare gap. But it is **golden-stands-alone**, *not* a monotone golden>silver>bronze
   order (silver ≈ bronze) — φ is the Hurwitz-extremal most-irrational = KAM-most-robust frequency (B176). The tie to
   the `P000` anchor is a one-way `[RHYME]`.

**Net:** the collective spectrum is **two-number-predictable** — `(α₁,α₂)` fix every gap's *position* and `(λ₁,λ₂)`
fix every gap's *width* (weak coupling) — a genuinely *collective* fact (the single unit has no combination gaps).

## A modelling caveat that matters (B175)

The gap **heights** (the module) are **potential-independent** — a theorem. But **which** labels actually open, and
their **widths**, are **potential-dependent**: the combination "ridge" opens wide in a smooth **cosine
(bichromatic)** chain but is **nearly closed** in the metallic **Sturmian-indicator** chain. *Module ≠ realized
gaps.* (This is why a cross-session pass that switched silently from the Sturmian to the cosine model over-read a
cosine-specific ridge as a universal property — B175 reconciles it.)

## The honest physics-contact statement

This is **emergent quasicrystal physics** (`K010` boundary) — and notably, both of the project's genuine contacts
with real physics are **collective**: (i) this multibody gap-labeled spectrum (bichromatic optical lattices and
quasicrystals are *measured* materials), and (ii) the SL(2,ℤ) trace-map = N=2\* class-S S-duality action (`B150`),
which is a **higher-genus / collective** statement. The thing "that makes the difference" was never in interrogating
one `κ`; it is in the network. **But the bound is the same as everywhere in this program:** this is predictivity over
**structure** (where gaps sit, how wide, which resonance is dressed) — **not** over the *value* of a fundamental
constant. The win is real and it is bounded; both halves true.

## What stays open (NEEDS-SPECIALIST)
Literal **large-N** gluing (multi-cusp building blocks; the genus-2 nesting, H5-a); the **exact** gap-label group for
the *discontinuous* Sturmian sampling; **which** labels open *actual* gaps off the real axis (B165); a **rigorous**
golden-privilege theorem (why φ uniquely stands alone); SL(n) higher-rank (B166).

**Anchors:** B171 (the woven baseline + density trap), B172 (the combination gap), B173 (the gap-labeling reduction /
L16), B174 (the gluing-map landscape / H5), B175 (two-number predictivity / the width law), B176 (the golden
privilege); `K007`/`K010` (the single-chain object), `K013`/`K014` (continuum vs interaction-born choice),
`../philosophy/P000` (the φ `[RHYME]`), `../speculations/S035` (the "building blocks' behaviour" reframe). External:
gap-labeling theorem (Johnson–Moser; Bellissard; Damanik–Fillman 2022); perturbation theory of quasiperiodic gaps;
bichromatic / Aubry–André operators; Hurwitz / KAM (φ = most-irrational = most-robust); Kitano–Nozaki 2020 (the
splice A-poly finiteness, the character-variety face).
