# B89 — M⁴ = L PROVED symbolic-exact at SL(4) (Task 1a)

**Status: PROVED (exact, over ℚ(ω)).** Upgrades V54 / B73 from `high-precision-numerical` (~1e-31)
to a symbolic-exact theorem — the SL(4) analogue of B71's exact SL(3) `M³ = L`.

## The claim
On the principal figure-eight Dehn-filling component `A = diag(1,1,ω,ω²)` (`ω = e^{2πi/3}`,
char `(z−1)²(z²+z+1)`, `tr A = tr A⁻¹ = 1`), the longitude `L = [A,B]` is the **rank-th power** of the
genuine meridian `μ = A⁻¹t` (V46):

```
        [A,B] = c · μ⁴ ,   c = −1/det t   ⟹   on SL(4) (det t = 1):  M⁴ = L,  c = −1,  c⁴ = 1.
```

## How it is proved (no numerics in the proof)
1. **Reduction to one equation.** Eliminating `B = A⁻²tAt⁻¹` from the bundle relations
   `tAt⁻¹=A²B`, `tBt⁻¹=AB` collapses them to `t A⁻² t A = A⁻¹ t A t` (validated vs B73 reps ~1e-15).
2. **The exact ideal.** Since `A³ = I` (cube-root spectrum) so `A⁻² = A`, the equation is equivalent to
   `(a_j − a_i⁻¹)·(tAt)_{ij} = 0`, i.e. `S = tAt` vanishes off the block pattern
   `{(1,1),(1,2),(2,1),(2,2),(3,4),(4,3)}` — **10 exact quadratic equations** (`probe.ideal_residuals`).
3. **The family.** The centralizer-of-`A` gauge normalizes the `Q = t[0:2,2:4]` block to `I₂` (dense
   slice). The `det t ≠ 0` reps live on the **rank-drop locus `t11 = ω·t22`**, on which the R-block
   carries one free parameter `s`. This gives an explicit **4-parameter family** `(t12,t21,t22,s)` over
   ℚ(ω) — `det t` a genuine nonzero polynomial, every B73 numerical rep gauging into it.
4. **The identity.** Clearing inverses via `t⁻¹ = adj(t)/det(t)`, the relation becomes the **pure
   polynomial matrix identity** `[A,B]·det(t)² = −det(t)·μ⁴` over ℚ(ω), verified `= 0` in every entry
   for all four parameters (`probe.m4_equals_l_identity`, <0.1 s).

## Controls & anchors (tests)
- **Degree is exactly the rank:** `M⁴=L` is scalar (~1e-14) while `M³`, `M⁵` are **not** (dev ~1) — the
  convention-independent `eig([A,B]) = eig(μ)^k` test.
- **Genuine reps:** every family member satisfies the bundle relations (~1e-15) and is irreducible
  (rank 16); `c = −1`, `c⁴ = 1`.
- **m=1 SL(2) baseline:** the figure-eight `Fix(T₁²)` end is the single geometric component (no
  Dehn-filling curve) — degree=rank starts at n=3 (B73 A0).
- **Coverage:** B73's numerical reps gauge onto the locus `t11 = ω·t22` ⇒ the family covers the
  component.

## Scope (honest)
- This proves the **principal** component (`tr A = tr A⁻¹ = 1`); the second SL(4) component
  `{prim 8th roots}` gives `M³ = L` (B88) and is not in scope here.
- `c = −1/det t` is the natural scalar; `c⁴ = 1` is automatic on `det t = 1` (det of `[A,B] = c μ⁴`).
- Uniform-in-`n` `Mⁿ = L` is **Task 1b** (B90); the tower capstone is **Task T** (B89-T). This stage is
  the exact `n = 4` rung only.

```bash
python frontier/B89_sl4_symbolic_M4L/probe.py
python -m pytest tests/test_b89_sl4_symbolic_M4L.py -q
```

No Origin-core claim; proven core P1–P16 untouched; outreach dormant.

> **Forward note (B149, V138).** B89 proves M⁴=L on a *posited* 4-parameter family. B149 (`../B149_sl4_ideal_completeness/`)
> closes the completeness question: an exhibited gauge-stratified decomposition of the defining ideal over ℚ(ω) +
> an exact-over-F_p Burnside classification show that **the only stratum carrying irreducible reps is this family
> (rank `Q=I₂`), where M⁴=L holds** — every other component of `V(I)` is reducible (MB7) or vacuous (`det t=0`). So
> B89's family is the **complete component of irreducible bundle reps** and M⁴=L is **unconditional on the irreducible
> locus** (not just the posited slice). B89's proof stands as written; B149 upgrades its scope from "on the principal
> component" to "the principal component is the irreducible locus."
