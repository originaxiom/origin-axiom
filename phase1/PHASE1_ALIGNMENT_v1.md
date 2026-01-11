# Phase 1 alignment memo (scope, claims, toy ensembles, and paper)

Status (2026-01-11): This memo records how the Phase 1 paper, scope/claims/assumptions documents, and the current repository surface align. It is descriptive only and does not introduce new claims.

## 1. Inputs used for this alignment

This memo is based on:

- `phase1/README.md` – Phase 1 overview and repository structure.
- `phase1/SCOPE.md` – Phase 1 scope definition and non-claims.
- `phase1/CLAIMS.md` – Phase 1 claims register.
- `phase1/ASSUMPTIONS.md` – explicit assumptions and limitations.
- `phase1/REPRODUCIBILITY.md` – reproducibility protocol.
- `phase1/config/phase1.yaml` and related configs – parameter surface for Phase 1 runs.
- `phase1/paper/main.tex` and its section files (`01_intro.tex`, `02_axiom.tex`, `03_toy_models.tex`, `04_methods.tex`, `05_results.tex`, `06_limitations.tex`, `07_conclusion.tex`).
- `artifacts/origin-axiom-phase1.pdf` – the Phase 1 paper built from the LaTeX sources.

Where convenient, this memo refers to paper sections by their LaTeX labels (e.g. `\section{Introduction}`, `\section{Axiom}`, `\section{Toy Models: Finite Phasor Ensembles}`) and by the section roles implied by the code and claims register.

## 2. Scope: minimal non-cancellation principle, no phenomenology

`phase1/SCOPE.md` defines Phase 1 as a narrow, foundational phase whose sole purpose is to establish a minimal non-cancellation principle (the Origin Axiom) in controlled toy ensembles and demonstrate that imposing a global amplitude floor prevents perfect destructive interference. It explicitly states that Phase 1 makes no phenomenology, flavor physics, θ★, φ, or unification claims and that any interpretation outside these toy ensembles is out of scope.

`phase1/README.md` repeats this: Phase 1 is the “Minimal Origin Axiom Core”, focused on toy phasor ensembles, residual amplitude floors, and clear numerics, with explicit statements that no cosmological constant solution, no data fits, and no real-universe predictions are claimed.

The Phase 1 paper’s introduction (`01_intro.tex`) describes the cosmological constant problem and the general “why not exactly zero?” question and then clearly separates what Phase 1 does and does not claim. It explicitly states that the work does not solve the cosmological constant problem, does not fix the numerical value of any physical vacuum energy scale, and does not claim phenomenological predictions. A “Scope and non-claims” paragraph in the introduction mirrors the text in `phase1/SCOPE.md`: Phase 1 isolates a structural question in toy ensembles and does not interpret results as physical predictions.

On the scope axis, the SCOPE file, README, and paper introduction are aligned: they present Phase 1 as a minimal, toy-level test of a non-cancellation axiom, with explicit non-claims regarding cosmology and phenomenology.

## 3. Axiom and toy ensembles vs. CLAIMS and ASSUMPTIONS

`phase1/CLAIMS.md` lists the main Phase 1 claims:

- C1 (Axiom): a strict non-cancellation bound exists, |A| > ε_floor > 0, treated as a postulate in Phase 1 (not derived).
- C2 (Toy lemma): forbidding perfect cancellation in finite sums of complex contributions implies a residual amplitude floor for non-π twists, with analytic and numeric demonstrations in toy phasor ensembles.
- C3–C5 (as sketched): numeric demonstrations that the constrained residual saturates at ε_floor while the unconstrained case scales to zero with system size and that constraint enforcement does not introduce order-one energy artifacts in the toy model, within tolerance.

These are explicitly framed as toy-theory claims: they pertain to finite phasor ensembles, the operational encoding of the axiom, and scaling properties in controlled numerics, not to real-world fields or cosmology.

The paper’s axiom section (`02_axiom.tex`) states the minimal non-cancellation axiom in essentially the same form as C1: a global complex amplitude A is subject to |A| > ε_floor > 0, treated as an axiom in Phase 1 rather than derived from a local Lagrangian. It explicitly notes that ε_floor is free in Phase 1 and that relating ε_floor to a physical energy density is deferred to Phase 2. This matches the C1 status (postulate) in the claims register.

The toy model section (`03_toy_models.tex`) constructs finite phasor ensembles and introduces a twist parameter θ as a control knob for cancellation. It treats θ as a generic “twist” and is careful to treat irrational choices as a class (“irrational” vs “rational”) rather than singling out a distinguished irrational. A paragraph in that section states that Phase 1 remains θ-agnostic and that any later claim about a specific irrational (e.g. φ^φ) must be justified by an independent principle and is explicitly deferred. This is consistent with the absence of any θ★-specific claim in `phase1/CLAIMS.md` and with the non-claims in `phase1/SCOPE.md` and `phase1/ASSUMPTIONS.md`.

`phase1/ASSUMPTIONS.md` (not reproduced here) enumerates modeling assumptions (e.g. choice of ensemble, finite system sizes, numerical tolerances, and the operational encoding |S| → max(|S|, ε_floor)). The toy-model section’s construction of ensembles and the methods section’s description of numerical sweeps match the kind of assumptions listed in `ASSUMPTIONS.md`: they are toy-level, finite-dimensional, and explicitly flagged as such.

Overall, the axiom and toy constructions in the paper are consistent with the claims register and assumptions file: Phase 1 posits a non-cancellation floor as an axiom and demonstrates its implications in finite ensembles without promoting any particular θ or interpreting results as real-world physics.

## 4. Numeric results and scaling vs. CLAIMS and outputs

`phase1/CLAIMS.md` includes claims about scaling (constrained vs unconstrained residuals) and energy discipline. The numeric parts of the paper (results and methods sections, `04_methods.tex` and `05_results.tex`) describe sweeps over system size and configurations that:

- show unconstrained residuals trending toward zero as N grows (e.g. random-walk style scaling),
- show constrained residuals saturating at the imposed ε_floor, and
- check that the constraint implementation does not inject order-one energy artifacts within the specified tolerances of the toy setup.

The Phase 1 repo structure under `phase1/outputs/` and `phase1/artifacts/` mirrors the claims register’s artifact references (figures, scaling curves, and sweep tables). The methods and results sections refer to these figures and tables in ways that match the claims ledger entries (e.g. C2 referencing a phasor toy figure, C4 referencing a scaling curve, C5 referencing an energy-discipline table or log).

Nothing in the Phase 1 paper’s results sections contradicts the claims ledger: the paper does not claim a universal scaling law beyond the documented toy models, does not extrapolate the numeric residuals to physical vacuum energy scales, and treats all results as toy-demonstrations of the axiom rather than direct cosmological claims. This matches the status and wording of C2–C5 in `phase1/CLAIMS.md`.

## 5. Reproducibility and environment vs. REPRODUCIBILITY.md and repo layout

`phase1/REPRODUCIBILITY.md` states that all Phase 1 figures and tables can be regenerated from version-controlled code and config, that Phase 1 uses a pinned Python environment (via `requirements-phase1-freeze.txt`), and that runs are controlled by YAML configurations under `phase1/config/`. It describes how to create a virtual environment (e.g. via `uv venv`), install dependencies, and run the Phase 1 sweeps and figure-generation scripts.

The repository structure under `phase1/` matches this description:

- `config/phase1.yaml` and variants (e.g. `phase1_binding_on.yaml`, `phase1_binding_off.yaml`) define the parameter sets used for different runs.
- `src/` contains the implementation of the toy ensembles, the non-cancellation floor, and the sweep/figure scripts.
- `outputs/` contains tables, logs, and run IDs that correspond to sweep results and tests.
- `artifacts/origin-axiom-phase1.pdf` is the paper built from `paper/main.tex`, while phase1-level figures and tables are generated by reproducible scripts.

The LaTeX sources (`04_methods.tex` and `05_results.tex`) describe the numeric experiments in a way that matches the REPRODUCIBILITY contract: figures and tables are described as outputs of specific classes of sweeps and environment assumptions, not as ad hoc hand-built results. There is no evidence that the paper relies on untracked or non-reproducible computations.

Thus the Phase 1 reproducibility protocol, the actual repo layout, and the paper’s methods/results sections are aligned: they all insist that Phase 1 numerics are generated by deterministic, version-controlled scripts with explicit configuration and pinned dependencies.

## 6. Non-claims and boundaries

Across Phase 1 documents (SCOPE, README, CLAIMS, ASSUMPTIONS, REPRODUCIBILITY, paper sections), the following non-claim boundaries are consistently enforced:

- Phase 1 does not attempt to solve the cosmological constant problem or to match any observational data.
- Phase 1 does not fix a physical value of ε_floor or interpret ε_floor as a measured vacuum energy density; it treats ε_floor as a free parameter in a toy axiom.
- Phase 1 does not promote any particular θ or irrational number (including φ or φ^φ) to a distinguished status; it treats “irrational” as a class and defers any selection of a specific irrational to later phases under separate principles.
- Phase 1 does not make claims about fields, FRW dynamics, or real cosmological histories; it restricts itself to finite phasor ensembles and toy implementations of non-cancellation.

These non-claims are spelled out in `phase1/SCOPE.md` and reinforced in the introduction and toy-model sections of the paper. There is no evidence that the paper text overreaches beyond these boundaries, and the claims register does not include any real-universe predictions.

## 7. Potential future doc rungs (not yet executed)

This memo suggests, but does not enact, the following documentation rungs for later passes:

- Add a short pointer from `phase1/SCOPE.md` or `phase1/README.md` to `phase1/PHASE1_ALIGNMENT_v1.md` as the canonical alignment memo for Phase 1.
- If figure and table numbering in the Phase 1 paper stabilises (or changes), update `phase1/CLAIMS.md` artifact references to use stable labels (figure/table numbers or explicit file paths under `phase1/outputs/` and `phase1/artifacts/`).
- If additional toy models or mechanism variants are added to Phase 1, ensure that any new claims are first introduced in `phase1/CLAIMS.md` and only then reflected in the paper, not the other way around.

These steps are deferred to later doc-audit or promotion rungs and do not change the current Phase 1 scope, claims, or reproducibility contract.
