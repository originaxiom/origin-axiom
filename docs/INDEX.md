# The document map — what is living, what is reference, what is history

*Currency: 2026-08-14 (Review 46). **Re-stamp this line at every decadal review** — a
router that does not carry its own date is how this file went five weeks stale while
looking authoritative. (Nothing in this repo is deleted — records are the credibility
model, GOVERNANCE §1/§9; this map says what to read for the current state.)*

## ⚠ ENTRY PROTOCOL — read BEFORE working, not after

| if you are about to… | read FIRST |
|---|---|
| **anything at all, first session** | `docs/THE_END_TO_END_CHAIN.md` **PART VIII** (the whole chain in one paragraph) |
| **question the framework's foundations** | `philosophy/P000_what_is_not_nothing.md` — **the framework does NOT start from a 3-manifold; m004 is DERIVED at C6** |
| **ask "is this novel / is this ours?"** | `THE_END_TO_END_CHAIN.md` **PART 0** (+ §0.1's corrected attribution) — the claim is a COST claim (ZERO dials · THREE priced axioms · TWO undetermined), not a priority claim; `docs/NOVELTY_SWEEP_LEDGER.md` for what is already known outside |
| **call something a choice / say "E₆ is chosen"** | `THE_END_TO_END_CHAIN.md` **PART 0.5** — the forcedness census: 39 of 43 links forced, the stretch C6→C17 axiom-free, **E₆ is what level 15 factors into** (CRT + McKay); gate `scripts/checks/forcedness_census.py` (B1123) |
| **touch a gate or a firewall** | `WORKING_RULES.md` §6 (**Gate 5 = no SM quantities into CLAIMS.md — an OUTPUT firewall; zero-dials is guarded by construction, not by Gate 5**) · `philosophy/GATE5Q_PHENOMENOLOGY_FIREWALL.md` |
| **compare anything to measured physics** | `docs/INPUT_COMPLETENESS_LEDGER.md` — twelve items **plus the crossing lane's R1–R11, BOTH filled in the prereg as rows** (THE RECONCILIATION), before sealing; fetches state their release and check the mirror |
| **claim something is absent / unprecedented** | **check the aliases first**: `docs/CLOUD_ALIAS_TABLE.md` (the qB/qL resolver) and `TERMINOLOGY.md`'s multi-referent registers — one object wears many names here (one field `K` appears as `13³`, `√77`, `953`, "the S₃ cubic", "the weight field"). **A search result you do not open is not a search result.** |
| **reuse machinery** | `docs/TOOLBOX_LIVE.md` — the live one-pager (the historical body is frozen at `docs/TOOLBOX.md`) |

## Living (the current state — always start here)

| file | role |
|---|---|
| `docs/THE_END_TO_END_CHAIN.md` | **the chain, genesis → SM** — every link labelled, with its addendum-corrections carried at equal weight |
| `THE_CLAIM.md` | the one-page theorem: what is claimed, in the proof-form it is proved in |
| `docs/THE_FRAMEWORK.md` | the whole assembly by layers, with the level ledger and the walls |
| `README.md` | the front door: Review banners, newest first = the true current state |
| `docs/CAMPAIGN_STATUS.md` | **the live board** — what is computing now, last banked |
| `CLAIMS.md` | **the ledger** — proven · conditional · certified · open · dead |
| `GOVERNANCE.md` · `WORKING_RULES.md` | the constitution, and the working rules (**Gate 5 lives in §6**) |
| `docs/OPEN_LEADS.md` · `docs/OPEN_PROBLEMS.md` | the live frontier |
| `docs/progress/REVIEWS.md` | the decadal-review ledger |
| `CHANGELOG.md` · `PROGRESS_LOG.md` | recent history · append-only working log |

## The registers (permanent, load-bearing — consult by question, not by browsing)

| question | register |
|---|---|
| is there a theorem for this? | `docs/THEOREM_REGISTRY.md` · `docs/THEOREM_LEDGER.md` |
| what law governs this? | `docs/LAW_MAP.md` (§G = the programme's own method-laws) |
| was this sealed, and when? | `docs/SEAL_LEDGER.md` |
| has this failed before? | `docs/ERROR_LEDGER.md` · `docs/ARCHIVE.md` (dead ideas, with causes) |
| is this comparison legitimate? | `docs/KIND_TABLE.md` (kinds) · `docs/INPUT_COMPLETENESS_LEDGER.md` (method) |
| is this already known outside? | `docs/NOVELTY_SWEEP_LEDGER.md` |
| has this recurred? | `docs/RECURRENCE_ATLAS.md` + `scripts/atlas/query.py card` |
| what would count, and what would kill it? | `docs/WHAT_WOULD_COUNT.md` · `docs/FALSIFIER_REGISTER.md` · the kill graph (`frontier/B738_pathfinder_compiler/kill_graph.json`) |
| what machinery exists? | `docs/TOOLBOX_LIVE.md` |

## Reference (permanent, load-bearing)

| file | role |
|---|---|
| `docs/UNIQUENESS_THEOREM.md` · `docs/TRACE_SELECTOR_THEOREM.md` | formalized evidence for C1 / C5 |
| `docs/ARCHIVE.md` | the dead-ideas register (why each died — permanent) |
| `docs/HINT_LEDGER.md` · `docs/NOVELTY_AUDIT.md` | the staged-rigor registers (METHOD.md governs) |
| `docs/RECURRENCE_ATLAS.md` + `scripts/atlas/` | the re-runnable probe atlas (420 probes) |
| `docs/TOOLBOX.md` | **the reuse index** — engines, lemmas, design patterns, by applies-when |
| `METHOD.md` · `ARCHITECTURE.md` · `PROVENANCE.md` · `REPRODUCIBILITY.md` | protocol, rooms, lineage, repro |
| `frontier/B*/FINDINGS.md` | the probe corpus — every result, refutation, and tombstone, each with locks |

## Historical snapshots (dated; bannered; never a source of claims)

`AUDIT_REPORT.md` (2026-05-22 consolidation) · `docs/SESSION3_SYNTHESIS.md` ·
`docs/CROSS_SESSION_2026-06-11_disposition.md` · `docs/STRATEGIC_SYNTHESIS.md` (2026-06) ·
`docs/UNIFIED_STATE.md` · `docs/RECONTEXT_AUDIT_AND_MASTERPLAN_2026-07.md` (2026-07-01) ·
`legacy/` (frozen prior history, GOVERNANCE §9) · `ROADMAP.md` (phase-level, low-churn)

## The governed rooms (one-way firewall; never promote to CLAIMS)

`speculations/` · `philosophy/` · `story/` · `knowledge/` — each with its own GOVERNANCE file; see
`ARCHITECTURE.md` for the rules. Surveyed 2026-07-03: no room makes ledger-state assertions — their
content is self-describing and unaffected by the promotion audit.

## Papers (`papers/`)

The write-up room: the flagship manuscript + `metallic_one_object/SYNTHESIS.md` (the four-faces map),
`VALIDATION_LEDGER.md` (V1…), `REVIEWABILITY_INDEX.md`, `FALSIFIABILITY_MATRIX.md`, `CANDIDATES.md`.
Paper claims cite probes and locks directly; the ledger is the arbiter where they overlap.
