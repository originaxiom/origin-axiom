# B1654 — THE NORM OF THE BOUNDARY CLASS: preregistration

cc (main), 2026-10-15. **No data.** 0 of 19. The first arc of C, at the owner's "B then C" (P-150), after B1653.
POINT_REGISTER P-151. It bears on P-129's second half (what lifts R) and on P-146 (T-NORM).

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
- B1642–B1653, and B1651's second addendum (the Szegő form v_r = R_r S_r; the framed class f(0); R·R = 0 and
  Σ R_r²e_r = 0 as the two facts behind isotropy).

**Literature:** the Szegő kernel of an even spin structure; S_r² = ℘ − e_r (Whittaker–Watson §21–22); Jacobi's
θ₃⁴ = θ₂⁴ + θ₄⁴; Kaluza–Klein normalisation of a zero mode; the regularised norm of a non-L² harmonic form.

## 0b. Disclosed

**Main's exploration before the seal** (`verification/before_the_seal/`, scripts with their outputs):
- **`szego_tame_check`.** P-151's first candidate is degenerate:
  - read as a (0, 1) Higgs, Res₀ S_r² = 0 to 10⁻³⁰;
  - read as a density, ∫|S_r|² grows as exactly 2π·log(1/ε).
- **`two_defects`, `two_defects_numeric`.** det Y(a; u) = (a·a)(u·u)(a·u). B1644 had it with u = R, so it is not new.
  The light masses go as the two isotropy defects. The script's second line compares a wrong guess, and its non-zero
  difference is that guess's error. The identity itself is the first line.
- **`end_data_defect`, `end_data_scan`.** The values the cells read were seen:
  - c_r at ω, i, t1 = 0.13+1.07i, t2 = 0.3+1.6i, t3 = 2.2i and t4 = 3.0i;
  - D/|R|² there: 0 at ω, then 1.09, 0.996, 0.41, 0.128 and 0.0155;
  - the trend toward the cusp, and the linear vanishing near ω;
  - a coarse grid of the fundamental domain to Im τ = 2.
  - The first version mis-indexed its Laurent correction. Its own split-radius test caught that, and it was fixed
    before any reading. The `end_data_defect` output keeps the first version.
- **`route_b`.** Route B agreed with route A to 3.7 × 10⁻¹² – 1.2 × 10⁻¹⁰ at ω, i and t1 (n = 40).
- **Smoke and glue tests** of the instrument: its functions at two τ, and the whole file run once in a scratch copy with
  the quadratures stubbed by fake numbers, to exercise the glue. Neither computed a sealed value.

**Two passes of read-only reviewing agents** (`verification/before_the_seal/review/` and `review2/`, with READMEs). The
first read the draft kept as `design_v1/`. **The first pass** found no decisive error in §1's mathematics. It found:
- **MAJOR.** N4's control (a), with cutoffs λ = (1, 2, 4), vanishes identically at τ = i, where θ₂ = θ₄ makes the shift
  ∝ R_i² − R_j² = 0. So N4 would have failed on a design error. λ = (1, 2, 1) replaces it.
- **MINOR.**
  - Output is now written after every cell, the angle is an atan2, and divisions are guarded: a near-cone draw could
    have crashed N6.
  - The theta series' cutoff falls from 40 to 24 terms, because 40 overflows above Im τ ≈ 5.7.
  - N5(c) cannot certify "no other zero", only "none within about 0.02 of a node". It is reworded, and given a positive
    control at the corners.
  - N6's "amplified about 10×" was wrong for the seeded draws: the realised σ₂/σ₁ are 0.161, 0.019 and 0.074.
  - D has a cutoff-free form (N2b, below).
- **TEXT.**
  - The conventions, the factorised vacuum behind P4, a third end condition P4″, P3's reason, and the modular
    invariance of |D|/|R|² are now stated.
  - The T-NORM paragraph's wording is corrected (now §1.11).
  - The redundant cells are named.
  - The cusp law's constant has a closed form, K = 8π(1 − 4 ln 2), identified by the reviewer from closed-form limits
    checked at heights other than the sealed ones. Main checked it against its own exploration values
    (c₂(4i) − 4π² = −11.548 = −2π·ln 2π to 10⁻³; c₃(4i) = −2.83747, against −2π·ln(π/2) − 8πq = −2.83738 − 0.00009).

**The second pass** checked the revision: no decisive or major finding, and every fix verified. It found:
- Three cells' flags would have been written as the strings "True"/"False". They are now booleans.
- Outputs went to the working directory. They are now written beside the script.
- The first pass's scripts need the v1 draft, which is now kept as `design_v1/`.
- Text: this section's blindness was overstated, a margin was overstated (4×, not 10×), one constant was misprinted,
  and four wordings were loose. All are corrected below. N4(a)'s sign is now tested (the signed ratio, not the moduli).

**What was seen before the seal, cell by cell:**
- **N0, N3, N4, N5(a, b), N6.** The reviewers replicated them with the instrument's own text and route-A values. All held.
  N6's margins are at least 4× (angle·L at i, near the cone, 1.0064 against 1 ± 0.03).
- **N2b.** The first pass computed the direct D at i and t1 (with nr = 64, against the cutoff sum); the second pass
  computed it at 15 other τ.
- **N5(c).** The first pass scanned an offset grid (to Im τ = 2.3) and printed its smallest far value and the
  near-corner slopes; the second pass computed the four near-corner nodes (2.70 and 2.93) and one far node,
  (0, 1.7), at 0.41. The sealed grid's top row (Im τ = 2) was seen.
- **N5(d).** `end_data_scan_output.txt` already shows D/|R|² at 4i (271.27·q·|R|²), and the second pass computed route
  A's c_r at 4i (27.930695, −2.837465, −2.837290). Nothing at 5i was computed by anyone.
- **N1, N2.** Only at τ other than the named points, before the seal.

**Unseen at the sealed nodes:**
- N1 and N2 at the named points;
- N2b at ω, t2, t3 and t4;
- N5(c)'s grid apart from its top row and the five nodes above;
- N5(d) at 5i, and the deviation from K there.

The thresholds below were set with all of the above in view.

## 1. The setting, the conventions, and the premises

- **Conventions.**
  - θ_r(z) ≡ θ_r(πz ∣ q = e^{iπτ}), and θ₁′(0) = d/dz θ₁(πz)∣₀ = 2πη³, with η = q^{1/12}∏(1 − q^{2n}).
  - E is the fibre torus at τ, with the puncture at 0, and P = {x + tτ : x, t ∈ [−½, ½]}.
  - The channels are the even spin structures r = 2, 3, 4. Their Szegő kernels S_r(z) = θ_r(z)θ₁′(0)/(θ_r(0)θ₁(z))
    have residue exactly 1 at 0, are odd, and satisfy S_r² = ℘ − e_r.
- **The residue triplet is B1644's:** R_i = −θ₂²/(2πη³), R_j = −θ₄²/(2πη³), R_k = iθ₃²/(2πη³).
  - Channel by channel, R_i ↔ S₂, R_j ↔ S₄ and R_k ↔ S₃.
  - R_r S_r(z) is B1651's pairing c_r θ_r(0)θ_r(z)/θ₁(z), with c = (−1, −1, i) for i, j, k (pinned in N0).
  - R·R = 0 by Jacobi, and Σ R_r²e_r = 0 is B1650's O6.
- **The Yukawa.** Y(a; u) = a uᵀ + u aᵀ − (a·u)𝟙 for a Higgs in M with direction a (B1645), with u = R at the puncture.
  Every entry of B1644's table carries a single channel, so a channel-wise weighting R_t → N_t R_t gives exactly
  Y(a; N∘R). That holds when the Higgs's vacuum factorises, Φ^s_t = a_s·h·n_t: one direction in M, times one weight per
  channel.

**The premises, stated and not tested:**
- **P1, the typing.** The Higgs couples as a (0, 1)-form (C0 point 2: the holomorphic cubic).
- **P2, the mode.** In each channel the massless Higgs is the boundary class (C0 point 3). Its bulk profile is the
  harmonic, least singular one, φ_r = S̄_r dz̄.
- **P3, the end.** One cutoff for the three channels, a curve asymptotically the circle |z| = ε in a local coordinate.
  The reason: every χ_r's holonomy around the puncture is trivial (the puncture loop is a commutator), so the three
  channels look identical at the end, and c_r's channel dependence is entirely global.
- **P4 against P4′ and P4″, the vacuum (factorised, as above).**
  - P4: the three channels' canonically normalised amplitudes are equal, as complex numbers.
  - P4′: their framed data are equal, which is C0's "one normalisation serves all three".
  - P4″: their unnormalised amplitudes are equal.
  - The arc computes P4 and P4′. Under P4″, u_r ∝ (2πL + c_r)R_r and u·u = 4πL·D + Σ c_r²R_r², which grows with L
    wherever D ≠ 0 (at ω, where the c_r are equal, u ∝ R).

**What follows by hand:**
1. ‖φ_r‖²_ε = ∫_{E∖D_ε} |S_r|² = 2π·log(1/ε) + c_r(τ) + o(1). The coefficient is 2π times the residue squared, the
   same for all r.
2. Channel r's Higgs couples to v_r by −2iR_r‖S_r‖²_ε, which per unit norm is ∝ R_r‖S_r‖_ε. So under P4,
   u_r = √(2πL + c_r)·R_r with L = log(1/ε). Under P4′, u = R.
3. u·u = 2πL(R·R) + D = D, where **D(τ) = Σ_r c_r(τ)R_r²**.
4. **D needs no cutoff: D = ∫_P Σ_r R_r²|S_r(z)|² dA.**
   - Near 0, with s₁^{(r)} = −e_r/2 and R_r² complex:
     Σ_r R_r²|S_r|² = (R·R)/|z|² − ½(Σ_r R_r²e_r) z/z̄ − ½(Σ_r R_r²ē_r) z̄/z + O(|z|²).
   - The first term vanishes by Jacobi and the second by O6. The third is bounded and has zero average on every circle
     about 0; it vanishes too where the e_r are real, as on τ = iy. Main checked this before the seal:
     |Σ R_r²ē_r|/(|R|²·max|e_r|) = 0.244 at t1 and 1.0 at ω, while Σ R_r²e_r vanishes to 10⁻²⁰.
   - So the integrand is bounded, and any common shrinking cutoff, circular or not, gives D.
   - A channel-dependent cutoff does not (N4(a)).
5. D does not depend on the local coordinate's scale: z′ = λz shifts every c_r by the same 2π·log|λ|.
6. **|D|/|R|² is modular invariant.** S and T permute the channels and the c_r, and multiply the R_r² by factors of one
   modulus. The common shift 2π·log|τ| drops out because R·R = 0. (The reviewer checked this at five images of a point:
   6 × 10⁻⁸ at the most skewed.) So the fundamental domain suffices.
7. **D(ω) = 0.** ζS_r(ζz) = S_{σ(r)}(z), with ζ = ω, permutes the three even spin structures cyclically and fixes the disc
   about 0. So c₂ = c₃ = c₄ there, and D = c·(R·R) = 0.
8. **At τ = i**, z ↦ iz swaps S₂ and S₄ and fixes S₃, so c₂ = c₄ and D = (c₃ − c₂)R_k².
9. **At the cusp** (τ = iy, q = e^{−πy}):
   - S₂ → π·cot(πz) gives c₂ = π²y − 2π·ln(2π) + O(q);
   - S₃ and S₄ → π/sin(πz) give c₃, c₄ = −2π·ln(π/2) ∓ 8πq + O(q²);
   - R_i²/|R|² = 8q(1 + O(q)) and R_j² + R_k² = −R_i².

   Hence **D/(q|R|²) = 8π²y + K + O(yq), with K = 8π(1 − 4 ln 2) = −44.550**.
10. **The masses.** Write s₁ ≥ s₂ ≥ s₃ for Y(a; u)'s singular values, and m₁ for the lightest. Then
    det Y(a; u) = (a·a)·D·(a·u).
    - As L → ∞, s₁ and s₂ ≈ √(2πL)·σ₁ and √(2πL)·σ₂, where σ₁ ≥ σ₂ are Y(a; R)'s nonzero singular values.
    - So **L·s₃/s₁ → |a·a|·|D|·|a·R| / (2π·σ₁²σ₂)**.
    - The light right singular vector tends to R (Y(a; R)R = a(R·R) = 0). Its angle from R is O(1/L), the same order
      as s₃/s₁. So the lift is diagonal along R, and angle/√(s₃/s₂) ∝ L^{−½}: not the Gatto–Sartori–Tonin texture.
11. **By hand, no cell: T-NORM for the matter.**
    - The generations ψ_p = C_pF are sections of the different flat bundles V ⊗ L_{χ_p}. A cross term is a section of
      the non-trivial flat bundle L_{χ_pχ_q}, and no invariant pairing joins sections of different flat bundles. So
      there is no kinetic mixing: the discrete charge forbids it.
    - The diagonal is ‖C_pF‖² = ‖F‖², since C_p is unitary. It is finite, because |F|² ~ 1/|z|.
    - So their L² metric is ‖F‖²·I₃.
    - Only the Higgs needs a cut, because |S|² ~ 1/|z|².

## 2. The instrument

`verification/the_norm_of_the_boundary_class.py`, one run. It writes `the_norm_of_the_boundary_class.json` and
`_run.txt` after every cell.
- **Route A.** Polar quadrature about 0 over P, with the radial variable s = log r, cut at ε; numpy theta series.
- **Route B.** Product Gauss–Legendre over P in (x, t), with 1/|z|² and 2Re(s₁z/z̄) subtracted and restored
  analytically; mpmath jtheta.
- **N2b's direct D.** Polar quadrature with r from 0, and no cutoff.
- Route A and route B share no decomposition and no theta code; both use Gauss–Legendre nodes. N2b shares route A's
  theta code and differs in the radial variable and in having no cutoff. The six named points are ω, i, t1, t2, t3 and
  t4.

## 3. The cells

| cell | prediction | prior |
|---|---|---|
| **N0**, plumbing (the run is void if any fails) | the numpy series against jtheta < 10⁻¹²; S_r² − S_s² constant in z < 10⁻²⁵; θ₁′(0) = 2πη³ < 10⁻²⁵; R·R/Σ\|R_r\|² < 10⁻²⁵ (40 digits) and < 10⁻¹⁴ (numpy); **the channel assignment**: route A's R_r S_r(z) against B1651's pairing c_r θ_r(0)θ_r(z)/θ₁(z) (c = (−1, −1, i)) < 10⁻¹² relative | 99% |
| **N1**, the universal log | at ω, i, t1 and t3, for each r: route A's ∫_{P∖D_ε}\|S_r\|² − 2π·log(1/ε) agrees across ε = 10⁻³, 10⁻⁴, 10⁻⁵ to < 10⁻⁹. **Control:** for 2S_r (residue 2) it drifts by 6π·log 10 per decade, to 10⁻⁶ relative | 99% |
| **N2**, two routes | c_r by route A (ε = 10⁻⁵) and route B (n = 40) agree to < 10⁻⁸ at the six named points | 95% |
| **N2b**, D without a cutoff | ∫_P Σ_r R_r²\|S_r\|² dA agrees with Σ_r c_r R_r² to < 10⁻¹⁰ \|R\|² at the six named points | 97% |
| **N3**, symmetry | at ω, c₂ = c₃ = c₄ (spread < 10⁻¹⁰); at i, c₂ = c₄ (< 10⁻¹⁰) with \|c₃ − c₂\| > 1. **Control:** at t1, every pairwise difference > 0.1 | 99% |
| **N4**, the cancellation made visible | u·u is independent of L ∈ {5, 20, 80} and equals D, to < 10⁻¹² relative to 2πL\|R\|². **Controls:** (a) doubling channel 3's cutoff (λ = (1, 2, 1)) shifts u·u by −2π·ln2·R_k² (signed), which is non-zero (> 10⁻³\|R\|²), to 10⁻⁹ relative; (b) the triplet R′ = (θ₂², iθ₄², θ₃²)/(2πη³), with R′·R′ ≠ 0, gives a u′·u′ growing in L with slope 2π(R′·R′), to 10⁻⁹ relative | 99% (a demonstration) |
| **N5**, D's zero and its cusp | (a) \|D(ω)\|/\|R\|² < 10⁻¹⁰ (N3 restated); (b) \|D\|/\|R\|² > 0.1 at i, t1 and t2; (c) on the 21 × 20 grid of the fundamental domain to Im τ = 2: \|D\|/\|R\|² > 0.05 at every node farther than 0.1 from both corners, and **positive control**: at every node within 0.1 of a corner, \|D\|/(\|R\|²·distance) lies in [1.8, 3.4] (D vanishes linearly there), all values finite; (d) the cusp: the slope [D/(q\|R\|²)](5i) − [D/(q\|R\|²)](4i) is 8π² within 10⁻³ relative, and \|D/(q\|R\|²)(5i) − 40π² − K\| < 2 × 10⁻³, with K = 8π(1 − 4 ln 2) | 88% |
| **N6**, the masses | three seeded random directions and one near the cone (about R̄; realised σ₂/σ₁ = 0.161, 0.019, 0.074 at ω, i, t1), at i and t1: (a) at ω, s₃/s₁ < 10⁻¹² for L ∈ {40, 160, 640, 2560} (follows from N5(a)); (b) under P4′ (u = R), s₃/s₁ < 10⁻¹² at ω, i and t1 (follows from N0); (c) L·s₃/s₁ at L = 2560 equals §1.10's limit within 2%; (d) the light right singular vector's angle from R scales as 1/L (angle·L at 2560 over at 640 within 3% of 1), and angle/√(s₃/s₂) halves from L = 640 to 2560 (0.5 ± 0.05). These L test an asymptotic law; they are not physical values of the end datum | 90% |

**What could fail, and what a failure would say:**
- **N0's channel assignment** fails if the code pairs a channel with the wrong theta.
- **N1's control** fails if the subtraction is not tied to the residue.
- **N2** fails if the two routes disagree, which would make the instrument suspect.
- **N2b** fails if the direct integral and the cutoff sum disagree. That would put the instrument or §1.4's identity in
  question. It does not test O6: both O(1) terms near 0 are bounded with zero circle mean, so only R·R = 0 matters for
  convergence and cutoff independence.
- **N3's control** fails if the symmetry argument is used where it does not hold.
- **N5(c)** fails if D has another zero within about 0.02 of a grid node. That would be a second τ in the domain where the
  canonical end condition keeps the first generation massless. Its positive control fails if the scan does not see the
  known zero as a linear one.
- **N5(d)** fails if §1.9's limits or its constant are wrong.
- **N6(c)** fails if §1.10's limit is wrong. **N6(d)** fails if the lift is not diagonal along R; an L^{−½} angle would
  be the Gatto–Sartori–Tonin texture.
- **N4** is a demonstration: its main lines are identities, and its controls show the cancellation is neither automatic
  nor cutoff-blind. **N5(a), N6(a) and N6(b)** restate N3 and N0, and are graded as consistency checks.

## 4. What it will not show

- which end condition is physical (P4, P4′ or P4″): the parent's clauses 4 and 6;
- the end datum L; τ; the Higgs's direction a;
- whether the vacuum factorises;
- any mass or mixing value;
- anything with a hypercharge line, which is the next arc's (the twisted channels, per sector);
- a comparison with data.

Context, not a test: nature's θ_C ≈ √(m_d/m_s) is the Gatto–Sartori–Tonin texture, and a lift diagonal along R is not
it.

0 of 19.
