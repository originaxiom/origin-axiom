# B1268 addendum (2026-09-09, from B1350) — two precision caps in the machinery, found where they bite

B1350 reused this arc's Newton search and cohomology report along the subregular point's V₁₀ classes and met two limits that the
V₈ computation of this arc never reached. Neither changes anything banked here (the V₈ point's ranks have gaps of 40 orders and
its Newton converged to 10⁻⁶³); both are recorded so the next user of `cusped_theta_odd_hp.py` knows them.

1. **The damping.** `newton()` regularises the normal equations by 10⁻²⁴·max G_ii. Along a class whose necessary corrections lie in
   directions of singular value of order ε (the cocycle directions that become genuine image directions only away from ρ₀), that
   damping suppresses the step and the search crawls at |res| ≈ 3.6·10⁻¹³ (B1350 `v10_direction_run_stall.txt`, forty iterations,
   1 % per iteration). At 10⁻⁵⁰ the same start converges quadratically to 10⁻⁶⁸ (`probe_mu50.txt`). B1350's driver takes the
   damping as a parameter with 10⁻⁵⁰ as its default; this arc's script is unchanged.
2. **The 70-digit transfer and the 10⁻³⁰ threshold.** `acb2mp` formats ball midpoints with 70 digits and `mp_rank` decides at a
   relative 10⁻³⁰; `OMEGA_ACB` is fixed at the import-time precision. At the V₁₀ points genuine pivots sit at 10⁻³³ … 10⁻³⁹ and the
   report misreads h¹(M; 27) as 2 and h⁰(∂M; 27) as 1 while violating the torus Euler characteristic. B1350's `report_hp.py` lifts
   the caps (2000 bits, 200-digit transfer, threshold 10⁻⁵⁰, the full pivot spectrum printed) and carries the two consistency
   checks — h⁰ − h¹ + h² = 0 on the torus and h¹(V) = h¹(V*), h²(V) = h⁰(V*) — that expose a misread rank. At this arc's V₈ point
   and at ρ₀ the re-reader reproduces this arc's numbers exactly.

A rank read at 60 digits is a rank only when its pivot gap says so; the report should print the gap, and did — the lesson is to
read it.
