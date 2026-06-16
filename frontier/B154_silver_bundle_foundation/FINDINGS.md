# B154 — the silver bundle (m=2, R²L²): foundation for the degeneration-generality question

**Date:** 2026-06-15 (updated 2026-06-16). **Status:** degree=rank GENERALIZES to the metallic family with
the derived meridian `µ=A⁻ᵐt`, and the exponent is **order-based, not rank-based** (`k=4−m(o−3)` fit;
"degree=rank" is a principal-spectrum coincidence). Matrix identity on a sub-locus; sub-locus
characterization + closed-form derivation OPEN. Standalone low-dim topology / character varieties; no
physics, no Origin-core claim; P1–P16 untouched; nothing to `CLAIMS.md`. Probes: `probe.py`,
`silver_construct.py`, `silver_degree_rank.py`, `silver_exp3.py`, `fig_exponent.py`; exact derivation:
`silver_tracemap.sage`. Ledger: V146.

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

### The metallic cusp meridian (DERIVED — the key) `µ = A⁻ᵐt`
The monodromy preserves the fiber boundary only **up to conjugacy**: `φ([A,B]) = Aᵐ[A,B]A⁻ᵐ`, an **exact
free-group identity** (m=1 figure-eight, m=2 silver; verified by word reduction `φ_silver([A,B]) =
AAABA⁻¹B⁻¹A⁻¹A⁻¹ = A²[A,B]A⁻²`, and well-conditioned matrices). Hence **`µ = A⁻ᵐt` commutes with `[A,B]`**
— it is the cusp meridian (the figure-eight's `A⁻¹t` is the `m=1` case). Confirmed on silver bundle reps:
`‖[µ,[A,B]]‖ ~ 1e-11`, `µ=A⁻²t`. (My first SL(3) scan used the *naive* `eig(t)` — the wrong framing — and
the matrix identity failed 0/38; that was a wrong-meridian artifact, now corrected.)

### Silver degree=rank DOES hold (matrix identity, with `µ=A⁻²t`) — on a sub-locus
With the correct meridian, the **matrix identity `[A,B] = ± µᵏ` holds** (det t = 1, so det µ = 1 = det[A,B]):
- `{1,ω,ω²}` (order 3) at SL(3): **`[A,B] = +µ⁴`** on 14/55 irreducible reps (err 1e-12, cond ~7).
- `{1,i,−i}` (order 4) at SL(3): **`[A,B] = +µ²`** on 6/37 (err 1e-12, cond ~15).
- `{1,1,ω,ω²}` at SL(4): **`[A,B] = −µ⁴`** (1 rep, cond ~1e3 — preliminary; random Newton barely reaches
  SL(4) silver). The sign/exponent match the figure-eight SL(4) result (`−µ⁴`), with `µ=A⁻²t` here.

**Conclusion (verified, CORRECTING the first cut):** degree=rank is **NOT figure-eight-special** — it
**generalizes to the metallic family** with the meridian `µ = A⁻ᵐt`. For silver it is a **matrix identity on
a SUB-LOCUS** (~25% of the irreducible reps at a finite-order spectrum), i.e. a *slice* phenomenon — vs the
figure-eight, where it held on the entire spectrum-locus (B149). So the rank-stratified picture extends, but
the "component vs slice" balance shifts toward slice for `m=2`.

### The exponent is ORDER-based, not rank-based — "degree=rank" is a principal-spectrum coincidence
The exponent `k` in `[A,B]=±µᵏ` is determined by the **order `o` of the boundary spectrum**, NOT by the rank
`n`. **Decisive test** (off-principal spectra, where `o` is *not* linked to `n`): the figure-eight
`{1,ω,ω²}` (o=3) gives `k=4` at **both** n=3 and n=4 — not `k=n`. So the celebrated `L=(−1)^{n-1}Mⁿ`
("degree=rank", `k=n`) is a **coincidence of the principal spectra**, whose order is tied to the rank by
B95 (`n=3↔o4, n=4↔o3, …`); the underlying invariant is the order.

Verified data `(m, o) → k` (the sign is forced by parity, `+` for n odd):

| | o=3 ({1,ω,ω²}-type) | o=4 ({1,i,−i}-type) |
|---|---|---|
| **figure-eight m=1** | k=4 (n=3 and n=4) | k=3 (n=3) |
| **silver m=2** | k=4 (n=3 and n=4) | k=2 (n=3) |

**Geometric meaning of k (eigenvalue probe, `eig_structure.py`):** `[A,B]=±µᵏ` is **not a point relation — it is
an A-polynomial component of slope `k`**. On the sub-locus the meridian eigenvalues `M=eig(µ)` are *generic*
(`|M|≠1`) yet `L=Mᵏ` holds along the whole curve (err 1e-11…1e-15); the special points where `M` is a root
of unity (e.g. the figure-eight principal `{1,i,−i}`: `M` of orders 3,2,6) are the genuine finite-order
**Dehn fillings** sitting on that component. So `k` is the **A-polynomial slope** — and it is order-determined.

A clean closed form fits every point: **`k = 4 − m(o−3)`** (m = metallic index, o = boundary-spectrum order).
[Honest tier: the *order-not-rank* conclusion is solid — the off-principal `k=4` at two ranks is decisive;
the closed form `k=4−m(o−3)` is an **empirical fit on o∈{3,4}, m∈{1,2}** (the constants 4,3 are not yet
derived), and the o=4 cases at SL(4) eluded random Newton (need a structured construction). Reproducers:
`silver_exp3.py`, `fig_exponent.py` in `audit/lab/`.]

**Data completeness note.** The closed form is tested on every *accessible* point: o=3 at n=3,4 (both m) and
o=4 at n=3 (both m). The o=4 spectra appear to admit irreducible reps **only at SL(3)** — `{1,1,i,−i}`@SL(4)
yields no irreducible reps even with the fast analytic solver (the figure-eight `{1,1,ω,ω²}`@SL(4) control
is found fine), for both figure-eight and silver. So the o=4/SL(4) data point does not exist to test, and
`k=4−m(o−3)` holds on all six accessible (m,o,n) points. (`fig_sl4_o4.py`.)

### Toward deriving `k` (attempt 2026-06-16: framework + honest reduction — NOT a derivation)
`k` is the exponent of the degree=rank A-polynomial component `[A,B]=±µᵏ` (verified as a **matrix identity**,
`µ=A⁻ᵐt`). Structural origin of the m-dependence: the monodromy conjugates the longitude by `Aᵐ`
(`φ_m([A,B])=Aᵐ[A,B]A⁻ᵐ`), forcing `µ=A⁻ᵐt`. For a *specific* spectrum the identity is derivable
algebraically from `A^o=I` + the bundle relations — the route **B89** used to prove `[A,B]=−µ⁴` from `A³=I`
at SL(4) (computer-assisted over `ℤ[m]`); the silver analogue is the same computation with the eliminated
`F1/F2` (harder, `B` not explicit). A **full first-principles derivation of the closed form `k=4−m(o−3)` is
OPEN** — it reduces to the exponent/slope of the *metallic* A-polynomial component at SL(n) for boundary
order o, i.e. the metallic generalization of the whole B67/B71/B89 A-polynomial program (a multi-stage
effort, not a quick result). Constraints a derivation must reproduce: sign forced by parity (`+` for n odd);
**order-determined, not rank**; `o=3 ⇒ k=4` independent of m (a fixed point of the m-dependence).
*(Methodology note: a naive log-log "slope" fit fails on complex-log branch cuts — `log(Mᵏ)≠k·log M` mod
2πi; the matrix identity `[A,B]=±µᵏ`, not a log-fit, is the correct statement.)*

## Still open
- **Derive `k=4−m(o−3)`** (the deep prize) — via the per-spectrum B89-style algebra (`A^o=I` + bundle
  relations) or the metallic A-polynomial; test o≥5 and higher m (bronze m=3) — needs a structured
  construction and admissible higher-order spectra.
- **Characterize the sub-locus** (slice vs component) and the **silver principal spectrum** (the B95-analogue).
  Reuse `../B153.../sln_toolkit.py` patterns (general in n).

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
