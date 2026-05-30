# Papers

Status: paper-candidate registry. This directory tracks possible papers,
technical notes, public reports, and archival artifacts. It does not promote
claims.

## Rule

```text
paper candidate != proven claim
paper candidate != publication-ready result
paper candidate = a coherent evidence cluster worth auditing
```

The governed source of truth remains `CLAIMS.md`. A paper card may organize a
result cluster, but it cannot upgrade the status of that result.

## Structure

```text
CANDIDATES.md = registry of candidate outputs
ARTIFACT_MANIFEST.md = manifest for copied PDFs, source files, data, and logs
REVIEWABILITY_INDEX.md = router for mathematical validation packets
FALSIFIABILITY_MATRIX.md = status-change and kill/rescope matrix
VALIDATION_WORKFLOW.md = process for auditing, triaging, and acting on findings
VALIDATION_LEDGER.md = public-safe ledger for validation outcomes and actions
candidates/ = one directory per candidate with a PAPER_CARD.md
```

## Readiness Labels

```text
SEED = idea exists, evidence not organized
EVIDENCE_EXISTS = local evidence exists but is not paper-shaped
NEEDS_VALIDATION = promising but must survive independent checks
DRAFTABLE = thesis, evidence, controls, and citations are coherent enough to draft
PUBLIC_DRAFT = released as preprint/report/website PDF
ARCHIVED_ONLY = historically useful but not a current research result
KILLED = failed under audit
```

## Draft Gate

A candidate is not draftable until it has:

```text
one-sentence thesis
clear scope
explicit non-claims
source or literature positioning
evidence files
reproduction command or proof path
negative controls where needed
known failure modes
one honest conclusion
```

For speculative models, also state:

```text
which assumptions are inserted
which quantities are derived
which quantities are fitted or free
which observations would kill the model
```

## Distribution Ladder

Use a ladder rather than depending on one venue:

```text
1. local registry in this directory
2. repo-hosted paper card
3. generated PDF attached to a release
4. website page generated from the atlas
5. stable archive for citation
6. preprint service when the draft fits the platform
7. journal or conference only when a specific venue fits
```

Before any public upload, check the current policy of the target platform.
