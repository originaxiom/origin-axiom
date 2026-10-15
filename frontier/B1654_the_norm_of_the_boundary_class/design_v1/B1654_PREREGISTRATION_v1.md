# B1654 — THE NORM OF THE BOUNDARY CLASS: preregistration

cc (main), 2026-10-15. **No data.** 0 of 19. The first arc of C, at the owner's "B then C" (P-150), after B1653.
POINT_REGISTER P-151; it bears on P-129's second half (what lifts R) and on P-146 (T-NORM).

## 0. Seen first

`VERDICT topic-sweep /tame higgs|parabolic higgs|szeg|simple pole|higgs profile|meromorphic higgs|logarithmic higgs|typed portal|density.type|regular part|G_?0\b|profile of the higgs|higgs.s profile/`:
7 of 1425 arcs on main match (NEGATIVE 2, PROVED 5). The nearest are B1642, B1650, B1651 and B1653.
`VERDICT topic-sweep /boundary class|Szeg[oő].{0,20}norm|norm of the (Higgs|boundary)|framed (datum|data|class)|end datum|one normali[sz]ation/`:
9 of 1425 arcs on main match. B1651's framed datum is the nearest; none normalises the boundary class.

**Read before the seal:**
- the SM seat's C0 (couplings as overlaps; point 2: "a cubic coupling of two holomorphic modes needs a Higgs of type
  (0, 1)"; point 3: "no normalizable massless Higgs carries a parity", the one class per channel a boundary class at the
  puncture; fork (a): "one normalisation serves all three");
- its §107 (the flat class's overlap diverges logarithmically) and §110;
- W61 (its two typings), W72 and W73;
- the web seat's T-NORM (the zero modes' physical L² metric "with a cut", untested), step 3a ("what P-128 needs is a lift
  that stays small") and its audit of its negatives;
- B1642–B1653, and B1651's second addendum (the Szegő form v_r = R_r S_r; the framed class f(0)).

**Literature:** the Szegő kernel of an even spin structure; S_r² = ℘ − e_r (Whittaker–Watson §21–22); Jacobi's
θ₃⁴ = θ₂⁴ + θ₄⁴; Kaluza–Klein normalisation of a zero mode; the regularised norm of a non-L² harmonic form.

## 0b. Disclosed

**Main's exploration before the seal** (`audit/drafts/c1/`, kept beside the seal as `verification/before_the_seal/`):
- **`szego_tame_check.py`.** P-151's first candidate is degenerate:
  - read as a (0, 1) Higgs, Res₀ S_r² = 0 to 10⁻³⁰;
  - read as a density, ∫|S_r|² grows as exactly 2π·log(1/ε).
- **`two_defects.py`, `two_defects_numeric.py`.** det Y(a; u) = (a·a)(u·u)(a·u). B1644 had this with u = R, so it is
  not new. The two light masses go as the two isotropy defects.
- **`end_data_defect.py`, `end_data_scan.py`.** The values this arc's cells read were seen:
  - c_r at ω, i, 0.13+1.07i, 0.3+1.6i, 2.2i and 3.0i;
  - D/|R|² there: 0 at ω, 1.09 at i, 0.996, 0.41, 0.128 and 0.0155;
  - D/(Im τ·|q|·|R|²) = 25 to 68 for Im τ = 1 to 4, and |D| ≈ 2.9|τ − ω|·|R|² near ω;
  - a coarse grid of the fundamental domain to Im τ = 2 (11 × 10 points), whose smallest |D|/|R|² sat at the grid
    points next to the two corners; the next smallest was 0.16 at Im τ = 2.
  - A first version mis-indexed the Laurent correction (a₂ for s₁). It was caught by its own split-radius test and fixed
    before any reading.
- **`route_b.py`.** Route B agreed with route A to 5 × 10⁻¹² – 1.2 × 10⁻¹⁰ at ω, i and 0.13+1.07i (n = 40).
- **A smoke test of the sealed instrument's functions** (route A at two τ; route B at n = 8), not of its cells.

**The thresholds below were set from these.** Not computed before the seal: the finer grid (21 × 20), the cusp at
Im τ = 5, N1's control, N4's controls and all of N6.

## 1. The setting, and four premises

- E is the fibre torus at τ, with the puncture at 0. The channels are the even spin structures r = 2, 3, 4, whose Szegő
  kernels S_r(z) = θ_r(z)θ₁′(0)/(θ_r(0)θ₁(z)) behave like 1/z at 0, are odd, and satisfy S_r² = ℘ − e_r.
- The residue triplet is B1644's: R_i = −θ₂²/(2πη³), R_j = −θ₄²/(2πη³), R_k = iθ₃²/(2πη³). Channel by channel,
  R_i ↔ S₂, R_j ↔ S₄ and R_k ↔ S₃, and the pairing triplet is v_r = R_r S_r (B1651's second addendum). R·R = 0 by
  Jacobi.
- Y(a; u) = a uᵀ + u aᵀ − (a·u)𝟙 for a Higgs in M with direction a (B1645), with u = R at the puncture.

**The premises, stated and not tested:**
- **P1, the typing.** The Higgs couples as a (0, 1)-form (C0 point 2: the holomorphic cubic).
- **P2, the mode.** In each channel the massless Higgs is the boundary class (C0 point 3). Its bulk profile is the
  harmonic, least singular one, φ_r = S̄_r dz̄.
- **P3, the end.** One cutoff for the three channels, a curve asymptotically the circle |z| = ε in a local coordinate.
  The end is the puncture's, not a channel's.
- **P4 against P4′, the vacuum.** P4: the three channels' canonically normalised amplitudes are equal. P4′: their framed
  data are equal, C0's "one normalisation serves all three". The arc computes both.

**What follows by hand:**
1. ‖φ_r‖²_ε = ∫_{E∖D_ε} |S_r|² = 2π·log(1/ε) + c_r(τ) + o(1). The coefficient 2π is the residue squared times 2π, the
   same for all r.
2. The coupling of channel r's Higgs to v_r is −2iR_r‖S_r‖²_ε. Per unit norm it is ∝ R_r‖S_r‖_ε. So under P4,
   u_r = √(2πL + c_r)·R_r with L = log(1/ε). Under P4′, u = R.
3. u·u = 2πL(R·R) + D = D, with **D(τ) = Σ_r c_r(τ)R_r²**. The universal log cancels because R·R = 0.
4. D does not depend on the cutoff's shape. A curve asymptotically the circle shifts c_r by o(1).
5. D does not depend on the local coordinate's scale. z′ = λz shifts every c_r by the same 2π·log|λ|, and R·R = 0.
6. **D(ω) = 0.** The order-6 automorphism of E_ω permutes the three even spin structures cyclically and fixes the disc
   about 0, so c₂ = c₃ = c₄ there. Then D = c·(R·R) = 0.
7. **At τ = i**, z ↦ iz swaps S₂ and S₄ and fixes S₃, so c₂ = c₄. Then D = (c₃ − c₂)R_k².
8. **At the cusp** (τ = iy, y → ∞):
   - S₂ → π·cot(πz), so c₂ = π²y + c₂⁰ + O(q);
   - S₃ and S₄ → π/sin(πz), so c₃ and c₄ tend to a common constant, with c₄ − c₃ = O(q);
   - R_i²/|R|² = 8q(1 + O(q)), and R_j² + R_k² = −R_i².

   Hence **D/(q|R|²) = 8π²y + K + O(q)**, with q = e^{−πy} and K a constant.
9. **The masses.** det Y(a; u) = (a·a)(u·u)(a·u) = (a·a)·D·(a·u).
   - As L → ∞, s₁ and s₂ ≈ √(2πL)·σ₁ and √(2πL)·σ₂, where σ₁ ≥ σ₂ are Y(a; R)'s nonzero singular values.
   - So **L·m₁/m₃ → |a·a|·|D|·|a·R| / (2π·σ₁²σ₂)**.
   - The light right singular vector tends to R, the null vector of Y(a; R), and its angle from R is O(1/L), the same
     order as m₁/m₃. So the lift is diagonal along R, not the Gatto–Sartori–Tonin texture: angle/√(m₁/m₂) ∝ L^{−½}.
10. **By hand, no cell: T-NORM for the matter.** The generations ψ_p = C_pF are sections of the different flat bundles
    V ⊗ L_{χ_p}, so no invariant pairing joins two of them. Their L² metric is ‖F‖²·I₃ (C_p unitary), the
    Hodge–Riemann form up to scale.

## 2. The instrument

`verification/the_norm_of_the_boundary_class.py`, one run. It writes `the_norm_of_the_boundary_class.json` and
`_run.txt`.
- **Route A.** Polar quadrature about 0 over the period parallelogram P, with the radial variable s = log r, cut at ε;
  numpy theta series.
- **Route B.** Product Gauss–Legendre over P in (x, t), z = x + tτ, with 1/|z|² and 2Re(s₁z/z̄) subtracted and restored
  analytically; mpmath jtheta.
- The two routes share no quadrature and no theta code.
- The named points are ω, i, t1 = 0.13+1.07i, t2 = 0.3+1.6i, t3 = 2.2i and t4 = 3.0i.

## 3. The cells

| cell | prediction | prior |
|---|---|---|
| **N0**, plumbing (the run is void if any fails) | the numpy series against jtheta < 10⁻¹²; S_r² − S_s² constant in z < 10⁻²⁵ (it is e_s − e_r); θ₁′(0) = 2πη³ < 10⁻²⁵; R·R/Σ\|R_r\|² < 10⁻²⁵ (40 digits) and < 10⁻¹⁴ (numpy) | 99% |
| **N1**, the universal log | at ω, i, t1 and t3, for each r: route A's ∫_{P∖D_ε}\|S_r\|² − 2π·log(1/ε) agrees across ε = 10⁻³, 10⁻⁴, 10⁻⁵ to < 10⁻⁹. **Control:** for 2S_r (residue 2) the same quantity drifts by 6π·log 10 per decade, to 10⁻⁶ relative | 99% |
| **N2**, two routes | c_r by route A (ε = 10⁻⁵) and route B (n = 40) agree to < 10⁻⁸ at all six named points | 95% |
| **N3**, symmetry | at ω, c₂ = c₃ = c₄ (spread < 10⁻¹⁰); at i, c₂ = c₄ (< 10⁻¹⁰) with \|c₃ − c₂\| > 1. **Control:** at t1, every pairwise difference > 0.1 | 99% |
| **N4**, the cancellation made visible | u·u is independent of L ∈ {5, 20, 80} and equals D, both < 10⁻¹² relative to 2πL\|R\|². **Controls that show what does the work:** (a) channel-dependent cutoffs ε_r = ελ_r, λ = (1, 2, 4), shift u·u by −2πΣ log(λ_r)R_r², which is non-zero (> 10⁻³\|R\|²), to 10⁻⁹ relative; (b) the triplet R′ = (θ₂², iθ₄², θ₃²)/(2πη³), with R′·R′ ≠ 0, gives a u′·u′ that grows in L with slope 2π(R′·R′), to 10⁻⁹ relative | 99% |
| **N5**, D's zero and its cusp | (a) \|D(ω)\|/\|R\|² < 10⁻¹⁰; (b) \|D\|/\|R\|² > 0.1 at i, t1 and t2; (c) on a 21 × 20 grid of the fundamental domain to Im τ = 2, \|D\|/\|R\|² > 0.05 at every point farther than 0.1 from both corners; (d) the cusp slope [D/(q\|R\|²)](5i) − [D/(q\|R\|²)](4i) equals 8π² within 0.5% | 90% |
| **N6**, the masses | for three seeded random directions a and one near the cone (about R̄), at i and t1: (a) at ω, m₁/m₃ < 10⁻¹² for every L ∈ {40, 160, 640, 2560}; (b) under P4′ (u = R), m₁/m₃ < 10⁻¹² at ω, i and t1; (c) L·m₁/m₃ at L = 2560 equals the limit of §1.9 within 2%; (d) the light right singular vector's angle from R scales as 1/L (angle·L at 2560 over at 640 is within 3% of 1), and angle/√(m₁/m₂) halves from L = 640 to 2560 (0.5 ± 0.05). These L test an asymptotic law; they are not physical values of the end datum. The near-cone direction amplifies the 1/L corrections by 1/(σ₂/σ₁) ≈ 10, which is why the asymptotic checks sit at large L | 85% |

**What could fail, and what each failure would say:**
- **N1's control** fails if the subtraction is not tied to the residue.
- **N3's control** fails if the symmetry argument is applied where it does not hold.
- **N5(c)** fails if D has another zero in the domain. That would be a second τ where the canonical end condition keeps
  the first generation massless.
- **N5(d)** fails if the cusp derivation (§1.8) is wrong.
- **N6(c)** fails if the limit formula is wrong. **N6(d)** fails if the lift is not diagonal along R; if the angle went
  as L^{−½}, the texture would be Gatto–Sartori–Tonin's.

N4 is a demonstration: its main lines are identities, and its controls show the cancellation is neither automatic nor
cutoff-blind. It is graded as such.

## 4. What it will not show

- which end condition is physical (P4 against P4′): the parent's clauses 4 and 6;
- the end datum L itself; τ; the Higgs's direction a;
- any mass or mixing value;
- anything with a hypercharge line, which is the next arc's (the twisted channels, per sector);
- a comparison with data.

Context, not a test: nature's θ_C ≈ √(m_d/m_s) is the Gatto–Sartori–Tonin texture. A lift diagonal along R is not it.

0 of 19.
