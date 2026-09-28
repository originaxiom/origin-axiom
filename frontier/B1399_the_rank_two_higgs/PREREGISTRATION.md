# B1399 PREREGISTRATION — THE RANK-TWO HIGGS: can two independent Higgs classes on a member of m004's class give three generations in a frame with 27 matter?

**Sealed 2026-09-28, before any harmonic form of the census is computed. Seat: cc (the SM-derivation branch). Occasion: B1398, the
frame's verdict. The seat's frame (7d E₆ super-Yang–Mills, the geometric SL(2)_β twist, an abelian Higgs field) cannot give three
generations with any completion on the record's menu. With 27 matter the frame's own rule admits exactly one anomaly-free,
exotic-free family, and no rank-one Higgs field realises it. This is the smallest escape (B1398 §3), and this seal tests it. The
run waits for the owner, who sees the verdict and this seal first.**

## The question

A rank-two abelian Higgs field is φ = Y ⊗ ω₁ + γ ⊗ ω₂, with ω₁, ω₂ independent cuspidal harmonic 1-forms: L² harmonic, from classes
vanishing on every cusp. That is the dynamical Higgs field of B1395.
- By the frame's rule, a spin-0 sector μ gets C(Y(μ)·ω₁ + γ(μ)·ω₂). Here C(v) is the count of the harmonic 1-form v: its signed zero
  number, which equals −Σ_c χ(∂⁺_c(v)) read from v's leading Fourier shell at each cusp (B1388 Theorem A; B1387's `chi_plus`).
- SL(2)_β doublets get 0 (B1372's Lemma A).
- In the frame with 27 matter (F27+78, or the E₇ frame F133 with the Higgs field in the (Y, γ) plane) the spin-0 sectors fall into
  six direction classes k, with primitive directions (a_k, b_k): (1, −4), (1, 0), (1, 1), (1, 6), (3, −2), (3, 8).
- The only anomaly-free, exotic-free spectrum the rule can give is g complete generations, with targets
  t = g·(1, 0, −1, 0, 1, −2) on those classes (B1398 (5)).

**The question: is there a census member M and cuspidal classes ω₁, ω₂ on M with C(a_k ω₁ + b_k ω₂) = t_k for all six k, at g = 3,
stably (below)?**

## The reduction (proved now)

**Oddness.** C is odd and homogeneous of degree 0 on V ∖ {0}, where V is M's cuspidal space: C(−v) = −C(v) (the positive and negative
partitions exchange) and C(sv) = C(v) for s > 0.

**Breakpoints.** Take a circle of directions v(θ) = cos θ·w₁ + sin θ·w₂, with w₁, w₂ a basis of V or of a plane W ⊂ V.
- At a cusp c the leading shell is the same for every direction (below). Let g₁, g₂ be its functions for w₁ and w₂, signed so that
  ∂⁺ = {g > 0}. The shell's function for v(θ) is F_θ = cos θ·g₁ + sin θ·g₂, and χ_c(θ) = χ({F_θ > 0}).
- χ_c changes only where a critical value of F_θ crosses zero. Write (g₁, g₂) = ρ(cos ψ, sin ψ). Then F_θ = ρ cos(θ − ψ), and on its
  zero set ∇F_θ = ±ρ∇ψ. So the breakpoints are θ = ψ(x) ± π/2 at the critical points x of the angle map ψ, in antipodal pairs.
- As θ increases through ψ(x) + π/2, the crossing critical point has ψ's type (the Hessian of F_θ there is ρ times ψ's) and leaves
  {F > 0}: a saddle raises χ_c by one, an extremum lowers it. Through ψ(x) − π/2 it enters, saddles staying saddles: the reverse. So a
  generic breakpoint changes C by ±1.
- The critical points are complete when the zeros of g₁∇g₂ − g₂∇g₁ have indices summing to zero (Poincaré–Hopf; each common zero of
  g₁ and g₂ has index +1).
- A shell of one or two directions gives χ_c = 0 in every direction. In adapted coordinates F_θ = A cos u + B cos u′, so {F_θ > 0} is a
  band (one direction: B1370's annulus).
- Checked at design time on synthetic shells (`verification/breakpoint_check.py`, record `breakpoint_check_run.txt`): on two
  3-direction and two 6-direction shells the predicted χ agrees with the Morse count at every one of 720 directions away from the
  breakpoints, and the index sums are zero; two-direction shells give χ = 0 throughout.

**Stability.** The question asks for a stable realisation: every class direction in an open arc between breakpoints. A pair that
sends a class onto a breakpoint is fine-tuned, and the count there is not read.

**The twelve rays.** In angular order the class directions are (1, −4), (3, −2), (1, 0), (1, 1), (3, 8), (1, 6), with targets
g·(1, 1, 0, −1, −2, 0); their opposites carry the negatives. A linear map keeps or reverses cyclic order. So C must visit these twelve
values in turn, and a realisation needs at least 12|g| breakpoints on the circle, counted with multiplicity: 36 at g = 3.

**Cuspidal dimension 2.** The pair (ω₁, ω₂) is a linear map L: ℝ² → V, (a, b) ↦ aω₁ + bω₂. Rank one is a rank-one Higgs field,
excluded by B1398 (6). So L ∈ GL(2, ℝ), and the question becomes whether some L maps each class direction (a_k, b_k) into an arc of V's
circle on which C takes the value t_k.
- "L(a_k, b_k) lies in the open arc (u, u′)", for an arc shorter than π, is two strict linear inequalities in L's four entries:
  det(u, L(a_k, b_k)) > 0 and det(L(a_k, b_k), u′) > 0. An arc of π or more is covered by two overlapping arcs shorter than π. (One
  longer than π contains opposite directions, so it carries C = 0.)
- So realisability is a finite union of linear feasibility problems, one per assignment of classes to arcs of the right value. Oddness
  makes the opposite rays automatic. The inequalities are homogeneous, so strictness is a margin of 1 and each linear program is exact.
- A feasible L is invertible: a rank-one map sends every class to ±w or to 0, and the target takes two absolute values.
- A positive is re-verified. With the L that maximises the smallest margin (entries bounded by 1), C is evaluated directly at the six
  image directions from both seeds' forms, each image farther than 10⁻³ from every breakpoint. ∎

**Cuspidal dimension 3.** The pair spans a plane W ⊂ V. For each plane the dimension-2 method applies to C restricted to W, but the
planes form a continuum.

## The census (fixed now)

**The members.** Every connected cover of degree 2 or 3 (SnapPy 3.3.2's `covers()`) of B1186's 99 arithmetic members whose
cuspidal dimension b₁ − (number of cusps) is at least 2, up to isometry.
- The count: 171 covers, 109 distinct up to isometry. 91 have cuspidal dimension 2 (8 of degree 2, 83 of degree 3) and 18 have
  dimension 3. They have 18–30 tetrahedra and 1–5 cusps: 29 have one cusp, 49 two, 23 three, 7 four and 1 five.
- The list, with each member's isometry signature, triangulation signature and parentage, is `verification/census_list.json`,
  committed with this seal; `verification/census_list.py` regenerates it byte for byte in about ten seconds. It was found at design
  time from homology and canonical triangulations alone. No harmonic form or count of any member was computed.
- None of the 99 base members has cuspidal dimension ≥ 2 (7 have 1). cube~3.24 has 1 (b₁ = 5, four cusps). Its own covers are outside
  by size: 180 tetrahedra at degree 2 (27 of its 31 double covers have cuspidal dimension ≥ 2) and 270 at degree 3.

**The Higgs pairs.**
- **Dimension 2.** Every L ∈ GL(2, ℝ), decided by the reduction.
- **Dimension 3.** The three coordinate planes of the solved basis and 200 planes with normals
  `numpy.random.default_rng(1399).normal(size=(200, 3))`, normalised, each decided by the dimension-2 method. A positive is exact once
  found; a negative is scoped to the sampled planes.

## The count function

**The harmonic forms.** B1387's Hejhal solve (sample points pulled back into SnapPy's fundamental polyhedron; one linear equation per
sample), generalised to a basis of V with one right-hand side per basis class.
- The ladder, fixed now: (K_n, τ) = (10, 0.10), then (14, 0.10), then (14, 0.08); chart seed 1; sample seeds 1 and 2 on every rung.
  The first rung on which both seeds pass acceptance is used.

**Acceptance.** The thresholds are set now. B1387's runs b–e meet them; its run a (K_n = 6) does not.
- full column rank, and every basis class vanishing on every parabolic;
- fit residual rms below 10⁻³, and test residual rms at heights 0.06 and 0.09 below 10⁻²;
- the sampling height below the lowest pulled-back normalised height (Hejhal's condition, as B1387 checked);
- the two seeds agree: the same leading shell at every cusp, breakpoints matched within 10⁻³ in angle, and the same C on every arc.

A member failing every rung is reported as unresolved. It is listed with the verdict and does not count toward NONE.

**The leading shells, decided on V.**
- At each cusp the shells are taken in order of |k|. A shell is killed when its coefficient map V → ℂ^m (in the solved basis) has norm
  below 10⁻² of the largest among the cusp's first six shells. That is B1387's threshold, applied to the map rather than to one
  vector. A ratio between 10⁻³ and 10⁻¹ makes the member unresolved.
- The leading shell is the first one not killed, the same for every direction.
- If the leading shell's map has real rank one (second singular value below 10⁻² of the first; between 10⁻³ and 10⁻¹, unresolved),
  the shell is ± one function, and χ_c flips at the two directions where the map vanishes.

**C on a circle.**
- At each cusp whose leading shell has three or more directions, the critical points of ψ are found by damped Newton on
  g₁∇g₂ − g₂∇g₁ = 0 from 64, then 128, then 256 seeds per side, until complete (index sum zero). Breakpoints closer than 10⁻⁶ are
  merged, their jumps added.
- C is evaluated by B1387's Morse count at the midpoint of every arc. Every change of C between neighbouring arcs must equal the
  predicted jumps between them.
- Cross-check on 720 equally spaced directions, on V's circle in dimension 2 and on the three coordinate planes in dimension 3: every
  direction farther than 10⁻³ from a breakpoint shows its arc's value.
- A failed check makes the member unresolved.

## BANKED IDENTITY:

Before any census number is read, the pipeline must reproduce the following inside itself. If any part fails, the run stops and
nothing below is read.
- **cube~3.24.** The generalised solve on its one-dimensional cuspidal space reproduces B1387:
  - C = +2 on B1387's generator v₊ (−2 on −v₊);
  - the leading shells: the first hexagonal shell at cusps 0 and 3, one direction at cusp 1, the √3-shell at cusp 2.
- **The breakpoint machinery,** re-run inside the pipeline on the design-time synthetic shells: no mismatch with the Morse count.
- **The linear-feasibility machinery.** On synthetic count functions: one built to realise the target at g = 3 must be found
  feasible, with the found L re-verified; one with a required jump removed must be infeasible.
- **B1398's target pattern,** recomputed from the record's vectors: the six classes and t at g = 3.

## Predictions, sealed

- **P1 (the kill test).** Does any resolved census member realise the three-generation pattern (g = 3)?
  - **NONE.** On the census, the rank-two escape is closed for three generations. The next escape is B1372's door-2 residual or
    independent walls, each with 27 matter.
  - **SOME.** The first three-generation, anomaly-free, exotic-free spectrum from the frame's own rule, on a named member with a named
    Higgs pair. That is not a derivation: the pair is chosen, the 27 matter's origin is unpaid, and the count's physical reading still
    needs sL-8's completion. 0 of 19 stays.
  - **Prior: NONE, about 85%.** The target needs |C| = 6 and at least 36 breakpoints on one circle, on covers with at most five cusps;
    78 of the 109 have one or two.
- **P2 (open).** Does any resolved member realise the pattern for some g ≠ 0 (any number of generations)? Prior NONE, about 60%.
- **P3 (read).** Per member: the maximum |C| on the circle (or on the sampled planes), the number of breakpoints, and the achievable g.

## Fences

- **The frame.** F27+78, or F133 with the Higgs field in the (Y, γ) plane. The 27 matter's origin (the E₇ frame, or localised E₇
  points) is not derived.
- **The Higgs field.** Cuspidal classes only, the dynamical Higgs field of B1395; sealed-cusp classes are fixed boundary data and are
  excluded. Rank two exactly; t-directions and rank three are outside. Stable realisations only.
- **The count.** The frame's rule, the far-up signed zero count (B1388 Theorem A). Its physical reading needs sL-8's completion
  (B1392–B1397). Doublets are 0 by Lemma A.
- **Symmetry.** None is imposed. Covers of degree ≤ 3 of the 99 only; larger covers, cube~3.24's covers and the class's other
  members are outside.
- **Numerics.** The count is read from numerical harmonic forms. The guards are the two-seed agreement, the jump accounting, the grid
  cross-check and a direct re-verification of any positive. An arc narrower than the solve can resolve remains a risk.

## PRIOR ART:

- **The design-time sweep.** `git grep` on main (`987c0c8f`) and the audit lane (`aff8a569`), both fetched 2026-09-28, and on this
  branch, for "rank-two Higgs", "two independent (harmonic|Higgs|cuspidal)", "rank-one Higgs", "Higgs pair", "angle map",
  "breakpoint" and variants. The hits are the MSSM's Higgs pair (H_u, H_d), unrelated Mahler-measure breakpoints, and this branch's
  B1393 "rank-one Higgs twist" scope.
- **This branch.**
  - B1386 and B1387 (the harmonic form and its count, cube~3.24);
  - B1388 (Theorem A; the count's stability);
  - B1389 (the rank-one frames);
  - B1392–B1397 (ends and completions);
  - B1398 (the verdict and the target pattern).
- **Main and the audit lane.** Nothing on a rank-two abelian Higgs in this frame, or on a count function's breakpoints.
- **The literature.** Hejhal's method for automorphic forms, Morse counts of harmonic 1-forms, and the critical points of an angle
  map (Poincaré–Hopf) are standard.
