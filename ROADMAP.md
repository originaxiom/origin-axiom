# Origin Axiom Program Roadmap

_Status note (2026-01-11)._ This document is a **legacy program roadmap**
from the pre-Stage-2 / early-phasing period. It is kept for historical
context and high-level narrative only. For the current, canonical view of
phase status and future work, prefer:

- `docs/STATE_OF_REPO.md` (current phase/Stage status),
- `docs/PHASES.md` (formal phase definitions and scopes),
- `docs/FUTURE_WORK_AND_ROADMAP.md` (up-to-date future work and roadmap).

Where this roadmap disagrees with those documents, the `docs/` versions
and per-phase `SCOPE.md`/`CLAIMS.md` files are authoritative.


This document summarises how the repository is structured as a multi–phase program
and what each phase is allowed to claim. It is intended for reviewers who want a
high–level picture of progression from abstract non–cancellation principle to
increasingly concrete physics tests.

The roadmap should be read together with:

- `README.md` (overview + how to run things),
- `docs/PHASES.md` (formal phase definitions),
- `docs/CLAIMS_INDEX.md` (global claim ledger),
- `phase0/CLAIMS.md`, `phase1/CLAIMS.md`, `phase2/CLAIMS.md`
  (phase–local claim registers).

---

## Program philosophy in one paragraph

The Origin Axiom project starts from a single organising idea: **physical reality
cannot realise a perfectly cancelling phase configuration**. Instead, there is always
a small, structured **residue** left over when one tries to cancel contributions.
The programme does *not* assume in advance that this principle explains our universe;
rather, it asks a narrower question:

> If a non–cancellation principle is taken seriously and implemented carefully,
> can one build toy models and pipelines where the residue is (a) well–defined,
> (b) numerically stable, and (c) constrained strongly enough that comparisons
> to standard cosmological observables become meaningful?

The phases are designed to separate:
- **governance and method claims** (Phase 0),
- **existence and robustness of a toy non–cancelling mechanism** (Phase 1),
- **behaviour of that mechanism in a stricter mode–sum model with FRW–style
  diagnostics** (Phase 2),

from any **strong cosmology or “theory of everything” claims**, which are explicitly
out of scope at this stage.

---

## Phase 0 — Governance, contracts, and corridor bookkeeping

**Directory:** `phase0/`  
**Paper:** `phase0/paper/main.tex`  
**Local claims:** `phase0/CLAIMS.md`

Phase 0 does **not** claim any physics result. Its role is to specify:

1. **Claim taxonomy and IDs**  
   - How claims are named (e.g. `P0-C01`, `P1-C02`, `P2-C21`, …).  
   - How claims are grouped by phase and type (existence / robustness / scaling /
     bounded viability / governance).

2. **Corridor and filter artefacts**  
   - How θ–prior ranges, θ–corridors, and filters are represented as JSON.  
   - How these artefacts are validated against schemas in `phase0/schemas/`.  
   - How their history is logged in `phase0/phase_outputs/`.

3. **Reproducibility contract**  
   - Requirements for Snakemake–based pipelines (inputs, outputs, pinned run IDs).  
   - What must be stored in `phaseX/outputs/figures/` vs
     `phaseX/outputs/runs/`.  
   - How `pip_freeze.txt`, `meta.json`, and `params_resolved.json` are used to
     make runs auditable.

4. **Failure modes and non–claims**  
   - Explicit examples of what the programme **does not** claim (no
     “new cosmology”, no parameter–free prediction of Λ, etc.).  
   - How negative or ambiguous results must be logged and kept visible.

Phase 0 is the **governance layer**. Phases 1 and 2 are considered valid only
insofar as they respect the Phase 0 contracts and register their claims through
`docs/CLAIMS_INDEX.md` and their own `CLAIMS.md` files.

---

## Phase 1 — Toy non–cancellation on a lattice

**Directory:** `phase1/`  
**Paper:** `phase1/paper/main.tex`  
**Local claims:** `phase1/CLAIMS.md`  
**Canonical figures:** `phase1/outputs/figures/`

Phase 1 is the first physics–facing step, but *strictly* at the level of a
toy model. Its goals are:

1. **Define a controlled toy setting**  
   - A scalar (or few–mode) lattice model where phases are constrained by an
     Origin–Axiom–type rule.  
   - Clear separation between unconstrained and constrained ensembles.

2. **Demonstrate existence and robustness of a residue**  
   - Show that under the toy non–cancellation rule, a non–trivial residue
     \(\mathcal{R}\) emerges and is numerically well–behaved.  
   - Study how \(\mathcal{R}\) behaves under changes in lattice size,
     sampling, and constraint strength.

3. **Quantify scaling behaviour**  
   - Provide figures and tables that show how relevant observables scale
     (or fail to scale) as model parameters and resolutions are varied.  
   - Keep the claims explicitly at the **toy level**: no direct cosmological
     interpretation is asserted.

4. **Bind results to reproducible runs**  
   - Every Phase 1 claim is tied to specific outputs under
     `phase1/outputs/figures/` and pinned run IDs under
     `phase1/outputs/runs/`.  
   - The Snakemake pipeline `phase1/workflow/Snakefile` is the canonical way
     to regenerate those artefacts.

**Allowed claim types for Phase 1 (per `docs/PHASES.md`):**

- Existence (of particular behaviours in the toy model),
- Robustness (under perturbations of parameters and initial conditions),
- Scaling (within the toy domain).

No claims are made about our universe, Λ, or observational data in Phase 1.

---

## Phase 2 — Mode–sum model and FRW–style comparisons

**Directory:** `phase2/`  
**Paper:** `phase2/paper/main.tex`  
**Local claims:** `phase2/CLAIMS.md`  
**Canonical figures:** `phase2/outputs/figures/`

Phase 2 tightens the connection between the non–cancellation mechanism and
familiar cosmological diagnostics, still under **strictly bounded claims**.

Key objectives:

1. **Define a mode–sum model with a residue**  
   - Construct a mode–sum where a non–cancelling phase rule produces an
     effective residual contribution.  
   - Make the regularisation and cutoffs explicit (ε, number of modes, etc.).

2. **Measure scaling and stability in the stricter model**  
   - Revisit existence and robustness questions in this more constrained
     setting.  
   - Study dependence on regularisation schemes and check for numerical pathologies.

3. **Compare to FRW–style observables in a bounded way**  
   - Use the residual energy density (or equivalent observable) as an input
     to FRW background and growth calculations, via scripts in
     `phase2/src/phase2/cosmology/`.  
   - Generate comparison plots (`figE_frw_comparison.pdf`, etc.) that show
     where the toy residue lies relative to standard ΛCDM benchmarks.

4. **Formalise “bounded viability” instead of “new cosmology”**  
   - Claims in Phase 2 are framed as: *given* the toy model and its fitted
     parameters, what ranges of behaviour are **compatible** or **in tension**
     with FRW–style diagnostics?  
   - Strong statements about “explaining dark energy” or “predicting Λ”
     remain explicitly out of scope.

As in Phase 1, all claims are backed by pinned runs in
`phase2/outputs/runs/` and canonical plots in `phase2/outputs/figures/`,
with a Snakemake workflow in `phase2/workflow/Snakefile`.

**Allowed claim types for Phase 2:**

- Existence (of well–defined residuals in the mode–sum model),
- Robustness (of those residuals to cutoffs and parameter variations),
- Bounded viability (relative to FRW–style observables, under clearly stated
  assumptions).

---

## Beyond Phase 2 — Guardrails for future work

Any future phases (Phase 3 and beyond) must:

1. **Declare scope + explicit non–claims** up front, in `phaseX/SCOPE.md`.
2. **Define canonical artefacts** (figures, tables, run indices) and log them in
   `phaseX/CLAIMS.md`, with IDs registered in `docs/CLAIMS_INDEX.md`.
3. **Obey Phase 0 governance rules** on schemas, reproducibility, and failure
   modes.
4. **Make negative or ambiguous results first–class citizens**, not something
   to be hidden or discarded.

Some natural directions for Phase 3+ (purely as placeholders, *not* claims):

- Coupling the residue mechanism to more realistic matter models.  
- Exploring continuous limits or field–theoretic analogues of the discrete
  constructions.  
- More systematic confrontation with observational data under tight priors.

Each such step would be treated as a **separate phase**, with its own paper,
its own claim ledger, and its own reproducible Snakemake pipeline.

---

## How to read this roadmap as a reviewer

A recommended order for a first–time reviewer is:

1. Skim `README.md` and `ROADMAP.md` (this file) to understand the overall plan.
2. Read `phase0/paper/main.pdf` and `phase0/CLAIMS.md` to absorb the governance
   and claim discipline.
3. Inspect Phase 1:
   - `phase1/paper/main.pdf`
   - `phase1/CLAIMS.md`
   - the canonical figures in `phase1/outputs/figures/`
   - optionally re–run `cd phase1 && snakemake -c 1 all`.
4. Inspect Phase 2 in the same way:
   - `phase2/paper/main.pdf`
   - `phase2/CLAIMS.md`
   - canonical figures in `phase2/outputs/figures/`
   - re–run `cd phase2 && snakemake -c 1 all`.

At every step, the expectation is that claims are:

- narrowly phrased,
- backed by concrete artefacts,
- reproducible from the repository alone (no hidden legacy files),
- explicitly tethered to the governance laid out in Phase 0.