# B1962's card — frame D1's cusp mixing, sealed before its outputs (P-861)

*Main, 2026-11-19. Written and committed before any output of frame D1's mixing is computed. Data-free: no output is
set beside a measured number. No values look follows from this card; that waits for the comparison rule (P-852, P-862).*

## Seen first

- **Swept:** `VERDICT topic-sweep /frame D1|shifted charges|cusp mixing|Szego zero|identity E|Higgs.s own twist/: 7 of 1702 arcs on main match (NEGATIVE 2, PROVED 5); 12 register rows match (DONE 1, QUEUED 11)`.
- **B1946 (PROVED):** frame C's cusp mixing, at the 24 points of order 5, heights 6 and 30. With the same Higgs reading
  in both sectors (S, S) it is aligned at both heights. (S̃, S̃) is aligned at height 6 and deranged at 30. The mixed
  readings are deranged at both. The derangement is a cyclic permutation of the rows.
- **B1947 (NEGATIVE as sealed):** twisting the Higgs inside frame C's coupling is not covariant under τ → τ + 1.
- **The web seat's W-B2 stage 3 (harvest row 1842), checked against main's own hand reduction (P-861, 2026-11-15):**
  - the only covariant place for the Higgs's twist is its own Szegő zero, at h = c·q_H·w with c = ±2;
  - there frame D1 equals frame C at shifted charges q′ = q − c·q_H/2, to 1e-14 at the residues (the identity E);
  - c = +2 gives (2q_L + q_R, q_L + 2q_R): up (−2, −7), down (4, 5), leptons (0, 9);
  - c = −2 gives (−q_R, −q_L): up (4, −1), down (−2, −1), leptons (−6, 3);
  - the Higgs's sign does not act as the reading, so frame D1 does not fix the reading;
  - which sign of c is the overlap's own is left open.
- **SM-C21 (register row P-873, 2026-11-18):** its negative on frame D1 holds for the two eigenlines of the Higgs
  ground plane, and not for the whole plane.
- **What P-861 still owes:** the mixing itself, which nobody has computed for frame D1.

## The definition

- **Frame D1** is frame C (B1940's extended-precision frame, as B1945 splits it and B1946 reads it) at the shifted
  charges of identity E. Nothing else changes: the exact channel weight, the canonical end, the 24 points of order 5,
  x = 0.13, the readings S and S̃ and B1946's unitary (left singular vectors, ascending).
- **Both signs of c are run.** The convention is not chosen here. If the outcome differs between the signs, the sign
  becomes load-bearing and is reported as such.
- **One hypothesis is assumed, not tested:** that identity E, shown at the residues, holds for the norms too. It is
  the debt's other owed item.

## Checks of the code, run before this card (disclosed)

- **C0a:** the charges entered match row 1842's: at c = +2, up (−2, −7), down (4, 5), leptons (0, 9); at c = −2,
  up (4, −1), down (−2, −1), leptons (−6, 3).
- **C0b:** one call of frame C's own code at height 30 takes 0.1 s. Frame D1's run needs no new numerical method.
- **No output of frame D1 was computed** in these checks.

## The cells

- **M0 (control, c = 0):** frame C's own charges. It must reproduce B1946's table to the digits printed there. If it
  does not, the run is void.
- **M1 (c = +2), M3 (c = −2):** for each reading pair (up, down) in {S, S̃}², over the 24 points at heights 6 and 30:
  the smallest diagonal |V| and the largest off-diagonal |V| of V = U_upᴴ U_down.
- **M2 (each c):** does the lepton sector copy the down sector? Per reading, the cell reports three numbers:
  - the largest distance of |U_lepᴴ U_down| from a 0/1 pattern (a plain copy);
  - the same against U(Y_downᵀ) (a transposed copy);
  - the largest difference of the normalised singular values (s/s_max).

## The classification, fixed now

- **A reading pair is classified at each height:**
  - **ALIGNED** if the smallest diagonal |V| is at least 0.9 at every one of the 24 points;
  - **DERANGED** if it is below 0.1 at some point;
  - **PARTIAL** otherwise.
- **The leptons, per reading and height:**
  - **COPY** if either pattern distance is below 1e-6 and the spectra agree to 1e-6;
  - **SEPARATE** otherwise.
- **The gate, P-861's test.** Frame D1 passes it, under a sign of c, if both of these hold:
  - every one of the four reading pairs is ALIGNED at both heights. Frame D1 does not fix the reading (row 1842), so it
    passes only if the reading does not matter for the mixing;
  - the leptons are SEPARATE at both heights for both readings.
- **Otherwise the result is NEGATIVE as sealed.** Frame D1 does not clear the gate. The mixing fault then returns to
  P-847, the principle that would fix the reading.

## Expectations, with priors, fixed now

- **E0:** M0 reproduces B1946. Prior 0.99; it is a code check.
- **E1:** at c = +2 the mixed readings are DERANGED at height 30, as in frame C. Prior 0.7. The reason: at c = +2
  the '+' characteristic is frame C's times 3, an automorphism of ℤ/5, and the '−' characteristic is unchanged.
- **E2:** at c = +2, (S, S) is ALIGNED at both heights and (S̃, S̃) is DERANGED at height 30, as in frame C. Prior 0.5.
- **E3:** at c = +2 the leptons COPY the down sector, transposed, at both heights (row 1842 reads this from B1934's
  law). Prior 0.7.
- **E4:** at c = −2 the table is frame C's with left and right exchanged, (q_L, q_R) → (−q_R, −q_L). Prior 0.5 that it
  equals M0's.
- **The overall outcome:** NEGATIVE as sealed. Prior 0.8.

## How it is run

- `verification/d1_mixing.py`, `python3 -B d1_mixing.py > d1_mixing_run.txt`.
- It refuses to run until this card is committed unchanged.
