# B824 — the character-variety motif FAILED its vacuity ceiling; "character variety" is ambient

cc banking seat, 2026-07-30. **Prereg `3ba7eacea2d19002`, sealed at `73ef6f65` before the edit.**
Repository-instrument scope; Gate 5 untouched.

## Verdict: FAILURE on criterion 2. Reverted; `B537` stays a recorded `GAP`.

| sealed criterion | required | got | |
|---|---|---|---|
| 1 — hits `B537` | yes | **yes** | ✅ |
| 2 — matches ≤ 15 % of corpus | ≤ 15 % | **18.4 %** (138/749) | ❌ |
| 3 — not ≥ 90 % inside any single existing motif | < 90 % | **76.8 %** (in `firewall`) | ✅ |

**My declared worry was wrong.** I predicted criterion 3 would be the dangerous one — that the motif
would turn out to be `trace_map` renamed, since `trace_map` already carries `Fricke.Vogt` and the
Markov surface *is* the Fricke identity's level set. **It was not redundant at all** (76.8 %, and
against `firewall` rather than `trace_map`). The kill came from the ceiling I expected to clear.

## The diagnosis, and it is the same lesson one level down

Per-pattern corpus share:

| pattern | share |
|---|---|
| **`character variety`** | **13.8 %** ← the whole overshoot |
| `xyz` | 4.1 % |
| `Markov` | 4.0 % |
| `x²+y²+z²` | 3.3 % |
| `trace coordinates` | 1.9 % |
| `(tr A, tr B, tr AB)` | 1.3 % |
| `trace triple` / `Fricke cubic` | 0.5 % each |
| `relative character` | 0.0 % |

> **"Character variety" is this programme's subject matter, not a topic within it.** One pattern
> carried 13.8 % of the corpus on its own — exactly the shape that killed B821, where `prereg`
> (27.6 %) made the meta-layer motif ambient. **B821's failure was about the ambient *method*;
> B824's is about the ambient *object*.**

The genuinely distinguishing content of `B537` is narrower: the **Markov cubic** and **trace
triples**, not "character variety" in general.

## Why this was not silently retried

The seal said *"on any failure: revert, and `B537` stays a recorded `GAP`."* It has been reverted,
and the registry still lists `B537` as open. **Tightening the patterns and re-running under the same
prereg would be tuning until it passes** — the criteria would be unchanged but the exposure would
not be recorded.

**B825 makes exactly one further attempt, under a fresh seal, with a cap of two attempts total
declared in advance**, so the multiple-comparison exposure is visible rather than absorbed. That cap
is the point: without it, "iterate the patterns" has no natural stopping rule and would eventually
produce a passing motif by search rather than by insight.

## What is worth keeping regardless of B825

**A gap honestly left open is better than one closed by a label that carries nothing.** If B825 also
fails, `B537` remains a recorded `GAP` in `docs/atlas/BLIND_ARCS.md` — which is a true statement
about the instrument, and strictly more useful than a motif that matches a sixth of everything.

`tests/test_b824_charvar_motif.py`
