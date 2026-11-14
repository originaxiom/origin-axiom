# S012 — `θ=−w₀` predicts the Dehn-filling c-values (FEEDS ρ_n)

**Status: `TESTED-NEGATIVE` (on the full hinge) — degree=rank's `c` stays OPEN, reframed.** Resolved by **B108**
(V95). Firewalled; not a claim. The question fed the central math target directly — and the answer sharpens it.

**B108 verdict (the hinge: `θ` must predict *all four* `c`).** **NO.** `θ=−w₀` is an **involution (order 2)**: it
commutes with `J(m)` and organizes the tower (the *positive* half), and it predicts the order-`≤2` scalars
`c ∈ {1, −1}` (W1, W2, principal — matching `c=(−1)^{n−1}`, B83). But it **cannot** produce the **order-4**
secondary `c=i`: the contragredient sends `c ↦ c⁻¹` (`i ↦ −i`), so an order-2 symmetry sees the `ℤ/4` only as a
`ℤ/2` flip. **The missing ingredient is an order-4 (`ℤ/4`) structure `θ` does not carry** — candidate: the forced
cusp spectrum `{1, i, −i}` (B95). See `../frontier/B108_theta_to_c/`.

**Successor lead.** The peripheral `ℤ/4` is now a separate live lead, `S022` — B111 proved the cusp arithmetic
*controls* the exponent (the `M⁴`-scalar impossibility forces `k=3` on the secondary), so the cusp is the right
place; the covering-degree mechanism is the candidate (open). The bulk θ vs peripheral cusp split is the
`TWO_SYMMETRY_FRAME.md` reframing. (The `s_n↔c` variant of this conjecture is also DEAD, same parity argument —
`TOMBSTONES.md`.)

**Structural facts (cited).** (i) The Dehn-filling components carry per-eigenvector scalars `c ∈ {1, 1, −1, i}`
(B106 D4: SL(3) `c=1`; SL(4) principal `c=−1`, secondary `c=i`). (ii) The opposition involution `θ=−w₀` splits the
height-2 root spaces asymmetrically `(2,0),(2,2),(4,2)` at `n=3,4,5` (B62, structural). (iii) B83 already gives
`c=(−1)^{n−1}` for the principal matching.

**The question (math, not physics).** Does `θ=−w₀` **predict** the full `c`-set — in particular the open secondary
`c=i` — directly from the root-system combinatorics? If yes, the three-phase vacuum architecture has a spine **and**
the prediction reproduces the opposition-involution multiplicities that are the **sharpened ρ_n target** (V90/V91).

**[HOOK] (the one that pays the rent).** Derive the `c`-values from `θ=−w₀`. This is a **bounded Lie-theory
computation already on the math roadmap** — the single most leveraged item in the whole speculation folder, because
it is simultaneously (a) the "what residual symmetry labels each vacuum" reading and (b) a step toward proving
`char(ρ_n) = catalog`. **It decides whether the off-locus sector (`S011`) is determined or independent.**

**Discipline note.** Until derived, label it ACTIVE/open — `c=(−1)^{n−1}` matches the principal, but the secondary
`c=i` is unproven. This is the *one* speculation whose hook lands inside `../frontier/` math; when derived it leaves
this folder for a `B`/`V` number.

**Probe notes (closed sub-routes — do not re-derive).**
- The **simple weight-space route** is **closed**: `θ=−w₀` acting on the A-eigendecomposition does *not* give `c`
  directly through eigenvalue counts. The per-eigenvector `c` comes from the **commutator residue**
  `[A,B]·μ^k = c·Id`, a property of the commutator structure, not of `A`'s weights alone.
- **Order mismatch.** The `c`-values are roots of unity of orders `{1, 2, 4}` (`c ∈ {1, −1, i}`), but the forced
  *cusp eigenvalue* orders are `{4, 3, 8}` (the `2cosθ=3−n` spectra) — **no simple order-preserving mapping**.
- So the derivation, *if it exists*, goes through **deeper Lie theory** (the explicit-matrix / tangent-space route
  of B108, not the naive weight count). Recorded so the explicit route is attempted, not the dead simple one.

Related: `S011`, `S004`, `PHYSICS_EXERCISE.md` pointer #1; the central target = the `ρ_n` catalog proof.
