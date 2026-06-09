# K015 — The chirality–arithmetic connection: eigenvalue field-fusion in the quantum layer

> **Explainer** (`GOVERNANCE.md`). Self-contained; standard material cited to the literature, the project's own use
> cited by `B`/`V` number (no re-proof). Nothing here promotes to `../CLAIMS.md`; never a premise in a proof. The
> bankable MATH of the quantum layer (B132/V121).

## The setting

On top of the classical character-variety picture (the metallic once-punctured-torus bundles `M_m`, their trace fields,
the chirality recursion `K011`, the two-seed fork `K014`) sits a **quantum layer**: the SU(2)_k Witten–Reshetikhin–
Turaev data `Z_k(M_m)`. Concretely, at level `k` the modular `(S,T)` data of SU(2)_k gives a `(k+1)`-dimensional
representation of the once-punctured-torus mapping class group (`R=T` the Dehn twist, `L=S T S⁻¹`); a metallic word maps
to the ordered product, and `Z_k` is its trace. All eigenvalues of `ρ_k(word)` are roots of unity, so each generates a
cyclotomic field: an eigenvalue of **order d** lies in `ℚ(ζ_d)` (order 6 or 3 → ℚ(√−3), order 4 → ℚ(i), order 12 →
ℚ(ζ₁₂)=ℚ(√−3,i)). This **eigenvalue-order method** is exact and precision-independent.

## The connection: chirality shifts the eigenvalue arithmetic (B132)

At the saturation level `k=4`:

- **Achiral / same-seed compositions → ℚ(√−3)** (golden). The figure-eight `RL`, the same-seed product `RLRL`,
  silver×silver `RRLLRRLL` (which *defuses* back), and the achiral triple `(1,2,1)` all have spectra in ℚ(√−3).
- **Chiral / cross-seed compositions → ℚ(ζ₁₂), and the partition function vanishes.** `fig8×silver` (RLRRLL) and the
  **chiral** triple `(1,2,3)` fuse to ℚ(ζ₁₂)=ℚ(√−3,i) and have `|Z|=0`.

So **breaking chirality shifts the eigenvalue arithmetic from ℚ(√−3) toward ℚ(i)**. This is **chirality-driven, not
word-length-driven** (`RLRL` is 4 letters and ℚ(√−3); the 12-letter `(1,2,3)` is ℚ(ζ₁₂)). For the single seeds, the
ℚ(i) content appears exactly when `m ≡ 2 mod 4` (the order-4 eigenvalues from the SU(2)₄ T-phase `exp(mπi/4)` at spins
j=1,3), so it is quantum-group arithmetic controlled by `m mod 8`.

This is the **quantum companion** of two classical facts: the chirality recursion (`K011`, B128 — *which* compositions
are achiral) and the two-seed fork (`K014`, B131 — composition of distinct seeds creates new structure). The classical
character-variety fork and the quantum eigenvalue-field fusion are the same composition phenomenon at two levels.

## The non-cancellation persistence hierarchy

The fused (chiral/cross-seed) states **vanish** (`Z=0`) at `k=4`, and chiral compositions vanish at *more* levels than
their achiral siblings. So the non-cancellation principle (`K010`, `P008`) **selects the achiral (symmetric) vacuum** as
the most persistent: m=1 achiral (`|Z|=1` at every level) > achiral compositions > chiral compositions (most fragile).
Chirality is a fragile perturbation that costs quantum persistence.

## What is the project's, and what is the field's

The SU(2)_k modular data and the WRT invariants are classical quantum topology (Reshetikhin–Turaev). What is the
project's is the **recognition**: that the metallic family's *chirality* (a classical, geometric property — `K011`)
controls the *cyclotomic field of its quantum eigenvalues*, with the symmetric (achiral) configurations the coherent,
persistent ones. The native physics of the quantum layer is the **Lee–Yang edge** (the σ₃ Galois conjugate; `S030`,
`K010`) — emergent non-equilibrium criticality, not the Standard Model.

**Anchors:** B132/V121 (the result + the validated convention), `K011`/B128 (the chirality recursion — classical),
`K014`/B131 (the two-seed fork — classical companion), `K010` (the Fricke–Vogt naming / Lee–Yang), `K016` (the m=1
selection criteria, incl. the quantum ones), `../speculations/S030` (Lee–Yang, now TESTED-POSITIVE). External: SU(2)_k
modular tensor category; Reshetikhin–Turaev; Lee–Yang / M(2,5).
