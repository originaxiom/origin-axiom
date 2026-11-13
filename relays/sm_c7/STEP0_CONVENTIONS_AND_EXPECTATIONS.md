# SM-C7 step 0: the conventions, sealed before any run on B1737's population, and the expectations

*Card SM-C7 (`relays/cards/SM_C7_the-slope-and-the-channel-norm-one-l-function.md`), steps 0 to 2 approved by main
(docs/seats/sm.md, M15, M17). The owner's word put SM-C7 ahead of SM-C6. This page is committed and pushed before the
population is computed. Data-free: no measured value is read, B1656 is not read, and steps 3 and 4 are not run.*

## What was done before this seal, and on what

- **B1737's population was dumped** from main's own code, unchanged (`relays/sm_c7/dump_population.py`, run in a
  worktree of main at f503b1f38). It holds 16 levels and 601 characters, each with its exact slope s(χ) and B1737's
  Z(0, χ). That reproduces B1737's computation; it computes nothing of this card.
- **Every convention was fixed on three calibration matrices outside the population:**
  - [[3, 1], [2, 1]] (trace 4); [[−3, −1], [−2, −1]] (trace −4); [[7, 4], [5, 3]] (trace 10);
  - none of these traces occurs among the population's 16 levels;
  - the record is `relays/sm_c7/calibration/calibration_run.txt`, from the scripts beside it.
- Nothing of the population was computed with the instruments below before this page was pushed.

## The conventions (step 0)

- **The objects.**
  - M = [[a, b], [c, d]] acts on the fibre's H₁ by v ↦ Mv.
  - A character is χ(v) = e((i v₀ + j v₁)/N), fixed by M: (i, j) M ≡ (i, j) mod N.
  - Its point is c = (i, j)/N, and its dual point is Jc = (−c₂, c₁).
- **The modulus and the geodesic.**
  - The Eisenstein lattice point (m, n) is v itself.
  - The modulus z is acted on by γ = Mᵀ, z ↦ (az + c)/(bz + d).
  - The thread's geodesic joins γ's fixed points β > β′, with z(t) = (β·ie^t + β′)/(ie^t + 1) and ds = dt.
  - One period is t ∈ [−ℓ/2, ℓ/2], ℓ = 2 log|λ|, and γ moves z(t) to z(t ± ℓ).
- **The form:** Q(v) = (v₀β + v₁)(v₀β′ + v₁)/(β − β′) = (b v₁² + (a − d) v₀v₁ − c v₀²)/√D, up to sign, D = tr² − 4.
- **The zeta functions:**
  - Z_tot(s, χ) = Σ over v ∈ (ℤ² − 0)/⟨M⟩ of χ(v)|Q(v)|^{−s}, split into
    - Z_same, over the cone where Q > 0;
    - Z_opp, where Q < 0.
  - B1737's Z(0, χ) is ½·Z_same(0, χ) (B1737's "per generator").
  - L_odd(1, χ) = Z_same(1, χ) − Z_opp(1, χ).
  - Cone sums use Shintani's cone decomposition, with twisted Euler–Maclaurin tails (Abel summation).
- **The Eisenstein series:**
  - **weight 0, v-twisted:** E_c(z, s) = Σ′ e(c·(m, n)) yˢ |mz + n|^{−2s};
  - **the Kronecker function:** K_c(z) = E_c(z, 1) = −2π log|g_Jc(z)|. Here g_a is the Siegel function
    q^{B₂(a₁)/2}(1 − qᵃ¹e(a₂)) Π (1 − qⁿ⁺ᵃ¹e(a₂))(1 − qⁿ⁻ᵃ¹e(−a₂)) with a = Jc. Derived on this page's run, and checked
    to 10⁻¹⁵;
  - **weight 2, v-twisted:** G_c(z) = Σ′ e(c·(m, n))(mz + n)^{−2}. It is holomorphic for c ≠ 0, and equals
    −2πi ∂_z log g_Jc, checked to 10⁻⁹ by finite differences;
  - **weight 2, u-shifted, Hecke's limit:** G^(u)*(z) = Σ over (m, n) ∈ u + ℤ² of (mz + n)^{−2}, minus π/y.
- **Hecke's formula, in these conventions:**
  - ∫ over one period of E_c(z, s) ds = H(s)·Z_tot(s, χ), with H(s) = 2^{−s} √π Γ(s/2)/Γ((s + 1)/2), so H(1) = π/2.
  - Calibration: to 10⁻¹⁴ at s = 1, 2 and 3, on 12 characters of the two signs of trace.
- **The two coefficients, as calibration fixed them** (24 calibration characters):
  - **The value coefficient (step 1):**
    - Z(0, χ_c) = (1/4π²)·∫ from z₀ to γz₀, along the geodesic, of G^(Jc)*(z) dz;
    - to 10⁻¹⁴, independent of z₀;
    - of the declared family (v-twisted at c or Jc, u-shifted at c or Jc), only u-shifted at Jc held. The other three
      gave ratios that are not constant.
  - **The Kronecker coefficient (step 2):**
    - Z_tot(1, χ) = (2/π)·∫ over one period of K_c ds = −4·∫ log|g_Jc| ds;
    - with its odd partner L_odd(1, χ) = ∫ from z₀ to γz₀ of G_c(z) dz = −2πi·Δ_γ log g_Jc.
    - So at s = 1 the one function g_Jc on the thread's geodesic gives the even part (its modulus, integrated) and
      the odd part (its argument's winding).
  - **At s → 0:**
    - Z_tot(0, χ) = 0 and Z_tot′(0, χ) = −ℓ/2 for every character. Calibration: 10⁻⁷ to 10⁻⁹ by a contour derivative.
    - So the derivative at 0 of the v-twisted total carries no character information. The card's "next coefficient at
      s = 0" is therefore taken at s = 1, where the Kronecker function lives (equivalent through the functional
      equation). This is said here, before the run.

## The expectations (written before the run)

Step 1, on all 601 characters:
- |s(χ) + ½#(−I) − P_u(Jc)/4π²| ≤ 10⁻⁹. P_u(Jc) is the period above, with 48 nodes; 96 nodes agree within 10⁻¹⁰.

Step 2, on all 601 characters (relative where the value exceeds 1):
- **(a) Hecke at s = 2:** ≤ 10⁻⁹.
- **(b) Hecke at s = 1, the Kronecker coefficient:** ≤ 10⁻⁹.
- **(c) the odd part at s = 1:** ∫ G_c dz = L_odd(1, χ), ≤ 10⁻⁹. Also L_odd(1, χ)/4π² is rational, within 10⁻⁹ of a
  fraction with denominator ≤ 24N².
- **(d) s → 0:** |Z_tot(0, χ)| ≤ 10⁻⁹ and |Z_tot′(0, χ) + ℓ/2| ≤ 10⁻⁶ (16-point contour of radius 0.3).

If step 1 or step 2(b) fails beyond these bounds on any level, the page reports outcome C for that level, in these
sealed conventions, and changes no convention after the run.

## The planted controls, which must fail

- **P1, a wrong character:**
  - c is replaced by c′ = c + (1/N, 0), or the next shift not fixed by M.
  - Step 1 against the true slope must miss by more than 10⁻⁶ on at least 99% of characters.
- **P2, a wrong geodesic:**
  - The periods are taken along the geodesic of M′ = [[t − 1, 1], [t − 2, 1]], which has the same trace t, with the
    same c.
  - Step 1 and step 2(b) must miss by more than 10⁻⁶ on at least 99% of characters.
- **P3, the orientation reversed:**
  - The period runs from γz₀ to z₀.
  - Step 1 must miss on every character whose value exceeds 10⁻⁶; the sign flips, as Ψ does under undoing.
- **P4, a normalisation error:**
  - A factor 2 is put on G^(Jc)* in step 1 and on E_c in step 2(b).
  - Both must miss on every character whose value exceeds 10⁻⁶.

## What is not done

Steps 3 and 4 (B1656's c_s along the geodesic and at its apex; the averaged norm per thread and line) are held by
main for a sealed card under the owner's hold. Nothing of them is run, and B1656 is not opened.
