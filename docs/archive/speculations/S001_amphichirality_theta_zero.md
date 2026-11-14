# S001 — amphichirality → θ=0 in `T[4₁]` (not 4d QCD)

**Status: `SUPPORTED` (the topology) + a pending verification.** Firewalled (`GOVERNANCE.md`); not a claim.

**Structural fact (cited).** The figure-eight knot `4₁` is **amphichiral** — equal to its mirror image — and has
`CS = 0` (`../CLAIMS.md` P9, software-verified census). The figure-eight complement is the mapping torus of
**`φ₁² = [[2,1],[1,1]]`** (the *square*, `Fix(T₁²)`, B67/B71).

**[PROVED, this round] Amphichirality is UNIVERSAL across the metallic family — it does NOT select `m=1`.**
For every `m`, the square monodromy `M_m² = [[m²+1, m], [m, 1]]` is **symmetric**; and any symmetric
`M ∈ SL(2,ℤ)` satisfies `S·M·S⁻¹ = M⁻¹` with `S = [[0,1],[−1,0]]` (verified symbolically + numerically for
`m=0..4`). So the bundle equals its mirror for the *whole* family — amphichirality is a property of the metallic
slice, not a distinguishing feature of `m=1`. **The systole (B92), not amphichirality, is what selects `m=1`.`**
This *resolves* the earlier "`m=1` uniquely amphichiral: UNVERIFIED" — the answer is **not unique, universal**.

**[LEAP] (kept separate).** In Chern–Simons theory, amphichirality gives `Z_k(M) = Z_{−k}(M)`, which forces the
analogue of `θ = 0`. *Read as:* a topological symmetry of the manifold forcing a physical-style symmetry with no
free parameter.

**Scope / honesty (the trims that keep it from overclaiming).**
- This is `θ = 0` **in `T[4₁]`** (a specific 3d N=2 theory), **NOT** "amphichirality solves Strong CP in 4d QCD."
  State it as a real structural distinction of *this manifold*, not a resolution of the physical puzzle.
- The amphichirality statement is about **`φ₁²`**, not the bare twist `φ₁`.
- ~~"**`m = 1` is uniquely amphichiral**"~~ — **RESOLVED (this round): NOT unique — ALL metallic `m` are
  amphichiral** (`M_m²` symmetric ⇒ `S·M²·S⁻¹ = (M²)⁻¹`). So amphichirality is *not* an `m=1`-selection criterion;
  the systole is. The structural fact is universal, which makes it a property of the *family* (a `θ=0`-type
  symmetry shared by every member), not a fingerprint of the golden seed.

**[HOOK] (bounded calc, not yet run).** Verify `Z_k(4₁) = Z_{−k}(4₁)` at SL(3) from B71's A↔B data — pure algebra
on `Fix(T₁²)`. *Caveat to honor:* the B71 relation `x1=x4, x2=x5` defines the V0 component / is a peripheral naming
convention; whether it *is* the mirror involution is part of what the hook checks, not an assumption. Second leg:
test `m ≥ 2` chirality.

**Negative beside the leap.** No dimensionful physics follows; `T[4₁]` is not the Standard Model. The value of S001
is a clean *topological* fact (#2 calculation pointer), not a claim about the strong interaction.

Related: `S004` (W1/W2 A↔B asymmetry), `S012` (θ=−w₀ → c), `PHYSICS_EXERCISE.md` T1.3.
