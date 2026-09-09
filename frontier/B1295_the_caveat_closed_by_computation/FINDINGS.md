# B1295 — THE CAVEAT CLOSED BY COMPUTATION: `c₍±2,0₎ = ∓4.260982635 i`, the census counts 2, and the tower has no third arc

*MASTERPLAN v3 Phase 1 = Door D4 (`docs/MAIN_GOAL.md`). Three computations that B1294's map owed, all run on
this bench: (a) the SM seat's uncomputed coefficient; (b) the census check owed by the registry row
`T-CLOSED-CLOSING-COUNTS-TWO-OR-NOTHING`; (c) the degree-≤10 cover scan, banked as a NEGATIVE with its script.
Plus one thing found on the way and firewalled as a CONJECTURE (§4). Verification in `verification/` — six
scripts, every one prints its own `SELFTEST`/`VERDICT` line; lock `tests/test_b1295_the_caveat_closed_by_computation.py`.*

## The sentence

> **The caveat is closed by computation, not by assumption.** The harmonic generator of `H¹(m004; ℝ) = ℝ`
> has leading θ-odd cusp coefficient `c₍0,2₎ = −4.260982635(2) i` (meridian-first indexing; the SM seat's
> `c₍±2,0₎ = ∓4.260982635 i`), **not zero and not close to it**: the competing `(±2, ±1)` pair carries 7.6 % of
> its radial amplitude at the maximal cusp. So `(±2, 0)` leads, the sign partition of every embedded horotorus
> is **two annuli each**, `χ(∂⁺M) = 0`, and B1290's `net chirality = −χ(∂⁺M)` is **0 by computation** in the
> smooth frame. **The theorem's census check is paid:** 360 finite-order symmetries of the nine closings
> `Y₁…Y₉`, counted by fixed *cells* (not by Lefschetz), give **χ(Fix) = 2 for every orientation-reversing one
> and 0 for every orientation-preserving one**, and the `b₁ = 1` control fires with `{0, 4}`. **The tower has
> no third arc:** 87 covers of degree ≤ 10, 1,376 cusp-fixing (isometry, cusp) pairs, `|det(A − I)| ∈ {0, 4}`
> — including on the **16 hexagonal cusps** the tower does contain.

## 1. D4(a) — the coefficient the SM seat did not compute

**The object.** `b₁(m004) = 1`; the harmonic 1-form `ω` normalised to meridian period 1 has, on the cusp
(`z ∈ ℂ/Λ`, `Λ = ℤ + 2√−3 ℤ` in the maximal-cusp frame, height `t`, maximal cusp at `t = 1`), the expansion
`ω = dx + dψ`, `ψ = Σ_μ c_μ · t K₁(2π|μ|t) e^{2πi⟨μ,z⟩}` over the dual lattice. **Index convention here:**
mode `(m₁, m₂)`, `m₁` along the **meridian** (translation 1), `m₂` along the **longitude** (translation
`τ = 2√−3 i`); the SM seat indexes `(k along λ, l along μ)`, so **the seat's `(±2, 0)` is `(0, ±2)` here.**

**The instrument** (`harmonic_generator.py`, unchanged from the pre-registration run; `cusp_coefficient.py`):
collocation of `ψ` against the 508 group moves of Γ (Riley holonomy) — the unknowns are the `c_μ` with
`|μ| ≤ R`, the equations are the matching conditions on a random point cloud at height `Y`. Four resolutions:

| R | Y | points | equations | unknowns | rank | residual rms |
|---|---|---|---|---|---|---|
| 4 | 0.55 | 500 | 492 | 166 | 166 | 3.0e−6 |
| 5 | 0.50 | 900 | 880 | 260 | 260 | 4.8e−7 |
| 6 | 0.50 | 1400 | 1380 | 380 | 380 | 1.4e−8 |
| **10** | **0.45** | **3200** | **3150** | **1076** | **1076** | **1.6e−12** |

Full rank at every resolution (the system is determined by the moves, not fitted), residual falling
four orders per step. `c₍0,2₎` across the four: `−4.2609814 i, −4.2609826 i, −4.2609826 i, −4.2609826349 i`;
successive differences `1.1e−6, 5.6e−8, 2.2e−9`. **Result: `c₀ := c₍0,2₎ = −4.260982635 i ± 2e−9`**, real
part `< 1e−10`; the seat's **`c₍±2,0₎ = ∓4.260982635 i`**.

**The allowed subspace, derived not transcribed.** The eight cusp isometries of m004 are found numerically as
the normaliser elements fixing ∞ (`z ↦ αz + β`, `z ↦ α z̄ + β`, `α = ±1`): identity; the half-longitude
translation `r²` (`β = τ/2`); two π-rotations (`β = 0, τ/2`); two glides (`z̄ + 1/2 + τ/4`, `z̄ + 1/2 +
3τ/4`, orientation-reversing, fixed-point free on the cusp); two rotatory reflections of order 4
(`−z̄ + τ/4`, `−z̄ + 3τ/4`). The symmetry constraints `c_{g·ν} e^{2πi⟨g·ν, β⟩} = α c_ν` plus reality cut the
90 modes with `|μ| ≤ 3` to an **allowed real dimension 11**; the seat's table (orbits `(0,1),(0,3),(1,0),
(1,1)` forbidden, `(0,2),(1,2)` allowed) is reproduced entry by entry; the solved vector lies in the allowed
subspace to `< 1e−5` relative; **every forbidden orbit is below `1.5e−11`** at R = 10. Three orbits are
allowed by symmetry and nevertheless vanish — `(2,0), (1,±6), (2,±6)` at `1.6e−11, 2.1e−11, 1.5e−10` — and
§4 explains all three (they are exactly the `√−3`-divisible `ν`).

**The sign partition.** `g = ∂_t ψ` on the horotorus at `t ∈ {0.6, 0.7, 0.8, 0.9, 1, 1.25, 1.5, 2, 3}`, sign
regions labelled on a `192 × 665` grid with torus wrap-around, Euler characteristic per region by the
vertex–edge–face count on the torus: **`{g > 0}` = two components of χ 0, `{g < 0}` = two components of χ 0,
at every height** — two annuli each, exactly the seat's `(±2, 0)` picture. The zero set passes through all
eight corners (the inversions' fixed points, `|g| < 3e−14` there). The `(±2, ±1)` pair (`(1, ±2)` here) has
radial amplitude **0.0763** of the leading mode at `t = 1`: the branch `(±2,0)` vs `(±2,±1)` is decided with
a factor 13, not by a near-cancellation. **`χ(∂⁺M) = 0`; the `χ = ±4` alternative is EXCLUDED.**

*What this is and is not.* A collocation solution with a `1.6e−12` residual and `2e−9` stability across a
factor-2.5 change of cutoff is a numerical fact, not a proof; the annular topology is robust under any
perturbation far smaller than the 7.6 % margin. It says nothing new about the two named assumptions'
*physics* — it removes one of them (`c₍±2,0₎ ≠ 0`) from the assumption list and puts it in the computed list.
No identification row moves; I-26 stays UNEARNED.

## 2. D4(b) — the census check of `T-CLOSED-CLOSING-COUNTS-TWO-OR-NOTHING` (paid)

**What the registry row owed.** B1294 proved: on a closed rational-homology-sphere closing every finite-order
symmetry `g` has `χ(Fix g) = 1 − deg g ∈ {0, 2}` (Lefschetz + `H₁(N;ℚ) = H₂(N;ℚ) = 0`), and owed a *geometric*
count on Y₃/Y₉ — a check that the fixed sets, counted directly, give what the trace formula says, and that a
non-QHS control gives something else.

**The instrument** (`census_fixed_points.py`, no Regina, SnapPy used only for gluing data and cross-checks):
for `n = 1…9`, `N_n` = the n-fold cyclic cover of m004 (2n tetrahedra); all automorphisms of the lifted
canonical triangulation enumerated by propagation from the image of one tetrahedron (`|Aut| = 8n`, equal to
SnapPy's `isomorphisms_to` count for every n); for each automorphism, `χ_c(Fix)` summed over the **open cells
mapped to themselves** by the induced corner-permutation type (tetrahedron: identity −1, transposition +1,
double transposition −1, 3-cycle −1, 4-cycle +1; face: identity +1, transposition −1, 3-cycle +1; edge: kept
−1, reversed +1), orientation `ε` from the permutation parity, the sign `a` of the action on `H₁(N_n; ℚ) = ℚ`
from the dual spine (exact, sympy), and the closed count `χ(Fix Y_n) = χ_c(Fix N_n) + χ(Fix C)` with the core
circle `C` of the filling solid torus contributing 2 iff the symmetry reverses it. **Internal consistency**,
per automorphism, all 368: `χ_c(Fix N_n) + χ(Fix ∂N_n) = Hopf trace on the dual spine = 1 − a`. SnapPy
cross-checks: every cusp matrix diagonal (the slope is kept); the multiset `(det A, A₁₁)` equals my `(ε, a)`.

| closing | tets | \|Aut\| | H₁(Y_n) | orientation-reversing: χ(Fix) | preserving: χ(Fix) |
|---|---|---|---|---|---|
| Y₁ (= S³) | 2 | 8 | 0 | **2** (×4) | 0 (×4) |
| Y₂ | 4 | 16 | ℤ/5 | **2** (×8) | 0 (×8) |
| Y₃ | 6 | 24 | (ℤ/4)² | **2** (×12) | 0 (×12) |
| Y₄ | 8 | 32 | ℤ/3 ⊕ ℤ/15 | **2** (×16) | 0 (×16) |
| Y₅ | 10 | 40 | (ℤ/11)² | **2** (×20) | 0 (×20) |
| Y₆ | 12 | 48 | ℤ/8 ⊕ ℤ/40 | **2** (×24) | 0 (×24) |
| Y₇ | 14 | 56 | (ℤ/29)² | **2** (×28) | 0 (×28) |
| Y₈ | 16 | 64 | ℤ/21 ⊕ ℤ/105 | **2** (×32) | 0 (×32) |
| Y₉ | 18 | 72 | (ℤ/76)² | **2** (×36) | 0 (×36) |
| **control Y₀** (longitude filling, `b₁ = 1`) | 2 | 8 | ℤ | **{0, 4}** — never 2 | 0 |

**Zero odd counts; zero counts other than 2 on the orientation-reversing side; the control fires** (its
orientation-reversing values are `2 − 2a`, the `b₁ = 1` Lefschetz value, `a = ±1` odd). The `H₁` column
matches B1294's Smith-normal-form computation independently (`(ℤ/4)²`, `ℤ/8 ⊕ ℤ/40`, `(ℤ/76)²`). The
hypothesis in force is *finite order + QHS*, which is why the non-hyperbolic `Y₁, Y₂, Y₃` belong in the
table as much as the hyperbolic `Y₄…Y₉`.

**The five kinds on m004 itself** (n = 1), matching B1294's table cell by cell but now by *cells*: the two
glides fix **no cell** of the ideal triangulation (fixed-point free in M; their 2 is the two points on the
knot); the two order-4 rotatory reflections fix **exactly the two tetrahedron centres** (χ_c = 2) and nothing
on the knot; the two π-rotations fix one whole edge plus two face-rays through a reversed edge's midpoint
(χ_c = −2, the two open arcs cusp-to-cusp, closing to a circle through the knot in S³); `r²` fixes a closed
geodesic through both tetrahedra (χ_c = 0); the identity (χ_c(M) = 0).

*Instrument finding, recorded because a reader will hit it:* SnapPy's peripheral basis on the cyclic covers is
**not uniformly `(μ̃, λ̃)`** — the meridian lift is basis curve `(1, 0)` for `n ≤ 3` and `(0, 1)` for `n ≥ 4`
(the flip is where the lifted meridian, length n, overtakes the longitude, `2√3 ≈ 3.46`). The script picks
`μ̃` as the basis slope whose filling kills `b₁` (exactly one does, asserted), which is legitimate because
every cusp matrix is diagonal; the counts are basis-independent.

## 3. D4(c) — the tower has no third arc (NEGATIVE, banked with the script)

**The claim killed.** That three arc endpoints — an odd isolated fixed-point count, i.e. a cusp rotation of
order 3 or 6 (`|det(A − I)| = 3` or `1`), or order 4 (`= 2`) — might be available on a cusp of a *finite cover
of m004*, inside the object's own tower, where B1291's one-cusp parity no longer binds.

**The computation** (`cover_scan.py`): every cover of m004 of degree 2…10 (all conjugacy classes of subgroups;
**87 covers**, 64 multi-cusped, cusp counts `1:23, 2:27, 3:27, 4:7, 5:3`, **201 cusps**); every isometry
(**968**, both orientations); every cusp it fixes (**1,376** pairs); `|det(A − I)|` of the peripheral matrix.
**Values: `0` (882 times: 380 orientation-reversing, 502 preserving) and `4` (494 times, all
orientation-preserving π-rotations). Never 1, 2 or 3. No canonization failures.**

**The sharpening.** SL₂(ℤ)-reduced cusp shapes over the 201 cusps: 122 rectangular/rhombic, 63 generic,
**16 hexagonal** (all in 14 covers of degree 10, isometry groups of order 4–32) — so the tower *does* contain
cusps whose Euclidean geometry admits ℤ/6, and **no isometry of any of those covers rotates them**: the
negative is about the covers' symmetry groups, not (as on m004 itself, B1291/B1292) about the cusp shape.
No square cusps at all through degree 10.

**Hatch:** degree > 10; or a cover whose isometry group is enlarged (a hexagonal cusp is necessary, not
sufficient — the 14 witnesses show the gap). Both are computations, not conjectures.

## 4. Found on the way, FIREWALLED — the divisor law (CONJECTURE, pre-registered, 88/88)

*Firewall: this section makes no physics claim. It is a statement about the Fourier coefficients of one
harmonic form on one manifold, found numerically, tested out of sample, unproved.*

Write the mode as `ν = a + b√−3 ∈ ℤ[√−3]`, `a = m₂/2`, `b = −m₁` (odd `m₂` is symmetry-forbidden); call `ν`
**even** iff `a + b` is even (`ν ∈ 2ℤ[ω]`, `2` being prime in ℤ[ω]). Over ordered factorisations `ν = d·e`
in ℤ[√−3] (up to common sign):

> `c(ν) = c₀ · S(ν)`, `S(ν) = (1/|ν|) Σ_{d e = ν} w(d, e)`, with `w = Re(d ē)` if d, e both odd;
> `+Im(d ē)/√3` if d odd, e even; `−Im(d ē)/√3` if d even, e odd; `0` if both even.

**Zero fitted parameters** (`c₀ = c(1)`). Values: `S(√−3·x) = 0`, `S(2ᵏ) = 0`, `S(3) = S(9) = 1`, `S(5) = 2`,
`S(7) = 16/7`, `S(1 + √−3) = −1`. **Test protocol** (`law_outofsample.py`, pre-registered before the R = 10
solve): the law was found on modes with `N(ν) ≤ 108`; the prediction for the **88 modes with
`108 < N(ν) ≤ 200`** was written down, the R = 10 solve run, tolerance fixed at `5e−3` from the in-sample
error `5.5e−7` — **PASS 88/88, worst deviation `3.4e−4`** (in the outermost band `|μ| ≈ 8` of a cutoff-10
solve; modes at `|μ| ≤ 6` agree to `5.5e−7` — truncation, not the law). In `cusp_coefficient.py` §5 the law is
re-checked on all **184** solved even modes with `N(ν) ≤ 200`: **0 failures, all 68 predicted exact zeros
vanish** — which is what explains the three allowed-but-vanishing orbits of §1.

**Why the shape is the expected one, and why it is still only a conjecture.** `b₁(m004) = 1 = #cusps`, so
`H¹` is entirely Eisenstein: the harmonic generator *is* an Eisenstein series of the index-12 subgroup
`Γ ⊂ PSL₂(ℤ[ω])` at its harmonic point, and Eisenstein Fourier coefficients are divisor sums. The specific
parity twist (the character of `ℤ[ω]/2 ≅ 𝔽₄` entering through the glides `c(−ν̄) = (−1)^{a+b} c(ν)`) is what
the object contributes. Proving it means writing that Eisenstein series down — registered as **L200**.
**`c₀` closed form: OPEN** — a bounded linear PSLQ (`|c₀|` or `|c₀|·k` against 1 and ≤ 2 of `π, √3, π²,
log 2, log 3, L(2,χ₋₃), ζ_K(2), G, ζ(3), vol(m004)`, coefficients ≤ 12, tol 1e−9) finds **nothing**; the
fractional-power search that "finds" 62 forms at 10 digits was run once, recognised as numerology, and
removed. Bonus observations get *recorded*, not chased (MASTERPLAN v3 §6).

## 5. What moves on the map

- **MAIN_GOAL JOIN 1, item 4:** the caveat clause "*c₍±2,0₎ is not computed*" is replaced by the computed value.
  The **two named assumptions become one** — θ-equivariance of the vacuum (fc's) is the only assumption left
  under B1294's map; **Door D1 = B1296** is next, exactly as sequenced.
- **THEOREM_REGISTRY:** the row `T-CLOSED-CLOSING-COUNTS-TWO-OR-NOTHING` has its census check **PAID** here
  (360 symmetries, 9 closings, control fires); no new law.
- **Kill graph:** one record (the cover scan), with the hexagonal-cusp sharpening as its hatch.
- **OPEN_LEADS:** L200 (prove the divisor law as an Eisenstein expansion; identify `c₀`).
- **Not claimed:** nothing about generation counts; no identification; the smooth-frame `χ(∂⁺M) = 0` is a
  *computed zero*, i.e. the smooth frame gives no chirality — that was the expected outcome of D4 and it is
  now a result, not a reading.

## Verification

`verification/` — run from that directory; each prints its verdict on the last line:

| script | what | runtime | verdict line |
|---|---|---|---|
| `harmonic_generator.py` | the cusp lattice, the 508 moves, the collocation solver (`solve`) | library | — |
| `cusp_coefficient.py` | §1 four-resolution solve → `c₀`; §2 the eight cusp isometries; §3 the derived allowed subspace; §4 the sign partition; §5 the divisor law + bounded PSLQ | ~55 s | `SELFTEST: PASS` (23/23) |
| `divisor_law.py` | `S(ν)`; CLI `divisor_law.py <json> <key> <nmax> <tol>` | s | table |
| `law_outofsample.py` | the pre-registered out-of-sample test (its own R = 10 solve) | ~30 s | `PRE-REGISTERED OUT-OF-SAMPLE TEST: PASS` |
| `census_fixed_points.py [--nmax N]` | D4(b); `--nmax 3` in 3 s, the banked run is `--nmax 9` (~100 s) | 102 s | `SELFTEST: PASS (71/71)` |
| `cover_scan.py` | D4(c) | ~1 s | `VERDICT: NEGATIVE` |

Every script is deterministic (seeded point clouds): a rerun reproduces `c₀` to the last printed digit. Outputs shipped: `cusp_coefficient.json/.out`, `law_outofsample.json/.out`, `census_fixed_points.json/.out`,
`cover_scan.json/.out`, `harmonic_generator.json`. Environment: snappy 3.3.2, scipy 1.16.3, numpy 2.4.0,
sympy, mpmath 1.3.0 (the canonical pyenv, no Sage, no Regina).
