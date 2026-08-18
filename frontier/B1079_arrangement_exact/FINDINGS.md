# B1079 — the rung arrangement EXACT over ℚ: B1078's residue closed, and the 64 Levis deposited

**Date:** 2026-08-18 · **Seat:** cc3 (audit) · **Lane:** MATHEMATICS. **Gate 5:** no physical
identification. **Verdict: PROVED**, exact over ℚ throughout — no primes, no numerics, no sympy.
Reproducer `arrangement_exact.py`. **Not preregistered**; the controls are falsifiable by things
this arc did not choose.

## What this closes

B1078 proved the paper's eleven-element rung bound is **tight**, and registered one residue: the
flat enumeration was exhaustive at **three faithful primes**, not a characteristic-zero
certificate, since reduction mod `p` can only *add* linear dependencies among weights.

**That residue is now closed**, by a construction sharing no code path with B1078.

## Where the route came from — and the rule that applies

The opening is **cc's no-moduli theorem** (B874 addendum, 2026-08-18):

> `dim C = 4` with `dim z(C) = 12` forces `|Φ ∩ C^⊥| = 6` with `C^⊥` two-dimensional; the only
> rank-≤2 root system with 6 roots is `A₂`; and all such subsystems lie in one `W`-orbit — so the
> stratification is **unique up to conjugacy**.

`WORKING_RULES` §2/§12 forbid banking a cross-seat claim by citation. **It is reproduced here**,
in-sandbox: the `A₂`-uniqueness among rank-≤2 systems (A₁:2, A₁×A₁:4, **A₂:6**, B₂:8, G₂:12), the
6 roots vanishing on `C`, and the 4-dimensional `C = (A₂)^⊥`. Nothing is imported and nothing is
merged; cc's locks stay on cc's branch.

## The consequence

The weights of `C` on `e₆` are just **the 72 roots of E₆ restricted to `C`**. Six restrict to
zero — giving `dim z(C) = 6 + 6 = 12` — and the other **66 = 72 − 6** form the arrangement, as
**30 distinct weights with profile 12×1 + 18×3**.

**That profile is exactly what B1078 computed from the charges**, through `ad`-matrices, an exact
ℚ characteristic-polynomial factorisation, and three primes. Neither route can see the other's code.

Every vector here is **rational**, so the arrangement is defined over ℚ, linear dependence among
rational vectors is unchanged by any characteristic-zero extension, and **the ℚ-enumeration is the
ℚ̄-enumeration**. The 109 flats and the eleven values

```
  {12, 14, 16, 18, 20, 26, 28, 30, 36, 46, 78}
```

are now exact. `dim z(S) = 14` is attained at 3-dimensional `S`, over ℚ̄, unconditionally.

## The nuance that reconciles this with the 46

The arrangement is rational; **the charge basis's position relative to it is not.** A flat that is
rational in root coordinates is a subspace the coordinates `x₈, x₁₄, x₁₆, x₂₂` reach only after
base change to `K`. So B1078's `(8,16)`-plane cubic being **irreducible over ℚ** and the lattice
being **rational** are statements about two different coordinate systems, and do not conflict.

## The 64 Levi subsystems — campaign item 3, deposited

| subsets | roots | dim | type(s) |
|---|---|---|---|
| 1 | 0 | 6 | — | 
| 6 | 2 | 8 | `A₁` |
| 10 | 4 | 10 | `2A₁` |
| 10 | 6 | **12** | `A₂` **or** `3A₁` |
| 10 | 8 | 14 | `A₂+A₁` |
| 5 | 10 | 16 | `2A₁+A₂` |
| 6 | 12 | **18** | `A₃` **or** `2A₂` |
| 5 | 14 | **20** | `A₃+A₁` **or** `2A₂+A₁` |
| 4 | 20 | 26 | `A₄` |
| 2 | 22 | 28 | `A₄+A₁` |
| 1 | 24 | 30 | `D₄` |
| 1 | 30 | 36 | `A₅` |
| 2 | 40 | 46 | `D₅` |
| 1 | 72 | 78 | `E₆` |

Root counts `0,2,4,6,8,10,12,14,20,22,24,30,40,72`; the fourteen ambient dimensions; **24 is not a
Levi dimension**; **26 is realized by exactly four `A₄` node-subsets** — matching cc's bench run,
reproduced here independently. **Exactly three dimensions carry two types — 12, 18, 20** — which
is `rem:leviscope`'s claim, and the four counts the paper leans on (`46→40→D₅`, `30→24→D₄`,
`26→20→A₄`, `14→8→A₂+A₁`) are each unambiguous.

## SCOPE

Exact over ℚ, needing no primes and no numerics. **Not claimed:** anything about the member, the
class, the sisters, the rows, or any real form. **The real-point question is a different one and
is untouched** — cc's addendum shows reality kills 14, 20 and 26 over ℝ, and nothing here
contradicts or supersedes that.
