# B1653 — THE RANK OF A POINT COUPLING: the fibre's zero modes read at one point (a value, or the puncture's residue) form a rank-one bilinear of one doublet, so for every flat line and every Higgs the record's coupling has rank ≤ 2; the massless left state is the left-handed field's alone, so V = 1 ⊕ U(2); at a point a flat hypercharge line does not lift the first generation, and only a coupling that does not act as a point does

**Verdict: PROVED.** Every cell holds as sealed. cc (main), 2026-10-15.
- Sealed `4e3981e24` (sha256 70ecef80) before the run. The output was committed unread at `832d17295`.
- No data. **0 of 19.**
- POINT_REGISTER P-128 (the owner's B, P-150), P-129's third premise, and P-151.

## 0. Seen first

As sealed: `VERDICT topic-sweep /wilson line|twisted zero mode|hypercharge line|flat line|twisted
(theta|szeg|residue)|rank one|point coupling|mean.value/: 24 of 1424 arcs on main match (NEGATIVE 2, OPEN 2, PROVED
20); 10 other lanes match`.
- None of the matches states the doublet's rank-one point coupling. B1645's rank-one statements concern Y(a) for
  special directions, and B1443's coupling tensor is a deck-orbit object.
- **Read before the seal:**
  - the SM seat's W59–W61 (its lines, the charges in units of 6Y, the record's selected vacua), §88, and W72 (the
    surface frame's overlap, rank 3);
  - chat1's Majorana note;
  - B1642–B1651, and B1651's second addendum.
- **Literature:** theta functions with characteristics; the mean-value property of holomorphic functions; Jacobi's
  quartic identities (Whittaker–Watson §21.2). That a bilinear form evaluated on vectors of one rank-one family has
  rank ≤ 2 is elementary linear algebra. Nothing here is claimed as new mathematics. What is new on the record is that
  the record's coupling has this form, and what follows from that for the first generation.

## 0b. Disclosed

In full in the preregistration's §0b; in brief:
- **Main's first design was wrong.** It read a "lift" of the first generation by a flat line from the triplet's
  R·R ∝ θ₁(ū)²θ₁(δ)², having dropped the identity unit's residue R₁.
- **A read-only reviewing agent made three passes before the seal.**
  - v1: the rank-one residue (decisive), the line convention w = ψ₁τ − ψ₂, and numpy's precision floor.
  - v2: the mean-value property, which broke v2's spread control (the apparent lift was aliasing), and a float
    comparison that could never pass.
  - v3: text fixes and the seeded margins.
- **Main's re-derivation and its U6 threshold computation.**

Designs v1 and v2, the review's code and main's pre-seal scripts are kept beside the seal (`design_v1/`,
`verification/before_the_seal/`).

## 1. The sealed run (`verification/the_rank_of_a_point_coupling.py`, unchanged; `the_rank_of_a_point_coupling.json`, `_run.txt`)

**Plumbing**, each required < 10⁻³⁰ or the run is void:

| check | value |
|---|---|
| jtheta against the series (t₀ and ω) | 3.7 × 10⁻⁴¹ |
| θ₁′(0) against 2πη³ (three τ) | 4.6 × 10⁻⁴¹ |
| characteristic shift | 2.3 × 10⁻⁴¹ |
| W59's minima ω-fixed (both families) | 9.2 × 10⁻⁴¹ |
| the half-period shift as a signed permutation | 2.6 × 10⁻⁴⁰ |

| cell | prediction | prior | result |
|---|---|---|---|
| **U0**, the frame | (a) the twisted holonomy laws < 10⁻²⁵; (b) the symmetric-phase control frame fails the form test by > 10⁻³ | 95% | **HOLDS:** (a) 5.4 × 10⁻⁴⁰; (b) min 0.134 |
| **U1**, the form | (a) constant in u < 10⁻²⁵; (b) N_s/(c_s θ_s(δ)) common, c = (−i, −1, −1, i); (c) B1642's stored c-values | 95% | **HOLDS:** (a) 2.4 × 10⁻³⁹; (b) 2.6 × 10⁻³⁹ (c₁ = −i at all fifteen cases); (c) 5.1 × 10⁻⁴¹ |
| **U2**, the residue is rank one | (a) det < 10⁻³⁰; (b) the null quaternion < 10⁻³⁰; (c) R·R = the formula < 10⁻²⁰; (d) the triplet alone non-isotropic > 10⁻³ | 99% | **HOLDS:** (a) 8.5 × 10⁻⁴¹; (b) 9.5 × 10⁻⁴¹; (c) 4.4 × 10⁻³⁹; (d) min 0.034 |
| **U3**, rank ≤ 2 at the puncture | (a) at five pairs and three τ; (b) at every line on the record and every sector; (c) the two-point CONTROL has rank 3 (> 10⁻⁶) | 99% | **HOLDS:** (a) 7.0 × 10⁻⁴¹; (b) 7.4 × 10⁻⁴¹ (32 lines × 3 sectors); (c) min 1.1 × 10⁻³ |
| **U4**, the shared null state | (a) up and down share the left null vector, max(1 − overlap) < 10⁻²⁵; (b) the CKM's massless row and column trivial < 10⁻²⁰; (c) a different left field does not (> 10⁻³) | 99% | **HOLDS:** (a) 1.1 × 10⁻⁴¹; (b) 8.1 × 10⁻⁴⁰; (c) min 0.0235 |
| **U5**, a regular point | the value bilinear is rank one, and its coupling has rank ≤ 2 (< 10⁻³⁰) | 99% | **HOLDS:** det 1.7 × 10⁻⁴⁰; ratio 1.1 × 10⁻⁴⁰ |
| **U6**, profiles | (a) radial about a regular point acts as the point (< 10⁻³⁰); (b) tilted, (c) elliptic and (d) radial about the puncture lift it | 95% | **HOLDS:** (a) det ≤ 1.9 × 10⁻³⁸, ratio ≤ 1.1 × 10⁻³⁹; (b) det ≥ 4.3 × 10⁻⁴, ratio ≥ 3.5 × 10⁻⁵; (c) ≥ 1.6 × 10⁻³ and ≥ 1.2 × 10⁻⁴; (d) ≥ 0.63 and ≥ 0.0104 |

## 2. The read-outs (U7)

- **c₁ = −i at all fifteen (τ, pair) cases**, to about 10⁻⁴⁰.
- **The triplet's R·R at the lines on the record, the pattern that misled the first design:**

  | line | up | down | leptons |
  |---|---|---|---|
  | half-periods | non-isotropic (0.27–0.97) | the same | the same |
  | W59's Higgs lines at ω | non-isotropic (0.22–0.89) | non-isotropic (0.22–0.89) | isotropic (≤ 6 × 10⁻⁴¹) |
  | ω's 3-torsion points | isotropic (≤ 6 × 10⁻⁴¹) | isotropic | isotropic |

  Wherever the triplet is non-isotropic, R₁ compensates it, and the full coupling's rank is 2 at every line (U3(b)).
- **The lifts' sizes.** Two points give σ_min/σ_max ≥ 1.1 × 10⁻³. The profiles' ranges are in U6.

## 3. What it says

- **P-128 is answered at a point: no flat line lifts the first generation.** The three generations are three
  quaternionic images C_p F of one doublet value, so any coupling read at one point, or at the puncture's residue,
  factors through ℂ² and has rank ≤ 2. The massless left state solves A u = 0 with A = [C_p v_x], so it is the
  left-handed field's alone. Up and down share Q, so V = 1 ⊕ U(2) for every line.
- **The record's zeros are one fact.** B1649's null R, B1651's isotropy at every point and B1650's O6 are the
  untwisted, antisymmetric case (R₁ = Fᵀ ε F = 0); B1651's second addendum gives the Szegő form. With a line, the
  triplet's R·R ≠ 0 but R₁² = −R·R, and the zero stays.
- **What lifts the zero is a coupling's shape, not a line:**
  - two points;
  - a profile with a non-zero holomorphic moment about a regular point (tilted or anisotropic);
  - a profile about the puncture, which reads the bilinear's regular part G₀.

  A radially symmetric profile about a regular point acts as the point, by the mean-value property, and keeps the
  zero.
- **This explains the frame dependence the record found:** the surface frame's coupling is an overlap integral (W72,
  rank 3), and the fibre frame's is a point (B1649).
- **So P-128 hands its question to P-151 and the parent (P-108):** what is the physical Higgs's profile on the fibre,
  and which typing reads it?
- **What it does not show:**
  - which profile is physical;
  - any mass or mixing value;
  - anything in the surface frame, where a line can still matter (the SM seat's W73 keeps its point).

## 4. Credit

- **Main's read-only reviewing agent:** the rank-one residue that reversed the first design's headline; the line
  convention; the mean-value property that reversed the second design's spread control; the float trap; the seeded
  margins. Three passes before the seal. A false claim was stopped before it was sealed, which is the review's purpose.
- **The SM seat:** the lines and the charges (W59–W61), and the surface frame's rank-3 overlap (W72), which this arc
  now explains.
- **chat1:** the Majorana note (δ = 0), and O6.
- **The audit lane:** the typing distinction.

## 5. Next

P-151, the Higgs's profile. A candidate first step for C (firewalled; to sweep and design): a tame Higgs field
carrying a parity is a holomorphic section of L_χ with a simple pole at the puncture, unique up to scale, namely the
Szegő kernel S_χ. Couple the zero modes to that profile in each typing, and read the rank and the shared null state.
