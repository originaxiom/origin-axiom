# B658 — THE ORDER-4 FLIP VERDICT: both families BROKEN; wall 8 is total
# (main seat, 2026-07-17; prereg 0c4a1115 sealed first; R21-6 closed)

**Both order-4 orientation-reversing families of Isom(4₁) = D₄ break on
the weld double's 27 local system — with the SAME singular intertwiner
as the order-2 classes: solution dimension 1, d = (0, 0, 1), supported
on Sym⁰ alone, no invertible member.**

The run (b658_order4.py → b658_output.txt, exact over ℚ(√−3), zero
floats):
- Control: the a-family reproduces its banked singular d = (0,0,1) ✓.
- φ(a) = A, b ↦ bAB (U = [[−1, ζ̄₆],[0,1]], det −1, PGL-valid lift):
  peripheral signature (w, s, t) = ('', −1, +1) — it inverts the
  meridian with the EMPTY conjugator and fixes the longitude class.
  Block-scalar system: 172 off-diagonal conditions, solution dim 1,
  **d = (0, 0, 1) — BROKEN.**
- φ(a) = B, b ↦ aBA (U = [[0,1],[−ζ₆,1]], det ζ₆): peripheral
  signature (w, s, t) = ('aBAb', −1, +1). Same system:
  **d = (0, 0, 1) — BROKEN.**
- Inner corrections cannot rescue either class (B643's Ad(w) argument:
  composition multiplies the intertwiner space by ρ(w), preserving
  (non)invertibility) — the obstruction covers both full outer classes.

## THE WALL-8 UPGRADE (the total statement)

> **The chord breaks every orientation-reversing symmetry of the
> object.** All FOUR orientation-reversing families of D₄ (two order-2
> flips, two order-4 elements squaring to the half-longitude) admit
> exactly one partial intertwiner on the double's 27 local system,
> supported on the invariant line (Sym⁰) alone. The symmetry of the
> double's 27-cohomology is the deck swap σ* exactly.

The object is amphichiral; its chord is not — and now totally so:
coupling breaks the mirror in every form the isometry group offers,
down to the swap.

## The observation (recorded, not claimed)

All four broken families retreat to the SAME line — d = (0, 0, 1) is
supported precisely on the invariant line v₀, the object of B657's
portal law. The one direction every broken mirror symmetry still
preserves is the one direction that couples to everything (rank-5
isomorphism). Whether "the broken symmetries' common fixed line = the
portal's source" has mechanism content is registered as a HINT, not
banked as a law.

Artifacts: PREREGISTRATION.md (0c4a1115, sealed before compute),
b658_order4.py, b658_output.txt. Locks: tests/test_b658_order4.py.
R21-6 closes; LAW_MAP wall 8 upgraded in the same PR.
