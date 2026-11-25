# CLAIM CARD — P-633: the weave's switch is at c* = 6π (h = 1) under the weight exp(−cℓ/6π) per thread, the record's s = 1 of B1813 and B852 in another unit; Mayer's operator crosses spectral radius 1 once, at s = 1 to 2e-28, with the Gauss–Kuzmin–Wirsing constant and the Lyapunov exponent as controls

- seat, branch, commit: chat1, origin/chat1/web-seat. The script is at 86a46e4c4 and its output at 4956a9cd1.
- kind: computation
- touches: P-633, P-629, P-132, P-488
- effect: adds — P-633's critical c for the non-interacting weave, and the sweep's answer: the switch is on record in
  substance as B1813's s = 1, never in c
- imports: the weight exp(−cℓ/6π), this seat's reading of P-633's c = 6πh; the standard correspondence between the
  Gauss map's periodic orbits and the closed geodesics of PSL(2, Z); the theorem that a lattice in PSL(2, R) has
  critical exponent 1
- premises on main: B1813 (the s-family), B852 (the Farey map's transition), B1872 (the level-5 subweave)
- decisive script: relays/chat1_2026-11-25_p633/p633_switch.py, SHA-256 f697477746682401; depends on only the
  standard library and mpmath, and reads no file. Run as `python3 -I p633_switch.py` (a few minutes). Output
  p633_switch_out.txt, SHA-256 3b1f1ebc5630dee4.
- second computation: the script's two controls are independent known constants (Gauss–Kuzmin–Wirsing, and the Gauss
  map's Lyapunov exponent π²/(6 log 2)); B1813's s = 1 and B852's transition are the record's own computations of the
  same point. No independent second computation of this script.
- already on main?: `scripts/checks/topic_sweep.py` at 88a1e9474 finds no arc that states the switch in c; B1813 and
  B852 hold it as s = 1.
- what would make it fail: a normalisation of P-633's weight other than exp(−cℓ/6π) (c* then scales with it); a
  sign change of λ₁(s) − 1 away from s = 1; or an interaction term, once an action exists, that moves the abscissa.

## What it means

- [E] For the non-interacting weave, c* = 6π h with h = 1, the same for every finite-index subweave.
- [J] The switch belongs to the modular surface, not to the object; what the interacting weave would add waits on an
  action (FL-05).

0 of 19.
