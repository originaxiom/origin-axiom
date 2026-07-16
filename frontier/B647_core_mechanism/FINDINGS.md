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

---

## Cell 2 (prereg d3e4faad) — THE ANOMALY CHARACTERIZATION

`b647_chain_swap.py` → `b647_cell2_output.txt` (weld-none double; the
banked machinery unmodified; J = U₂₇∘conj per B638).

**M2-G1 verdict: the structured middle** (stronger than either prereg
branch): on the three lawful triples (1,3,4), (0,2,3), (1,2,3) the
swap is CHAIN-LEVEL EXACT in seven of the eight evaluation slots —
both forward transports and rev(μ,λ) — and the entire invariant
concentrates in the single remaining slot:

> **THE DEFECT LAW: S₂(J·z₁; λ,μ) − conj S₁(z₁; λ,μ) = 2·conj(Y)**
> exactly, on all three lawful triples (sympy re-verification in the
> lock). Equivalently: **Y = ½·conj(the swap's chain anomaly)** — the
> chord's cubic IS the obstruction to chain-level swap equivariance,
> localized in one certificate.

Consistency both ways: (i) fwd-exactness + the defect law DERIVES the
banked cohomological law Y∘σ* = conj(Y) (three-line computation in
the lock's comments); (ii) on the dial triple (2,3,4) no single slot
is exact, but the four defects satisfy exactly the forced combination
(dA₁−dA₂) − (dR₁−dR₂) = 2·conj(Y[234]) — verified exactly.

**M2-G2 routing:** the phase question (arg Y[134] = π/6, cell 1's
reduction) now targets ONE object: the homotopy content of the side-2
(λ,μ) certificate. Cell 3 (registered): expand that certificate's
H₂-correction chain and extract the phase — the anomaly
characterization makes the cubic exactly the kind of chain-level
object a reality structure can pin.

Two in-run notes: the first launch hit the sides_of pair structure
(fixed, trail in-place); the first lock draft hit sympy's √−3
normalization (I·√3 internally — subs-based conjugation silently
no-ops; use sp.conjugate; an E-class candidate for tooling notes).
