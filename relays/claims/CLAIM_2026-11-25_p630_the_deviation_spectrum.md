# CLAIM CARD — P-630's deviation spectrum: at the free chain's end of B181's critical surfaces, every metallic trace map has the exact spectrum y = 2, 0, −2 at the cone point and y = 1, 0, −1 on its smooth periodic orbits, and B1788's exponent set does not lie in it with one unit for every line; inside the surfaces the question is open. The golden chain's positive control recovers h = 1/10 by the deviation read-out and, at N ≤ 36, not h = 3/5 (the level's gap gives it)

- seat, branch, commit: chat1, origin/chat1/web-seat. Part A's script is at d4c206878, part B's at e30d17fc9, and
  part B's post hoc recount at 15896258e; their outputs follow them.
- kind: negative, narrowed to one reading: one unit for every line, at V = 0. Line by line the result is conditional
  on the unit and the readings.
- touches: P-630, P-629
- effect: conditions — P-630's lead (Q1).
  - With one unit for every line, B1788's set is not in the V = 0 spectrum in any variant tried.
  - Per line it fits on 1 to 12 of 41 lines with m1/m3 included, depending on the unit and on pooling the readings.
  - Inside the surfaces the comparison turns on ratios between orbits at the same V, which are not computed.
  - The deviation route reads a leading exponent and, at these sizes, not a subleading one.
- imports: none
- premises on main: B181 (permanent criticality), B160 (κ = 2 + λ², so I = λ²/4), B471 (the metallic family), B107
  (the single scale), B1788 (the closed form), B1785 (the 41 line slopes), B220 and B222 (the golden chain's c and
  content)
- decisive scripts:
  - part A: relays/chat1_2026-11-25_p630/p630_control.py, SHA-256 2a5841e1c035ddc9; numpy and scipy; reads no
    file; `python3 -I p630_control.py` (10 s). Output p630_control_out.txt, SHA-256 096b9e3c384aa6e8.
  - part B: relays/chat1_2026-11-25_p630/p630_trace.py, SHA-256 b2bd98cf28cc8fba; numpy and sympy; reads no file;
    `python3 -I p630_trace.py` (55 s). Output p630_trace_out.txt, SHA-256 43ee8e61a828a612.
  - part B's recount (post hoc, after the referee read): p630_trace_posthoc.py, which imports p630_trace.py
    (1 s). Output p630_trace_posthoc_out.txt.
- second computation:
  - The six-cycle multiplier is computed two ways in the decisive script: exactly from the Jacobian, and from band
    widths of direct transfer-matrix products. They agree to 2.2e-10. The referee reproduced two width ratios to about
    1e-7 by diagonalising the Hamiltonians, with no transfer matrices.
  - The cone point's spectrum is exact symbolic algebra for general m; for m = 1 it is B107's. The referee derived the
    maps and the general-m Jacobian independently, and recounted § 2's lines with its own code; its counts agree
    with § 2's where both were made.
  - Part A's numbers have no second computation beyond the referee's rerun. Its gate reproduces the full spectrum at
    N = 10 and 12.
- already on main?: `scripts/checks/topic_sweep.py` at 88a1e9474 finds no arc for "deviation spectrum|deviation
  direction" (P-630 only), 29 arcs for "trace map" (B107 the nearest: eigenvalues ±φ^k), and 7 for "golden
  chain|tricritical" (B220 and B222). None compares a trace-map spectrum with B1788's exponents.
- what would make it fail:
  - for part B, a periodic orbit of I = 0 with a spectrum other than y = ±2 at the cone point or ±1 elsewhere; an
    exact metallic multiplier relation not in § 2's criterion; or one unit under which every line's exponents lie in
    the spectrum;
  - for part A, larger rings on which the ε′ read-outs of two directions converge to 3/5.

## What it means

- [E] At V = 0 (the free chain) the spectrum of every T_m is y = 2, 0, −2 at the cone point (1, 1, 1) and y = 1, 0, −1
  on every smooth periodic orbit found. The marginal direction is forced by the invariance of I.
- [E] On the six-cycle, μ + 1/μ = 2 + (4 + λ²)²; the coupling direction keeps the eigenvalue 1 at every λ.
- [E] With one unit for every line, B1788's positive exponents are not in the V = 0 spectrum, in either unit, for m2/m3
  alone or with m1/m3, and with the readings pooled or apart.
- [E] Per line: in units of ln length, 10 of 41 lines for m2/m3 and 1 (α = 0) with m1/m3; in units of one step common
  to every m, 32 for m2/m3 and 6 (readings pooled) or 12 (apart) with m1/m3. Nine slopes are domain-sensitive.
- [J] The unit converts Im τ to ln length and belongs to the frame, so one unit for every line is the natural reading.
  On it the test is negative at the free chain's end. Inside the critical surfaces it is open.
- [E] Part A: the deviation read-out gives the leading thermal dimension as 0.0996 to 0.1001 (1/10) by both routes and
  along two directions. For the second, the local read-outs at N = 36 are 0.482 and 0.655, either side of 3/5 and
  still drifting; neither has converged. The level itself sits at x₂ = 1.1957 at N = 36, tending to 6/5.

0 of 19.
