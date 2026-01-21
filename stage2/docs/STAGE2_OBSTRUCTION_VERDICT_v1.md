# Stage 2 obstruction verdict (v1)

Status: internal Stage 2 diagnostic only. This document does not modify any Phase 0–5 contracts, claims, or promotion gates.

## 1. Scope

The obstruction program asks a concrete question:

> Given the current Phase 3 mechanism module and Phase 4 FRW toy pipeline, does anything in the combined stack make it hard or impossible to maintain a nonzero "no-cancellation floor" once we enforce reasonable FRW- and host-style corridors?

This document summarises what the *current* Stage 2 obstruction helpers say about that question. It draws only on:

- the locked Phase 3 and Phase 4 artifacts,
- the Stage 2 FRW corridor and joint mech–FRW belts,
- and the new obstruction helpers built in the obstruction-program branch.

It records what we *see* and what we explicitly *do not claim* yet.

## 2. Inputs used in this verdict

The verdict is based on the following Stage 2 artifacts (all reproducible from the repo):

- Static FRW kernel and families:
  - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_v1.csv`
  - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_families_v1.csv`
- Internal toy corridors:
  - FRW corridor belt outputs under `stage2/frw_corridor_analysis/outputs/tables/`
  - LCDM-like band and shape masks from:
    - `phase4_F1_frw_lcdm_probe_mask.csv`
    - `phase4_F1_frw_shape_probe_mask.csv`
  - Toy late-time corridor from the LCDM box:
    - `stage2_obstruction_toy_lt_corridor_from_lcdm_box_v1.csv`
    - `stage2_obstruction_toy_lt_corridor_from_lcdm_box_summary_v1.csv`
- External-style corridors:
  - External age corridor v2:
    - `stage2_obstruction_external_age_corridor_v2.csv`
    - `stage2_obstruction_external_age_corridor_summary_v2.csv`
  - External late-time corridor v1:
    - `stage2_obstruction_external_lt_corridor_v1.csv`
    - `stage2_obstruction_external_lt_corridor_summary_v1.csv`
  - External age+expansion+structure corridors v1:
    - `stage2_obstruction_external_age_expansion_corridors_v1.csv`
    - `stage2_obstruction_external_age_expansion_summary_v1.csv`
- Mechanism overlay and summaries:
  - Kernel with attached mechanism amplitudes:
    - `stage2_obstruction_kernel_with_mech_v1.csv`
  - Mechanism amplitudes under external corridors:
    - `stage2_obstruction_kernel_mech_vs_external_corridors_summary_v1.csv`
- Supporting design docs:
  - `docs/OBSTRUCTION_EMPIRICAL_PROGRAM_v1.md`
  - `stage2/docs/STAGE2_OBSTRUCTION_TESTING_SPINE_v1.md`
  - `stage2/docs/STAGE2_EXTERNAL_CONSTRAINTS_DESIGN_v1.md`
  - `stage2/docs/STAGE2_OBSTRUCTION_EXTERNAL_AGE_CORRIDOR_V2.md`
  - `stage2/docs/STAGE2_OBSTRUCTION_EXTERNAL_LT_CORRIDOR_V1.md`
  - `stage2/docs/STAGE2_OBSTRUCTION_EXTERNAL_AGE_EXPANSION_V1.md`
  - `stage2/docs/STAGE2_OBSTRUCTION_KERNEL_WITH_MECH_V1.md`.

Any future change to this verdict must go through updated versions of these artifacts or new, clearly documented ones.

## 3. What we see in FRW space

3.1 Pre-data FRW kernel.

- The FRW viability mask carves out a **pre-data kernel** that occupies roughly half of the theta grid (about 1000 out of 2048 points).
- Sanity checks like "has matter era" and "smooth H^2" are always satisfied in the current snapshot; the nontrivial cut is the late-acceleration condition.
- The aggregate FRW data flag is currently always false, so all corridors are interpreted as **pre-data** corridors. No real data gate is open yet.

3.2 Internal toy corridors.

Within this pre-data kernel:

- The FRW toy corridor and LCDM-like band define structured subfamilies similar to those in the original Stage 2 FRW corridor belt.
- A simple late-time corridor built from the LCDM box selects an internal **toy late-time corridor** inside the kernel.
- The intersection of:
  - the pre-data kernel,
  - the LCDM-like island,
  - the toy FRW corridor,
  - and the toy late-time box
  remains **non-empty**. In the current snapshot this "sweet subset" consists of a small number of points (order 10^1), not a single spike and not a vanishing set.

3.3 External-style corridors (toy v1/v2).

We then add simple external-style corridors:

- A nontrivial age band (external age corridor v2) selects a subset of the kernel compatible with a late-time universe of order fourteen billion years old.
- A late-time corridor v1 mirrors the current LCDM-like island but is treated as an external-style helper.
- Age+expansion+structure corridors v1 add simple, host-inspired proxies:
  - broad and tight age bands,
  - broad and tight expansion boxes,
  - basic structure-friendly proxies (combinations of age and expansion that roughly correspond to "enough time and not too extreme vacuum").

Under these helpers:

- The **kernel remains non-empty** after each individual corridor.
- Combining the nontrivial age band with the internal toy corridor and the LCDM-like band still leaves a **40-point sweet subset**.
- Tight age+expansion+structure proxies reduce the kernel to a few dozen points but do not collapse it; viable points survive.

These corridors are deliberately simple and are not fits to real data. They are meant to check whether the current FRW toy backbone can survive nontrivial host-style filters without collapsing.

## 4. What we see in mechanism amplitudes

Using the joined kernel+mechanism table and the mechanism-under-corridors summary, we can compare the behaviour of the Phase 3 amplitudes in different families:

- On the **full grid** the mechanism amplitudes span a modest range.
- On the **pre-data kernel** this range is already narrower: amplitudes cluster in a band well above zero.
- On the **40-point sweet subset** (kernel, LCDM-like, toy FRW corridor, age v2) the amplitudes concentrate further into a narrow band, still comfortably away from zero.
- On the **tight age+expansion+structure subset** the amplitudes again live in a narrow band similar in scale to the sweet subset, not driven towards zero and not wildly fluctuating.

In other words:

- The current external-style corridors carve out small, structured subsets in FRW space.
- Within those subsets the mechanism amplitudes behave **smoothly** and remain **nonzero**.
- There is no sign that tightening these first corridors, in this toy setup, forces the mechanism towards exact cancellation or an obviously pathological regime.

At the same time:

- We do **not** yet see a sharp, corridor-driven selection of a single theta value or a tiny cluster that would stand out as an obvious "fixed point" of the obstruction picture.
- The sweet subset is small but not a spike; it is still a patch of the kernel.

## 5. What this does and does not say about forbidden cancellation

5.1 Positive statements (internal to the toy stack).

Within the current Phase 3 / Phase 4 / Stage 2 stack:

- The mechanism module and the FRW toy pipeline are **compatible** with a nonzero floor under a range of simple host-style filters.
- Internal FRW viability, a toy late-time corridor, a nontrivial age band, and simple expansion/structure proxies can all be imposed **without collapsing** the kernel or forcing the amplitudes to zero.
- The 40-point sweet subset is a concrete object:
  - it sits inside the pre-data kernel,
  - it respects the internal FRW filters and the LCDM-like band,
  - it survives a nontrivial age band,
  - and it carries smooth, nonzero mechanism amplitudes.

This is **evidence of viability** for the obstruction program inside the current toy stack: nothing in these first external-style corridors obstructs a nonzero floor.

5.2 Explicit non-claims.

At the same time we explicitly *do not* claim:

- that any of the current external-style corridors are realistic fits to data,
- that the 40-point sweet subset is physically preferred or unique,
- that the current amplitudes define a canonical measure on theta,
- or that the obstruction program has been confirmed as a statement about the actual universe.

All conclusions here are **internal** to the present Phase 3 / Phase 4 snapshot and the particular toy corridors we have encoded.

5.3 What would be needed for a genuine obstruction claim.

A genuine, publishable "forbidden cancellation" statement would require something much stronger, for example:

- a small, well-motivated family of **external corridors** tied to:
  - late-time expansion and age bounds,
  - early structure formation,
  - and host-level constraints (e.g. galaxies capable of producing long-lived observers),
- a demonstration that **any** choice of corridors in this family that keeps host-like universes non-empty also enforces a **strictly positive lower bound** on the mechanism floor (independent of fine tuning of theta),
- and an analysis showing that this lower bound is stable under reasonable variations of the model and of the external corridors.

We are deliberately **not** there yet. The current verdict should be read as:

> The present Phase 3 / Phase 4 / Stage 2 stack can support a nonzero floor under simple, interpretable host-style filters without contradiction, but we have not yet demonstrated that such a floor is *forced* by any realistic external corridor family.

## 6. Next structured steps

The obstruction program continues along a few clear lines:

1. **Sharpen the external corridors** (design rung).
   - Move from toy bands (age v2, simple expansion boxes, basic structure proxies) to a small menu of external corridors with explicit motivation from cosmology and host arguments.
   - Encode these as separate Stage 2 helpers with clearly documented thresholds.

2. **Re-run the obstruction tests under sharpened corridors** (O3.x).
   - Rebuild the static kernel, the sweet subset, and the mechanism-overlay tables under the sharpened corridors.
   - Check whether the kernel and sweet subset remain non-empty and how the amplitudes behave.

3. **Clarify the role of special theta values**.
   - Use the existing theta-alignment diagnostics to check whether any sharpened corridor family produces a nontrivial selection effect near special values (including the value singled out in Phase 3).
   - Record negative results as explicitly as positive ones.

4. **Prepare for Stage II hosts**.
   - Keep obstruction results clearly separated as Stage 2 diagnostics.
   - Use them as input to Stage II host design (for example in `docs/STAGEII_COSMO_HOSTS_DESIGN_v1.md`), where host-level questions can be formulated in terms of the kernel and corridors rather than direct raw parameters.

Until those steps are completed, this verdict remains an internal Stage 2 snapshot: it says that the obstruction program is viable and nontrivial inside the current toy stack, but it does not yet promote any obstruction-flavoured statement into the locked phases.


---

## O2.3 – Floor and θ★ in the obstruction stack (2026-01-21)

This rung extends the obstruction verdict with two pieces of quantitative evidence
from the current Stage 2 stack:

1. **Non-cancellation floor vs external corridors.**

   Using the joined kernel–mechanism table
   (`stage2_obstruction_kernel_with_mech_v1.csv`) and a simple non-cancellation
   floor on the binding amplitude,
   \[
     \text{floor\_v1}:\ \ \texttt{mech\_binding\_A0} \ge 0.045,
   \]
   we find:

   - `KERNEL_AND_FLOOR_V1`: 894 out of 1016 pre-data kernel points survive the
     floor (≈ 0.88 of the kernel).
   - `KERNEL_AGE_TIGHT_EXP_STRUCT_TIGHT_AND_FLOOR_V1`: 49 kernel points
     (≈ 0.048 of the kernel) survive simultaneously:
       - the tightened age band (`EXTERNAL_AGE_CORRIDOR_V2`),
       - the tightened expansion + structure proxies
         (`EXPANSION_TIGHT_V1`, `STRUCT_PROXY_TIGHT_V1`),
       - and the non-cancellation floor.
   - `KERNEL_SWEETLIKE_AND_FLOOR_V1`: 32 kernel points (≈ 0.031 of the kernel)
     survive inside the 40-point “sweetlike” intersection region and the same
     floor.

   In all three families the six Phase 3 amplitudes
   (`mech_baseline_*`, `mech_binding_*`) are tightly clustered; in particular,
   the binding amplitude sits in a narrow band around
   \(\texttt{mech\_binding\_A0} \sim 0.046\), well above zero. This shows that
   a strictly positive lower bound on the mechanism amplitude is compatible with
   non-empty, non-pathological subsets of the FRW kernel even under non-trivial
   (though still toy) external-style corridors.

   These results live in:

   - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_kernel_mech_vs_external_corridors_summary_v1.csv`
   - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_non_cancel_floor_vs_corridors_v1.csv`

2. **Status of θ★ in the obstruction stack.**

   We probe the θ★ ≃ φ^φ target (here fixed at
   `theta_star_target = 2.1784575679…`) against the same obstruction stack
   using the helper:

   - `stage2/obstruction_tests/src/analyze_theta_star_in_obstruction_stack_v1.py`
     → `stage2_obstruction_theta_star_in_stack_v1.csv`.

   In the current snapshot:

   - the nearest grid point is `theta ≈ 2.1782527` (index 710),
     with |Δθ| ≈ 2.0×10⁻⁴;
   - this point **is in** the pre-data FRW kernel;
   - it is **not** LCDM-like, **not** in the toy FRW corridor, and **not** in
     the tightened age/expansion corridors;
   - it does satisfy the broad age band and the basic structure proxy, and its
     binding amplitude lies comfortably above the non-cancellation floor
     (`mech_binding_A0 ≈ 0.0563`).

   In other words, θ★ is neither ruled out by the current obstruction stack
   nor singled out by it: it sits inside the broad kernel and above the floor,
   but is not picked out by the present toy external corridors.

**Verdict at O2.3.**

- The current Phase 3/4 + Stage 2 stack supports **non-empty, well-behaved
  subsets of FRW kernels that survive both a positive mechanism floor and
  simple external-style corridors**. Forbidden cancellation is therefore
  *compatible* with this snapshot; it is not trivially obstructed.
- At the same time, the stack does **not** yet produce a narrowly collimated,
  static θ corridor or a unique θ★ candidate. Any serious claim of a preferred
  θ★ or a sharply localised kernel will require:
  - sharper, data-driven external corridors (age + expansion + structure),
  - and a more principled non-cancellation floor tied to mechanism structure,
    not an ad-hoc scalar threshold.

Subsequent obstruction rungs (O3.x) are reserved for such sharpened,
externally-motivated corridors and for any future attempt to promote an
obstruction-flavoured statement into the phase papers under explicit Phase 0
gates.