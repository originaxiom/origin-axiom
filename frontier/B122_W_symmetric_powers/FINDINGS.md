# B122 — the tower is symmetric powers of the external monodromy fundamental `W = V⊕1` (unifies B121)

The two-sequence (B117) re-expressed, and **unified with B121**: as a virtual GL(2)-module,
```
   ρ_n  =  Sym^n(W)  ⊕  ( Sym^{n−3}(W)  ⊖  W ),      W = V ⊕ 1   (3-dim),
```
`V` = the 2-dim defining rep of the figure-eight monodromy, `1` = trivial. Banked at **honest strength**: a genuine
GL(2)-module repackaging + a canonical identification of `W` — **not** a proof route / wall-bypass. No physics; the
3+1 / spin-2 readings are firewalled (`S028`); nothing to `CLAIMS.md`; the `ρ_n`/Sym-`μ_d` proof stays the prize;
P1–P16 untouched.

## (1) The character identity (verified n≤11)

`ρ_n = Sym^n(W) + Sym^{n−3}(W) − 1 − V` decomposes into `Sym^k(V)` with multiplicity `== μ_d` (B103/B117), verified
**n=2..11**. Since `W=V⊕1`, `Sym^a(W) = ⊕_{k=0}^a Sym^k(V)` — the contiguous band that makes the staircase. The
cleaner form: `Sym⁰⊕Sym¹ = 1⊕V = W`, so the correction is `Sym^{n−3}(W) ⊖ W` (the *nonlinear part* of the
lower-order invariants).

## (2) It is a genuine GL(2)-MODULE iso (the corrected hinge — not vacuous)

A first pass called the module-iso "automatic," but that is only true over the cyclic `⟨M⟩`. The tower is a
**GL(2,ℤ)-representation** (B103), and over GL(2) module-iso is *not* implied by a single element's character. The
real test: the identity
```
   Σ_d μ_d · h_d(x,y)  =  h_n(x,y,1) + h_{n−3}(x,y,1) − 1 − (x+y)
```
holds **symbolically in general `(x,y)`, independent of `det`**, for n=2..8 (`h` = complete homogeneous symmetric
poly = `Sym`-character). Because `Sym^a(V⊕1) = ⊕_{k≤a}Sym^k(V)` is a **functorial** module decomposition, this is a
**genuine GL(2)-module iso** — proved module-level at n=3,4 (B103's `P`-iso), character-level for all n.

## (3) `W` is B121's external fundamental — the unification (no double-count)

`det(W=V⊕1) = det(V)·1 = −1` → the **external `det=−1` parity** (B121); `det(Fricke = Sym²V) = +1` → the **internal
principal/Kostant parity**. So **Chat-2's kill of "`W` = Fricke 3-space" IS B121's external≠internal**: the Fricke
space carries the internal embedding (even weights, det+1), the tower carries the external monodromy one (mixed
parity, det−1). The tower's **odd weights** = `Sym^n(V⊕1)` including `V` (weight 1) = the **B121 parity obstruction,
re-derived**. So **B121 and the W-identity are one object**, not two characterizations — the monodromy grading *is*
`Sym(external fundamental)`.

## Corollaries (math tier; A7a / A1)

- `Sym⁴(3-space) = 15 = dim sl(4)`, and **4 is the unique saturating order** (`Sym³(3)=10≠8`, `Sym⁵(3)=21≠24`) —
  the n=4 fixed point of the dimension identity (B117), restated as "the 4th symmetric power of a 3-space saturates
  the adjoint."
- Band **offset = dim(W) = 3** (in the `W`-power index) = the offset-2 in the `Sym(V)`-index (B117 doubling): **one
  structure, reconciled readings** — not competing results.

## Not a wall-bypass (the brave functorial test, run and reported)

The identity is the elementary expansion `Sym^a(V⊕1)=⊕Sym^k(V)` applied to the two-sequence; it is **module-iso-
equivalent** to the two-sequence (proving it for all n **==** proving `μ_d`). **No functorial `Sym(W)→trace-ring`
map** was found; the `Sym⁴(3)=15` saturation is n=4-only (the correction term blocks a single clean `Sym^n`). So it
**repackages** the prize and **identifies `W` canonically**, but does **not** lower the trace-ring wall.

> **Re-aimed prize:** prove the tower is *functorially* `Sym^n(W) ⊕ (Sym^{n−3}(W) ⊖ W)` for the external
> fundamental `W` — a construction that does not yet exist. This is the **magnitude layer** (the `Sym` content); the
> signs `char(M^h)` vs `char(−M^h)` are the orthogonal **`det=−1` layer** (B118's `(−1)^{h+1}`).

## Extensions (Chat-2 interlude — terrain-sweeping; none touch the wall)

- **The two layers split by `det` (Finding 1).** The figure-eight monodromy is the **golden unit squared**:
  `M₁² = [[2,1],[1,1]]`, `det=+1`, eigenvalue `φ²`. From this the layers separate:
  - **Magnitude layer (the W-identity / `μ_d`) is `det`-INDEPENDENT.** The identity is a polynomial identity in
    `(x,y)` (above), so it holds for `det=+1` as well as `det=−1` — it is **more general than the metallic ray**
    (not a `det=−1` feature). The multiplicity form matches `μ_d` **through n=14** (confirmation, past the banked
    n≤11).
  - **Sign layer (the inversion identity `char(M⁻¹)=char(−M)`, the parity sector) is `det=−1`-SPECIFIC.** Symbolic:
    `char(M⁻¹)−char(−M) = 0` at `det=−1`, `= −2tτ` at `det=+1` (fails). The parity factor `(t−1)(t−det)` collapses
    `(t−1)(t+1) → (t−1)²` going golden (`det=−1`) → fig-8 (`det=+1=`golden²) — squaring squares the eigenvalues and
    collapses the signs while leaving the `Sym` content intact. **This confirms the two-layer model exactly:** W =
    magnitude (`det`-independent); signs = the metallic/orientation feature (B118, `det=−1`).
- **The `Sym` organization is VOID-SPECIFIC (Finding 2; explicit at SL(2), corroborates B106).** On the trace map
  `T(x,y,z)=(z,x,xz−y)`: at the **void `(2,2,2)`** the Jacobian eigenvalues are `{−1, φ², ψ²} = Sym²(M)` (the n=2
  tower); at the **other fixed point `(0,0,0)`** they are `{−1, e^{±iπ/3}}` = **6th roots of unity** (char poly
  `λ³+1`, `DT⁶=I` — order **6**, *not* cube roots / order 3), an elliptic spectrum, **not** `Sym`-organized. So the
  `Sym^d(M)` tower lives where the abelianization `M` acts — the void — making B106's "non-void reps are a different
  spectral type" explicit and computable at SL(2).

**The standing truth.** None of this lowers the wall. The functorial `Sym(W)→trace-ring` construction (a natural map
defined without the ambient `SL(n)` trace ring) is still the one missing piece — a construction to be found, not a
probe to be run.

**Ledger:** V111 (light annotation for these extensions). **Reuses:** `B103.two_sequence_mult`. **Unifies:** B121
(the external action) + Chat-2's W-identity. **Anchors:** B117 (two-sequence + dimension identity), B118 (the sign
layer), B120 (m-universality), B106 (void vs non-void spectral types).
