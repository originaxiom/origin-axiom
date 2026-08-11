# THE INSTRUMENTS ARE BLIND WHERE WE ARE WORKING

**cc3, 2026-08-11.** Gate 5-Q. Measured from `scripts/forcing/forcing_graph.json`
and `docs/views/CLOSED_DOORS.md` on `origin/main`. **No new mathematics.**

## The question

Would the atlas and toolbox tell us anything about the bottlenecks? **Yes — and
what they say is that they cannot see the part of the programme we are auditing.**

## 1. The forcing graph cannot see the derivation theorem

`scripts/forcing/build.py` states its own purpose: *"it is enough to make **GAPS
VISIBLE**, which is the property the owner asked for: a branch that is not in the
graph shows up as a hole rather than being quietly forgotten."*

Its `gaps` field reports `faces_with_no_proved_arc = ["axioms", "cascade",
"character-variety"]`. **True — and not for the reason it reads as.**

| face | arcs attached |
|---|---|
| being | **332** |
| hearing | **260** |
| mtc-overlay | 124 |
| sln-tower | 106 |
| congruence-tower | 84 |
| meeting | 77 |
| children | 74 |
| coupled-double | 63 |
| emittance-eigenvalues | 13 |
| emittance-lengths | 11 |
| infinite-hecke | 6 |
| **axioms** | **1** |
| **cascade** | **1** |
| **character-variety** | **1** |

**The `cascade` face holds exactly one arc — B971.** Every arc that actually
performs the cascade — **B861, B862, B863, B864, B892, B978** — is in
`arcs_on_no_face`: **attached to nothing.**

> **The instrument built to make gaps visible has the entire derivation theorem
> invisible to it.** Not unproven — *unattached*. It reports "the cascade has no
> proved arc" and the true statement is "no cascade arc was ever attached."

## 2. Nearly a third of the corpus is outside the anatomy

**282 of 972 arcs — 29 % — are attached to no face at all.**

## 3. The graph is era-bound, like the documents B1010 caught

Highest arc it knows: **B989**. It **does not know B1000+** — so it predates the
whole B1009–B1026 window, **including B1014, which wrote THE_CLAIM itself.**

That is precisely B1010's finding (*"LAW_MAP and THE_FRAMEWORK each describe only
their own era"*) recurring in a *generated* artifact, where regeneration was
supposed to prevent it.

## 4. And `CLOSED_DOORS` flags its own version

> *"**749 recorded closures** — of which **582 are CLASSIFIED** by mechanism and
> **167 are merely ROUTED**, carrying an authored NEGATIVE verdict **but no read
> of the arc yet**."*

**22 % of the closed doors are closed by assertion and unexamined.**

## The bottleneck, named

**Every hand-finding of the last two days is the same shape as this measurement:**

| found by hand | the same thing, measured |
|---|---|
| the input list is enumerated **four different ways** | `axioms` face: **1 arc** |
| **75 %** of self-fencing arcs drop the fence in the claim line | — |
| the nine conclusions are **provenance-blind** about E₆ | `cascade` face: **1 arc** |
| three of five declared inputs are **inert** | — |
| B787's headline contradicts its own body, **unnoticed since July** | 282 arcs on **no face** |

> **The object-facing layer is heavily instrumented — 332 arcs on `being`, 260 on
> `hearing`. The physics-facing layer is not instrumented at all: three faces,
> one arc each.** The derivation theorem is where the programme's claims about
> the world live, and it is the least-measured part of the corpus.

**That is the bottleneck.** Not a missing computation — a missing *attachment
layer* on the side that faces physics.

## Cheapest repairs, in order

1. **Regenerate the forcing graph** — it is generated and 37 arcs stale. Free.
2. **Attach the cascade arcs to the cascade face.** B861/B862/B863/B864/B892/B978
   exist and are PROVED; nothing is missing but the edges. **This alone converts
   `faces_with_no_proved_arc` from a false alarm into a true reading.**
3. **Triage the 167 ROUTED closures** — or at minimum stop counting them
   alongside the 582 classified ones.

## Scope

Measured, not inferred; every number is read from the committed JSON and the
generated view. **What is not established** is *why* the cascade arcs were never
attached — whether the lexicon misses them, whether the attachment predates them,
or whether nobody ran it after the SM-structure window. **That is one question for
cc and it is cheap.**
