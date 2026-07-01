# B347 — the E₆ character-variety tangent of the figure-eight, and its two ℤ/2 gradings

**Status: banked (frontier) as standalone low-dimensional topology / character-variety data. Computer-assisted
(mpmath, high precision), self-verified. Firewalled; nothing to `CLAIMS.md` — no physics claim.** This is the
*correct* replacement for a cross-session handoff whose "E₆ dictionary" rested on a mis-computed E₆ Cartan spectrum
(the claimed eigenvalues `{2−√3, 3, 2+√3}` are the **G₂⊕A₂** spectrum, not E₆'s — E₆'s Cartan matrix has six
*distinct* eigenvalues `2−2cos(mπ/12)`). Here the tangent is computed from the actual object.

## The object (the correct bridge: the principal SL₂)

`ρ₀ : π₁(4₁) → SL(2,ℂ)` is the geometric (discrete-faithful) holonomy of the figure-eight. Compose with the
**principal homomorphism** `SL(2) → E₆`, whose spins are the **E₆ exponents `{1,4,5,7,8,11}`**; the E₆ adjoint
decomposes as `𝔢₆ = ⊕ᵢ Sym^{2mᵢ}` (dims `3+9+11+15+17+23 = 78`). Hence the Zariski tangent to the E₆ character
variety at `ρ = (principal)∘ρ₀` is a **sum of twisted cohomologies of the figure-eight at the exponent spins**:
`H¹(π₁(4₁), 𝔢₆) = ⊕ᵢ H¹(4₁, Sym^{2mᵢ})`. This ties the E₆ story to the repo's own trace-map/monodromy-grading
tower (B67, B121, B264/B265) — *not* a "Cartan ⊗ gluing tensor". Computed by Fox calculus on the SnapPy census
presentation `⟨a,b | a b³ a B A² B⟩` (relator self-verified against the hard-coded rep to `~1e-70`).

## Results (all reproduced by `run_all()`)

**1. The correct tangent: `dim H¹(4₁, Sym^{2m}) = 1` for every exponent ⇒ total `= 6 = rank E₆`.**
The sl₂ anchor `dim H¹(4₁, Sym²) = 1` comes out exactly (as it must — the A-polynomial curve). The ranks are
unambiguous (singular-value gaps `10⁸⁵–10¹¹⁹`). So the "6-dimensional moduli space" is real, but the honest grading
is **uniform — one deformation direction per exponent, none privileged.** This **refutes** the handoff's
degenerate-cascade reading (three doubly-degenerate "breaking scales, softest breaks first"): all six exponents
contribute *equally*.

**2. Amphichirality acts uniformly.** The orientation-reversing involution `σ₋` (`a→ababAB, b→baBA`, verified
`ρ∘σ₋ = D ρ̄ D⁻¹`) acts on each 1-dim line as a **real structure `J² = +1`** — uniformly, no split. So amphichirality
does **not** select among exponents; it is a uniform symmetry of the deviation space (CP-even everywhere),
consistent with "the object is the symmetric, achiral centre" (K022) — a clean negative.

**3. The hyperelliptic involution grades onto the E₆→F₄ split.** The orientation-*preserving* involution
`a→a⁻¹, b→b⁻¹` (the fibre-torus hyperelliptic involution; `σ²=id` exactly) is ℂ-linear and grades the six lines by
**`ε_m = (−1)^{m+1}`**:

| exponent m | 1 | 4 | 5 | 7 | 8 | 11 |
|---|---|---|---|---|---|---|
| hyperelliptic sign | **+** | **−** | **+** | **+** | **−** | **+** |

- **`−1`-eigenspace `= {4,8}`** — *exactly* the `𝔢₆/𝔣₄ = 26` coset (B265's "escape" sector, E₆-Zariski-dense).
- **`+1`-eigenspace `= {1,5,7,11}`** — *exactly* the **F₄ exponents**.

So the figure-eight's own ℤ/2 symmetry splits its E₆ tangent along the **E₆ → F₄ folding**, and its `−1`-eigenspace
is the escape sector B265 showed generates all of `𝔢₆`. A symmetry origin for the escape/trapped split.

## Honest tiers

- **Exact-verified:** the tangent dimensions (rank gaps `10⁸⁵⁺`), the sl₂ anchor `= 1`, both involutions'
  eigenvalues (`|Im|` down to `10⁻⁵⁵`, cocycle residuals `10⁻⁴⁰…10⁻⁸⁸`), the relator and `symrep`-homomorphism checks.
- **Structural fact (not this computation):** `{4,8} = 𝔢₆/𝔣₄` coset is B265; `{1,5,7,11}` are the F₄ exponents.
- **OPEN (flagged, not claimed):** whether the hyperelliptic involution *literally acts as* the E₆ diagram
  involution `θ` (both currently give the same signs because both equal exponent parity `(−1)^{m+1}`) — a
  representation-theoretic identity to prove, not yet a coincidence-vs-theorem verdict. And the E₆-*irreducibility*
  / integrability of the `{4,8}` directions is B265/B270's open cup-product obstruction, untouched here.

## Firewall

Standalone topology of the figure-eight complement; **no physics claim**. The `E₆ → F₄` split is Lie theory; any
reading of these directions as "flavor / breaking scales" is *not* asserted (that was the handoff's overreach). The
value of this probe is a *correct* object where the handoff had a broken one, plus two forced structural gradings
(forms, not values).

**Provenance.** Principal-SL₂/adjoint decomposition: standard. Twisted-cohomology / trace-map tower: B67, B121.
E₆ character variety + escape/trapped `{4,8}`/`{5,7,11}`: B264, B265 (+B270 obstruction). Symmetric-centre /
amphichirality-as-form: K022, B318, B289. Supersedes the cross-session E₆-dictionary handoff (its E₆ Cartan spectrum
was G₂⊕A₂). Reproducer: `e6_tangent_gradings.py`; test: `tests/test_b347_e6_tangent_gradings.py`.
