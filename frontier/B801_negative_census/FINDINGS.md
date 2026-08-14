# B801 — the negative census: `kill_graph`'s 217 covers about two-thirds of the corpus's negatives

cc banking seat, 2026-07-29. The W1 pilot found 2 of its 5 negatives absent from `kill_graph` and
I flagged that as a lower bound rather than extrapolating from n = 5. This measures it properly.
Repository quality only; nothing to `CLAIMS.md`.

## Design, fixed before drawing

- **Pool:** the **557** arcs that have a `FINDINGS.md` and **no** record in `kill_graph.json`.
- **Sample:** **60**, drawn with a seed fixed *before* the draw (`20260729`), so the sample cannot
  be re-rolled toward a preferred answer.
- **Rule, stated before counting:** an arc is NEGATIVE when its **headline** is that a claim,
  candidate or mechanism was killed, refuted, found null, or shown not to hold.
- **Ambiguous arcs are called NON-negative.** This biases the estimate **down**, so the true count
  is likely at or above what follows, not below.

## Result

**12 of 60** sampled arcs are negatives ⟹ **p = 0.200** (95 % CI 0.099–0.301).

| | estimate | 95 % CI |
|---|---|---|
| unregistered negatives among the 557 | **111** | 55–168 |
| **true negative count** | **≈ 328** | 272–385 |
| `kill_graph` coverage of the negatives | **66 %** | 56 %–80 % |

The twelve: `B114` (TESTED-NEGATIVE, covering-degree mechanism unsupported) · `B142` (three
subtractive items) · `B300` (Column B = two walls) · `B308` (a precise negative) · `B417` (bar NOT
cleared) · `B449` (the forcing boundary) · `B480` (NULL — structural type-mismatch) · `B549` (the
cosmic-ratio null) · `B643` (the flip obstruction, honest negative) · `B695` (φ unreachable ⟹ the
avatar cannot carry the golden) · `B748` (V₄-SILENT) · `B790` (thesis unsupported, plan mis-scoped).

Five arcs were judged ambiguous and counted as non-negative: `B244`, `B722`, `B739`, `B760`, `B772`.

## What this means

**`kill_graph`'s 217 is not a census — it is roughly two-thirds of one.** About **111 negatives are
unregistered**, so any statement of the form "the programme has N closed doors" understates by
about half as much again.

This does **not** impugn B738. Its 217 records are 100 %-populated on their nine-field core and
B799 showed its `fact_computed` flag carries real information. B738 compiled the *atlas-visible*
negatives; the corpus simply contains more, sitting in arcs whose headline is a kill but which were
never routed into the compiler.

**Consequence for the generated views:** `docs/views/CLOSED_DOORS.md` projects 217 and must say what
share that is. `COVERAGE.md` already carries the caveat; it now carries the measured number.

## Residual

Route the ~111 unregistered negatives into the kill graph at the next compile — cheap per arc, since
each already states its own kill in its headline, and it is the same authoring pass as W1's verdicts
(`arc_verdict.json` already carries the kill sub-record for `NEGATIVE` verdicts).

`census.json` — the sample, the rule, the twelve, and the five ambiguous calls, recorded in full.
