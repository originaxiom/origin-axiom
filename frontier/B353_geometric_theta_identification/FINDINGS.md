# B353 — the geometric θ-identification: the hyperelliptic involution *is* θ on the E₆ tangent (L52)

**Status: banked (frontier) as computer-assisted (mpmath dps 100) standalone Lie theory + twisted
cohomology. Closes B347's last open item (L52), completing the arc B347 → B351 → B352 → B353.
Firewalled; nothing to `CLAIMS.md`; no physics claim.**

## The question

B347 computed that the figure-eight's **hyperelliptic involution** (`a→a⁻¹, b→b⁻¹`) acts on the six
tangent lines `H¹(4₁, Sym^{2m})` of the E₆ character variety by `(−1)^{m+1}`, and flagged as open
whether this *is* the **E₆ diagram involution θ** or a sign coincidence. B351 half-settled it
(θ's eigenvalue on each exponent *line* is the same `(−1)^{m+1}`, exact). What remained was the
**operator-level identification** through the module isomorphism `𝔢₆ = ⊕ₘ Sym^{2m}` — signs matching
per line is weaker than the involutions *being the same map*.

## Results (all at the dps-100 precision floor; `run_all()` reproduces)

- **(A) θ in the geometric basis IS the block-scalar operator** `⊕ₘ (−1)^{m+1} Id_{2m+1}`:
  transporting B351's exact θ (root basis, entries in `{0,±1}`) through B352's `S`-intertwiner into
  the chain/symrep basis gives the full 78×78 identity with **max residual `7.1e-102`**. (Schur —
  θ commutes with the principal sl₂ and each `Sym^{2m}` has multiplicity one, so θ *must* be `±1`
  per block; here the whole matrix identity is verified, not inferred.)
- **(B) θ commutes with the full holonomy Ad-image** (`X_root(a)`, `X_root(b)`; residual `1.8e-88`):
  θ fixes the principal SL₂ subgroup pointwise, so the σ-twisted and θ-twisted Fox complexes are the
  *same* complex, and `Θ(z) = θ∘z` is a chain map.
- **(C) The gauge certificate, line by line:** for every exponent `m ∈ {1,4,5,7,8,11}`, the
  hyperelliptic cocycle action satisfies `J(z₀) = (−1)^{m+1} z₀ + d⁰(v)` with an **explicit
  coboundary** `v` — least-squares certificate residuals `9.9e-72 … 3.6e-79`, eigenvalue exactly
  `(−1)^{m+1}` (imaginary parts ≤ `1e-65`).

**Conclusion.** The hyperelliptic involution induces **exactly θ** on the tangent space of the E₆
character variety at the principal-geometric representation — as operators on the deformation
complex (gauge-certified), not merely as matching sign patterns. Combined with B347(3)/B351(vi):
the manifold's own ℤ/2 symmetry realizes the **E₆ → F₄ folding**, and its `(−1)`-eigenspace is the
`𝔢₆/𝔣₄ = 26` escape sector whose second-order integrability B352 established.

## Honest scope

- **Settled:** the tangent/deformation-complex level at the principal-geometric point (the H¹-level
  intertwining L52 asked for, with explicit gauge certificates).
- **Not claimed:** the global, variety-level statement (`ι* = θ*` as automorphisms of the whole E₆
  character variety away from this point) — the natural conjectural frame, untested.
- Numerics: mpmath dps 100 throughout; residuals sit at the precision floor of each object
  (`1e-102` for the exact-integer θ transport; `1e-72…1e-88` for the holonomy-dependent parts,
  matching B352's machinery-integrity scale). Two independent code paths touch θ (root-basis
  commutators; chain-basis transport).

**Provenance.** Machinery: B351 (exact 𝔢₆, `theta_map`), B352 (two-basis architecture, `S`,
`X_root`), B347 (Sym-block Fox cohomology, the hyperelliptic `D`). Question: B347 "OPEN" flag = L52
(`docs/OPEN_LEADS.md`). Reproducer: `geometric_theta.py`; test:
`tests/test_b353_geometric_theta_identification.py`. Next in the arc: **L53** (third-order /
Massey obstruction).
