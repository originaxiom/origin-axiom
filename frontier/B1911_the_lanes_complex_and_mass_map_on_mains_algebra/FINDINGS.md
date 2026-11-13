# B1911 — The physical lane's elliptic complex and fermion mass map hold as algebra, on main's own code (WP-2.1, its first part; P-749)

**Verdict: PROVED** (every algebraic identity of the complex, the gauge-fixed potential and the mass map that the two parent
proofs state is checked, and holds; the analysis on the punctured surface is not part of this arc). cc (main), 2026-11-13
(S306p). The lane's proofs were read through main's binding-minimum mask at its `1aa76251f`; none of its code was run. No
data; no physical quantity is evaluated. **0 of 19.**

## 1. The answer first

The plan's WP-2.1 asks whether the lanes' curved functional, with its kinetic weights and four-slot operator, holds as
written. Its first part, read from two parent proofs (`weave_two_neutral_index_2026_10_08/PROOF.md`, lines 1–170, and
`weave_physical_mass_2026_10_08/PROOF.md`, lines 1–180), holds as algebra:

- **The complex.** C0 = E, C1 = (E⊗K̄) + 2(E⊗S), C2 = 2(E⊗S⊗K̄) + (E⊗K), C3 = E⊗K⊗K̄ with
  D0 ε = √2(D̄ε, −i[q, ε], −i[r, ε]), D1(a, u, v) = (D̄u + i[q, a], D̄v + i[r, a], [q, v] − [r, u]), D2(p1, p2, t) = D̄t − [q, p2] + [r, p1].
  **D1D0 = −i√2([D̄q, ·], [D̄r, ·], [[q, r], ·]) and D2D1 = [D̄q, v] − [D̄r, u] − i[[q, r], a] identically,** so the complex closes
  exactly when D̄q = D̄r = [q, r] = 0, as the proof says (Leibniz and Jacobi).
- **The metrics.** C0: Ω², C1: diag(½, Ω, Ω), C2: diag(Ω⁻¹, Ω⁻¹, 2), C3: 2Ω⁻². D0† and D2† as the proofs write them are the
  adjoints in these metrics. **The weight 2 on t is derived here** (the page's own entry is behind the mask); it is the F-residual
  norm's 2|t|², as the proof says C2 is.
- **The potential.** D_z a − 2iΩ([q†, u] + [r†, v]) = G + iM₁ with G (the gauge condition) and M₁ (the D-moment) Hermitian, so
  |D0†x|² = ∫(G² + M₁²)/(2Ω²); and on a charge block the moment's soft term m₀M₂/Ω² is −k times the whole a, u, v kinetic norm.
  Together: **g₆²V₂,gf = |D0†x|² + |D1x|² − k|x|²**, as written. On a background where the complex closes, |T(x, σ)|² splits with
  no cross term; on a generic background it does not (the control).
- **The mass map.** The Hessian of W₂ = ∫κ(u D̄v + i a([q, v] − [r, u])) has density dual coefficients (i t, p₂, −p₁), and
  **M = U_out T U_in**, row by row, as the proof writes M. U_in and U_out are isometries exactly when the four fermion densities are
  **(Ω², ½, Ω, Ω) for (λ, a, u, v)**. Two of the lane's files list three densities for four fields (a finding of main's reader of
  the first sealed packet, B1907); these four are what isometry requires.
- **The cusp block at h = 1.** From the second half of the complex, rescaling the two residuals by y and √(2y), with
  σ = α/(√2 y^{3/2}), gives i(∂_t + δ)v − bα and bv + i(∂_t − δ)α with δ = k + m/2 and b² = (j − m)(j + m + 1)/2, as the proof says.

## 1a. Seen first

`VERDICT topic-sweep /mass map|elliptic complex|two.neutral|weave_physical_mass|curved action|D0 dagger|WP-2.1/: 3 of 1649
arcs on main match (OPEN 2, PROVED 1); 1 register rows match (QUEUED 1)`. B1909 (the paired pole, whose last two steps wait
on this package) and P-749 (the lane's analytical results to bring in) bear on it; B1196 and B1206 match on words only.
**Literature:** the component mass structure of a supersymmetric gauge theory (the lane cites Martin's primer, equations
whose numbers the mask hides); the Hodge-type operator of an elliptic complex; standard.

## 2. How it was checked (`verification/the_complex_and_the_mass_map.py`)

The identities are local, so they are checked on a periodic square with a spectral grid (40 × 40): gl(3)-valued smooth random
fields, a smooth positive Ω, a smooth background A (and, for E7, a real connection and fields in one charge block of a
diagonal Z). κ is the trace; the Hermitian pairing is tr(X†Y); the spectral derivative is exactly skew-adjoint on the grid.
The cusp block is checked symbolically.

| | check | result | planted |
|---|---|---|---|
| E1 | the Hessian's dual coefficients (i t, p₂, −p₁) | 1.4 × 10⁻¹⁶ | (i t, p₂, +p₁) fails |
| E2 | D0† in C0 and C1 | 2.7 × 10⁻¹⁶ | weight 1 on a fails |
| E3 | D2† in C2 and C3, t's weight 2 | 3.0 × 10⁻¹⁶ | weight 1 on t fails |
| E4 | D1D0 and D2D1 as the obstruction terms | 1.6 × 10⁻¹⁵, 1.1 × 10⁻¹⁵ | — |
| E5 | M = U_out T U_in | 4.9 × 10⁻¹⁶ | U_in without Ω² fails |
| E6 | U_in, U_out isometries for (Ω², ½, Ω, Ω) | 1.2 × 10⁻¹⁶, 3.5 × 10⁻¹⁹ | — |
| E7 | g₆²V₂,gf = \|D0†x\|² + \|D1x\|² − k\|x\|², and D_z a − 2iP = G + iM₁ | both sides 1080.648…; 2.4 × 10⁻¹⁶ | the soft term as +k fails |
| E8 | the h = 1 cusp block | exact | — |
| E9 | \|T\|² with no cross term on a closed background | 2.1 × 10⁻¹⁶ | on an open one the cross term is there |

18 checks, none failing.

## 3. What is not shown

- **The analysis.** The punctured hyperbolic surface and its cusp; the complete domains and graph closures; the Fredholm
  property, the thresholds and the index (the proofs' lines 112–283 and the mass proof's lines 117–264). These are claims of
  the lane's proofs that this arc does not test.
- **The background's existence:** that a stationary background with D̄q = D̄r = [q, r] = 0 at the stated fluxes exists is a
  premise; E4 shows it is exactly what the complex needs.
- **The rest of WP-2.1:** the real gauge operator P_v = 2k†k, the gauge fixing and the one-loop weights (the lane's
  `SAME_ACTION_REAL_GAUGE_FIXING_AND_ONE_LOOP_WEIGHTS.md`), which the paired pole's steps 3, 4 and 6 need. The next arc.

## Files

- `verification/the_complex_and_the_mass_map.py` → `the_complex_and_the_mass_map.json`, `_run.txt`.
- The lock: `verification/test_b1911_the_complex.py`.

## Reproduce

```
cd frontier/B1911_the_lanes_complex_and_mass_map_on_mains_algebra/verification && python3 -B the_complex_and_the_mass_map.py
```
