# B503 — the tower time-box (Closure Campaign Phase 4): **SHARPER-REDUCTION**

**Pre-registered** (`docs/CLOSURE_CAMPAIGN_2026-07.md`, Phase 4; enum PROVED · SHARPER-REDUCTION ·
UNCHANGED; HARD box = one session — respected, stopped clean). One serious attempt at the standing
prize `char(ρ_n) = ∏_d char(Sym^d M)^{μ_d}` (= the B122 W-identity at module level). **Full proof
NOT reached; verdict SHARPER-REDUCTION** — the sharpest since B103: the trace-map **dynamics is
eliminated** from the conjecture, which becomes **static classical invariant theory** plus one
precisely located splitting problem. Script `probe.py` (exit 0, budget logged: 14.7 s of the box);
test `tests/test_b503_tower_timebox.py` (10 passed, ~16 s). **Nothing to `CLAIMS.md`**; no physics;
P1–P16 untouched; the three foreclosed shortcuts (B84 pinv, B85 Λ²V, B89-T cohomological) were
**not retried** — this route works on the trace-coordinate cotangent, the object B89-T itself
identified as the tower-carrier.

## The filtration theorem (T) — the new reduction (the "fifth route")

Let `X_n = Hom(F₂,SL_n(ℂ))//SL_n`, `x₀` the trivial character, `T_φ` the trace map of
`φ ∈ Aut(F₂)` with abelianization `N ∈ GL(2,ℤ)`; `T_φ` fixes `x₀`. On the **intrinsic** cotangent
space `𝔪/𝔪²` at `x₀`:

1. **(formal slice)** `Ô_{X,x₀} ≅` the completion of the *graded* invariant ring
   `R = ℂ[sl_n ⊕ sl_n]^{SL_n}` via `(A,B) = (eᵃ, eᵇ)` (equivariant formal exp; invariants of a
   reductive group commute with completion; completing does not change `𝔪/𝔪²`).
2. **(order is preserved)** `T_φ*` acts by `f ↦ f∘Φ`, `Φ(a,b) = (log w₁(eᵃ,eᵇ), log w₂(eᵃ,eᵇ))`;
   by BCH, `Φ = N⊗id_{sl_n} + O(deg 2)` with `N⊗id` invertible, so `ord(f∘Φ) = ord(f)` and the
   lowest term of `f∘Φ` is `f_d∘(N⊗id)`.
3. **(gr = the static module)** hence `T_φ*` preserves the decreasing filtration
   `F^{≥d} = ({ord ≥ d} + 𝔪²)/𝔪²`, whose graded pieces are `G_{n,d} := R_d/(decomposables)_d` — the
   degree-`d` **indecomposable invariants of two traceless matrices** (Procesi FFT: spanned by
   trace words) — and it acts on `gr_d` by the **natural GL(2)-action of `N`**.

**Consequence:** `char(T_φ* | 𝔪/𝔪²) = ∏_d char(N | G_{n,d})`, and since each `G_{n,d}` is a rational
GL(2)-module `⊕_j (Sym^{d−2j}V ⊗ D^j)^{m_{d,j}}` (`D = det`):

> **the Sym-⊗-det-block FORM of the tower is FORCED, for all n and all monodromies** (universality
> — dependence on `N` alone — is manifest); **only the static multiplicities `m^{(n)}_{d,j}`
> remain.** This answers B89-T's "*why* is `J` a Sym module" at the intrinsic level, and it is
> form-not-values in the program's own sense.

Label: **proved** at probe-writeup strength (standard cited ingredients: formal Luna slice, Procesi
FFT, BCH; the `N`-vs-`N⁻¹` convention pinned empirically against the banked B103 objects); a full
formal writeup is §5-gate work, and the verdict here is deliberately *not* PROVED for the catalog.

## What the static module gives (computed, exact ranks, two independent seeds)

| n | `G_{n,d}` (degrees) | consequence |
|---|---|---|
| 2 | `Sym²`@2 — nothing else | intrinsic **= catalog**: the n=2 tower **re-derived**, verified symbolically on words, **both det signs** |
| 3 | `Sym²`@2, `Sym³`@3, `D²`@4, `D³`@6 (total 9 = **Lawton embdim**) | intrinsic = **catalog × (t − det N)**; **Lawton's t9 IS the D³ generator**; quotient by `F^{≥6}` re-derives the n=3 tower (verified symbolic-in-m on the banked exact `J(m)` + det=+1 foreign control) |
| 4 | carriers `Sym²`@2, `Sym³`@3, `Sym⁴⊕D²`@4, `V⊗D²`@5 (**dim 15 = n²−1, exactly the catalog**); extras start at 6: `Sym²D²⊕D³`@6, `VD³`@7 | the canonical `T*`-stable quotient `𝔪/𝔪²/F^{≥6}` **carries exactly the n=4 catalog** (identity verified symbolically, both det signs; spot-checked against B80's proved `J(m)`) |
| 5 | all **24 catalog carriers present** at degrees 2..6 — including the **contested doubled Sym² (B62's `char(M²)²`)**: it is `Sym²⊗D²`@6 with **multiplicity 2** (certified) | `G_{5,6} = (Sym²D²)² ⊕ D³`: the doubled-Sym² **carrier collides with the first extra in one graded piece**; catalog₅ **divides** the intrinsic char (symbolic, both det signs) |
| 6 | first arm `Sym²..Sym⁶` exactly (**Cayley–Hamilton cutoff at d=n**); doubled `Sym²`@6 and doubled `Sym³`@7 present (each mult 2 = carrier+extra) | the collision pattern persists and grows with n |

Labels, honest: existence/lower bounds (e.g. the doubled Sym² at n=5) are **exact certificates** —
`dim Indec ≥ rank(E_all) − rank(E_dec)` for exact integer evaluation ranks, unconditionally.
Equalities ("nothing else at this weight") are exact ranks with 2× oversampling, stable across two
independent seeds: **probability-1 grade**, and *pinned* at n≤3 by the classical presentations
(free ring at n=2; Lawton's 9 at n=3). The single-letter weight line is **classical** (Chevalley:
`ℂ[sl_n]^{SL_n} = ℂ[tr a²,…,tr aⁿ]`), so: **the untwisted-Sym^d multiplicity in `G_n` is
`[2≤d≤n]` for ALL n — the catalog's first arm, including its Cayley–Hamilton cutoff at `d=n`
(degree=rank's `μ_n=1`, B117), is PROVED at the intrinsic level.** (The task's suggested
"CH structure of the trace-ring generators" is realized exactly here.)

## The character layer, closed for all n (upgrades B122 (2))

`h_a(x,y,1) = Σ_{k≤a} h_k(x,y)` (generating function `1/((1−z)(1−xz)(1−yz))` — one line), plus the
multiplicity bookkeeping `[0≤d≤n]+[0≤d≤n−3]−[d=0]−[d=1] = μ_d`, makes the **W-form ≡ two-sequence
catalog an identity for ALL n** (B122 had verified it to n=8). Elementary, but it closes that gap:
proving the catalog for all n **is exactly** proving `char(ρ_n)` = the W-form.

## The n=5 wall, located (the sharpest statement reached)

For **n ≤ 4** the degree filtration **separates carriers from extras** (carriers ≤ 5, extras ≥ 6):
the catalog is the canonical quotient — no choices. From **n = 5** the second-arm carrier
`Sym²⊗D²`@6 and the first extra sit in the **same graded piece as a 2-dim isotypic multiplicity
space**, which the filtration *cannot* split — exactly where the eps-series gauge corruption lives
(B104's 3 corrupted factors; B61/B62's unresolved modes; B105-V91's "the contested piece is only
B62's `char(M²)²`"). The remaining open problem, now static:

> **Sharpened open problem.** Give the canonical rule that selects the carrier copy inside the
> multiplicity space of `G_{n,d}` for n ≥ 5 (equivalently: identify the banked `(n²−1)`-dim
> Jacobian as a canonical `T*`-subquotient of `𝔪/𝔪²`). Candidate source for the rule: the
> opposition-involution height grading (B62/B112, the V91-sharpened target) as a second,
> filtration-independent grading on `G_{n,d}`. No trace map, no eps-series, no Procesi σ needed.

Residual observation (hint-grade, not ledgered — scope of this probe is B503-only): the extras
computed so far look like a `D³`-twisted third arm (`D³`@6, `VD³`@7 at n=4), suggesting `G_n` is a
stack of det-twisted arms of which the catalog keeps exactly two; if that closed form holds, the
splitting rule may fall out of it.

## Why the full proof stalls (one honest paragraph)

Three lines were attempted inside the box. (i) The character-level CH route: closes the *first arm*
for all n (above) but says nothing about the D²-twisted second arm's multiplicities — the weight
(d,0) line is blind to twists. (ii) The equivariant filtration: proves the FORM for all n and
reduces everything to `m^{(n)}_{d,j}`, but those multiplicities are exactly the hard part of the
classical two-matrix invariant theory (fully known only for small n), and no closed form for the
second arm was proved here — only computed n ≤ 6. (iii) The subquotient identification: canonical
for n ≤ 4, obstructed at n ≥ 5 by the multiplicity-space collision — the same 3-dim sector that
killed every dynamical route, now visible as a *static* degeneracy, which is why it is banked as a
reduction and not a proof.

**Ledger:** this probe only (no CLAIMS row, no promotions; PROMOTION-CANDIDATE not applicable —
verdict is not PROVED). **Reuses:** `B103.two_sequence_mult`, `B103.lawton_jacobian`,
`B103._Jm_n3_exact`, `B103._Jm_n4_exact` (B80's proved SL(4) Jacobian). **Anchors:** B89-T (the
module-iso (M) + the trace-coordinate carrier), B103/B104 (ρ_n, the walls), B105-V91 (the three
n=5 obstacles; the contested piece), B62/B112 (the θ-split, the candidate splitting rule), B117
(two-sequence), B121/B122 (the W-form).

```bash
.venv/bin/python frontier/B503_tower_timebox/probe.py
.venv/bin/python -m pytest tests/test_b503_tower_timebox.py -q
```
