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

---

## ADDENDUM (2026-07-15, same day — the process repairs; the owner's catch)

The owner directed a read-back of PROGRESS_LOG against this arc; three
process elements of the house standard were missing and are now supplied.
The sealed run is UNTOUCHED; nothing below alters the verdict.

**1. Pipeline controls (`b631_controls.py`, `controls_output.txt`) — the
"the null is real, not a broken pipeline's" standard (B575):** C1
positive control: framework := |U_PMNS|² itself gives D = 0 and
p = 1/(N+1) exactly. **C2 power demonstration: a unitary genuinely near
PMNS (U·e^{iεK}) fires MATCH-CANDIDATE — ε = 0.02 → p = 0.00027,
ε = 0.05 → p = 0.0061** — the instrument COULD have detected a real
match; the 0.700 is discriminating, not vacuous. C3 sampler calibration:
Haar |U_ij|² reproduces the exact Beta(1,2) law (mean 1/3,
P(x ≤ 1/2) = 3/4) at 200k samples. C4 seed robustness: p = 0.7008 /
0.6995 under fresh seeds. C5 path consistency: loop-vs-vectorized D
identical to 1e-15.

**2. The MB13 retro-sweep (`MB13_RETRO_SWEEP.md`):** run AFTER sealing —
a lapse, recorded. Findings: the held-out claim SURVIVES (no prior
matrix-level comparison anywhere); contextual prior art that belonged in
B630's MB12: B322 (PMNS angles already chance-level in the 6241-number
value hunt) and B342 (the object's ℤ/3 = trimaximal symmetry; the
uniform DFT circulant's TM2 pattern already DISFAVORED by data — B631's
non-uniform circulant losing at the moduli level is the same lesson one
layer up).

**3. The dual-protocol routing:** hints H134 (the κ=10 golden
eigenspace's golden-rational delocalization weights) and H135 (the
one-field ℚ(ζ₂₈) closed form; symbolic proof gate) registered in
HINT_LEDGER; leads L86/L87 (the deferred points 2/3, GATED) and L88 (the
symbolic Latin-square proof) registered in OPEN_LEADS; the stale L85 row
closed as resolved-by-outcome-B. CANDIDATES.md PC26 row updated with the
round's §9 content.
