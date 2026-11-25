# B1999 — the agy lane's C59 package (C57 and C58 stopped before output), checked on main

Written 2026-11-25, **after** the checks it records were run in main's scratchpad. The author relayed the lane's summary and
asked "is this true", then "are u sure ure not downplaying or sabotaging anything". The checks answer claims the seat had
already stated. There are no blind expectations here, and this card is not a preregistration. Data-free. 0 of 19.

## The claims checked (the lane's summary, and its card AGY-C59 at the lane's local commit `e4d220b75` on this machine, not yet pushed)

1. **E1:** the three trace-3 systoles of B1993's (3, 3, 3) torus are conjugate to m004's LR, cycled by B1994's LR⁻¹; "all
   three of them are m004".
2. **E2:** after 12 steps of LR at the golden point, the up sector's Yukawa returns with a primitive fifth root of unity, and
   the down and lepton sectors with 1. This is said to force the ±R_σ fold.
3. **E3a:** summing the two halves forces J = 0; clockwise and counterclockwise give the same CP-even outputs and opposite J.
4. **E4:** a "zero-parameter" 21 × 21 linear boundary-Dirac matrix "replaces the discrete product rule". It gives steep
   hierarchies, CKM alignment and |J| ≈ 10⁻³, on the "(a₅/5) = +1, wall v₀" chain.

## The checks

- **E1:** U = LR, V = L⁻¹R⁻¹ and (UV)⁻¹, checked in this conversation (sympy); the result is recorded on the page.
- **E4, the construction** (`schur_identity.py`, main's own code): the Schur complement of the seat's 21 × 21 matrix against
  the ordered product of its seven diagonal blocks, for random blocks and for three step sizes.
- **E2, E3a and E4's response to its choices** (`check_c59.py`; frame C's Yukawas come from the seat's sealed function, run
  by the ruling of 2026-11-24):
  - (0) main's driver against the seat's sealed output, on all 8 chains;
  - (1) the chain length K from 1 to 11;
  - (2) all 96 starting sheets at K = 7;
  - (3) the 12-turn phases;
  - (4) clockwise against counterclockwise at every mirror wall.

## What it means

- **This settles which of the four claims are mathematics and which are readings or choices.**
- **Nothing is compared with data.** The outputs are reported as how they respond to the declared choices, never as how close
  they come to anything.
