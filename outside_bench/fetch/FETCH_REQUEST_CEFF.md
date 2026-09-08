# FETCH REQUEST — the `c_eff` literature, and one more knot's `F_K`

**Filed 2026-09-08 by the outside bench (lane 1B), for memo 177.**
This container's egress proxy blocks `arxiv.org`, `researchgate.net` and
`api.semanticscholar.org`. Everything below was located **by title through web search only** and
has **not been read**. The owner has previously offered to download what the bench cannot.

## A. Blocking memo 177's novelty claim — must be read before §§3–6 are described as new

| # | reference | why |
|---|---|---|
| A1 | **S. Gukov, M. Jagadale, "`c_eff` for 3d `N=2` theories", arXiv:2308.05360** (Aug 2023) | Introduces `c_eff` for `T[M₃]` and the relation `a_n ~ exp(2π√(c_eff n/6))` — the definition memos 174–177 use throughout. Need: the definition as stated, and any bound on `c_eff`. |
| A2 | **S. Harichurn, M. Jagadale, D. Noshchenko, D. Passaro, "`c_eff` from Surgery and Modularity", arXiv:2508.10087** (DIAS-STP-25-20, Aug 2025, 50 pp., 7 tables, 10 figures) | **Same subject as memo 177 §§3–5.** Need: any formula for `c_eff` in terms of the surgery coefficient; any upper bound on `c_eff`; anything about `4₁`; any range of applicability. If it contains the Legendre law or the ceiling `sup c_eff = 1`, memo 177 must be rewritten as a reproduction. |
| A3 | "`c_eff` from resurgence at the Stokes line", **JHEP 02 (2026) 075** (Springer) | Third paper on the same quantity; need its relation to A2. |
| A4 | The paper carrying the figure *"The conformal window for 3d `N=2` theories `T[M₃]`, where `M₃ = S³_p(4₁)` is the integral `p`-surgery on the figure-8 knot"* — ResearchGate figure id `fig7_303521255`, so publication **303521255** (mid-2016, Gukov et al.) | A **conformal window in `p` for surgeries on the figure-eight** is exactly the shape of memo 177 §4's threshold `\|p/r\| < 4`. Need: what the window is, and in what variable. |

## B. The priced open computation — one more hyperbolic knot's `F_K`

Memo 177 addendum 2 names the single highest-value next computation: **is `c_edge = 1` for every
knot whose blocks widen?** If yes, the ceiling `c_eff < 1` is universal and closes
`c((E₆)₁) = 6` on this route for *all* knots, not just `4₁`. It needs `F_K` for one more
hyperbolic knot.

| # | reference | why |
|---|---|---|
| B1 | **S. Park, "Large color `R`-matrix for knot complements and strange identities", arXiv:2004.02087** | Reported to compute `F_K(x,q)` for a large class of knots including **`5₂` and all twist knots** — exactly what is needed. Need: the explicit `F_{5₂}(x,q)` coefficients, or the `R`-matrix recipe in enough detail to run it. |
| B2 | S. Park, "Inverted state sums, inverted Habiro series, and indefinite theta functions", arXiv:2106.03942 | Alternative route to the same series. |
| B3 | S. Park, "Higher rank `Ẑ` and `F_K`", arXiv:1909.13002 | Context. |
| B4 | "Branches, quivers, and ideals for knot complements", arXiv:2110.13768 | Quiver form of `F_K`; may give `Ξ_k` directly. |
| B5 | "3d Modularity Revisited", arXiv:2403.14920 | Bears on the `false ↔ mock` orientation pairing that memo 173 got wrong and memo 177 §1 now uses. |

## C. What the bench would do with each, stated so the ask is falsifiable

* **A2 arrives and contains the law** → memo 177 §§3–5 are rewritten as an independent
  reproduction, with credit, and the contribution narrows to the 39 525-coefficient series and
  the exact `c = −1/16`.
* **A2 arrives and does not** → the novelty fence on memo 177 comes off, with A2 cited for
  what it does cover.
* **A2 contradicts the ceiling** → memo 177 §5 is retracted and the disagreement is localised
  to a specific slope, where the bench's series is exact and can settle it.
* **B1 arrives** → run `xi_recursion.py`'s ansatz against `F_{5₂}`, read off its block widths
  (giving its `c`, hence its threshold) and its edge sequence (giving its `c_edge`). Two
  outcomes, both publishable-shaped: `c_edge = 1` again, or not.

## D. What is NOT being asked for

Nothing behind a paywall beyond A3, and nothing that requires an institutional login. All of
A1, A2, A4, B1–B5 are open arXiv preprints; only the egress proxy is in the way.
