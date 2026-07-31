# B834 — wave 3b: κ replicates to four decimal places, the drift replicates unanimously, and coverage closes

cc banking seat, 2026-07-30. Same sealed prereg `ddb2ff0b25c2d777`, re-run on the **correct** frame
after B832's execution error. Repository-instrument scope; Gate 5 untouched.

## 1. κ replicates — three measurements, one instrument

| run | block | readers | κ |
|---|---|---|---|
| wave 2 | 15 arcs, **2 categories** (accidentally) | 12 | **0.9312** |
| wave 3a | 16 arcs, **4 categories** | 12 | **0.9305** |
| **wave 3b** | **same 16 arcs**, independent readers | 12 | **0.9300** |

> **Three measurements spanning 0.0012.** Wave 3b is a genuine replication — the same calibration
> block, a fresh panel — and it lands on wave 3a's value to three decimal places.

**This closes my failed prediction definitively.** I expected four categories to score *lower* than
two. It does not: **agreement is a property of the panel, not of the vocabulary's width.**

## 2. The corpus divergence replicates, and hardens to unanimous

| arc | corpus | wave 3a | **wave 3b** |
|---|---|---|---|
| **B61** | `OPEN` | 12/12 `PROVED` | **12/12 `PROVED`** |
| **B556** | `OPEN` | 11/12 `PROVED` | **12/12 `PROVED`** |
| **B746** | `NEGATIVE` | 12/12 `PROVED` | **12/12 `PROVED`** |

Consistency: **78.6 %** (3b) against **79.7 %** (3a) — and **exactly the same three arcs, in exactly
the same direction, with B556 hardening from 11/12 to 12/12.**

> **24 independent readers across two panels, judging blind: 24/24, 23/24, 24/24 against the
> corpus.** A single-panel result is an opinion; a replicated unanimous one across independent
> panels is a measurement.

## 3. What the three are, and the rule that resolves them

All three are the **same shape: a verified core with an unsettled extension.** B556's own header
says it — *"the computational core is VERIFIED EXACTLY; the tower-as-physics-ladder reading is
banked as a labelled HYPOTHESIS."* B61 is *"not a symbolic proof"* at 22 of 24. B746 established a
two-column law **while gapping** the hypothesis it tested.

**The four-category vocabulary forces one label onto both halves.** The corpus resolved them toward
what remains unsettled; the panel toward what was established — and `PRACTICES` says the verdict
labels **what the arc established**. **The panel was reading the rule correctly.**

**All three relabelled to `PROVED`**, with the claim line now carrying **both halves explicitly**
(`ESTABLISHED: … UNSETTLED: …`), so nothing is lost by the relabel. **New rule registered in
`PRACTICES`** — *label a mixed arc by what it established, carry the unsettled half in the claim;
`OPEN` is for an arc that settled nothing.*

**B832 deliberately relabelled nothing on one panel's word.** With replication it is no longer one
panel's word.

## 4. The frame was correct this time

| | |
|---|---|
| verdicts **written** | **89** |
| **already authored — 0** | the frame was exact |
| no findings document — skipped | 45 |
| ambiguous directory (`B58`) | 1 |

**Zero already-authored skips** is the check that B832's hand-typed list failed: every arc sent was
genuinely unjudged. The args were copied verbatim from the computed file.

## 5. Coverage

> **756 of 803 arc ids carry an authored verdict — 94.1 %.** From 42.5 % at the start of this campaign.

**Corrected while writing this:** the generated ledger reports *"756 of 759"*, which is **99.6 % of
the ATLAS's population, not of the arc ids on disk** (803). I wrote the ledger's number down first.
**Two denominators again — the same composition error this session keeps producing, caught here by
my own coverage lock rather than by reading carefully.**

The residue is **47 ids**, of which **45 are directories holding no findings document at all** —
unwritable by design, not by omission.

## Carried

- The 45 no-document directories: decide whether each is a stub to retire or an arc awaiting a
  write-up. **Not a verdict problem.**
- `B58`'s three directories still defeat any single-id writer.

`tests/test_b834_wave3b.py`
