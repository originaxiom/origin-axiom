# B965 — THE LAW_MAP SCOPE AUDIT: 165 rows, 5 flagged, **all five written today**

**Date:** 2026-08-08 · **Seat:** cc (banking) · **Lane:** MATHEMATICS / AUDIT.
Gate 5 untouched. **Commissioned by the owner** after B964, to stop the class of error that
a gate cannot see.

---

## 1. The method — mechanical, not editorial

For each of LAW_MAP's **165** claim rows: load **every arc it cites**, and check whether
scope-limiting language present in the **arc's own verdict** is **absent from the row**.
Scope markers: *only for, scope, assumes, not established, conditional, up to, one-prime,
not certified, NOT claimed, post-hoc, inferred, cited-not-re-derived, screened, necessary
not sufficient, limits, does not*.

This asks one question and asks it uniformly: **does the row claim more than its own arc
does?**

## 2. The result, and it is the finding

| | |
|---|---|
| claim rows audited | **165** |
| rows flagged | **5** |
| flagged rows written **before today** | **0** |
| flagged rows written **today** | **5** |
| needing real fixes | **3** |

> **Zero of the older rows overclaim. Every flagged row was written today.**

That is the diagnosis, and it is not about competence: **it is about rate.** The corpus
built slowly is scoped correctly. The corpus built in one day is not.

## 3. Adjudication, row by row

**PASS — `NO CENTRALIZER CONSTRUCTION REACHES RANK 4`.** Carries *"SCOPE NOW UNCONDITIONAL
(B960)"* and names *"(Steinberg)"* as its citation. Correctly scoped; the heuristic fired on
a row that had already been amended.

**FIX 1 — `THE TWO SEEDS HAVE COMPLEMENTARY DEFECTS`.** Stated an **inference as a fact**:
*"the shed directions are U(1)_ψ, U(1)_χ."* B953's own verdict says this is **inferred from
the rank bookkeeping, not computed**, and says so explicitly. The row did not. **Corrected.**

**FIX 2 — `τ DOES DOUBLE DUTY`.** Presented **cited standard facts as established here**.
The three equivalences (w₀ = −τ; −1 ∈ W ⟺ self-dual; outer involutions = τ) are standard and
were *cited*, not re-derived; only τ's existence and the 63 gradings were computed.
**Corrected.**

**FIX 3 — `THE F₄ WALL IS THE GENERIC VEV`.** Used **"VEV" bare** — **the exact error class
B964 retracted one hour earlier.** Every VEV in that row is a **27** VEV; adjoint VEVs are
the measurement cascade and behave *oppositely*. **Corrected, with B964's rule cited inline
so the row now teaches the distinction it depends on.**

## 4. What this says about the failure mode

The most uncomfortable finding is FIX 3: **an error class was diagnosed, retracted, given a
rule — and then survived, unfixed, in a row written the same day.** Retracting a claim does
not retract its instances. **A retraction needs a sweep, not just a correction.**

Second: the audit's discriminating power came entirely from **comparing a row to its own
arc's verdict.** In all three fixes, the arc's verdict was *correct* and appropriately
scoped — the loss happened in the **summarisation step**. That localises the problem
precisely: **the arcs are honest; the LAW_MAP rows compress them, and compression drops
qualifiers.**

## 5. Registered

- **L139 — RETRACTION SWEEPS.** When a claim is retracted, **sweep for its instances** across
  LAW_MAP, CAMPAIGN_STATUS, README and the ledgers — do not merely correct the source. FIX 3
  is the proof this is needed.
- **L140 — THE COMPRESSION STEP IS THE LEAK.** Every fix here was a qualifier lost when an
  arc verdict was compressed into a LAW_MAP row. A candidate gate: **a row citing an arc
  whose verdict contains a scope marker must carry a scope marker of its own.** Mechanical,
  and it would have caught all three.

## 6. Honest limits

1. The scan is a **keyword heuristic**. It can miss a scope loss phrased without any of its
   markers, and it fired once on a correctly-scoped row (the PASS above). It is a **triage
   tool, not a proof of correctness.**
2. Only **LAW_MAP** was audited. CAMPAIGN_STATUS, README and the PROGRESS_LOG headlines carry
   compressed claims too and are **not** covered here.
3. "Zero older rows flagged" means zero *flagged by this heuristic* — not that the older
   corpus is clean.

---

**Verdict: AUDIT — 3 fixes applied.** 165 rows, 5 flagged, all five from today, zero from
before. The arcs are scoped honestly; the loss is in **compression**. And an error class
retracted an hour earlier was still live in a row written today — **retractions need
sweeps.** L139 and L140 registered.
