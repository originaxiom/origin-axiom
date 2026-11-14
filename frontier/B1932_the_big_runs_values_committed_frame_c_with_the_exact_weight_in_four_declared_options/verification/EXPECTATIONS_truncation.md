# Pre-seal check Q8: does the channel weight's truncation move frame C's seven values? Expectations, before any run
(main, 2026-11-14 ~15:50)

Frame C weights each channel by sqrt(2 pi L_2 + c_s), the leading form of the kernel's norm outside the length-2 horoball.
The exact norm (B1667's cell minus the horoball, the frame's twisted kernel; the web seat's exact_end machinery, on main
under B1838) adds exponentially small terms. At Im tau ~ 3 they were 0.6 % of the norm (harvest row 1459). The read-out on
the whole integrates over the whole modular surface, down to Im tau ~ 0.87.

Computed: at 8 points of the fundamental domain (Im tau 0.9 to 3), for all 24 lines of order 5 and the three sectors,
the exact norm against 2 pi L_2 + c_s (L_2 from B1667's geometry at the point), then world 1's seven claimed outputs
(up and down ratios, the three mixing moduli) averaged over the 24 lines with each weight.

Outcomes: NEGLIGIBLE if the largest change of any of the seven averaged outputs, in ln, is below 1e-3 at every point
(the read-out's own precision); MATERIAL if above 1e-2 anywhere (then frame C's values must be computed with the exact
weight, or the truncation declared as part of the frame, before they are committed); between: reported as found.
Firewall: no output compared with any measured value.

## Result (2026-11-14, ~16:20; truncation_run.txt, truncation.json; 1469 s)
MATERIAL. At all 8 points (Im tau 0.9 to 3), the exact norm differs from 2 pi L_2 + c_s by 0.14-0.33 % in median (up to
1.5 %), and world 1's seven outputs averaged over the 24 lines move by up to 1.64e-2 in ln. Per output, median over the
points: up m1/m3 8.7e-3, down m1/m3 1.1e-2, |V12| 7.0e-3, |V13| 8.4e-3; up m2/m3, down m2/m3 and |V23| below 1e-3. The
shift does not grow toward the boundary (L_2 rises from 2.34 to 2.77 as Im tau falls). So frame C's values computed with
the truncated weight carry a systematic of about 1 % in four of the seven outputs. Before they are committed: the
weight is the norm at the cut (C06's definition), so the exact norm is the frame's own value and the truncation an
approximation; the cheap route is Theorem 90's closed form (B1838's note), whose residual against these exact norms is
the next check.
