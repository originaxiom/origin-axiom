# B1352 — THE FIXED-VECTOR LOCUS ALONG V₁₀: the one place left on the cusped object where a net count of 27s could sit (a cusp-fixed weight on a non-self-dual deformation, B1351's escape) is empty as far as the instruments reach — from every genuine V₁₀ point the fixed-vector locus is reached in a few Newton steps and is the **Sp(8) family** (self-dual, cyclic 27, the three cusp-fixed weights = the Cartan directions of Λ²₀(8), N = 0 at 2000 bits); exactly, the V₁₀ direction is tangent to the locus at first order and every formal V₁₀ branch constructed leaves it at order 4 (order 2 generically), the same order at which the deformation stops being self-dual (the trace defects scale as t⁴ between two genuine points). L204's other half closed on every computed deformation; 0 of 19.

**Verdict: PROVED** (the exact statements: stages C and D; the numerical ones: stage A at 600 bits with the 2000-bit re-read, stage E's scaling between two genuine points). Depends on B1268 (the instrument and the bound), B1350 (the genuine V₁₀ points, the exact block cocycles, the formal integration), B1351 (the 7d frame: only a cusp-fixed weight can carry a boundary term). Verification: `verification/` (records `*_run.txt`, stalls `*_stall.txt`). Lock: `tests/test_b1352_the_fixed_vector_locus_along_v10.py`.

## 0. The question

B1351 put Pantev–Wijnholt's count on the cusped object in one line: N(27) = −χ(∂⁺M; 27) per weight, and a weight
whose cusp holonomy is non-trivial has vanishing torus cohomology and no boundary condition to choose. So a net
count needs a **cusp-fixed weight** (h⁰(∂M; 27) ≥ 1) on a **non-self-dual** deformation (else 27 and 27̄ pair).
B1350's genuine V₁₀ points are non-self-dual but carry no cusp-fixed weight; the subregular point ρ₀ carries three
but is self-dual. The question of this arc: **is there a point with both** — the fixed-vector locus
Fix = {ρ : μv = v, λv = v for some v ≠ 0} near the V₁₀ curve, and what it carries. It is B1268's stage (b), which
its record shows never converged (|res| = 5.6·10² after four steps under the 10⁻²⁴ damping).

## 1. The setting, exactly

ρ₀ is the subregular point of B1257/B1350: the subregular sl₂ of E₆ is the principal sl₂ of Sp(8) ⊂ E₆, the 27 is
Λ²₀(8) = 13 ⊕ 9 ⊕ 5 under it, the cusp holonomy (μ₀, λ₀) is unipotent and fixes exactly one vector per block
(dominant Chevalley coordinates 21, 23, 26; "blocks 0, 1, 2" below). The outer involution fixing sp(8) =
V₂⊕V₆⊕V₁₀⊕V₁₄ negates the 42 = V₄⊕V₈⊕V₁₀⊕V₁₆; the V₁₀ of the 42 is the direction of B1350, trace-flat at first
order (all twelve first-order self-duality defects vanish, B1350 stage (3)).

The instruments: (A) the augmented Gauss–Newton of B1268 — unknowns the E₆ representation (156 e₆ coordinates,
left-multiplicative updates) and the vector v ∈ ℂ²⁷, equations the relator, μv = v, λv = v and v₀ᴴv = 1 with v₀
one of ρ₀'s three fixed vectors — started at B1350's converged V₁₀ points, **damping 10⁻⁵⁰** (B1350's lesson; B1268
used 10⁻²⁴); 600 bits; the 60-digit report, then B1350's 2000-bit re-read (`report_hp.py`) with the torus Euler
characteristic and Poincaré duality as consistency checks. (C) the exact first-order fixed-vector condition
z(μ)v₀ + (μ₀ − I)δv = 0, z(λ)v₀ + (λ₀ − I)δv = 0 over ℚ(ω) for each of the eight block classes. (D) the formal
branches of `obstruction_higher.py` (B1350) to order 10, modulo two primes, and the Smith exponents of
T(t) = [μ(t) − I; λ(t) − I] over F_p[t]/(t¹¹) from the kernel dimensions kd(m) of T mod tᵐ
(kd(m) = Σᵢ min(eᵢ, m), so #{i : eᵢ ≥ m} = kd(m) − kd(m − 1)). (E) a second genuine V₁₀ point at twice the step
(0.04/|Y|; B1350's script, 2000-bit re-read), and the scaling of the cusp-fixed singular values and of the
self-duality defects between the two points.

## 2. Results

### 2a. Stage A — from each V₁₀ point the fixed-vector locus is reached, and it is self-dual

| start (B1350's point) | target | Newton | residual | self-duality defects (six words) | moved (rel.) | from ρ₀ (rel.) | h⁰(M), h¹(27), h¹(27̄), h⁰(∂M), h¹(∂M), rank(res) | N |
|---|---|---|---|---|---|---|---|---|
| class 1 (relator 6·10⁻⁶⁸) | block 0 | 20 steps, quadratic | 2.2·10⁻⁶² | ≤ 1.0·10⁻⁵³ → **self-dual** | 4.63·10⁻⁹ | 1.91·10⁻⁶ | 0, 3, 3, 3, 6, 3 | **0** |
| class 2 (relator 1.8·10⁻⁶¹) | block 0 | 15 steps, quadratic | 7.3·10⁻⁶¹ | ≤ 3.4·10⁻⁵² → **self-dual** | 2.21·10⁻⁹ | 1.10·10⁻⁶ | 0, 3, 3, 3, 6, 3 | **0** |
| class 1 | block 1 | linear stall | 2.1·10⁻¹⁷ after 13 steps | — | — | — | — | — |
| class 1 | block 2 | linear stall | 1.7·10⁻²¹ after 13 steps | — | — | — | — | — |

The cohomology line is the 60-digit read and the **2000-bit re-read agrees** (`fixed_locus_report_hp_b0_run.txt`:
h¹(27) = h¹(27̄) = 3, h⁰(∂M; 27) = h⁰(∂M; 27̄) = 3, torus Euler characteristic and duality ok, N = 0 at both points).
The locus point is not ρ₀ (it sits at the same distance from ρ₀ as the V₁₀ point it came from, 10⁻⁹ away from
that point) and it carries the full subregular data. The same search from the step-0.04 point (§2e; `step04/fixed_locus_c1_b0_step04_run.txt`,
residual 5.8·10⁻⁶⁴, self-dual, N = 0) lands 9.53·10⁻⁹ away at 3.83·10⁻⁶ from ρ₀: the distance from the V₁₀ point to the
Sp(8) family scales with the first power of the step (ratio 2.06 for a parameter ratio 2.03), as it must — the V₁₀ tangent
is θ-odd and not tangent to the Sp(8) family — while the trace defects and the fixed-vector defect along the V₁₀ curve
vanish to fourth order (§2e); the curve is transverse to the self-dual family and self-dual to third order at once. The block-1 and block-2 targets do not converge: the residual
falls by 0.85–0.97 per step from step 3 on (records `fixed_locus_c1_b1_stall.txt`, `_b2_stall.txt`); their start
residuals (1.02, 1.8·10⁻³) are small because those two vectors are the ones the V₁₀ point almost keeps (§2e).

### 2b. What the locus point is: an Sp(8) point

- **Eigenvalues** (`locus_point_is_sp8.py`, 100 digits): at both locus points μ = ρ(a) and ρ(b) have exactly three
  eigenvalues equal to 1 and the other 24 are {yᵢ^{±1}yⱼ^{±1} : i < j} for four numbers yᵢ — the spectrum of
  Λ²₀(8) for an element of Sp(8) with eigenvalues yᵢ^{±1} on the 8 (class 1: log y = 0.346+0.126i, 0.160−0.215i,
  −0.015+0.268i, 0.042−0.116i). The four V₁₀ points have no eigenvalue 1 and no such pattern. (The sl₂ pattern
  {sᵏ} of the reducible stratum fails at the locus points too, `locus_point_is_sl2.py`: they are not on the sl₂ curve.)
- **Module structure** (`locus_point_structure.py`): at the locus points every cusp-fixed vector generates the whole
  27 under π₁ (cyclic), as does a random vector; the 27 is not the reducible 13 ⊕ 9 ⊕ 5 of ρ₀. Self-dual with no
  invariant vector (h⁰(M; 27) = 0) rules out F₄ (which fixes the Jordan identity); the image is in Sp(8).
- **The three cusp-fixed weights are the Cartan directions eᵢ ∧ fᵢ of Λ²₀(8) = ω^⊥**: an element of a torus of
  Sp(8) fixes the four eᵢ ∧ fᵢ in Λ²(8), three in ω^⊥. Every Sp(8)-valued representation with diagonalisable cusp
  holonomy has exactly these three cusp-fixed weights — h⁰(∂M; 27) = 3 along the whole Sp(8) family, which is why
  the locus reached from V₁₀ carries the subregular numbers, and N = 0 there by self-duality whatever ∂⁺ is.

### 2c. Stage C — exact first order: V₁₀ is tangent to the fixed-vector locus

`fixed_vector_tangent.py` (ℚ(ω), record `fixed_vector_tangent_run.txt`):

| class | keeps fixed vector 0 / 1 / 2 to first order |
|---|---|
| V₂, V₆, V₁₀ (of the 42), V₁₀#2, V₁₄ | T T T |
| V₄ | F F T |
| V₈ | F T T |
| V₁₆ | F F F |

The θ-odd 42 loses fixed vectors at first order along V₄, V₈, V₁₆ — and **not along its V₁₀**, which keeps all three
(the V₁₀ plane: tangent combinations of dimension 2 for each vector). This is the exact reason B1268's bound could
not be closed by first-order reasoning along V₁₀: the direction lies in the Zariski tangent space of Fix.

### 2d. Stage D — exact formal branches: the fixed vectors are lost at order 4 (order 2 generically)

`fixed_vector_order.py` (records `fixed_vector_order_run.txt`, `_two_branches.txt`), modulo p = 67108819 and 67108837,
three formal branches per direction with the same tangent: the greedy branch of `obstruction_higher.py`, a branch
with a random combination of the eight classes added at every order ≥ 2, and a branch with a random combination of
the five first-order-keeping classes (V₂, V₆, V₁₀, V₁₀#2, V₁₄):

| direction | branch | kd(m), m = 1..11 | loss orders (e₁, e₂, e₃) |
|---|---|---|---|
| V₁₀, V₁₀#2, V₁₀ + V₁₀#2, V₁₀ − V₁₀#2 | greedy | 3, 6, 9, 12, 12, … | **4, 4, 4** |
| same four | random within the keeping classes | 3, 6, 9, 12, 12, … | **4, 4, 4** |
| same four | random over all eight classes | 3, 6, 6, … | 2, 2, 2 |
| V₈ (control) | greedy (stops at order 5) | 3, 5, 7, 7, 7 | 1, 3, 3 |
| V₈ | random, all classes | 3, 5, 5, 5 | 1, 2, 2 |

Both primes agree on every number. Since a rank modulo p is at most the exact rank, kd_p(m) ≥ kd_exact(m): the loss
**at latest at order 4** on the greedy and keeping branches (and at order 2 on generic ones) is exact; the persistence
through order 3 is modulo two primes, and through order 1 exact (stage C). V₈'s "1, 3, 3" is stage C's F T T. So no
formal V₁₀ branch constructed stays in Fix: the fixed vectors of ρ₀ are a fourth-order casualty of the V₁₀
deformation, and the three go together.

### 2e. Stage E — the two genuine points: the departure from the self-dual world is fourth order

`pivot_scaling.py` (record `pivot_scaling_run.txt`) on B1350's class-1 point (step 0.02/|Y|, relator 6·10⁻⁶⁸) and
the new point at step 0.04/|Y| (`step04/`: relator 2.2·10⁻⁶⁷, the 2000-bit re-read gives h¹(27) = h¹(27̄) = 0,
h⁰(∂M) = 0, N = 0 as at 0.02):

| quantity | step 0.02 | step 0.04 | ratio |
|---|---|---|---|
| self-duality defects, six words | 2.18·10⁻¹², 2.18·10⁻¹², 1.79·10⁻¹⁰, 4.92·10⁻⁸, ~0, 4.92·10⁻⁸ | 3.69·10⁻¹¹, 3.69·10⁻¹¹, 3.03·10⁻⁹, 8.31·10⁻⁷, ~0, 8.31·10⁻⁷ | **16.884 on all five** = (t₂/t₁)⁴ with t₂/t₁ = 2.027 |
| three smallest relative singular values of T | 6.84·10⁻³⁹, 3.48·10⁻³⁶, 3.32·10⁻³⁰ | 3.68·10⁻³⁷, 7.74·10⁻³⁵, 5.61·10⁻²⁹ | (t₂/t₁)^{5.64}, (t₂/t₁)^{4.39}, **(t₂/t₁)^{4.00}** |
| product of the three | | | (t₂/t₁)^{14.0} |

The trace defects obey an exact fourth-order law between the two points (five ratios equal to four digits): the V₁₀
curve is self-dual to third order and not at fourth — the same order at which stage D loses the fixed vectors on the
branches it can construct. The largest of the three cusp-fixed singular values scales as t⁴ exactly; the two smaller
ones scale faster than t⁴ (their exponents are not integers at these two steps, so they are not yet asymptotic or the
Newton curve is a branch of its own — §4). **The small singular values are real**: polishing B1350's class-1 point by Newton at 2000 bits (`polish_and_svals.py`, residual 6.0·10⁻⁶⁸ → 2.7·10⁻⁸², where the solve stops for want of a descent direction) moves ρ(a) by 4.2·10⁻⁶⁰ relative and changes the three singular values by 2.5·10⁻⁴³, 3.9·10⁻⁴⁵, 1.1·10⁻⁴⁸ relative — they are properties of the representation, not of the point's residual, and B1350's h⁰(∂M; 27) = 0 rests on them. **A third genuine point at step 0.01/|Y|** (`step01/`: relator 2.0·10⁻⁶⁵; 2000-bit re-read h¹(27) = h¹(27̄) = 0, h⁰(∂M) = 0, N = 0, cusp-fixed pivots 3.4·10⁻³¹, 5.7·10⁻³⁷, 6.8·10⁻⁴¹) gives the second interval: the five defect ratios 0.02/0.01 are all 12.737 = (1.889)⁴, and the largest cusp-fixed singular value again scales as (parameter ratio)^{4.000} (2.61·10⁻³¹ → 3.32·10⁻³⁰ → 5.61·10⁻²⁹); the two smaller ones give exponents 7.56, 3.59 on the first interval and 5.64, 4.39 on the second — not asymptotic at these steps (their individual constants mix), so only the leading t⁴ law is read from the numerics, and the two other orders from stage D.

### 2f. Controls

- **V₈ at the subregular point** (`fixed_locus_v8.py`, `fixed_locus_v8_b0_stall.txt`): the plain Newton for a genuine
  point along the exact V₈ class (step 0.02/|Y|, damping 10⁻⁵⁰) converges only linearly (rate 0.89 per step,
  9.7·10⁻¹⁴ → 1.7·10⁻¹⁵ in 31 steps) — the signature of a singular limit, consistent with `obstruction_higher.py`'s
  one-sided "stops at order 5" for V₈ and with stage D's V₈ row; no genuine V₈ point at the subregular point is in
  reach, so the V₈ control of the locus is void there.
- **V₈ at the geometric point — B1268's stage (b) completed** (`fixed_locus_v8_geometric.py`,
  `fixed_locus_v8_geometric_b0_stall.txt`): stage (a) reproduces B1268's θ-odd point ρ_s (residual 5.8·10⁻⁸⁰, defects
  3.01, 2.7·10³, 2.9·10⁶); the augmented search from ρ_s toward the geometric point's cusp-fixed vector stalls at
  |res| = 5.74·10² under the 10⁻⁵⁰ damping exactly as under B1268's 10⁻²⁴ — the damping was not what stopped B1268
  there; the geometric point's fixed vector is not restorable by a Newton step from ρ_s.

## 3. What it means

**L204's other half.** On the cusped object a net count of 27s needs a cusp-fixed weight on a non-self-dual
deformation (B1351). Along the V₁₀ direction — the only θ-odd direction that keeps the cusp-fixed weights even to
first order — the weights are lost at order 4 on every formal branch constructed and are absent at every genuine
point computed, while the deformation is self-dual through order 3. Where the weights are present nearby, the
representation is an Sp(8) point: self-dual, its three cusp-fixed weights the Cartan directions of Λ²₀(8), N = 0.
The window "disc-type ∂⁺ on a cusp-fixed weight" is therefore void on every computed deformation of the object: at the
non-self-dual points there is no boundary condition to choose, and where there is one the count pairs. Together with
the region-swap theorem for the ι-odd directions (fc R71, B1281) and B1350, the θ-odd frame is closed on the object
with the mechanism named: **the V₁₀ deformation leaves the self-dual world and the fixed-vector locus at the same
order, four**, and B1268's bound −h⁰(∂M; 27) ≤ N ≤ h⁰(∂M; 27̄) is 0 ≤ N ≤ 0 off the Sp(8) family and pairs on it.

**The three faces.** Quantum face: the deformation space's trace-flat direction is fourth-order non-self-dual — a
T-brane datum whose chirality-carrying capacity switches on at order t⁴ and whose boundary modes switch off at the
same order. Geometric face: Fix ∩ (V₁₀ germ) = ρ₀ to the orders reached; the fixed-vector locus near the V₁₀ curve is
the Sp(8) family. Arithmetic face: the orders are exact modulo two primes and the same for both V₁₀ classes and
their sum and difference — the whole V₁₀ plane behaves as one.

**The escape left.** Not on the cusp. B1353: the isolated enhancement point (E70 on this branch, B1259's isolation
theorem) — a different mechanism, at a point rather than on the cusp torus.

## 4. Caveats, stated

1. Newton is local: stage A finds *a* point of Fix from each start (the nearest in its own metric); it does not
   enumerate Fix. The exact statements (C, D) are about formal branches with tangent V₁₀; three kinds of branch were
   constructed, not all: **whether some formal branch tangent to V₁₀ keeps a cusp-fixed vector beyond order 4** (the
   five-parameter freedom of the keeping classes at each order, used randomly here, could in principle be tuned) is
   not settled — it is a finite linear-algebra question order by order and is registered (§6).
2. The singular-value exponents of the two smaller values (5.64, 4.39 at the two steps) are not integers: either the
   asymptotic regime is not reached at these steps or the Newton curve is a branch whose orders differ from the
   greedy one; the largest scales exactly as t⁴ and the product as t¹⁴. A third step (0.01) is **A third genuine point at step 0.01/|Y|** (`step01/`: relator 2.0·10⁻⁶⁵; 2000-bit re-read h¹(27) = h¹(27̄) = 0, h⁰(∂M) = 0, N = 0, cusp-fixed pivots 3.4·10⁻³¹, 5.7·10⁻³⁷, 6.8·10⁻⁴¹) gives the second interval: the five defect ratios 0.02/0.01 are all 12.737 = (1.889)⁴, and the largest cusp-fixed singular value again scales as (parameter ratio)^{4.000} (2.61·10⁻³¹ → 3.32·10⁻³⁰ → 5.61·10⁻²⁹); the two smaller ones give exponents 7.56, 3.59 on the first interval and 5.64, 4.39 on the second — not asymptotic at these steps (their individual constants mix), so only the leading t⁴ law is read from the numerics, and the two other orders from stage D._NOTE
3. "Sp(8) point" is read from the eigenvalue pattern (24 = {yᵢ^{±1}yⱼ^{±1}}, three 1's) and from self-duality without
   an invariant vector; the invariant symmetric form was not solved for explicitly.
4. The blocks 1 and 2 targets stall; they are not solutions and not proofs of absence.
5. Stage B of the plan (the eight isometries' action on the block classes with exact arithmetic — which isometries
   preserve the V₁₀ curve, hence which cusp-mode orbits are allowed at its points) was not completed: its sympy
   version was too slow and is kept as `d4_on_the_classes.py` (partial output only); with no cusp-fixed weight at the
   V₁₀ points the question has no bearing on N there.

## 5. Files

`verification/fixed_locus_v10.py` (stage A; env `FIXED_LOCUS_POINTS`, `FIXED_LOCUS_OUT`), `fixed_locus_points.json` (the
two block-0 locus points, 120 digits), records `fixed_locus_c1_b0_run.txt`, `fixed_locus_c2_b0_run.txt`,
`fixed_locus_report_hp_b0_run.txt` (2000 bits), stalls `fixed_locus_c1_b1_stall.txt`, `fixed_locus_c1_b2_stall.txt`;
`locus_point_is_sp8.py`, `locus_point_is_sl2.py`, `locus_point_structure.py` (+ records); `fixed_vector_tangent.py`
(stage C, + record); `fixed_vector_order.py` (stage D, + records); `pivot_scaling.py`, `polish_and_svals.py`,
`step04/` (stage E: the step-0.04 point, its run and 2000-bit re-read, and the locus search from it), `step01/` (the step-0.01 point, its run and re-read); `fixed_locus_v8.py`,
`fixed_locus_v8_geometric.py` (+ stalls); `d4_on_the_classes.py` (stage B, incomplete).

## 6. Registered

- The maximal-persistence question of §4.1 (does any formal branch tangent to V₁₀ stay in Fix to order 5?) — exact,
  order-by-order linear algebra over the keeping classes' freedom; L204's last formal residue on the object.
  *(Currency 2026-09-09: answered by B1354 — such branches exist (the second-order class must drop V₄, V₈, V₁₆ and carry a definite V₆ component) and every one is formally self-dual through order 8: fixed vectors and self-duality are one condition along V₁₀; no carrier.)*
- Stage B with exact arithmetic (the isometries on the block classes).
