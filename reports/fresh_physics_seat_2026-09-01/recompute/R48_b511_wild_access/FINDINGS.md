# R48 — B511/D3 "wild-register accessibility": the committed script is numerically broken, but its claim reproduces by a well-posed method

**Banked (B511_physics_verdict/D3_FINDINGS.md):** D3.3 "P(κ ≈ 2 classical) ≥ 0.84; P(wild-accessible κ) ≤ 0.10 across
all mixes"; D3.1 "stationary measure concentrates on κ = 2 … median 2.0" with percentiles [≈1.8, 1.99999, 2.0, 2.0, 2.0]
(`d3_results.json`). Scripts `d3_wild_access.py` / `d3_measure.py`: n Haar-random SU(2) pairs (A,B), 3000 steps of
F: (A,B) → (AB, A) (80 %), M: (A,B) → (AB, BA), D: (A,B) → (A², B²) (read off the `np.where` branches), matrices rescaled
by √|det| every 20 steps, κ = x²+y²+z²−xyz−2 from the traces.

**1. The committed scripts do not run to a number here (Phase C agent, then the seat; numpy 2.4.6).** Every history is NaN
by step ≈ 200; both scripts print 0.000 / 0.000. Cause (`r48b_output.txt`, `r48e_output.txt`): the Fibonacci-type
recursion multiplies round-off by Fibonacci numbers (error ~ φ^t), so double-precision matrices leave SU(2) after
≈ 70 steps whatever the renormalisation; √|det| rescaling then overflows. On the numpy the arc used, the same drift
evidently produced huge-but-finite matrices whose collapsed traces give κ = 2.000000000000 identically — the banked
percentiles "2.0, 2.0, 2.0" to 13 digits are that collapse, not a measured distribution. **Those numbers are artifacts.**

**2. The claim itself, done properly.** Only F preserves κ (Nielsen move; 3e−15); M and D change it (`r48e_output.txt`).
On trace coordinates (x,y,z) the three moves are exact polynomial maps — F: (z, x, xz−y); M: (z, z, w); D: (x²−2, y²−2, w)
with w = tr(A²B²) = xyz−x²−y²+2, all verified against matrices to 1e−15 — and the dynamics stays on the compact SU(2)
trace region, so it can be run at any precision (`r48f_mp.py`, 300 histories × 3000 steps):

| mix | dps = 15 (≈ double): escaped / P(classical) / P(wild) | dps = 60: escaped / P(classical) / P(wild) | banked |
|---|---|---|---|
| M10/D10/F80 | 0.317 / 0.893 / 0.024 | **0.000 / 0.927 / 0.040** | ≥ 0.84 / ≤ 0.10 |
| D20/F80 | 0.433 / 0.953 / 0.012 | **0.000 / 0.967 / 0.020** | ≥ 0.84 / ≤ 0.10 |
| M20/F80 | 0.337 / 0.794 / 0.126 | **0.000 / 0.850 / 0.083** | ≥ 0.84 / ≤ 0.10 |
| F100 control | 0 / 0.023 / 0.803, κ conserved to 1.7e−14 | 0 / 0.023 / 0.803, κ conserved to 1.4e−59 | (κ must be conserved) |

At 60 digits no history escapes and the three mixes give P(classical) = 0.93 / 0.97 / 0.85 and P(wild) = 0.04 / 0.02 /
0.08: **D3.3 reproduces in substance** (M20/F80 sits right at the ≥ 0.84 bound). The control confirms the method: with
F only, κ is exactly conserved and the Haar distribution (P(classical) 0.02) is untouched, so the concentration on κ = 2
comes from the M and D events, which is B511's mechanism.

**3. Seat's own errors, recorded.** (a) My first version of this cell read M as (A, BA) and called it κ-preserving; the
committed M is (AB, BA) and changes κ. (b) My first "corrected" run re-projected the matrices onto SU(2) every 20 (then
every) steps and found the measure wild (P(classical) ≈ 0.06); that method is worthless here because the recursion
amplifies the projection error by φ^t (its own F100 control fails to conserve κ, max |Δκ| = 3.8), and I initially
reported it as "reverses the verdict". Retracted. The relay row was corrected the same hour.

**Verdict: REPRODUCES IN SUBSTANCE, SCRIPT BROKEN.** B511 D3.3's sentence stands as a claim about the model; its
committed evidence does not (NaN here; artifact-valued there). `d3_wild_access.py` / `d3_measure.py` should be replaced
by the trace-map formulation (which is also ~100× cheaper), and `d3_results.json`'s "2.0000000000" percentiles should
be re-banked from a run that keeps the pairs on SU(2). Files: `r48.py`, `r48b_collapse.py`, `r48d_tracemap.py`
(first trace-map attempt, wrong M), `r48e_clean.py`, `r48f_mp.py`, outputs `r48*_output.txt`, `r48c_timeseries.txt`.
