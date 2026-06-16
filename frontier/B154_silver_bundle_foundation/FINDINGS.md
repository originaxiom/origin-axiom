# B154 — the silver bundle (m=2, R²L²): foundation for the degeneration-generality question

**Date:** 2026-06-15. **Status:** FOUNDATION (verified) — the generality question is **OPEN**. Standalone
low-dim topology / character varieties; no physics, no Origin-core claim; P1–P16 untouched; nothing to
`CLAIMS.md`. Probe: `probe.py` (pyenv); exact derivation: `silver_tracemap.sage` (Sage). Ledger: V146.

## Question (Phase C of the B153 campaign)
Does the rank-stratified degeneration of degree=rank (`L=(−1)^{n-1}Mⁿ`: genuine component at n=3, slice at
n=4, absent at n=5 — [[../B153_degree_rank_degeneration]]) **generalize** from the figure-eight (m=1, `RL`)
to the **silver bundle** (m=2, `R²L²`), or is it figure-eight-specific?

## Established (verified)

1. **The silver monodromy.** On `F₂=⟨A,B⟩`, with Dehn twists `σ_R: A↦A, B↦AB` and `σ_L: A↦AB, B↦B`:
   - figure-eight `φ = σ_R∘σ_L`: `A↦A²B, B↦AB` (abelianization `[[2,1],[1,1]] = M₁²`) — matches the toolkit;
   - **silver `φ = σ_R²∘σ_L²`: `A↦A³BA²B, B↦A²B`** (abelianization `[[5,2],[2,1]] = M₂²`, trace 6).

2. **The trace-map fixed locus = the bundle SL(2) character variety.** Bundle reps are the fixed points of
   `φ` acting on the Fricke coordinates `(x,y,z)=(tr A, tr B, tr AB)`. **Convention (a bug-class caught here):
   characters transform CONTRAVARIANTLY**, so the trace map of `φ=σ_R∘σ_L` is `t(σ_L)∘t(σ_R)` (reversed),
   where `t(σ_R):(x,y,z)↦(x,z,xz−y)`, `t(σ_L):(x,y,z)↦(z,y,yz−x)`. The figure-eight control then reproduces
   **B67 exactly** (`y=z=x/(x−1)`, `κ=x²+z²−x−z−2`) — the validation gate.

3. **The silver SL(2) character variety** (Sage, exact): the det-saturated fixed locus has **2 components**.
   The **geometric component** is `y = xz/2`, `x²z² − 2z² − 8 = 0` (i.e. `x² = 2 + 8/z²`), carrying
   **`κ = tr[A,B] = ½z² + 8/z² − 2`** — *distinct* from the figure-eight's `κ = x²+z²−x−z−2`. (The other
   component is the degenerate `x=y=0`, `κ=z²−2`.) Verified numerically (`probe.py`) and symbolically.

4. **The monodromy `t`** (`tA=φ(A)t`, `tB=φ(B)t`) is solved convention-free over the `E_ij` basis
   (residual ~1e-15); needed for the peripheral / degree=rank analysis.

## Open (Phase C continues)
- **The silver principal spectrum** — the B95-analogue for `R²L²` (degree=rank is a relation at the
  *principal / forced finite-order* point, NOT generic on the curve; a first peripheral scan over generic
  points shows no clean `L=±Mᵏ`, as expected).
- With it: the **SL(n) silver degeneration** at n=3,4,5 — component / slice / absent? Is the exponent still
  `n` (as figure-eight) or `m·n` / different for `m=2`? Reuse `../B153.../sln_toolkit.py` (general in n).

## Method notes (verify-don't-trust payoffs)
Two of my own bugs were caught by the figure-eight control before any silver conclusion: (i) the trace-map
**composition order** (contravariance — `t(σ_L)∘t(σ_R)`, not the reverse); (ii) the **`vec` convention** in
the monodromy solver (numpy `reshape` is row-major; the `kron` `vec(XYZ)=(Zᵀ⊗X)vec(Y)` identity is
column-major) — fixed by building the linear map over the `E_ij` basis. A control that must reproduce a
known answer (here B67) is the cheapest guard.

## Reproduce
```bash
python frontier/B154_silver_bundle_foundation/probe.py
sage   frontier/B154_silver_bundle_foundation/silver_tracemap.sage   # exact fixed locus (needs Sage)
python -m pytest tests/test_b154_silver_bundle_foundation.py -q
```
