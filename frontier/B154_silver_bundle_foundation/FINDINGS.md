# B154 — the silver bundle (m=2, R²L²): foundation for the degeneration-generality question

**Date:** 2026-06-15 (updated 2026-06-16). **Status:** FOUNDATION verified + **SL(3) partial result**
(degree=rank generality is genuinely *weaker* for silver — see below); full characterization OPEN. Standalone
low-dim topology / character varieties; no physics, no Origin-core claim; P1–P16 untouched; nothing to
`CLAIMS.md`. Probes: `probe.py` (SL(2) foundation), `silver_construct.py` (SL(n) construction + scan); exact
derivation: `silver_tracemap.sage` (Sage). Ledger: V146.

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

## Partial progress (SL(2)–SL(3), verified) — silver degree=rank is WEAKER than figure-eight

The silver bundle relations eliminate (R1+R2) to the clean degree-2 system in `(B,t)` given `A`:
`F1: tB² = A⁻¹tA` and `F2: tBt⁻¹ = A²B` (with `{F1,F2} ⟺ {R1,R2}`, verified). This is the silver analogue of
B89's construction (`silver_construct.py`). The SL(2) build reproduces `κ=½z²+8/z²−2` (validation).

**SL(3) spectrum scan + skeptical verification** (the verification matters — the raw scan's "best err 1e-15"
was a cherry-picked single rep):
- `{1,ω,ω²}` (order 3): 38 irreducible silver reps; `L=Mⁱ` with `M=eig(t)` holds **as an eigenvalue relation
  on only ~10/38**, exponent `i=4`; the **matrix identity `[A,B]=t⁴/det t` holds on 0/38** (median err ~4).
- `{1,i,−i}` (order 4): 29 irreducible; eigenvalue `L=M²` on ~4/29; matrix identity **0/29**.
- `{1,1,1}`, `{ω,ω,ω}`: 0 irreducible. Generic: irreducible but no relation.

**Conclusion (verified):** silver does **NOT** carry the figure-eight's *uniform matrix-identity* degree=rank
(`[A,B]=(−1)^{n-1}µⁿ` held on the *entire* spectrum-locus for figure-eight, B149). For silver there is at
most an **eigenvalue relation on a sub-locus** (~26% of the irreducible reps at a given finite-order
spectrum), with a spectrum-dependent exponent (4 at order-3, 2 at order-4) in the *naive* meridian `eig(t)`.
So the rank-stratified degeneration is, at this stage, **figure-eight-special in the strong sense**.

## Still open
- **The correct silver cusp meridian.** The figure-eight meridian is `µ=A⁻¹t` (a fiber-word × t); the naive
  `eig(t)` is almost certainly the wrong framing for silver. The clean relation (if any) likely needs `µ =
  (fiber word)·t` — derive the silver cusp framing, then re-test the matrix identity. (The ~26% sub-locus
  hints something real is there in the right coordinates.)
- Characterize the sub-locus (component? slice?) and extend to SL(4)/SL(5). Reuse `../B153.../sln_toolkit.py`
  patterns (general in n).

## Method notes (verify-don't-trust payoffs)
Two of my own bugs were caught by the figure-eight control before any silver conclusion: (i) the trace-map
**composition order** (contravariance — `t(σ_L)∘t(σ_R)`, not the reverse); (ii) the **`vec` convention** in
the monodromy solver (numpy `reshape` is row-major; the `kron` `vec(XYZ)=(Zᵀ⊗X)vec(Y)` identity is
column-major) — fixed by building the linear map over the `E_ij` basis. A control that must reproduce a
known answer (here B67) is the cheapest guard.

## Reproduce
```bash
python frontier/B154_silver_bundle_foundation/probe.py            # SL(2) foundation (kappa + control + t-solver)
python frontier/B154_silver_bundle_foundation/silver_construct.py # SL(n) construction + SL(3) degree=rank scan
sage   frontier/B154_silver_bundle_foundation/silver_tracemap.sage # exact fixed locus (needs Sage)
python -m pytest tests/test_b154_silver_bundle_foundation.py -q
```
