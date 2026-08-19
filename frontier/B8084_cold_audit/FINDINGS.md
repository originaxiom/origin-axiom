# B8084 — the cold audit: is there systematic negative bias? (in progress)

**Date:** 2026-08-19 · **Seat:** cc3 (audit) · **Owner-routed.** This seat had no hand in any of
the audited computations, which is the point of asking it. **Verdict so far: no negative bias found
in B1075's design or arithmetic; one finding against the framing of the request itself.**
Reproducer `audit_b1075.py`. **In progress** — B1074's parity law and B1076's gauges are not yet
audited, and B1076 is not yet pushed.

## F1 — the request's premise is more negative than the record *(design finding)*

The audit request sets its scene with *"after four sealed crossings missed."* The record does not
say that.

| crossing | verdict | |
|---|---|---|
| `B915_the_crossing` | `NEGATIVE` | |
| `B925_second_crossing` | `NEGATIVE` | |
| **`B929_third_crossing`** | **`PROVED`** | **"SEALED VERDICT HIT-SHAPE — TIER 1 PASS"**, `superseded_by: null` |

B929 recorded a **Tier-1 PASS** on a blind triple computed with **zero flavour input**, prereg
pushed before data contact, and it stands unretracted and unsuperseded. **The crossing machinery
can emit a positive, because it did.** A summary that counts a standing pass as a miss is the same
failure mode as a one-way gate — and it appeared in the document commissioning the search for one.

## F2 — B1075's exclusion arithmetic is exactly right *(recomputation)*

From cc's own pinned NuFIT 6.1 3σ boxes, recomputed here without reading their scripts:

| claim | check |
|---|---|
| *"1/2 about 5σ below \|Ue2\|'s 3σ edge"* | box `[0.531, 0.5676]` → σ = 0.00610; `1/2` is **5.08σ** below the edge ✓ |
| *"1/(2φ) near no e-row box"* | `1/(2φ) = 0.3090`; nearest edge 0.1535 away ✓ |
| *"two random values land somewhere with p ≈ 0.80"* | `1 − (1−0.55)² = 0.7975` ✓ |

## F3 — the test was winnable, and that is the answer to the owner's question *(design)*

The decisive question is not whether the outcome was negative but whether a **positive was
reachable**. It was:

- the exclusion-capable e-row boxes have total measure **0.0737** of the unit interval;
- so under the null a genuine e-row hit had probability **≈ 14%** for the two sealed values.

**Not zero and not near-certain.** A rigged-negative design would have set the success region at
measure ≈ 0; a rigged-positive one would have set it near 1. Fourteen percent is a test that could
have been lost *and could have been won*, with a win worth something.

**And the grading that looks pessimistic is the opposite.** Six landings did occur in the δ-free
μ/τ boxes — a *hit shape* — and were graded **below success** because that sector's union covers
0.55, so p(at least one landing) = **0.80**. **Refusing to count an 80%-by-chance event as a
success is required, not pessimism.** The arc reported the hit shape rather than suppressing it,
and stated the number that disqualifies it.

## What is NOT yet audited

- **B1074's parity law** `det-ratio₂₇ = (−1)^flips` over all sixteen `X^τ` structures, and the
  frame-blind `W3` block — read, not yet recomputed.
- **B1076's two gauges** `864/413` and `6912/3047` — cc's own "if you take one thing to full depth,
  take this". **B1076 is not pushed**; it is absent from every remote branch.
- The prompts given to the cells, which is where F1 says to look next.
- The kill graph's structural asymmetry: **754 entries, no symmetric positive register, 167
  `unrouted-unclassified`**.

## Context that cuts against a global negative thumb

Across 400 banked `arc_verdict.json` on main: **`PROVED` 66.2%, `NEGATIVE` 30.2%, `OPEN` 2.8%,
`RETRACTED` 0.8%.** Two-thirds positive. A corpus with a systematic negative bias does not look
like this.
