# B1976 — The level as a lens: at points of order N frame C sees the charges mod N; level 5 is minimal SU(5)'s ties, order 6 makes up and down share their left structure, and order 30 on the act's line breaks the ties at most points, keeps the mixing aligned, and shows a 2–3 mixing that barely falls with height

**Verdict: PROVED** for E0, E2 and E5, as sealed.
- **E1 holds for the mixing.** It holds in part for the couplings: exact equality at 12 of 24 points, and equality up to theta phases at the rest.
- **E3 and E4 hold at most points** (88 and 92 of 96), not at every point as written.
- **E6 fails** (26 of 96).
- **The slowly falling 2–3 mixing is a post hoc observation, labelled.**

Main, 2026-11-24. Data-free. The card and the script were hashed before the run (`EXPECTATIONS_HASHED.md`, with one disclosed mend). Register rows P-845 and P-860 (d). **0 of 19.**

## Seen first

- **Swept:** `VERDICT topic-sweep /order 30|level 30|lcm\(5, ?6\)|exponent grid|1/30|level as a lens|units of Z/N/: 0 of 1717 arcs on main match (none); 3 register rows match (DONE 1, QUEUED 2)`.
- **The record:** B1698 (sectors coincide at orders dividing 4 or 5), B1942 (order 15), B1949 (e_lep(α) = e_down(3α)), B1971 and B1975 (the order-5 and order-8/10 census), and P-845 (which level the object picks).
- **The seats:** agy-002's M33 (an order-10 lift splits the leptons), the agy lane's C7 (lcm(5, 6) = 30 inside a weave model), agy-exp's LINK4 (averaging over K5 and K6).
- **The literature:** minimal SU(5)'s Yukawa relations: Y_u symmetric, Y_e = Y_dᵀ.

## The results (`verification/level30.py`, `level30_run.txt`, `level30_run.json`)

| id | sealed expectation | result |
|---|---|---|
| E0 | the unit test: ties by units of Z/N | **holds**: mod 5 the lepton is tied to down (swapped); mod 6 up is tied to down; mod 30 no two sectors are tied |
| E1 | at order 6, Y_up = Y_down and the mixing is the identity | **the mixing holds:** 1 − least diagonal = 0 at all 24 points (the run's own "identity" count read 0 because its bar, 1 − 1e-20, rounds to 1.0 in double precision, a fault of the test; `top_points_run.txt` prints the exact values). **The couplings in part:** Y_up = Y_down exactly at 12 of 24 points, and at the other 12 they differ by the theta functions' phases under integer shifts of the characteristics (relative difference 1.7) while sharing their left vectors. **The lens holds up to phases, not exactly** |
| E2 | the order-5 control | **holds**, 4 of 4 |
| E3 | order 30 splits the leptons from down at every point | 88 of 96. At 8 points the tie persists, a sub-lattice: (1/5, 7/30), (1/5, 17/30), (2/5, 19/30), (2/5, 29/30) and their negatives |
| E4 | order 30 gives the up sector a '1' channel at every point | 92 of 96. It is absent at (2/5, 19/30), (2/5, 29/30), (3/5, 1/30), (3/5, 11/30) |
| E5 | the mixing stays aligned at most points | **holds**, 96 of 96, better than the prior 0.45 |
| E6 | the mixing grows at most points | **fails**: 26 of 96. Median largest off-diagonal 1.4e-10, against 6.3e-5 and 2.2e-13 at the act's order-5 points |

## Post hoc (labelled; `verification/top_points.py`, written after reading the run)

- **Where:** the five order-30 points with the largest mixing, (4/15, 1/30), (4/15, 11/30), (4/15, 7/10), (11/15, 3/10) and (11/15, 19/30).
- **What:** all five share one pattern. |V₂₃| = 0.0181 at height 30, with a rate between heights 20 and 30 of **0.032 in ε units (near 1/30)**; V₁₂ falls at 0.600 and V₁₃ at 0.633.
- **Why it matters:** the 2–3 mixing barely falls with height. Every mixing entry at level 5 falls at a rate of 1/10 or more.
- **A reading, not a result:** at level N the frame's exponents live on a grid of about 1/N, so a finer level allows smaller exponents and larger mixing.

## What it means

- **The structural ties are the level's.** The lepton–down tie and the symmetric up matrix are minimal SU(5)'s relations, which level 5 imposes. B1698 found the first of them in October.
- **Order 6 makes up and down share their left structure** (the mixing is the identity), because u and d differ by 6 in 6Y.
- **Order 30 on the act's line breaks both ties at most points and keeps the mixing aligned.** So the lepton–down split and the alignment can coexist, which level 5 could not give.
- **The mixing's size is not cured in general.** At some points level 30 gives a 2–3 mixing that barely falls with height.
- **Nothing here derives that the object picks level 30** (P-845). Nothing is compared with data.

## What is open

- **The exponent grid's law:** does the smallest mixing exponent at order N track 1/N? A card is owed.
- **The masses at the slow-mixing points:** their hierarchy, not computed here.
- **The sub-lattices where the ties persist,** in closed form.
- **Whether a principle puts the object at level 30:** the act's 5 times the gauge centre's 6, P-845.
