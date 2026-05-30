# Integration Manifest -- Atlas and Paper Roadmap

Status: public-safe migration manifest. No claims. This file is generated from
the local delta audit between the canonical repository and the private staging
workspace.

## Source And Destination

```text
canonical repo: /Users/dri/origin-axiom
staging workspace: /Users/dri/tem_zip
canonical base: 514c046 / session3-synthesis-freeze
planned branch: roadmap/atlas-paper-integration
```

The staging workspace is not a Git repository and should remain a private
research lab. The canonical repository should receive only curated, public-safe
artifacts.

## Delta Summary

The local delta audit compared non-cache, non-raw files from both trees:

```text
origin comparable files: 116
tem_zip comparable files: 2995
excluded private/cache/raw artifacts: 8069
common same hash: 36
common different hash: 23
only in origin: 57
only in tem_zip: 2936
```

The large delta is expected. Most `tem_zip` content is exploratory sandbox
material, raw campaign output, private audit inventory, or source-mining output.
It should not be bulk-copied.

## Migration Policy

Use these categories:

```text
COPY_SANITIZED = copy after public-safety scan
REWRITE_PUBLIC_SAFE = rewrite into neutral public documentation
SUMMARIZE_ONLY = migrate only a concise synthesis, not raw files
PRIVATE_ONLY = keep local; never commit
NEEDS_MANUAL_REVIEW = inspect before deciding
DO_NOT_MIGRATE = excluded from canonical repo
ALREADY_CANONICAL = already represented in the public repo
```

Public-safety rules:

```text
no raw chat transcripts
no model or private-tool names in public migration docs
no private workflow narration
no third-party private identity details
no local whole-computer manifests
no downloaded PDFs unless explicitly approved and licensed
no large campaign JSONL/result logs
no claims beyond CLAIMS.md status labels
```

## Migration Batches

### R0 -- This Manifest

Status: complete (`e1bf927`).

Destination:

```text
docs/atlas/INTEGRATION_MANIFEST.md
```

Purpose:

```text
record what will migrate
record what will stay private
make migration auditable before adding atlas or paper content
```

### R1 -- Atlas Skeleton

Status: complete (`973e77f`).

Public-safe source material:

```text
/Users/dri/tem_zip/docs/RESEARCH_ATLAS_PLAN.md
reader-experience architecture note from local staging
/Users/dri/tem_zip/docs/PAPER_CANDIDATE_PIPELINE.md
```

Destination:

```text
docs/atlas/README.md
docs/atlas/RESEARCH_TREE.md
docs/atlas/AUDITOR_GUIDE.md
docs/atlas/FAILURE_ATLAS.md
docs/atlas/SUCCESS_ATLAS.md
docs/atlas/GLOSSARY.md
docs/atlas/SIMULATOR_ECOSYSTEM_MAP.md
```

Migration rule:

```text
rewrite, do not copy verbatim
remove private workflow references
preserve governance boundaries
```

### R2 -- Paper Candidate Registry

Status: complete (`a34df57`).

Public-safe source material:

```text
/Users/dri/tem_zip/papers/README.md
/Users/dri/tem_zip/papers/CANDIDATES.md
/Users/dri/tem_zip/papers/ARTIFACT_MANIFEST.md
/Users/dri/tem_zip/papers/candidates/PC01_obstruction_atlas/PAPER_CARD.md
/Users/dri/tem_zip/papers/candidates/PC02_conditional_rigidity/PAPER_CARD.md
```

Destination:

```text
papers/README.md
papers/CANDIDATES.md
papers/ARTIFACT_MANIFEST.md
papers/candidates/PC02_conditional_uniqueness/PAPER_CARD.md
papers/candidates/PC04_noncommutative_residue/PAPER_CARD.md
papers/candidates/PC06_quantum_selector_bridge/PAPER_CARD.md
```

Migration rule:

```text
paper candidate does not mean claim
PC02 is first ship target
PC04 and PC06 need new public-safe paper cards
PC01 remains a later obstruction-atlas candidate
```

### R3 -- Quantum Selector Campaign Synthesis

Status: complete (`7ef8e77`).

Private source material:

```text
/Users/dri/tem_zip/sandbox/continuous_explorer/runs/campaign_quantum_selector_v1_01/
/Users/dri/tem_zip/docs/progress/2026-05-28_quantum_selector_campaign_synthesis.md
```

Destination:

```text
docs/atlas/campaigns/quantum_selector_v1.md
```

Migration rule:

```text
summarize only
do not copy raw JSONL, scoreboards, downloaded source audits, or local run logs
preserve only counts, verdicts, survivors, killed routes, and theorem questions
```

Public-safe summary facts:

```text
cycles completed: 232
unique mechanisms evaluated: 50
verdicts: 6 survives, 28 stalled, 8 killed, 8 needs-expertise
main survivor: ordered noncommutative L/R residue
main obstruction: missing selector/functor/units/observable bridge
```

### R4 -- PC02 External-Review Packet

Status: complete (`b8ddd5a`).

Canonical source:

```text
docs/UNIQUENESS_THEOREM.md
tests/test_uniqueness_theorem.py
CLAIMS.md
```

Destination:

```text
papers/candidates/PC02_conditional_uniqueness/REVIEW_PACKET.md
```

Migration rule:

```text
do not alter C1 status
state substrate/order assumptions explicitly
write torsion lemma as the missing paper-grade proof task
```

### R5 -- PC04 Noncommutative Residue

Status: complete (`19c2e66`).

Private source material:

```text
campaign survivor summaries
frontier/V5_R27_noncommutative_cancellation_residue/
related V5 holonomy/residue synthesis files
```

Destination:

```text
papers/candidates/PC04_noncommutative_residue/PAPER_CARD.md
docs/atlas/nodes/noncommutative_cancellation_residue.md
```

Migration rule:

```text
formalize only as mathematical residue
do not claim physics
make distinguishability -> order a theorem task, not a slogan
```

### R6 -- PC06 State-Integral Selector

Status: complete (`d9a38cb`).

Private source material:

```text
quantum selector campaign theorem questions
source synthesis summaries
state-integral / thimble route notes
```

Destination:

```text
papers/candidates/PC06_quantum_selector_bridge/PAPER_CARD.md
docs/atlas/nodes/state_integral_selector_gap.md
```

Migration rule:

```text
state integrals are a serious host
no claim that a selector exists
record the needed theorem precisely
```

## Private-Only Material

Do not commit:

```text
legacy_audit/*.tsv
legacy_audit/FILE_MANIFEST.tsv
legacy_audit/THEMATIC_HITS.tsv
legacy_audit/SOURCE_INVENTORY.tsv
sandbox/continuous_explorer/runs/*/*.jsonl
sandbox/continuous_explorer/runs/*/scoreboard.json
sandbox/continuous_explorer/runs/*/events.jsonl
sandbox/continuous_explorer/runs/*/results.jsonl
sandbox/continuous_explorer/runs/*/sources/pdfs/
raw source-mining output
raw model/chat transcripts
whole-computer local path inventories
```

These may inform public summaries but should not appear directly in the public
repository.

## Same-Path Differences To Avoid Bulk Overwrite

Several canonical files differ between `origin-axiom` and `tem_zip`:

```text
CHANGELOG.md
CLAIMS.md
PROGRESS_LOG.md
PROVENANCE.md
README.md
ROADMAP.md
frontier/README.md
paths/PATHS.md
paths/README.md
```

Do not overwrite these from `tem_zip`. Update them manually only when a migration
batch requires a public-safe log/changelog/navigation entry.

## Verification Gate For Every Batch

Run from `/Users/dri/origin-axiom`:

```bash
python -m pytest -q
git diff --cached --check
git diff --cached --name-only
```

Public-safety staged scan:

```text
run the private sensitive-term scan used by the migration workflow
```

Expected result for public migration docs:

```text
no model or private-tool names
no raw transcript language
no private identity data
no accidental credentials
```

## Closure Batch

### R7 -- Integration Closure And Merge Gate

Status: complete (`f92b579`, merged to `main`, tagged `atlas-paper-integration-v1`).

Purpose:

```text
mark R0-R6 complete
record the final QA gate
merge the integration branch only if branch-wide checks pass
tag the integrated state after merge
```

Merge gate:

```text
git status clean on roadmap/atlas-paper-integration
python -m pytest -q passes
git diff --check main...roadmap/atlas-paper-integration passes
branch-wide public-safety scan passes
no raw/private files detected in changed paths
CHANGELOG.md and PROGRESS_LOG.md include closure entry
```

Planned tag after merge:

```text
atlas-paper-integration-v1
```

## Current Decision

R0-R7 are complete. `main` contains the atlas/paper integration v1 state, tagged
as `atlas-paper-integration-v1`. Future work should proceed as new focused
branches, starting with the PC02 conditional-uniqueness review track.
