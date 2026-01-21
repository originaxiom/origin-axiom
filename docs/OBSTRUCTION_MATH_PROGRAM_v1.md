# Obstruction math program (v1)

This memo frames the obstruction program in explicitly mathematical terms using only objects that already exist in the repo: the θ-grid, the FRW pre-data kernel and masks, and the Phase 3 mechanism amplitudes. It does not introduce new claims or promotion gates; it is a design document for future work that aims to turn the informal “forbidden cancellation” picture into precise, testable statements.

## 1. Setup and objects

We work on the fixed θ-grid used throughout Phase 3 and Phase 4, sampled at N = 2048 points with coordinates θ_i. On this grid we already have:

- FRW scalars: E_vac(θ_i), ω_Λ(θ_i), age_Gyr(θ_i).
- FRW masks: has_matter_era(θ_i), has_late_accel(θ_i), smooth_H2(θ_i), frw_viable(θ_i), lcdm_like(θ_i), toy corridor flags, and the derived static pre-data kernel flag kernel_pre_data(θ_i).
- External style corridor flags from the obstruction program: toy_LT_from_LCDM(θ_i), external_age_v2(θ_i), external_LT_v1(θ_i), and the age/expansion/structure proxy bands AGE_BROAD_V1, AGE_TIGHT_V1, EXPANSION_BROAD_V1, EXPANSION_TIGHT_V1, STRUCT_PROXY_BASIC_V1, STRUCT_PROXY_TIGHT_V1.
- Mechanism amplitudes from Phase 3, aligned with the same θ-grid via the joint mech–FRW table: mech_baseline_A0(θ_i), mech_baseline_A_floor(θ_i), mech_baseline_bound(θ_i), mech_binding_A0(θ_i), mech_binding_A(θ_i), mech_binding_bound(θ_i).

The Stage 2 obstruction helper `stage2_obstruction_kernel_with_mech_v1.csv` assembles these into a single table on the θ-grid, and `stage2_obstruction_kernel_mech_vs_external_corridors_summary_v1.csv` summarises how the amplitudes behave under various external-style corridors.

For the math program, we treat:

- The θ-grid as a discrete approximation to some underlying θ continuum.
- The kernel K as the set of θ-points where the pre-data FRW filters accept the model (currently ~50% of the grid).
- The “sweet subset” S as the intersection of K with a specific combination of external-style corridors (for example the 40-point set that survives the pre-data kernel, the toy LCDM-derived box, and the external age v2 band).
- The mechanism amplitudes as scalar fields A_j(θ) defined on the same grid, with A_floor(θ) encoding a candidate non-cancellation floor.

## 2. What “forbidden cancellation” should mean here

Informally, the obstruction idea is that reality never achieves exact cancellation of the relevant vacuum-like contributions: there is a non-zero residue that cannot be tuned away globally. On the θ-grid this should translate into statements of the following type:

1. Non-vanishing floor on a non-trivial set. There exists ε > 0 and a set S of θ-values with non-zero FRW weight (for example a subset of the pre-data kernel) such that for all θ in S we have A_floor(θ) ≥ ε. In words: once we restrict to θ that survive the FRW and external-style filters, the mechanism amplitude cannot be arbitrarily small everywhere.

2. Obstruction to global cancellation. There is no choice of θ in the kernel for which all relevant amplitudes simultaneously fall below some small threshold while also satisfying a specified bundle of FRW and external-style constraints. In words: if you insist on “good” FRW behaviour plus external corridors, you cannot make the mechanism arbitrarily invisible everywhere.

3. Structured residue rather than noise. On the surviving set S, the amplitudes behave in a controlled way (for example they are approximately monotone or have bounded variation in θ) and are strongly correlated with FRW scalars. This is closer to “structured obstruction” than to a random numerical leftover.

At the current Stage 2 obstruction level we are not in a position to prove strong statements of these forms. What we can do is:

- Construct explicit candidate sets S (pre-data kernel, sweet subsets under external bands).
- Measure the distribution of the existing amplitudes A_j(θ) on S (min, max, mean).
- Check whether current snapshots already show a non-trivial floor, or whether the amplitudes could in principle be tuned arbitrarily small without breaking the FRW and external filters.

## 3. What the current snapshot tells us

Using the Stage 2 obstruction helpers we have established that:

- The pre-data FRW kernel K is non-empty and contains roughly half the θ-grid.
- The external-style corridors we introduced (toy LCDM-derived box, external age v2 band, age and expansion proxies) carve K down to smaller but still non-empty subsets. In particular, there is a small “sweet subset” of order a few percent of the kernel (for example the 40-point intersection of kernel, LCDM-like, toy corridor and external age v2) that survives several filters at once.
- On K and on these subsets, the Phase 3 amplitudes are smooth and tightly distributed. The summary tables show that the minimum and maximum values of the six amplitudes on K and on the tighter subsets lie in narrow ranges, with no evidence of a pathological spike or collapse.
- Nothing in the current snapshot forces the amplitudes to zero on K or on the sweet subset S; at the same time, nothing in the current snapshot singles out a unique θ* or a unique θ-band as mathematically distinguished by the amplitudes alone.

At this stage the obstruction program has therefore produced:

- A concrete, non-empty pre-data kernel K in FRW space.
- A family of explicit, non-empty external-style corridors and their intersections with K.
- Evidence that the mechanism amplitudes behave smoothly and remain non-zero on these sets, but without a sharp lower bound or a unique θ singled out by the current diagnostics.

## 4. Gaps between this and a real obstruction theorem

To turn the above into something closer to a theorem or a reproducible claim about “forbidden cancellation” we would need at least:

1. A mathematically precise lower-bound condition. Instead of qualitative statements about non-zero amplitudes, we would need inequalities of the form A_floor(θ) ≥ ε on a non-trivial set S, with ε and S defined in terms of clear, reproducible thresholds (for example FRW viability plus age and expansion bands tied to explicit cosmological bounds).

2. A well-defined notion of allowable tuning. At present the obstruction tests are snapshots: they take the existing kernel and amplitudes as fixed and ask how they behave under added filters. A stronger statement would require specifying what kinds of deformations of the mechanism or FRW sectors are allowed and showing that no allowed deformation can drive all amplitudes below a small threshold on S.

3. A clear limiting procedure. The θ-grid is finite and coarse. Any strong obstruction statement should specify whether it is meant only at this resolution or in a limiting sense as the grid is refined. In the latter case we would need to control how K and the amplitudes behave under refinement.

4. Connection to observational corridors. The current external-style corridors are deliberately simple and internal. A serious obstruction program must decide which external constraints to regard as part of the kernel definition (for example age bounds, late-time expansion bands, structure proxies) and must tie their thresholds, at least qualitatively, to observational arguments.

Until these elements are in place, the obstruction program remains a structured diagnostic: it shows that the current mechanism and FRW stack support non-empty, non-degenerate corridors under a set of internal and semi-external filters, but it does not yet deliver a mathematically sharp “no full cancellation possible” statement.

## 5. Near-term rung plan from the obstruction perspective

Given the current repo state, a realistic near-term plan is:

- O4.1 – Threshold design. Define a small set of candidate thresholds for age, expansion, and structure proxies that are motivated by simple external arguments (for example conservative age bounds and broad late-time expansion boxes) and implement them as explicit parameters in the Stage 2 obstruction helpers.

- O4.2 – Floor diagnostics. Using `stage2_obstruction_kernel_with_mech_v1.csv`, explicitly measure, for each candidate sweet subset S, the minimum and distribution of A_floor and related amplitudes. Check whether a sensible ε can be extracted that is stable under small variations of the external thresholds.

- O4.3 – Robustness sweeps. For a few nearby choices of external thresholds, scan how the size of S and the amplitude floors change. Record whether there is a regime where the corridors remain non-empty and the amplitude floor remains clearly bounded away from zero.

- O4.4 – Snapshot obstruction statement. If such a regime exists, crystallise it into a careful, Phase 0 style statement: not yet a theorem, but a reproducible summary such as “under these thresholds, the pre-data kernel plus external corridors cannot make the mechanism amplitude arbitrarily small everywhere on S”.

All of these rungs live in Stage 2 obstruction land; they do not alter any Phase 0–5 contracts or promotion gates. Any attempt to promote a “forbidden cancellation” flavoured statement into a phase paper would come only after these diagnostics are stable and would require its own gate and alignment check.

## 6. Relation to the existing phases

In the current stack:

- Phase 3 provides the mechanism amplitudes and the non-cancellation floor ansatz.
- Phase 4 provides the FRW masks and the pre-data kernel.
- Stage 2 provides the diagnostic belts and the obstruction helpers that combine amplitudes, kernel, and external-style corridors.

The obstruction math program sits on top of this structure. Its job is not to redefine the phases but to ask, given the locked Phase 3 and Phase 4 setup and the Stage 2 diagnostics, what kinds of mathematically explicit “no full cancellation” statements are even on the table, and what additional work is required to make any of them precise enough to be worth locking.

