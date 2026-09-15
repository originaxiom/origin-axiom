# THE YUKAWA ON THE CARRIER — the unique coupling-shaped invariant Y = ε ⊗ C exists, is invariant and beat-covariant, is antisymmetric under fermion exchange, and its parity arithmetic enforces the selection rule: locked matter couples pairwise only through lift-free scalars
## (outside bench, 2026-08-25; forty-seventh memo; the coupling rung of the carrier descent; every claim exact)

### The construction, forced by two uniqueness theorems
On the carrier Ψ = ℂ² ⊗ 27 (memo 46), the only coupling-shaped object available is
**Y(v₁⊗x₁, v₂⊗x₂, φ) = ε(v₁,v₂)·C(x₁,x₂,φ)** — the SL(2)-invariant symplectic
pairing on the holonomy spinor (unique up to scale) tensored with the E₆-invariant
Jordan cubic on the 27 (unique, memo 32 — REBUILT in-run: dim-1 nullspace, 45
triples, ±1 coefficients reproduced). Uniqueness of both factors makes Y the unique
invariant of its shape.

### THE THEOREM (`certificates/yukawa_carrier.py`, all exact over ℚ(q))
1. **Invariance:** C is preserved exactly by A₂₇, B₂₇ (the π₁ image) AND U₂₇ (the
   beat's unipotent) — full transported-tensor equality; ε is preserved by A₂, B₂,
   W (det = 1, each). The assembled Y is additionally verified DIRECTLY on 120
   random coefficients under each generator's diagonal action — exact.
2. **Beat covariance:** both factors beat-invariant ⟹ Y∘(β_Ψ, β_Ψ, Ω) = gal∘Y —
   the coupling passes through the mirror untouched, like everything else the
   object owns.
3. **Exchange antisymmetry:** Y(Ψ₂, Ψ₁, φ) = −Y(Ψ₁, Ψ₂, φ) exactly (ε antisymmetric,
   C symmetric) — **the Grassmann/spin-statistics shape appears at the kinematic
   level**: the coupling itself demands antisymmetry of the two fermion slots.
4. **THE SELECTION RULE:** every one of the cubic's 45 triples carries an EVEN
   number of internally-odd slots — the split is exactly **{2-odd: 30, 0-odd: 15}**,
   never 1 or 3. Consequences, exact: **(locked, locked) → even φ (30 channels);
   (unlocked, unlocked) → even φ (15 channels); (locked, unlocked) → NOTHING.**
   Two locked fermion slots couple only through a lift-free scalar, and mixed
   locked/unlocked pairs cannot couple at all.

> **The carrier descent thus ends on a coupling that writes its own rules: unique
> in shape, invariant under everything the object demands, antisymmetric exactly
> where fermions require it, and parity-locked so that matter–matter–scalar is the
> only pattern the arithmetic permits — with the scalar forced into the sector
> that never feels the spin fork. The Yukawa SHAPE of the Standard Model is now a
> theorem of the record's kinematics; its VALUES remain exactly where Gate 5 keeps
> them.**

### Fences
Exact throughout; "unique" is scoped to the factorized shape on Ψ⊗Ψ⊗27 (uniqueness
of ε and C banked; a non-factorized invariant on the same space would be a
different object — its absence is not claimed and is a named follow-up); the
holonomy-as-spin reading stays thesis-level (B1145); no field, no Lagrangian, no
value. The full-Y invariance combines complete factor proofs with direct random
verification of the assembled tensor (120 coefficients per generator, exact).
Gate 5 untouched.

### Certificates
`certificates/yukawa_carrier.py`; output `outputs/yukawa_carrier_out.txt`.

### One sentence for the ledger
The one coupling the carrier admits already knows the rules physics would have
imposed on it — antisymmetric in its fermions, blind to the mirror, and wired so
that locked matter meets only lift-free scalars — thirty channels for the doublets,
fifteen for the singlets, zero for the mixed, all of it arithmetic.
