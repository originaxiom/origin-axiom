# Stage 2 external constraints design (v1)

Status and scope.  
This memo describes how external-style constraints will interface with the Stage 2 diagnostic belts and the obstruction-program interpretation. It is a design document only: no new code, parameters, or data files are introduced here. The goal is to specify how late-time expansion constraints, early-structure requirements, and host consistency checks could be encoded as downstream filters on existing Stage I and Stage 2 artefacts, while respecting Phase 0 governance and the non-canonical status of Stage 2.

Position in the stack.  
Stage 2 currently consists of internal diagnostic belts: FRW corridors, mechanism and measure analysis, joint mech–FRW correlations, FRW data probes, and a θ* diagnostic rung, together with synthesis and verdict documents. The obstruction-program memos describe how these belts can be read as tests of static θ corridors and kernels, without altering any phase contracts. External constraints add a further layer on top of this: they are intended to encode, in simplified form, the demands imposed by realistic cosmology on expansion histories and structure formation, without turning Stage 2 into a full data-fitting pipeline.

Design principles.  
Any external-constraints belt added to Stage 2 should satisfy the following principles:
- Downstream only: it reads Stage I and Stage 2 outputs (for example FRW tables and mechanism-derived scalars), and optionally host-level outputs from future Stage II modules, but does not modify those artefacts.
- Corridor-based: it encodes external knowledge as corridors or boxes in observable or effective-parameter space, rather than as best-fit points or detailed likelihoods.
- Transparent: the definition of each corridor (its variables, bounds, and justification) is written out in plain language and simple formulae, with references to the underlying literature where appropriate.
- Reproducible: each external filter is implemented via a documented script that takes existing CSV tables or host outputs as input and produces new CSV tables with explicit pass/fail flags and summary statistics.
- Non-promotional by default: passing an external filter does not automatically promote any Stage 2 result into a phase paper or claims table. Promotion, if any, requires separate rungs and gates.

External corridor families.  
For the purposes of this branch, external constraints are organised into three conceptual families:

1. Late-time expansion corridors.  
   These corridors encode simple requirements on the late-time expansion history of the universe. Examples include:
   - Effective equation-of-state constraints expressed in a reduced parameterisation such as (w0, wa), with allowed regions chosen to reflect current survey results while leaving room for modest evolution.
   - Bounds on the Hubble expansion rate H(z) over a low-redshift range, expressed as inequalities relative to a reference curve.
   - Constraints on the present-day age of the universe and its consistency with independent probes.
   In Stage 2 terms these would be implemented as functions of FRW scalars already present in Phase 4 outputs or derived from them, assigning flags such as passes_w0wa_box, passes_Hz_corridor, and passes_age_bound for each θ on the grid.

2. Early-structure-friendly corridors.  
   These corridors encode the requirement that the expansion history and matter content allow early and efficient structure formation. In the present framework this will initially be treated at a coarse level, for example:
   - Age-of-universe constraints at selected high redshifts, ensuring that sufficient cosmic time is available for the observed early galaxies and massive structures to form.
   - Simple growth-of-structure proxies derived from the background history (for example approximate growth factors or growth indices), constrained to stay within a band around a reference model.
   The first implementation is expected to use age-based bounds only, with more refined growth proxies deferred to later work or external host modules. Stage 2 external-constraints scripts would annotate each θ with flags such as passes_highz_age_bound and, later, passes_growth_proxy_box.

3. Host consistency corridors.  
   These corridors govern the comparison between obstruction-inspired FRW models and external host solvers or cosmology codes, once Stage II host interfaces exist. They summarise, in compact metrics, how closely a given θ-point matches host-level predictions for quantities such as age, H(z), and derived distance measures. Examples of metrics include:
   - Fractional differences in age at z = 0 and selected higher redshifts,
   - Fractional differences in H(z) sampled over a redshift grid,
   - Simple root-mean-square misfits between toy FRW and host curves.
   Host consistency corridors are not about fitting data directly; they measure whether the obstruction-inspired background histories can be embedded into standard cosmological codes without obvious pathologies.

Data model and outputs.  
When implemented, an external-constraints belt would operate primarily at the level of CSV tables. A representative workflow would be:
- Inputs:
  - A Stage 2 table that already carries θ, FRW scalars, and internal diagnostic families (for example a joint mech–FRW table or a refined FRW summary table).
  - Optionally, host-level summary tables produced by Stage II modules.
- Processing:
  - For each corridor family, compute the relevant derived quantities (for example effective w0, wa; ages at selected redshifts; host comparison metrics).
  - For each corridor, apply a simple pass/fail rule defined in terms of these quantities.
- Outputs:
  - A new Stage 2 table with added boolean or categorical columns indicating whether each θ-point passes each corridor, together with summary rows or separate summary tables giving the sizes and fractions of surviving sets.

Interpretation for the obstruction program.  
From the obstruction-program perspective, external corridors are additional filters on static θ corridors and kernels. A θ-band that survives internal Stage 2 diagnostics but is excluded by all reasonable external corridors would count as evidence against the corresponding obstruction variant. Conversely, a small but structured kernel that survives both internal and external filters would be a candidate obstruction-compatible set, subject to the usual robustness checks. In all cases the interpretation remains static: the focus is on the existence and structure of allowed θ regions, not on dynamical θ trajectories.

Governance and future work.  
This design memo does not introduce any concrete corridor definitions, numerical bounds, or host interfaces. It records the intended structure of a future Stage 2 external-constraints belt and its relation to the obstruction-program memos, the Stage 2 testing spine, and the Stage 2 master verdict. Before any specific external corridor is implemented the following steps will be required:
- A short design note specifying the corridor in detail (variables, bounds, and motivation).
- A script implementing the corridor as a downstream filter on existing tables.
- A documentation update describing how the new corridor interacts with the obstruction-program interpretation and Stage 2 synthesis.

Only after those steps, and subject to Phase 0 style gates, would the outputs of an external-constraints belt be eligible for promotion into phase-level text. Until then, external constraints remain a planned extension of the existing diagnostic stack, not an active part of the Origin Axiom Stage I contract.

---

## Initial external-style corridor menu (design-only, v1)

This section records a first-pass menu of external-style corridors that could be applied to the static FRW pre-data kernel and its families in future obstruction rungs. All items are design-only: no thresholds, parameter values, or data sources are fixed here. Any concrete implementation will require separate, tightly scoped rungs and Phase 0–style gates.

### 1. Late-time expansion corridor (LT-corridor)

Intent.  
Capture the idea that viable cosmologies should sit inside a band of late-time expansion histories compatible with external measurements (for example effective dark-energy density or equation-of-state behaviour), without yet committing to specific observational numbers.

Design sketch.  

- Work at the level of FRW scalars already present in the Phase 4 masks:
  - `E_vac`, `omega_lambda`, `age_Gyr`, and any derived late-time summary scalars we choose to add in future rungs.
- Define a corridor \(\mathcal{C}_{\mathrm{LT}}\) as a bounded region in a small set of such scalars, e.g. a box or smooth window in \((E_{\mathrm{vac}}, \omega_{\Lambda})\) and possibly a loose constraint on `age_Gyr`.
- Require that:
  - the corridor is specified by explicit inequalities on documented columns,
  - the logical definition and any parameter choices are recorded in a dedicated design+gate doc,
  - the resulting mask is implemented as a separate Stage 2 helper over the static kernel (not by changing Phase 4 masks directly).

Future work.  
Later rungs can:
- propose concrete ranges for \(\mathcal{C}_{\mathrm{LT}}\) informed by external FRW fits,
- implement an explicit `lt_corridor` flag over `stage2_obstruction_static_frw_kernel_v1.csv`,
- study intersections such as kernel ∩ LT-corridor and kernel ∩ LT-corridor ∩ LCDM-like.

### 2. Early-age corridor (EA-corridor)

Intent.  
Introduce a simple way to encode the idea that the Universe must be “old enough” at given redshift or in aggregate, without yet building a full high-redshift data pipeline.

Design sketch.  

- Use `age_Gyr` from the Phase 4 FRW tables as a coarse proxy for age constraints.
- Define a corridor \(\mathcal{C}_{\mathrm{EA}}\) as a lower-bound–type condition on `age_Gyr` (or on a future derived early-age proxy) that is:
  - loose enough to be uncontroversial at the design stage,
  - clearly documented as a one-sided constraint in θ-space.
- Treat any later use of more refined age information (for example redshift-dependent age or high-redshift structure ages) as a separate Stage 2 or Stage II module, not as a retrofit to this corridor.

Future work.  
Later rungs can:
- decide whether a single global age cut is adequate or whether a small family of cuts is needed,
- implement an `early_age_ok` flag in a Stage 2 helper and compare kernel vs non-kernel behaviour under this cut,
- test whether any putative “sweet spot” θ-region survives EA-corridor tightening.

### 3. Structure-friendly corridor (SF-corridor)

Intent.  
Provide a slot for constraints motivated by the existence and timing of structure (for example that the vacuum sector and expansion history must allow galaxies and clusters to form early enough), again at the design level only.

Design sketch.  

- Conceptually tie this corridor to combinations of:
  - vacuum energy scale (through `E_vac` or `omega_lambda`),
  - age information (`age_Gyr` or future derived columns),
  - and potentially simple summary proxies for growth (to be added in later rungs).
- Define \(\mathcal{C}_{\mathrm{SF}}\) as a region in this reduced parameter space where structure formation is judged “plausible enough” by external arguments, without encoding a full Boltzmann or N-body pipeline.
- Make clear that:
  - any concrete parameterisation (for example informal “too fast / too slow expansion” bands) is provisional,
  - promotion into phase-level claims will require stronger justification or dedicated structure-focused work.

Future work.  
Later rungs can:
- propose one or more SF-corridor candidates with explicit inequalities,
- implement a `structure_friendly` flag in Stage 2 helpers,
- study intersections such as kernel ∩ LT-corridor ∩ SF-corridor, and how these compare to the LCDM-like and toy corridor families.

### 4. Host-consistency filters (HC-filters)

Intent.  
Prepare for Stage II “cosmo hosts” by sketching simple host-consistency filters that operate on the static kernel and its families, expressing questions like “does this θ-region admit host scenarios that look broadly like ours?”.

Design sketch.  

- Treat hosts (galaxies, environments, or observer-like configurations) as labels on subsets of θ rather than as new parameters encoded directly in the FRW masks.
- Define HC-filters as boolean tags over θ, such as:
  - `admits_host_type_X`,
  - `admits_host_with_property_Y`,
  - where the semantics of X and Y are recorded in Stage II host design docs (`docs/STAGEII_COSMO_HOSTS_DESIGN_v1.md` and descendants).
- Initially, interpret HC-filters as thought experiments or scenario labels, not as data-driven exclusions.

Future work.  
Later rungs can:
- define a small set of host scenarios with explicit, reproducible criteria,
- implement host-style flags as additional columns over the static kernel,
- ask obstruction-style questions about which θ-regions survive simultaneous FRW and host-consistency filters.

### 5. Gating principles

Across all external-style corridors and filters, the following principles apply:

- Design-first: corridors are first specified in design docs with clear logical definitions and intended use, before any code is written.
- Stage-2-only implementation: any concrete corridor is implemented as a Stage 2 helper over existing artifacts, not by modifying Phase 3/4 pipelines or masks.
- Explicit promotion gates: any use of external-style corridors in phase papers or claims requires:
  - separate, tightly scoped promotion rungs,
  - explicit Phase 0–style gates,
  - and updates to the relevant Phase and Stage 2 docs.
- θ-neutrality: corridors should be chosen and documented in a way that does not implicitly hard-wire any preferred θ value; any apparent θ preference must emerge from the filters, not from their construction.

This menu is a living design sketch. Future rungs can refine, split, or retire corridor candidates as the obstruction program and Stage II hosts become more concrete.
