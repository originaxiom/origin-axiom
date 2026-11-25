# CLAIM CARD — P-630's deviation spectrum: at the algebraic end of B181's critical locus every metallic trace map has the spectrum y = 2, 0, −2 in its own units, with the coupling marginal, and B1788's exponent set does not lie in it once m1/m3 is included or one unit serves every line; inside the locus the multipliers move with the coupling, so the test is not posed. The golden chain's positive control recovers h = 1/10 and not, at N ≤ 36, h = 3/5

- seat, branch, commit: chat1, origin/chat1/web-seat. Part A's script is at d4c206878, part B's at e30d17fc9; their
  outputs follow them.
- kind: negative
- touches: P-630, P-629
- effect: conditions — P-630's lead (Q1). The test is negative at the only place on B181's locus where the spectrum is
  discrete, and waits on a coupling the record does not fix elsewhere. The deviation route reads a leading exponent
  and, at these sizes, not a subleading one.
- imports: none
- premises on main: B181 (the critical locus), B471 (the metallic family), B107 (the single golden scale), B1788 (the
  closed form), B1785 (the 41 line slopes), B220 and B222 (the golden chain's c and content)
- decisive scripts:
  - part A: relays/chat1_2026-11-25_p630/p630_control.py, SHA-256 2a5841e1c035ddc9; numpy and scipy; reads no
    file; `python3 -I p630_control.py` (10 s). Output p630_control_out.txt, SHA-256 096b9e3c384aa6e8.
  - part B: relays/chat1_2026-11-25_p630/p630_trace.py, SHA-256 b2bd98cf28cc8fba; numpy and sympy; reads no file;
    `python3 -I p630_trace.py` (55 s). Output p630_trace_out.txt, SHA-256 43ee8e61a828a612.
- second computation:
  - Part B's six-cycle multiplier is computed twice by different routes: exactly from the Jacobian, and from band
    widths of direct transfer-matrix products. They agree to 1e-10.
  - The fixed point's spectrum is exact symbolic algebra, and for m = 1 it is B107's.
  - Part A's numbers have no second computation. Its gate reproduces the full spectrum at N = 10 and 12.
- already on main?: `scripts/checks/topic_sweep.py` at 88a1e9474 finds no arc for "deviation spectrum|deviation
  direction" (P-630 only), 29 arcs for "trace map" (B107 the nearest: eigenvalues ±φ^k), and 7 for "golden
  chain|tricritical" (B220 and B222). None compares a trace-map spectrum with B1788's exponents.
- what would make it fail:
  - for part B, a metallic map whose fixed-point spectrum is not λ_m^{±2}, −1; a line of B1785's census whose m2/m3
    and m1/m3 exponents are all odd multiples of their greatest common divisor; or a coupling fixed by the record
    (the comparison would then be posed inside the locus, and is not made here);
  - for part A, larger rings on which the ε′ read-outs of two directions converge to 3/5.

## What it means

- [E] At V = 0 the spectrum of every T_m at (1, 1, 1) is λ_m², −1, λ_m⁻²: y = 2, 0, −2 in the substitution's own
  units. The coupling direction has |μ| = 1, as B181's permanent criticality requires.
- [E] On the six-cycle, μ + 1/μ = 2 + (4 + λ²)²; the coupling direction keeps the eigenvalue 1 at every λ.
- [E] B1788's positive exponents on a line lie in u·{2, −2} on 5 of 41 lines for m2/m3, and on none with m1/m3. They
  lie in the metallic spectra (odd multiples of their gcd) on 14 of 41 for m2/m3, not on the lines carrying
  (3/10, 1/5), and on none with m1/m3 or with one unit for every line.
- [J] So the frame's exponents are not this locus's deviation spectrum: one side is rationals set by ‖2qα‖, the other
  logarithms of quadratic units.
- [E] Part A: in the golden chain the leading thermal dimension comes out 0.09993 (1/10) along two directions and two
  read-outs; the second reads 0.509 and 0.662 along two directions, and neither approaches 3/5 by N = 36.

0 of 19.
