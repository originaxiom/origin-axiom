# B833 — B801's estimate becomes a measurement, and its coverage figure compares two different units

cc banking seat, 2026-07-30. Repository-instrument scope; Gate 5 untouched.

## What changed since B801 could only estimate

B801 sampled 60 arcs, found 12 negatives (p = 0.200), and **estimated 111 unregistered negatives
(95 % CI 55–168)**. It could not count them: at that time most arcs carried no verdict.

**They now do.** Waves 1–2 authored 617 verdicts, so the set is directly computable:

| | |
|---|---|
| arcs carrying a `NEGATIVE` verdict | **206** |
| of those, **absent from the kill graph** | **137** |
| B801's estimate | 111 (CI **55–168**) |

> **137 is inside B801's interval. Its sampling estimate is corroborated by a direct count** — a
> genuine check of a statistical method against the census it predicted, which is rarer than it
> should be.

## But the coverage percentage compares two different units

B801 reported *"`kill_graph` coverage of the negatives = 66 %"*. Recomputing arc-for-arc gives
**33.5 %**, and **the discrepancy is not a drift — it is a unit mismatch, and my first framing had
the same fault.** Decomposing the graph's 217 records:

| | count |
|---|---|
| plain arc ids (`B<number>`) | **172** |
| **not arc ids at all** — cells and walls (`W1-hardened-record`, `W2-typing-wall-1prime`, …) | **45** |

and of the 172 arc-id records, by the arc's *authored* verdict:

| authored verdict | records |
|---|---|
| `NEGATIVE` | 69 |
| **`PROVED`** | **56** |
| (no verdict yet) | 38 |
| `RETRACTED` | 6 |
| `OPEN` | 3 |

> **The two registers are not measuring the same thing.** `arc_verdict` records **what an arc
> established** — one headline per arc. `kill_graph` records **individual kills**, which are often
> sub-arc and which frequently live inside arcs that are *net positive*: **56 kill records sit on
> `PROVED` arcs**, and that is correct, not contradictory. An arc can prove one thing while killing
> another.

**So neither 66 % nor 33.5 % is "the coverage of negatives".** A ratio between an arc-level register
and a kill-level one has no clean meaning, and quoting either invites the reader to think one
register is two-thirds (or one-third) of the other.

**The number that survives is the actionable one: 137 arcs whose established headline is a kill and
which the kill graph has never seen.**

## Why the routing is NOT done in this arc

B801's residual calls it *"cheap per arc"*. It is cheap for the fields that copy across —
`claim_killed`, source, priority. **It is not cheap for `fact_computed`**, which B799 showed carries
real information and which the B525 audit exists to protect: it asserts that the arc's
*discriminating* computation is in the repository. **Setting it mechanically would fabricate exactly
the signal the field is for**, and B741's provenance sweep found that reading it wrongly is how
"located but the located computation is itself a citation" slips through.

**Deferred deliberately, and to the right moment:** wave 3 (B832) is authoring verdicts on 183 more
arcs as this is written, which will change the negative set. Routing now would compile a list that
is stale before it lands. **Registered as the next instrument step, to run once after wave 3, with
`fact_computed` left unset rather than guessed.**

## Carried

- Route the (then-current) unrouted negatives into the kill graph, **`fact_computed` unset**, each
  flagged for the provenance pass rather than asserted.
- `docs/views/CLOSED_DOORS.md` projects the graph's 217 and should state **what that number is** — a
  kill-level register including 45 non-arc keys — rather than implying an arc census.

`tests/test_b833_negative_routing.py`
