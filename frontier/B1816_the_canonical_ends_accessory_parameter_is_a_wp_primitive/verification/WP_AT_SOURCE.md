# WP AT SOURCE — which measure is native to B1667's construction (P-481; literature at source; audit room, 2026-10-29)

*Read-only for the repository. Data-free (no SM quantity anywhere). One exploratory, unsealed numerical check on B1667's
sealed instrument (§5), run in the scratchpad: nothing in it is a banked result.*

## 0. Answer first

- **The native measure is Weil–Petersson.** B1667's accessory parameter is a primitive of the WP Kähler form, not of the
  hyperbolic area form. With C = 2c the Schwarzian accessory parameter (c is the instrument's):
  - **∂C/∂τ̄ = i·h_WP(τ)**, where h_WP = ⟨∂_τ, ∂_τ⟩_WP is in Wolpert's normalisation (cometric ∫φψ̄ρ⁻², ω_WP = ½Σdℓ∧dτ_FN);
  - equivalently **4·∂c/∂τ̄ = i·J**, where J dx∧dy = dℓ∧dt is the Fenchel–Nielsen area.
- **Status of that identity.**
  - It follows from McMullen's Theorem 1.5. That theorem is proved for genus g with n punctures, so it covers T(1,1).
    The step is the holomorphy of the ℘-reference: **derived here, not found stated in a source.**
  - Fırat (2023) states it as an unproved claim, calibrated at the cusp.
  - **§5 checks it pointwise on the instrument:**
    - 13 points from Im τ = 0.95 to 8, by two independent routes, the accessory parameter and the Fenchel–Nielsen
      Jacobian of the traces;
    - they agree to ≤ 4.4 × 10⁻⁶;
    - Re ∂c/∂τ̄ = 0 to ≤ 3.9 × 10⁻⁶.
    - It is unsealed.
- **Cusp constant.** g_WP = (π²/2)|dτ|²/(Im τ)³ · (1 + O(1/Im τ)) in Wolpert's normalisation. In the symplectic
  normalisation ω = Σdℓ∧dτ (Mirzakhani, Wright, Fırat) the constant is π².
- **Volume of H/PSL(2,ℤ).** π²/12 in Wolpert's normalisation, π²/6 in the symplectic one. Halve each for the stack or
  orbifold convention.
- **Height tail under the normalised WP measure:**
  - **P(Im τ > Y) = 3/Y² to leading order.** Sharper: 3/(Y + 4 ln 2/π)² · (1 + O(Y⁻³)) + O(e^(−2πY)).
  - The bare 3/Y² is poor below Y ≈ 10: it gives 0.1875 at Y = 4, where the exact value is 0.1267.
  - **Exactly in the systole: P(ℓ_sys < ε) = 3ε²/π² for ε ≤ 2 arcsinh 1.**
  - Hyperbolic area for comparison: P = 3/(πY), exactly, for Y ≥ 1.
- **What is native to which structure:**
  - **Hyperbolic area** belongs to the Teichmüller metric and flow, the Masur–Veech (Haar) measure, and the horocycle
    flow.
  - **WP** belongs to the fibre's hyperbolic uniformisation (the accessory parameter and the Liouville action), the
    Fenchel–Nielsen twist and earthquake flows, and the WP geodesic flow, which is ergodic for (1,1).

## 1. The instrument's accessory parameter (read in full: `frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.py`)

**The equation and its normalisation.**
- The equation is y'' + (℘(z)/4 + c) y = 0, with ℘ for the lattice ℤ + τℤ (periods 1 and τ) and Laurent constant term 0.
- Its Schwarzian is {w, z} = ½℘(z) + 2c, so **C := 2c is the Schwarzian accessory parameter.** This is:
  - Fırat's c at border length 0, from his eq. (2.10): T = δ℘ + c with δ = ½ and ψ'' + ½Tψ = 0;
  - Takhtajan–Zograf's convention for the Schwarzian (T_φ, with u'' + ½T_φ u = 0).

**How c is fixed.**
- Newton on c makes Im tr A_a = Im tr A_b = 0, so the monodromy is Fuchsian.
- c is continued from c = 0 at τ = i; this excludes a grafted root.
- The gate checks c = 0 at i and at ω, and the Markov relation x² + y² + z² = xyz on the Fricke traces.

**What the instrument exposes:**
- c(τ);
- the Fricke traces x = |tr A_a|, y = |tr A_b|, z = |tr A_aA_b|, where a is the 1-cycle, short at the cusp;
- the cusp translation λ, min|c_γ| and Im B.
- **The traces are all that the WP recipe in §3 needs.**

**Modularity.** C(τ+1) = C(τ) and C(−1/τ) = τ²C(τ). The involution gives C(−τ̄) = C̄.
- Source: Fırat (2.13)–(2.14), §2.2 read.
- Menotti, abstract read, calls the Heun accessory parameter "a weight two modular form" and real-analytic in τ away from a
  measure-zero set.

## 2. Q1 — the WP metric on M(1,1) near the cusp

**Normalisations (at source).**
- Wolpert 2008, "The Weil–Petersson metric geometry" (arXiv:0801.0175; §2 read).
  - Definition 1 is the cometric ⟨φ, ψ⟩ = ∫ φψ̄ (ds²)⁻¹.
  - Theorem 3 gives the Kähler form, ω_WP = ½ Σ dℓ_j ∧ dτ_j.
- BMW (arXiv:1004.5343; introduction and §1.4–1.5 read) use the same normalisation: ω_WP = ½ Σ dℓ ∧ dτ and
  g_WP(v, w) = ω_WP(v, Jw).
- Wright's tour (arXiv:1905.01753; §2.8 and §3 read) instead defines ω_WP := Σ dℓ_i ∧ dτ_i, and calls it "twice the
  one arising from the Weil-Petersson Kähler structure".
- McMullen (2000, §1) writes "ω_WP = dℓ ∧ dτ" in an informal paragraph with all constants dropped (ℓ ∼ 1/y, τ ∼ x/y). Do
  not take constants from it.

**The boundary expansion (at source).** Wolpert 2003, "Geometry of the WP completion" (arXiv:math/0502528), Theorem 2
and Corollary 4 (read).
- In hyperbolic-metric plumbing coordinates t, g_WP(∂_t, ∂_t) = π³/(|t|²(−log|t|)³) · (1 + O((log|t|)⁻²)).
- Equivalently, dg² = π³(4dr² + r⁶dθ²) with r = (−log|t|)^(−1/2).
- The same survey, in the proof of Corollary 21 (read), gives ℓ = 2π²/(−log|t|) + O((log|t|)⁻³). Corollary 21 itself
  gives the WP distance to the stratum as (2πℓ)^½ + O(ℓ²).
- Masur (1976, Duke 43, 623–635) is the original expansion. **Not read**; seen only through Wolpert's citation of it.
- Yamada's refinement and Wolf–Wolpert: **not read.**

**For M(1,1)** (a substitution, mine):
- The plumbing parameter is t = κq(1 + O(q)) with q = e^(2πiτ). So |dt|/|t| = 2π|dτ| and −log|t| = 2π Im τ − log|κ|.
- Hence **g_WP = (π²/2) |dτ|²/(Im τ)³ · (1 + O(1/Im τ))** in Wolpert's normalisation, and π²|dτ|²/(Im τ)³ in the
  symplectic one.
- **Three independent consistency checks, all at source:**
  - Wolpert 2008's table (read) gives ⟨grad ℓ^½, grad ℓ^½⟩ = 1/(2π) + O(ℓ³). With ℓ ≈ π/y this forces the constant π²/2.
  - Wolpert 2003 Cor. 21, and Gadre (arXiv:2011.12034, §2.1 read) citing Wolpert's Cor. 4.10, give the WP distance to
    the cusp as √(2πℓ) + higher order. Integrating (π/√2) y^(−3/2) dy gives √2 π y^(−1/2) = √(2π·π/y). ✓
  - ω = ½dℓ∧dt with ℓ ≈ π/y and t ≈ ℓ Re τ gives ½ · π²/y³ dx∧dy. ✓
- BMW §0.1 and Matheus's notes (arXiv:1601.00690, Ex. 2.12) state g_WP ∼ 2|dz|²/Im(z)³ "to first order". The constant
  there is not meaningful: they set ℓ ∼ 1/y and drop the π's.

**The 1/Im τ correction**, which matters below Im τ ≈ 5.
- The constant κ comes from the standard cusp coordinates of the limiting thrice-punctured sphere ℂ∖{0, 1}. The
  λ-function gives λ = 16 e^(iπτ) + …, so the cusp coordinate is ζ/16 at 0, and likewise at ∞.
- Gluing ζ ∼ qζ then gives **t = q/256**, so ℓ = π/(Im τ + δ) with **δ = 4 ln 2/π ≈ 0.88254**.
  - This derivation is mine.
  - It **agrees exactly with Fırat's** eqs. (3.16)–(3.17) at λ = 0: ℓ = 2πλ_s ≈ 2πξ, ξ = 2π/(s₁ − log|q|²), and
    s₁(0) = −8(γ + ψ(½)) = 16 ln 2 (§3.2 read).
  - Fırat's λ_s series has its first perturbative correction at relative order ξ³ (eq. 3.21).
- So **h_WP = (π²/2)/(y + δ)³ · (1 + O(y⁻³)) + O(e^(−2πy))**, with y = Im τ.
- The sealed run gives π/ℓ − y = 0.8189, 0.8386, 0.8579, 0.8668 at y = 1.5, 2, 3, 4 (x = 0.25), approaching δ.
- §5 adds y = 5, 6, 8, where π/ℓ − y = 0.8717, 0.8746, 0.8777. The O(y⁻³) term fits 5ζ(3)/(π(y+δ)³) in h_WP to 3 digits
  of the correction.

**Volume.** M(1,1) = H/PSL(2,ℤ) as a set.
- **π²/6 in the symplectic normalisation.**
  - Wright §3 (read) applies Mirzakhani's McShane unfolding with ω = dℓ∧dτ; it gives ½Vol = ∫∫ (1+e^ℓ)⁻¹ = π²/12.
  - Fu (arXiv:1506.04534, §3 read) gives the same: Vol(M(1,1)) = 2∫ℓ/(1+e^ℓ)dℓ = π²/6.
  - Fırat (3.39) gives V(L) = π²/6 + L²/24 in his conventions.
- **π²/12 in Wolpert's normalisation.**
- **The stack convention halves both,** because every point carries the elliptic involution (Wright, footnote 1).
- Wolpert's original computation (CMH 58 (1983) 246–256): **not read.** It is reported as π²/6 by secondary sources only.

**The height tail** (normalised, so independent of convention).
- Leading order: ∫ over |x| ≤ ½, y > Y of (π²/2)y⁻³, divided by π²/12, gives **P_WP(Im τ > Y) = 3/Y² + O(Y⁻³)**.
- Exact statement in the systole. This is Mirzakhani's unfolding, plus the collar lemma: two distinct simple geodesics on a
  punctured torus intersect, so sinh(ℓ_α/2)sinh(ℓ_β/2) ≥ 1.
  - The systole is therefore unique when it is below 2 arcsinh 1, and **P_WP(ℓ_sys < ε) = (ε²/2)/(π²/6) = 3ε²/π²
    exactly for ε ≤ 2 arcsinh 1 ≈ 1.7627.**
  - At the bound, P = 0.9445. The supremum of the systole is 2 arccosh(3/2) = 1.9248, at ω.
  - The collar-lemma constant is standard (Buser), **not read at source.**
- **Refined tail:** P_WP(Im τ > Y) = 3ℓ(Y)²/π² up to O(q), so P ≈ 3/(Y + δ)².

| Y | P_WP = 1 − 12c(¼+iY)/π² | 3ℓ_a²/π² (sealed traces) | 3/(Y+δ)² | 3/Y² | P_hyp = 3/(πY) |
|---|---|---|---|---|---|
| 1.5 | 0.55788 | 0.55788 | 0.52849 | 1.333 | 0.6366 |
| 2 | 0.37233 | 0.37233 | 0.36105 | 0.7500 | 0.4775 |
| 3 | 0.20157 | 0.20157 | 0.19902 | 0.3333 | 0.3183 |
| 4 | 0.12666 | 0.12666 | 0.12584 | 0.1875 | 0.2387 |

- The first two columns are the two exact routes of §3, evaluated on the sealed run's own numbers. They agree to 5
  digits.
- **The bare 3/Y² is a poor approximation below Y ≈ 10.** Use 3/(Y + 4 ln 2/π)², or the exact routes.

## 3. Q2 — Zograf–Takhtajan, and the accessory parameter of the punctured torus

**What is proved, at source:**
- **Punctured spheres.** Takhtajan–Zograf; the statements are restated in the intro of arXiv:math/0112170 (read) and
  in Park–Takhtajan–Teo §2.2 (read).
  - (I) c_i = −(1/2π) ∂S/∂z_i;
  - (II) ∂c_i/∂z̄_k = (1/2π)⟨∂/∂z_i, ∂/∂z_k⟩_WP;
  - so ∂∂̄S = −2i ω_WP, and −S is a Kähler potential.
  - Here T_φ = Σ[1/(2(z − z_i)²) + c_i/(z − z_i)] with u'' + ½T_φ u = 0.
- **Compact surfaces (Schottky).** Zograf–Takhtajan 1987, cited as footnote 1 of math/0112170; the original was **not read**.
  McMullen (§1, read) restates it as d(σ_F − σ_S) = −iω_WP, "discovered by Takhtajan and Zograf".
- **Genus g with n punctures, quasi-Fuchsian reference.** McMullen, "The moduli space of Riemann surfaces is Kähler
  hyperbolic" (Annals 151, 2000; arXiv:math/0010022; §1, §2 and the start of §7 read).
  - The setting is S of "genus g with n punctures", with the WP cometric ∫ρ⁻²|φ|².
  - Theorem 1.5: θ_WP(X) = σ_F(X) − σ_QF(X, Y) = −β_X(Y) satisfies **d(iθ_WP) = ω_WP**.
  - BMW (§1.4, read) restate it as their Theorem 1.1(3), attributing it to McMullen's Theorem 7.1.
- **Schottky with punctures, S(g,n).** Park–Takhtajan–Teo (arXiv:1508.02102; Theorems 1–4 read).
  - Here the Liouville action is a potential for a *combination*: ∂∂̄S = −2i(ω_WP − (4π²/3)ω_TZ), Theorem 2(iii).
  - The Takhtajan–Zograf metric enters through the regularisation at the punctures.
  - On quasi-Fuchsian deformation spaces of type (g,n), Theorem 4 gives dϑ = ∂∂̄S = −2iω_WP, pure WP.
  - **Caution:** not every reference gives pure WP. §5 tests whether the ℘-reference does.

**For the once-punctured torus with the Lamé / ℘ reference.**
- **The relation I derive** (the derivation is mine; not found stated in any source):
  - The flat coordinate z is a fibre coordinate on the universal curve (ℂ × H)/ℤ² that depends holomorphically on τ.
    ℘(z; τ)dz² is holomorphic in τ.
  - So σ_ref := [z-structure] + ½℘ dz² is a holomorphic section of the projective structures adapted to the cusp.
  - σ_F − σ_ref = C(τ) dz² lies in Q(X). Here the quadratic differentials with at most a simple pole at the puncture are
    the constants times dz², because the residue sum vanishes.
  - σ_QF(·, Y) − σ_ref is then a holomorphic (1,0)-form on H, so d(σ_F − σ_ref) = d(σ_F − σ_QF) = −iω_WP by McMullen.
  - With the pairing ⟨q, μ⟩ = ∫qμ, a constant Beltrami μ = ε moves τ by δτ = −2iε Im τ. So σ_F − σ_ref is the 1-form
    ϑ = (i/2) C dτ, and dϑ = −∂_τ̄C dx∧dy.
  - Hence **∂C/∂τ̄ = i h_WP**, which means:
    - **Re ∂C/∂τ̄ = 0;**
    - **h_WP = Im ∂C/∂τ̄ = ½(∂_y Re C + ∂_x Im C);**
    - **ω_WP = h_WP dx∧dy = ½ dℓ∧dt.**
  - In the instrument's c: **∂c/∂τ̄ = (i/2)h_WP = (i/4)J.**
- **This is the torus analogue of Takhtajan–Zograf (II),** with ∂/∂z_i replaced by ∂/∂τ and the factor 1/(2π) replaced
  by i through the τ-pairing.
- **Fırat (arXiv:2306.08599, §3.3 read)** claims g_ττ̄ = A ∂_τ̄ c_F = −2πiA ∂_τ∂_τ̄ S_HJ with A = −2i, using ω = dℓ∧dθ.
  He fixes A in the degeneration limit and tests it by Monte Carlo volume (V(L) ≈ 1.635 + 0.0413L² against
  π²/6 + L²/24).
  - His status words: "As far as the knowledge of the author goes such a relation hasn't been proven".
  - His A = −2i is exactly the derived relation: −2i · (i/2)J = J in his normalisation.
- **Physics-level antecedents** (Hadasz–Jaskólski–Piątek on the classical torus block and the accessory parameter;
  Piątek 2014): **not read.**
- **Keen–Rauch–Vasquez** (Trans. AMS 255 (1979) 201–230): **only the bibliographic record and a search summary were
  seen.** It is the origin of "the accessory parameter of Lamé's equation" for punctured tori; its exact normalisation
  was not checked.

**Two closed-form consequences** (derived; conditional on the relation, which §5 checks).
- **(a) The cusp value is the WP volume.**
  - As Im τ → ∞, C → π²/6. This holds at source: Fırat (3.28)–(3.31) give c → (1+λ²)π²/6.
  - Independently: pulling the thrice-punctured-sphere connection back through u = e^(2πiz) gives {w, z} = π²/(2 sin² πz)
    = ½℘_∞ + π²/6.
  - By modularity, ϑ = (i/2)C dτ is invariant under T and S, so Stokes on the standard fundamental domain keeps only the
    cusp edge. That gives **∫_F h_WP = ½·π²/6 = π²/12**, which is Wolpert's volume.
- **(b) An exact horocycle and level-set law.**
  - On the cylinder H/⟨τ ↦ τ+1⟩ the coordinates (ℓ_a, θ_a = 2πt/ℓ) are global, and ω = d((ℓ²/8π)dθ). Stokes then gives
    **∮_{ℓ_a=ε} C dτ = π²/6 − ε²/2** for every ε. This is the accessory-parameter form of Mirzakhani's thin-part volume
    ε²/2.
  - Along a horocycle, ⟨C⟩_x(Y) = π²/6 − ½⟨ℓ_a²⟩_θ(Y). So **P_WP(Im τ > Y) = 1 − (6/π²)⟨C⟩_x(Y) for Y ≥ 1.**
  - On the sealed run's column Re τ = 0.25, Re C agrees with π²/6 − ℓ_a²/2 to within:
    - 1.8 × 10⁻⁵ at Im τ = 1.25;
    - 10⁻⁶ at Im τ = 2;
    - 4 × 10⁻⁴ at Im τ = 1.
  - So the §2 table's first two columns agree. At the cusp this also matches Fırat's C ≈ π²/6 − 2π²ξ².

## 4. Q3 — computing g_WP(τ) numerically from B1667's instrument

**Inputs.** τ, then c(τ) from `solve_accessory`, then the traces (x, y, z) from `monodromy` and `traces`.

- **Route A: the Fenchel–Nielsen Jacobian.** Pure hyperbolic geometry; no theorem about C is needed.
  1. ℓ = 2 arccosh(x/2), the a-curve, which is the systole on the standard domain.
  2. t = 2 arcsinh((2z − xy)/(2x)), the twist along a.
     - Derived from the punctured-torus identities cosh(ℓ_b/2) = coth(ℓ/2)cosh(t/2) and
       cosh(ℓ_ab/2) = coth(ℓ/2)cosh((t+ℓ)/2), the latter because a Dehn twist shifts t by ℓ.
     - Checks: t = 0 at i, t = ℓ/2 at ω, and t = ℓ Re τ at 0.25 + 4i to 5 digits.
     - The identities are standard (Wolpert 1982; Buser) but **were not read at source.**
  3. **h_WP(τ) = ½ |∂(ℓ, t)/∂(Re τ, Im τ)|**, by central differences with step 10⁻³. That costs 4 extra accessory
     solves of about 2 s each.
- **Route B: the accessory parameter, one derivative.**
  - **h_WP = Im ∂C/∂τ̄ = ½(∂_y Re C + ∂_x Im C)** with C = 2c.
  - Built-in check: Re ∂C/∂τ̄ = ½(∂_x Re C − ∂_y Im C) = 0.
  - Routes A and B are independent: A uses only lengths and twists, B only c. Their agreement is the test of §3.
- **Route C: closed forms.**
  - Near the cusp: h_WP ≈ (π²/2)/(Im τ + 4 ln 2/π)³.
  - Tails: P(Im τ > Y) = 1 − (6/π²)⟨C⟩_x(Y), or 3ℓ_a²/π² up to O(q).
- **Closed-form checks available:**
  - C(i) = C(ω) = 0, already in the instrument's gate;
  - C → π²/6;
  - ∫h = π²/12;
  - ℓ = π/(y + 4 ln 2/π)(1 + O(y⁻³));
  - ∮_{ℓ=ε} C dτ = π²/6 − ε²/2;
  - P(ℓ_sys < ε) = 3ε²/π².
- **The hyperbolic alternative fails visibly.** The only weight-2 real-analytic modular C_hyp with ∂̄C_hyp ∝ the Poincaré
  form and the same cusp value is (π²/6)E₂*(τ), with E₂* = E₂ − 3/(πy).
  - It has π²/6 − C_hyp ≈ (π/2)/y. B1667's C has π²/6 − C ≈ (π²/2)/y².
  - At τ = 0.25 + 4i these are 0.3927 and 0.2083 respectively.

## 5. Exploratory numerical check on B1667's instrument (UNSEALED; scratchpad; not a banked result)

**What was run.**
- Script:
  `reader_scratch/wp_vs_accessory.py` (copied from session storage at landing), with output in `.jsonl` and `.log`.
  The probes `near_i.py` and `probe_i.py` were not kept.
- It imports the sealed instrument read-only (no bytecode written) and uses its own `solve_accessory`, `monodromy`,
  `traces` and `newton_walk`.
- Each start is the sealed run's c at the nearest grid point.
- At each τ, the 4 neighbours τ ± 10⁻³ and τ ± 10⁻³i are solved, and two independent quantities are formed:
  - **Route B:** h_B = 2 Im ∂c/∂τ̄;
  - **Route A:** h_A = ½ ∂(ℓ, t)/∂(x, y), from the traces alone.
- Run conditions: 2 workers at nice 10 with single-threaded BLAS, alongside a running 8-worker suite.
- **Disclosed:** a first launch was stopped after about 8 minutes, before any output. It had 6 workers, too many beside
  the suite, and a Newton tolerance of 10⁻¹³ that the instrument cannot reach. The rerun used the instrument's own
  tolerance of 10⁻¹².
- 12 + 2 points; the slowest, τ = 0.25 + 8i, took 302 s.

| τ | h_WP = 2 Im ∂c/∂τ̄ | h_A / h_B | ∣Re ∂c/∂τ̄∣/∣∂c/∂τ̄∣ | (π²/2)/(y+δ)³ | (π/4)/y² (hyperbolic form, same total) |
|---|---|---|---|---|---|
| 0.45+0.95i | 1.06967 | 0.999996 | 1.3e-6 | 0.80188 | 0.87025 |
| 0.02+1.00i | 0.96108 | 1.000004 | 5.3e-7 | 0.73967 | 0.78540 |
| 0.25+1.00i | 0.96284 | 1.000000 | 3.9e-6 | 0.73967 | 0.78540 |
| 0.10+1.10i | 0.79330 | 1.000002 | 1.5e-6 | 0.63329 | 0.64909 |
| 0.03+1.20i | 0.66396 | 1.000002 | 3.1e-7 | 0.54637 | 0.54542 |
| 0.15+1.25i | 0.61040 | 1.000001 | 1.0e-6 | 0.50883 | 0.50265 |
| 0.35+1.50i | 0.41620 | 1.000000 | 3.2e-7 | 0.36488 | 0.34907 |
| 0.05+2.00i | 0.22215 | 1.000000 | 1.2e-8 | 0.20604 | 0.19635 |
| 0.25+3.00i | 0.087010 | 1.000000 | 2.8e-10 | 0.084318 | 0.087266 |
| 0.25+4.00i | 0.043080 | 1.000000 | 5.7e-10 | 0.042397 | 0.049087 |
| 0.25+5.00i | 0.024467 | 1.000000 | 1.4e-10 | 0.024242 | 0.031416 |
| 0.25+6.00i | 0.015224 | 1.000000 | 3.8e-9 | 0.015136 | 0.021817 |
| 0.25+8.00i | 0.0070604 | 1.000000 | 9.9e-9 | 0.0070414 | 0.012272 |

**Reading.**
- **Over 13 valid points, max ∣h_A/h_B − 1∣ = 4.4 × 10⁻⁶ and max ∣Re ∂c/∂τ̄∣/∣∂c/∂τ̄∣ = 3.9 × 10⁻⁶.**
- The relation ∂C/∂τ̄ = i h_WP holds pointwise, from the symmetric points out to Im τ = 8, at finite-difference accuracy.
- **The hyperbolic alternative fails.** Its ratio to h_WP drifts from 0.81 to 1.74.
  - In the bulk, around Im τ ≈ 1.2–3, the two densities happen to be within a few per cent of each other. Only the
    tail, or the pointwise identity with the Fenchel–Nielsen Jacobian, discriminates.
  - c is also far from (π²/12)E₂*: at 0.25 + 8i they are 0.79116 and 0.72429.
- **Excluded point: τ = i itself.**
  - There both routes came out negative (−0.144), with ratio 0.999986.
  - Cause: on Re τ = 0 the Lamé ODE has real coefficients along both transfer paths, so every real c gives real traces.
    Newton started from c = 0 at τ = i ± 10⁻³i stops at the wrong root c = 0.
  - This is the degeneracy that the instrument's `track` avoids by nudging off the axis. Even `track` returns +0.00082
    on both sides of i along the axis, against the antisymmetry that S forces.
  - At 0.02 + 1.00i, where all neighbours are off the axis, the ratio is 1.000004 and h = 0.961.
  - **Lesson for any instrument use:** never difference across Re τ = 0.
- **The cusp law.**
  - δ_eff = π/ℓ − y is 0.8579, 0.8668, 0.8717, 0.8746, 0.8777 at y = 3, 4, 5, 6, 8. It approaches δ = 4 ln 2/π = 0.88254.
  - The residual fits (δ − δ_eff)·8(y + δ)² = 2.97, 3.00, 3.02, 3.03, 3.04. That is consistent with
    ℓ = (π/(y+δ))(1 + ζ(3)/(π(y+δ)³) + …), whose coefficient is 8ζ(3)/π = 3.061.
  - With that correction, h_WP/((π²/2)/(y+δ)³) − 1 is predicted as 5ζ(3)/(π(y+δ)³) = 0.0327, 0.0164, 0.0094, 0.0059,
    0.0027. Observed: 0.0319, 0.0161, 0.0093, 0.0058, 0.0027.
  - **The ζ(3) coefficient is a fit, not a source reading.**
- **The level-set law.** ∣C − (π²/6 − ℓ²/2)∣ at x = 0.25 is 3.2e-7, 6.0e-10, 1.3e-12, 3.8e-14 at y = 3, 4, 5, 6. It is
  exponentially small, O(q), as §3(b) says.
- **Tails,** with the ζ(3) correction: 3/(Y+δ)² · (1 + 2ζ(3)/(π(Y+δ)³)) = 0.20162 and 0.12667 at Y = 3 and 4, against
  the exact 0.20157 and 0.12666.

## 6. Q4 — which flows preserve which measure

- **Fenchel–Nielsen twist (and earthquake) flow: preserves ω_WP.**
  - BMW §1.5 (read): ∂/∂τ_α is the symplectic gradient of ½ℓ_α, that is ½dℓ_α = ω_WP(·, ∂/∂τ_α), equivalently
    grad ℓ_α = −2J∂/∂τ_α. They attribute this to Wolpert. So the twist flow is Hamiltonian and preserves ω_WP.
  - Wright's survey of the earthquake flow (arXiv:1810.07571, §6 read):
    - Theorem 6.1 states that earthquakes preserve the WP measure;
    - μ_Th × μ_WP is invariant on ML × T;
    - Theorem 6.3 (Bonahon–Sözen) gives F_λ*(μ_Th) = μ_WP.
  - Mirzakhani's earthquake flow on P¹M is measurably conjugate to the Teichmüller horocycle flow and is ergodic for
    ν = (Thurston cone measure) × WP (Fu §1–2, read).
  - **Projected to M(1,1),** ν is B(X) dμ_WP with B(X) = μ_Th{λ : ℓ_X(λ) ≤ 1}. This is not WP itself.
    B ≍ 1/(ε log(1/ε)) at systole ε, by Fu's Claim (read), so ν({ℓ_sys < ε}) = O(ε/log(1/ε)).
  - Mirzakhani's IMRN 2008 paper itself: **not read.**
- **Teichmüller geodesic and horocycle flows: preserve Masur–Veech, which for (1,1) is Haar.**
  - Teichmüller metric on T(1,1) = H: "|dz|/(2y)" (McMullen §1, read), i.e. curvature −4.
  - Forni–Matheus (arXiv:1311.2758, §1.4 and footnote 5, read) identify the unit bundle with SL(2,ℝ)/SL(2,ℤ). They note
    that the Masur–Veech measure there comes from Haar measure, and give the area of the modular domain as π/12 in the
    curvature −4 normalisation.
  - The Teichmüller flow is the geodesic flow of the modular surface: unit Teichmüller speed is hyperbolic speed 2 in
    curvature −1.
  - Haar measure projects to hyperbolic area dx dy/y², with total π/3 in curvature −1.
  - **The projection statement is standard and was not read at source.**
  - **Hyperbolic area is the measure native to the Teichmüller structure.**
- **WP geodesic flow on M(1,1): ergodic, with invariant measure the WP Liouville measure.**
  - BMW Theorem 1 (read) assumes 3g + n ≥ 4, which includes (1,1). The flow on M¹(S) is ergodic, in fact Bernoulli, for
    WP volume, with finite positive entropy.
  - Pollicott–Weiss–Wolpert: transitivity and dense periodic orbits for (1,1). **Cited by BMW; not read.**
  - Burns–Masur–Matheus–Wilkinson, via Matheus's notes §1.2 (read): mixing is rapid, super-polynomial, for
    3g − 3 + n = 1. **The original was not read.**
  - The Liouville measure projects to normalised WP area on M(1,1), because each fibre is a circle. This is standard.
- **The WP metric itself** (BMW §0.1, Matheus Ex. 2.12, McMullen §1, all read):
  - it is incomplete: the distance to the cusp is about 2^(1/2)π (Im τ)^(−1/2) in Wolpert's normalisation;
  - its curvature tends to −∞ at the cusp (K ∼ −3/(2ℓ) per BMW);
  - its cusp is modelled by the surface of revolution of y = x³.

## 7. Unverified, flagged

- **The torus relation ∂C/∂τ̄ = i h_WP.**
  - It is derived here from McMullen's Theorem 1.5. No source states it for the ℘ reference; Fırat states it as unproved.
  - §5 is the only direct check, and it is unsealed.
  - Park–Takhtajan–Teo's Takhtajan–Zograf term shows that the choice of reference can matter at punctures.
- **δ = 4 ln 2/π.**
  - It is my derivation from the λ-function cusp normalisation, matched to Fırat's s₁(0) = 16 ln 2.
  - Wolpert's plumbing normalisation for M(1,1) was not read at source.
  - The ξ⁴ term of Fırat's eq. (3.21) was garbled in extraction.
  - The coefficient ζ(3)/π in ℓ = (π/(y+δ))(1 + ζ(3)/(π(y+δ)³)) is a fit to §5 (k → 3.04 against 8ζ(3)/π = 3.061),
    not a reading.
- **The instrument is degenerate on Re τ = 0.** §5's τ = i row is excluded. Any instrument-based WP census must not
  difference across the axis.
- **The twist formula, the collar constant, and the Haar-to-area projection.** Standard, not read.
- **Not read:** Masur 1976; Wolpert 1982, 1983 (Annals and CMH) and 1985 (AJM); Yamada; Wolf–Wolpert; Zograf–Takhtajan
  1987 (both originals); Takhtajan–Teo 2003 (downloaded, not read); Keen–Rauch–Vasquez; Mirzakhani 2007 and 2008;
  Pollicott–Weiss–Wolpert; Hadasz–Jaskólski–Piątek.

## 8. Sources (read-depth)

- **Section-level reading:**
  - Wolpert, arXiv:math/0502528 (Surveys in Diff. Geom. VIII, 2003): Theorem 2, Corollary 4, Prop. 9's proof.
  - Wolpert, arXiv:0801.0175 (2008 survey): §2, the table, §5.
  - McMullen, arXiv:math/0010022 (Annals 151, 2000): §1, §2, §7 opening.
  - Takhtajan–Zograf, arXiv:math/0112170: §1 and footnotes.
  - Park–Takhtajan–Teo, arXiv:1508.02102: abstract, §2.2, Theorems 1–4.
  - Fırat, arXiv:2306.08599 ("Hyperbolic string tadpole", 2023): §2.2, §3.2, §3.3.
  - Burns–Masur–Wilkinson, arXiv:1004.5343 (Annals 2012): introduction, §0.1, §1.4–1.5.
  - Wright, arXiv:1905.01753 (tour): §2.8, §3. Wright, arXiv:1810.07571 (earthquake flow): §6.
  - Fu, arXiv:1506.04534: §1–3.
  - Gadre, arXiv:2011.12034 (Math. Z. 2023): §2.1.
  - Forni–Matheus, arXiv:1311.2758: §1.4 and §2.
  - Matheus, arXiv:1601.00690: §1.2, Ex. 2.12.
- **Abstract and introduction only:** Menotti, arXiv:1207.6884 (JHEP 2012).
- **Bibliographic record only:** Keen–Rauch–Vasquez 1979; Masur 1976; Wolpert CMH 1983.
