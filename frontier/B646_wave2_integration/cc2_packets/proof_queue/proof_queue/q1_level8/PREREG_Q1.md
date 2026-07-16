# Q1 — E6 LEVEL 8 (kappa = 20): THE TRIPLE-PREDICTION CELL (sealed; cc2, 2026-07-16)

One build adjudicates THREE independent sealed laws simultaneously — each prediction
was banked and DELIVERED before this cell was opened:

- P-Q1-a (the resonance model; jeffrey_extension.json, packet sha 52005c8c):
  **Z_8 = +1** exactly (sector split not predicted — bank blind).
- P-Q1-b (the clock law; ADDENDUM_N2.md seal 09fc3565): **clock = ord(B_odd) = 60**,
  equality (ord(T_8) = 60 = 2^2*3*5; kill set empty: 5 inert, 3 shallow;
  ord(A1 mod 60) = 60). First predicted clock exceeding 36.
- P-Q1-c (the splitting law, third inert-prime test; law banked via B600/R1):
  kappa = 20 carries odd prime 5 === 2 (mod 3) INERT in Q(sqrt-3) => a REAL-QUADRATIC
  Q(sqrt5) import in the odd-block magnitude minpolys (as at kappa=15). A sqrt-p
  import for p not in {2, 5} REFUTES the law's typing; NO import is outcome-B
  (law survives only if 5-content appears in another inert form — flag for analysis).

Formula-determined constants (MB12 guard, part of this seal): N = 372, theta-fixed 32,
dim_odd 170, dim_even 202; ord(T_8) = 60; zeta order for S: 6K = 120; exact-Z
certificate mod Phi_240.

Falsifier structure: the three laws are INDEPENDENT — any subset can die here.
Z_8 != +1 kills the resonance model (and with it the six-rung bank); clock != 60
kills the k>=3 clock law (60 is also the first non-{12,18,36,60}-ambiguous value:
any proper divisor cannot be confused with the k=3 rung's 60); wrong-field import
kills the splitting law's inert typing.

Procedure: the B600 engine unchanged; banked-rung gates k = 1..7 reproduced in-run
(hard stop; k=7 gate = (231, 105, Z=2.0, ord=36)); BLIND BANK level8_readouts.json +
npz BEFORE any comparison; certificates: exact-Z zero-poly / value mod Phi_240,
Tr(Theta rho) exact, ord(B_odd) mp-certified at dps 50 incl. proper divisors,
magnitude minpolys <= deg 16 with disc factorization, even-sector control.
Runner verification per the L6 lesson: `grep "Level(8" level8_run.py` before launch.
Runtime estimate: counts ~2.6x level 7; mp odd block 170-dim — background, hours.
