# THE CARRIER AND THE LOCK — Ψ = ℂ² ⊗ 27 is an exact π₁-module with 24 spinor×doublet slots, beat-closed with antiunitary square = the meridian; and its fermion-shaped sector is precisely where the spin-lift ambiguity cancels
## (outside bench, 2026-08-25; forty-sixth memo; the carrier question of memo 45, answered at the kinematic level; every check direct on the 54×54 matrices, no factor-wise shortcuts)

### The cell
Memo 45 proved the no-go half of the bridge: fermionicity cannot ride on the e₆
modules (integer-spin, exactly, through the whole tensor tower); the record's one
spin-½ object is the holonomy's ℂ². The minimal carrier the no-go permits is the
diagonal π₁-module
**Ψ = ℂ² ⊗ 27, γ ↦ ρ₂(γ) ⊗ ρ₂₇^int(γ)** — the tautological spinor tensored with
the internal (minimal-A1, memo-29) bridge. This cell verifies every algebraic
requirement the record can impose on it, and finds one it didn't ask for.

### THE THEOREM (`certificates/carrier.py`, all 54×54 over ℚ(q))
1. **Ψ is well-defined:** the relator acts as **+I₅₄** (direct word computation).
2. **The content:** joint (spin, internal) weight table
   {(±1,±1): 6 each = **24 doubly-odd states**, (±1,0): 15 each = 30 singlet-slots}
   — twenty-four spinor×doublet slots, the exact shape of chiral matter kinematics.
3. **The beat closes on the carrier:** β_Ψ = (W ⊗ U₂₇)∘conj intertwines the diagonal
   action exactly — ρ(a) fixed, ρ(b) ↦ ρ(w(b)) — and **β_Ψ² = ρ_Ψ(a): the beat's
   antiunitary square on the carrier is the meridian**, on the nose.
4. **THE LOCK (the unasked-for find):** the two spin lifts differ on Ψ by
   C_Ψ = (−I₂) ⊗ C₂₇ = diag((−1)^{1+wt}). This is **+1 on exactly the 24 doubly-odd
   states and −1 on the 30 others**: the lift-independent sector of the carrier IS
   the fermion-shaped sector. Spin parity and internal parity cancel precisely on
   the matter slots — a spin-internal lock, exact. The object still selects χ = +1
   at the group level (memo 28); the carrier's own matter sector never even feels
   the fork.

> **So the carrier question has a kinematic answer: Ψ exists, is unique-minimal
> given the no-go, satisfies every closure the record demands, and organizes
> itself — the physically shaped slots are exactly the projectively unambiguous
> ones. What remains beyond it is genuinely dynamical: a bundle, a Dirac operator,
> propagation. No such thing is claimed.**

### Interpretive note (labeled)
The lock has the flavor of a spin-charge relation: states with half-integer "spin"
carry odd internal charge and vice versa, enforced not by postulate but by the
arithmetic of the two central elements. In the freedom-ledger frame: on the carrier,
the spin bit and the internal parity bit merge into one bill — and it is already
paid.

### Fences
Exact throughout, all four claims computed directly on Ψ (no tensor-identity
shortcuts — the 54×54 relator, intertwinings, and square are evaluated as matrices);
the identification of ℂ²'s weight ±1 with "spin" is the holonomy-as-spin-cover
reading (thesis-level per B1145's fence — the algebra is exact, the 4d reading is
not a theorem); ρ₂₇^int is the minimal-A1 bridge (the fermion-capable choice, memo
45's dichotomy). Kinematics only. Gate 5 untouched.

### Certificates
`certificates/carrier.py`; output `outputs/carrier_out.txt`.

### One sentence for the ledger
The smallest thing the no-go allows turns out to be enough: two components of
holonomy woven into the twenty-seven make a module where the relator closes, the
beat squares to the meridian, and the twenty-four slots shaped like matter are
exactly the ones on which the spin fork's ambiguity annihilates itself — the
carrier exists, and it locks.
