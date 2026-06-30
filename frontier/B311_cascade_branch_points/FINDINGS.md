# B311 — The cascade's object-specific core is the trinification branch point (only); the chain is not realized on the curve

**Status: banked (frontier). Verify-don't-trust on Chat-2's proposed extension to B306/B310; refines B310. Nothing to
`CLAIMS.md`.** Chat-2 (after honestly retracting its own "mislabel" flag) offered the last in-sandbox piece of the
cascade question: *u = 2πi/3 (M = e^{iπ/3}) and u = πi (M = i) are special points on the figure-eight's A-polynomial —
compute the E₆ centralizer there and the deformation realization closes.* I ran it. **The branch-point claim is true;
the realization does not close — and the computation caught what the "just compute the centralizer" optimism missed.**

## What the A-polynomial actually says
The figure-eight geometric A-polynomial component is `A(M,L) = M⁴L² − (M⁸−M⁶−2M⁴−M²+1)L + M⁴` (the coefficient sign is
fixed by the complete-structure check: at `M=1`, `A = (L+1)²`, so the geometric longitude is `L=−1`, the *abelian* line
is `L=1`). Its discriminant in `L`, in `x = M²`, factors **exactly**:

```
Disc(x) = (x−1)² (x+1)² (x²−3x+1) (x²+x+1)
                        [GOLDEN]   [EISENSTEIN]
```
- `x²+x+1 → x = ω, ω²` — the **ℚ(√−3) (Eisenstein)** end.
- `x²−3x+1 → x = φ², φ⁻²` — the **ℚ(√5) (golden)** end.

So the program's **two arithmetic ends sit in one figure-eight discriminant** — a genuine object-specific fact,
consistent with the banked two-ended theme.

## The cascade grading points, and the catch
Via the principal lift (the E₆ meridian holonomy acts on a height-`h` root with eigenvalue `M^{2h}`; the centralizer is
`{h ≡ 0 mod N}` when `M^{2h}=1`):

| step | `M` | `x=M²` | branch point? | `L_double` | rep |
|---|---|---|---|---|---|
| N=2  (SU(6)×SU(2)) | `i` | `−1` | **yes** | `+1` | **reducible (abelian)** |
| N=3  (trinification) | `e^{iπ/3}` | `ω` | **yes** | `−1` | **irreducible (geometric)** |
| N≥4 | `e^{iπ/N}` | `i, …` | **no** | — | not on the curve |

**The catch Chat-2's optimism missed:** the *first* cascade step (N=2, SU(6)×SU(2)) lands on the **reducible (abelian)
locus `L=1`** — not a genuine irreducible E₆ flat connection — and N≥4 are **not branch points at all**. The grading
points are **isolated** branch points, the first one reducible. So this is **not a connected deformation realizing the
chain**. The *only* cascade step sitting at a genuine **irreducible** object-specific branch point is the
**trinification (N=3, `M=e^{iπ/3}`, Eisenstein, same `L=−1` as the complete structure).**

## Verdict
- **Chat-2's branch-point claim is verified** (both points are branch points of the figure-eight's own A-polynomial).
- **It does not close the deformation realization** — N=2 is reducible, N≥4 are off the curve; the points are isolated.
- **It refines B310.** B310's "no new object-specific content beyond the banked ω" was slightly too strong: there *is*
  object-specific content — the trinification is **character-variety-special** (an irreducible A-poly branch point),
  which **upgrades B305 from arithmetic-eigenvalue to character-variety relevance**, and the two arithmetic ends live in
  one discriminant. But that content is **one step (trinification)**, exactly the object connection B305/B310 already
  named — *not* the full cascade.
- **The full physical realization of the chain remains the `T[4₁;E₆]` CRUX** (specialist).

## The honest reading
This is the multi-seat discipline working in *both* directions: Chat-2 was right that there was an in-sandbox
computation B310 skipped, and running it found a real object-specific fact (the trinification is an irreducible branch
point; the two ends in one discriminant). But the same computation **refutes the stronger hope** — the cascade is *not*
realized as a breaking on the figure-eight's curve, because its first step is reducible and its higher steps are not on
the curve at all. The object-specific core of the cascade is, once again, exactly the **trinification step** (B305) —
now with a stronger certificate (an irreducible branch point, not just an eigenvalue coincidence). Everything past that
one step stays the CRUX.

## The fence
Pure symbolic A-polynomial algebra (sympy) + the principal-lift centralizer rule + the complete-structure sign check.
The "physical gauge dynamics" reading is the CRUX, firewalled. Nothing to `CLAIMS.md`.

`cascade_branch_points.py` (pyenv) · `tests/test_b311_cascade_branch_points.py`. Related: `B310` (the cascade
exhaustion — refined here), `B305`/`B306` (the cascade; the trinification ω — strengthened here), `B285` (the Eisenstein
`ω` Riley root), the two-ended object (Eisenstein/golden — now both in one discriminant), `B281` (the CRUX). Lit:
Cooper–Culler–Gillet–Long–Shalen (the figure-eight A-polynomial); Slansky (1981, the E₆ chain).
