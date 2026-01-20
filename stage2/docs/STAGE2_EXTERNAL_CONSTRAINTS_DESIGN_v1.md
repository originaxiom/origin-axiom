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

---

## 3. Prioritised external-style corridor menu (v1)

This section lists a small, prioritised set of external-style corridors that are natural next steps for the obstruction program. Each item is a design-only target: no thresholds are fixed here and no code is implied yet. The aim is to define *what kind of question* each corridor will ask of the existing FRW kernel and sweet subset.

### 3.1 Late-time expansion corridor (LCDM-adjacent box)

Type.  
- A corridor in the effective late-time expansion plane, phrased in terms of vacuum-sector scalars that are already present in the Phase 4 masks (for example \(E_{\text{vac}}\) and \(\omega_\Lambda\)), but interpreted as an approximation to an external late-time constraint rather than a purely internal mask.

Motivation.  
- The static FRW kernel already supports:
  - a broad pre-data viable band,
  - a narrow LCDM-like band,
  - a toy late-time corridor derived from the LCDM box and the FRW toy corridor.
- The 40-point sweet subset sits at the intersection of these ingredients. A real late-time corridor should ask whether this region remains nonempty once we move away from purely internal bands.

Design sketch.  
- Start from:
  - existing internal LCDM-like region and FRW toy corridor in \((E_{\text{vac}}, \omega_\Lambda)\),
  - external information about plausible late-time expansion behaviour,
  - and the principle that any external corridor should not be fine-tuned directly to the current 40-point subset.
- Define:
  - a small family of candidate boxes or bands in the \((E_{\text{vac}}, \omega_\Lambda)\) plane that are:
    - interpretable as “late-time expansion consistent with external constraints,”
    - broad enough to avoid overfitting the current snapshot,
    - auditable in terms of how they map onto the pre-data kernel, LCDM-like band, FRW toy corridor, and the sweet subset.
- For each candidate corridor we will later ask:
  - Does the kernel remain nonempty?
  - Does the 40-point sweet subset survive, shrink, move, or disappear?
  - How sensitive are the answers to modest changes in the box boundaries?

Standards.  
- External-style corridors here must be defined in terms of quantities that could, in principle, be calibrated to data, even if this rung does not yet perform that calibration.
- Thresholds must be chosen by simple external arguments or bands, not by tailoring them to preserve the current sweet subset.

### 3.2 Age corridor (refining the toy band)

Type.  
- A corridor in the cosmic age scalar `age_Gyr`, tightening the broad `[10, 20]` Gyr toy band into a more realistic, obstruction-style age filter.

Motivation.  
- The toy external age corridor `[10, 20]` Gyr shows that the machinery for external-style scalar bands works and currently behaves as a structural no-op: it preserves the entire pre-data kernel, the LCDM-like band, the FRW toy corridor, and the 40-point sweet subset.
- The next natural step is to move from:
  - “age band wide enough to test the machinery,” to
  - “age band narrow enough to actually challenge parts of the kernel,” while remaining defensible as an external-style choice.

Design sketch.  
- Define a family of candidate age bands of the form:
  - \([t_{\min}, t_{\max}]\) Gyr with \(t_{\min}\) in a realistically motivated range (for example, comfortably below current best estimates of the cosmic age) and \(t_{\max}\) relaxed enough to avoid artefacts from the toy FRW setup.
- For each candidate band we will later examine:
  - fraction of the pre-data kernel that survives,
  - survival or collapse of the LCDM-like band,
  - behaviour of the 40-point sweet subset.
- The goal is not to tune an “optimal” band, but to understand which age corridors, if any, genuinely obstruct the current kernel or sweet subset.

Standards.  
- Age bands should be justified by simple, external-style arguments (for example: “definitely too young,” “comfortably consistent with observed ages”), not by post-selection on the current kernel.
- Any corridor that completely empties the kernel must be flagged explicitly as an “obstruction candidate” and subjected to additional robustness checks before being taken seriously.

### 3.3 Structure-friendly corridor (early-structure proxy)

Type.  
- A corridor that proxies “early-structure-friendly” behaviour, for example via a very simple diagnostic derived from the FRW setup (or a later extension) that tracks whether the background is compatible with forming long-lived, structured hosts.

Motivation.  
- The obstruction program ultimately cares about whether a given θ value admits host-level structure at all, not just late-time expansion and age.
- A first, crude structure-friendly corridor can serve as a placeholder for more detailed Stage II host work and as a way to test whether the existing kernel is obviously incompatible with even minimal structure requirements.

Design sketch.  
- Identify a small number of FRW-derived scalars or flags that might correlate with structure-friendliness in a very weak sense (for example, the presence of a matter era and qualitatively reasonable expansion history over a broad time range).
- Define simple corridor conditions (for example, “satisfies a minimal set of structural sanity flags”) and apply them to the static kernel.
- Record:
  - how many kernel points survive,
  - how this interacts with the LCDM-like band, the FRW toy corridor, and the 40-point sweet subset.

Standards.  
- This corridor must be clearly marked as a **proxy** for structure friendliness, not as a realistic model of galaxy or host formation.
- Any interpretation in terms of real hosts will be deferred to Stage II and to separate, more detailed host design documents.

### 3.4 Gating and versioning

For each external-style corridor that moves beyond the current toy level:

- A separate design rung will:
  - specify the chosen thresholds or inequalities and their justification,
  - implement the corresponding helper script and summary tables,
  - record the impact on the pre-data kernel, the LCDM-like band, the FRW toy corridor, and the 40-point sweet subset.
- A follow-up verdict rung will decide whether the new corridor:
  - is kept as an internal diagnostic only, or
  - is serious enough to be recorded as an “obstruction candidate” in the Stage 2 verdict.
- Any promotion of external-style results into phase-level text will require Phase 0–style gates and updates to the relevant Phase 4/5 documents; this memo remains strictly at the Stage 2 design level.

---

## 3. External-style age and expansion corridors v1 (design rung EXT-DESIGN-1)

This section records a first sharpened set of external-style corridors in FRW scalar space, intended as Stage 2 diagnostic helpers applied to the static FRW kernel in `stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_v1.csv`. They are not data fits and do not modify any Phase 4 FRW masks or Stage 2 promotion gates; they are structured bands that encode “reasonable” ages and vacuum sectors informed by current cosmological inferences.

All corridors below are defined on the 2048 point θ grid with columns `theta`, `E_vac`, `omega_lambda`, and `age_Gyr`, together with the pre-data kernel flag used elsewhere in the obstruction program.

### 3.1 Age corridors

We define two age-based external-style corridors in terms of `age_Gyr`:

- `AGE_BROAD_V1`: a broad, physically sane age band,
  - definition: `11.5 <= age_Gyr <= 15.0`,
  - motivation: rules out very young universes that would struggle to host old stellar populations and very old universes that are in strong tension with standard ΛCDM age estimates, while leaving generous room around current best-fit ages.
- `AGE_TIGHT_V1`: a tighter, ΛCDM-like age band,
  - definition: `13.0 <= age_Gyr <= 14.2`,
  - motivation: centered around ≈ 13.8 Gyr with enough slack for moderate shifts, intended to represent “broadly ΛCDM-consistent” ages without tying to any specific dataset.

In later implementation rungs these corridors will be represented as boolean columns `age_broad_v1` and `age_tight_v1` on the static kernel table, and summary tables will always report:

- total grid fraction and kernel fraction for each band, and
- overlaps with the existing FRW toy corridor, LCDM-like band, and the 40 point sweet subset used elsewhere in the obstruction program.

### 3.2 Expansion corridors in {E_vac, omega_lambda}

We likewise define two external-style corridors in the vacuum sector using the existing `omega_lambda` and `E_vac` columns. The intent is to distinguish background cosmologies where dark energy is dynamically relevant but not absurdly small or overwhelmingly dominant.

- `EXPANSION_BROAD_V1`:
  - definition:
    - `0.55 <= omega_lambda <= 0.85`, and
    - `E_vac` between the 5th and 95th percentiles of `E_vac` restricted to the pre-data kernel,
  - motivation: captures a wide range of dark energy fractions that remain qualitatively “ΛCDM-like” while excluding extremely small or extremely large vacuum densities relative to the present kernel.

- `EXPANSION_TIGHT_V1`:
  - definition:
    - `0.62 <= omega_lambda <= 0.78`, and
    - `E_vac` between the 10th and 90th percentiles of `E_vac` in the pre-data kernel,
  - motivation: narrows in on a strip in vacuum sector space that tracks current ΛCDM-like expectations more closely while still allowing modest shifts and avoiding hard-coded single values.

In implementation rungs these will be represented as boolean columns `expansion_broad_v1` and `expansion_tight_v1` on the same static kernel table, with summary tables tracking their grid and kernel fractions and their intersections with the FRW toy corridor, LCDM-like band, age bands, and the 40 point sweet subset.

### 3.3 Simple “structure-friendly” proxy corridors

Without a full structure formation model, we restrict ourselves to a primitive structure-friendly proxy based on FRW phase structure and timescales:

- require:
  - `has_matter_era == 1`,
  - `smooth_H2 == 1`,
  - `frw_viable == 1`,
  - together with age and expansion bands.

We define two proxy corridor families to be implemented as intersections of existing flags and the bands above:

- `STRUCT_PROXY_BASIC_V1`:
  - definition: points in the pre-data kernel satisfying
    - `frw_viable == 1`,
    - `has_matter_era == 1`,
    - `smooth_H2 == 1`,
    - and `AGE_BROAD_V1`,
  - interpretation: FRW backgrounds that have a clean matter era, smooth expansion, and a broadly reasonable cosmic age, treated as a minimal proxy for “could plausibly host long-lived structure” on toy grounds.

- `STRUCT_PROXY_TIGHT_V1`:
  - definition: points in the pre-data kernel satisfying
    - `frw_viable == 1`,
    - `has_matter_era == 1`,
    - `smooth_H2 == 1`,
    - `AGE_TIGHT_V1`,
    - and `EXPANSION_TIGHT_V1`,
  - interpretation: a stricter proxy corridor that asks for age and vacuum-sector parameters that are both ΛCDM-like and internally well behaved.

At this design rung no new structure proxies beyond these FRW-based combinations are introduced. Later Stage II host-level work may add genuinely structure-related diagnostics (for example simple growth-factor or halo proxies); if so, new proxy corridors will be defined in separate design rungs with explicit notation and promotion gates.

### 3.4 Non-claims and promotion discipline

All corridors defined in this section are:

- Stage 2 diagnostic helpers only,
- not fits to any particular dataset,
- and not substitutes for a proper likelihood or posterior analysis.

They do not:

- alter Phase 4 FRW masks,
- introduce new Phase-level claims,
- or change any Stage 2 promotion gates.

Any future use of these corridors in Phase 4 or Phase 5 narratives will require:

- separate implementation rungs that attach boolean columns and summary tables to the static kernel,
- a refreshed obstruction verdict that explicitly reports their impact on the pre-data kernel and the 40 point sweet subset,
- and Phase 0–style gates plus explicit doc updates if any corridor or surviving subset is ever considered for promotion into phase papers.
