# Blind arcs — the triage registry

**Generated-adjacent but HAND-MAINTAINED. The `atlas-lexicon-current` gate reads this file.**

A *blind* arc is one whose `FINDINGS.md` matches none of the atlas lexicon's motifs. B821 showed
that a raw blind **count** conflates three unlike things, and B822 showed that capping it with a
threshold is self-referential — the arc documenting the gate incremented the very count it was
fixing. So there is **no ceiling**. Instead every substantial blind arc (`FINDINGS.md` ≥ 2000 bytes)
must appear below with a disposition, and the gate fails **only on untriaged arcs**.

Thin arcs (< 2000 bytes) are excluded from the metric entirely — an arc reading *"Logged
observation, not a claim."* cannot match any lexicon and none should try.

## Dispositions

- **`GAP`** — a real object topic the lexicon does not cover. **This is open instrument work.**
- **`INSTRUMENT`** — an arc about the programme's own machinery, with no object content. An
  **object** atlas is *correct* to miss it. Not a defect, and not to be closed by adding a motif:
  B821 proved that a motif for the meta-layer matches 46 % of the corpus, because self-audit
  vocabulary is the house method's ambient register, not a distinguishing topic.

**Adding a row is a judgement, and it is recorded here rather than absorbed into a number.** The
honest failure mode of this design is labelling everything `INSTRUMENT`; that is visible and
auditable in a way a passing threshold never was.

| arc | disposition | why |
|---|---|---|
| `B679` | INSTRUMENT | An `engine_v7` gate-report patch, prepared and verified but not deployed; explicitly about a seat conduit that is not a repo-tracked file. |
| `B770` | INSTRUMENT | The closure census — Phase 0 bookkeeping over the programme's own arcs. |
| `B793` | INSTRUMENT | Gate 8R2-A, blocked on an **architectural finding about the B788 solver**. About the apparatus, not the object. |
| `B798` | INSTRUMENT | The algebraicity falsifier's power box — discharges review actions R32-4/R32-5 by pricing a `(d, H)` test budget. It **governs** an object claim without making one. *(Borderline: the falsifier it prices is load-bearing for B796, so if the lexicon ever gains a motif for falsifier design, revisit.)* |
| `B818` | INSTRUMENT | The verdict-vocabulary errors and the `RETRACTED` disambiguation. |
| `B819` | INSTRUMENT | The coverage-frame correction to B817. |
| `B827` | INSTRUMENT | The shadow-progress-log recovery and the fail-open-by-drift gate fix. About the repository's own bookkeeping; an object atlas is correct to miss it. |
| `B833` | INSTRUMENT | The negative-routing measurement and the arc-register vs kill-register unit mismatch. About the repository's own bookkeeping; an object atlas is correct to miss it. |
| `B836` | INSTRUMENT | Routing the negative backlog into the kill graph. About the repository's own bookkeeping; an object atlas is correct to miss it. |

**Open `GAP` count: 0.** `B537` was closed by B825's `markov_cubic` motif.

> **Zero open gaps means "no known uncovered object topic among substantial blind arcs" — NOT "the
> lexicon is complete."** The 18+1 motifs remain grounded in K001–K022 and unrevisited since
> 2026-07-01; B806's call for a full re-grounding is untouched.

**Known false-positive mode of `markov_cubic` (B825):** B821/B822/B823 dropped off this registry not
because they are about the Markov cubic but because they **quote** it while discussing the gap. A
regex motif matches *mentions*, not *subjects*. Recorded rather than filtered, because filtering
would mean classifying by topic — the thing B822 refused.
