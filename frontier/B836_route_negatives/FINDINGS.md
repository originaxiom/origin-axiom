# B836 — the negative backlog is routed, with the judgement fields left honestly empty

cc banking seat, 2026-07-30. Repository-instrument scope; Gate 5 untouched. Discharges the residual
B801 named and B833 deliberately deferred until after wave 3.

## What was done

**167 arcs carrying an authored `NEGATIVE` verdict but absent from the kill graph are now in it.**
The graph goes **217 → 384 records**, and the backlog is **zero**.

The number grew from B833's measured 137 because waves 3a/3b authored 51 further negatives while it
waited — which is precisely why B833 refused to route earlier: *"routing now would compile a list
that is stale before it lands."*

## What was deliberately NOT filled in

Each routed record carries `id`, `claim_killed` (the arc's own authored claim), and its provenance.
**Every judgement field is left unset:**

| field | value | why |
|---|---|---|
| `fact_computed` | **`None`** | it asserts the kill's **discriminating computation is in the repository**. B799 showed the flag carries real information and the B525 audit exists to protect it. **Setting it mechanically would fabricate exactly the signal it is for.** |
| `kill_form` | `"unrouted-unclassified"` | a **visible bucket**, not a guess. Assigning one of the 10 real forms requires reading the arc. |
| `faces_consulted` | `[]` | empty, not invented |
| `hatch`, `revival_score` | `None` | B830 showed a wrong revival score is worse than none — it topped the ranking with a resolved question |
| `priority` | `"UNTRIAGED"` | says so |

> **A routed record makes a kill VISIBLE to the compiler and flags it for the provenance pass. It
> does not pretend the pass has happened.**

## The view was saying something false, and now says what is true

`CLOSED_DOORS.md` opened with *"384 classified closures"* the moment the routing landed — but
**167 of them are not classified at all.** Corrected in the generator:

> **384 recorded closures — of which 217 are CLASSIFIED by mechanism and 167 are merely ROUTED**,
> carrying an authored NEGATIVE verdict but no read of the arc yet.

**A count that silently changes meaning when its population changes is the same defect as B833's
unit mismatch** — and it appeared here within one commit of B833 naming it.

## Consumers checked before the write, not after

`kill_graph.json` is read by the views generator, the forcing-graph builder and five test files.
Their requirements were read first: `faces_consulted` must be iterable, `kill_form` hashable,
`fact_computed` truthy-testable. `None` for `fact_computed` reads as falsy — so routed records count
as **"fact not computed"**, which is the correct reading: *we do not know that it is.*

31 consumer tests passed on the first run; the only failure was **B833's own lock**, which guarded a
backlog that no longer exists — a tripwire firing on its own success, re-anchored to assert the
backlog **stays** cleared.

## Carried

**The provenance pass over the 167.** Each needs its arc read to assign a `kill_form` and,
critically, to determine `fact_computed` honestly. **That is judgement work per arc and cannot be
batched** — which is the whole reason this arc did not attempt it.

`tests/test_b833_negative_routing.py` (extended)
