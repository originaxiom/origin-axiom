# Success Atlas

Status: map of surviving structures. "Success" here means a result survived
the relevant governance gate; it does not mean final physics.

## Proven Core

The proven ledger is maintained in `CLAIMS.md`. The atlas does not restate that
ledger as authority; it explains the shape of what survived.

Current broad spine:

```text
L/R record operations
  -> A = LR
  -> trace 3, determinant 1, discriminant 5
  -> phi-spectrum
  -> figure-eight / punctured-torus monodromy host
  -> derived Mobius vector field
  -> derived cubic potential
```

The latest core expansion is the Session-3 synthesis: the vector field and
potential are exact consequences of the chosen based representative `A = LR`.

## Conditional Core

The strongest conditional result is formalized in
`docs/UNIQUENESS_THEOREM.md`:

```text
minimal-record axioms -> A = LR, up to order -> P1-P16
```

Why it matters:

- The conditional theorem compresses the core into a finite hypothesis set.
- The `12 x 12` local search collapses from 144 hyperbolic positives to one
  torsion-free primitive closure.
- The remaining binary order convention is visible instead of hidden.

Why it stays conditional:

- The axioms are motivated by the non-cancellation program.
- They are not derived from literal nothing.
- The order convention selects the golden representative rather than its
  mirror.

## Strong Surviving Observations

These are not all claims, but they guide future work:

- The from-nothing direction repeatedly stalls at inserted structure.
- The exact internal algebra of `A` keeps producing linked structures.
- The derived potential moved the project from a static skeleton to an exact
  dynamical object, while the physical lift remains open.
- Based data matter: conjugate matrices can share trace and spectrum while
  giving different fixed-point polynomials.
- The trace-map half-step campaign gives a canonical character-variety lift, an
  `SL(3)` higher-rank trace extension, and a finite-approximant Fibonacci
  spectrum anchor at dimensionless `lambda/h=1`; B38-B47 and
  `docs/TRACE_SELECTOR_THEOREM.md` further make the selector conditional on C5/T1,
  tangent-filter inheritance. This is useful conditional/frontier structure, not
  a physical prediction.

## The representation program (B59–B124)

The project's center of gravity moved from the "from-nothing" spine above to a single, fully-recognized
representation-theory object. Surviving structures, strongest gate first (full ledger in `papers/VALIDATION_LEDGER.md`,
narrative in `docs/archive/story/`, background in `knowledge/`):

- **`M⁴ = L` symbolic-exact at `SL(4)`** over `ℚ(ω)` (B89) — the figure-eight A-polynomial "degree = rank" relation
  proved exactly (`knowledge/K004`).
- **The Dickson tower `ρ_n = ⊕_d Sym^d(M)^{μ_d}`** proved exact at `n ≤ 4` (B80 from first principles; B103 made
  `char(ρ_n)` a **class function** of the abelianization — the same catalog for all metallic and non-metallic seeds,
  V87). `knowledge/K003`.
- **The sign half of the catalog, proved for all `n`** (B112, V99): the opposition involution `θ = −w₀` gives
  `mult char(±M^h) = ⌈/⌊(n−h)/2⌋` — engine-free. `knowledge/K005`.
- **`ρ_n = Sym^n(W) ⊕ (Sym^{n−3}(W) ⊖ W)`, `W = V⊕1`** (B122, V111): the tower named as symmetric powers of the
  **external monodromy fundamental** (`det W = −1`, B121/V109), a genuine `GL(2)`-module identity. `knowledge/K008`.
- **The `(n; trace, det)` determination** (B120, V107): the tower depends only on the rank and the seed's conjugacy
  invariants; m-universality of the `μ_d` content.
- **Three fixed-point classes** (B106) and **the per-eigenvector law** `Lᵢ = c·Mᵢ^k`; the geometric component `V0` =
  the `SL(3,ℝ)` Hitchin/Fuchsian locus (B101, V85).
- **`m=1` is special for three independent reasons** — systole (B92), expansion threshold (P004/B120),
  arithmeticity (B123: the unique arithmetic knot, Reid 1991). `knowledge/K009`.

**The standing prize (the wall):** prove the tower is **functorially** `Sym^n(W) ⊕ (Sym^{n−3}(W) ⊖ W)` — the missing
`Sym(W) → trace-ring` construction. The `n ≥ 5` explicit catalog stalls at exactly this point (three distinct
obstacles converge there, V91). The proven core `P1–P16` is independent of all of it; the physics chapter is CLOSED
(`knowledge/K006`, `K007`).

## What Counts As A Future Success

A future result should be classified by the strongest gate it actually passes:

- Proven: exact theorem or exact computation under stated hypotheses.
- Conditional: exact consequence of explicit assumptions not derived inside the
  project.
- Frontier: bounded probe with a named missing object.
- Dead: falsified, circular, or killed by controls.

For a physics bridge, the bar is higher:

```text
specific observable
fixed comparison target
independent parameter setting
clear failure condition
```

Without those, the result may still be good mathematics, but it should not be
promoted as physics.
