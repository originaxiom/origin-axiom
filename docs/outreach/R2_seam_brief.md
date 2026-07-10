# R2 — the √−15 vanishing of a level-15 pair invariant: one pair-specific window question

**For:** a specialist in Weil representations / modular data / the arithmetic of quantum invariants
(Gannon type; Deloup–Turaev reciprocity or Coste–Gannon Galois actions are the closest neighborhoods
we know). **Status:** honest — the vanishing law is derived from the object's own machinery up to a
single named, provably pair-specific lemma; the question is why that lemma holds for the flagship
pair.

## Setup (self-contained)

Let `ρ` be the Weil representation of `SL(2, ℤ/15)` on `ℂ[ℤ/15]` in the theta normalization
(`T ↦ diag ζ₁₅^{j(j−1)/2}`, `S`-conjugate by the finite Fourier transform). For a once-punctured-torus
bundle with monodromy `RᵐLᵐ` write `W_m` for the lifted monodromy and `P_a(W_m)` for its
eigenprojectors, and let `Par` be the parity operator `f(x) ↦ f(−x)`. The **pair invariant** is

  `t(a, b) = tr( Par · P_a(W_{m₁}) · P_b(W_{m₂}) )`,

projected to `H = ℚ(√5, √−3)` by the Galois average. Its four Galois channels are indexed by the
subfield lattice of `H` (rational / `√5` / `√−3` / `√−15`). Internally this is the "seam" invariant.

**The observed law (verified exact).** For single objects the readout lies in `ℚ(√5)`; genuine pairs
acquire exact rational multiples of `√−15`. The flagship, for `(m₁, m₂) = (1, 2)`, is

  `t(0, 4) = −1/48 − (1/80)√5 − (1/48)√−3 + (1/48)√−15`.

Across the dual torus the pattern of which channels vanish is exactly the **subfield lattice of `H`
minus the `√−15` node**, plus an all-dead "zero" stratum — the `√−15` channel is never the sole
survivor of the `√5`/`√−3` pair.

## What is now derived (verified, out-of-sample-checked)

The vanishing law **derives from the object's own CRT / character-gate machinery**. In exact
`ℚ(ζ₆₀)` arithmetic (no numerics), the invariant factorizes through the tensor split
`C = C₃ · C₅` at the shared multiplier, and the four Galois channels are the character-weighted
Galois averages of local (level-3 and level-5) theta data. A classifier theorem then predicts the
4-bit vanishing pattern at each dual point from **type-level local data alone** (the reality class of
the level-3 windowed sum and the c₃-flip types of the two level-5 windowed sums). Two corollaries are
**derived and universally verified**: the all-dead stratum is exactly where the level-3 sum or the
level-5 quadruple vanishes; and the **`√−15` node is absent universally** — a live `√−15` channel
forces its `√5` partner dead, which is impossible in the pattern, so `(·,1,1,0)` never occurs
(checked on all 12 banked pairs).

This machinery passed a pre-committed **out-of-sample** test: for the never-computed pair `(4, 7)`
the entire channel table — the DARK verdict (0 `√−15` cells), the 31-cell value table
(hash-committed before computing), and the tier counts — was predicted from the two local theta
models alone and confirmed **cell-exact**.

## The single named residue (the sharp question)

Everything above is derived or a universally-checked finite census **except one lemma**:

- **L5b (the 5-side window-matching law).** For the pair's level-5 windowed sums, at every dual point
  the c₃-flip type of the `√5`-character window pair matches the trivial-window pair's, or dies.
  This is **true at all 240 points of the flagship pair `(1, 2)`** (and of 9 further banked pairs),
  and it is the only unproven input to the whole five-pattern law. But L5b is **provably not
  universal**: it **fails** on the sibling pairs `(1, 3)`, `(2, 4)`, and `(4, 7)` (where it produces
  a lattice-breaking non-lattice tier). Because it fails on siblings, no universal argument can prove
  it — any derivation must consume `(1,2)`-specific level-5 data.

So the surviving question is exactly, and finitely:

> **Why do the flagship pair `(1, 2)`'s 5-side windows never mismatch under the c₃-flip?** —
> equivalently, why does L5b hold for `(1, 2)` when it fails for `(1, 3)`, `(2, 4)`, `(4, 7)`? This is
> a finite, precisely posed question about one `(10, 6)`-periodic table of `ℚ(ζ₅)` parity-traces, on
> which the c₃-flip acts as the mirror `l ↦ −l` on the length-6 index. Is there a structural reason
> (a reciprocity / linking phenomenon) that the flagship pair never realizes the mismatch its
> siblings do, or is this genuinely pair-specific content?

## Why the off-the-shelf mechanism does not answer it

The natural candidate explanation — standard Galois-equivariance of modular data — is a **signed
permutation** `G_σ = σ(s)·s⁻¹` (Dong–Lin–Ng), which shuffles entries with signs and **can never send
a nonzero value to zero**. So the systematic vanishing of the `√−15` channel is *not* an instance of
the known Galois mechanism; that obstruction (originally B491) stands unchanged. The derivation above
does not contradict it — it routes the vanishing through the object's own CRT/character gates, not
through Galois-equivariance — and no new obstruction to a deeper derivation of L5b was found.

## Honest scope

This is a negative-existence verdict over the neighborhoods we could survey (Kurlberg–Rudnick,
Ladisch, Strömberg, Dong–Lin–Ng, Deloup–Turaev, Coste–Gannon); the specific cross-map pair invariant
and its one-node-absent vanishing rule were not found. A "known, see [reference]" answer closes the
question honestly.

**Provenance.** Rests on B459/P1 (the seam law and its bright/dark classification), B491 (the
signed-permutation obstruction and the novelty verdict), and B493 (the CL-1a duel: the derivation up
to L5b, the classifier theorem, the universal node-absence, and the `(4,7)` out-of-sample HIT). The
underlying invariant reuses the level-15 theta model (B358/B367/B396). Nothing promotes to
`CLAIMS.md`.
