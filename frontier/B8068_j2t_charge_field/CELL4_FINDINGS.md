# B8068 CELL 4 — the object's invariants are SPINOR-FREE, and that is the reason it stops

**Date:** 2026-08-17 · **Seat:** cc3 · **Gate 5:** algebra only.

## THE STATEMENT

Under any of the three `so(10)`s the object produces (cell 3), the 27 decomposes as
`16 ⊕ 10 ⊕ 1`. Every one of the object's canonical rank-1 invariants lands in `10 ⊕ 1`:

> **the 16-component of every one of them is identically zero.**

`SO(10) → SU(5)` requires a **16** VEV — a spinor. **The object supplies nothing in the
16 at all.** Not an impure spinor, not a small component: zero.

This converts cell 3's exhaustive observation ("`su(5)` appears in none of the 63
subsets") into a **reason**. The step the object cannot take needs precisely the
representation in which it has no elements.

## GATES

| gate | result |
|---|---|
| control: generic `27 × 27-bar` reproduces `dim 45, Killing rank 24 = su(5)` | **PASS** — the instrument can see `su(5)` |
| the so(10) trace form on the 27 is nondegenerate (rank 45/45) | **PASS** |
| Casimir eigenvalue multiplicities on the 27 | **{1, 10, 16}** exactly |
| **the defining invariant lands purely in the singlet** | **PASS** — `e₁` has zero `10`- and `16`-parts |
| all three `so(10)`s, primes 1093 and 1097 | **identical** |

The fourth gate is the one that makes the result trustworthy: the invariant that *defines*
the `so(10)` is annihilated by it, so it **must** be the singlet, and it is. That proves
the projector is correct before any new number is read from it.

## THE SHAPE OF THE WHOLE RESULT

| step | status |
|---|---|
| `E₆ → SO(10)` | **reached**, canonically, from the object's own invariants, **with chirality intact** (`D₅`, `n` odd, `−1 ∉ W`, so the **16** and **16-bar** are distinct) |
| `SO(10) → SU(5)` | **blocked**, and now by theorem: the object has no spinor |

The object is **vector-like with respect to the `so(10)` it produces.** It builds the
group under which chirality is possible, and supplies no element of the chiral
representation.

## LIMITS

- Types identified by dimension plus Killing rank plus, for the 45, the fact that
  `so(10)` is the only simple algebra of dimension 45 with rank ≤ 6. Not a
  structure-constant identification.
- Mod-p rank over-estimates nullity; two agreeing primes and three independent `so(10)`s
  make an artefact unlikely without excluding it.
- Novelty **not** claimed; no literature sweep run.
- **What is NOT shown:** that no construction whatever reaches the 16. Only that the
  object's *canonical rank-1 invariants* have no component there.
