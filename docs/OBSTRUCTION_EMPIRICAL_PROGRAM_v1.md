# Obstruction empirical program (v1)

Status and scope.  
This memo records how the obstruction-program interpretation will interact with empirical tests in the Origin Axiom Stage I stack and its Stage 2 diagnostic belts. It is intentionally conservative: it describes what would count as meaningful evidence for or against the obstruction picture in the current framework, without promoting any new claims into the phase papers. All statements here are interpretive and downstream of the locked Phase 0–5 contracts and Stage 2 verdicts.

Static versus dynamic θ.  
At the axiom level the obstruction picture imagines a non-cancelling phase twist and a residual floor that prevents perfect cancellation. In that sense θ* is a fixed ingredient of the rule set, alongside the corridor structure that the theory is allowed to explore. In the current Stage I and Stage 2 implementation θ is treated as a static label on configurations: we scan a θ-grid and study which points or bands survive various consistency and toy empirical checks. We do not yet model θ as a dynamical field θ(t) or θ(x). The obstruction empirical program in this branch is therefore about the existence and structure of static θ corridors and kernels that are compatible with the current FRW and diagnostic machinery, not about full dynamical θ models. Any future move to a genuinely dynamical θ field will require separate design work, explicit Phase 0 gates, and new code paths.

What counts as a meaningful positive outcome.  
Within the current Stage I and Stage 2 stack the obstruction picture earns empirical credibility only if it can be threaded through concrete, reproducible filters. In this branch a meaningful positive outcome would look like the following pattern, without overclaiming:
- There exists a non-empty subset of the current θ-grid (a corridor or kernel) that passes:
  - the Phase 3 mechanism consistency checks,
  - the Phase 4 FRW viability and shape diagnostics,
  - the Stage 2 FRW corridor and data-probe belts, and
  - simple external sanity filters modelled after standard cosmological constraints.
- That surviving set is structured rather than accidental, for example:
  - it occupies a coherent band or cluster in θ rather than isolated numerical glitches,
  - it sits in a region of FRW parameter space that looks recognisably “ΛCDM-like” at late times, and
  - it is not destroyed by small, transparent variations in mapping choices or thresholds.
- The mapping from θ into FRW quantities and any external parameterisations is explicitly documented and reproducible from the repo.

Even if such a kernel is small, the combination of existence, structure, and mild robustness would justify treating the obstruction picture as an empirically non-trivial hypothesis rather than a loose metaphor.

What counts as a meaningful negative outcome.  
The empirical program is equally interested in precise negative results. A meaningful negative outcome would look like:
- For a broad and reasonable set of mapping choices and thresholds, all non-trivial θ corridors are destroyed once FRW viability, data-facing probes, and simple external constraints are applied.
- Any apparent surviving kernels turn out to be artefacts of:
  - extreme fine-tuning of thresholds,
  - choices that are clearly incompatible with standard cosmological constraints, or
  - numerical pathologies rather than stable structures.
- These failures can be traced back to specific features of the obstruction ansatz and recorded as “ruled out obstruction variants” in a way that is useful for future work.

In that case the obstruction program would still be valuable, but as a documented no-go result: a class of non-cancelling stories that cannot be made compatible with even toy-level empirical corridors.

Role of existing Stage 2 belts.  
The first generation of obstruction empirical work is required to stay within the existing Stage 2 diagnostic belts. In particular:
- The FRW corridor belt and its θ-histograms and family fractions provide the basic notion of a viable FRW corridor on the current 2048-point grid.
- The mech/measure belt provides smooth θ-indexed scalars derived from the Phase 3 mechanism module, but does not yet promote any single quantity to a canonical measure over θ.
- The joint mech–FRW belt demonstrates strong correlations between mechanism amplitudes and FRW scalars, showing that the mechanism behaves as a smooth reparameterisation of the toy vacuum sector at this resolution.
- The FRW data-probe belt clarifies the status of the current data flag: in the present snapshot the aggregate “data ok” mask is empty, so all corridors should be interpreted as pre-data toy corridors.
- The Stage 2 θ* diagnostic rung records that θ* lies inside the broad FRW-viable band but is not singled out by the current corridor machinery.

The obstruction empirical program treats these belts as the starting point. Early rungs in this branch will only rearrange, summarise, and interpret their outputs, without changing their code or claims. Any new filters, such as external cosmology corridors or host-based metrics, will be introduced as additional downstream layers.

Relation to real cosmology (Λ, DESI hints, early galaxies).  
The real universe places strong constraints on any obstruction-based picture. Late-time expansion is well described by a nearly constant dark energy sector, with current surveys allowing at most modest evolution in the effective equation of state. Early-universe observations show that galaxies and massive structures appear very quickly, which constrains how much the expansion history can be modified at high redshift without destroying structure formation. In this branch we will use these facts in two stages:
- Conceptual guardrails now: when choosing which toy filters or mappings to explore, preference will be given to constructions that can in principle resemble a nearly constant dark energy sector at late times and that do not obviously ruin early structure formation.
- Concrete external corridors later: at a later stage, and only after dedicated design work, simple external “corridor” constraints (for example boxes in effective w0–wa space or age-of-universe bounds at given redshift) may be encoded as additional Stage 2 or Stage II filters. Those steps will be explicitly documented and will not be treated as live data-fitting in the current branch.

Until those external corridors are formalised the obstruction empirical program should be read as an internal consistency and pre-alignment exercise: we study which θ corridors have any hope of surviving realistic constraints, without claiming that the present toy stack has been fully confronted with data.

Static θ as the current testbed.  
Given the above, the empirical questions addressed in this branch are deliberately narrow and static:
- Do there exist non-empty, structured θ corridors that survive the current FRW viability and diagnostic belts and any initial external-style filters we apply?
- How do those corridors sit inside the existing Stage 2 family structure (FRW-viable, LCDM-like, toy corridors, intersections)?
- Can we describe any surviving kernels in terms of simple FRW and mechanism quantities in a way that could later be mapped to standard cosmological parameters?

All of these questions can be addressed using static θ slices and the existing Stage 2 artefacts. Dynamical θ models, structure-formation pipelines, and detailed data contact are explicitly deferred to future phases and will require new governance decisions.

Phase 0 governance and promotion.  
Nothing in this memo changes the status of any Phase 0–5 contract or Stage 2 verdict. The obstruction empirical program is a planning layer and a set of interpretive guardrails. Any future promotion of obstruction-flavoured statements into phase papers, or any introduction of external data into the main stack, will require:
- an explicit design rung and written contract,
- a Phase 0 style gate that records what is being promoted and why,
- and corresponding updates to the relevant phase or Stage 2 documentation.

Until such promotions are enacted the obstruction program should be read as a disciplined way of asking questions of the current stack, not as a new set of claims about the universe.

## Minimal ψ–floor toy experiments (Stage 2 internal note)

The Stage 2 obstruction stack now includes a pair of 0D ODE “ψ + floor” toy models, documented in `stage2/docs/STAGE2_OBSTRUCTION_MINIMAL_PSI_FLOOR_TOYS_V1.md`. They are deliberately pre-cosmological: ψ is a generic complex scalar, the floor is a hard norm constraint at |ψ| = ε, and there is no FRW geometry or data.

The toys serve two purposes. First, they force us to distinguish clearly between a static floor and a genuinely frustrated dynamical process: pure dissipation plus a hard floor collapses and freezes on the floor, whereas adding a drive term produces a non-trivial attractor near the floor with the floor itself rarely active. Second, they reinforce that any serious “frustrated-cancellation” story must be carried by explicit dynamics and drive terms, with the floor acting as a constraint, not as an energy source.

These experiments do not change any Phase 0–5 contracts, FRW masks or promotion gates. They are recorded here as an internal conceptual lab that informs how we talk about floors and frustration while the empirical obstruction program itself remains a static analysis on the θ-grid with FRW and external-style corridors.
