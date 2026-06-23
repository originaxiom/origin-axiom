# B191 — the formal 2-cusp connector: the κ-selection nests past the pair-cap

**Date:** 2026-06-23. **Status:** Masterplan III, **Track F** (closes the track; H5-a). B185 showed the 1-cusp
metallic units cap at **pairs**, so an `N≥3` interaction needs a `≥2`-cusp **connector**. **Computed** the formal
connector at the trace-ring level. **Result: the κ-selection NESTS** — a *coupling* 2-cusp connector propagates one
leaf's constraint into a discrete fork on the other, so the selection mechanism extends past the pair-cap to `N≥3`
in principle, staying **discrete-and-proliferating** (not forced-unique); an *uncoupled* connector gives a
continuum. The true geometric metallic 2-cusp 3-manifold is the **NEEDS-SPECIALIST** residual. **Firewall-side:**
emergent character-variety math (`K010` boundary); no scale/Λ; **nothing to `../../CLAIMS.md`**; P1–P16 frozen.
Ledger V187. Reproducer `connector.py` (`ALL CHECKS PASS`).

## The setup

A chain **leaf₁ — connector — leaf₂**. Each leaf is a figure-eight once-punctured-torus bundle with A-poly curve
`q = f(p) = p⁴−5p²+2` (B67) on its boundary torus. The connector has **two** boundary tori; its character variety
**couples** them, modeled by the connector's internal mapping class `φ_c` (`boundary₂ = φ_c(boundary₁)`, the B174
`(p,q,r)` GL(2,ℤ) action). The chain fork = `{boundary₁ on leaf₁'s curve AND φ_c(boundary₁) on leaf₂'s curve}`.

## Results

- **C1 — the dimension count (discrete *iff* the connector couples).** B185: `dim(glued) = Σcusps − 2·gluings`.
  For `leaf(1) — connector(2) — leaf(1)`: `dim = (1+2+1) − 2·2 = 0` ⟹ a **discrete** selection — *provided* the
  connector's character variety genuinely **couples** its two boundaries (a `dim 2 = #cusps` relation). **Uncoupled**
  (independent boundaries): each end is a free curve ⟹ `dim 2` (a continuum², **no** selection). Coupling is what
  makes the selection.
- **C2 — κ NESTS via the connector (control: identity → continuum).** The chain fork is **discrete** for a coupling
  connector (`φ_c = T → 9`, `S → 16`, `ST → 32` — finite, `>1`) and a **continuum** for the **identity** connector
  (no coupling ⟹ leaf₂ lands on leaf₁'s own curve, no constraint). The connector's mapping class is the coupling
  that propagates the κ-constraint from one leaf to the other.
- **C3 — discrete-and-PROLIFERATING, not forced-unique.** The chain fork count **grows** with the connector's
  complexity (`T: 9 < T²: 10`; `S: 16 < ST: 32`) and never collapses to 1 — so κ nests into a discrete-proliferating
  selection, **not** a single forced value (consistent with B185/B190; the over-determination route, not uniqueness).
- **C4 — verdict + NEEDS-SPECIALIST.** The κ-selection mechanism **extends to `N≥3`** via coupling 2-cusp connectors.
  The formal connector = its mapping class `φ_c` (free input). The **true** metallic 2-cusp 3-manifold connector —
  a genuine `dim 2` character-variety 2-cusp hyperbolic manifold with the right boundary coupling — is
  **NEEDS-SPECIALIST** (H5-a).

## What this means for the search (S036)

B182/B185 left "selection past a pair" as the open route to multi-unit structure, capped by the 1-cusp topology.
B191 shows that, **given a coupling connector**, the κ-selection genuinely **nests** to `N≥3` — leaf₁'s constraint
propagates through the connector's mapping class into a discrete fork on leaf₂ — and it stays **discrete and
proliferating** (the fork grows with the connector's complexity), exactly the B185/B190 character (selection-to-
discrete, never forced-unique). So "more units, chained through connectors" gives **ever-richer discrete structure**,
not convergence to a unique value — the consistent verdict of the whole selection thread. What's *not* settled
in-sandbox is whether a **metallic 2-cusp 3-manifold** realizing such a coupling exists geometrically (the genuine
`φ_c`), which is the H5-a specialist question.

## Scope / honesty
- Pure trace-ring computation (sympy resultants), reusing the B174/B190 machinery on the leaf—connector—leaf chain;
  the connector's coupling is modeled by a mapping-class word `φ_c`, the honest abstract stand-in for a 2-cusp
  character variety's boundary relation.
- The identity-connector **control** (→ continuum) is the validation that the discreteness comes from the *coupling*,
  not from the construction (verify-don't-trust).
- The **true geometric** metallic 2-cusp 3-manifold connector (existence, which `φ_c`, dim-2 character variety) is
  **NEEDS-SPECIALIST** — not claimed here.
- Emergent low-dim-topology / character-variety mathematics (`K010` boundary); nothing to `../../CLAIMS.md`.

## Anchors
`B185_constraint_selection` (the 1-cusp pair-cap + the dim count this extends), `B190_iterated_gluing` (the fork
under a mapping-class word — the same machinery, here the connector), `B174_gluing_map_landscape` (the `(p,q,r)`
maps), `B131`/`K014` (the κ-fork), `B164` (the (0,4) cubic — a concrete multi-boundary character variety),
`docs/OPEN_LEADS.md` H5-a. External: cusp/torus gluing of hyperbolic 3-manifolds; the character-variety canonical
component dimension = number of cusps; mapping-class actions on boundary-torus trace coordinates.

## Reproduction
`python frontier/B191_two_cusp_connector/connector.py` — C1 the dim count + the uncoupled continuum; C2 κ nests via
a coupling connector (control: identity → continuum); C3 discrete-and-proliferating; C4 the verdict + the
NEEDS-SPECIALIST residual. Prints `ALL CHECKS PASS`. Fast locks in `tests/test_b191_two_cusp_connector.py` (2 tests).
