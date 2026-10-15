# B1653 — PREREGISTRATION: THE RANK OF A POINT COUPLING — the fibre's zero modes read at one point (a value, or the puncture's residue) form a rank-one bilinear of one doublet, so for every flat line and every Higgs the record's coupling has rank ≤ 2; the twisted residue quaternion is null, R₁² + R·R = 0, with R·R ∝ θ₁(ū)²θ₁(δ)²; the massless left state is the left-handed field's alone, so up and down share it and V = 1 ⊕ U(2): at a point a flat line does not lift the first generation; a radially symmetric profile about a regular point acts as the point, while two points, a non-radial (tilted or anisotropic) profile, or a radial profile about the puncture lift it

cc (main), 2026-10-15. **Sealed before `verification/the_rank_of_a_point_coupling.py` runs.** No data. 0 of 19. POINT_REGISTER P-128 (the owner's B, P-150), and P-129's third premise.

**Why it matters.**
- B1649's first-generation zero rests on four premises (P-129). The owner chose P-128 as the frontier computation:
  whether the flat hypercharge line that the record's own potential places (W59, W60) lifts the zero, sector by
  sector. On the residue route the first generation's masses, the Cabibbo angle and J would come from that lift.
- The design's first version claimed a lift. **Its pre-seal review found the claim false for the record's coupling,
  and main re-derived the review's finding (§0b).**
- This arc seals the corrected statement. At a point no flat line lifts the zero, because the zero is the rank of a
  point coupling. It also seals what does lift it, as controls.

## 0. Seen first

- The topic sweep, widened at the seal: `VERDICT topic-sweep /wilson line|twisted zero mode|hypercharge line|flat
  line|twisted (theta|szeg|residue)|rank one|point coupling|mean.value/: 24 of 1424 arcs on main match (NEGATIVE 2,
  OPEN 2, PROVED 20); 10 other lanes match`. The added terms match B1208, B1335, B1443, B1471, B1477, B154, B1621,
  B1645 and B1651. None states the doublet's rank-one point coupling: B1645's rank-one statements concern Y(a) for
  special directions (a·a = 0), and B1443's coupling tensor is a deck-orbit object.
- Read before writing:
  - the SM seat's reading before W59 (the charges in units of 6Y), W59 (its lines as holonomy phases), W60, W61, and
    §88;
  - chat1's Majorana note (P-146);
  - B1642 (R1, R2), B1644 (`Y_unit`), B1645–B1651, and B1651's second addendum (§107; the Szegő reading; the rank-one
    root);
  - B955 and B956 (L133), for attribution.

## 0b. Disclosed: what was computed before writing this

1. **Main's exploration** (`verification/before_the_seal/explore_twist.py`; its output file is a re-run at 00:16 of
   this deterministic script, whose first run printed only to the terminal; unsealed):
   - the twisted doublet's frame;
   - the pairings' form for the four units, constant in u to 10⁻³⁰;
   - N_s = κ c_s θ_s(δ), with κ common to 10⁻³⁰;
   - R·R = κ²θ₁(ū)²θ₁(δ)²/θ₁′(0)² from contour residues, to 10⁻³⁰;
   - the quartic identity.

   From this, main's first design read a "lift" of the zero. **It was wrong: it used the three-component triplet and
   dropped the identity unit's residue R₁.**
2. **The pre-seal review, first pass** (main's read-only reviewing agent, on design v1, which is kept in
   `design_v1/`): ten findings, all accepted. Its own implementation computed, before this seal:
   - the residue's rank one (∣det∣/max² ≈ 10⁻⁴¹);
   - the null quaternion (10⁻⁴⁰);
   - B1644's coupling at rank 2 (σ_min/σ_max ≈ 10⁻⁴¹) at generic twists, at a half-period at ω and at a W59 line;
   - the shared left null vector (overlap 1 to 15 digits);
   - c₁ = −i at twelve cases, and R·R magnitudes at the lines;
   - that numpy's SVD cannot certify below about 10⁻¹⁶ (E82, as in B1645).
3. **Main's re-derivation** (`verification/before_the_seal/check_rank_one.py` and its output), at three random twist
   pairs with B1644's exact coupling, mpmath SVD and random S ∈ M₂(ℂ):
   - ∣det Res B̃∣/max² ≈ 10⁻⁴²;
   - ∣R₁² + R·R∣ ≈ 10⁻⁴¹, while ∣R·R∣/∣R∣² = 0.2–0.6;
   - σ_min/σ_max ≈ 10⁻⁴¹;
   - left null overlap 1.0.
4. **The pre-seal review, second pass** (on design v2, which is also kept in `design_v1/`), on the instrument's exact
   seeded draws with its own code. It found:
   - v2's spread control was wrong: a radially symmetric profile about a regular point gives (∫ w)·G(c₀) by the
     mean-value property, and v2's apparent lift was aliasing (eight angular nodes);
   - a float comparison that could never pass (U4(a));
   - the rank cells are identities of the construction (Σ_s R_s² = 4 det M for every 2 × 2 M);
   - the plumbing had no thresholds, and small text–code mismatches.

   Its margins on the seeded draws: U0(b) 0.134; U2(d) 0.034; U3(c) minimum 1.1 × 10⁻³ (median 0.020); U4(c)
   minimum 0.0235.

   Its profile numbers, which shaped v3's U6:
   - v2's eight-node radial profile gave ∣det M∣/max² = 1.3 × 10⁻⁸ to 3.1 × 10⁻⁷;
   - with 12 and 16 nodes, 1.5 × 10⁻⁹ and 8.8 × 10⁻¹²;
   - on a dense quadrature, 1.5 × 10⁻¹⁰, then 5.3 × 10⁻¹⁴ on refinement;
   - with other parameters, an elliptical profile gave 0.0125, a tilted one 1.7 × 10⁻⁴, and one radial about the
     puncture 0.629.
5. **Main's U6 threshold computation** (`verification/before_the_seal/u6_thresholds_before_the_seal.py`; its output
   file is a deterministic re-run, identical to the first run's printout; the exploration's series code, three random
   pairs, 64 angles):
   | profile | ∣det M∣/max² | coupling σ_min/σ_max |
   |---|---|---|
   | radial about a regular point | about 10⁻³⁸ | about 8 × 10⁻⁴⁰ |
   | tilted | 6.5 × 10⁻⁴ to 2.8 × 10⁻³ | ≥ 6.1 × 10⁻⁵ |
   | elliptic | 3.9 × 10⁻³ to 1.0 × 10⁻² | ≥ 1.6 × 10⁻⁴ |
   | radial about the puncture | 0.46 to 1.18 | ≥ 0.034 |

   U6's thresholds below were set from these, with margins of 34× or more on main's own pairs.
6. **The pre-seal review, third pass** (on v3, on the instrument's exact seeded draws, with its own code; no defects;
   text-only fixes, all taken). The seeded margins:
   | profile | ∣det M∣/max² | margin | σ_min/σ_max | margin |
   |---|---|---|---|---|
   | (a) radial about c₀ (must stay below 10⁻³⁰) | ≤ 1.9 × 10⁻³⁸ | 5 × 10⁷ | ≤ 1.1 × 10⁻³⁹ | 9 × 10⁸ |
   | (b) tilted | 4.3 × 10⁻⁴ to 2.7 × 10⁻³ | 42.6 | ≥ 3.5 × 10⁻⁵ | 34.7 |
   | (c) elliptic | 1.6 × 10⁻³ to 1.0 × 10⁻² | 15.9 | ≥ 1.2 × 10⁻⁴ | 124 |
   | (d) radial about the puncture | 0.63 to 0.96 | 62.9 | ≥ 0.0104 | 10.4 |

   So the smallest margins are 10.4 (U6(d)'s σ ratio) and 15.9 (U6(c)'s determinant). The aliasing for (a), by hand,
   is (0.1/0.3606)⁶⁴ ≈ 2.2 × 10⁻³⁶; weighted, it is about 5 × 10⁻³⁸, as measured.

   The plumbing on the seeded draws: jtheta against the series 3.7 × 10⁻⁴¹; θ₁′(0) against 2πη³ 4.6 × 10⁻⁴¹; the
   characteristic shift 2.3 × 10⁻⁴¹; ω-fixed 9.2 × 10⁻⁴¹; the signed permutation 2.6 × 10⁻⁴⁰. All are at least
   10⁹ below the void threshold.

**So the arc's central cells test a statement already seen several times, and several are identities of the
construction.** Their weight is a third, sealed instrument (mpmath's
jtheta with characteristics by shift, B1651's convention, against two series codes) over every line on the record and
every sector, together with controls that can fail: two-point couplings and non-radial or puncture-centred profiles
must have rank 3, a radially symmetric profile about a regular point must not, and a different left field must not
share the null vector.

## 1. The derivation, by hand, written before the run

1. **The object** (W21; B1642; B1644).
   - The zero mode is F = (f(u), f(u + τ)), with f(u) = θ₃(u; 2τ)/√θ₁(u; τ), in the period-1 convention, carrying
     ρ_Q: a ↦ QI, b ↦ QJ.
   - The generations are the blocks C_p F, with C_p = j, i, k.
   - The coupling of fields x and y through a Higgs S ∈ M₂(ℂ) at the puncture is Y_ab = Res (C_a F_x)ᵀ εS (C_b F_y)
     (B1644's `Y_unit`).
2. **A flat line** (the reviewer's and main's frame; design v1 §1.2).
   - θ₃(u; 2τ) is replaced by θ[a, b](u; 2τ), and the record's frame is F̃ = (f(u), e^{iπb} f(u + τ)).
   - The field's twist has multipliers e^{2πia} along 1 and e^{−iπb} along τ, and its line point is w = aτ + b/2.
   - **Stated inputs.**
     - Hypercharge is a flat U(1) on the fibre, with the Standard Model's charges in units of 6Y (Q 1, u^c −4, d^c 2,
       L −3, e^c 6, H 3). This is the dictionary's, not derived (B1652's F1 D3 is OPEN).
     - A line on the record is given by holonomy phases (ψ₁ along 1, ψ₂ along τ), so w = ψ₁τ − ψ₂ (the reviewer's
       finding 4). A field sees 6Y · w.
3. **The pole.**
   - θ₁(u + τ) = −e^{−iπτ−2πiu}θ₁(u) also vanishes at 0, so both components of F̃ behave like u^{−1/2}:
     F̃ ≈ u^{−1/2} v.
   - **So Res(F̃_x F̃_yᵀ) = v_x v_yᵀ is rank one.** A value at a regular point, F̃_x(u₀)F̃_y(u₀)ᵀ, is rank one too.
4. **Rank ≤ 2.** Y_ab = (C_a v_x)ᵀ (εS)(C_b v_y) = (Aᵀ εS B)_ab, with A = [C_a v_x] and B = [C_b v_y], both 2 × 3. So
   rank Y ≤ 2 for every line and every S. The left null vector solves A u = 0, so it depends on v_x alone.
5. **The null quaternion.**
   - The four unit residues are R_s = Res F̃_xᵀ ε C_s F̃_y, for C_s ∈ {1, i, j, k}. They are the quaternion components
     of a rank-one 2 × 2 matrix, so R₁² + R_i² + R_j² + R_k² = 0.
   - With the exploration's formula, R_s = κ c_s θ_s(ū)θ_s(δ)/θ₁′(0) with c = (−i, −1, −1, i), the null quaternion is
     the quartic identity θ₂²θ₂² + θ₄²θ₄² − θ₃²θ₃² = θ₁²θ₁².
   - **So the triplet's R·R = −R₁² ∝ θ₁(ū)²θ₁(δ)² is not zero, yet the coupling is still rank 2.**
   - Untwisted, R₁ = Fᵀ ε F = 0 by antisymmetry, which recovers B1649 and B1651's U3a.
6. **The sectors.** Up (Q, u^c) and down (Q, d^c) share the left field Q, so they share the left null vector:
   V = 1 ⊕ U(2) for every line, and the first generation is massless and unmixed. The leptons (L, e^c) have their own.
7. **What lifts it, and what does not.** G(z) = F̃_x(z) F̃_y(z)ᵀ is holomorphic away from the puncture.
   - **A radially symmetric profile about a regular point c₀ acts as the point.** By the mean-value property,
     ∫ w(∣z − c₀∣) G = (∫ w) G(c₀), which is rank one, so the zero is kept.
   - **These lift it:**
     - two points: a sum of two rank-one bilinears, generically rank 3;
     - a profile with a non-zero holomorphic moment ∫ w (z − c₀)ⁿ, n ≥ 1, i.e. a tilted or anisotropic one: M has
       rank 2;
     - a radially symmetric profile about the puncture. It reads the regular part G₀ = v_x v′_yᵀ + v′_x v_yᵀ (the
       circle average of the 1/z pole vanishes), which is rank 2. The residue is a contour reading, the (0, 1)
       typing's, and is not the limit of shrinking radial profiles.

   This is the frame dependence the record found: W72's surface-frame overlap has rank 3, and B1649's point has the
   zero.

## 2. The cells

| cell | prediction | prior |
|---|---|---|
| **U0, the frame** | (a) the record-frame bilinears obey P̃(u + 1) = e^{2πi(a_x+a_y)} QI P̃ QIᵀ and P̃(u + τ) = e^{−iπ(b_x+b_y)} QJ P̃ QJᵀ, at five random twist pairs, three points and three τ (one of them ω), to < 10⁻²⁵; (b) the CONTROL frame with the symmetric phase e^{iπ(b_x+b_y)/2} on both i-parity terms fails U1's form test by > 10⁻³ whenever b_x ≠ b_y (the reviewer's sharper control) | 95% |
| **U1, the form** | for the four units: (a) P_s(u) θ₁(u) e^{−2πiAu}/θ_s(u + ū) is constant in u to < 10⁻²⁵; (b) N_s/(c_s θ_s(δ)) is common to the four units to < 10⁻²⁵, with **c = (−i, −1, −1, i)** for (1, i, j, k); (c) untwisted, the c-values reproduce B1642's stored R2 c-values (`residue_coupling.json`), at two τ, to < 10⁻²⁵ (the stored values are rounded floats; the comparison works because they are exactly −1, −1 and i) | 95% |
| **U2, the residue is rank one** (a, b: identities of the construction) | at the five pairs and three τ: (a) ∣det Res B̃∣/max² < 10⁻³⁰; (b) ∣R₁² + R·R∣/Σ∣R_s∣² < 10⁻³⁰; (c) R·R = κ²θ₁(ū)²θ₁(δ)²/θ₁′(0)² to < 10⁻²⁰ relative; (d) the triplet alone is not isotropic: ∣R·R∣/∣R∣² > 10⁻³ at all five generic pairs, at three τ | 99% |
| **U3, rank ≤ 2 at the puncture** (a, b: identities; c: the rank detector's positive control) | B1644's coupling with 20 random S ∈ M₂(ℂ), by mpmath SVD at 40 digits, σ_min/σ_max < 10⁻³⁰: (a) at the five pairs and three τ; (b) at every line on the record, sector by sector (up, down, leptons), with five of the draws at each: the three half-periods at ω and at a generic τ, ω's eight non-zero 3-torsion points, and W59's 18 Higgs lines at ω, in W59's phases; (c) the CONTROL, a two-point coupling (S₁ at the puncture plus S₂ at the regular point u₀ = 0.3 + 0.2i, the value scaled to the residue's size) has σ_min/σ_max > 10⁻⁶ for every one of the 20 draws at three pairs, at a generic τ | 99% |
| **U4, the shared null state** (a, b: identities; c: the overlap detector's positive control) | with independent random S_u and S_d: (a) the left null vectors of Y_up (Q, u^c) and Y_down (Q, d^c) coincide, max(1 − overlap) < 10⁻²⁵ computed in mpmath, at five random lines at a generic τ (drawn from the seed) and at every line on the record; (b) so the CKM's first row and column are trivial: ∣V_12∣, ∣V_13∣, ∣V_21∣, ∣V_31∣ < 10⁻²⁰; (c) the CONTROL, a down-type sector whose left field carries a different twist (6Y = 2 in place of 1), has 1 − overlap > 10⁻³ at the five random lines | 99% |
| **U5, a regular point** (an identity) | at a generic τ, three points u₀ and the five pairs: the value bilinear F̃_x(u₀) F̃_y(u₀)ᵀ has ∣det∣/max² < 10⁻³⁰, and its coupling (B1644's form with the value in place of the residue) has σ_min/σ_max < 10⁻³⁰ for five draws | 99% |
| **U6, profiles** (the determinant detector's controls) | at a generic τ and three pairs, on a polar grid of 64 angles (radii 0.01–0.1 about c₀ = 0.3 + 0.2i; 0.02–0.1 about the puncture), with g(r) = e^{−r²/0.0025}: (a) radially symmetric about c₀, weight g: ∣det M∣/max² < 10⁻³⁰ and σ_min/σ_max < 10⁻³⁰ over 20 draws (acts as the point); (b) tilted, g(r)(1 + Re(z − c₀)/0.05), a signed weight (it is negative where Re(z − c₀) < −0.05; a Higgs profile is a complex field, and what matters is its non-zero dipole moment): ∣det M∣/max² > 10⁻⁵ and σ_min/σ_max > 10⁻⁶; (c) elliptic, e^{−(Re(z−c₀)/0.1)² − (Im(z−c₀)/0.03)²}: > 10⁻⁴ and > 10⁻⁶; (d) radially symmetric about the puncture, weight g: > 10⁻² and > 10⁻³ | 95% |
| **U7, read-out** | c₁ and κ at each of the fifteen (τ, pair) cases; R·R per sector at each line on the record (the triplet's numbers, for the record); the two-point minimum ratio; U6's ranges | — |

**Plumbing, on known cases only, each < 10⁻³⁰, or the run is void as an instrument failure (disclosed, fixed, not
counted)** (`the_rank_of_a_point_coupling.py`; seeds: numpy default_rng(16531) for the twist pairs, the twenty S and
the random lines):
- jtheta against the series at t₀ AND at ω;
- θ₁′(0) = 2πη³;
- the characteristic shift against the series;
- W59's minima 3w are ω-fixed in the phase convention, for both families (1/9 and 2/9) (the reviewer's check);
- the half-period shift of one field acts on the four pairings as a signed permutation. This is design v1's U3, which
  can fail only on the frame algebra, so it is plumbing and not a cell.

## 3. The reading, if the cells hold

- **P-128 is answered at a point: no flat line lifts the first generation.** The zero is the rank of a point
  coupling. The three generations are three quaternionic images of one doublet value, so any coupling read at one
  point (or at the puncture's residue) factors through ℂ².
- **The record's zeros are one fact.** B1649's null R, B1651's isotropy at every point and B1650's O6 are its
  untwisted, antisymmetric case. With a line, the triplet's R·R ≠ 0 but R₁ compensates, and V = 1 ⊕ U(2) for every
  line.
- **What lifts the zero is not a line but a coupling's shape:** two points, a profile with a non-zero holomorphic
  moment, or a profile about the puncture that reads its regular part. A radially symmetric profile about a regular
  point acts as the point and keeps the zero. This is why the surface frame (an overlap integral, W72) lifts it and the
  fibre frame (a point) does not. P-128 thus becomes P-108's and P-151's question: what is the physical Higgs's profile
  on the fibre, and which typing reads it? (A point defect; several points; a stationary solution that is radially
  symmetric about a regular point, which would keep the zero; one that is anisotropic; or one centred on the
  puncture.)
- **What it does not show.**
  - Which profile is physical.
  - Any mass or mixing value.
  - Anything in the surface frame, where a line can still matter (the SM seat's W73 keeps its point).

## 4. Commitments

- One run. Its output is committed before it is read.
- No data.
- Any failed cell is reported as failed.
- Designs v1 and v2, all three review passes' findings and code, and main's pre-seal computations are committed with
  the seal as disclosed history (`design_v1/`, `verification/before_the_seal/` and its `review/`).
