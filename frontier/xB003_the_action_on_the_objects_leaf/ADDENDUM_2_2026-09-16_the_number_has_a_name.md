# xB003 — ADDENDUM 2 (2026-09-16): the multiplier has a name, the record already gave it one, and fence (2) of this arc is CORRECTED

## The correction, first

This arc's fence (2) reads: *"`ℚ(√21)` is UN-INTERPRETED… Recorded as a computed number awaiting a
reason."* **That is wrong, and it is corrected here.** The number was interpreted in this record on
**B425**, which computed, by Fox calculus at `ρ_geo`:

> **adjoint polynomial `(t−1)(t²−5t+1)/t³`, roots in `ℚ(√21)` (3-governed)**

i.e. the **adjoint twisted Alexander polynomial** of the figure-eight knot. Our `(5 ± √21)/2` are
its roots. The number is a named knot invariant and has been since B425.

## What this addendum adds: a second, independent route

The two computations share **no code, no method and no coordinates**:

| | B425 | xB003 |
|---|---|---|
| object | twisted Alexander polynomial | derivative of the monodromy action |
| method | Fox calculus on the knot group | fixed point on the character variety |
| where | at `ρ_geo`, `ρ(a)=[[1,1],[0,1]]`, `ρ(b)=[[1,0],[−ω,1]]` | on the leaf `κ = −2`, at `(2+ω̄, 2+ω, 2+ω)` |
| result | `(t−1)(t²−5t+1)/t³`, roots in `ℚ(√21)` | `(λ−1)(λ²−5λ+1)`, leaf pair `(5±√21)/2` |

**They agree**, and they must: for a fibred knot the twisted Alexander polynomial *is*
`det(t·φ_* − I)` on `H¹(fibre; Ad ρ)`, which is exactly the derivative this arc computed. So xB003
is an independent confirmation of B425 — worth having, since B425's own status line says that
invariant was *"computed here for the first time."*

## What the 5 means, in one line

> `H₁(Σ)` carries the monodromy with trace **3**. `H¹(Σ; Ad ρ)` carries it with trace **5**.
> The object's leaf multiplier is the **adjoint analogue of the homological trace**.

That is the reading fence (2) said it did not have.

## A defect this seat nearly reported, and did not — recorded so nobody else does

B425 states the Fox **determinant** as `(t−1)⁴(t²−5t+1)/t³` (line 39) and the adjoint **polynomial**
as `(t−1)(t²−5t+1)/t³` (lines 27, 73). That looks like an internal contradiction. It is not:
the twisted Alexander polynomial is the Fox determinant divided by `det Φ(b−1)`, and the meridian
is parabolic, so `Ad(ρ(b))` is unipotent with all eigenvalues 1 and
`det(t·Ad(ρ(b)) − I) = (t−1)³` — **verified here**. `(t−1)⁴/(t−1)³ = (t−1)`. **B425 is internally
consistent** and nothing is owed against it.

## And the split ADDENDUM 1 left open is now named, not mysterious

ADDENDUM 1 observed that `LR`, `LLR`, `LLRR` give integer derivative traces while `LLLR`, `LLLLR`,
`LLRLR` give irrational sets, and flagged it as the next question. Under the identification it is
**the factorisation over `ℚ` of that bundle's own adjoint twisted Alexander polynomial** — an
ordinary question about a standard invariant, with no object-specific content implied. Named,
and closed as a mystery.

## Standing

ADDENDUM 1's result is untouched: the multiplier is **not** a function of `tr(M)` (`LLRR` and
`LLLLR` share trace 6 and differ), so it carries information beyond the homology class. What
changes here is only that the information has a name. The `21 = 3·7` / `77 = 7·11` resemblance to
`ℚ(√77)` and `disc K` stays **declined** — B425 already reads the 21 as 3-governed, which is the
reading, and nothing licenses carrying it to the `E₆` layer.
