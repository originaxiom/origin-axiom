# B185 — the selection / constraint door: the gluing side selects continuum→discrete, but not to a forced-unique

**Date:** 2026-06-22. **Status:** the fifth hunt of the search specification (`../speculations/S036`) — the
**SELECTION / CONSTRAINT** door: the route to selection-to-*unique* that `B182` flagged as *"a constraint (gluing)
phenomenon, multi-cusp NEEDS-SPECIALIST."* We **computed** how far the constraint side actually goes before the
genuine specialist boundary (per the directive: we calculate; NEEDS-SPECIALIST only at the actual exhaustion).
**Result: a sharpening of `B182`, not a new wall.** The constraint side **genuinely selects** — cusp-gluing collapses
each piece's character-variety *curve* (a continuum) to a **discrete/finite** set (the κ-fork, `B174`/`B131`); this is
the real ">1 building block" selection mechanism, distinct from superposition which *proliferates* (`B182`). **But it
does not deliver a forced-unique value**, and for the metallic *units* the single cusp **caps** all-unit interaction
at **pairs**. **Firewall-side**: emergent character-variety / 3-manifold gluing math (`K010` boundary); no scale/Λ;
**nothing to `../../CLAIMS.md`**; P1–P16 frozen. Ledger V179. Reproducer `constraint_selection.py` (`ALL CHECKS PASS`).

## The diagnostic and the result

The selection-to-unique question reduces to: *when you impose more and more gluing constraints, does the solution
set collapse to a single forced value?* The decisive invariant is the **gluing dimension count**.

- **C1 — the units are 1-cusped → degree-1 nodes.** Every metallic once-punctured-torus bundle (figure-eight `4_1`,
  silver `m003`/`m136`, …) has **exactly one cusp** (SnapPy `num_cusps = 1`). In a cusp-gluing graph a 1-cusp piece
  is a **leaf**: its single cusp can be glued at most once.
- **C2 — all-UNIT interaction caps at PAIRS.** A connected gluing of `k` pieces needs `Σ(degrees) = 2E ≥ 2(k−1)` (a
  tree); but 1-cusp pieces have degree ≤ 1, so `Σ(degrees) ≤ k` ⟹ `2(k−1) ≤ k` ⟹ **`k ≤ 2`**. So the maximal
  connected interaction of metallic *units* is a **pair**, and a glued pair (cusps `1+1`, one gluing) is **closed**
  (`dim = Σcusps − 2E = 0`). To interact `N ≥ 3` units you must insert `≥ 2`-cusp **connectors** — which are *not*
  once-punctured-torus bundles (you leave the unit class).
- **C3 — the constraint side SELECTS continuum → DISCRETE, not to forced-unique.** `dim(`canonical component of the
  glued result`) = Σcusps − 2·gluings = #unglued cusps ≥ 0` (physically realizable gluings never over-determine to
  negative dimension). A **complete (closed)** gluing has `dim 0` → a **finite** set (Bézout = the κ-fork, `B174`) —
  a genuine selection (continuum → discrete). **But** the fork has size `> 1` and **multiplies** under composition
  (it *grows*, `B174`), and its value is a topological invariant of the **freely-chosen** gluing data (which pieces,
  which `GL(2,ℤ)` maps) — *unique-per-choice*, with the choices proliferating. So **selection-to-discrete: yes;
  selection-to-forced-unique: no.**
- **C4 — the verdict + the honest exhaustion.** The constraint side **is** the genuine selection mechanism
  (continuum → discrete κ-fork, `B174`/`B131` — unlike superposition's proliferation, `B182`), but it selects to a
  **discrete-finite** set (count *growing*), not to a forced-*unique* value. The literal `N ≥ 3` all-unit interaction
  is **impossible** (the 1-cusp cap, C2); `N ≥ 3` needs non-unit 2-cusp connectors = a **different object** =
  **NEEDS-SPECIALIST**, now reached as the genuine computational boundary (not a premature defer).

## What this means for the search (S036)

The **SELECTION** ingredient asked for a *unique / specially-structured forced* choice. Across the two channels:
- **superposition (weaving), `B182`:** *proliferates* (gap-label rank `1+N → ∞`) — enrichment, never selection;
- **constraint (gluing), `B185` (this):** genuinely *selects* the continuum down to a **discrete** κ-fork
  (`B174`/`B131`) — the real multi-unit selection — but **not** to a forced-unique value (the fork grows and is
  choice-dependent), and the literal large-N interaction of the 1-cusp units is **capped at pairs** (`N ≥ 3` =
  non-unit connectors = NEEDS-SPECIALIST).

So **selection-to-unique is not delivered by either channel** — superposition proliferates, gluing selects-to-discrete
(growing, choice-dependent) and then hits the multi-cusp wall. This *computes* the boundary `B182` only named, and
keeps the pattern of every reachable door: a genuine structural fact (the constraint side really does select to
discrete — distinct from superposition) **plus** the honest relocation (forced-uniqueness stays out of reach; the
remaining route is the specialist multi-cusp object).

## Scope / honesty
- Establishes the **dimension/cap** structure of the gluing selection (pure graph theory + the standard
  cusp/character-variety dimension count + SnapPy cusp counts), and reuses `B174`'s computed κ-fork behaviour
  (finite, multiplies under composition). It does **not** construct the multi-cusp `N ≥ 3` object — that is the
  genuine NEEDS-SPECIALIST boundary (a different class of 3-manifold).
- "The fork multiplies / is choice-dependent" is `B174`'s result, reused; no new gluing computation beyond the
  dimension count here.
- Emergent character-variety / 3-manifold gluing mathematics (`K010` boundary); no physical-magnitude claim; nothing
  to `../../CLAIMS.md`; P1–P16 untouched.

## Anchors
`../speculations/S036` (the search register — the SELECTION ingredient, both channels), `B182` (the superposition
channel — proliferates; flagged the constraint side as the route to uniqueness, NEEDS-SPECIALIST — sharpened here),
`B174`/`B131`/`K014` (the cusp-gluing κ-fork — continuum → finite, the fork multiplies under composition — the
selection mechanism this counts), `B181`/`B183`/`B184` (the prior hunts — scale/arrow/gauge). External: cusp/torus
gluing of hyperbolic 3-manifolds; the SL(2,ℂ) character-variety canonical-component dimension = number of cusps
(Thurston); Mostow rigidity (closed → isolated discrete rep); A-polynomial / Culler–Shalen (the boundary curve).

## Reproduction
`python frontier/B185_constraint_selection/constraint_selection.py` — C1 the units are 1-cusped (SnapPy, gated);
C2 the all-unit cap at pairs (graph theory); C3 the dimension count (closed → discrete finite fork; not forced-unique);
C4 the verdict + the honest NEEDS-SPECIALIST boundary. Prints `ALL CHECKS PASS`. Fast locks in
`tests/test_b185_constraint_selection.py` (3 tests; SnapPy cusp check `importorskip`-gated).
