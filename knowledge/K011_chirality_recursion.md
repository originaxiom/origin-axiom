# K011 — The chirality recursion: when a metallic concatenation is amphichiral

> **Explainer** (`GOVERNANCE.md`). Self-contained; standard material cited to the literature, the project's own use
> cited by `B`/`V` number (no re-proof). Nothing here promotes to `../CLAIMS.md`; never a premise in a proof. This is
> the bankable MATH of the symmetry-breaking arc (B128/V117) — a sharpening of the B127 CS=0 result.

## The setup

The orientable metallic bundles are the once-punctured-torus bundles whose monodromy word is `M_m² = R^m L^m`
(`K002`, `K004`). B127 (`K010`) showed each **pure** metallic word is **achiral** (Chern–Simons invariant ≡ 0). The
natural next question is what happens to *concatenations* of metallic blocks — gluing several towers:
```
   W = R^{m₁}L^{m₁} · R^{m₂}L^{m₂} ··· R^{m_k}L^{m_k},   block-length sequence (m₁,…,m_k).
```
These are again punctured-torus bundles (the SnapPy `b++` words), so amphichirality (achirality) is a well-defined,
computable property of each.

## The recursion theorem (B128)

> **`W` is amphichiral (achiral) ⟺ the block-length sequence `(m₁,…,m_k)` is itself amphichiral** — i.e. its reversal
> `(m_k,…,m₁)` is a cyclic rotation of `(m₁,…,m_k)`.

The chirality question **recurses one level up**: from the `R/L` word down to the integer sequence of block-lengths.
Consequences:

- **Every double is achiral.** Any `(a,b)`: the reversal `(b,a)` is a cyclic rotation of `(a,b)`. (This is exactly the
  B127 pure-word case `k=1` plus the simplest concatenations.)
- **Triples and higher are achiral only when the block-sequence is palindromic-up-to-cyclic.** `(1,2,1)`, `(2,1,3,1)`,
  `(1,1,2,2)` are achiral; `(1,2,3)`, `(1,3,2)`, `(1,2,3,4)`, `(1,2,2,3)` are **chiral**.

The structural reason: the manifold mirror is realized by the `R↔L` block swap (B127's reverse+swap symmetry), which
**lifts the integer-sequence reversal**; doubles close by cyclic conjugacy of the monodromy product, triples and
higher do not.

**Status: PROVED (B134/V123)** — as an elementary corollary of **Goodman–Heard–Hodgson 2008** (arXiv:0801.4815), which
classify the symmetries of a once-punctured-torus bundle by its L/R monodromy word: amphichiral ⟺ the word is
**anti-palindromic** (`reverse(W) = swap_{L↔R}(W)` cyclically). For a metallic-block word, `reverse(W)` and `swap(W)`
are both `LᵃRᵃ`-block words with block-length sequences `(m_k,…,m₁)` and `(m₁,…,m_k)`; they agree cyclically ⟺ the
block-length sequence is a cyclic palindrome. So **amphichiral ⟺ `(m₁,…,m_k)` is a cyclic palindrome** — proved. (Was a
`15/15` computer-verified conjecture; the novelty audit located the GHH mechanism — see `../docs/NOVELTY_AUDIT.md`,
`../frontier/B134_chirality_recursion_proved/`. The **block-length lift** is the project's novel kernel; the chirality
mechanism is GHH's. One outstanding specialist check: GHH's criterion as a strict iff for all these bundles.)

## The order parameter and the `Z₂` (B128)

- **The order parameter is the ordering, not the count.** The three chiral triples `(1,2,3),(1,3,2),(3,2,1)` all have
  `#R=#L=6` (imbalance zero) yet are chiral (CS = ±0.00888). So **achiral ⟹ #R=#L** (necessary) but **#R=#L does not
  imply achiral**. The genuine order parameter is the **block-sequence chirality**; `#R−#L` is a mean-level proxy.
- **An exact `Z₂`.** Block-reversal = the mirror image = negates CS exactly (machine zero). The `R↔L` swap is the `Z₂`
  whose *choice of orientation* is the symmetry-breaking selection.

## The method note (correct chirality test — also a `REPRODUCIBILITY.md` SCAN)

Naive `M.is_isometric_to(M_mirror)` is **orientation-blind** and gives **false positives** for amphichirality (it
admits orientation-reversing isometries; the mirror map is always one — it returns `True` for the known-chiral
m015/m016/m009). Raw CS **sign** is also unsafe (period/modulus; a small CS can still be genuinely chiral). The
**correct** test is `M.symmetry_group().is_amphicheiral()` gated on `M.symmetry_group().is_full_group() == True`.
Controls: m004/m003 amphichiral, m015/m016/m009 chiral.

## What this is, and what it is not

The recursion is **MATH** — a fact about which punctured-torus bundles are amphichiral. Its physics reading is the
B128 *sharpening*, firewalled: composition **permits** a parity break (the chiral triples are the first
metallic-derived objects to break CS=0) but **never forces** it, and *which* arrangement is chiral is a free
**ordering** choice — the symmetric structure cannot force its own breaking (`../philosophy/P007`, `P008`; the fifth
firewall direction). It does **not** license a gauge group: the companion attempt to read homology torsion as an
`SU(n)` center is tombstoned (`K-F`, `../speculations/TOMBSTONES.md`; torsion tracks periodicity, not chirality, and
center≠gauge — `S029`/`S030`).

**Anchors:** B128/V117 (the recursion, the order parameter, the `Z₂`, the method bug, `K-F`), **B134/V123 (the PROOF
via GHH)**, B127/`K010` (the CS=0 pure-metallic locus this sharpens), `K002`/`K004` (the metallic bundles),
`../philosophy/P007`/`P008` (the firewall), `../speculations/S029`/`S030` (the rank-1 abelian fence / Yang–Lee fork),
`../docs/NOVELTY_AUDIT.md` (R1). External: **Goodman–Heard–Hodgson 2008 (arXiv:0801.4815, the anti-palindromic word
criterion)**; Kauffman–Lambropoulou (palindromic rational knots); once-punctured-torus bundles; SnapPy
`symmetry_group().is_amphicheiral()`.
