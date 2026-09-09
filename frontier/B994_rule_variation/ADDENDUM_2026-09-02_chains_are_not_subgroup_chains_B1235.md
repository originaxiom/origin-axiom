# Addendum (2026-09-02) — the exhibited chains are rendering, not descent; the endpoint survives (B1235)

`FINDINGS.md:27` shows `SU(3)³ → SU(5)×U(1) → SM` and `SU(3)³ → Pati-Salam → SM`. Neither is a subgroup chain: a
simple factor maps injectively or trivially, and dim su(4) = 15, dim su(5) = 24 exceed dim su(3) = 8, so neither
Pati–Salam nor SU(5) embeds in SU(3)³.

Recomputed with B869's committed engine (`frontier/B869_false_positive_control/false_positive_control.py`,
`all_descents`) on the three parents — `frontier/B1235_two_seat_harvest/verification/b994_parent_menus.py`, output
`b994_parent_menus.txt`: SU(3)³'s menu is `{su(2)+su(3)+su(3)+u(1)} × 3` with no PS/SU(5) rung, and all three parents
cascade to `su(2) + su(3) + 3 u(1)`. **B994's endpoint claim stands on a real subgroup basis**; the two chains in
the FINDINGS table were a rendering error, not a computation. Source: fab5cloud D10/P2, recomputed here.
