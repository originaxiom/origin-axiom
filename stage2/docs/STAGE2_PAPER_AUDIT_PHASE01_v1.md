# Stage 2 paper audit — Phases 0 and 1 (governance and axiom)

Status (2026-01-11): This note records a Stage 2–era consistency scan of the Phase 0 and Phase 1 papers against the current program structure. It is descriptive only and does not propose edits to the LaTeX sources.

## 1. Inputs and sections inspected

Papers:

- `artifacts/origin-axiom-phase0.pdf` (“Phase 0: Contracts for a Reproducible Non-Cancellation Program”)
- `artifacts/origin-axiom-phase1.pdf` (“The Origin Axiom (Phase I): A Minimal Non-Cancellation Principle and a Reproducible Toy Demonstration”)

Phase 0–1 docs:

- `phase0/CLAIMS.md`, `phase0/CONTRACTS.md`, and related governance docs
- `phase1/SCOPE.md`, `phase1/ROLE_IN_PROGRAM.md`, `phase1/REPRODUCIBILITY.md`
- global docs: `docs/PHASES.md`, `docs/CLAIMS_INDEX.md`, `docs/PROJECT_OVERVIEW.md`

Stage 2 context:

- `stage2/docs/STAGE2_MASTER_VERDICT_v1.md`
- Phase 2–4 paper audit notes
- Alignment memos for Phases 2–5 (to ensure the higher phases are using Phase 0–1 as intended)

Paper sections explicitly inspected:

- Phase 0: abstract, introduction, governance vocabulary, corridor governance, reproducibility contract
- Phase 1: abstract, introduction, axiom statement, toy models, methods, and Phase I claims section

The aim is to confirm that Phase 0–1 still provide a clean governance and axiom foundation for the Stage 2 snapshot and that later phases and belts have not drifted away from what these papers declare.

## 2. Phase 0 paper: governance and contracts

The Phase 0 paper defines the governance layer of the Origin Axiom program. It introduces the basic vocabulary of claims, evidence, canonical artifacts, provenance, falsifiers, and phase scope contracts, and it formalises corridor governance and reproducibility rules.

Key points from the paper:

- Phase 0 makes no physics claims; it is explicitly a governance and method phase.
- It defines corridor governance with an emphasis on append-only history and explicit narrowing, preventing silent tightening of global filters such as θ-corridors.
- It demands that every claim has an ID, statement, explicit evidence pointers, non-claim boundaries, falsifiers, and provenance.
- It sets a reproducibility contract, including run-bundle structure and failure handling that quarantines broken evidence rather than hiding it.

Comparing this with the current repo:

- Later phases and Stage 2 belts are structured in ways that respect the Phase 0 vocabulary and contracts. Claims are separated from non-claims, evidence is tied to specific files, and reproducibility and provenance are explicitly tracked.
- Stage 2 belts (FRW, mechanism, joint, data-probe, doc audit) are downstream diagnostics that do not silently revise Phase 0 rules; they operate within the governance framework defined by Phase 0.
- No later doc claims to override or weaken the Phase 0 governance principles; instead, Phase 0 is cited and used as the reference for locking, gating, and archiving decisions.

Verdict: the Phase 0 paper remains a faithful description of the project’s governance constitution at the Stage 2 snapshot, and the current repo structure complies with its core principles.

## 3. Phase 1 paper: axiom and toy existence proof

The Phase 1 paper introduces a minimal θ-agnostic non-cancellation axiom prohibiting perfect cancellation of a global complex amplitude |A| > ε > 0. It presents finite-dimensional toy models and a reproducible lattice existence proof showing that enforcing a non-cancellation floor prevents deep destructive interference while remaining dynamically stable. It makes clear that the axiom is introduced as a global constraint rather than a local field-theoretic modification and that Phase 1 deliberately isolates the principle from phenomenology and parameter extraction.

Key points from the paper:

- The axiom is stated and interpreted as a minimal global non-cancellation condition on a complex amplitude.
- Toy phasor ensembles and simple constructions provide intuition and confirm that the axiom is non-vacuous.
- A lattice existence proof demonstrates a concrete setting in which a non-cancellation floor can be enforced without numerical instability.
- Phase I claims are limited to existence and stability within the constructed toy systems; cosmological interpretation and θ★ selection are explicitly deferred to later phases.

Comparing this with the current program and Stage 2 verdict:

- Later phases (2–4) and Stage 2 belts treat the Phase 1 axiom as a guiding principle rather than as a fully physical law. They build toy mechanisms and FRW stubs consistent with the non-cancellation idea but do not retroactively reinterpret the Phase 1 claims.
- The Stage 2 master verdict, which focuses on broad viability bands, redundant diagnostics, and negative θ★ results in the present toy universe, is compatible with Phase 1’s modest claims. Nothing in Stage 2 contradicts the Phase 1 existence and stability statements.
- Phase 1 is not misused as a source of strong physical predictions elsewhere in the docs; the global docs and alignment memos keep its role as an axiom and toy existence phase clear.

Verdict: the Phase 1 paper still accurately represents the axiom and toy demonstration layer of the program. Later phases and Stage 2 diagnostics extend the story but do not conflict with its claims or non-claims.

## 4. Global consistency conclusion

From the Stage 2 perspective:

- Phase 0 provides a stable governance constitution that the current repo and Stage 2 belts respect.
- Phase 1 introduces the non-cancellation axiom and toy existence proof in a way that is still compatible with how later phases and belts talk about the mechanism and FRW stubs.
- There is no tension between the Phase 0–1 papers and the Stage 2 master verdict; rather, Phase 0–1 provide the conceptual and governance foundations that make the later belts auditable.

Any future edits to Phase 0–1, if undertaken, can be extremely conservative and focused on minor clarifications or explicit cross-links to later phases rather than changes in claims or structure.
