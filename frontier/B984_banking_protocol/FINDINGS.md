# B984 — the banking protocol, and the first gate that checks SURFACES rather than arcs

**Date:** 2026-08-09 · **Seat:** cc (banking) · **Lane:** repository governance. Gate 5 untouched.
**Owner directive:** a banking protocol that guarantees every document is updated after new
findings, verified by an agent that did not write the arc, with every decadal review certifying
that **no markdown document misrepresents the current state** — claims, theorems, speculations,
philosophy, interpretations, logs and easy-read alike — so that any reader, human or agent, can
follow the complete chain from philosophy through aAbB to symmetry breaking and the gauge groups.

---

## The gap this closes

**Every gate in the repository checked *arcs*. No gate checked *surfaces*.** The consequences were
already banked and had simply never been generalised:

- **`ROADMAP_TOE.md`** described the programme's position as *"the kinematic/symmetry frame is
  forced arithmetic"* for a **month** after B862/B863/B864 made that false.
- **`THE_SM_VERDICT.md`** shipped omitting **eleven of the twelve** cascade-closure arcs and
  **contradicting two banked results** (ℤ₆ and hypercharge).

Both were found by a human noticing, not by an instrument.

## What was built

**1. `docs/BANKING_PROTOCOL.md`** — four parts.
*Part I*, the banking checklist (19 rows), including two the corpus learned the hard way: the
findings file **must be named `FINDINGS.md`** (`scripts/forcing/build.py` silently skipped **45
arcs**, B1–B5 among them), and **the verdict must be the right kind** — an arc establishing that
*another* arc's claim fails is an **auditor**, `PROVED`, never `RETRACTED` (B818).
*Part II*, **independent verification**: a banking pass is not complete until an agent **that did
not write the arc** confirms the checklist **from the repository, not the conversation** — given
the arc ID and the checklist, and deliberately **not** given the author's reasoning or the claim.
It checks **presence and currency**, never correctness; correctness is the locks' job.
*Part III*, the decadal review's **room-by-room currency reading** — claims, the chain, the
negatives, method, speculation/philosophy, logs/easy-read — each with the one question it must
answer.
*Part IV*, **the chain that must stay legible**, with its thin links named rather than hidden.

**2. `doc-currency` (gate 25 of 25).** For each registered living document, the **newest arc it
cites** against the **newest arc that exists**, failing past a per-document tolerance.

**It found real staleness on its first run:**

| document | newest citation | lag |
|---|---|---|
| **`docs/TOOLBOX.md`** | B370 | **613 arcs** |
| **`CLAIMS.md`** | B854 | **129** |
| `docs/THEOREM_LEDGER.md` | B920 | 63 |
| `docs/GUT_REQUIREMENTS_LEDGER.md` | B952 | 31 |

**`TOOLBOX.md` is the sharpest**: the pre-compute protocol adopted hours earlier says *read the
toolset before any important probe*, and the toolset document is **613 arcs out of date**.

**3. Two visible pass-throughs, neither silent** — the direct lesson of **B982**, where seven gate
exemptions rested on an audit that never named them. `frozen` is an in-file opt-out **reported on
every run**; `DECLARED_DEBT` **names what is owed and when**, **prints on every run**, and the lock
fails if the set grows. **A declared debt is not an exemption.**

## Applying the protocol to the owner's own list

P3 run against the named chain — aAbB, SL(n) towers, metallic families, figure-eight, monodromy,
cusp, seam, torus, puncture, Markov blanket, feedback, symmetry breaking, gauge groups. Eleven are
well covered. **Two are not**, and both are now ladder rungs:

- **X31 — MARKOV BLANKET: 0 arcs, in no document.** And it carries a **conflation hazard** worth
  more than the rung itself: the corpus is saturated with **Markov *triples* / the Markov cubic**,
  a **different object**. Anyone grepping "Markov" — human or agent — will read this as covered.
- **X32 — FEEDBACK MECHANISM: 2 arcs**, named by the owner as *very important*, effectively
  unbuilt. Its honest difficulty is already banked: the object is **timeless** (B716/B717) and its
  modular flow is **trivial** (B721), so "feedback" needs a carrier that is not dynamics — which
  must be *defined* before it is probed.

## Scope

**Governance, not mathematics.** It proves nothing about the object. And the currency measure is
**deliberately crude**: newest-citation lag is a proxy — a document can be current while citing
nothing recent, or stale while citing a fresh arc. It is **a prompt to read, not a proof of
staleness**, which is why the failure message says a stale surface is *owed a read* rather than
that it is wrong. The `LIVING` registry is a judgement call about which surfaces matter, and it
will need revision as the corpus grows.
