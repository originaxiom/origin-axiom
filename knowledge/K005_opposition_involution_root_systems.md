# K005 — The opposition involution `θ = −w₀` and root systems

> **Explainer** (`GOVERNANCE.md`). Self-contained; standard material cited to the literature, the project's own use
> cited by `B`/`V` number (no re-proof). Nothing here promotes to `../CLAIMS.md`; never a premise in a proof.

## Root systems and heights

The Lie algebra `sl(n)` has root system `A_{n−1}`: its roots are `e_i − e_j` (`i ≠ j`), the adjoint representation is
`sl(n)` itself (dimension `n²−1`), and the positive roots `e_i − e_j` with `i < j` have **height** `j − i`
(`1 ≤ height ≤ n−1`). There are exactly `n − h` positive roots of height `h`. Heights stratify the `(n²−1)`-dimensional
adjoint into the Cartan (height 0, dimension `n−1`) plus the height-`h` root spaces — the grading the tower's catalog
(`K003`) is organized by.

## The longest Weyl element and the opposition involution

The Weyl group of `A_{n−1}` is the symmetric group `S_n`, and its **longest element** `w₀` is the order-reversing
permutation `i ↦ n+1−i`. The **opposition involution** is
```
   θ = −w₀ ,
```
a diagram automorphism of `A_{n−1}` (it is the flip of the Dynkin diagram). On a root,
```
   θ(e_i − e_j) = e_{n+1−j} − e_{n+1−i} ,
```
which is **height-preserving**: on the `n − h` positive roots of height `h` it acts as the **reversal involution**
`σ(i) = (n−h+1) − i`. `θ` is the abstract incarnation of "contragredient / dual": at the group level it sends a
representation to its dual, and on characters it is the substitution `m ↦ −m` whose Dickson signature is
`L_k(−m) = (−1)^k L_k` (`K003`).

## The `(+,−)` eigenspace split and the multiplicity question

Because `θ` is an involution, each height-`h` root space splits into its `+1` and `−1` eigenspaces. A reversal
involution on `m = n − h` points has eigenspace dimensions
```
   (+1, −1) = (⌈m/2⌉, ⌊m/2⌋)
```
(odd `m`: one fixed point + `(m−1)/2` swapped pairs; even `m`: `m/2` swapped pairs). Matching the `+1` sector to
`char(M^h)` and the `−1` sector to `char(−M^h)` (the B64 contragredient/parity assignment) gives the **sign half** of
the catalog,
```
   mult char(M^h) = ⌈(n−h)/2⌉ ,     mult char(−M^h) = ⌊(n−h)/2⌋ ,
```
the first piece of the `ρ_n` catalog proved from first principles for **all `n`** (B112), engine-free (no Procesi
ring, no ε-series). The net `(+)`-excess is `⌊n/2⌋`.

## A scope caution (carried from the audits)

The opposition-involution decomposition proves the **sign half** (the `θ`-split combinatorics) for all `n`. It is
**not** the whole tower: the full catalog is this split *plus* the magnitude / `μ_d` content (`K003`), and the
identification of the `θ`-split with the Sym two-sequence holds only `n ≤ 5` — at `n ≥ 6` they diverge (V103/B116).
So `K005`'s machinery is the **sign-structure** engine, complementary to the still-open `μ_d` prize. Two attempts to
push `θ` further were killed cleanly and are tombstoned: `θ → c` (an order-2 symmetry cannot single out the order-4
degree=rank scalar, B108) and `s_n → c` (the order-≤2 tower sign, B111).

## How the project uses it

`θ = −w₀` is the backbone of the sign analysis: B62 first saw the height-2 `(4,2)`/`(2,1)` splits, B74 connected them
to the root system, B112 (V99) turned the reversal lemma into the proved sign half, B118 (V106) pinned the fixed-root
sign `(−1)^{h+1}`, and B121 (V109) recognized the resulting parity as the **external `det=−1` monodromy** grading
(`K008`). The two-symmetry framing (`θ` and the secondary `ℤ/4`) is in `../speculations/TWO_SYMMETRY_FRAME.md`.

**Anchors:** B62 (height-2 splits), B74 (the root-system reading), B112/V99 (the sign half proved), B118/V106 (the
fixed-root sign), B121/V109 (the parity = external monodromy). External: Bourbaki, *Lie Groups and Lie Algebras*
(root systems, the longest element); the opposition involution / Dynkin diagram automorphisms (standard structure
theory).
