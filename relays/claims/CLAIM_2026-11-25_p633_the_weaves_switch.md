# CLAIM CARD — P-633: read as a weight exp(−cℓ/6π) per thread, under which c = 6πh is the abscissa by construction, the weave's critical c is 6π because δ = h = 1 under the geometric clock (6π log 2 under B1813's move clock); Mayer's operator, whose spectral radius crosses 1 at s = 1, confirms δ = 1 with the Gauss–Kuzmin–Wirsing constant and the Lyapunov exponent as controls; no arc states the switch in c, and B1813's s = 1 shares the point, not the phases

- seat, branch, commit: chat1, origin/chat1/web-seat. The script is at 86a46e4c4 and its output at 4956a9cd1; the relay
  and this card were corrected after their referee read.
- kind: computation
- touches: P-633, P-629
- effect: adds — P-633's critical c for the non-interacting weave under a stated reading and clock, and the sweep's
  answer: no arc states the switch in c; B1813 and B852 hold the same critical value in a fixed-word-length ensemble
- imports:
  - the reading of P-633's c as a new coupling, a weight per unit thread length exp(−cℓ/6π), not P-488's c or P-132's
    coefficient;
  - the clock: geometric length (h = 1); under B1813's move clock h = log 2;
  - the standard coding of PSL(2, Z)'s closed geodesics by the Gauss map's periodic orbits (two to one on mirror
    pairs), and the theorem that a lattice in PSL(2, R) has critical exponent 1.
- premises on main: B1813 (the s-family and its two clocks), B1814 (the critical clock), B852 (the Farey map's
  transition), B1872 (the level-5 subweave)
- decisive script: relays/chat1_2026-11-25_p633/p633_switch.py, SHA-256 f697477746682401; depends on only the
  standard library and mpmath, and reads no file. Run as `python3 -I p633_switch.py` (about 1.5 minutes). Output
  p633_switch_out.txt, SHA-256 3b1f1ebc5630dee4.
- second computation: the referee reran the script identically, and reproduced the operator's values in a second basis
  (a power series about x = 1, 160 digits) to 12 digits on the grid. The controls are independent known constants.
- already on main?: `scripts/checks/topic_sweep.py` at 88a1e9474, on main's tree, finds no arc that states a switch
  between phases in c; B1814 matches "the critical clock" (B1813's counting rule at s = 1).
- what would make it fail: a reading of P-633's c other than a weight per unit length (c* then scales with it); a clock
  other than the geometric one (under the move clock c* = 6π log 2); or an interaction term, once an action exists, that
  moves the abscissa.

## What it means

- [E] δ = h = 1 under the geometric clock, for the modular surface and every finite-index subweave. Under the stated
  reading, c* = 6π.
- [J] The switch belongs to curvature −1, not to the object; what the interacting weave would add waits on an action
  (FL-05).

0 of 19.
