# Theorem 90's leading form against the exact norm (main, 2026-11-14 ~16:30), expectations before the run
Weight N_T90 = 2 pi L_2 + c_s - pi |a0_s|^2 e^{-2 L_2} (a0 from the frame's a0_of; the e^{-4L} term dropped), against the exact
horoball norm (twisted_norms), at 3 points (0.25 + 3i, 0.25 + 1.5i, i), 24 lines, 3 sectors.
SUFFICIENT if the norm gap falls below 1e-4 in median and the seven averaged outputs move by less than 1e-3 in ln (the
read-out's precision); then the exact-weight frame is computed on B1928's whole grid with N_T90. INSUFFICIENT otherwise
(then the e^{-4L} term or the exact norm on the grid).

## Result (~17:10, t90_run.txt): SUFFICIENT. Norm gap median 7-9e-6 (max 4.9e-5) against 1.5-3.3e-3 for the truncation;
the seven averaged outputs move at most 3.1e-5 in ln (truncation: ~1e-2). Frame C's exact-weight values can be computed on
B1928's grid with N_T90. NOTE: this script's (and truncation.py's) B1667 geometry, reached by Newton walks with large
steps, gives L_2 below B1667's committed values at low Im tau (tau = i: 2.603 and 2.697 against 2.7193; at Im tau >= 1.5
equal); B1667's committed grid (reproduced by agy-exp's X-OWN F1) stands. The comparisons above are at each run's own L_2,
and the correction enters through e^{-2 L_2} only, so the conclusions stand; the grid run uses B1667's committed ends.

# W-F16's test (D o C in the fibre frame), expectations before the run (~17:12)
D (the scar duality) acts on the fibre frame by flipping every matter charge with the Higgs partner, keeping each world
(agy-exp's X-SCAR); C exchanges S and S~. Compare world 1 at line (a, b) with world 2 at line (-a, -b), 3 points x 3 lines,
canonical ends. SYMMETRY if max |log ratio| < 1e-9; NOT A SYMMETRY if > 1e-3 (then one bit of the second block is a genuine
input in frame C, H3's rows 2 or 4). Control: world 1 at (a, b) against world 1 at (-a, -b) must agree (matter's parity).
## Result: NOT A SYMMETRY. World 1 at (a, b) against world 2 at (-a, -b): 3.06 in log; control (matter's parity) 6.0e-14.
