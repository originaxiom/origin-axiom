# K003 — The Dickson tower

> **Explainer** (`GOVERNANCE.md`). Self-contained; standard material cited to the literature, the project's own use
> cited by `B`/`V` number (no re-proof). Nothing here promotes to `../CLAIMS.md`; never a premise in a proof.

## Symmetric powers of a 2×2 matrix

Take `M ∈ GL(2)` with eigenvalues `α, β` (so `tr M = α+β`, `det M = αβ`). For each `d ≥ 0` the `d`-th **symmetric
power** `Sym^d(M)` is the `(d+1)`-dimensional matrix acting on degree-`d` polynomials in two variables; its
eigenvalues are the `d+1` monomials
```
   α^d,  α^{d−1}β,  …,  β^d        (i.e. α^{d−j} β^j, j = 0..d).
```
These are the irreducible `SL(2)` representations; their characters are the **Chebyshev / Dickson polynomials** in
`(tr M, det M)`. Writing `L_k := tr(M^k) = α^k + β^k`, the `L_k` satisfy the Dickson recurrence
`L_k = (tr M)·L_{k−1} − (det M)·L_{k−2}`, with the **Dickson parity**
```
   L_{−k} = (det M)^{−k} · L_k,   and for det M = −1:   L_{−k} = (−1)^k L_k.
```
That last sign is the whole reason `det = −1` (the metallic case, `K002`) splits the bookkeeping into even and odd
sectors.

## The tower

At the trivial fixed point of the `SL(n)` figure-eight trace map, the linearization (the **tower**) is an
`(n²−1)`-dimensional representation that **decomposes into symmetric powers** of the abelianized monodromy `M`:
```
   ρ_n  ≅  ⊕_d  Sym^d(M)^{μ_d},        μ_d  =  [2 ≤ d ≤ n]  +  [0 ≤ d ≤ n−3].
```
The multiplicity sequence `μ_d` is the **two-sequence** (B103/B117): one contiguous band from `d=2` to `d=n`, plus a
second from `d=0` to `d=n−3`. Equivalently the tower's characteristic polynomial is the **catalog**
```
   char(ρ_n)  =  (parity) · ∏_k char(± M^k),
```
a product of the 2×2 factors `char(±M^k) = t² ∓ tr(M^k) t + (det M)^k`, with the `±` signs fixed by the `det = −1`
twist (`Sym^d ⊗ det^k` contributes a `(−1)^k`). The `char(−M^k)` "negative" sectors are precisely the metallic
orientation twist; at `det = +1` they are absent (`K008`, B124).

## What is proved, and the open prize

- **Universality / class-function** (B103, all `n`, Route 1): `char(ρ_n)` factors through the abelianization `N`, so
  it is a polynomial in `(tr N, det N)` — the *same* catalog for metallic and non-metallic monodromies, with the
  **det-sign parity** law (sharpening B94).
- **Explicit catalog `μ_d`** proved exactly over `ℚ[m]` at `n = 3, 4` (B103 module-iso; B80 the `n≤4` tower
  `Z[m]`/CRT route); the **sign half** of the catalog — the multiplicities `char(M^h): ⌈(n−h)/2⌉`,
  `char(−M^h): ⌊(n−h)/2⌋` — is proved for all `n` by an opposition-involution argument (B112, `K005`).
- **The open prize:** prove the two-sequence `μ_d` (equivalently the full catalog) for **all `n`**. The clean modern
  form is that `ρ_n` is **symmetric powers of `W = V⊕1`** (B122, `K008`): `ρ_n = Sym^n(W) ⊕ (Sym^{n−3}(W) ⊖ W)`. This
  is a genuine `GL(2)`-module identity but **not** yet a functorial construction; the wall is to find the functorial
  `Sym(W) → trace-ring` map. The `n ≥ 5` regime is where the explicit catalog stalls (three distinct obstacles, V91).

## How the project uses it

The Dickson tower is the project's central object: B59–B66 built it up the ranks (SL(5) modes, the SL(6) `|k|=3`
multiplicity), B80 proved it for `n≤4` from first principles, B103 made it a class function, B112–B122 split it into
the proved sign half + the open magnitude/`μ_d` half. The "degree=rank" relation `L = (−1)^{n−1} M^n` (`K004`) is the
statement that `char(M^n)` is always a tower factor (`μ_n = 1` ∀n).

**Anchors:** B59–B66 (building the tower; Dickson parity, B64), B80 (the `n≤4` proof), B103 (class function +
two-sequence, V87), B112 (the sign half all `n`, V99), B117/B122 (the two-sequence / `Sym^n(W)`, V104/V111).
External: Dickson polynomials (Lidl–Mullin–Turnwald); Chebyshev / `SL(2)` representation theory; Procesi, *The
invariant theory of `n×n` matrices*.
