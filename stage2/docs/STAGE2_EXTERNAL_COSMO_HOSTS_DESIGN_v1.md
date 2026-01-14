# Stage 2 – External Cosmology Hosts Design (v1)

*Status:* design / forward-looking  
*Scope:* Stage 2 only (diagnostic belts), no new Phase-level claims.  
*Goal:* Define how the Origin-Axiom program could later talk to serious cosmology codes (CLASS/CCL/etc.) in a way that stays strictly within the Phase 0 contract.

---

## 0. Motivation

We now have:

- A **mechanism module** (Phase 3) that turns a non-cancelling twist into a vacuum scale and related diagnostics.
- A **toy FRW module** (Phase 4) that turns that vacuum scale into:
  - an effective \`omega_lambda\`,
  - a toy FRW age \`age_Gyr\`,
  - viability flags and masks.
- A **Stage 2 belt** that:
  - builds joint θ-grids,
  - defines FRW viability / toy corridors / empirical anchors,
  - and now cross-checks the toy FRW age against a simple **analytic FRW host**.

This already gives us a *diagnostic* sense of where the axiom’s θ-corridors live relative to:

- a coarse empirical box in \`(omega_lambda, age_Gyr)\`,
- and a calibrated FRW-background host.

The next natural question is:

> How could we **safely** escalate this to more realistic cosmology engines (CLASS/CCL/…)
> without breaking Phase 0 discipline or over-claiming?

This document is the design sketch for a future Stage 2 “external cosmology hosts” belt that answers that question.

---

## 1. Phase 0 constraints (what we are *not* allowed to do)

Any contact with serious cosmology codes must respect:

1. **Phase 0 anti-overclaiming**
   - No “we fit Planck,” “we explain Λ,” or similar.
   - At most: “for this mapping and these priors, the model’s θ-corridor does / does not
     intersect simple, pre-declared viability regions.”

2. **Phase hierarchy**
   - Phases 1–5 + Stage 2 belts define the canonical story.
   - External hosts live in Stage 2 (and later Stage II), as **diagnostic instruments**,
     not as part of the core mechanism definition.

3. **Gating for real data**
   - Full likelihood pipelines (Planck, BAO, SN, etc.) are *not* part of this Stage 2 design.
   - At this level we only allow:
     - background quantities (H(z), distances, age, etc.),
     - maybe very coarse power-spectrum shape checks,
     - but still **no** official data likelihoods.

All of this means:

> External hosts are “lab benches we push θ onto,” not oracles that certify the axiom.

---

## 2. What counts as an “external cosmology host”?

For this design, an external host is any *validated* code/library that:

- Takes standard cosmological parameters as input:
  - \`Omega_m\`, \`Omega_lambda\`, \`Omega_r\`, \`H0\`, possibly \`w0, wa\`, …
- Returns background and/or linear-theory quantities:
  - \`H(z)\`, comoving distances, age of the universe, growth factor, simple Cℓ / P(k), …

Typical examples (not yet wired in, just targets):

- **CLASS** – Boltzmann + background solver.
- **CCL** – Core Cosmology Library, for validated background and clustering quantities.
- **PyCosmo** – Python-oriented background and Einstein–Boltzmann solver.

In the repo, these would live in a new belt under:

- \`stage2/external_cosmo_hosts/\`

separate from the current \`stage2/external_frw_host/\` (which is purely analytic).

---

## 3. Conceptual architecture

The architecture should mirror what we already do for the toy FRW and joint grids:

1. **Mapping layer: θ → standard parameters**
   - A *thin* module that maps:
     - \`theta\` (and existing mechanism outputs like \`E_vac\`)
     - to standard cosmological parameters:
       - e.g. \`(Omega_m, Omega_lambda, H0)\`.
   - This mapping is part of the **theory side**, not the host.
   - It must be documented with:
     - scope,
     - assumptions,
     - and explicit non-claims.

2. **Host interface modules**
   - Small wrappers that:
     - receive a table of parameter tuples,
     - call the external library (CLASS/CCL/…),
     - and return:
       - background quantities (\`H(z)\`, age, distances),
       - possibly a few linear observables (optional, future rung).

3. **Stage 2 diagnostics**
   - Scripts that compare:
     - host outputs vs toy FRW outputs,
     - host outputs vs empirical boxes,
     - host-defined viability corridors vs existing FRW corridors and empirical anchors.

4. **Output tables**
   - All host interactions must produce:
     - explicit, versioned CSVs under \`stage2/external_cosmo_hosts/outputs/tables/\`,
     - with clear column names, grid definitions, and masks.

At all times:

> The mechanism lives in Phase 3,
> the FRW toy lives in Phase 4,
> and hosts are independent “checkers” living in Stage 2.

---

## 4. Proposed belt structure

This is a forward-looking belt; names and rungs may evolve, but the spirit should remain:

### 4.1 Belt root

- Directory: \`stage2/external_cosmo_hosts/\`
- Subfolders:
  - \`src/\` — Python scripts (no heavy dependencies imported unless explicitly enabled).
  - \`config/\` — JSON/YAML configs for parameter grids, redshift grids, and “empirical boxes.”
  - \`outputs/tables/\` — CSV tables with host outputs + masks.
  - \`docs/\` — belt-specific docs (if needed; top-level Stage 2 docs already exist).

### 4.2 Rung HC1 – Mapping θ to host parameters (design-only at first)

Even before code, we want a design doc:

- \`stage2/external_cosmo_hosts/docs/HC1_THETA_TO_PARAMS_DESIGN_v1.md\`

It should:

- Specify the allowed mappings:
  - e.g. \`theta -> E_vac(theta) -> Omega_lambda(theta)\`,
  - plus any assumptions about \`Omega_m\`, \`H0\`, etc.
- Make explicit:
  - whether we keep \`Omega_m\`, \`H0\` fixed to fiducial values,
  - or introduce additional theory parameters.
- Declare non-claims:
  - this mapping is a *toy embedding*, not a final, unique derivation.

### 4.3 Rung HC2 – Background-only host grid

A first actual code rung (future):

- Script (placeholder): \`stage2/external_cosmo_hosts/src/run_background_grid_with_host_v1.py\`
- Inputs:
  - A θ-grid table (likely the existing joint grid),
  - A mapping config (how to compute \`Omega_lambda, Omega_m, H0\` from θ),
  - Host config (which host to call, which redshift grid).
- Outputs:
  - A CSV like:
    - \`stage2/external_cosmo_hosts/outputs/tables/stage2_external_cosmo_host_background_grid_v1.csv\`
  - Columns:
    - \`theta_index, theta, Omega_lambda, Omega_m, H0, age_Gyr_host, ...\`

The design requirement:

- This rung **must not** depend on any data likelihoods.
- It is purely a “background calculator plus sanity filters.”

### 4.4 Rung HC3 – Host vs toy FRW background comparison

An analogue of what we already did with the analytic host:

- Script: \`compare_host_vs_toy_background_v1.py\`
- Inputs:
  - Host background grid (from HC2),
  - Phase 4 FRW toy table(s),
  - Joint θ-grid if needed.
- Diagnostics:
  - Differences in \`omega_lambda\`, \`age_Gyr\`, and other shared quantities.
  - Masks for:
    - host-viable,
    - toy-viable,
    - overlap sets (host ∧ toy ∧ corridor, etc.).

The goal is *not* to make them match, but to quantify the mismatch in a reproducible way.

### 4.5 Rung HC4 – Host-defined empirical boxes (optional)

Once HC3 is stable, we can define “host-native” empirical boxes such as:

- host age window around observed age,
- simple constraints on \`Omega_lambda\`,
- optional constraints on integrated distances (e.g. distance to last scattering).

These would be configured via JSON and only used to define *diagnostic masks*:

- host_age_anchor,
- host_distance_anchor,
- etc.

They should mirror the spirit of our current empirical anchor boxes:
small, explicit, and designed to be falsifiable.

---

## 5. Dependencies and toggles

Because external hosts can be heavy and environment-sensitive, the belt must be designed with:

1. **Soft dependencies**
   - No import of CLASS/CCL/etc. at module import time.
   - Host-dependent code should be guarded behind explicit flags and try/except blocks.

2. **Reproducibility**
   - All rungs must:
     - print their configuration (host choice, parameter mapping, redshift grid),
     - write that configuration alongside the outputs (e.g. a JSON next to the CSV).

3. **Disable-by-default**
   - In Phase 0/Stage 1 contexts, the external host belt can be **disabled** by default.
   - The main repo should remain buildable without any host libraries installed.
   - Running these rungs becomes a deliberate action by a user who has the right environment.

---

## 6. Claim discipline and promotion

Any result from this belt must pass through a **promotion gate** before entering Phase-level narratives.

We anticipate a future gate document:

- \`docs/EXTERNAL_COSMO_HOST_PROMOTION_GATE_v1.md\`

with rules such as:

- No promotion unless:
  - host computations are independently reproduced,
  - mapping θ → params is frozen and documented,
  - sensitivity analysis has been carried out,
  - the effects of grid resolution and numerical settings are understood.

Early-stage results from this belt should be framed as:

- “host-background diagnostics,”
- “alignment/misalignment profiles,”
- not as evidence “for” or “against” the axiom itself.

---

## 7. Relation to current FRW + host work

The existing:

- \`stage2/external_frw_host/\` belt,
- FRW toy tightening (Phase 4),
- and empirical anchors (Stage 2),

already play the role of a **zeroth-order host**:

- Analytic flat-FRW ages,
- Age windows around observed Universe age,
- Toy vs host comparisons on the background level.

The future external-cosmo-host belt is intended as:

- A *superset* of this structure,
- With more realistic background dynamics and, optionally, linear observables,
- But *not* replacing the toy FRW or the analytic host in the baseline story.

---

## 8. Next steps (when we decide to activate this belt)

When/if we decide to move forward:

1. Flesh out \`HC1_THETA_TO_PARAMS_DESIGN_v1.md\` with a concrete mapping proposal.
2. Implement a minimal HC2 rung that:
   - reads a small θ-subgrid,
   - calls one external library (e.g. CCL or CLASS),
   - and produces a background grid CSV.
3. Mirror the existing analytic-host diagnostics (HC3/HC4) on top of that grid.
4. Add a short Stage 2 doc section summarizing:
   - which external host was used,
   - what was computed,
   - and what claim shapes are allowed.

Until then, this document serves as a **design contract**:
a way to keep future “real physics” ambitions disciplined and compatible with the structure we’ve already built.
