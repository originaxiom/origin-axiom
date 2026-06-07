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
| `CLAIMS.md` | the living ledger of proven results (P1–P16) | — (it *is* the ledger) |
| `src/`, `tests/` | the tested package locking the proven core | via the gates only |
| `frontier/` | speculative-but-computed `open` work, quarantined + gated; the `B`-probes | only through `conditional → proven` |
| `papers/` | paper-candidate registry; the `V`-validation-ledger | — |
| `docs/atlas/` | navigation + the **FAILURE_ATLAS** (dead ideas, first-class negatives) | — |
| **`speculations/`** | the **evolving-ideas** room: the catalog `S001…S021`, the "final theory" exercise, the **HELD** value-matches, the **DEAD** tombstones, the `archive/` | **never** |
| **`philosophy/`** | the **motivation** layer: `P000–P003` + the `P1–P5` argument register + `METALLIC_FOUNDATIONS` | **never** |
| **`story/`** | the **honest narrative** — how the project actually unfolded, with `V`/`B` traceability, no duplicated math | **never** |
| **`knowledge/`** | self-contained explainers `K001–K007` (stubbed; lowest priority) | **never** |
| `paths/` | the systematic emergence-mechanism survey (`E`-paths) | via mathematization |
| `legacy/` | frozen prior history; never edited; never a source of claims | — |

## The discipline in one breath

The proven mathematics (the tower, degree=rank, the plethysm, P1–P16) stands **without a word** of `philosophy/`,
`speculations/`, or `story/`. The **ρ_n catalog proof** is the central math target. The **physics chapter is
CLOSED**. The two lines never crossed: **numerology** and **tower-eigenvalues = masses**. Bravery is preserved —
it lives in a labeled, versioned room (`speculations/`) with an honest door.

See: `speculations/GOVERNANCE.md`, `philosophy/GOVERNANCE.md`, `story/GOVERNANCE.md`, `GOVERNANCE.md` (root).
