# B201 — the metallic (silver) SL(3) character variety from the trace-map fixed locus

**Date:** 2026-06-24. **Status:** the SL(3) extension of the "metallic A-polynomial" direction. **Part 1
(BANKED, exact):** the silver (m=2) SL(3) character variety `Fix(T_2²)` has **four** dim-2 components — **one more
than the figure-eight's three** (B71) — including a component with no figure-eight analog. m=1 reproduces B71 exactly
(validation). **Part 2 (DEFERRED, not banked):** the per-component peripheral A-variety relations (the silver analog of
B71's `M³=L`) are *not* extracted here — my quick peripheral pipeline failed its figure-eight `M³=L` validation gate, so
per verify-don't-trust nothing from it is banked; the correct route is recorded. Standalone character-variety /
low-dim-topology math; **no physics; nothing to `CLAIMS.md`; P1–P16 untouched.** Ledger V194.

## Setup

The bundle monodromy of the metallic bundle `RᵐLᵐ = M_m²` (`M_m=[[m,1],[1,0]]`) acts on the 8 SL(3) trace
coordinates of the fiber `F₂=⟨a,b⟩` by `T_m²`, where `T_m` is the B48 metallic trace map (`φ_m: a→aᵐb, b→a`,
Cayley–Hamilton recurrences). A fiber character extends over the bundle iff it is **fixed** by `T_m²` (B67/B71). So
`Fix(T_m²)` is the metallic SL(3) character variety. m=1 is the figure-eight (B71); m=2 is silver (new).

## Part 1 — the silver SL(3) character variety has FOUR components (exact)

`Fix(T_2²)` (Sage, `minimal_associated_primes` over ℚ), all components dim 2:

| comp | defining (linear) relations | type |
|---|---|---|
| **0** | `x1=x4, x2=x5` (`tr A=tr A⁻¹`, `tr B=tr B⁻¹`) | **geometric** — same form as the figure-eight's V0 (contains Sym²) |
| 1 | `x1=x4` (+ a cubic) | Dehn-filling-type |
| 2 | `x2=x5` (+ a cubic) | Dehn-filling-type |
| **3** | `x1+x4+1=0, x2+x5+1=0, x3=x5` (`tr A+tr A⁻¹=−1`, `tr B+tr B⁻¹=−1`) | **NEW — no figure-eight analog** |

**Validation (m=1):** `Fix(T_1²)` gives exactly **3** components reproducing B71 — V0 geometric `{x1=x4,x2=x5}`,
W1 `{x1=x4=1}`, W2 `{x2=x5=1}`. So the method is correct, and the silver result (**4** components) is a genuine
structural difference: **the silver bundle's SL(3) character variety is richer than the figure-eight's**, with an
extra `tr+tr⁻¹=−1` component (an order-related / non-cusp component absent at m=1). The geometric component keeps the
`{x1=x4, x2=x5}` form across the family. `[exact — Sage Gröbner decomposition; m=1 validated against B71]`

## Part 2 — the peripheral A-variety relations (DEFERRED; not banked)

The actual A-polynomial *relations* (the silver analog of B71's `M³=L` on the Dehn-filling components, and the
"no tidy form" of the geometric component) require realizing reps on each component and extracting the
meridian/longitude eigenvalues. A quick in-house pipeline (random-slice point sampling on each component + a fresh
realize/monodromy copy + meridian `µ=A⁻²t`) **failed its validation gate**: run on the *figure-eight*, it did **not**
recover the known `M³=L` (it reported "no tidy monomial" on every component — a pipeline artifact). The fault is
isolated: B71's **native** machinery (`peripheral.realize` + `peripheral.meridian` on B71's explicit `W1(p,q)`
parametrization) recovers `M³=L` cleanly (`Mh³/Lh = 1`, spread `7e-10`; `Ms³/Ls = 1`) — so the relation and B71's
code are sound; my **point-sampling/glue** was wrong. Per verify-don't-trust, **none of the Part-2 numbers are banked.**

**The correct next step (recorded, not run here):** derive explicit 2-parameter parametrizations of the four silver
components (from their prime ideals, the silver analogs of B71's `V0/W1/W2(p,q)`), feed them through B71's *native*
`peripheral` pipeline with the silver meridian `µ=A⁻²t` and silver monodromy word, and read the per-component
`Mᵃ Lᵇ` relations. Expected (by analogy with B71 + B199): the Dehn-filling-type components give tidy relations
(`Mᵏ=L` for some silver `k`); the geometric component has **no tidy form** (Falbel-size, the 141-poly analog) —
NEEDS-SPECIALIST, consistent with B199's SL(3)-geometric verdict.

## Firewall
Standalone character-variety / low-dimensional-topology mathematics. No physics; nothing to `CLAIMS.md`; P1–P16
untouched. Extends B71 (figure-eight SL(3)) to the metallic family.

## Reproduction
- `sage-python charvar.sage` — the exact component decomposition: m=1 → 3 components (B71 validation), m=2 → 4
  components (the silver result). *(Sage, not the pyenv test runner.)*
- `tests/test_b201_silver_sl3_charvar.py` (pyenv) — locks the foundation: the B48 `T_m²` construction reproduces
  B71's published `T_1²` at m=1, and B71's geometric V0 is a genuine fixed point with the `{x1=x4,x2=x5}` form.
- `frontier/B71_sl3_apoly/peripheral.py` — the native peripheral pipeline (validated `M³=L`), the basis for the
  deferred Part 2.
