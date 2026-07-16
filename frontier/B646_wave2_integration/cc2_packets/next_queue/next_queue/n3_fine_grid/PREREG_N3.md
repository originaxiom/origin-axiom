# N3 — ONE ORGAN OR TWO (sealed prereg; cc2, 2026-07-16)

**The question (R3's residual-hint, banked):** the v11 "middle-organ" box_dim(κ) statistic
(metallic_word golden m=1, periodic diagonalization, B186-exact `box_dim`) has a plateau on
κ∈[0.8,1.5] at depth 14, top κ*=1.1, adjacent to the MST-gap/diam fragmentation maximum at
κ=1.2 (MECHANISM-CANDIDATE, banked). R3's own 0.1-step grid found TWO local maxima inside the
plateau — κ=1.1 (top) and κ=1.4 (second) — "2 steps apart" (R3's own words), gap_top2=0.0055,
smaller than R3's own baseline_std (0.0229). Is this ONE broad peak with sub-baseline wiggle,
or TWO genuinely resolved peaks? This cell answers at 2× the resolution (step 0.05) with a
same-point repeat-measurement jitter estimate (not R3/V11b's cross-point baseline_std proxy).

## Machinery reused (byte-identical copy, diffed against source, zero edits)
`lib_banked.py` copied from `veins/v11_kappa/lib_banked.py` (confirmed identical via `diff`).
Statistic: `box_dim(spectrum(metallic_word(depth,1), λ, periodic=True))`, λ=i·μ, μ=√(2−κ)
(κ<2 branch throughout this grid). Depth 14 word: `metallic_word(14,1)`, L=987. Depth 15:
`metallic_word(15,1)`, L=1597.

## The jitter problem (why this cell adds one new, additive piece of machinery)
`box_dim`/`spectrum`/`metallic_word` are **fully deterministic** — no `np.random` appears
anywhere in `lib_banked.py`. R3/V11b's "noise scale" (`baseline_std`) is the spread of the
statistic **across different κ grid points**, a cross-point proxy, not a same-point repeat
measurement. The task requires the latter (≥5 seeded replicates per point, jitter σ per
point). Since the core statistic has no intrinsic randomness, this cell adds ONE new,
additive, non-invasive function — **not a modification of `lib_banked.py`** — that estimates
the sampling jitter intrinsic to `box_dim`'s box-counting step via random grid-origin offsets
(a standard technique in box-counting-dimension estimation: the count of occupied boxes at a
fixed scale depends on where the grid lines fall; averaging/spreading over random origins is
the textbook way to quantify that placement sensitivity). Definition:

```python
def box_dim_offset(ev, rng, scales=2.0 ** np.arange(-2, -8, -1)):
    P = np.c_[ev.real, ev.imag]
    rng_range = np.ptp(P, axis=0); rng_range[rng_range == 0] = 1
    P = (P - P.min(0)) / rng_range              # IDENTICAL normalization to lib_banked.box_dim
    Ns = []
    for s in scales:
        ox, oy = rng.uniform(0, s), rng.uniform(0, s)   # independent per-scale origin shift
        Px, Py = P[:, 0] + ox, P[:, 1] + oy             # NO wraparound (bounded planar set,
        cells = set(zip(np.floor(Px/s).astype(int).tolist(),  # not a torus -- wraparound would
                         np.floor(Py/s).astype(int).tolist())) # glue far-apart points)
        Ns.append(len(cells))
    return float(np.polyfit(np.log(1/scales), np.log(np.array(Ns, float)), 1)[0])
```

Validated (design-calibration only, on κ=1.9 and κ=0.0 — both OUTSIDE this cell's target grid,
already banked/used elsewhere, so no target grid point was touched before sealing this
prereg): at all-zero offsets this reduces to `L.box_dim(ev)` bit-for-bit (`|diff|=0` exactly,
confirmed both points). Across 10 seeded replicates, σ≈0.012–0.017 at those two reference
points — comparable order of magnitude to R3's baseline_std (0.0229) / V11b's (0.0200), i.e a
sane, non-degenerate noise scale (neither trivially small nor swamping). A small systematic
downward bias vs the zero-offset value was observed (~0.01–0.03, expected direction for
randomly-placed vs corner-anchored counting grids) — for this reason **the reported point
estimate for every κ stays the deterministic zero-offset `L.box_dim` value** (banked
convention, continuous with R3/V11b), and the seeded replicates are used **only** to estimate
σ, never to replace the point estimate.

**Seeding (fixed now, not touched by outcomes):** grid point index i=0..15 (κ=0.80+0.05·i),
replicate index r=0..9 (**N_REPLICATES=10**, exceeds the ≥5 floor; cost is negligible — the
expensive step is the one-off `spectrum()` diagonalization per κ, box-counting itself is
~5–10ms regardless of replicate count). `rng = np.random.default_rng(seed=1000*i + r)`.
Depth-15 confirmation points reuse the same function with seeds offset by +100000 (see below).

## Grid and design
**Fine grid:** κ ∈ {0.80, 0.85, 0.90, ..., 1.55} — 16 points, step 0.05, depth 14
(`metallic_word(14,1)`). Per point: 1 deterministic `L.box_dim` point estimate + 10 seeded
`box_dim_offset` replicates → per-point sample std s_i (ddof=1).

**Pooled jitter σ:** σ_pool = sqrt( mean_i( s_i² ) ) over the 16 grid points (standard pooled
std, equal group sizes).

**Local maximum (index i, 0-indexed over the 16-point grid):** v_i ≥ both existing grid
neighbors (boundary points compared to their single neighbor only), with strict `>` on at
least one side (ties on both sides = not flagged). Contiguous runs of flagged indices merge
into one PEAK REGION, represented by its highest point (ties broken toward the lower-κ index).

**"Separated by ≥2 grid points"** is read as **index-gap ≥ 2** between two peak regions' 
representative indices (i.e., at least one grid point strictly between them, available to serve
as "the intervening minimum"). Justification: R3's own banked language calls κ=1.2 vs κ=1.4
(index-gap 2 on the 0.1-step grid) "2 steps apart" — i.e. this project's own convention counts
index-gap, not point-count-between. On this fine (0.05-step) grid, index-gap 2 = κ-gap 0.10,
which not coincidentally equals the OLD coarse grid's own step — a scale-consistent translation
of the same rule, not an arbitrary choice.

## THE DECISION CRITERION (verbatim; mechanical; applies to the 16 deterministic point
estimates v_0..v_15 and σ_pool as defined above)

> **TWO-ORGANS** iff there exist two local-maxima peak regions, index-gap ≥ 2, such that BOTH
> (v_peakA − intervening_min) > 2·σ_pool AND (v_peakB − intervening_min) > 2·σ_pool, where
> intervening_min = min(v_j) over grid points j strictly between the two regions.
> **ONE-ORGAN** iff exactly one peak region exists on the grid (mechanically unimodal).
> **UNRESOLVED** iff ≥2 peak regions exist but no index-gap-≥2 pair clears the 2·σ_pool bar on
> both sides.

If multiple qualifying TWO-ORGANS pairs exist, the canonical pair for depth-15 confirmation is
the one with the largest combined margin (sum of both sides' excess over 2σ_pool); ties broken
toward the higher-value region, then toward lower κ. "The valley" = the intervening index with
the lowest v_j (ties broken toward the index closest to the pair's midpoint, then lower κ).

## Depth-15 confirmation (sealed now; asymmetric by design — depth 15 can only CONFIRM or
## DOWNGRADE the depth-14 verdict toward UNRESOLVED, never upgrade it)
Re-run `metallic_word(15,1)` (L=1597): deterministic point estimate + 10 seeded
`box_dim_offset` replicates (seeds 100000+1000·k+r, k enumerating the confirmation points in
the fixed order below, r=0..9) at:
  - **if depth-14 verdict = TWO-ORGANS:** {peakA, valley, peakB} (the canonical triple above).
    SURVIVES iff, using σ_pool **from depth 14** (kept fixed as the yardstick — it is the
    better-conditioned 16-point estimate; a depth-15-only pool would rest on n=3 points):
    v15(peakA) − v15(valley) > 2·σ_pool_d14 AND v15(peakB) − v15(valley) > 2·σ_pool_d14.
    Else → final verdict downgrades to UNRESOLVED.
  - **if depth-14 verdict = ONE-ORGAN:** {κ*, flank}, where κ* = the peak region's
    representative and flank = the non-peak-region grid point with the LOWEST depth-14 point
    estimate (ties broken toward greater index-distance from κ*). SURVIVES iff
    v15(κ*) − v15(flank) > 2·σ_pool_d14. Else → final verdict downgrades to UNRESOLVED.
    (Honest limitation, stated up front: a 2-point spot-check can confirm the peak's elevation
    persists but cannot itself re-verify unimodality shape — exactly the same limitation
    R3/V11b's own depth-15 spot-checks had.)
  - **if depth-14 verdict = UNRESOLVED:** run the TWO-ORGANS-style triple anyway (two
    globally-highest peak regions + intervening valley) for transparency, but the reported
    FINAL verdict stays UNRESOLVED regardless of what depth 15 shows (locked rule: depth 15
    never upgrades).

## Anchor gate (HARD STOP, run BEFORE this grid — reproduce, do not rebuild)
(1) κ=1.0, depth13 golden `box_dim` vs `veins/v11_kappa/grid_results.json` (banked
    0.9806266343819846). (2) κ=1.0, depth14 vs `veins/v11_kappa/depth14_results.json` (banked
    1.0747651555463955). (3) κ=1.1, depth14 vs `residuals_loop/r3_peak/r3_results.json` (banked
    1.0804255006420715) — this point sits inside our own target grid, so its banked
    reproduction is the most on-point trust check available. All three gated at
    `|diff| < 1e-9`. (4) Self-consistency (not a "banked" reproduction, but foundational to
    trusting every σ in this cell): `box_dim_offset(ev, rng)` forced to zero offsets must equal
    `L.box_dim(ev)` on the same eigenvalue set, exactly. Any of (1)-(4) failing is a HARD STOP —
    no grid point below gets computed or trusted.

## Budget discipline
Per-point depth14 cost ≈ one `spectrum()` diagonalization (L=987, ~7–10s per R3's own logged
times) + negligible jitter overhead; depth15 spot points ≈16–23s each per R3's logged times.
Total estimated wall-clock for the full design ≈ 4–6 minutes — comfortably under the ~10
min/point ceiling. Fallback (stated per task instructions, not expected to trigger): if any
single depth-14 grid point exceeds ~10 minutes, drop replicates to 3 for the remaining points
and state so plainly in FINDINGS.

## What this cell does NOT do
Re-run R3's mechanism comparisons (gamma / MST-gap / liftoff) — out of scope; R3 already
sealed MECHANISM-CANDIDATE on that question. This cell answers ONLY the peak-shape question.
