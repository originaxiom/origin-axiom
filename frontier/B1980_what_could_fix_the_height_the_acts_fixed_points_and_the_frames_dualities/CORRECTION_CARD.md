# B1980 correction card — part B rerun with the canonical end read on the whole curve

Written 2026-11-25, before the rerun, after main found its own instrument fault in part B, between the run and the landing
(the landing was stopped before any push). Data-free. 0 of 19.

## The fault

- **Frame C's channel norm uses the canonical end L(τ),** B1667's horocycle of length 2.
- **B1927 established that L is covariant,** so its invariant form is a modular function. It is to be read at τ carried
  into the fundamental domain.
- **B1927's table** (`canon_readout.py`) covers the fundamental domain from height 0.866 to 6. Outside it, it returns the
  nearest table value (below), or the value at height 6 (above).
- **Frame C's code** (`determinant_law.parts`) reduces only Re τ mod 1 before reading the table.
- **The consequence for part B.** The S-move partners at heights 2/3 and 0.4, and every partner below 0.866, read the
  table outside its domain: L = 2.7193 at all of them, where the covariant value at i/y is L(iy). The sources above
  height 6 read the clamped value.
- **So part B's "frame C fails S" is unproven,** and its K ≠ 1 results mix in-domain and out-of-domain ends.

## The rerun (`verification/duality_cov.py`)

- **The frame.** `determinant_law.parts`, copied with one change: L is a parameter. A control at 12 points checks that,
  given the end `parts` itself reads, it reproduces `parts`' matrices exactly.
- **The covariant end.** L_cov(τ) = L_2(τ_FD), where τ_FD is τ carried into the fundamental domain by T and S. On the
  axis this is iy for y ≥ 1 and i/y for y < 1. Heights above 6 stay clamped as in every run on record; that clamp is
  disclosed, not fixed here.
- **The S move.** Source heights 1.25, 1.5 and 2.5 against 0.8, 2/3 and 0.4. The matching is as in part B: B1976's 96
  points against all 899 nonzero points of E[30], under any bijection, with sectors and reading fixed. If that fails,
  the wider matching of `s_wider_posthoc.py` is used (any sector permutation, either reading, up/down order).
- **The K ≠ 1 family**, the same K and heights as part B, with the covariant end on both sides.

## Expectations, with priors

| id | expectation | prior |
|---|---|---|
| K0 | the copied frame reproduces `parts` exactly at 12 points, given the same end | 0.99 |
| S-cov | with the covariant end, the S move matches every point within 1e-8 at all three height pairs (plain or wider matching) | 0.40 |
| F-cov | with the covariant end, no K ≠ 1 passes | 0.90 |

## What each outcome means

- **S-cov holds:** frame C is S-covariant once its end is read on the whole curve. The one-hole defect was the
  implementation of the end, not the frame. P-882 then reduces to reading the end covariantly everywhere.
- **S-cov fails:** the breaker is elsewhere: the channel norm F_u, the a₀ term, the characteristic map (a, 2b), or the
  Higgs. P-882's search continues with ablations.
- **Nothing is compared with data.**
