# Archive and Deprecation Policy

This repo is intentionally kept clean and reproducible.

- Old exploratory notebooks, intermediate runs, and bulky experiment dumps should live in a separate legacy archive (outside git) unless explicitly promoted into a Phase with canonical artifacts.

Promotion rule:
Exploration → Phase candidate → bounded claims → canonical figures → reproducibility contract → merge.


## Legacy migrations (origin-axiom-legacy → phased repo)

The file `docs/LEGACY_MIGRAIONS_PHASE0_MAP.MD` records how legacy runs and artifacts
from the older `origin-axiom-legacy` repository map into the phased program under
Phase 0 contract rules. It is a governance and provenance index, not a claim
document, and should be consulted when:

- deciding whether a legacy result is a candidate for promotion into a Phase, or
- checking how a particular legacy run relates to current Phase 0–5 artifacts.

Legacy content remains in the archive unless and until it is explicitly promoted
through a Phase 0 gate and registered in the phase-local `CLAIMS.md` and
`docs/CLAIMS_INDEX.md`.

## Stage 2 archive status map

In addition to this policy document and Phase 0 contracts, the current practical
map of canonical vs archived/experimental areas is maintained in:

- `stage2/docs/STAGE2_ARCHIVE_STATUS_v1.md`

That document records, at the repository level, which trees are treated as
canonical phases (e.g. `phase0/`–`phase5/`), which are Stage 2 diagnostic belts
(e.g. `stage2/`), and which are archived or experimental areas (for example,
`experiments/phase3_flavor_v1/` and the Phase 5 sandbox files). It should be
consulted together with this archive policy when deciding where new work lives
and how legacy artifacts are classified.
