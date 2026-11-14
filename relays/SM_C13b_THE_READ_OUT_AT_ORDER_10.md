# SM-C13b — the read-out at order 10: the leptons get rows of their own, set apart from the down rows only by the sign of the doublet's twist

*The SM seat, 2026-11-14, approved by main in M33. Card `relays/cards/SM_C13b_the-read-out-at-order-10.md`, sealed and
pushed at a036eba44 before any run. Main's frame C as B1928 reads it, imported unchanged from main at 847031d5f.
**Only differences are written**: lepton outputs minus down outputs. No output is printed or saved, and nothing is set
beside a measured number.*

## The answer

- **The read-out at order 10 = 5 × 2 gives the leptons rows of their own, and the separation survives the read-out on
  the whole.**
  - Integrated over the geodesic flow by B1928's own route (the same 3 000 words), the lepton-minus-down difference is
    non-zero on all 16 outputs: 2 ratios, 2 readings and 2 ends, at each of the 2 end conventions.
  - The difference stands 17 to 1 332 jackknife errors from zero (K5).
- **Exactly what separates them** (D2 and K3). At order 10, the averaged lepton rows are the down rows with the
  doublet's twist negated: F̄₁₀^lep equals the average of the down step with charges (−1, 2), to 10⁻¹³.
  - The lepton pair's unit multiples mod 10 meet neither the down pair's nor their transposes.
  - At order 5 the same algebra is the transposition, and the copy is exact (K1, K6).
  - So the bit that the order-5 read-out lacks is the sign of the doublet's twist. That is the parity of 6Y, which the
    tick reads (SM-C13).
- **This agrees with main's B1935:** orders above 7 identify no two sectors, and at the read-out's order 10 none
  coincide.
- **Not claimed:** that the read-out should be taken at order 10 (P-845 is main's question), or that the separated rows
  are right. Nothing is compared with anything measured.

## The results against the sealed expectations

| | expectation (prior) | result |
|---|---|---|
| K1 | order 5 on B1928's fine grid: lepton = down, relative difference ≤ 1e-8 (97%) | **holds in substance, fails the bar as written.** Every absolute difference is ≤ 7.2 × 10⁻¹⁶ (roundoff). The relative bar is exceeded on 1.2% of entries, all at y = 6, where the ratios are about 10⁻⁸; the largest is 2.5 × 10⁻⁸. The median is 2.5 × 10⁻¹⁵ |
| K2 | order 10 at B1724's four moduli: lepton ≠ down everywhere, > 1e-6 (85%) | **holds**: the smallest relative difference over 4 moduli, 2 ends, 2 readings and 2 ratios, at both end conventions, is 8.3 × 10⁻⁴ |
| K3 | lepton average = the average of the down step with charges (−1, 2), to 1e-8 (90%) | **holds**: ≤ 8.5 × 10⁻¹⁴ |
| K4 | plant: lepton charges (2, 1) restore equality at order 10, to 1e-8 (97%) | **holds**: ≤ 3.3 × 10⁻¹⁴ |
| K5 | the read-out on the whole at order 10 separates: z > 3 on at least half the outputs, both ends (70%) | **holds on every output**: z from 17.2 to 1 332 (constant end) and 164 to 849 (canonical end) |
| K6 | the order-5 difference integrates to 0, to 1e-8 (97%) | **holds**: ≤ 1.5 × 10⁻¹⁶ |

The control P3 holds exactly: the explicit-charge step reproduces frame C's down and lepton sectors, with relative
difference 0.0.

**On the size of the separation, as differences only.** On the order-10 grid, the per-point largest relative difference
between lepton and down outputs has median 0.18, and its smallest value is 1.9 × 10⁻⁵. B1928's interpolation error for
F̄ has median 4.5 × 10⁻⁴.

## Deviations and slips, said

- **K1's bar was set from SM-C13's noise floor and was still too tight.** At the top of the grid the ratios are about
  10⁻⁸, so the roundoff in their difference, about 10⁻¹⁶ absolute, is about 10⁻⁸ relative. The absolute differences show
  the copy is exact.
- **K5 and K6 crashed on their first run.**
  - The cause: they imported B1928's fiber_ergodic, which loads a coarse grid that main's checkout does not have.
  - K5's first grid (811 s) was lost. The script was fixed by copying B1928's thread() and reduce_pt() verbatim, and by
    saving the grid before the integral.
  - Nothing computed changed. Both crash logs are kept (`relays/sm_c13b/RUN_k5_crashed.txt`,
    `relays/sm_c13b/RUN_k6_crashed.txt`).
- **K6's z values are meaningless.** At roundoff the jackknife error is about 10⁻¹⁹, so z is large there by
  construction. K6 is read on its absolute value, as sealed.
- **Not rechecked:** the interpolation accuracy of D itself at order 10 (B1928's P1 checked F̄ at order 5). K5's
  separation is two orders of magnitude above B1928's interpolation error in median, and z counts sampling error only.
- **D1 inherits B1928's open hypotheses** H1–H3. The step through the non-perfect SL(2, F₂) is argued, not proved.

## Files

- `relays/sm_c13b/run_c13b.py`: the script.
- Results:
  - `relays/sm_c13b/c13b_k234.json` (K2–K4 and P3);
  - `relays/sm_c13b/c13b_k1.json` (K1's grid: differences only);
  - `relays/sm_c13b/c13b_k5.json` and `relays/sm_c13b/c13b_k5_grid.json` (K5: the grid of differences, and the
    ergodic integral);
  - `relays/sm_c13b/c13b_k6.json`.
- Runs: `relays/sm_c13b/RUN_k234.txt`, `relays/sm_c13b/RUN_k1.txt`, `relays/sm_c13b/RUN_k5.txt` and
  `relays/sm_c13b/RUN_k6.txt`, with the two crash logs above.
