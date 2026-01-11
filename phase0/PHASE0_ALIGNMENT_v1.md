# Phase 0 alignment memo (contracts, paper, and repo surface)

Status (2026-01-11): This memo records how the Phase 0 paper, scope/claims documents, and the current repository surface align. It is descriptive only and does not introduce new claims.

## 1. Inputs used for this alignment

This memo is based on:

- `phase0/SCOPE.md` – Phase 0 scope and non-claims.
- `phase0/CLAIMS.md` – Phase 0 claims ledger for governance and method.
- `phase0/REPRODUCIBILITY.md` – Phase 0 reproducibility contract.
- `docs/THETA_ARCHITECTURE.md` – θ and amplitude architecture note (explicitly marked as draft, non-binding).
- `artifacts/origin-axiom-phase0.pdf` – the Phase 0 paper (“Phase 0: Contracts for a Reproducible Non-Cancellation Program”).

Where needed, this memo refers to Phase 0 paper sections by their headings as they appear in the PDF (e.g. “Reproducibility contract: deterministic pipelines and run provenance”, “Falsifiability and failure modes”).

## 2. Phase 0 scope vs. paper abstract and introduction

`phase0/SCOPE.md` defines Phase 0 as the governance and method layer of the Origin Axiom program and states explicitly that Phase 0 does not make physics claims, does not fix a value of θ★, and does not interpret numerical results from later phases. Instead, it is responsible for claim taxonomy, phase contracts, θ-corridor and filter schemas, reproducibility, provenance, and archive/deprecation policies.

The Phase 0 paper’s title and abstract (“Phase 0: Contracts for a Reproducible Non-Cancellation Program”) match this description. The abstract states that Phase 0’s purpose is to make later phases auditable by requiring bounded claims, canonical and file-addressable evidence, explicit provenance, and explicit falsifiers and failure modes, and it explicitly states that Phase 0 makes no physics claims, does not assert a value of θ★, and does not infer cosmology or treat motivation as evidence.

The paper’s introduction further describes Phase 0 as defining the governance layer for a multi-phase program, with phases as governed units of work that must obey scope and claim contracts. This is fully consistent with the description in `phase0/SCOPE.md` and in the global repo docs under `docs/` (e.g. `docs/PROJECT_OVERVIEW.md`, `docs/PHASES.md`, and `docs/GATES_AND_STATUS.md`).

At the level of high-level purpose and non-claims, there is no conflict between the Phase 0 scope document, the Phase 0 paper abstract and introduction, and the global description of Phase 0 in the repo.

## 3. Claims ledger vs. paper structure

`phase0/CLAIMS.md` emphasises that Phase 0 does not make physics claims and instead defines governance, bookkeeping, and reproducibility contracts that later phases must obey. It organises Phase 0 claims as a ledger with stable IDs `P0-Cxx`, each with a statement, evidence pointers (files or sections), and non-claim boundaries.

From the paper’s table of contents and body, the main structural components (sections on project vocabulary for claims and evidence, canonical artifacts and provenance, corridor governance, reproducibility contract, and falsifiability/failure modes) align with the types of claims listed in the ledger:

- Sections that define “claim”, “evidence”, “canonical artifact”, and “provenance” correspond to governance claims about how claims must be structured and what counts as evidence.
- Sections on corridor governance and θ-corridors as schema-validated artifacts provide narrative backing for claims that corridors and filters are first-class, schema-governed objects with append-only histories.
- Sections on reproducibility (deterministic pipelines, canonical vs regenerable artifacts, run provenance, run bundles, and workflow contracts) correspond to reproducibility claims in the ledger.
- Sections on falsifiability and failure modes provide the structure and examples that Phase 0 expects later phases to adopt when specifying falsifiers and failure handling rules.

Within this slice, there is no evidence that the paper introduces physics claims or new claim types that are not present in `phase0/CLAIMS.md`. The paper’s narrative is consistent with the ledger’s emphasis on governance contracts and non-physics scope, and the ledger’s use of “Phase0-paper: <section>” references fits the structure of the PDF.

## 4. Reproducibility contract vs. paper Sections 5 and 6

`phase0/REPRODUCIBILITY.md` describes a reproducibility contract in terms of deterministic pipelines, canonical vs regenerable artifacts, run provenance, run bundles, workflow contracts, and failure handling. It treats these as requirements that later phases must satisfy for their artifacts to count as evidence.

The Phase 0 paper’s section “Reproducibility contract: deterministic pipelines and run provenance” and its subsections (canonical artifacts vs regenerable outputs, run provenance, run bundle structure, workflow contract, and reproducibility failure handling) mirror this content. The paper describes principles and required structure in language that is in line with, and slightly more expository than, the concise form used in `phase0/REPRODUCIBILITY.md`.

Sections on “Falsifiability and failure modes” (falsifiers, failure modes, and failure handling rules) similarly back the expectations expressed in the claims ledger and in the reproducibility file: Phase 0 requires explicit falsifiers and failure modes for each claim, and requires that failures be quarantined and recorded instead of silently erased.

On this axis, the paper, reproducibility file, and claims ledger are aligned: they all insist on deterministic pipelines, canonical artifacts, explicit run provenance, and explicit falsifiers and failure modes as preconditions for later phases’ claims to be considered valid.

## 5. θ and amplitude architecture vs. Phase 0 contracts

`docs/THETA_ARCHITECTURE.md` is explicitly marked as a draft, non-binding design document. It inventories how θ and the “global amplitude / residue” observable appear across phases, separates implementation details from candidate physical structure, states constraints that any canonical θ must satisfy if the program is to contact real physics, and sketches candidate architectures.

This is consistent with Phase 0’s role: Phase 0 is allowed to define constraints and governance for θ (e.g. that θ-corridors are schema-governed, that filters and corridors have append-only histories, and that architectural proposals must respect certain non-negotiable constraints), but it is not allowed to assert a specific value of θ★ or to make direct physics claims about cosmology or particle phenomenology.

The draft θ architecture note respects this by:

- being labelled as draft and non-binding,
- delegating binding claims to Phase 0–3 papers and co-located `CLAIMS.md` / `CLAIMS_TABLE.md` files,
- and treating itself as a speculative design note that is allowed to propose architectures and mark TODOs without changing claims.

As currently written, there is no conflict between Phase 0 contracts and the θ architecture note; the note lives in the allowed design space and is explicitly subordinated to the Phase 0–3 claims.

## 6. Non-claims, boundaries, and slack

Across the Phase 0 surface (paper, SCOPE, CLAIMS, reproducibility, θ architecture note, and global docs), the following non-claim boundaries and slack are consistent:

- Phase 0 does not make physics claims about θ★, cosmology, or particle phenomenology.
- Phase 0 defines governance and reproducibility contracts that later phases must obey (claims ledger structure, canonical artifacts, provenance, corridor governance, falsifiers, failure modes).
- Phase 0 can specify constraints that any canonical θ and associated amplitudes must satisfy, but it does not choose θ★ or infer physical predictions.
- Design notes like `docs/THETA_ARCHITECTURE.md` are allowed to speculate under explicit draft labels and do not override claims.

The main slack is conceptual rather than contradictory: Phase 0 defines strong governance and reproducibility constraints but leaves open exactly which θ-architecture (and which physical interpretation of θ and the residue) will be advanced in later phases. That slack is intentional: it is the job of Phases 1–3 to explore concrete mechanisms and diagnostics under the Phase 0 contracts.

## 7. Potential future doc rungs (not yet executed)

This memo suggests, but does not enact, the following possible future documentation rungs:

- Add a short pointer from `docs/PHASES.md` or `docs/PROJECT_OVERVIEW.md` to `phase0/PHASE0_ALIGNMENT_v1.md` as the canonical alignment memo for Phase 0.
- If the Phase 0 paper evolves, update evidence pointers in `phase0/CLAIMS.md` to reference specific sections by number or title in a consistent way.
- If new θ or amplitude architecture notes are added, ensure they are labelled consistently with `docs/THETA_ARCHITECTURE.md` (draft, non-binding) and that they remain subordinate to Phase 0–3 claims.

These are deferred to later doc-audit or promotion rungs and do not change the current Phase 0 contracts or claims.
