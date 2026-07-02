# Architecture — the one-page map

The repository keeps **proven mathematics** and **everything that motivates or speculates about it** in separate
rooms, connected by a **strictly one-way arrow**. This page is the map.

## The one-way arrow (the rule everything obeys)

```
   philosophy/   speculations/   story/                 frontier/   papers/   src/   CLAIMS.md
   (motivation)  (evolving ideas)(narrative)            (the proven & gated mathematics)
        │              │            │                          ▲
        └──────────────┴────────────┴───────  cite  ──────────┘
                         (B / V / P numbers, for traceability)

        ✗ the mathematics NEVER cites philosophy / speculations / story
```

A motivation/speculation/narrative doc **may cite** a proved result (`B`-probe, `V`-ledger, `P`-claim number) to
say *"this is the mathematics it points at."* The proven core — `CLAIMS.md`, `frontier/` FINDINGS, `papers/`
notes, the `V`-ledger, `src/` — **never cites the other direction.** If a motivational sentence is ever needed to
*support* a mathematical claim, the boundary has been crossed: restate it as neutral mathematics or drop it. (Root
`GOVERNANCE.md` §5/§8/§9.)

## The rooms

| Room | What it holds | Promotes to `CLAIMS.md`? |
|---|---|---|
| `CLAIMS.md` | the living ledger (`proven` P · `conditional` C · **certified data** E · `open` O · `dead` D; §5 gates + the §5.1 promotion-audit lane, 2026-07-03) | — (it *is* the ledger) |
| `src/`, `tests/` | the tested package locking the proven core | via the gates only |
| `frontier/` | speculative-but-computed `open` work, quarantined + gated; the `B`-probes | only through `conditional → proven` |
| `papers/` | paper-candidate registry; the `V`-validation-ledger | — |
| `docs/atlas/` | navigation + the **FAILURE_ATLAS** (dead ideas, first-class negatives) — **historical (B124-era); see its freeze banner** | — |
| `docs/OPEN_LEADS.md` | the **actionable-leads register** (`L1…L50`); the disposition column records what is done / withdrawn (grep before computing). The current frontier + its four specialist gates live in `docs/OPEN_PROBLEMS.md` | promotes via a `frontier/` probe → the gates |
| `docs/HINT_LEDGER.md` | the **hint register** — pre-decision observations (patterns, coincidences, anomalies, unasked questions); the generative counterpart to the `V`-ledger (governed by root `METHOD.md`) | promotes **to `OPEN_LEADS.md`**, never directly to CLAIMS |
| **`speculations/`** | the **evolving-ideas** room: the catalog `S001…S045`, the "final theory" exercise, the **HELD** value-matches, the **DEAD** tombstones, the `archive/` | **never** |
| **`philosophy/`** | the **motivation** layer: `P000–P013` + the `P1–P5` argument register + `METALLIC_FOUNDATIONS` | **never** |
| **`story/`** | the **honest narrative** — how the project actually unfolded, with `V`/`B` traceability, no duplicated math | **never** |
| **`knowledge/`** | self-contained explainers `K001–K022`, **all written** — the textbook layer (trace map, metallic family, Dickson tower, figure-eight/A-poly, opposition involution, 3d-3d, quasicrystal) + the `(n;trace,det)` determination, the `m=1` selections, **the object's proper name** (K010), the firewall-robust characterization (K018), the collective/multibody spectrum (K019), **the structural theorem as a Galois theorem + the four levels** (K020), **the founding identity `g=−R·L⁻¹`, the two ends, and where the values are/are not** (K021), and **the object as the symmetric centre — it forces the *form* of the deviation space, not the magnitudes** (K022) | **never** |
| `paths/` | the systematic emergence-mechanism survey (`E`-paths) | via mathematization |
| `legacy/` | frozen prior history; never edited; never a source of claims | — |

## The discipline in one breath

The proven mathematics (the tower, degree=rank, the plethysm, P1–P16) stands **without a word** of `philosophy/`,
`speculations/`, or `story/`. The **ρ_n catalog proof** is the central math target. The **physics chapter is
CLOSED**. The two lines never crossed: **numerology** and **tower-eigenvalues = masses**. Bravery is preserved —
it lives in a labeled, versioned room (`speculations/`) with an honest door.

See: `speculations/GOVERNANCE.md`, `philosophy/GOVERNANCE.md`, `story/GOVERNANCE.md`, `GOVERNANCE.md` (root).
