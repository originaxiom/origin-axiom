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

**Ledger:** V111. **Reuses:** `B103.two_sequence_mult`. **Unifies:** B121 (the external action) + Chat-2's
W-identity. **Anchors:** B117 (two-sequence + dimension identity), B118 (the sign layer), B120 (m-universality).
