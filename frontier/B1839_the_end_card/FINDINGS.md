# B1839 THE END CARD — findings

*Sealed c70b356f0 (PREREGISTRATION sha8 dc05a5c4) before its census or look ran. Census run once on the seal (26 060 s,
exit 0; outputs committed at 329873b23). The web seat's third opinion of the census (2ea0a65be) agrees to 2.0 × 10⁻¹⁴ at
its levels. Look run once on the seal (15 713 s, exit 0, empty stderr). Its output was committed unread at 1d218f158 and
read after the push. Read together with B1841's verdict, as B1841's PRE_RUN_NOTE fixed before either look was read. One
look on the six (LOOK_LEDGER). 0 of 19.*

## The cells, as sealed

| cell | result |
|---|---|
| VOID | not void: 1 364 314 rows (223 apexes × 266 lines × 23 ends), every row's features finite; the data's minima finite |
| C0 | HOLDS: the web seat's sealed E2 rows A–D reproduced through this card's path (30.664372, 39.148931, 53.700282, 40.830656), max rel dev 8.2 × 10⁻¹² |
| C1 | HOLDS (the class cache against `twisted_norms()`; per-sector maximum 7.9 × 10⁻¹⁵ up, 1.4 × 10⁻¹⁴ down, 3.5 × 10⁻¹⁴ lepton) |
| C2 | HOLDS (the split quadrature against the instrument, δ = 6 and 10 included) |
| C3 | HOLDS: B1798's small-cut census through this card's null reproduces the referee's hits exactly (bounded 82 of 40 000, seat 11) |
| P1 | HOLDS: least χ²_six 4.613885 with c continuous (the nine c: 5.372228; {1, 3}: 11.360492) < 16.75 |
| **D** | **FAILS: 24 252 of 10⁶ random hierarchies as low under the fully matched null (apex, line, reading, c and the level δ re-made per target over the same rows); r97.5 = 2.4555 × 10⁻² > 0.01** |

D with the nine c: 2.087 %. With {1, 3}: 2.519 %. All three fail.

## Read-outs (not looks)

- **The data's minimum per level** (c continuous): 14.75 at δ = 0; 7.91, 5.19, **4.61**, 5.00 and 5.91 at δ = 0.05–0.25;
  rising to 18.6 at δ = 1 and 75.7 at δ = 6; 37.0 at δ = 10; 137 597 at the cusp limit.
- **The best row:** apex 162, τ₀ = (½, 2.949576…), line (2/5, 4/5) (order 5), δ = 0.15, reading (S̃, S, S), c = 3.7611.
  Model/measured, in the order (c/t, u/t, s/b, d/b, μ/τ, e/τ): 0.996, 1.247, 0.885, 1.183, 1.059, 1.059.
  - It is **B1841's best row:** the same apex, line and reading. B1841's E4 = L₂ − π/2 lies at δ = 0.125 at this apex,
    0.025 from the free optimum.
- **δ among D's hits:** spread over every level (1 711 at δ = 0 … 2 779 at δ = 10; none at the cusp). The free level's
  look-elsewhere is what costs the screen.
- **Single-level read-outs:**
  - δ = 0 alone: 14.75 (r97.5 2.36 %), the small-cut census's level at the exact norm.
  - The cusp limit alone: 137 597 (85 %).
  - **The five-ality lines alone:** 4.61, r97.5 0.787 %. This is a read-out, not a cell, chosen before the run.

## Reading (as sealed, with B1841's PRE_RUN_NOTE)

**P1 holds and D fails.** A geometric end reaches the six, but with its level free the frame reaches random hierarchies too
often.

B1839's own reading:
- the family's level-1 pass belonged to the ansatz end;
- THE SIX ON THE STRIP, at the small-cut end, stops being a candidate;
- no held-out target is spent for it;
- any later end must be derived, not chosen.

B1841 passes. The joint rule fixed in B1841's PRE_RUN_NOTE therefore governs:
- a principled end carries the six specifically while a free level does not;
- the free level's larger look-elsewhere (23 ends against 4) costs it the screen;
- B1839's fail is recorded as the free-level reading's;
- the candidate is frozen at B1841's row.

The confirmation the joint rule would start from that row **is held by the owner's ruling** (P-709, 2026-11-05, "hold
them"). The reason is B1841's third opinion (P-706): its best row, which is also this card's, is on an order-5 line. There
the lepton ratios equal the down ratios (Y_e ∝ Y_dᵀ), so the lepton half tests nature's Georgi–Jarlskog pattern with c
fitted. The frame's quark four alone are not specific: 9.2 % of random hierarchies at E4, 17.5 % over B1841's four ends.
With 23 levels in place of 4, this card's quark four can only be less specific; no further look was spent to measure it.

**What B1839 settles (P-421):**
- the end is not a free number the six can fit specifically;
- the small-cut ansatz (A07, A09) is retired from the candidate;
- the end, if the six are to rest on one, is B1841's principled entry.


## Seen first

- **The card's own sweep** is its PREREGISTRATION's: `VERDICT topic-sweep /free cut|cut level|scale free|L free|end.{0,12}free|horoball norm|exact end|end card|Higgs twist/`, with B1838, B1798, B1753 and B1741 read.
- **The landing's added sweep** is B1841's third-opinion sweep (`VERDICT topic-sweep /lepton.{0,12}down|Y_e = Y_d|Georgi|Jarlskog|quark four|double ratio|D_frame/ (full text): 56 of 1589 arcs on main match (NEGATIVE 15, OPEN 4, PROVED 37); 41 register rows match (DECLINED 3, DONE 26, QUEUED 12)`). It found B1728's order-5 identity, which bears on this card's best row as on B1841's.
- **The literature:** horoball and collar geometry of the modular cusp, as cited in B1840. The look-elsewhere cost of a free scale is standard (a scan over 23 levels priced in the null); Georgi and Jarlskog (1979) for the lepton factor's meaning on order-5 rows.

## Disclosed

- The look took 15 713 s. Most of it, 15 276 s, went to the cusp-limit read-out's exhaustive pair evaluation (2.3 × 10¹⁰
  pairs). That read-out is not a cell.
- None of the six's held-out neighbours (P-585, P-638) was computed or touched.
