# xB004 — PREREGISTRATION (sealed BEFORE any computation of this arc)

**Seat `xb`, branch `sep16-branch`, 2026-09-16. This is the first design of this seat sealed in
the correct order: written, hashed and committed before the cells run. The hash is recorded in
`ARTIFACT_HASHES.txt` in the same commit as this file and BEFORE the commit that adds any result.
Chronology here is checkable from the git history of this branch, which is the thing xB001 found
the record's other seals cannot support.**

## P0 — the quantifier, stated before computing

This computes on the **trace map's character variety of the fibre**, at the object's own fixed
point on the leaf `κ = −2`. It is **not** a 4d Lorentzian field action; TOE row 4 asks for one and
this is not it. Gate 5 absolute: no measured quantity enters any cell.

## Background (all banked, none re-derived here)

* **B6/P15/P16** built a potential by: take `A = [[2,1],[1,1]]`, form `log A`, read off the Möbius
  vector field `v(τ) = b + (a−d)τ − cτ²` on `H`, integrate to `V(τ) = κ(τ³/3 − τ²/2 − τ)`.
  Its stationary points are `φ`, `−1/φ`.
* **B7/B8/B9** stand on that `V`: a Fisher–KPP front, `mass² = V''(φ) = κ√5 ≈ 1.924847`, and a
  cubic vertex `κ/3`.
* **xB003 ADDENDUM 4** verified that `φ`, `−1/φ` are the Möbius fixed points of `A`, which is
  hyperbolic (`|tr| = 3 > 2`), so they lie on `∂H` — ideal boundary points, not points of the
  moduli space. B6 itself lists "τ as a field rather than a coordinate on `H`" as inserted.
* **xB003** located the object's own point: the fixed point of the monodromy on `κ = −2`, traces
  `(2+ω̄, 2+ω, 2+ω)`, minimal polynomial `x²−3x+3` (disc −3), where the derivative on the leaf is
  symplectic with char poly `λ² − 5λ + 1`.

## The question

**Run B6's own recipe at the object's point instead of at the boundary, and report what B7/B8/B9
become.** B6 integrates the vector field of `log` of the matrix that acts. At the object's point
the acting object is the monodromy's derivative on the leaf, `D`, a real-trace-5 symplectic 2×2.

## Cells and two-outcome criteria — declared before running

| cell | question | PASS | FAIL |
|---|---|---|---|
| **C1** | is B6's recipe well defined at the object's point? | `log D` exists (D has no non-positive real eigenvalue) and yields a definite quadratic form | it does not — the recipe does not transport, and that is the finding |
| **C2** | is the leading potential there **quadratic**, where B6's is **cubic**? | leading term exactly quadratic, first non-quadratic order computed and reported | a cubic appears at leading order |
| **C3** | the mass² analogue | computed exactly and compared with B8's `κ√5 ≈ 1.924847`; **either outcome is reported**, equality is not expected | — |
| **C4** | does B9's cubic vertex have an analogue? | the cubic coefficient of the normal form at the fixed point is computed; **zero and non-zero are both informative and both reported** | — |

Each cell asserts its own mathematics and can fail on the instance (WORKING_RULES §7, §8).

## Declared prior (so the arc can overrule it)

This seat expects **C2 PASS** — the generating function at an interior fixed point is quadratic at
leading order, so the cubic vertex B9 rests on is an artefact of the *boundary* location, where the
Möbius field is quadratic and integrates to a cubic. It expects **C4 non-zero** (a vertex surviving
at the next order), but with low confidence; a vanishing cubic would be the more interesting
outcome and is named here in advance as the answer that would NOT be convenient.

## Conventions declared (WORKING_RULES §4)

* Full traces `(X,Y,Z)`, `κ = X²+Y²+Z²−XYZ−2`; the object's leaf is `κ = −2`.
* The monodromy trace map is `F_L ∘ F_R` (xB003 cell 2, the literature presentation).
* `D` = the derivative restricted to the leaf's tangent at the fixed point; the transverse
  eigenvalue 1 is dropped.
* Principal branch of `log` on the symplectic block; the branch is stated with the result.
* `ω = (−1+√−3)/2`.

## Scope

Dynamics layer. No value, no generation count, no physics reading. Nothing promotes to `CLAIMS.md`.
