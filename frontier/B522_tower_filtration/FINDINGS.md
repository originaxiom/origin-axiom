# B522 — The tower filtration theorem (integrated from the audit's B503; SHARPER-REDUCTION)

**What this is.** The parallel closure audit's tower-prize attempt (oaudit B503_tower_timebox) on the
standing conjecture `char(ρ_n) = ∏_d char(Sym^d M)^{μ_d}` (the B122 W-identity at module level). Full proof
NOT reached; verdict **SHARPER-REDUCTION** — the sharpest reduction since B103. Integrated here under a
fresh trunk number (the audit's B503 collides with this trunk's `B503_external_contact`), with the checkable
cores **independently recomputed** (`verify_filtration.py`). Firewalled; nothing to `CLAIMS.md`; no physics.
Cross-refs the trunk's tower line: B61–B66, B89-T ([[b89t-tower-cohomology-closed]]), B117, B122, B153.

## The filtration theorem (T) — the "fifth route"
On the intrinsic cotangent space `𝔪/𝔪²` at the trivial character `x₀ ∈ X_n = Hom(F₂,SL_n)//SL_n`:
1. **Formal slice.** `Ô_{X,x₀} ≅` completion of the graded invariant ring `R = ℂ[sl_n ⊕ sl_n]^{SL_n}`
   via `(A,B)=(eᵃ,eᵇ)` (Luna slice; reductive-group invariants commute with completion; `𝔪/𝔪²` unchanged).
2. **Order is preserved.** `T_φ*: f ↦ f∘Φ`, `Φ(a,b)=(log w₁(eᵃ,eᵇ),log w₂(eᵃ,eᵇ)) = N⊗id_{sl_n} + O(deg 2)`
   by BCH, `N⊗id` invertible ⟹ `ord(f∘Φ)=ord(f)`, lowest term `f_d∘(N⊗id)`.
3. **gr = the static module.** `T_φ*` preserves the filtration `F^{≥d}`; graded pieces
   `G_{n,d} = R_d/(decomposables)_d` = degree-`d` indecomposable invariants of two traceless matrices
   (Procesi FFT), acted on by the **natural GL(2)-action of `N`**.

**Consequence — the Sym-⊗-det block FORM is FORCED for all n and all monodromies** (dependence on `N`
alone = universality is manifest), since each `G_{n,d}` is a rational GL(2)-module
`⊕_j (Sym^{d−2j}V ⊗ D^j)^{m_{d,j}}` (`D=det`). Only the static multiplicities `m^{(n)}_{d,j}` remain. This
answers B89-T's "*why* is J a Sym module" at the intrinsic level. Built from standard cited ingredients
(formal Luna slice, Procesi FFT, BCH) — the audit labels it "proved at probe-writeup strength, deliberately
NOT PROVED for the catalog"; a full formal writeup is §5-gate work. Trace-map DYNAMICS is eliminated; the
conjecture becomes **static classical invariant theory + one located splitting problem.**

## Independently recomputed here (`verify_filtration.py`)
- **Character layer closed for all n (upgrades B122(2)):** `h_a(x,y,1) = Σ_{k≤a} h_k(x,y)`, generating
  function `1/((1−z)(1−xz)(1−yz))` — **confirmed symbolically a = 0…5.** Proving the catalog for all n is
  *exactly* proving `char(ρ_n)` = the W-form.
- **The carriers reconstruct the catalog** (Sym^k V has dim k+1; D^j = det is 1-dim; V is 2-dim):
  | n | carriers (degree) | total | = |
  |---|---|---|---|
  | 2 | Sym²@2 | 3 | **n²−1 = 3** ✓ |
  | 3 | Sym²@2, Sym³@3, D²@4, D³@6 | 9 | **Lawton embdim = 9** ✓ (intrinsic = catalog × (t−det N); D³ is Lawton's t9) |
  | 4 | Sym²@2, Sym³@3, Sym⁴⊕D²@4, V⊗D²@5 | 15 | **n²−1 = 15** ✓ (canonical quotient `𝔪/𝔪²/F^{≥6}` carries exactly the catalog) |
- **First arm PROVED for all n (classical):** Chevalley `ℂ[sl_n]^{SL_n} = ℂ[tr a²,…,tr aⁿ]` ⟹ the untwisted
  `Sym^d` multiplicity in `G_n` is `[2≤d≤n]` for ALL n — the catalog's first arm, incl. its Cayley–Hamilton
  cutoff at `d=n` (degree=rank's `μ_n=1`, B117), PROVED at the intrinsic level.
- **μ_d bookkeeping** `[0≤d≤n]+[0≤d≤n−3]−[d=0]−[d=1]` — confirmed to reproduce the multiplicity structure:
  n=4 → all 1; **n=5 → μ₂ = 2 (the doubled Sym², = B62's contested `char(M²)²`)**; n=6 → μ₂ = μ₃ = 2.

## The n=5 wall, located (the sharpest statement reached)
For **n ≤ 4** the degree filtration separates carriers (deg ≤ 5) from extras (deg ≥ 6): the catalog is the
canonical quotient, no choices. From **n = 5** the second-arm carrier `Sym²⊗D²`@6 and the first extra sit in
the **same graded piece as a 2-dim isotypic multiplicity space** the filtration cannot split — exactly where
the ε-series gauge corruption lives (B104's 3 corrupted factors; B61/B62's unresolved modes). The remaining
open problem is now **static**:
> **Sharpened open problem.** Give the canonical rule selecting the carrier copy inside the multiplicity
> space of `G_{n,d}` for n ≥ 5 (equivalently: identify the banked `(n²−1)`-dim Jacobian as a canonical
> `T*`-subquotient of `𝔪/𝔪²`). Candidate rule: the opposition-involution height grading (B62/B112) as a
> second, filtration-independent grading. **No trace map, no ε-series, no Procesi σ needed.**

## Provenance / honesty
The deep step (Luna slice + Procesi FFT + BCH ⟹ `T_φ*` preserves the filtration and acts by `N` on `gr`) is
the audit's, built from standard cited theorems, at "probe-writeup strength" — **not** a catalog-grade proof;
integrated at the audit's own label **SHARPER-REDUCTION**. The checkable cores above (character layer,
carrier-dim reconstruction n≤4, first-arm Chevalley, μ_d bookkeeping incl. the n=5 doubled Sym²) are
**independently recomputed on this trunk**. Lock: `tests/test_b522.py`.
