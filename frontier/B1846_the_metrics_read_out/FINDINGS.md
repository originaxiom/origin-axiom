# B1846 — the metric's read-out: harmonic time, its energy, its volume (data-free)

*Main, 2026-11-06, at the owner's word ("lets craft a goal around your last message and not stop until its either
achieved or proven unachievable"), after the owner's question on the foundation's weakest point (FL-05, the bridge to
dynamics). The goal: using only the object's own hyperbolic metric (Mostow-rigid; no chosen kinetic term), decide
whether the frame's couplings are read at a point of the fibration circle or as an average. Every number below is
computed by a script in `verification/`, with its committed output. No measured number is read by any script, no
held-out quantity is computed, and nothing is compared with data. 0 of 19.*

## 1. The instrument: harmonic time

- **Harmonic time.** A fibred member M with b₁ = 1 carries one primitive class χ ∈ H¹(M; ℤ). The metric fixes, with no
  choice, the harmonic map θ: M → ℝ/ℤ in that class (dθ closed and co-closed, of minimal growth in the cusp), unique up
  to a rotation of the circle.
- **The solver.** B1295's Hejhal collocation for the harmonic generator of H¹(m004), generalised to any SnapPy
  holonomy (`oa_harm.py`):
  - the holonomy conjugated so the peripheral group fixes ∞, scaled so the maximal cusp sits at height 1;
  - χ from the relator exponent sums, tracked exactly on words;
  - the Ford domain's isometric spheres from a word search over SnapPy's simplified and original generators;
  - φ = φ_lin + Σ c_μ t K₁(2π|μ|t) e^{2πi⟨μ,z⟩}, solved from φ(γP) = φ(P) + χ(γ) at pulled-back points.
- **The checks, on every member** (`step3_*.out`, `step3_*.json`):

| check | m004 (control) | excursion member L⁶RLR | run of 10, L¹⁰RLR |
|---|---|---|---|
| B1295's known coefficient \|c₍₀,₂₎\| = 4.260982635 | 4.260982635 | — | — |
| Ford domain volume (Monte Carlo) against SnapPy's | 2.0308 ± 0.0023 (2.029883) | 5.5981 ± 0.0214 (5.586362) | 5.7354 ± 0.0350 (5.750182) |
| collocation unknowns; residual (rms) | 378; 1.8 × 10⁻⁹ | 3198; 1.5 × 10⁻¹¹ (Rcut 12) | 4250; 7.6 × 10⁻¹⁰ |
| equivariance φ(MP) − φ(P) − χ(M) on the face pairings | 1.8 × 10⁻⁹ | 2.6 × 10⁻¹¹ | 1.5 × 10⁻⁹ |
| φ at two collocation heights (max difference) | 1.5 × 10⁻⁹ | 1.1 × 10⁻¹¹ | 4.5 × 10⁻¹⁰ |
| T1: χ² of the energy profile against flat (39 dof) | 38.6 | 42.0 | 34.9 |

## 2. Two theorems, on every member

- **T1. The energy is uniform in harmonic time.**
  - By the coarea formula, the energy in θ ∈ [a, b] is ∫ₐᵇ F(s) ds, with F(s) = ∫_{Σ_s} ⋆dθ the flux through the level
    set Σ_s.
  - F does not depend on s. Two level sets bound a region, and d⋆dθ = 0 there (Stokes). With the cusp cut at a
    horotorus of height T, the cut torus adds ∫ ∂_t ψ, and ψ decays like e^{−2π|μ|T}.
  - The cusp's divergent part (ℓ log T) is itself uniform in s, because χ is nonzero on the cusp torus.
  - Sard's theorem covers critical points: only regular values are needed.
  - **So the metric's energy places no point, on any member.**
  - **Measured:** m004, χ² = 38.6 on 39 degrees of freedom against flat. The excursion member is flat within its noise
    (`E profile`).
- **T2. The volume weight has no atom.**
  - The volume pushed to the circle has density ρ(s) = ∫_{Σ_s} dA/|dθ|.
  - θ is harmonic, hence real-analytic, and not constant, so each level set has zero volume.
  - In 3D, a nondegenerate critical point leaves ρ continuous.
  - **So no measure the metric supplies on the circle is a point.**
- **Consequence.** A point read-out is not forced by the metric on any member. What the metric fixes is:
  - a clock: harmonic time;
  - two weights: the energy weight, which is uniform, and the volume weight ρ;
  - the points those weights single out: their symmetry centres and the mode of ρ.

## 3. The excursion member (P-717's run of 6, W₁(6) = L⁶RLR)

- **Its thin part is the run's tube.** Its shortest geodesic is the word aaBa, of complex length 0.184870 − 0.802102i
  (SnapPy's length spectrum agrees). χ = 0 on it: it is a fibre curve, the curve the L-run twists. The run of 10
  shortens it to 0.080 (`step1_group.py`, SnapPy).
- **A symmetry.** The word is a cyclic palindrome: its reversal RLRLLLLLL is its rotation by 6. Reversal equals
  conjugation by diag(−1, 1) composed with inversion. So M has an isometry σ (by Mostow) that reverses both the fibre
  and the circle. By uniqueness, θ∘σ = −θ + c, so ρ(s) = ρ(c − s).
- **The volume weight is one hump, centred on the tube** (`step3_b++LLLLLLRLR_R12.json`; Rcut 10 agrees, within 0.11 on every bin):
  - ρ/mean runs from a maximum of 1.75 down to a minimum of 0.81 (Rcut 10: 1.74 and 0.78);
  - it is symmetric about s = 0: the reflection's χ² is 19.4 on 20 degrees of freedom;
  - **θ ≡ 0 on the tube's core.** Over 96 points of aaBa's axis, θ = 1.2 × 10⁻¹⁰ with spread 1.7 × 10⁻¹¹
    (`step5_exc_run.txt`; on the run of 10, spread 1.4 × 10⁻¹⁰). The core lies in σ's fixed set, so there θ = −θ, which forces θ ∈ {0, ½}.
- **The second method agrees: sampling through SnapPy's own nine ideal tetrahedra.** This uses SnapPy's developed
  tetrahedra in place of the Ford domain (`step5_tets.py`):
  - each tetrahedron's volume matches its Bloch–Wigner value; the nine sum to 5.574, against 5.586;
  - ρ via the tetrahedra is 1.73 1.44 1.25 … 1.26 1.36 1.76, matching the Ford-domain profile within noise.
- **The layers in harmonic time.** By tetrahedron, with θ as a circular mean:

| tetrahedron | volume (Bloch–Wigner) | θ | concentration |
|---|---|---|---|
| 3, the run's middle | 0.2149 | 0.0003 | 0.997 |
| 2, 4 | 0.2811 | ±0.033 | 0.991 |
| 1, 5 | 0.5739 | ±0.111 | 0.92 |
| 0, 6 | 0.8711 | ±0.23 | 0.82 |
| 8, 7 (the R L R part) | 0.9596 | 0.388, 0.612 | 0.73 |

  Harmonic time advances 0.03 per layer at the tube and 0.22 through RLR, about 7× slower at the tube. The volume per
  layer there is about 4.5× smaller. The net contrast in ρ is about 2.
- **The convergence rerun.** Rcut 12 (3198 unknowns) against Rcut 10 (2214): the residual falls from 1.0 × 10⁻⁹ to
  1.5 × 10⁻¹¹, and the profile is unchanged within noise.

## 4. The golden control: m004 has no hump

- On the figure-eight (LR; no thin part), ρ is flat. ρ/mean runs from 0.981 to 1.027 over 40 bins, with a per-bin
  standard error of 0.014.
- **So the excursion member's hump comes from its run, not from the method.**

## 5. The run of 10 (L¹⁰RLR; the tube at 0.080)

- **The tube is shorter.** The run of 10 has shortest geodesic 0.080226 with χ = 0, and θ ≡ 0 on its core.
- **The hump is higher and narrower.** ρ/mean has maximum 2.53 at s = 0.013 and minimum 0.75. The reflection's χ² is
  19.7 on 20 degrees of freedom.
- **The volume within |s| < 1/40 of the tube:**

| member | volume within \|s\| < 1/40 |
|---|---|
| uniform | 0.050 |
| m004 | 0.050 |
| L⁶RLR | 0.086 |
| L¹⁰RLR | 0.121 |

- **The second method agrees.** Through its 13 tetrahedra, ρ is 2.32 1.52 1.22 … 1.45 2.38, against the Ford domain's
  2.53 1.47 1.21 … 1.39 2.29.
- **Harmonic time stalls harder.** The middle layers (volumes 0.090, 0.079, 0.090) sit at θ = 0.005, 0.000 and −0.005:
  steps of 0.005 per layer, against 0.03 for the run of 6.
- **The golden part dilutes the tube.** Along L⁶R(LR)^k, SnapPy's volume grows by 2.21 and then 2.07 per period (toward
  m004's 2.03), while the tube stays at 0.185 (`tet_volumes_run.txt`). So the tube's share of the volume falls like
  1/k. In the one-departure limit, the metric's average is blind to the departure, as S306a found for the arclength
  average.

## 6. What this decides, and what it does not

- **Decided: no point is forced.** By T1 and T2, the metric's own measures on the circle are atomless on every member.
  A point read-out is not something the metric produces; it would be a reading.
- **Decided: if a point is read, the metric says which.**
  - The only points it singles out are σ's two fixed points, the tube (s = 0) and the middle of R L R (s = ½).
  - The volume weight's mode is the tube, the middle of the run. That is where P-717 places the apex.
  - The symmetry argument alone does not rank them. S306a (HARVEST row 1593) found the apex forced "given a point
    read-out with no arrow" on the one-departure history, but "on a closed thread apex and anti-apex remain".
  - **The metric ranks them.** The apex (the tube, s = 0) is the volume weight's maximum. The anti-apex (s = ½) lies in
    its broad trough.
- **Decided: if the read-out is an average, the metric fixes its weight.**
  - A coupling that is a scalar density on M averages with ρ. One built from dθ averages uniformly (T1).
  - Which kind a coupling is depends on its field content (B6's kinetic input). That is named, not chosen here.
  - On a closed member the weight sees the excursion: it is concentrated at the tube, more so as the run grows. In the
    one-departure limit (k → ∞) it is blind (§ 5). So S306a's remaining premise, "that the read-out is a point", is
    not supplied by the metric. The metric supplies the alternative: an average that sees the excursion while the
    history is closed and short.
- **Not decided: the value of τ at the tube.**
  - The three object-native readings at the run's middle still disagree: the apex 3.65 (√(40/3)), the deepest pleated
    layer 2.87, and the tetrahedron 2.58 (P-723).
  - The metric-native fourth reading would be the conformal structure of the level surface Σ₀ through the tube. σ acts on
    it anticonformally, so Re τ is fixed and one real number is owed. This instrument is not built.
- **The clock (P-439, B1815).** Harmonic time is a clock the metric fixes on the circle with no choice. The clocks on
  record (move count, Teichmüller area, Weil–Petersson) are clocks on moduli space. The bridge between the two is the
  level-surface modulus map s ↦ τ(Σ_s), not yet built. So B1815's "the clock stays CHOSEN" stands for clocks over
  histories. The circle's own clock is not chosen.

## Seen first

- **Swept:**
  - `VERDICT topic-sweep /volume along the fibration/: 0 of 1591 arcs on main match (none); 0 register rows match (none)`;
  - `VERDICT topic-sweep /harmonic generator/: 2 of 1591 arcs on main match (PROVED 2); 1 register rows match (DONE 1)`;
  - `VERDICT topic-sweep /harmonic (map|form|function)/: 0 of 1591 arcs on main match (none)`;
  - `VERDICT topic-sweep /Margulis|short geodesic|thin tube/: 0 of 1591 arcs on main match (none)`;
  - `VERDICT topic-sweep /energy .*(uniform|equidistrib)/: 0 of 1591 arcs on main match (none)`;
  - `VERDICT topic-sweep /Kaluza|KK reduction|internal volume/: 0 of 1591 arcs on main match (none)`;
  - `VERDICT topic-sweep /real.?analytic|level sets? (of|have)|atom(less|ic)/: 0 of 1591 arcs on main match (none)`;
  - `VERDICT topic-sweep /clock/: 37 of 1591 arcs on main match (NEGATIVE 7, OPEN 4, PROVED 26); 32 register rows match`;
  - plus a grep of the record for "coarea", "Margulis tube", "thin part" and "harmonic map".
- **Read:**
  - B1295, the harmonic generator of H¹(m004), the solver generalised here and its known answer;
  - B1845 § 4 and P-455, the arclength period average;
  - harvest row 1593 (S306a), the history's symmetry: the apex on the one-departure history, apex and anti-apex on a
    closed thread;
  - P-723, the three object-native readings;
  - P-439, B1815 and the web seat's 3d32077ea, the clocks;
  - harvest row 1047, the audit fork's growth of a harmonic map at the cusp, a different object.
- **What the sweep found:** nothing on the record pushes the volume or the energy to the circle by a harmonic map, or
  locates the Margulis tube in harmonic time.
- **The literature:**
  - the coarea formula and Stokes' theorem, and real-analyticity of harmonic functions (classical);
  - the existence of the harmonic map to S¹ in a class (classical; Eells–Sampson in the compact case);
  - thin parts and harmonic forms: Brock–Dunfield, norms on the cohomology of hyperbolic 3-manifolds (named, not
    re-derived; THEOREM_REGISTRY marks the tube law NEEDS-LIT);
  - Minsky's model, which relates Margulis tubes to short curves along a Teichmüller geodesic (coarse; named only).

## 7. Disclosures

- **Three instrument errors were caught by the integrity checks and fixed before any reading** (the owner's rule of
  2026-11-06):
  - a loxodromic test rejected complex traces with |tr| < 2, and missed the tube;
  - a Monte Carlo floor taken from about 10 accepted points truncated the domain;
  - a generator check waited for points that a large-|c| generator can never produce.
- **Two more were caught at the landing test:**
  - **a shadowed variable.** The tetrahedron loop overwrote the stored tube θ, so the first JSONs recorded the last
    tetrahedron's angle in radians. The printed value was correct. The variable was fixed and both outputs regenerated.
  - **an untested tolerance.** The symmetry test's first tolerance (0.12 on any bin) was set without statistics. The
    converged run exceeded it by 0.0002, about the size of the bin noise. It is replaced by a χ² on 20 degrees of freedom
    from the stated per-bin errors.
- **Exploration tier: the ρ profiles are Monte Carlo** (3 × 10⁵ to 4 × 10⁵ points, 40 bins). Their per-bin errors are
  stated.
- **The value question is untouched.** No coupling, ratio or scale was computed.
