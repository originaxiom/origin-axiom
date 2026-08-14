# B838 — the lexicon re-grounding is TESTED AND DECLINED: K023–K025 are syntheses, not topics

cc banking seat, 2026-07-30. Repository-instrument scope; Gate 5 untouched. Answers **R35-7**, open
since B806 and carried through five reviews.

## The standing call

B806 observed that the atlas lexicon is grounded in **K001–K022** and that **K023, K024, K025 are
not in its grounding**, and called for a full re-grounding. That has been carried as an open item
ever since — never tested, only deferred.

## It is now tested, and it does not yield a motif

**The diagnostic B824 taught me to run first** — measure candidate term frequency *before* sealing an
attempt — settles it without one:

| candidate, drawn from K023–K025 | arcs | share | |
|---|---|---|---|
| **`forcing` / `forced`** | 320 | **41.9 %** | **ambient** — worse than `character variety` (13.8 %), which killed B824 |
| `forces` | — | 13.6 % | ambient |
| `escape` | 43 | 5.6 % | viable band, but generic |
| `anatomy` | 20 | 2.6 % | viable band, but generic |
| `recurrence` | 16 | 2.1 % | names the **instrument**, not the object |
| **`held slot`** | **1** | **0.1 %** | a K025 coinage that appears in **one** arc |
| **`two ingredients`** | 1 | 0.1 % | likewise |
| `one root` | 3 | 0.4 % | likewise |

Widening to the 60 commonest K023–K025 terms, **23 land in the viable 2–15 % band — and they are
generic English**: `conserved`, `dynamics`, `objects`, `probes`, `product`, `scripts`, `meeting`.
**Vocabulary, not topics.**

> **Every distinctive K023–K025 term is either AMBIENT (41.9 %) or ABSENT (0.1 %). There is no
> middle.** A motif built from the first is a catch-all that fails B825's 15 % ceiling; one built
> from the second matches nothing. **Neither is a lexicon improvement.**

## Why — and this is the part worth keeping

**K023–K025 are retrospective SYNTHESES, not new topics.** K023 *is* the Recurrence Atlas — the
instrument itself, and B821 proved the meta-layer cannot be a motif because it is the corpus's
ambient register. K024 (*the forcing map*) and K025 (*the one root and the held-open slot*) name
**structures across already-indexed material**, in coinages that live in the explainer and nowhere
else.

> **A motif lexicon indexes TOPICS. A synthesis does not add a topic — it re-describes ones already
> indexed.** So the K-layer growing past K022 does **not** imply the lexicon is behind it.

**B806's premise was that a K-layer entry not represented in the lexicon is a gap. That premise is
wrong for syntheses**, and K023–K025 are all three syntheses.

## R35-7: CLOSED, not deferred

The lexicon needs no re-grounding on K023–K025's account. **What B806 correctly identified — that the
lexicon is frozen and hand-authored — remains true and remains recorded** in `BLIND_ARCS.md`, which
states in place that an empty `GAP` column is not a finished instrument. The single genuine gap
B821 found was closed by B825.

**This closes a five-review carry with a computed reason rather than a sixth deferral.**

## What would re-open it

A new K-layer entry naming a **topic** — something the object *is* or *does* — whose vocabulary lands
in the 2–15 % band and is not ≥ 90 % contained in an existing motif. **The test is B825's, unchanged**,
and this arc's diagnostic is the cheap pre-check that decides whether to spend a seal on it.

`tests/test_b838_regrounding.py`
