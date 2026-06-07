# Speculation catalog — `S001…S027`

The index of the project's speculative readings. **Firewalled** (see `GOVERNANCE.md`): nothing here promotes to
`../CLAIMS.md`; speculations cite proved results, never the reverse; the physics chapter stays CLOSED. Status enum:
`POSTULATED / SUPPORTED / TESTED-POSITIVE / TESTED-NEGATIVE / HELD(value-matching) / DORMANT / WALLED / DEAD`. The
full physics-bridge terrain (dead/live/heavy) is mapped in **`PHYSICS_BRIDGE_MAP.md`**.

Live speculations have a per-entry file (`S0xx_*.md`); DEAD ones are epitaphs in `TOMBSTONES.md`. The long-form
exercise that generated these is `PHYSICS_EXERCISE.md`.

| ID | speculation | status | evidence / depends |
|---|---|---|---|
| S001 | amphichirality → θ=0 in `T[4₁]` (not 4d QCD; about `φ₁²`; **ALL metallic `m` amphichiral — PROVED**, `M_m²` symmetric; the systole, not amphichirality, selects `m=1`) | SUPPORTED | B67, B71, B92 |
| S002 | arrow of time = trace-map flow direction (no e-folds) | SUPPORTED | B106; D2 pending |
| S003 | κ-conservation (structural); flatness = Ω is analogy | SUPPORTED | quasicrystal anchor (B107) |
| S004 | W1/W2 (A↔B) asymmetry, structural | SUPPORTED | B102, B106 |
| S005 | baryon-asymmetry amplitude `|Z(W1)/Z(W2)| ≈ 10⁻⁹` | HELD(value-matching) | B106 D1 |
| S006 | Bell/CHSH on the Fricke surface — the *classical* variety is deterministic (`z=f(x,y)`) ⇒ CHSH ≤ 2, cannot violate Bell; a real test needs the quantized variety (`SU(2)_k`) | TESTED-NEGATIVE | — |
| S007 | mass gaps = gap-labeling structure of the SL(n) operator | POSTULATED | gap-labeling (Bellissard, external) |
| S008 | trace-map orbit count (DORMANT-D2) \| "iterations = e-folds" (HELD) | split | D2 pending |
| S009 | confinement from `M³=L` | DORMANT | SL(3) Wilson loops |
| S010 | n=4 boundary = `W₄` truncation | DORMANT | L5 literature |
| S011 | irreducible OFF-locus sector (the open fork; **NOT** B106) — **B110: EMPTY for 4₁ at SL(3)** (all 3 irreducible components on the forced locus, HMP); narrowed to higher-rank / other-manifold, still OPEN | ACTIVE (narrowed) | **B110**, HMP 1505.04451 |
| S012 | θ=−w₀ predicts the Dehn-filling c-values (FEEDS ρ_n) — **B108: NO** on the hinge; θ (order 2) predicts the order-`≤2` c but not the order-4 secondary c=i; degree=rank's c stays OPEN, missing a ℤ/4 ingredient | TESTED-NEGATIVE | B62, B106, **B108** |
| S013 | hierarchies = powers of one scale (structural); value-match = HELD | SUPPORTED | — |
| S014 | cosmological-constant **value** | DEAD | null hypothesis (`../CLAIMS.md` D1–D3) |
| S015 | tower eigenvalues = masses | DEAD | dictionary correction (B107) |
| S016 | Goldman metric (1,1) Lorentzian | DEAD | computation gives (2,0) |
| S017 | phase-space 3+1D at SL(3) | DEAD | B101 split-form ladder |
| S018 | spacetime tower up the ranks | DEAD | B101 split-form ladder |
| S019 | Fisher metric on CS level k | DEAD | heuristic, not rigorous |
| S020 | 3+1D from Cartan geometry | WALLED | type-mismatch (3d→4d) |
| S021 | entanglement = holographic | TESTED-NEGATIVE | generic CFT (V37) |
| S022 | the peripheral ℤ/4 for degree=rank's `c` (the successor to θ→c; B111 proves the cusp arithmetic controls the exponent; covering-degree is the candidate mechanism, OPEN) — **scoped low-rank `n∈{3,4}` (B120/V107)** | ACTIVE (lead) | B95, B76, B106, **B111**, B120 |
| S023 | the **metallic means are genuinely distinct real quasicrystals** — gap-label fields `ℚ(√5),ℚ(√2),ℚ(√13)`, RG scale `φ_m`, spectral dim all m-distinct, even though the tower algebra is m-universal (B120). 1D condensed matter, firewalled (Phase 1 of `PHYSICS_BRIDGE_MAP.md`) | **TESTED-POSITIVE** | **B120**, B107, K007 |
| S024 | the tower lives on the **monodromy side of Hitchin**, separated from the Fuchsian/principal section by the `det=−1` parity (the math is **proved**, B121; the Hitchin/Langlands/class-S reading is the firewalled leap, ceiling N=4 SYM) | POSTULATED | **B121**, B101, K006 |
| S025 | independent spectral content **off the principal locus at higher rank** (the S011 continuation) — EMPTY for 4₁/SL(3) (B110); open only at SL(4)/SL(5) or other manifolds; obstruction = no SL(4) char-variety classification + non-Hermitian realization | DORMANT | B107, B110, B115 |
| S026 | does the SL(n) tower **organize the `T[4₁]` state-integral** (fixed knot, varying rank)? — moduli/A-variety level in-house (B71/B83, vol B82); quantum state-integral at higher rank = heavy/deferred (quantum-dilog) | DORMANT | K006, B71/B83, B82 |
| S027 | the **metallic Kashaev invariants as a family of quantum modular forms** (the `GL(2,ℤ)` cocycle) — feasibility in-house (`kashaev_feasibility.py`: `J_N(4₁)→vol`); open = the cocycle + the per-knot arithmetic in `ℚ(√(m²+4))` (the continuous family-in-m is DEAD, Gate 1) | DORMANT | B82, V37–V38, S023 |

**Reading the pattern (the organizing insight).** Every `SUPPORTED`/`ACTIVE` entry is **structural** (symmetry,
hierarchy, vacuum architecture, the direction of flow); every `HELD`/`DEAD` entry asks for a **value** or a
**real-time dynamics**. The framework is a theory of *the architecture of the possible, not the furniture of the
actual* — and the catalog is that insight in ledger form. The five ranked **calculation pointers** (the only
output the exercise licenses) are in `PHYSICS_EXERCISE.md`; the top one, **S012 (`θ=−w₀ → c`)**, feeds the central
`ρ_n` proof directly.
