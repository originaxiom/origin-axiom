# B1268 — addendum (2026-09-06): the remaining computation is closed by a theorem (B1280)

§3 of the findings left one computation named and bounded in advance: the locus near the geometric point where the
θ-odd cusp holonomy (μ_s, λ_s) keeps a common fixed vector on the 27 — the only place |N(27)| = 1 was still allowed —
registered as **L200**. It is closed without being found. **B1280** (`frontier/B1280_the_chirality_probe/verification/theta_odd_pairing.py`,
exact over two primes) computes the action of the object's inversion ι (a ↦ a⁻¹, b ↦ b⁻¹) on the six deformation
classes H¹(M; V_n), n ∈ {2, 8, 10, 14, 16, 22}, of the E₆ holonomy: the signs are (+, −, +, +, −, +) — exactly the
signs of the E₆ outer automorphism θ (+1 on f₄ = V₂ ⊕ V₁₀ ⊕ V₁₄ ⊕ V₂₂, −1 on the 26 = V₈ ⊕ V₁₆). Two commuting
involutions of the germ of the E₆ character variety at [ρ₀] with the same action on the Zariski tangent space are
equal on the germ, so θρ ≅ ι\*ρ for every ρ near ρ₀, hence 27̄_ρ ≅ ι\*(27_ρ) and **N(27_ρ) = 0 identically** — on
m004 and on every cusped cyclic cover (ι lifts). The bound −h⁰ ≤ N ≤ h⁰ of §1 is sharpened to N = 0 near the
geometric point, θ-odd or not; the θ-odd point of §3 (N = 0 with no cusp invariants) is one instance. Nothing in
§§1–4 changes; the "named remaining computation" of §3 is done. See `docs/CHIRALITY_MAP_2026-09-06.md`.
