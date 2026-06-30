# B293 — The emergent clock: the peripheral symplectic structure (Goldman = NZ), trajectory gated

**Status: banked (frontier). The symplectic clock is verified two ways; the trajectory is a stop-gate. Nothing to
`CLAIMS.md`.** Phase V of the seam arc (dynamics / time). B286 noted the clock is peripheral (`H₁(cusp)=ℤ²`,
`⟨μ,λ⟩=1`); B293 makes the symplectic structure explicit and reads its meaning, with the physics firewalled and the
trajectory gated.

## The result — the clock is the peripheral symplectic pairing (two methods)
1. **Goldman bracket** (the character-variety symplectic form). On the figure-eight (once-punctured torus)
   `SL(2,ℂ)` character variety with `x=tr a, y=tr b, z=tr ab`:
   ```
       {x,y} = 2z − xy,   {y,z} = 2x − yz,   {z,x} = 2y − xz,
   ```
   and the **boundary/commutator trace `κ = x²+y²+z²−xyz−2`** (= `tr[a,b]`) is the **Casimir** (`{κ,·}=0`). So the
   cusp data is **Poisson-central**; the symplectic **leaves are `{κ=const}`**, and on each leaf the peripheral
   `(μ,λ)` holonomies are a **canonical conjugate pair** — the clock.
2. **Neumann–Zagier frame** (B263). The peripheral NZ datum has `A·Bᵀ` symmetric (a valid **Lagrangian**), and the
   mixed BF coupling `k_um = −1` (a **unit** pairing) realises the `μ ↔ λ` conjugacy. The **same** canonical structure
   as (1), computed independently.

A **filling slope `(p,q)`** picks a **Lagrangian line** in the peripheral `(μ,λ)` plane — a choice of "time
direction"; the conjugate variable is the evolving one. (This is the same "filling = polarization" the seam reframe
named.)

**Honest caveats (red-team, Arc II).** Three scoping points, none affecting the claim as worded but worth stating:
(a) the `kappa_is_casimir()` check follows from the **Nambu-bracket construction** (`{κ,·}=0` for *any* cubic via the
repeated-vector triple product) — the *content* is the identification of this bracket with the **Goldman** bracket and
`κ` with the boundary trace `tr[a,b]`, imported from Goldman/Fricke, not derived here; (b) `A·Bᵀ` symmetric is the
**generic** Neumann–Zagier theorem (true for every ideal triangulation of every cusped manifold), instantiated here,
not a figure-eight-specific fact; (c) the BF coupling **`k_um=−1` is frame-dependent** (the `Sp(2,ℤ)` duality group;
B263 notes the frame-invariant content is the partition function) — the frame-**robust** reading is "a *unit* mixed
pairing," and that is what realises the `μ↔λ` conjugacy. "Goldman = NZ" is the standard interpretive identification,
asserted (the two pictures each carry a symplectic structure), not an exhibited isomorphism.

## [HOOK — firewalled] the Λ ↔ CS-time resonance
Alexander–Magueijo–Smolin 2018 (`arXiv:1807.01381`, logged in S044) make physical **time emerge as the variable
conjugate to `Λ`** (Chern–Simons time). The peripheral symplectic pairing is the **structural analog** — a
Hamiltonian / conjugate-pair skeleton. This is a genuine resonance (the object carries exactly the conjugate-pair
structure the physics uses), tagged `[HOOK]`, not a derivation.

## [STOP-GATE] what is not in-sandbox
- The **derived `k(t)` trajectory** is **not** computable here (S044: *conjugacy yes, trajectory no*); the
  **122-order gap** stands. A conjugate pair is a Hamiltonian structure, not a solved flow — and a flow still needs an
  initial condition to locate "now."
- Whether the running clock **dynamically gauge-fixes** the `τ`-sign (the live frontier from B295) is the **shared**
  open question of B293 + B295 — the *structure* is here, the *trajectory* is specialist-gated.

## Where this lands
B293 banks the **clock as math**: the peripheral symplectic pairing (Goldman = NZ), with the cusp trace as Casimir
and the filling as a polarization. It does **not** derive an arrow, a rate, or `k(t)`. Consistent with the seam
reframe: the object carries the conjugate-pair *structure* (the clock skeleton) in its boundary; the *trajectory* (the
actual evolution) is not supplied.

## The fence
Symplectic geometry of the character variety, computed two ways. The emergent-cosmological-time reading is
**HELD/[LEAP]** in `S002`/`S044`; the trajectory is a stop-gate. Nothing to `CLAIMS.md`.

`peripheral_clock.py` (pyenv: Goldman bracket + Casimir + B263 NZ frame) · `verdict.py` ·
`tests/test_b293_peripheral_clock.py`. Related: `B286` (the seam, peripheral clock), `B263` (the NZ frame), `B71`
(μ,λ machinery), `B285`/`B289`/`B295` (the τ-sign and the gauge-fixing frontier), `S002` (the dynamics fork),
`S044` (Alexander Λ↔CS-time).
