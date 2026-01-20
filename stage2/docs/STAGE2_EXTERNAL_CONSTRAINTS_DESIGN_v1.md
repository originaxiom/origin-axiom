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
