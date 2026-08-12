# B1046 — the arc graph does not carry what the bodies know

**Date:** 2026-08-11 · **Lane:** the consolidation refresh — the arc metadata. Gate 5 untouched;
zero anchors; nothing to `CLAIMS.md`; **no mathematics asserted or disturbed.**
**Files:** `verify.py` → `results.json` (11 checks) · lock `tests/test_b1046_arc_graph.py` ·
instrument `scripts/checks/supersession.py` · gate **`supersession`** (the **28th**) · registry
`docs/consolidation/SUPERSESSIONS.md`.

**Occasion.** Phase 9 set out to disposition the seam cluster. Reading its bodies found something
that outranks it: **three of the fourteen carry headlines their own successors refuted, and the
metadata does not say so.** Measuring that corpus-wide is this arc.

---

## 1. THE SUPERSESSION GRAPH IS ONE-WAY

| | |
|---|---|
| arcs declaring `supersedes` | **42** |
| arcs carrying `superseded_by` | **5** |
| **one-way links** | **41** |
| …whose target is still **cited on a curated surface** | **12** |

**Nothing read `superseded_by`** — no gate, no check, verified against the gate file's own text.

**The twelve include `B123`** — the arc B1037 declined to restore *because B125 refutes it* — and
**`B111`**, which B1037 dispositioned as SUBSUMED. **A reader of the metadata cannot tell those
from live arcs.**

> **This is the same defect from both sides.** B1037 caught B123 **by reading a body**; B1043
> missed B564 because **no body said so**. **The graph is the thing that should have said so.**

## 2. SELF-CORRECTING ARCS ARE UNREGISTERED — and B408 is the worst case in the corpus

**35** `FINDINGS.md` carry a `CORRECTION`/`REFUTED`/`WITHDRAWN` banner **below their own headline**;
**31 have no `docs/RETRACTIONS.md` row**, against that file's own rule — *"every future retraction
adds its row in the PR that banks the correction."*

**`B408`, verdict NEGATIVE:**

> **Headline:** *"BANKED: **THE SEAM DOES NOT CONTRACT — the one scale lever stands**"*
> **27 lines later:** *"**CORRECTION** … the seam **CONTRACTS** — persistence was an artifact …
> max over embeddings **is biased by embedding count** … the object has **NO scale lever in any
> tested channel**."*

**A scale-lever claim is the most firewall-sensitive object in the programme** — it is what
`WHAT_WOULD_COUNT` grades Tier 2 on. The `arc_verdict` is correctly NEGATIVE and the generated
ledger carries that; **only the same-PR retraction rule was skipped.** And **a body-reading pass
meets the refuted headline first** — which is precisely how this campaign reads.

## 3. THE INSTRUMENT, AND THE TWO THINGS IT REFUSES TO DO

**Triaged, not capped** (B821/B823): the gate fails only on **untriaged LOAD-BEARING** items — a
superseded arc still *cited*, or a self-correction whose *verdict is not PROVED*. **72 candidates,
21 load-bearing.** The remaining **51 are published as a measured backlog**, not hidden.

> **It does not triage all 72.** That would mean writing 72 judgements without reading 72 bodies —
> the claim-line sin this instrument exists to name.

> **It does not write the back-links.** `supersedes` conflates **REPLACES** with **EXTENDS**, and a
> mechanical rule would mark live arcs dead.

## 4. ITS FIRST REAL CATCH WAS ITS AUTHOR

The gate fired on **five superseded arcs that this refresh's own restorations put on `LAW_MAP`** —
**B141, B154, B157, B164, B95**, cited by B1039/B1040/B1044.

**All five are genuinely EXTENDS**, and I can say so because those bodies were read at restoration
time: B142 upgrades B141's *principal* case while **B141's Item 1 stays rigorous for all n ≥ 3**;
B157 refutes a closed form while B154's `µ = A⁻ᵐt` survives; B198 *removes* B157's tooling wall;
B169 corrects B164's **C4** only; B153 narrows B95's *"forced"* to an ansatz.

> ### That is the outcome that vindicates not auto-writing back-links.
> A mechanical rule would have marked all five dead — **and B141's live Item 1 with them**, the
> very result B1039 restored.

---

**Verdict: PROVED** as an audit-and-instrument. 11 checks. **28 gates green.**

**The registry disposes in three directions, not one.** **REPLACES** (B123, B111, B408, B702 — a
restoration would re-import a refuted claim) · **EXTENDS** (ten, including the five above) ·
**SELF-LABELLED** (B731, B437, B385, B812, B331, B558 — the headline already carries its own
withdrawal, so no reader is misled). *A registry that only ever says "superseded, drop it" would be
as useless as one that never fires.*

**Self-correction — a first draft of the instrument hardcoded an arc into itself.** Detecting the
B408 shape by regex needed `"SCALE LEVER" not in head` to catch a headline that *contains* a
negation (*"DOES NOT CONTRACT"*) while *asserting* a positive (*"the one scale lever stands"*).
**That is an arc-specific rule inside a general instrument.** Removed: all non-PROVED
self-corrections are surfaced and **the judgement lives in the registry**, which is the posture
everywhere else here.

**And a container rewind mid-arc, caught by a symptom rather than explained away.** The tree
reverted to `ca786ba` (B1037), silently dropping B1038–B1045 locally. **The symptom was the gate
count reading 26 when it had been 27** — `law-siblings` had vanished from `GATES`. Last time this
happened in this session I explained a similar signal away; this time I checked `git log`, found
HEAD rewound, **fetched to confirm origin was intact at `8578b0c`**, backed up this arc's
uncommitted files, restored, re-set the git identity, and **re-applied the gate to the restored
`gates.py` rather than the saved one** — which mattered, because the saved copy predated
`law-siblings` and would have deleted gate 27 while adding gate 28.
