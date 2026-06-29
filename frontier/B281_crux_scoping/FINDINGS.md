# B281 — scoping the CRUX: `input-E₆ = output-E₆`

**Status: banked scoping (frontier). FIREWALLED. Nothing to `CLAIMS.md`.** The CRUX is the single load-bearing
conjecture of the E₆ bridge (B278): everything physical hangs on it. This document scopes it — states it precisely,
decomposes it, runs the computable probes, and gives an honest verdict on what is settleable in-sandbox.

## The CRUX, precisely — two different E₆'s
- **INPUT E₆** — the 3d-3d / class-S **type** `G` one chooses for `T[4₁; G]` (the 6d (2,0) theory compactified on
  4₁). Its geometric data is the `G(ℂ)`-**character variety** of `π₁(4₁)` (the flat `G`-connections, B264–B275).
- **OUTPUT E₆** — the **McKay** E₆ from the arithmetic reduction `π₁(4₁) ↠ SL(2,𝔽₃) = 2T`, `McKay(2T) =` affine E₆
  (B266). A **finite-quotient** fact.

The CRUX asks: *is the input type forced to equal the arithmetic output, i.e. is there a reason `G = E₆`?*

## The four-level decomposition (each tagged by where it settles)

| level | question | answer | where |
|---|---|---|---|
| combinatorial | do the two E₆'s share Lie data? | **YES, but tautological** | in-sandbox (B267); both *are* E₆ so agreement is automatic (B272) — not evidence |
| **geometric** | does 4₁'s character variety distinguish E₆? | **NO** | **in-sandbox, SETTLED** (below) |
| arithmetic | is E₆ selected? | **YES — output only** | in-sandbox (B266): a finite-quotient mechanism, independent of the 3d-3d input |
| physics forcing | does 3d-3d force input = output? | **UNSETTLED** | **not in-sandbox** — the specialist/tool gate |

### The geometric level — settled in-sandbox (the decisive scoping result)
Using B264's `dim H¹(Sym^{2k}) = 1 ∀k`: for the principal `sl(2)→g`, `Ad = ⊕_{m∈exp(g)} Sym^{2m}`, so
`dim H¹(Ad ρ_prin) = #exp(g) = rank(g)`. Verified (`crux_geom_probe.py`) for **A₂, G₂, A₃, B₂, F₄, A₄, D₄, E₆, E₇ —
every type gives dim H¹ = rank.** This is the Falbel–Guilloux bound (R6) realized concretely.

**Consequence:** the figure-eight carries a rank-dimensional family of flat connections for **every** Lie type
equally. **E₆ is not geometrically distinguished at all.** The 3d-3d input type is **geometrically free** — there is
no character-variety mechanism that would make the input E₆. (Even "2T appears in the mod-3 reduction" is generic:
the principal `SU(2) ⊃ 2T` sits in *every* `G`.)

### The finer check — irreducibility, not just dimension (`density_probe.py`)
`dim H¹ = rank` is *coarse*. The physically relevant invariant is **irreducibility**: does 4₁ have genuinely
`G`-Zariski-dense (irreducible) flat connections, or do the principal deformations stay trapped in a subalgebra? If
E₆ were the *only* type with dense flat connections, the character variety **would** distinguish it. Computed (B265's
density method, generalized): for the principal `sl(2)→g`, `dim⟨principal sl(2), v_m⟩` per exponent `m` —
> **A₂**: exp 2 → 8 (dense) · **G₂**: exp 5 → 14 (dense) · **A₃**: exp 2 → 15 · **D₄**: exp 3 → 28 · **F₄**: exps
> {5,7,11} → 52 (*fully* dense) · **E₆**: exps {4,8} → 78, {5,7,11} → 52 (trapped in F₄).

**Every type has a dense direction.** So the figure-eight has genuinely `G`-irreducible flat connections for **every**
`G` — E₆ is not distinguished even at the irreducibility level. (Aside: E₆'s trapped exponents {5,7,11} are exactly
the F₄ exponents — the `F₄⊂E₆` symmetric pair / the τ-fixed subalgebra, B271 — a nice consistency, not a
distinction.) **The geometric-level conclusion holds two invariant-levels deep.**

## What would make the CRUX TRUE — and why it's not in-sandbox
The only candidate forcing principle: **impose `G = McKay(arithmetic reduction)`** — E₆ is the *unique* type whose
McKay finite-subgroup graph equals the figure-eight's arithmetic quotient `2T`. This is a genuine selection *rule one
could impose*, but the standard 3d-3d correspondence does **not** impose it (`G` is a free 6d input). Confirming it
as a *physical* principle is exactly the **R6 "arithmetic-selection overlay" novel kernel** (NEEDS-SPECIALIST) — so
**the CRUX and the novelty gate are the same specialist question.**

Settling CRUX = TRUE the direct way needs **`T[4₁; E₆]`** — the type-E₆ 3d-3d theory — and checking whether its
structure is tied to `2T`. Assessment (to confirm with a specialist): exceptional-type 3d-3d theories have **no
constructive Lagrangian/quiver/state-integral** (the DGG / Andersen–Kashaev octahedron model is `SL(N)`-only);
`T[4₁; E₆]` is not computable in-sandbox and arguably not known constructively in the literature. **Tool-gated.**

## Verdict
- The CRUX is **computably unforced.** The geometry treats all types equally (settled in-sandbox), so nothing on
  the input/character-variety side prefers E₆. The arithmetic selects E₆ only as a McKay **output** of a finite
  reduction — a different object that does not feed back into the 6d type choice.
- The computable evidence therefore **leans against** the CRUX (the input is free, not forced to equal the output)
  in the *standard* framework. The only TRUE-route is the candidate forcing principle, which **is** the already-known
  specialist gate; the direct `T[4₁; E₆]` route is tool-gated and not in-sandbox.
- **Net:** the CRUX is downgraded from "open conjecture, the whole bridge hangs here" to "**computably unforced;
  the burden is a forcing mechanism, and the geometry is positive evidence against one.**" This *strengthens* the
  structural theorem: even the E₆ "selection" is an arithmetic-output coincidence, not a forced physical input —
  the object supplies structure, not the selection of a dynamical type.

## Where a real "miss" could still hide (the honest residual)
The geometric level is now closed at **two** invariant-levels (dimension *and* irreducibility) — E₆ is provably not
distinguished there. The one place a genuine forcing could still live is the **physics-forcing level**: a real
`T[4₁; E₆]` computation could, in principle, reveal that the type-E₆ 3d-3d theory has structure tied to `2T` that
the character variety alone doesn't see. I **cannot rule this out in-sandbox** (exceptional 3d-3d is tool-gated). So
the honest statement is *"unforced by everything computable here,"* **not** *"provably false."* That residual is
exactly — and only — the specialist gate; it is not a computation I can do.

## Recommendation
Do **not** spend in-sandbox cycles attempting `T[4₁; E₆]` (tool-gated, not constructively known). The CRUX is now a
**single, sharp specialist question** — *"is `G = McKay(reduction mod the ramified prime)` a physical forcing
principle for 3d-3d, or a numerological coincidence?"* — identical to the R6 arithmetic-selection-overlay gate. Fold
it into the specialist-outreach packet; consolidate the structural theorem as the deliverable.

## Files
`crux_geom_probe.py` (sage; every-type-rank table) · `crux_verdict.py` (pyenv) · `tests/test_b281_crux_scoping.py`.
