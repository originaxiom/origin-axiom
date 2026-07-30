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
| `B537` | **GAP** | The Markov-type surface `x²+y²+z²−xyz=c` and SL(2,ℤ) trace triples `(tr A, tr B, tr AB)`. **Genuine object topic, no motif covers it** — the single real lexicon gap B821 identified. Worth a character-variety/Markov motif under its own seal. |
| `B679` | INSTRUMENT | An `engine_v7` gate-report patch, prepared and verified but not deployed; explicitly about a seat conduit that is not a repo-tracked file. |
| `B770` | INSTRUMENT | The closure census — Phase 0 bookkeeping over the programme's own arcs. |
| `B793` | INSTRUMENT | Gate 8R2-A, blocked on an **architectural finding about the B788 solver**. About the apparatus, not the object. |
| `B798` | INSTRUMENT | The algebraicity falsifier's power box — discharges review actions R32-4/R32-5 by pricing a `(d, H)` test budget. It **governs** an object claim without making one. *(Borderline: the falsifier it prices is load-bearing for B796, so if the lexicon ever gains a motif for falsifier design, revisit.)* |
| `B818` | INSTRUMENT | The verdict-vocabulary errors and the `RETRACTED` disambiguation. |
| `B819` | INSTRUMENT | The coverage-frame correction to B817. |
| `B821` | INSTRUMENT | The failed lexicon refresh — an arc about the lexicon, correctly invisible to it. |
| `B822` | INSTRUMENT | The gate fix; the arc whose own existence broke B822's ceiling and motivated this registry. |
| `B823` | INSTRUMENT | This registry itself. Its own arc went blind and demanded a row — the same self-reference that broke B822's ceiling, now resolving into a judgement to record instead of a number to bump. |

**Open `GAP` count: 1** (`B537`).
