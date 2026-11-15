# B1938 — Frame C's coupling is a Szegő kernel times two twisted determinants, and its read-out does not see the flat line's gauge group

**Verdict: PROVED** (each identity exact to the precision stated, on two routes where stated, each with a planted fault
caught; the gauge-class read-out equal within its sampling error, with a planted control caught). Main, 2026-11-14,
from main's own multi-agent run on frame C's dictionary (four investigators, an adversarial checker each, a synthesis),
every computation re-run by main. Register rows P-850, P-845, P-337. **No value is compared with any measured
number.** **No joint of frame C changes type, and the count of inputs does not fall.** 0 of 19.

## Seen first

- **Swept:** `VERDICT topic-sweep /Szeg|Kronecker.s function|Ray-Singer|Parseval/: 4 of 1679 arcs on main match (NEGATIVE 1, OPEN 1, PROVED 2); 3 register rows match (DONE 2, QUEUED 1)`.
  - B1651 and B1654 compute the boundary class and its norm.
  - B1165 and B1168 are unrelated uses of the words.
- **Swept:** `VERDICT topic-sweep /Szeg|Kronecker('s)? (function|theta)|Ray-Singer|twisted Laplacian|spin structure|Parseval|gauge group|Pin\(2\)/: 38 of 1679 arcs on main match (NEGATIVE 9, OPEN 2, PROVED 26, RETRACTED 1); 16 register rows match (DONE 8, QUEUED 8)`.
  - The channels as spin structures are P-337's.
  - K_s's closed form, the vanishing of Σ R_s² and the zero law are B1906's.
  - The two normalisations P4 and P4′ are B1654's.
  - The four order-5 lines, and the U(1) no-go in character form, are B1867 § 4, B1914 § 1 and P-721.
  - The D₅ representations are P-718's.
- **The literature:** Kronecker's theta function is the Szegő kernel, the d̄-Green's function of a flat line bundle on
  the torus. Kronecker's second limit formula gives the twisted Laplacian's zeta-regularised determinant (Ray–Singer).
  Both are classical. What is new here is that frame C's construction is exactly these objects, at these lines.

## 1. The coupling is the Higgs's own Szegő kernel (`kernel_is_kronecker.py`, `kronecker_other_lines.py`)
- **The identity.** For each channel s, B1906's bilinear is P_s(u) = R_s K_s(u) exactly, with
  K_s(u) = e^{2πiα_s u} θ₁′(0) θ₁(u + z_s) / (θ₁(u) θ₁(z_s)) and z_s = (q_L + q_R) w − h_s.
  - This is Kronecker's function, with residue 1 at the puncture, multipliers e^{2πiα} and e^{−2πiβ}, and d̄K = πδ.
- **What z_s means.** q_L + q_R = −3, +3, +3 (up, down, leptons) is minus or plus the Higgs's 6Y, so the kernel lives
  on the Higgs field's own hypercharge line.
  - h_s = 0, ½, τ/2, (1+τ)/2 for channels 1, i, j, k: the four spin structures, channel 1 the odd one (P-337; B1935's
    fixed centre).
- **Route 1, against B1906's closed form** (frame C's 24 lines of order 5, three sectors, three τ, four channels, at 20
  digits):
  - the kernel against the bilinear agrees to 6.7e-18;
  - the Kronecker form, the multipliers and z_s agree to 1e-18;
  - R_s = κ_s Z(c_s) Z(d_s)/(2πη), with Z(c) = ϑ[c](0)/η, to 5.1e-21;
  - Σ_s R_s² = 0 to 5.2e-19 relative;
  - up's R₁ vanishes on every order-5 line.
- **Route 2, against main's own numpy contour residues** (not the closed form), on random lines, lines of order 7 and
  12, and a τ outside the strip: 96 cases to 6.2e-15.
- **Plants.** Using the relative line as the kernel's line fails by 0.23. Moving channel i's half period fails by 0.18.

## 2. The residue is two twisted determinants (`residue_as_determinants.py`; route 2 above)
- **The formula.** |R_s| = √(det Δ_{χ_s} det Δ_{δ_s}) / (2π∣η∣), where det Δ_χ is the zeta-regularised determinant of
  the flat Laplacian on the line bundle of holonomy χ = c − (½, ½).
- **The check.** The identity |ϑ[c](0)/η|² = det Δ_χ (Kronecker's second limit formula) is checked against an
  independent Mellin computation of −ζ′(0) from the lattice theta series: 12 cases to 1.1e-14. On the frame's lines,
  route 2 gives 8.4e-15.
- **Plant.** Using χ = c instead of c − (½, ½) fails by 0.30.
- **Caveat.** Characteristics must be reduced mod ℤ² first; unreduced ones fail by up to 7e-2. No figure here uses
  unreduced ones.

## 3. B1919's constant, derived by Parseval (`parseval_constant.py`)
- **The expansion.** K_s = Σ_v e_v/λ_v over the shifted dual lattice, with λ_v = (m + α)τ − (n − β). Its norm is
  Im τ · Σ∣λ_v∣⁻², which diverges logarithmically.
- **The constant.** With heat regularisation, the disc-cut norm's constant is
  c_s = C_heat + 2π log y − πγ − 2π log π + π log 2, with y = Im τ.
  - Against main's own norm (B1656's definition): 22 channel cases to 1.6e-12.
  - Equivalently, c_s = F_u + π log y − 2π(γ + log π): B1919's identity, now derived without F_u.
- **Plant.** Taking log y with the opposite sign fails by 0.85.

## 4. The read-out does not see the flat line's gauge group (`gauge_class_readout.py`, `gauge_class_control.py`)
- **The question.** On the golden act, a U(1) flat line extends over the thread only when the word fixes the mark's
  vector mod 5 (M v = v). A word that sends it to −v needs Pin(2) or O(2), whose image is binary dihedral or dihedral.
  So frame C's read-out could hide a choice of gauge group.
- **The computation.** The read-out on the whole was computed separately on 3 000 words of each class:
  - U(1): M v = v;
  - Pin(2): M v = −v;
  - neither.
  It used B1928's ergodic integral on B1932's exact-weight grid, with the canonical end.
- **The expectation,** written before the run: the three agree. The class is a finite-index condition, and B1928's limit
  is the same at every point.
- **The result:** the three agree within sampling error on all fourteen outputs of both Higgs worlds.

  | comparison | max ∣Δ ln∣ | max ∣z∣ | rms z |
  |---|---|---|---|
  | U(1) against Pin(2) | 0.0046 | 1.8 | 1.16 |
  | U(1) against neither | 0.0026 | 1.7 | 0.74 |
  | Pin(2) against neither | 0.0021 | 0.7 | 0.50 |

  Each class's median relative sampling error is about 2e-3.
- **The control.** U(1) words on the exact-weight grid against Pin(2) words on the truncated grid must differ by the
  truncation's ~1 %. They do: max |z| 2.4, so the comparison would have seen a 1 % effect.
- **So the gauge group of the flat line is invisible to frame C's values.** The run's options need no gauge-group
  option.

## 5. What the dictionary run settled and what it did not (verdicts after the adversarial checks)

| joint | verdict | what it means |
|---|---|---|
| the coupling (B1906's bilinear) | partly derived | sections 1 to 3. The construction is a free chiral-fermion correlator on the Higgs's line, but that correlator does not fix the channel weights |
| C06, the channel weights | partly derived | the frame divides the Higgs's channel mode by its norm, as dimensional reduction requires (B1654 § 1 step 2), so the weight's meaning is derived. The choice moves to the vacuum premise P4 (equal canonically normalised amplitudes); any exponent β of the norm has a vacuum that gives it. Equal weights (P4′) give rank 2 by Riemann's quartic relation |
| S01, flatness | partly derived | the flat line can be read as a stationary point of Chern–Simons on the thread's mapping torus. That reading costs 3 or 4 named choices: the principle, the group Pin(2)/O(2), dropping the trivial line, and equal weights without the phases. One ANSATZ would become several named choices; it is offered, not adopted |
| C07 (H = I), C08 (one coupling) | not derived | both stay CHOSEN, with the content the record already gives (the A08 basis, P-705, P-711) |

**Not adopted:** the reading of the residue as a two-fermion theory (SO(4)₁). It is a rewriting, and no script computes
it.

**A correction the run found in a sentence of the record.** "A flat line extends exactly when the history fixes its
character" holds only up to inverse, by the Pin(2)/O(2) extension above. The sentence's homes are registered for a dated
note.

## Not claimed
- That any normalisation of the channel weights is physical. P4, P4′ and the other readings stay choices.
- That frame C is a stationary-phase reading. Stationary phase at level 5 gives the trivial line weight 1 and the two
  twins conjugate phases e(±k/5); frame C uses equal weights and no trivial line. Registered as a lead.
- Any value, and anything about measured numbers.
