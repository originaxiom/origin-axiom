# xB003 — DESIGN (seal POST-HOC; labelled, per WORKING_RULES §3)

**Provenance, stated first.** The computations ran during a working session before this file was
written. Labelled post-hoc; the seal certifies integrity, never chronology. **One partial
exception, recorded because it is the only honest part:** the cell-1/cell-2 criterion (*"is T²
literally the monodromy, or some other element of the trace-map group?"*) was stated as a
two-outcome question, in advance and in writing, before it was computed — but it was not hashed,
so it is a stated criterion, not a pre-registration.

## Purpose

B1341 proved that the object's half-tick is anti-variational and that the **double** tick admits a
discrete Lagrangian, then found the explicit generating function `S(u,U) = u²/2 − uU + U²` only on
the leaf `I = 0` (`κ = +2`) and recorded, with its own check, that **the object is not on that
leaf** (`κ = −2`, `I = −1`) and that the explicit `S` does not apply there. This arc attempts that
named gap.

## Two-outcome criteria, declared

| cell | criterion | PASS | FAIL |
|---|---|---|---|
| 1 | is `T²` the monodromy? | `T² = F_R ∘ F_L` identically, twists preserving κ, abelianisation trace 3 | any mismatch — B1341's "double tick" would not be the monodromy and nothing downstream may be read as the object's |
| 2 | independent route | the literature presentation `φ(a)=ab, φ(b)=bab` induces `F_L ∘ F_R` | disagreement — one of the two derivations is wrong |
| 3 | fixed points on `κ = −2` | node + a conjugate pair; the pair's traces have norm 3 and lie in `Z[ω]` | anything else |
| 4 | derivative at the pair | eigenvalue 1 transverse, a symplectic pair of product 1 | product ≠ 1 — no action there, contradicting B1341 |

Every cell asserts its own mathematics and fails on the instance if the mathematics differs
(WORKING_RULES §7, §8): cell 3 fails if the norms are not 3 or the traces leave `Z[ω]`, cell 4
fails if the multipliers do not multiply to 1.

## Conventions declared (WORKING_RULES §4)

- **Coordinates.** Full traces `(X,Y,Z) = (tr a, tr b, tr ab)` on the `SL(2,ℂ)` character variety
  of the once-punctured torus. B1341's half-traces are `x = X/2`; the invariants relate as
  `I = (κ−2)/4`, so `κ = +2 ↔ I = 0` and `κ = −2 ↔ I = −1`.
- **κ.** `κ = tr[a,b] = X²+Y²+Z²−XYZ−2` (Fricke; re-derived from explicit `SL(2)` matrices, not
  quoted).
- **The leaf.** A level set of κ. The object's is `κ = −2` because its cusp makes the fibre's
  boundary commutator parabolic.
- **`ω = (−1+√−3)/2`**, so `Z[ω]` is the ring of integers of `ℚ(√−3)`.
- Conjugacy-invariant quantities only: the eigenvalues of the derivative are basis-independent.

## Scope

Dynamics layer, on the trace map. **Not** a 4d Lorentzian field action — TOE-ledger row 4 asks for
one and this is not it, exactly as B1341's own P0 scoped it. Gate 5 untouched: no measured
quantity enters. No value, no generation count, no physics reading.
