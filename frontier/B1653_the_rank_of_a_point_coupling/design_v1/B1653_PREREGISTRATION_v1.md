# B1653 — PREREGISTRATION: THE TWISTED ZERO MODE — a flat hypercharge line on the fibre's zero modes, sector by sector: the residue triplet becomes c_r θ_r(ū) θ_r(δ), so R·R ∝ θ₁(ū)² θ₁(δ)² and the first generation is lifted exactly where the Higgs is twisted and the pair is twisted relative to itself; at the record's lines the colour centre keeps every zero, a half-period lifts every sector alike, and W59's Higgs lines lift the quarks and keep the leptons

cc (main), 2026-10-1x. **DRAFT — not sealed.** Sealed before `verification/twisted_zero_mode.py` runs. No data.
0 of 19. POINT_REGISTER P-128 (the owner's B, P-150), the third of P-129's premises.

**Why it matters.**
- B1649's first-generation zero rests on four premises (P-129). The first, a Higgs at a point, is settled by B1651
  and its second addendum: the zero belongs to point Higgs fields.
- The third is "zero Wilson line". The record's own one-loop potential places a hypercharge line: W59 finds the
  colour centre's 3-torsion lines at ω for charged bosons, and W60 finds a half-period line once the Higgs is included.
- So the question is what such a line does to the residue coupling, sector by sector. On the residue route this is
  where the first generation's masses, the Cabibbo angle and J would come from (P-128).
- This arc computes the structure: the twisted residue and its zero set at the lines on the record. The masses' and
  the mixing's read-outs, including the Gatto–Sartori–Tonin cell, are the next arc (B1654), sealed after this one lands.

## 0. Seen first, and disclosed

**Seen first.**
- The topic sweep: `VERDICT topic-sweep /wilson line|twisted zero mode|hypercharge line|flat line|twisted
  (theta|szeg|residue)/: 15 of 1424 arcs on main match (NEGATIVE 1, OPEN 1, PROVED 13); 10 other lanes match`.
- Read before writing:
  - the SM seat's reading before W59 (point 4: the charges in units of 6Y; no 2-torsion line splits d from e; a
    3-torsion line twists only the quarks), W59, W60 and W61, and its §88 (CP and the line);
  - chat1's note that a Majorana self-pairing has δ = 0 (P-146);
  - B1642 (R1, R2; "a flat Wilson line does not change this", said of the antisymmetry), B1644–B1651, and B1651's
    second addendum (§107 checked; the Szegő reading; a spread Higgs lifts the zero);
  - B955 and B956 (L133, Wilson-line breaking in the GUT era): a different object, read for attribution.

**Disclosed: what main computed before writing this** (`verification/exploration_before_the_seal.py` and its output,
committed with the seal; unsealed):
- the twisted doublet's frame, by hand (§1.2);
- numerically, for generic twists: the form of the twisted pairing (constant in z to 10⁻³⁰); N_r = κ c_r θ_r(δ) with κ
  common to the three parities (to 10⁻³⁰, three twist pairs); R·R from contour residues equal to
  κ² θ₁(ū)² θ₁(δ)²/θ₁′(0)² (to 10⁻³⁰); the quartic identity (to 4 × 10⁻³¹);
- by hand from the formula: the half-period subtlety (§1.4) and the map at the lines (§1.5).

**So U0–U3 test a formula already seen.** Their weight is the independent instrument: mpmath's jtheta in B1651's π z
convention with characteristics by shift, against the exploration's series in B1642's period-1 convention. Their
controls, including the naive frame that must fail, test the crux. U4 and U5 are computed for the first time in the
run, though their pattern was predicted by hand from the formula.

## 1. The derivation, by hand, written before the run

1. **The object.** The record's zero mode is (W21; B1642) F = (f(z), f(z + τ)) dz, with f(z) = θ₃(z; 2τ)/√θ₁(z; τ),
   carrying ρ_Q: a ↦ QI = diag(i, −i), b ↦ QJ = [[0, 1], [−1, 0]]. A field of hypercharge Y on a line sees the flat
   U(1) twist 6Y · w at the point w of the Jacobian, modulo the lattice (the SM seat's convention). **Stated inputs:**
   hypercharge as a flat U(1) on the fibre, with the Standard Model's charges in units of 6Y, is the dictionary's
   (F-MC; W27; the reading before W59), not derived (B1652's F1 D3 is OPEN). Every field's zero modes are the same
   doublet's, twisted by its own charge (B1649's "one fibre"), and the Higgs sits at the puncture (P1; B1651's
   second addendum: the zero is a property of point Higgs fields).
2. **The twisted doublet, and the crux.**
   - Replace θ₃(z; 2τ) by θ[a, b](z; 2τ). The a-holonomy becomes e^{2πia} QI.
   - The b-holonomy becomes [[0, 1], [−e^{−2πib}, 0]] = e^{2πiβ} D QJ D⁻¹, with β = −b/2 and D = diag(1, e^{−iπb}).
   - **So the doublet in the record's frame is F̃ = (f(z), e^{iπb} f(z + τ)).** The field's line point is w = aτ + b/2.
   - The invariant pairing F̃_xᵀ ε C F̃_y then carries e^{iπ(b_x + b_y)} in the j and k parities, but e^{iπb_x} and
     e^{iπb_y} separately in the i parity. This relative phase is the crux P-128 named. It does not cancel, and it is
     what makes the three parities combine.
3. **The pairing and its residue.** For each parity r (i ↔ θ₂, j ↔ θ₄, k ↔ θ₃; c = (−1, −1, i)):
   - P_r(z) = κ · c_r θ_r(δ) · e^{2πiAz} θ_r(z + ū)/θ₁(z), with A = a_x + a_y, ū = w_x + w_y and δ = w_x − w_y. This
     is a twisted Szegő kernel at ū, times θ_r(δ).
   - **R_r = κ c_r θ_r(ū) θ_r(δ)/θ₁′(0).**
   - **R·R = κ² θ₁(ū)² θ₁(δ)²/θ₁′(0)²,** by θ₂(x)²θ₂(y)² + θ₄(x)²θ₄(y)² − θ₃(x)²θ₃(y)² = θ₁(x)²θ₁(y)².
   - At every point, v·v ∝ θ₁(δ)² θ₁(z + ū)²/θ₁(z)².
   - **So the zero survives iff ū ∈ Λ or δ ∈ Λ.** In a Yukawa the hypercharges sum to zero, so ū is minus the Higgs's
     own line point. The first generation is lifted exactly when the Higgs is twisted AND the pair is twisted relative
     to itself. A Majorana pair has δ = 0 (chat1).
4. **Shifts.**
   - A lattice shift of one field moves ū and δ by the same lattice vector. The quasi-periodicity signs cancel in
     θ_r(ū)θ_r(δ), and R changes by a common scalar: no physics.
   - A half-period shift h of one field is ρ_Q ⊗ χ ≅ ρ_Q through a unit u, which moves that field's generations to
     shifted parities. R becomes the u-inserted triplet, and R·R ∝ θ₁(ū + h)² θ₁(δ + h)² (not 0 at w = 0).
5. **The lines on the record.** In units of 6Y the charges are Q 1, u^c −4, d^c 2, L −3, e^c 6, H 3.
   - Up (Q, u^c): ū = −3w, δ = 5w. Down (Q, d^c): ū = 3w, δ = −w. Leptons (L, e^c): ū = 3w, δ = −9w.
   - w = 0: every zero survives.
   - The colour centre's 3-torsion lines: 3w ∈ Λ, so ū ∈ Λ, and every zero survives.
   - The half-periods: ū ≡ δ ≡ h in every sector, so every sector is lifted. The leptons' δ differs from the down
     quarks' by 8h, an even lattice step, so R_up ∝ R_down ∝ R_lep: no d–e split.
   - W59's Higgs lines at ω, (1/9, 1/9) and (2/9, 2/9) plus ⅓ℤ²: ū ∉ Λ. The quarks' δ (5w, −w) are not in Λ, but the
     leptons' δ = −9w is. So the quarks are lifted and the leptons keep their zero: a d–e split, with the electron
     massless at leading order.

## 2. The cells

| cell | prediction | prior |
|---|---|---|
| **U0, the frame** | (a) the record-frame doublets' bilinears obey P̃(z + 1) = e^{2πi(α_x+α_y)} QI P̃ QIᵀ and P̃(z + τ) = e^{2πi(β_x+β_y)} QJ P̃ QJᵀ, at five random twist pairs and three points, to < 10⁻²⁵; (b) the CONTROL: the naive frame D = 1 fails the τ-law by > 10⁻⁶ whenever b_x ≠ b_y | 97% |
| **U1, the form** | (a) P_r(z) θ₁(z) e^{−2πiAz}/θ_r(z + ū) is constant in z to < 10⁻²⁵; (b) N_r/(c_r θ_r(δ)) is the same for the three parities to < 10⁻²⁵; (c) the untwisted case reproduces B1642's R2 to < 10⁻²⁵; (d) the odd unit's pairing (C = 1, θ₁) has the same form, with a constant c₁ (read out) that agrees across the five twist pairs to < 10⁻²⁰ | 95% |
| **U2, R·R** | (a) contour residues give R·R = κ² θ₁(ū)² θ₁(δ)²/θ₁′(0)² to < 10⁻²⁰ relative; (b) Majorana pairs give ∣R·R∣/∣R∣² < 10⁻²⁵; (c) the quartic identity to < 10⁻²⁵; (d) a scaling control: with δ fixed and ū = ε u₀, ∣R·R∣/∣R∣² ∝ ε², with a log-slope of 2 ± 0.05 over ε from 10⁻¹ to 10⁻⁴ | 95% |
| **U3, the shifts** | (a) a lattice shift of one field (by 1 and by τ) leaves R's component ratios unchanged to < 10⁻²⁰; (b) a half-period shift of one field gives the u-inserted triplet up to a common scalar, to < 10⁻²⁰ | 85% |
| **U4, the lines** | at τ = ω and at a generic τ, with the charges above: (a) w = 0: every sector has ∣R·R∣/∣R∣² < 10⁻²⁵; (b) at ω's eight non-zero 3-torsion points: every sector < 10⁻²⁵; (c) the three half-periods: every sector > 10⁻³, and the three sectors' R are proportional to < 10⁻²⁰; (d) W59's 18 Higgs lines at ω: the up and down sectors > 10⁻³, the leptons < 10⁻²⁵ | 85% |
| **U5, the masses' zero pattern** | with a Higgs at the puncture, Y(a; R_s) = a R_sᵀ + R_s aᵀ − (a·R_s) 1 for 20 random complex directions a (the real democratic class is a read-out in U6, since a·R = 0 would zero a value for another reason): the smallest Takagi value is < 10⁻²⁰ × the largest exactly where U4 gives R·R = 0, and > 10⁻⁸ × the largest where it does not | 90% |
| **U6, read-out** | each line's (ū, δ) and ∣R·R∣/∣R∣² per sector; at the half-periods, the common ratio m₁/m₃ for the democratic a (a read-out, compared with no data) | — |

**Plumbing controls, on known cases only:**
- the untwisted pairing against B1642's stored R2;
- θ₁′(0) = 2πη³ (the period-1 convention of B1642);
- the characteristic-by-shift theta against the direct series at three points.

## 3. The reading, if the cells hold

- **The third premise of the Cabibbo zero is decided by the line.** The zero is lifted exactly where the Higgs is
  twisted and the pair is twisted relative to itself.
- **At the record's selected states:**
  - the colour centre keeps every zero;
  - W60's half-period minimum lifts every charged sector alike, with no d–e split and one common R, so no
    misalignment;
  - W59's Higgs lines split the quarks from the leptons and keep the electron massless at leading order.
- **A tension to state.** At W60's state the SM seat's W61 bulk-overlap coupling is degenerate, while main's residue
  coupling lifts the first generation. Two couplings at one state; which is physical is the dictionary's question
  (P-108; the parent's clause 4).
- **What it does not show.**
  - No mixing and no value: B1654 does those.
  - Not which line: the dynamics on record selects W60's half-period line, where nothing misaligns.
  - Not which Higgs: point or spread; this arc uses the puncture's residue.
  - Not the dictionary: the charges are the Standard Model's, an input.

## 4. Commitments

- One run. The output is committed before it is read.
- No data. B1654 is sealed only after this lands.
- Any failed cell is reported as failed, with the formula's status re-read from the cell that failed.
- The exploration's script and output are committed with the seal, unchanged.
