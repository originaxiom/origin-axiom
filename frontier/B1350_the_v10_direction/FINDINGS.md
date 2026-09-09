# B1350 — THE V₁₀ DIRECTION: the one deformation of the cusped object's E₆ holonomy that B1280's pairing law does not cover — the V₁₀ inside the 42 at the subregular point (θ = −1, ι* = +1; L207, main's L204) — carries genuine, non-self-dual E₆ representations along every direction of its class space, and N(27) = 0 on all of them: h¹(27) = h¹(27̄) = 0, no cusp-fixed vector, the window of B1268's bound closed. The θ-odd frame is closed on every sl₂ germ of the object.

**Date:** 2026-09-08 · **Seat:** cc (the SM-derivation branch) · **Status:** PROVED (stages 0–3 and 5 exact over ℚ(ω) / modulo two primes; stage 4 at 600 bits with the cohomology re-read at 2000 bits, 200-digit ranks, every zero forty orders below every non-zero; the Newton stall of the first run diagnosed and removed) · **Price: unchanged** · **Numbering:** B1350, the first of the range this branch now numbers from (the collision note in `docs/SM_SEAT_ALIAS_TABLE.md`).

## Why this arc — the last unpaired direction

B1280 proved that the inversion of m004 acts on the six deformation classes of the E₆ holonomy at the geometric
(principal) point by θ's signs, so every flat-sector deformation there is symmetry-paired and N(27) ≡ 0 on the germ.
Its mod-4 criterion then found that at the other even sl₂ point, the subregular E₆(a₁) — e₆ = V₂⊕V₄⊕V₆⊕V₈⊕V₁₀⊕V₁₀⊕V₁₄⊕V₁₆,
27 = 13 ⊕ 9 ⊕ 5, the outer involution fixing sp(8) = V₂⊕V₆⊕V₁₀⊕V₁₄ and negating the 42 = V₄⊕V₈⊕V₁₀⊕V₁₆ — seven of the
eight tangent directions agree and exactly one does not: **the V₁₀ of the 42**, where θ = −1 but the inversion acts by
(−1)^{10/2+1} = +1. Main's B1299 verified the hole exactly and priced the computation at about a day with a prior of 15 %
for a non-zero net count. This arc does it with B1268's machinery: exact cocycles, Newton to genuine E₆ representations
at 400 bits, twisted cohomology of the 27 and the 27̄ at 60 digits, and B1268's bound −h⁰(∂M; V) ≤ N ≤ h⁰(∂M; V*), which
says a non-zero N needs a cusp-fixed vector at the deformed point.

## 1. The point ((0), (1), exact)

The subregular triple (weighted Dynkin (2,2,2,0,2,2); B1267's instrument) grades e₆ so that the kernel of ad e on each
weight space gives the block multiplicities {2: 1, 4: 1, 6: 1, 8: 1, 10: **2**, 12: 0, 14: 1, 16: 1} — the two V₁₀'s.
ρ₀ = (exp e, exp u f) on the 27 (u the Riley root) is an exact representation of π₁(m004) over ℚ(ω) with

| | h⁰(M) | h¹(M) | h⁰(∂M) | h¹(∂M) | rank(res) | N |
|---|---|---|---|---|---|---|
| 27 at ρ₀ | 0 | 3 | 3 | 6 | 3 | 0 |
| 27̄ at ρ₀ | 0 | 3 | 3 | 6 | 3 | 0 |

(the 3 = one class per block of 27 = V₁₂ ⊕ V₈ ⊕ V₄, exact and at 60 digits alike).

## 2. The two V₁₀ classes and the cusp ((2), exact over ℚ(ω))

For each V₁₀ block (basis ad(f)^k hv, k = 0 … 10) the Fox complex of the block representation gives dim Z¹ = 12,
dim B¹ = 11, **h¹ = 1**: one class per block, two in the isotype. Their restriction to the cusp torus ⟨μ, λ⟩:
**neither class alone is cusp-trivial**, and on the two-dimensional class space the restriction map to H¹(∂M; e₆) has rank
**2** — there is no cusp-trivial combination: every deformation in the V₁₀ isotype moves the cusp holonomy, so by B1268's bound a non-zero N at the deformed point needs the cusp holonomy to keep a fixed vector, which is what stage 4 measures (h⁰(∂M) at ε ≠ 0).

## 3. First-order trace-flatness ((3))

The first-order self-duality defect d/dε [tr ρ_ε(w) − tr ρ_ε(w⁻¹)] along either class vanishes identically on six test
words (to 10⁻¹⁵⁷ in ball arithmetic): both V₁₀ classes are **trace-flat at first order**, so the θ-parity of the class
space cannot be read from first-order character variations (the same was true, implicitly, of B1268's V₈ direction, which
broke self-duality only at finite ε). The parity is read from the finite deformations of §4.

## 4. The deformations ((4) Newton at 600 bits; (5) the exact obstruction calculus modulo two primes)

**(a) The Newton search stalls.** From the first-order point exp(0.02·Y/|Y|)ρ₀ along either V₁₀ class (start residual
1.2·10⁻⁴), B1268's Gauss–Newton (damping 10⁻²⁴·max G_ii, 40 iterations) falls to |res| ≈ 4·10⁻¹³ in seven iterations and
then crawls — 3.98·10⁻¹³ → 3.44·10⁻¹³ over the next fifteen (record `v10_direction_run_stall.txt`; the same with
`verbose=False` in `v10_direction_run_A_stalled.txt`, whose "N = 0" lines are printed at a non-representation — relator
residual 3·10⁻¹³, cusp commutator [μ, λ] ≈ 77 — and mean nothing). B1268's V₈ search converged linearly to 10⁻⁶³ under the
same code. A stall of this shape is either a geometric obstruction (no representation near the first-order point) or a
numerical one (the directions that must be corrected are damped away). Stage (5) decides which, exactly.

**(b) No obstruction at second order — exactly.** `obstruction.py` (record `obstruction_run.txt`): for each of the eight
sl₂-blocks one exact non-coboundary cocycle (ℚ(ω)); the linearised relator map d¹: e₆ ⊕ e₆ → e₆ has rank **70** modulo both
primes (= 156 − dim Z¹ = 156 − 86 with h¹(M; e₆) = 8, so the rank is exact and dim H²(M; e₆) = 8); the second-order term
Q(Y) of ρ_ε(REL) lies in im d¹ for **every one of the eight block classes**, the two V₁₀'s included; on the V₁₀ plane the
quadratic map c ↦ [Q(c₁Y₁ + c₂Y₂)] ∈ H² **vanishes identically** (its three coefficient classes are all zero in H²); over the
whole eight-dimensional H¹ the 36 coefficient classes of Q span a 3-dimensional subspace of H², and the mixed terms with a V₁₀
factor are non-zero exactly for V₄, V₆, V₁₄, V₁₆ and zero for V₂, V₈ and the other V₁₀. Both primes agree on every rank.

**(c) Formally integrable through order six.** `obstruction_higher.py` (record `obstruction_higher_run.txt`) continues
ρ_ε(g) = exp(εY_g + ε²W_g + ε³V_g + …)ρ₀(g) order by order, solving d¹(X_k) = −R_k modulo the cocycle freedom at order
k − 1: **V₁₀, V₁₀#2, V₁₀ + V₁₀#2 and V₁₀ − V₁₀#2 are all integrable through order 6** (exact: a formal solution is
exhibited modulo two primes), each needing the cocycle freedom from order 3 on — the higher Taylor coefficients of the
curve have components along the other classes. The method is one-sided (its "stop" is not a proof of obstruction: the V₈
control stops at order 5 under the greedy continuation although B1268 integrated V₈ to a genuine representation), so the
positive verdicts are what it establishes. **The stall of (a) is therefore numerical**: the Newton correction has to move
along directions whose singular values at the first-order point are of order ε and are suppressed by the damping.

**(d) The Newton search converges once the damping is lifted.** Three probes on class 1 (`probe_*.txt`): with the damping
at 10⁻⁵⁰ and the step 0.02 the residual goes 1.2·10⁻⁴ → 3.6·10⁻¹³ → 9.3·10⁻¹⁸ → 3.0·10⁻³² → 4.7·10⁻⁴⁵ → 1.1·10⁻⁵² → **6.0·10⁻⁶⁸**
(quadratic from the second step: the stall was the damping and nothing else); with the step raised to 0.2 at the old damping it
crawls (2.4·10⁻⁹ → 6.4·10⁻¹¹ over three iterations); with both changed it does not move. Damping 10⁻⁵⁰ is now the default.

**(e) The genuine representations along the V₁₀ directions, and N(27) there — read at 2000 bits.** B1268's report decides
ranks at 60 digits with a relative threshold 10⁻³⁰; at the deformed points its pivots straddle the threshold (d¹: 5.6·10⁻²⁹
accepted against 1.3·10⁻³³ rejected; Z¹(T²): 1.5·10⁻³⁰ against 1.7·10⁻³¹) and the torus numbers it prints violate
h⁰ − h¹ + h² = 0, so `report_hp.py` re-reads every converged point (the 600-bit midpoints, `v10_direction_points.json`) at
2000 bits with 200-digit ranks, threshold 10⁻⁵⁰, the full pivot spectrum printed, and the torus Euler characteristic and
Poincaré duality (h¹(V) = h¹(V*), h²(V) = h⁰(V*)) checked; at ρ₀ it reproduces the exact stage (h¹ = 3, h⁰(∂M) = 3, N = 0,
exact zeros at 10⁻²⁰⁵). At the deformed points the "rejected" pivots of the 60-digit report are genuine (10⁻³³ … 10⁻³⁹, forty
orders above the noise) and every zero is a zero:

| direction (ε = 0.02/|Y|) | residual | self-dual? | h¹(M; 27) | h¹(M; 27̄) | h⁰(∂M; 27), h⁰(∂M; 27̄) | h¹(∂M), h²(∂M) | N(27) |
|---|---|---|---|---|---|---|---|
| class 1 | 6.0·10⁻⁶⁸ | no (defects to 4.9·10⁻⁸) | **0** | **0** | 0, 0 | 0, 0 | **0** |
| class 2 | 1.8·10⁻⁶¹ | no (defects to 8.9·10⁻¹¹) | **0** | **0** | 0, 0 | 0, 0 | **0** |
| class 1 + class 2 | 2.7·10⁻⁶⁶ | no (defects to 2.3·10⁻⁸) | **0** | **0** | 0, 0 | 0, 0 | **0** |
| class 1 − class 2 | 7.5·10⁻⁶¹ | no (defects to 4.0·10⁻⁸) | **0** | **0** | 0, 0 | 0, 0 | **0** |

Along every direction the deformed holonomy is **not self-dual** (the θ-odd deformations they were predicted to be), the three
classes of the 27 at ρ₀ all die (h¹ = 0 for the 27 and for the 27̄), the cusp holonomy keeps **no fixed vector** in either —
B1268's bound closes to 0 ≤ N ≤ 0 — and **N(27) = 0**, exactly as pre-registered: the classes are not cusp-trivial, the deformed
cusp has no fixed vector, the count vanishes. (The 60-digit report's lines in `v10_direction_run.txt` — "h¹ = 2, h⁰(∂M) = 1,
bound −1 ≤ N ≤ 0" — are the misread described above; `report_hp_run.txt` is the record of the ranks. The points are banked
at 100 significant digits, more than the 10⁻⁶¹ … 10⁻⁶⁸ to which they are representations.)



## 5. What this settles

**The hole in the pairing law is closed by computation.** B1280 proved N(27) ≡ 0 on the germ of every E₆ point of the cusped
object's character variety where an isometry realises θ, and found exactly one direction where none does — the V₁₀ of the 42 at
the subregular point. Along that direction (both classes, their sum and their difference) genuine E₆ representations exist (the
classes are unobstructed to every order tested and Newton converges to 10⁻⁶¹ … 10⁻⁶⁸ once B1268's damping is lifted), they are
**not self-dual** — the θ-odd deformations they were predicted to be — and at each of them **h¹(M; 27) = h¹(M; 27̄) = 0**, the cusp
holonomy has **no fixed vector** in the 27 or the 27̄, and **N(27) = 0**. The mechanism is the one pre-registered: the V₁₀ classes are
not cusp-trivial, the deformed cusp keeps no fixed vector, and B1268's bound −h⁰(∂M; 27) ≤ N ≤ h⁰(∂M; 27̄) closes to 0 ≤ N ≤ 0. So
the θ-odd frame — the last frame in which the cusped object could have carried a net count of 27s — is closed on every sl₂ germ:
main's 15 % prior for N ≠ 0 resolves to 0, L207(i) and main's L204 hole are done, and the chirality map's O1 row loses its one open
direction. What remains for chirality on the object is what was outside this frame already: the higher-rank components (O2), the
general theorem (O3), and the singular G₂ closing (O4), where chirality is a 7-dimensional index and not an h¹ of m004.

**Three lessons banked with the result.** (i) B1268's Gauss–Newton damps by 10⁻²⁴·max G_ii; along a class whose corrections lie in
directions of singular value ~ε that damping stalls the search at |res| ≈ 10⁻¹³ (§4a) and a cohomology report evaluated there is
meaningless — the first run's "N = 0" lines were of that kind and are kept as a record of the failure mode. (ii) B1268's report
transfers acb → mpmath at 70 digits and decides ranks at 10⁻³⁰; at points where genuine pivots reach 10⁻³⁹ this misreads
h¹ and h⁰(∂M) and violates the torus Euler characteristic (§4e) — the consistency checks (Euler, duality) are what caught it, and
they now travel with the re-reader. (iii) The exact obstruction calculus modulo primes (§4b, §4c) is the cheap, decisive
complement to the numerics: it says where a Newton stall is geometry and where it is arithmetic.

## Controls (MB12)

- **The point** reproduces B1280's data (h¹ = 3 = 3 at the subregular point, N = 0) exactly and numerically.
- **The classes** are exact (ℚ(ω)), non-coboundary by an exact rank test, and their block h¹ = 1 matches B1280's
  one-dimensional H¹(m004; Sym¹⁰).
- **The cusp restriction** is computed exactly in the block and in the full e₆ (78 coordinates, exact Ad exponentials).
- **B1268's machinery unchanged** (imported, not copied): the Newton search, the cohomology report, the dual.
- **E70-class:** the cocycle values use the left-module Fox convention throughout (B1267's Rep.fox), the adjoint Fox
  operator of B1268 for the first-order derivative.

## Verification

- `verification/v10_direction.py` (stages 0 … 4; controls `V10_STEP`, `V10_MU`, `V10_ITERS`, `V10_CLASSES`; the exact
  stages alone in `v10_direction_stage0123_run.txt`; the stalled Newton in `v10_direction_run_stall.txt`).
- `verification/obstruction.py` (stage 5a/5b: the eight exact block cocycles, rank d¹, the second-order obstruction classes
  and the quadratic map on H¹; `obstruction_run.txt`); `verification/obstruction_higher.py` (stage 5c: formal
  integrability order by order; `obstruction_higher_run.txt`).
- `verification/report_hp.py` (stage 4′: the converged points re-read at 2000 bits / 200-digit ranks with the torus
  consistency checks; `report_hp_run.txt`; the points in `v10_direction_points.json`); the probes `probe_mu50.txt`
  (converges), `probe_step02.txt` (crawls).
- Lock `tests/test_b1350_the_v10_direction.py`: fast — stages 0 … 3 (multiplicities, the point, the two classes and
  their cusp restriction, trace-flatness); slow — stage 4.
- Depends on B1280 (the criterion and the hole), B1268 (the bound and the machinery), B1267 (the instrument), main's
  B1299 (the hole verified and priced).

*(Currency 2026-09-09: VERIFIED ON MAIN — main's B1322 re-read the four banked points with its own Fox calculus (left derivatives, full-pivot ranks at 110 digits): h¹(27) = h¹(27̄) = 0, no cusp-fixed weight, N(27) = 0 on all four; the seat's `report_hp.py` reproduced line for line; L204 CLOSED on main. The fourth order of the departure and the fixed-vector branches are B1352 and B1354 here.)*
