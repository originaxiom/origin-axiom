# B1976 card — the level as a lens: frame C (every sector reading S) at points of order 30

Written 2026-11-24 before any run, at the author's word ("go ahead"), after main's reading of the record and seats on
levels: B1698 (sectors coincide at orders dividing 4 or 5), B1942 (order 15 keeps the leptons and moves the quarks),
B1949 (e_lep(alpha) = e_down(3 alpha)), agy-002's M33 (an order-10 lift splits the leptons), the agy lane's C7
(lcm(5, 6) = 30 in a weave model). Nobody has computed frame C at order 30. Data-free. 0 of 19.

## The hypothesis

- **The lens.** At a point of order N, frame C sees a sector only through its charges 6Y times the point, so only mod N.
  - Two sectors are tied exactly when a unit of Z/N carries one charge pair to the other, swapped or not.
  - Mod 5 this is minimal SU(5): the up pair (1, -4) is (1, 1), so the up matrix is symmetric; the lepton pair (-3, 6)
    is 3 x down (1, 2), swapped.
  - Mod 6 the up and down pairs coincide, since u and d differ by 6.
- **Order 30** (the act's 5 times the gauge centre's 6) is the first level at which no unit ties any two sectors.

## The points and settings

- **P30:** the 96 points of exact order 30 whose order-5 part lies on the act's line ⟨(1/5, 2/5)⟩ (B1943): w5 + w6,
  for 4 points w5 and the 24 points w6 of exact order 6.
- **Controls:**
  - P6: the 24 points of exact order 6;
  - P5: the 4 points of the act's line.
- **Settings:** height 30, column 0.13; frame C through B1945's `parts`, unchanged; every sector reading S (B1970).

## Expectations, with priors

| id | expectation | prior |
|---|---|---|
| E0 | the unit test: no two sectors are tied by a unit mod 30; mod 5 the lepton is tied to down (swap) and up to itself (symmetric); mod 6 up is tied to down | 0.95 |
| E1 | at every P6 point Y_up = Y_down to working precision, so the mixing is exactly the identity | 0.85 |
| E2 | at every P5 point the up '1' channel vanishes and the lepton ratios equal the down ratios (B1971, SM-C13) | 0.97 |
| E3 | at every P30 point the leptons' generation ratios differ from the down quarks' (max of the two log ratios above 0.1) | 0.8 |
| E4 | at every P30 point the up '1' channel is nonzero (above 1e-10 of the largest channel) | 0.85 |
| E5 | the mixing is aligned (least diagonal at least 0.9) at most P30 points | 0.45 |
| E6 | at most P30 points the largest off-diagonal entry is larger than at the act's order-5 point it contains (the mixing grows at level 30) | 0.45 |

## What kills it

- **The lens is wrong** if E0 fails, or if E1 fails at any P6 point (up and down not identical at order 6).
- **Level 30 does not remove the ties** if E3 or E4 fails at most P30 points.
- E5 and E6 decide whether level 30 helps the mixing. They can fail without killing the lens.
- Nothing here derives that the object picks level 30. That is P-845's question, and the card does not claim it.
