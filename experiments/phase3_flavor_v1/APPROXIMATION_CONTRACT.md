# Phase 3 Approximation Contract

This contract distinguishes:
- **Exact:** Definitions, file formats, provenance rules, gating rules.
- **Approximate:** Fit ansatz choices, simplified mappings, toy model approximations inherited from Phase 2.

## Exact commitments
1. Every Phase 3 claim must map to an artifact (figure/table/run manifest).
2. All Phase 3 artifacts used in the paper must be reproducible from the repo (Level A/B), or verifiable via paper_bundle hashes (Level A).
3. All inference language must match the claim tier (fit result vs hypothesis vs interpretation).

## Approximate modeling (explicit)
- The θ fit is within a chosen ansatz class; changes require Scope Addendum.
- The θ→vacuum injection is a hypothesis layer on top of the Phase 2 mechanism.
- Any cosmological interpretation in Phase 3 is descriptive only unless explicitly derived and gated.

## Reporting rule
Every approximation used in a figure must be noted either in:
- figure caption, or
- the figure manifest JSON, or
- a dedicated appendix note.
