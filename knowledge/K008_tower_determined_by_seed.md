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

## The plethysm has a name: symmetric powers of a 3-dim rep (B122)

The Sym two-sequence is not a custom decomposition — it is **symmetric powers of the 3-dimensional rep `W = V⊕1`**
(the 2-dim defining `V` plus a trivial). As a virtual `GL(2)`-module:
```
   ρ_n  =  Sym^n(W)  ⊕  ( Sym^{n−3}(W) ⊖ W ),      W = V ⊕ 1.
```
- `Sym^a(V⊕1) = ⊕_{k=0}^a Sym^k(V)` (a contiguous band) is what makes the two-sequence's staircase; `Sym⁰⊕Sym¹ =
  1⊕V = W`, so the correction is the "nonlinear part" `Sym^{n−3}(W) ⊖ W`.
- It is a **genuine `GL(2)`-module iso** (verified symbolically in general `(x,y)`, det-independent, n≤8; proved
  module-level at n=3,4 via B103) — not merely a character coincidence.
- **`W` is canonical:** it is the **external monodromy `SL(2)`'s fundamental** (B121). `det(W)=−1` (the external
  parity), whereas the Fricke 3-space `= Sym²(V)` has `det=+1` (the internal/principal/Kostant rep) — which is *why*
  the natural guess "`W` = Fricke space" is wrong. The tower's odd `Sym`-weights come from `W∋V`; this is the same
  `det=−1` parity that splits the catalog (B93/B94) and gives the inversion sign (B118).
- **`Sym⁴(3-space) = 15 = sl(4)`**, and `4` is the *unique* order where `Sym^a(3-space)` saturates `n²−1` — the n=4
  fixed point of the dimension identity, restated.
- **The magnitude layer is `det`-independent; the sign layer is the metallic feature.** The W-identity is a
  polynomial identity in the eigenvalues, so it holds for `det=+1` as well as `det=−1` (verified through n=14) — the
  `Sym` content is **more general than the metallic ray**. The *signs* (`char(M^h)` vs `char(−M^h)`, the inversion
  identity `char(M⁻¹)=char(−M)`, B118) are `det=−1`-specific and collapse under squaring (the figure-eight monodromy
  `= `golden²`, det=+1`). And the `Sym` tower is **void-specific**: it is the linearization where the abelianization
  `M` acts (the trivial fixed point); off the void the trace map is elliptic / root-of-unity (e.g. order-6 at SL(2)),
  not `Sym`-organized (B106).

## A centralizer reading of the multiplicities (framing note, 2026-06-11)

A review session offered an elementary re-reading of the B121/B122 multiplicity data (a *framing*, not new
math): a seed lift into `SL(n)` leaves unbroken the centralizer of its image, which over the eigenvalue
multiplicities `(m_i)` is `S(∏_i GL(m_i))`. Consequences, all immediate from the data above:
- an **irreducible `Sym^k` lift breaks to the maximal torus at every rank** — `φ` is not a root of unity, so
  `Sym^k(M)` has distinct eigenvalues and the centralizer is `(GL_1)^{·}∩SL`;
- **non-abelian unbroken factors arise only from repeated weights** (e.g. a `GL(2)` in `SL(4)` from the
  `A⊗A` multiplicity, or from `Λ²(Sym³)` — the `Λ²` of the B85 functor — in `SL(6)`).
This is linear algebra on the banked `Sym`-decomposition, recorded as a pointer to B121/B122; it adds no
claim. STRUCTURAL framing only.

## The spectrum is reciprocal-closed: time-reversal and a det=−1 handedness residue (B124)

The trace map is a reversible area-preserving (symplectic) map, so the tower spectrum is **reciprocal-closed**
`(λ,1/λ)` and **time-reversal** (the inverse map) acts as `λ↔1/λ`, swapping the stable/unstable manifolds — generic
to all such maps (the anchor is the SL(2) void Jacobian `{φ²,−1,φ⁻²}`: a reciprocal pair + the self-reciprocal `−1`,
`det=−1`). This is **symplectic geometry, not a metallic feature**; the only metallic-specific datum is the **rate**
`log φ²`. Two facts on top of it (B124/V113):

- **No arrow.** Expanding-mode count `==` contracting-mode count, **exactly, every `n`, both `det` signs** (reciprocal
  pairing forces it). The two "time directions" carry identically many modes — there is no forward-vs-backward
  preference in the spectrum.
- **A det=−1 chirality (P) residue.** Yet `det=−1` carries **negative** reciprocal-pair modes (the `char(−M^h)`
  sectors; `det=+1` carries none) — the same amphichirality as the inversion identity `char(M⁻¹)=char(−M)` (B118),
  surfacing in the mode counts. So the metallic structure breaks **chirality (P-like)** while **preserving
  time-direction symmetry (T-like)**. The imbalance is real and `O(n/2)`, but its **exact constant is open**
  (bookkeeping-dependent: the raw `±1` excess is period-4, not `⌊n/2⌋`; the n≥5 regime is inflated by the B117
  middle-band doubling).

The geometric/physical "two-headed time" *reading* of this reciprocity is an interpretation, firewalled in
`../philosophy/P006` and `../speculations/S002` — it never enters here.

## What it does *not* license

This is a structural determination and a clean **repackaging**, not a closure: the W-identity is module-iso-
*equivalent* to the two-sequence, and there is **no functorial `Sym(W)→trace-ring` map** (the `Sym⁴(3)=15`
saturation is n=4-only). So it identifies `W` canonically and re-aims the all-`n` target — *prove the tower is
functorially `Sym^n(W) ⊕ (Sym^{n−3}(W)⊖W)`* — but it does **not** lower the trace-ring wall. **Update (B232):**
the all-`n` target is reduced to a *local* induction — the **one-step stabilization** `ρ_n ≅ ρ_{n−1} ⊕ Sym^n(V)
⊕ Sym^{n−3}(V)` (verified on the real Jacobian `n≤5`, extended to `n=8`, and shown to fail for the foreclosed
cohomological route); the residual lemma is now the single stabilization step (the lag-3 `Sym^{n−3}` from the
degree-`n` Cayley–Hamilton relation, `dim W=3`), not the whole catalog. A relocation of the wall to a cleaner
statement, not a closure. It is the **magnitude
layer** (the `Sym` content / eigenvalue magnitudes); the **signs** `char(M^h)` vs `char(−M^h)` are the orthogonal
`det=−1` layer (B118). The all-`n` formula for `μ_d` remains the central target (B103), behind the wall.

**Anchors:** B103 (the `GL(2,ℤ)`-rep + the `ℚ[m]`-iso, V87), B117 (the Sym two-sequence + the dimension identity,
V104), B120 (the `(n;trace,det)` determination + m-universality, V107), **B121** (the external monodromy `sl(2)`,
V109), **B122** (the `W=V⊕1` symmetric-power identity, V111), **B124** (reciprocal pairs / time-reversal + the
det=−1 chirality residue, V113). External: classical plethysm / branching of `SL(2)` representations; the
geometric/physical readings of `W` (and the "two-headed time" reading of the reciprocity) are firewalled
(`../speculations/S028`, `../philosophy/P006`, `../speculations/S002`).
