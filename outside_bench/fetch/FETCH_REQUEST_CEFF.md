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

> ### **[B AND B' ARE CLOSED IN-SANDBOX, 2026-09-08. DO NOT SPEND ANYONE'S TIME ON THEM.]**
>
> **B is closed.** `F_{m(5₂)}` was computed here, from B1's own method rather than from its
> printed formulas — Park's large color `R`-matrix on the lowest weight Verma module, eq (17),
> (18), (25)–(26), (31), on his braid `σ₂^{−3}σ₁^{−1}σ₂σ₁^{−1}`. It reproduces every block he
> prints. **Memo 183 addendum 1**, `certificates/park_large_color.py`.
>
> **B' is closed for `5₂`.** `Φ_{m(5₂)} = Σ_{k≥0}(−1)^k q^{k(k+1)/2}` — a **false theta**, not
> `(q;q)_∞`, so the ceiling is knot-specific as a measurement rather than as an argument, and
> `c_eff(1/Φ) = ∞`. **Memo 184**, `certificates/tail_52.py`. B'1–B'3 would still be *useful*
> (which tails are achievable across families) but they are no longer blocking anything.
>
> **B'4 (connected sums) is untouched and still open**, and is now *less* interesting: memo 184
> §3 OUTCOME A would reach `c_eff = 6` on a single hyperbolic knot without any connected sum.
>
> **THE ASK THAT REPLACES THEM — see §B''.**

## B''. THE ONE THING NOW BLOCKING (added 2026-09-08, memos 183–184)

Memo 183: **the quantum A-polynomial printed in Park eq (32), p.17, does not annihilate
`F⁺_{m(5₂)}`** — `[Â F⁺]_{x^{7/2}} = q^{13} f_0(q) ≠ 0`, exact on 23 nonzero coefficients to
`q^{270}`, with `f_0` the paper's own block; and no single monomial repairs it (five candidates,
all refuted at `q^{17}` against `Ẑ(Σ(2,3,11))`). Without it the blocks are reachable only to
tens of `q`-coefficients, where `c_eff` needs thousands — so memo 184 §3's preregistered cell
cannot be decided.

| # | what is needed | why it settles it |
|---|---|---|
| **B''1** | the **arXiv LaTeX source** of arXiv:2004.02087 eq (32) (`arxiv.org` is egress-blocked from this container; two independent extractions of the PDF agree with each other, so this is about the paper, not the OCR) | if the source differs from the typeset page, the erratum dissolves and the recursion runs |
| **B''2** | **Garoufalidis–Koutschan, the non-commutative A-polynomial of the twist knots** — Park cites [GK13] as the source of his eq (32) | the same operator from its origin |
| **B''3** | `f_4^{m(5₂)}(q)` from any independent computation, to **more than ten** coefficients past `q^{−2}` | this bench has 36 converged coefficients of `f_4`; one independent set fixes the repair by the defect method of memo 183 §5 and needs no source at all |

> **[UPDATED 2026-09-08 after memo 183 addendum 4 — `B''3` IS NO LONGER THE BINDING CONSTRAINT.]**
> `f_4` is now in hand to 28 converged coefficients and `f_5` to 11, from Park's own large color
> `R`-matrix. What blocks the repair is not one more coefficient but the **split of each
> correction among the five `a_i`**: `δ_d` determines `U_d(0) = Σ_i c_{i,d} Q^i` exactly but not
> the five `c_{i,d}` separately, and the split is fixed only by `U_d(1) … U_d(4)`, which live in
> `δ_{d+1} … δ_{d+4}`.
>
> ### Closing every `x`-degree up to 12 needs blocks to about `f_16`. This bench has `f_5`.
>
> A sequential single-index fit does **not** substitute: memo 183 addendum 4 shows it absorbs each
> wrong split into the next correction and fails once the degrees run out — at `q^{141}` with every
> degree of `a_1` used, `q^{164}` with `a_0`'s `x^{12}` as well.
>
> **So `B''1` or `B''2` — one document — is now worth more than any amount of further computation
> here.** `B''3` survives only in the much larger form "`f_6 … f_16`", which is a different ask.

> ### **[2026-09-09 — THE ASK IS NOW EXACT, AND IT IS NOT ARXIV.]**
>
> Park's **footnote 12** names where eq (32)'s data came from: *"The data for the quantum
> A-polynomial can be found in [GS10, GK13, NRZS12]."* Two of those citations carry **direct data
> URLs in his own bibliography** — machine-readable files for exactly this object, from the
> primary source he transcribed:
>
> | # | what | where |
> |---|---|---|
> | **B''A** | **[GS10]** Garoufalidis & Sun, *"The non-commutative A-polynomial of twist knots"*, J. Knot Theory Ramifications **19(12):1571–1595, 2010** | `people.mpim-bonn.mpg.de/stavros/publications/twist.knot.data/index.html` |
> | **B''B** | **[GK13]** Garoufalidis & Koutschan, *"Irreducibility of q-difference operators and the knot 7₄"*, Algebr. Geom. Topol. **13(6):3261–3286, 2013** | `people.mpim-bonn.mpg.de/stavros/publications/double.twist.data/index.html` |
> | B''C | fallback only: the LaTeX source of arXiv:2004.02087 | `arxiv.org/e-print/2004.02087` |
>
> **Both hosts, and arxiv.org, are blocked by this container's egress policy** — verified by
> `curl` (HTTP 403 from the proxy) and by `WebFetch` (`EGRESS_BLOCKED`), not assumed.
>
> **WHAT IS NEEDED FROM IT:** the operator `Â` for **`5₂`** — Park's `K_{2,1}`, the twist knot with
> two twists — as the coefficients `a_0 … a_4` of `ŷ^i`, polynomials in `x` and `q`. **Any format**:
> Mathematica, plain text, a PDF page. Nothing else from those pages is wanted.
>
> **HOW TO TELL IT IS THE RIGHT OBJECT, without trusting me:** the printed eq (32) fails a test the
> correct operator must pass. Applied to Park's own `F⁺`, its `x^{7/2}` coefficient is
> `q^{13} f_0(q) ≠ 0` instead of `0`.
> **Just run** `python3 certificates/ahat_ingest.py <the file>` — it accepts labelled lines or a
> Mathematica list, in `M` or `x`, understands `Sqrt[q]` and `q^{11/2}`, divides out any overall
> monomial, and searches seven presentation conventions (`q→1/q`, `x→1/x`, `ŷ`-degree reversal
> and combinations) so a convention mismatch cannot be misread as disagreement. It prints a
> verdict. Its own self-test — run it with no argument — must pass first, and does.
>
> **WHY THIS SETTLES IT EITHER WAY.** If the primary source's operator differs from eq (32), the
> erratum is confirmed and the repair is handed over rather than fitted. If it agrees, then eq (32)
> is faithfully copied and the defect is older and further upstream than Park — which is a
> different and larger finding. **There is no outcome in which this is wasted.**

`δ_4` remains pinned exactly, for anyone checking against it:
`[Â_printed F⁺]_{x^{9/2}} = q^{12} − q^{13} + q^{15} + q^{16} − q^{17} − 3q^{18} + …`



Memo 177 addendum 2 names the single highest-value next computation: **is `c_edge = 1` for every
knot whose blocks widen?** If yes, the ceiling `c_eff < 1` is universal and closes
`c((E₆)₁) = 6` on this route for *all* knots, not just `4₁`. It needs `F_K` for one more
hyperbolic knot.

| # | reference | why |
|---|---|---|
| B1 | **S. Park, "Large color `R`-matrix for knot complements and strange identities", arXiv:2004.02087** | Reported to compute `F_K(x,q)` for a large class of knots including **`5₂` and all twist knots** — exactly what is needed. Need: the explicit `F_{5₂}(x,q)` coefficients, or the `R`-matrix recipe in enough detail to run it. |
| B2 | S. Park, "Inverted state sums, inverted Habiro series, and indefinite theta functions", arXiv:2106.03942 | Alternative route to the same series. **PROMOTED 2026-09-09 (memo 185).** The *naive* cyclotomic route to `f_K` is now closed by exact computation (`certificates/cyclotomic_vs_fk.py`): `C_{4₁}(x,q)` is not a power series, and on `3₁` it is not `f_K` up to any monomial. Park's *inverted* Habiro series is the only surviving route of this kind and this bench does not hold the paper. **Rank: below §B'' (the A-polynomial data), above any colored Jones table.** |
| B3 | S. Park, "Higher rank `Ẑ` and `F_K`", arXiv:1909.13002 | Context. |
| B4 | "Branches, quivers, and ideals for knot complements", arXiv:2110.13768 | Quiver form of `F_K`; may give `Ξ_k` directly. |
| B5 | "3d Modularity Revisited", arXiv:2403.14920 | Bears on the `false ↔ mock` orientation pairing that memo 173 got wrong and memo 177 §1 now uses. |

## B'. SUPERSEDES B (cheaper, added by memo 177 addendum 4)

Addendum 4 identifies the ceiling as `c_edge(K) = c_eff(1/Φ_K)` with `Φ_K` the **colored Jones
tail**, verified for `4₁` (`Φ = (q;q)_∞`, ceiling 1). That turns the priced open computation
from *"get `F_K` for a second hyperbolic knot"* into a **question about tails**, which is a
developed subject.

| # | reference | why |
|---|---|---|
| B'1 | **C. Armond, O. Dasbach, "Rogers–Ramanujan type identities and the head and tail of the colored Jones polynomial"** (arXiv:1106.3948 — it is reference [7] of the GM paper) | The tail of an alternating link is that of its reduced all-`A` graph. Need: which tails are achievable, and whether `(q;q)_∞^m` for `m ≥ 2` occurs. |
| B'2 | S. Garoufalidis, T. Lê, "Nahm sums, stability and the colored Jones polynomial" | The stability theorem itself, and the shape of the stable series. |
| B'3 | M. Hajij, on tails of alternating links / the `q`-series of graphs | Computed tails for families; the fastest way to find a knot with a high-power tail. |
| B'4 | **Whether `F_K` is multiplicative under connected sum** — i.e. does `F_{K₁#K₂}` have block edge `1/(Φ_{K₁}Φ_{K₂})`? | This is the whole of addendum 4 §3's preregistered cell. The colored Jones side is free; only the `F_K` side is unknown here. A one-line answer from anyone who works with `F_K` settles it. |

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
* **B'4 answered yes** → six connected copies of `4₁` give `c_edge = 6`, the ceiling is
  unbounded over knots, and memo 177's bound is confirmed as `4₁`-specific.
* **B'4 answered no** → addendum 4 §3's route is dead and the cell closes on OUTCOME B.

## D. What is NOT being asked for

Nothing behind a paywall beyond A3, and nothing that requires an institutional login. All of
A1, A2, A4, B1–B5 are open arXiv preprints; only the egress proxy is in the way.


---

## B''' — WHAT THE COLORED JONES TABLES ARE AND ARE NOT FOR (added 2026-09-09, memo 185)

`people.mpim-bonn.mpg.de/stavros/publications/twist.knot.data/CJTwist.<p>.txt.gz`, `p = −14…15`,
holds `J_{K_p,n}(q)` for `n = 1…60` of the twist knots, normalised `J_{p,1} = 1`, with
`K_0 = U`, `K_{−1} = 4₁`, `K_1 = 3₁`, `K_{−2} = 6₁`, `K_2 = 5₂`, `K_{−3} = 8₁`, `K_3 = 7₂`.

**They will NOT unblock `f₆` and beyond.** Memo 185 closes the route that would have made them
do so. Do not prioritise them for that reason.

**They are worth having for exactly three reasons.**

1. Memo 184's stability fence goes from **7** stabilised coefficients to **~60**.
2. `K_{−1}` and `K_1` are **free controls**: check them against GM eq (166) and GM eq (24)
   (`certificates/cyclotomic_vs_fk.py` implements both and they pass) **before** claiming
   anything from any other file in the set.
3. Memo 184 addendum 1's family goes from **4 knots to 30**.

Priority subset if size is a problem: `p = 2, −1, 1, −2, 3, −3` (`5₂, 4₁, 3₁, 6₁, 7₂, 8₁`).

**The files that decide the erratum are the operator files on the same page, not these.**
See §B''.
