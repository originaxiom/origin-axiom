# B1967 — The trade-off is not in the coupling's form: with tuned channels a nearly null Higgs gives an aligned mixing and a heavy-pair hierarchy under the charge rule

**Verdict: PROVED** (an explicit example, recomputed at 50 digits). Main, 2026-11-19. Data-free. Register rows P-879
and P-847. **0 of 19.**

## Seen first

- **The sweep of B1965 and B1966 covers this question**, in the record's own words (nearly null, non-null Higgs,
  reality, V_ud, dichotomy, Standard Model's reading).
- **What it bears on:**
  - **B1966** proves the trade-off's two ends exact for every channel. At reality 0 the two readings' light states
    are orthogonal; at reality 1 the floor m₂/m₃ ≥ 1/3 of B1727 holds.
  - **B1965** searched frame C's own channels at four points and found alignment only at reality near 1.
  - **P-879** conjectured the interior for frame C's channels.
  - **B1742's third regime** is two nearly null directions read S in every sector: hierarchy and alignment, mixing too
    small. It is not under the charge rule; this example is.
- **The literature:** none bears on this coupling.

## What was run

- **The search (`verification/free_channels.py`, `free_channels_small.py`).**
  - The coupling is B1736's form, Y(h; u, w) = u hᵀ + h uᵀ − (u·h)·1 + w[h]_×, under the charge rule: the up sector
    takes h̄ with its channels (u_u, w_u), the down sector h with (u_d, w_d).
  - Both sectors' channels are free in ℂ⁴, and the Higgs h = (cos t, i sin t, 0) has reality r = |h·h| = cos 2t.
  - Nelder–Mead from 40 starts per r looks for an aligned mixing (smallest diagonal ≥ 0.9) with both m₂/m₃ in
    [1e-6, 1e-2] and both m₁/m₂ ≤ 0.5, so three distinct nonzero masses.
  - **Disclosed:** the first form of the objective let a nearly degenerate coupling score below −2 without alignment.
    The run with it was stopped. The objective was corrected to penalise m₂/m₃ < 1e-6 and m₁/m₂ > 0.5 before the kept
    runs.
- **The example (`find_counterexample.py`, `counterexample_channels.json`)** at r = 0.003, recomputed at 50 digits
  by `verify_counterexample.py`.

## The results

**The least m₂/m₃ compatible with alignment 0.9, with free channels:**

| r | 0 | 0.003 | 0.01 | 0.03 | 0.1 | 0.3 | 0.5 | 0.7 to 1 |
|---|---|---|---|---|---|---|---|---|
| least max m₂/m₃ | alignment impossible (B1966) | 4.6e-3 | 1.2e-2 | 1.8e-2 | 0.06 | 0.18 | 0.31 | about 0.40 |

**The example at r = 0.003, at 50 digits:**

| sector | singular values | m₁/m₂ | m₂/m₃ |
|---|---|---|---|
| up (h̄) | 0.002929, 0.005859, 1.2666 | 0.500 | 4.63e-3 |
| down (h) | 0.001240, 0.005964, 3.4592 | 0.208 | 1.72e-3 |

The mixing's diagonal is |V| = (0.967, 0.901, 0.915).

## What it means

- **The trade-off of B1965 is not a property of the coupling's form.**
  - Exactly at reality 0 alignment is impossible (B1966).
  - Just off it, tuned channels rotate both light states into alignment: the rotation grows like r·|u|/m₂, so a small
    m₂ allows it.
  - So "for every channel" fails in the interior.
- **Any exclusion of the mixing in frame C must use the channels the frame produces.** They are fixed by the matter
  charges, the point and the end norms, not chosen. B1965's four points did not reach the tuned region. P-879 is
  restated: whether frame C's channels ever reach it.
- **The light pair is only mildly split in the example** (m₁/m₂ 0.2 to 0.5). The example shows the trade-off is not a
  theorem of the form. It is not a candidate for the masses, and nothing is compared with data.

## Files

`verification/free_channels.py`, `free_channels_small.py`, `find_counterexample.py` and `verify_counterexample.py`,
each with its run file, and `counterexample_channels.json`. The lock is `verification/test_b1967_counterexample.py`.

0 of 19.
