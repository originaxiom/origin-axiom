# B8088 — the menu is homogeneous, but ARITHMETICALLY: W alone gives 25 orbits, not 9

**Date:** 2026-08-19 · **Seat:** cc3 (audit) · **Verdict: PROVED.** Reproducer
`row_homogeneity.py`. Gate 5 untouched.

## The claim under test

The owner's synthesis states, attributing it to B8086: *"the ℤ/5 menu is exactly one W × Galois
orbit per row — perfectly homogeneous; no counting rule can prefer a point."*

**B8086 did not establish that.** It verified the nine rows, their counts, and that every row has
rank 6. **It never computed orbits.** *"One orbit per row"* is strictly stronger than *"one
centraliser type per row"*: a row is a **fibre of the type map**, and a fibre may be a union of
several orbits carrying the same type.

**Why the distinction is load-bearing.** A single orbit forces a **unique** invariant measure. A
union of `k` orbits admits a **(k−1)-parameter family** of invariant measures — reweight the pieces
freely. The "only object-consistent measure is uniform" step depends entirely on which is true.

## The claim HOLDS

**Nine rows, nine W × Galois orbits, one-to-one**, sizes matching B8086's banked counts exactly:
`[4320, 4320, 2160, 1728, 1440, 864, 540, 144, 108]`.

Argued, not eyeballed: each row is a **union** of W × Galois orbits (type is constant on orbits —
controlled below), and a partition into 9 parts refined by a partition into 9 parts **is the same
partition**.

## THE SHARPENING — and it changes what the claim can be used for

**Under W alone there are 25 orbits, and eight of the nine rows split:**

| row | W-orbits | | row | W-orbits |
|---|---|---|---|---|
| 4320 (A₁+A₁+A₂) | 2 × 2160 | | 1728 (A₄) | 4 × 432 |
| 4320 (A₁+A₃) | 4 × 1080 | | 864 (A₁+A₄) | 4 × 216 |
| 2160 (A₃) | **1 × 2160** ← the lone exception | | 540 (D₄) | 2 × 270 |
| 1440 (A₁+A₂+A₂) | 2 × 720 | | 144 (A₅) | 2 × 72 |
| | | | **108 (D₅)** | **4 × 27** |

**The homogeneity is arithmetic, not geometric.** The Galois action `(ℤ/5)*` is doing the work: it
fixes each vanishing set *pointwise* (scaling a pairing by a unit cannot change whether it is zero),
so it can only ever fuse **within** a row — and it does, collapsing 25 → 9.

**Therefore the uniform measure is forced only by W × Galois-invariance, not by W-invariance.**
Demanding only the Weyl symmetry leaves eight of nine rows with a 1- or 3-parameter family of
invariant measures. **The measure argument needs the arithmetic symmetry as a stated hypothesis** —
which is an improvement, because it is a condition someone can reject.

## A number explained

The external proposal's **108 = 27 × 4**, offered as an observation, is literally **four
Galois-conjugate W-orbits of size 27**.

## SCOPE

The W-action on the 5-torsion of the `E₆` torus. Establishes homogeneity of the rows, hence
uniqueness of the invariant measure **on each row and only for W × Galois**. Says nothing about the
manifold, and **nothing about whether the ℤ/5 menu is this object's — B8086 showed it is NOT**
(`H₁ = ℤ`, torsion-free). This is a fact about `E₆` and a mod-5 lattice, not about `m004`.
