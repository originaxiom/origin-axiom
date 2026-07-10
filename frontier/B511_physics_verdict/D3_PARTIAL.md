# B511/D3 — THE MEASURE DOOR: partial data (D3.1 + D3.2 run 2026-07-11; verdict is Session-2)
**NOT a verdict — D3.3 (typical-history field statistics) and D3.4 (anchor translation) remain.
Recorded honestly to avoid an end-of-context rush.**

## D3.1 stationary measure (M10/D10/F80, 2 seeds × 2 sizes) — reproducer `d3_measure.py`
κ-percentiles [5,25,50,75,95] concentrate at **κ=2** (classical floor): median 2.0 at every seed/size;
only the bottom ~5% sits below 2. With any decimation present (a strict contractor, E[log mult_D]=−2),
the stationary measure lives on the classical leaf. **Reading:** classicalization confirmed as a
stationary-measure statement — the B506/B507 content, restated; nothing beyond it. NOTE: the β-zero at
κ*=0 (B507) is the *M-only slow-flow* attractor; it is NOT the concentration point of a D-inclusive
mix (D overrides toward κ=2). The gate as pre-worded conflated the two flows — corrected here: κ=2 for
D-inclusive, κ=0 attractor only for pure-M.

## D3.2 arcsine test (F80/M20) — CORRECTED interpretation
Occupation-fraction histogram of positive-S time: `[996,351,113,28,10,2,0,0,0,0]` — **one-sided**
(monotone decreasing from bin 0), NOT the U-shaped arcsine. (The script's auto-line "U-SHAPED" is a
BUG: it summed bin[0]+bin[9] but bin[9]=0, so there is no high-end peak.) **Correct reading:** the walk
spends almost all time with S<0 ⇒ **negative drift dominates** ⇒ this **re-confirms B506's negative
stationary drift**, and shows the pure-arcsine (driftless) regime is NOT reached at F80/M20 — driftless
occupation would require exactly-Haar criticality. Nothing beyond B506.

## D3 trend (not the verdict)
Both cells re-confirm already-banked B506/B507 content; no new structure. Expected terminal:
**CLOSED** — pending D3.3/D3.4 in Session 2 (does the MEASURE select fields differently from the
uniform-word census? + the λ-variable consistency lock). Only D3.3 could still surprise.
