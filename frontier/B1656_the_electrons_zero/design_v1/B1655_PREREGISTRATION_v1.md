# B1655 — THE ELECTRON'S ZERO: preregistration

cc (main), 2026-10-15. **No data.** 0 of 19. The second arc of C (P-151), after B1654. It bears on the parent's
clause 7 (split the down quarks from the charged leptons), on P-128 and on P-129.

## 0. Seen first

`VERDICT topic-sweep /twisted (channel|szeg|norm)|electron.{0,20}(zero|massless)|lepton.{0,20}(zero|massless)|9.torsion|omega.fixed|order.3 rotation/`:
13 of 1426 arcs on main match (NEGATIVE 1, PROVED 12); 10 other lanes match. None states an electron zero. The matches are
ω-fixed or 9-torsion points in other settings (B1042, B1291, B1292, B1302, B1320, B1321, B1435, B1490, B928, B931), the chirality
bit (B1294), a harvest (B1453) and B1654. The nearest fact on record is B1653's U7 read-out, which found the leptons' triplet
isotropic on W59's lines. By the null quaternion that is R₁(leptons) = 0, seen there without the norms and without its
consequence for the mass.

**Read before the seal:**
- B1653 (the twisted pairing: P_s = N_s e^{2πiAu}θ_s(u + ū)/θ₁(u); R_s = κ c_s θ_s(ū)θ_s(δ)/θ₁′(0), c = (−i, −1, −1, i);
  the null quaternion R₁² + R·R = 0; ū = w_x + w_y and δ = w_x − w_y; the hypercharges in units of 6Y as a stated
  dictionary input; W59's lines as holonomy phases);
- B1654 (the boundary class's norm; the canonical end condition; D = Σ c_s R_s²);
- the SM seat's W59–W61 (the lines, the charges, the selected vacua) and C0;
- B1653's U7 read-out ("at W59's Higgs lines at ω: up and down non-isotropic, leptons isotropic").

**Literature:** twisted Szegő (Kronecker) kernels; the order-3 automorphism of the hexagonal torus and its fixed points
(the three points fixed by z ↦ ωz are 0 and ±(ω − 1)/3).

## 0b. Disclosed

**Main's exploration before the seal** (`verification/before_the_seal/`):
- **`twisted_D_explore`, `twisted_D_lines`.** At τ = ω, on all 18 W59 Higgs lines, D_sector/|R|²:
  - leptons ≤ 5 × 10⁻¹³;
  - quarks in {1.0312, 2.4629, 2.7416}, cycling between up and down, with minimum 1.03;
  - the half-period and 3-torsion lines give 0 in every sector;
  - at the generic τ = 0.13+1.07i, the leptons give 3.08.
- **The channel norms at ω on W59's lines:** c_i = c_j = c_k = 2.231269 and c₁ = −3.575627 in every sector, and R₁ = 0
  for the leptons.
- **`controls_explore`.**
  - On the 9-torsion lines (1/9, 2/9) and (1/9, 0), whose 3w is not ω-fixed, the leptons' R₁ ≈ 10⁻¹⁶ but the imaginary
    norms split (−2.78, −2.78, 22.6), and the lepton lift is 2.92.
  - With fictitious lepton charges (−3, 5) on a W59 line, R₁ = 0.36|R| and D = 3.23.
- **A smoke test of the instrument's functions** (route A at one sector and line; the dual basis; route B at n = 8).

All the values this arc's cells read were seen, except E2's route-B values at n = 32, E1's control, and E6. The
thresholds were set with these in view.

## 1. The setting, and what follows by hand

- **The premises are B1654's P1–P4, with four channels.** The Higgs is S ∈ M₂(ℂ) = span{1, i, j, k}. Each unit's pairing
  P_s is a channel. Its boundary class is the conjugate twisted Szegő kernel K̄_s, K_s = P_s/R_s, cut at one end radius.
  The vacuum factorises, and the canonical end condition equalises the four channels' canonical amplitudes.
- **Stated inputs, not derived:**
  - the hypercharge dictionary (Q 1, u^c −4, d^c 2, L −3, e^c 6, H 3, in units of 6Y);
  - a flat hypercharge line w = ψ₁τ − ψ₂ (B1653);
  - τ = ω;
  - W59's Higgs lines (ψ₁, ψ₂) ∈ {(b + i/3, b + j/3) : b ∈ {1/9, 2/9}, i, j ∈ {0, 1, 2}}, the SM seat's selection.
- **The sectors.** A field of charge q sees qw. For a sector (left, right), ū = (q_L + q_R)w and δ = (q_L − q_R)w.
  - Hypercharge conservation gives q_L + q_R = ±3 = ±q_H for every sector, so ū = ±3w, the Higgs's twist.
  - δ is 5w (up), −w (down) and −9w (leptons).

**What follows:**
1. **The cancellation.** u_s = √(2πL + c_s)·R_s, so u·u = 2πL(R₁² + R·R) + D = D, with D_sector = Σ_s c_s R_s². The log
   cancels because the residue quaternion is null (B1653).
2. **On W59's lines the Higgs's twist is ω-fixed.**
   - 3w = (3ψ₁)ω − 3ψ₂ with 3ψ ∈ (1/3 or 2/3) + ℤ, which is ±(ω − 1)/3 modulo the lattice. Those are the fixed points of
     z ↦ ωz.
   - The rotation then maps each imaginary channel's kernel to another's (it permutes i, j, k, as in B1654 §1.7) and
     fixes the identity channel, with ū fixed and the disc about 0 preserved.
   - So c_i = c_j = c_k =: c_⊥ in every sector, and **D_sector = c₁R₁² + c_⊥(R·R) = (c₁ − c_⊥)·R₁²**.
3. **The electron's zero.**
   - R₁ ∝ θ₁(ū)θ₁(δ). On W59's lines 9w lies in the lattice, since 9ψ ∈ ℤ, and θ₁ vanishes on the lattice.
   - So R₁(leptons) ∝ θ₁(−9w) = 0, while θ₁(ū) ≠ 0.
   - So D_lep = 0, u_lep ∝ R_lep is null, and the lepton coupling has rank ≤ 2 for every Higgs S and every L.
   - **The electron stays massless at this order.** The cause is the hypercharge arithmetic: q_L − q_e = −9 = −3q_H,
     while q_Q − q_u = 5 and q_Q − q_d = −1. The leptons' charges are integer multiples of the Higgs's; the quarks' are
     not.
4. **The quarks.** 5w and −w are not in the lattice, so R₁(up) and R₁(down) ≠ 0. Then D_q = (c₁ − c_⊥)R₁(q)² ≠ 0, and
   the first generation is lifted by about D/(2πL) (B1654), for generic S.
5. **Both conditions are needed.**
   - With 9w in the lattice but 3w not ω-fixed, R₁(lep) = 0 still, but the imaginary norms split and D_lep ≠ 0.
   - With fictitious charges whose difference is not a multiple of 9, R₁(lep) ≠ 0.
   - At a generic τ there is no rotation, and D_lep ≠ 0.

## 2. The instrument

`verification/the_electrons_zero.py`, one run. It writes `the_electrons_zero.json` and `_run.txt` beside itself, after
every cell.
- **Route A.** numpy theta series, polar quadrature about 0 with s = log r, cut at ε.
- **Route B.** B1653's mpmath bilinear and product Gauss–Legendre over P, with 1/|z|², 2Re(a₀/z̄) and 2Re(a₁z/z̄)
  subtracted and restored analytically. The twisted kernels are not odd, so a₀ ≠ 0.
- **The coupling with channel weights.** M′ = Σ_s u_s E_s, with {E_s} dual to the unit pairings; Y_ab is B1644's coupling
  of M′ with the generations' blocks.
- **Points.** The 18 lines are W59's. The generic control is τ = 0.13+1.07i. The non-fixed lines are (1/9, 2/9),
  (1/9, 0) and (2/9, 1/9).

## 3. The cells

| cell | prediction | prior |
|---|---|---|
| **E0**, plumbing (void if any fails) | route A's bilinear against B1653's mpmath bilinear < 10⁻¹¹ relative (two lines, three sectors, two points); the null quaternion < 10⁻¹²; B1653's residue formula R_s ∝ c_s θ_s(ū)θ_s(δ) (ratios to R_i) < 10⁻¹⁰ at five lines, two τ and three sectors | 99% |
| **E1**, the universal log, four channels | every channel's norm agrees across ε = 10⁻³, 10⁻⁴, 10⁻⁵ to < 10⁻⁹ (a W59 line at ω and at the generic τ, all sectors). **Control:** the residue-2 kernel drifts by 6π·log 10 per decade, to 10⁻⁶ relative | 98% |
| **E2**, two routes | routes A and B (n = 32) agree to < 10⁻⁷ on every channel of three cases: up on a W59 line at ω, leptons on a non-fixed line at ω, down at the generic τ | 90% |
| **E3**, the equal norms | on all 18 lines, every sector: c_i = c_j = c_k (spread < 10⁻¹⁰); the gap c₁ − c_⊥ is the same in every sector and on every line (spread < 10⁻⁹) and \|gap\| > 1; D_sector = (c₁ − c_⊥)R₁² to < 10⁻¹⁰\|R\|² | 97% |
| **E4**, the electron's zero | on all 18 lines: \|R₁(lep)\|/\|R\| < 10⁻¹² and \|D_lep\|/\|R\|² < 10⁻¹⁰; the quarks: \|R₁\|/\|R\| > 0.1 and \|D\|/\|R\|² > 0.5 | 95% |
| **E5**, the controls bite | (a) at the generic τ, \|D_lep\|/\|R\|² > 0.1 on three lines; (b) on the three non-fixed 9-torsion lines at ω, \|R₁(lep)\|/\|R\| < 10⁻¹² yet \|D_lep\|/\|R\|² > 0.1; (c) fictitious leptons (−3, 5) on three W59 lines, \|D\|/\|R\|² > 0.1 | 95% |
| **E6**, the masses | for five seeded random Higgs fields S ∈ M₂(ℂ), on three W59 lines: the lepton coupling with canonical weights has σ₃/σ₁ < 10⁻¹² at L ∈ {40, 640, 2560}; the quarks have σ₃/σ₁ > 10⁻⁶ at L = 40, and L·σ₃/σ₁ converges (2560 against 640 within 2%) | 90% |
| **E7**, read-outs | the four channel norms per sector on the line (1/9, 1/9); the three quark values of \|D\|/\|R\|² and their cycle | — |

**What could fail, and what a failure would say:**
- **E3** fails if the rotation argument is wrong: the norms unequal, or the gap sector-dependent.
- **E4** fails if the lepton R₁ is not zero (the residue formula or the arithmetic is wrong), or if a quark sector has
  no lift.
- **E5(b)** fails if equal norms are not needed: then the electron's zero would come from R₁ alone.
- **E5(c)** fails if the charges do not matter.
- **E6** fails if the coupling's rank does not follow D.

## 4. What it will not show

- which end condition is physical;
- whether τ = ω and W59's lines are nature's (both are stated inputs);
- any mass value: the quark lifts carry the end datum L and the Higgs's direction;
- the second generation;
- the neutrinos (a Dirac pairing with L − ν^c = −3 would have δ = −3w, not in the lattice, so it would be lifted; that
  is noted, not tested);
- a comparison with data.

Context, not a test: in nature the electron is lighter, relative to its generation's heaviest, than the down quark, and
heavier than the up quark.

0 of 19.
