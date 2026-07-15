# B631 — THE MATRIX COMPARISON RUN (the interaction round, part 3 of 3)

**Date: 2026-07-15. Status: BANKED. One mechanical run under the sealed
design (B630, sha e217e623…, hash-verified in-run) on the sealed values
(B629, sha 0ec9ac39…, hash-verified in-run). Per the directive, this
arc's entire output is the deliverable sentence plus the raw data. No
interpretation beyond the sentence.**

## The sentence

**"The 3×3 odd hearing form at E₆ level 2 does not match the PMNS
matrix at the 1% tier, with null-model p-value 0.7000."**

## The raw data (run_output.txt, verbatim numbers)

Frozen measured table (PDG 2024 central, δ_CP = 1.19π, derived
mechanically from B615's byte-identical sin² freeze):

    |U_PMNS|² = [ 0.677754  0.300246  0.022000 ]
                [ 0.091358  0.374654  0.533988 ]
                [ 0.230888  0.325100  0.444012 ]

Framework table at the D-optimal alignment (of the 72 declared; the
circulant has 12 distinct variants, reported):

    aligned |B|² = [ 0.543134  0.349292  0.107574 ]
                   [ 0.107574  0.543134  0.349292 ]
                   [ 0.349292  0.107574  0.543134 ]

ALL NINE deviations |aligned − measured| (no selection):

    [ 0.134620  0.049046  0.085574 ]
    [ 0.016216  0.168480  0.184696 ]
    [ 0.118404  0.217526  0.099122 ]

Matches at |Δ| ≤ 0.01: **0/9** (null expectation 0.7748).
Matches at |Δ| ≤ 0.001: **0/9** (null expectation 0.0775).

Verdict statistic: D_obs = 0.13407059.
Haar-U(3) null (N = 10⁶, seed 20260715, identical min-over-72
statistic): median 0.102176, 1% quantile 0.024559, 10% quantile
0.050218, minimum 0.001974.

**p_D = P(D_rand ≤ D_obs) = 700005/1000001 = 0.700004.**

Robustness rows (declared in the design, no verdict weight):
R-a (the handoff's NuFIT-proxy table): D = 0.13586323.
R-b (δ_CP scan at frozen angles): D = 0.09650176 (δ=0),
0.13020611 (π/2), 0.12945508 (π), 0.13020611 (3π/2).

## The verdict (locked table, design §5)

p_D = 0.700 ≥ 0.1 → **STRUCTURED-NULL. The stopping rule fires: the
program's SM-comparison capability at this level is exhausted. The
mathematics publishes as mathematics.** Per the directive's binding
clause, there is no "next layer" continuation; any future SM-facing
comparison requires a new owner-level directive with its own principled
preregistration. Seat 4 reviews this raw output alongside the two seals.

## Protocol record

Values sealed and banked first (B629, PR #1004); design sealed second
(B630, PR #1005); one run, no reruns (one pre-run syntax bug — a stray
tuple comma in the verdict branch — was fixed before any distance was
computed; nothing was altered after first output). The pre-banked MB12
structural floor (D ≥ 0.0285 from the s₁₃² entry) was not binding:
the observed D = 0.134 is 4.7× the floor, and the null decided the
region is typical, not rare. Lock:
tests/test_b631_matrix_comparison.py (fast: seals + D_obs + 0/9;
OA_SLOW=1: the seeded null reproduced exactly).
