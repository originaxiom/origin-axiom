# B1940 — The big run's area options corrected in extended precision: the frame lost the first generation and the mixing high in the cusp

**Verdict: PROVED** (the defect shown and located; the extended-precision frame checked against the double-precision
frame where that is sound and against τ → τ + 1 where it is not, with a planted fault; the corrected values computed
once, their second computation owed). Main, 2026-11-14, before the big run's look. Register rows P-853, P-850, P-845.
**No value is compared with any measured number.** 0 of 19.

## Seen first

- **Swept:** `VERDICT topic-sweep /extended precision|double precision|mpmath|high in the cusp|tau \+ 1|area measure|area option/: 16 of 1682 arcs on main match (NEGATIVE 3, OPEN 1, PROVED 12); 8 register rows match (DONE 4, QUEUED 4)`. No arc on main computes the frame above height 6 in extended precision; B1932 is the area options' source.
- **The literature:** none. The defect is in the record's own code.

## 1. The defect (`double_precision_fails.py`, `svd_alone_does_not_repair.py`, `closed_residues_do_not_repair.py`)
- **The test.** F̄ is invariant under SL(2, ℤ) (B1928), so F̄(τ + 1) = F̄(τ) exactly. In the record's double-precision
  frame (B1932's exact-weight form):
  - the identity holds to 2.5e-10 at height 6 and 1e-5 at height 9;
  - it fails by 0.12 at height 12, 0.32 at 20 and 2.8 at 30;
  - at height 12 the mixing moduli of W₋ come out with |V₂₃| and |V₁₃| exchanged.
- **The SVD is not the cause.** A 50-digit SVD of the same entries fails as before.
- **Neither are the residues.** B1906's closed-form residues in place of the contour fail as before.
- **The cause is the coupling itself.** The true m₁/m₃ falls below 1e-15 by height 12 (B1940's own frame gives 1.8e-15
  at 12, 2e-26 at 20 and 2e-60 at 45). So no coupling assembled in double precision resolves the first generation
  there, and the mixing that depends on its singular vector is noise.
- **The frame's zero test does not misfire** (`zero_test_does_not_misfire.py`). The test is |R_s| > 1e-12, meant for
  the zero law's exact zeros. No non-zero residue of the 24 points falls below it up to height 12; the smallest is
  6.5e-9 of the largest there.
- **Who it reaches.**
  - **The move-count options are untouched.** Their read-out grid stops at height 6 (B1928's grid), where the frame is
    sound, and agy-exp's X-EXACT-W agrees with them (B1937).
  - **The area options are not.** B1932's area measure computes F̄ at heights 6 to 45, and the area gives the region
    above height 11 about 9 % of its weight.

## 2. The frame in extended precision (`frame_mp.py`, `validate_frame_mp.py`)
- **What it computes.** Every step of the frame is redone in mpmath, at 30 + 2 Im τ digits:
  - the residues by B1906's closed form;
  - a₀ as the constant term of Kronecker's function, 2πiα + θ₁′(z)/θ₁(z);
  - the channel norm by B1919's closed form, with Theorem 90's correction;
  - the zero law's exact zeros, by exact rational characteristics;
  - the Higgs triplet from the record's q-series, unrounded;
  - the coupling, the SVDs and the CKM.
  The canonical end L₂ is the record's table, read at x reduced mod 1, as the definition's input.
- **The checks:**
  - **V1, against the double-precision frame where that is sound:** 2.4e-15 at height 1.5, 5.6e-14 at 3, and 1.3e-10
    at 6 (the double frame's own error there).
  - **V2, τ → τ + 1:** 7e-18 at height 12, 4e-18 at 20 and 3.6e-19 at 45.
  - **V3, a planted run at 15 digits:** the τ → τ + 1 check fails by 0.45 at height 20. Caught.
- **The cusp's structure.** High in the cusp the averaged mixing moduli tend to 5/12, 5/12 and 7/12 (W₋, at height 45:
  0.41667, 0.41667, 0.58333). The mass ratios tend to zero.

## 3. The area options recomputed (`area_measure_mp.py`, `assemble_values_v2.py`)
- **What is kept from B1932's construction:**
  - below height 6: its grid and quadrature, since the double frame passes there;
  - above 6: the average over five columns, the trapezoid in height, the end in two brackets (held at its height-6
    value; continued on the trend A + B/y), and the tail beyond 45 held.
- **What changes:** F̄ above height 6 comes from the extended-precision frame, on B1932's nine heights and on a refined
  set of 17.
- **The corrected values file** is `BIG_RUN_VALUES_v2.json`, sha256
  `9ece85e154238ae9c1fc3dc1664fbb3230a818096a3fcb608a5e22efca168115`.
  - It sits beside B1932's file, which stays in the record.
  - The move-count options are carried unchanged.
  - The area options take the held bracket on the refined heights.
  - Their error is the end's two brackets and the change of heights, in quadrature: 0.2 % to 0.6 % on the mixing,
    and below 1e-4 on the mass ratios.
- **What moved** (∣Δ ln∣ against B1932's file, positions up m₂/m₃, up m₁/m₃, down m₂/m₃, down m₁/m₃, |V₁₂|, |V₂₃|,
  |V₁₃|):

  | option | the mass ratios | the mixing moduli |
  |---|---|---|
  | W₋∣b (area) | below 1e-4 | +0.047, +0.020, −0.068 |
  | W₊∣b (area) | below 1e-4 | +0.014, +0.006, −0.034 |
  | W₋∣a, W₊∣a | 0 | 0 |

  The largest change, 0.068 in ln, is about two-thirds of the run statistic's σ floor of 0.10. So it was material.
- **The numbers are stable.** B1932's heights against the refined ones differ by at most 5.5e-3, and the end's two
  brackets by 3.0e-3.

## 4. The run's script, version 3 (`big_run_look_v3.py`, `big_run_windows_v3.py`)
- **The script.** Version 2's statistics, bars, calibration and outcome are unchanged; only the values file it pins
  changes: `big_run_look_v3.py`, sha256 `a5cabed5538b2847fd9551314e97b76d48f3c0a5cc8922a0293a213dc49a8438`.
- **The window companion** reads version 3: `big_run_windows_v3.py`, sha256
  `a5bc2a2971a3e579de6a8ed556a35c00a64a15743ec2fb4a787dace491a1b670`.
- **The lock** repeats B1937's synthetic tests on version 3. It also holds that the corrected file changes only the
  area options' mixing, and keeps the defect and the repair.
- **The rule's amendment A13:** version 3 governs. B1932's version 1 is run beside it on the values it sealed, and is
  reported. Version 2 is not run, since its values are superseded.

## What the wall teaches
- **A frame validated at moderate heights can still fail high in the cusp.** The hierarchy it builds
  (m₁/m₃ ~ e^{−3y}) outruns the arithmetic it is computed in.
- **A symmetry the object must have is the cheapest test of every computation of it.** Here the symmetry is
  τ → τ + 1. It found this defect in one line; checking every height a computation uses costs seconds.
- **Every use of the frame above height 9 needs the same check** (P-853, Q3).

## The second computation (the same night)
- **The comparison.** agy-exp's X-MEASURE was sealed unread at 04293e826. Main compared it with this arc's corrected
  file, using `compare_area_second.py`, committed before that output existed, through a mechanical adapter
  (`compare_area_x_measure.py`).
- **Both area options agree:** W₋∣b at worst 0.12 of the tolerance, W₊∣b at 0.14.
- **Against B1932's uncorrected file they disagree,** at 2.52 and 1.74 of the tolerance. An independent code, which
  treats the cusp in extended precision, confirms both the defect and its correction.
- **Label:** the area options are recomputed independently (one seat).

## Not claimed
- Any comparison with a measured number.
