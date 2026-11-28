# Expectation, Q0008 (banking seat V1, fam1-v1-unset-04), committed before any computation

*2026-11-28. Card: relays/claims/CLAIM_2026-11-27_C8_two_registers.md on audit/physical-bridge-2026-09-05 at
2de93d2e65125601804e66dbc1f8631e9d9ec55c (the queue's record; the card names 22e94b0c1 for its script). Read: the card,
its decisive script (read as text, not run), the intake's record check (queue/checks/Q0008.json) and the queue record.
Disclosed: reading the record's history showed one line summarising the peer stage's outcome; the peer note itself was
not opened. This seat checked other packets of the same lane earlier (relays/SM_CHECK_PHYSICAL_*.md on its old branch);
none of them is this card. No code run yet.*

## The claim, as this seat reads it

For F25 = F5[d]/(d^2 - 2), G = SL(2, 25), the even Weil module of dimension 13 put into Spin(16) through 13 + 3 and then
into E8 by the semispin inclusion, the adjoint 248 = Lambda^2(16) + (64 x 2): with the geometric holonomy alone
(meridian U(1), longitude Z U(-2d)) the peripheral torus has 8 adjoint spin coefficients with periodic meridian spin;
with the commuting dihedral sheet lift joined (the meridian adds j, j^2 = -1), it has 0. The card's eight decisive lines
also state: 13 distinct joint labels and 13 nonzero Fourier links; 6 negative eigenlines of an involution with spin
square -1; spin multiplicities 4 at zero, 3 on squares, 2 on non-squares; both adjoints of size 248; the counts
(36, 12, 32, 8, 0) and (36, 8, 32, 0, 0); the sheet group's centre and the central multiplication kernel; and the
central product's order 156 000.

## How this seat will recompute (own code, sharing nothing)

- the Weil representation built as explicit matrices in the Schrodinger model on functions on F25 (multiplication by a
  character for U(b), reflection for -I, a Fourier transform for w), restricted to the even functions;
- the joint eigen-phases of the meridian and longitude read off those matrices, not from a trace formula;
- the spin square of an involution read from the Fourier involution's eigenvalues, its sign fixed by det = +1;
- the spin weights and the adjoint's joint characters assembled from those phases; the sheet group computed from its
  presentation (r^5 = 1, j r j^-1 = r^-1, j^2 = -1).

## Expectations

| | expectation | prior |
|---|---|---|
| X1 | 13 distinct joint labels on the even module; every Fourier link to the zero vector nonzero | 90% |
| X2 | an involution of PSL(2, 25) has 6 eigenvalues -1 on the 13, so its spin lift squares to -1 | 70% |
| X3 | the spin weight multiplicities 4, 3, 2 as stated | 75% |
| X4 | the counts (36, 12, 32, 8, 0) geometric and (36, 8, 32, 0, 0) joint | 70% |
| X5 | the central product's order 156 000 and the stated kernel | 80% |
| V | verdict ACCEPT (the card's decisive lines all recomputed) | 60% |

The likeliest fault, if any: the spin lift's sign on the longitude (X2), which decides the 8 against the 0.
