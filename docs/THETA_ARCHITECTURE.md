# θ & A Architecture Note (Draft)

Status: **Draft, non-binding design document.**  
Binding claims and contracts still live in the Phase 0–3 papers and their
co-located `CLAIMS.md` / `CLAIMS_TABLE.md` files. This note is allowed to
speculate, propose architectures, and mark TODOs, but it does **not** change
any existing claims by itself.

The goal of this document is to:
- assemble a phase-by-phase inventory of how the phase parameter θ and the
  “global amplitude / residue” observable (A, Δρ_vac, etc.) currently appear;
- separate implementation details from candidate physical structure;
- state non-negotiable constraints that any **canonical θ** must satisfy if
  the Origin Axiom is to make contact with real physics;
- sketch a small number of **candidate architectures** for θ and A across all
  phases; and
- use those architectures to inform the design of Phase 4 and beyond.

This is intentionally higher-level than any single phase paper. It is meant
to be the “wiring diagram” for the Origin-Axiom program as a whole.

---

## 1. Phase-by-phase inventory of θ and A

### 1.1 Phase 0 (Corridor / Ledger / Contracts)

**Role of θ**

- Phase 0 does *not* fix a specific θ or even a unique parametrization.
- Instead, it defines a **corridor-style workflow**:
  - each phase can emit an *admissible region* in some θ-like parameter
    space (often 1D θ, but not necessarily);
  - Phase 0 aggregates these regions into a global corridor by intersection;
  - the “ledger” records provenance, run IDs, and certificates.
- θ is therefore treated as:
  - a *handle* by which different phases talk about potentially the same
    underlying structure, without committing to what that structure *is*;
  - something whose canonical value (if it exists) should be **earned** by
    narrowing the corridor, not assumed.

**Role of A / “amplitude”**

- Phase 0 is mostly agnostic about the detailed observables:
  - it knows that phases may expose quantities like “global amplitude”,
    “vacuum residue”, etc.;
  - it only requires that such quantities can support **binding certificates**
    and well-defined filters.
- The key structural idea:
  - there exists some “global something” A whose non-cancellation is enforced
    by the Origin Axiom;
  - phases may expose different *proxies* for A (e.g. A_0, Δρ_vac) but they
    should eventually be related.

**Takeaway for this doc**

Phase 0 gives us a *shape* of the inference problem (corridors, filters,
certificates), but not the ontology. In this architecture note we have to
decide what θ and A actually *are* if we want a canonical picture.

---

### 1.2 Phase 1 (Phasor / Lattice Toy)

*(Summary; details should be cross-checked against the Phase 1 paper & code.)*

**θ in Phase 1**

- θ enters as a *twist* parameter in a phasor ensemble / lattice interference
  system.
- It is used to parametrise how phases are assigned or shifted, so that:
  - different θ values correspond to different interference patterns;
  - some θ values will lead to stronger cancellation, some to more residue.

In other words, θ in Phase 1 is a **dial on interference structure** in a toy
model that is not yet tied directly to real fields of the Standard Model or
gravity.

**A in Phase 1**

- A is essentially a **global amplitude / residue** of the phasor ensemble:
  - think: some norm or aggregate magnitude of the resulting complex sum.
- The Origin Axiom is implemented as:
  - an enforcement that A does not fall below some floor ε_floor > 0;
  - numerical experiments show that enforcing such a floor is stable and
    yields a non-trivial distribution of A across θ.

**Implementation vs candidate physics**

- Implementation detail:
  - the exact lattice structure, phase assignment rule, and numerical
    integrator are model choices.
- Candidate physical structure:
  - the *idea* that there is a global amplitude-like quantity A(θ) whose
    non-cancellation is enforced as a floor.

---

### 1.3 Phase 2 (Vacuum Residue & FRW Embedding)

*(Summary; details should be cross-checked against Phase 2 docs.)*

**θ in Phase 2**

- Phase 2 introduces a toy **vacuum-residue mechanism**:
  - θ appears as an injection parameter into this mechanism;
  - the idea is that different θ map to different vacuum-side configurations.
- There is also a pathway to embed the resulting vacuum residue into a
  **toy FRW cosmology**, producing trajectories that can be compared to a
  reference Λ_obs case.

So θ here is a **vacuum-side dial**: it selects different vacuum configurations
and thus different effective vacuum energy proxies.

**A / Δρ_vac in Phase 2**

- Phase 2 exposes a **residual energy proxy**:
  - call it Δρ_vac(θ) or similar;
  - this plays the role of “vacuum residue” after the non-cancellation
    mechanism has acted.
- This residue can then be normalised and interpreted as a toy contribution
  to cosmological constant–like behavior in an FRW module.

**Implementation vs candidate physics**

- Implementation detail:
  - the exact lattice / discretisation, potential, and FRW embedding scheme;
  - the exact normalisation connecting Δρ_vac to Ω_Λ.
- Candidate physical structure:
  - a **mapping from θ to a vacuum energy–like observable**;
  - the idea that enforcing a floor on a global amplitude can be interpreted
    as enforcing a non-zero vacuum “something” that behaves qualitatively
    like vacuum energy.

---

### 1.4 Phase 3 (Mechanism) – New Toy Vacuum Mechanism

This is the **newly defined Phase 3 mechanism**, distinct from the archived
flavor-calibration experiment in `experiments/phase3_flavor_v1/`.

**θ in Phase 3 (mechanism)**

- θ is a continuous parameter in [0, 2π), entering as a phase in a deterministic
  ensemble of complex modes:
  - each mode has a phase α_j + σ_j θ;
  - the ensemble is fixed by a `VacuumConfig`.

Thus θ here is **explicitly a global phase angle**: it “twists” all modes
coherently according to their σ_j coefficients.

**A_0(θ) and A(θ) in Phase 3**

- A_0(θ):
  - defined as the **global unconstrained amplitude**, the magnitude of the
    mean of the ensemble of complex modes.
- A(θ):
  - defined by enforcing the Origin Axiom’s floor:
    \[
      A(\theta) = \max\big(A_0(\theta), \varepsilon_{\mathrm{floor}}\big)
    \]
- The mechanism exposes:
  - `amplitude_unconstrained(θ, cfg)` → A_0(θ);
  - `amplitude_with_floor(θ, cfg, epsfloor)` → A(θ);
  - scanners that sweep θ over a grid and report binding diagnostics.

**Binding regime diagnostics**

- Baseline scan is used to:
  - measure the distribution of A_0(θ);
  - choose ε_floor as a quantile (e.g. 25th percentile);
  - confirm that 0 < frac_bound < 1 (a genuine binding regime).
- Binding certificate diagnostics:
  - mean shift between A and A_0;
  - L² distance between A and A_0;
  - binding fraction;
  - min/max and quantiles.

**Implementation vs candidate physics**

- Implementation detail:
  - choice of mode ensemble, specific quantile used for ε_floor, grid size;
  - purely numerical thresholds in diagnostics.
- Candidate physical structure:
  - **A is explicitly a global amplitude of a vacuum-like mode ensemble**;
  - the non-cancellation floor is implemented directly on this A(θ);
  - this is the cleanest toy realisation so far of “global amplitude
    constrained by a floor”.

---

## 2. Non-negotiable constraints for a canonical θ & A

If the Origin Axiom is to be more than an algorithmic toy, a canonical θ and
its associated A must satisfy at least the following:

1. **Globality**
   - θ must represent a global structural degree of freedom, not a patchwork
     of unrelated model parameters.
   - Changes in θ should have coherent effects across whatever sectors it
     touches (vacuum, fields, cosmology).

2. **Vacuum relevance**
   - There must be a principled way to interpret A(θ) as a vacuum-side
     observable (or tightly related to one), not just a numerical artifact.
   - In particular, it should be possible to connect A(θ) or its residue to
     something like an effective vacuum energy density or similar invariant.

3. **Corridor compatibility**
   - θ must live in a space where different phases can express **filters**
     that are meaningfully intersected.
   - If phases use different parametrisations, there should exist a clean
     mapping into a common θ-space.

4. **Non-cancellation semantics**
   - The floor constraint A(θ) ≥ ε > 0 must be interpretable as a physical
     principle (e.g. a global obstruction to perfect cancellation), not just
     a coding trick.
   - There should be at least one candidate mechanism (e.g. topological,
     geometric, variational) that could enforce such a floor.

5. **Empirical path**
   - There must be a plausible route from θ & A(θ) to **empirical contact**:
     - vacuum energy,
     - FRW expansion,
     - SM parameters,
     - or other observables.
   - Even if not executed yet, the architecture must not rule this out by
     construction.

6. **Non-numerology**
   - Any special values of θ (e.g. a θ* or narrow corridor) must arise from
     structural constraints, not because they “look nice” (golden ratio, etc.).
   - Numerology can inspire hypotheses but cannot be the endpoint.

---

## 3. Candidate architectures for θ & A

Below we sketch a small set of candidate architectures. The goal is **not** to
decide immediately, but to make explicit what each choice would imply for
Phase 4 and beyond.

### 3.1 Architecture A: θ as a *pure vacuum phase*

**Definition**

- θ is a single global phase parameter of a vacuum mode ensemble, as in
  Phase 3 (mechanism).
- A_0(θ) and A(θ) are global amplitude observables of that ensemble.
- Other phases (Phase 1, Phase 2, FRW modules, etc.) must map their internal
  parameters into this vacuum θ (or functions of it).

**Implications**

- Phase 3 becomes the *canonical home* of θ and A.
- Phase 1 and 2 are reinterpreted as **toy implementations / projections**
  of the same underlying vacuum structure, or as **consistency tests**:
  - they must justify how their internal θ maps to the canonical vacuum θ;
  - any corridor they produce must be expressible in the canonical θ-space.
- Phase 4 should:
  - focus on connecting A(θ) and its floor-enforced residue to vacuum energy
    and FRW evolution in a tighter way;
  - explore whether a narrow corridor in θ emerges when imposing consistency
    between vacuum-side constraints (mechanism + FRW + observational targets).

**Pros**

- Clean ontology: θ lives in one place (vacuum); A is clearly defined.
- The non-cancellation floor has a natural home: the global vacuum amplitude.

**Cons / Risks**

- Flavor sector, SM parameters, and other phenomena must be tied to θ via
  possibly intricate mappings; this may be hard or impossible without a much
  deeper mechanism.
- Strong dependence on the plausibility of the vacuum-mode picture.

---

### 3.2 Architecture B: θ as a *cross-domain phase hook*

**Definition**

- θ is still a single global parameter, but the architecture explicitly allows
  **sector-specific maps**:
  - θ^vac = f_vac(θ),
  - θ^flavor = f_flavor(θ),
  - θ^FRW = f_FRW(θ),
  - etc.
- A(θ) is defined canonically in the vacuum sector (as in Phase 3), but other
  sectors may couple to θ via derived quantities.

**Implications**

- Phase 3 still defines the canonical A(θ), but:
  - Phase 1, Phase 2, and any future flavor/cosmology phases can introduce
    **controlled reparameterisations**.
- Corridors now live in a slightly richer space:
  - each phase can constrain θ via its own f_sector;
  - Phase 0 ledger must be able to map those constraints back to the
    canonical θ domain for intersection.

**Pros**

- More flexible: easier to imagine how θ might show up differently in vacuum,
  flavor, and cosmology while still having a single underlying parameter.
- Lets us keep some of the spirit of the archived flavor experiment as a
  potential future Phase-4+ extension, without forcing direct overlap at the
  mechanism stage.

**Cons / Risks**

- Increases the danger of **hidden numerology** or arbitrary mappings:
  - unless f_sector are strongly constrained, one can fit almost anything.
- Difficult to keep the architecture simple and explainable in a final ToE
  narrative.

---

### 3.3 Architecture C: θ as part of a *higher-dimensional structure*

**Definition**

- θ is not alone: the true object is something like
  \[
    \Theta = (\theta_1, \theta_2, \dots)
  \]
  or a geometric object from which different effective θ’s emerge.
- The phases we have so far only probe one effective direction; Phase 4+
  would explore additional directions.

**Implications**

- Phase 3 mechanism:
  - A(θ) becomes A(θ_1, …) restricted to a 1D slice.
- Phase 4 might:
  - explore whether the corridor naturally collapses to a lower-dimensional
    manifold in a higher-dimensional Θ-space.

**Pros**

- Conceptually rich: could match with ideas like multiple phases, Berry
  phases, or moduli spaces.
- Might explain why “just one θ” feels too rigid.

**Cons / Risks**

- Greatly expands the space of possibilities.
- Might postpone rather than solve the question “what is θ physically?”
- Harder to keep the program finite and publishable.

---

## 4. What Phase 3 (mechanism) has achieved so far

- We now have a **clean toy vacuum model** with:
  - deterministic ensemble of complex modes;
  - global amplitude A_0(θ);
  - floor-enforced amplitude A(θ) with a quantile-based ε_floor;
  - demonstrated binding regime with non-trivial diagnostics.
- This is the **closest thing to a canonical home for θ and A** that the
  program currently has:
  - A(θ) is clearly defined;
  - the floor is enforced in a transparent way;
  - binding behavior is quantified.

Phase 3 (mechanism) therefore strongly suggests **Architecture A or B**, with
Phase 3 as the vacuum anchor.

---

## 5. Implications for Phase 4 design

Given the architectures above, we can now frame Phase 4 as:

> A structured attempt to connect the Phase 3 vacuum mechanism
> (θ, A_0(θ), A(θ)) to **external constraints** in a way that:
> - respects the corridor and ledger logic of Phase 0;
> - does not rely on numerology;
> - has a plausible path to empirical contact.

Concrete options for Phase 4, conditional on architecture choice:

1. **If we choose Architecture A (vacuum-only θ at this stage):**
   - Phase 4 focuses on:
     - refining the vacuum mechanism;
     - embedding A(θ) into FRW in a more principled way;
     - exploring whether a narrow θ-corridor emerges when demanding
       consistency with qualitative cosmological behavior (e.g. sign and
       rough scale of vacuum energy, expansion behavior).
   - Flavor / SM contact is postponed to Phase 5+.

2. **If we choose Architecture B (cross-domain hook):**
   - Phase 4 might:
     - define a careful f_FRW(θ) and/or f_flavor(θ) with explicit non-claims;
     - re-attempt a **minimal** cross-domain corridor intersection, with
       strong safeguards against overfitting;
     - interpret any empty corridors as diagnostic of the mappings rather
       than of the axiom itself.

3. **If we choose Architecture C (higher-dimensional Θ):**
   - Phase 4 would need to:
     - define Θ and its geometry;
     - reinterpret all existing phases as slices;
     - this is significantly more ambitious and may delay publication.

---

## 6. Next questions to answer before coding Phase 4

Before we touch new scripts or LaTeX for Phase 4, this doc should be updated
to answer, explicitly:

1. **Which architecture are we tentatively adopting?** (A, B, C, or a hybrid?)
2. **Where does canonical θ live?**
   - Is it the Phase 3 vacuum θ?
   - If not, what is the canonical definition?
3. **How do Phase 1 and Phase 2 map into this canonical θ-space?**
   - Are they:
     - illustrative toy models that will *not* constrain θ in the final
       program?
     - or are they meant to produce honest filters that must be respected?
4. **What is A, in words fit for a final ToE-style paper?**
   - “Global amplitude of vacuum mode ensemble”?
   - “Gauge-invariant scalar of underlying phase-space structure”?
5. **What does a *successful* Phase 4 outcome look like?**
   - Example: “A well-defined θ-corridor from vacuum + FRW constraints that
     is non-empty, non-trivial, and robust under reasonable variations.”
6. **What would we count as a *negative* but informative Phase 4 outcome?**
   - Example: “Any attempt to reconcile vacuum-side A(θ) with FRW behavior
     and observed scales leads to empty corridors, suggesting this specific
     floor mechanism is not physically viable.”

Once those questions are answered in this document (even tentatively), we will
have a much clearer, architecture-driven path for designing Phase 4 and, later,
revisiting external sectors like flavor with less risk of drift.


---

## 7. Current working decisions (2026-01-07 draft)

This section records the **current working choices** for θ and A across the
program. It is still non-binding, but it should guide Phase 4 design unless a
later rung explicitly revises it.

### 7.1 Architecture choice

We **adopt Architecture A (vacuum-anchored θ)** as the working architecture:

- Canonical θ lives in the **Phase 3 mechanism vacuum model**:
  - θ is a single global phase parameter in \([0, 2\pi)\).
  - It enters as the phase in a deterministic ensemble of vacuum modes
    (phases α_j + σ_j θ).
- The canonical global observable is:
  - \(A_0(\theta)\): unconstrained global amplitude;
  - \(A(\theta) = \max(A_0(\theta), \varepsilon_{\mathrm{floor}})\):
    floor-enforced amplitude.

Other phases must either:
- map their internal parameters into this canonical θ space, or
- be treated as illustrative / non-binding toy models that do not constrain
  the final corridor.

We keep open the possibility of **Architecture B-style sector maps** in later
phases (e.g. θ^FRW(θ)), but we do *not* assume them yet.

### 7.2 Where canonical θ lives

- Canonical θ is **the vacuum θ of Phase 3 (mechanism)**.
- Any future θ-like variables must be explicitly mapped into this θ, or
  clearly marked as non-canonical / illustrative.

### 7.3 How Phases 1 and 2 relate to canonical θ

Current working interpretation:

- **Phase 1**:
  - Treated primarily as a *didactic / exploratory* toy model of interference
    and non-cancellation.
  - Its θ is allowed to be *informally* aligned with the canonical θ, but
    Phase 1 does **not** presently impose a binding corridor on canonical θ.
- **Phase 2**:
  - Provides a toy vacuum-residue-and-FRW embedding.
  - For now, its θ is also treated as **illustrative** rather than a binding
    filter on canonical θ.
  - Phase 2 is still valuable:
    - it demonstrates that a non-cancellation-style residue can be threaded
      into an FRW module without numerical pathologies;
    - it provides design lessons for Phase 4.

In other words: until we define explicit mappings from their internal θ to the
canonical vacuum θ (and audit them), Phase 1–2 corridors are **non-binding**
with respect to canonical θ. They remain part of the historical and conceptual
scaffolding of the program.

### 7.4 What A is, in human words

Working narrative definition of A for future ToE-style writing:

> A(θ) is a global amplitude-like observable of a vacuum-mode ensemble.
> It measures how “far from perfect cancellation” the ensemble is at a
> given global phase θ, and the Origin Axiom enforces that this global
> amplitude cannot cross below a strictly positive floor ε > 0.

More concretely:

- In the Phase 3 mechanism:
  - The vacuum is modelled as a fixed set of complex modes.
  - A_0(θ) is the magnitude of their ensemble-averaged complex sum.
  - A(θ) is A_0(θ) with a non-cancellation floor imposed.
- In later phases:
  - A(θ) (or a derived residue) is the quantity we aim to connect to
    vacuum-energy-like observables and FRW behaviour.

### 7.5 Success & failure criteria for Phase 4 (high level)

**Success (working definition):**

- Using the Phase 3 mechanism as the canonical vacuum,
- and treating θ as the canonical global phase,
- Phase 4:
  - constructs a principled mapping from A(θ) or its residue into a toy FRW
    or vacuum-energy-like observable;
  - defines a clear **θ-corridor** (possibly broad) that is:
    - non-empty,
    - qualitatively compatible with basic cosmological behaviour
      (e.g. sign and rough scale of vacuum energy, no grossly unphysical
      FRW dynamics),
    - robust under reasonable variations in modelling choices
      (grid resolution, moderate parameter tweaks).

**Informative failure:**

- Any reasonably broad class of mappings from A(θ) to vacuum-energy-like
  observables leads to:
  - empty θ-corridors, or
  - corridors that require extreme fine-tuning or pathological behaviour,
- in which case Phase 4 should:
  - explicitly record that the *current* global-amplitude mechanism appears
    incompatible with even toy-level cosmological behaviour,
  - and propose concrete alternatives (e.g. modified vacuum ensembles,
    different floor semantics, or abandoning this particular mechanism).

The goal is that Phase 4 deliver either:
- a **live corridor** worth further sharpening in Phase 5+, or
- a **clear diagnostic** that this specific realisation of the Origin Axiom
  is not viable, without contaminating the broader axiom.


## Obstruction-program view of θ

From the obstruction program perspective, θ indexes how a non-cancelling phase twist threads the space of near-cancelling configurations rather than serving as a free, unstructured label. The locked Stage I stack does not fix a unique physical interpretation of θ, but several recurring roles are visible in the existing artefacts: Phase 1 uses θ to track toy ensembles and residues, Phase 3 uses it as a control parameter for mechanism amplitudes and penalties, and Phase 4 uses it as the coordinate along which FRW-like masks and corridors are defined. In all of these, θ organises how far the system sits from a notional perfectly cancelling class and how that “distance” behaves under coarse-graining.

The obstruction program treats θ\* as a structurally distinguished point in this space of near-cancelling configurations, defined by the non-cancelling phase twist that sits at the root of the Origin Axiom constructions. It does not currently claim that θ\* is selected by existing FRW or data probes; Stage 2 analyses instead check θ\* for neutrality and redundancy, and Stage II is designed to test whether any θ corridor that survives external hosts and data gates needs θ\* specifically. For details of this interpretive layer, see `docs/OBSTRUCTION_PROGRAM_OVERVIEW_v1.md` and the Stage 2 empirical anchor and external host docs referenced there.
