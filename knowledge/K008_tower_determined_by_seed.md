# K008 — The trivial-point tower is determined by `(n; trace, det)`

> **Explainer** (`GOVERNANCE.md`). Self-contained; cites the project's own results by `B`/`V` number (no re-proof)
> and standard material to the literature. Nothing here promotes to `../CLAIMS.md`; never a premise in a proof.

## What the object is

At the trivial fixed point of the `SL(n)` figure-eight trace map, the linearization (the "tower") is an
`(n²−1)`-dimensional representation of the abelianized mapping-class group — concretely a `GL(2,ℤ)`-representation
`ρ_n`, where the abelianization `N ∈ GL(2,ℤ)` is the seed matrix (for the metallic family, `N = M_m = [[m,1],[1,0]]`,
`det = −1`). The tower decomposes under the principal `SL(2)` as a multiset of symmetric powers,
`ρ_n ≅ ⊕_d Sym^d(M)^{μ_d}`, with the **two-sequence** multiplicities `μ_d = [2≤d≤n] + [0≤d≤n−3]` (the Dickson
catalog; proved exact over `ℚ[m]` at `n=3,4`). See `K003` (the Dickson tower) and B103/B117 for the structure.

## The determination

The tower's characteristic polynomial is a function of only **two inputs**:

1. **the unfolding depth `n`** — which fixes the *content* `{Sym^d : μ_d > 0}` and the multiplicities `μ_d` (B117:
   the two-sequence; its shape is forced by the dimension identity `(n+1)(n+2)/2 − (n²−1) = −(n−4)(n+1)/2`);
2. **the seed `(trace, det)` of `N`** — which fixes the *eigenvalues*. Each `Sym^d` eigenvalue is a degree-`d`
   monomial in the two eigenvalues of `N`, and those are determined by `N`'s characteristic polynomial — i.e. by
   `(trace, det)` alone.

So the tower factors as `tower(n ; trace, det)`. Two consequences, both verified (B120/V107):

- **Same `(trace,det)` ⇒ same tower.** Distinct integer matrices with equal `(trace, det)` — e.g. `[[2,1],[1,0]]`
  and `[[1,2],[1,1]]`, both `(2,−1)` — produce *identical* towers (n=3,4,5). The specific entries of `N` are
  invisible; only its conjugacy invariants enter.
- **m-universality of the content.** The multiplicity structure `μ_d` depends only on `(n, det)`, **not** on the
  trace `m`: changing `m` rescales the eigenvalues (`φ_m`) but leaves the `μ_d` fixed. This is the representation
  `ρ_n` being trace-blind — the `μ_d` are its plethysm/branching multiplicities under the principal `SL(2)`, which
  see only the abstract rep (`n`) and the parity (`det`). (Proved `n=3,4` via B103's `ℚ[m]`-iso; the all-`n`
  statement is the same open problem as the two-sequence itself.)

## Why the two inputs are the interaction-word seed

In the mapping-class group the metallic unit factors as `M_m = (twist)^m · (swap)`. The two invariants read off
the word: the **twist-count → trace** (the seed `m`, the expansion rate) and the **swap-count mod 2 → det**
(orientation, the parity sector — the proved `det = −1` parity, B93/B94). The sign structure of the tower (the
inversion identity `char(M^{−h}) = char(−M^h)` for odd `h`, B118) is itself a `det=−1` feature. So
"`n` = how far the unfolding goes; `(trace,det)` = the seed it unfolds" is the precise, all-`n` form of
"the interaction determines the tower."

## What it does *not* license

This is a structural determination, not a closure of the open problem: writing down the all-`n` formula for `μ_d`
(the two-sequence / the plethysm) remains the central target (B103), behind the trace-ring wall. m-universality
**reframes** that target as a plethysm computation but does not lower the wall.

**Anchors:** B103 (the `GL(2,ℤ)`-rep + the `ℚ[m]`-iso, V87), B117 (the Sym two-sequence + the dimension identity,
V104), B120 (the `(n;trace,det)` determination + m-universality, V107). External: classical plethysm / branching
of `SL(2)` representations.
