# B647 — the core-law mechanism hunt (R20-5/R20-6; cell 1 banked)

**The question (R20-5):** what forces Y[023] = 24ζ₆·Y[123]? B643 proved
no flip symmetry exists to force it; B638's swap law alone leaves 10
real dimensions. Cell 1 sharpens the reduction.

## Cell 1 — swap law + zero law: NOT sufficient, but the residuals collapse

`b647_ratio_forced.py` (exact sympy over ℚ(√−3)): impose Y∘σ* = conj(Y)
(the banked σ*-matrix) AND the zero law (Y[012] = Y[013] = Y[014] =
Y[024] = 0, the silent-class pattern). Result:

- the constrained solution space has **real dimension 6** (down from 10);
- the core ratio is **NOT forced** — its residual is ONE ℝ-linear
  condition among the six frees;
- the spectator extension's residual FACTORS:
  Y[034] − 24ζ₆·Y[134] = 4(3+√3i)·(3b₁₃₄ − a₁₃₄) — so given swap+zero,
  **the B645 spectator law ⟺ arg Y[134] = π/6** (the a = 3b locus), and
  the banked value 1/24 + (1/72)√−3 sits EXACTLY on it.

## What this changes

The mechanism question reduces from "why the 24ζ₆ ratio" to "what
cochain-level structure pins two phase/linear conditions" (one for the
core slot pair, one single-slot phase for the spectator pair). Phase
conditions are exactly what a reality/positivity structure on the
cochain complex (e.g. a B_θ-type pairing on H¹(D;27), or the swap's
real structure applied at the chain level rather than cohomology) can
force. Cell 2 (registered, not run): compute the swap's action at the
CHAIN level on the specific certificate chains behind Y's evaluation
and check whether the π/6 phase is a chain-level identity.

No SM numbers; internal exact algebra; the arc continues under R20-5/6.
