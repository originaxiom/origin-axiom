# B1033 — the second debt register meets the first, and the gated one **cannot see two-thirds of the corpus**

**Date:** 2026-08-11 · **Lane:** AUDIT of an instrument, plus a correction of this refresh's own
deliverable. Gate 5 untouched; zero anchors; nothing to `CLAIMS.md`; **no mathematics asserted.**
**Files:** `verify.py` → `results.json` (24 checks) · locks appended to
`tests/test_consolidation_coverage.py` (6 new).

**Occasion:** before continuing the campaign, checking whether the repository already had a debt
register. **It does**, and reconciling the two measured something larger than the omission.

---

## 1. THE OMISSION — `DEBT_LEDGER.md` was the *second* register, and the first one is gated

`docs/REPRESENTATION_TRIAGE.md` (from **L143 / B976**), swept by
`scripts/checks/representation_sweep.py`, lists every *substantial* banked arc cited on no
synthesis surface, with dispositions **PENDING / PROCESS / SURFACE**, and the
`representation-sweep` gate **fails the build** when such an arc is untriaged: *"An untriaged
unrepresented arc is the defect."*

**`DEBT_LEDGER.md` cited it, the sweeper, and the gate zero times** across three versions.

| | `REPRESENTATION_TRIAGE` (gated) | `DEBT_LEDGER` (this refresh) |
|---|---|---|
| verdicts | PROVED ∪ NEGATIVE | PROVED |
| substantiality filter | **`claim_one_line` ≥ 500** | none |
| surfaces | **9** synthesis surfaces | **5** curated consolidations |
| asks | *"represented anywhere a reader looks?"* | *"**distilled** into a curated consolidation?"* |
| count | **10 live** (17 rows, 13 PENDING) | **234** |
| overlap | **6 arcs** | |

Both are defensible; **publishing one without the other is not.** Same shape as the defect B1030
filed against `THE_CLAIM` vs B1000 — two registers, two counts, no cross-reference — with the
unreferenced one this time being mine. **B976** — whose lead created the triage — is in the
ledger's rows and *not* in the triage, and **correctly**: it is cited on `THE_SM_VERDICT` and
`SM_SPECIFICATION_LEDGER`, sweep surfaces rather than curated ones. Both registers behaved as
designed; only the cross-reference was missing.

## 2. AND THE GATED REGISTER'S SUBSTANTIALITY BAR IS A STEP IN TIME

Median `claim_one_line` length, by band:

| band | B0–99 | B100–799 | **B800–899** | **B900–999** | **B1000+** |
|---|---|---|---|---|---|
| median chars | 145 | 156–162 | **733** | **2571** | **3084** |
| share ≥ 500 | 0 % | **0 %** | 56 % | 95 % | 100 % |

> ### **Zero of the 731 arcs banked before B800 can ever clear the bar.** The gate that exists to catch *"a row that was never written"* is structurally blind to two-thirds of the corpus.

**This is not a miscalibration.** The register was calibrated on the **eleven** lost cascade arcs
(B860–B873; B862 excluded, another seat having cited it) and it catches **11 of 11** — a
post-convention block, where `claim_one_line` is an abstract rather than a one-line summary. **The
bar is right for the job it was built for.** What is missing is a stated era scope: the rule reads
*"every **substantial** banked arc."*

**Three measurements that change what should be done about it:**

- **The margin on its own calibration block is TWO CHARACTERS.** **B862** — same block, the arc
  that **derives the global ℤ₆ form**, the programme's most-cited structural win — has a claim line
  of **498**. It sits outside the calibration set only because a different seat had cited it an
  hour earlier. Had it not, *"11 of 11"* would have been **11 of 12**, and the miss would have been
  the block's most consequential member.
- **The obvious repair fails, and was tested before being offered.** A band-relative threshold
  (≥ 2× the band median) recovers **1 of 12** of the calibration block. Trading a *known* blind
  spot for an *unknown* one is worse than naming the known one. **Registered as L158**, not
  proposed as a fix.
- **The measure the register rejected is the era-stable one.** FINDINGS.md size holds a median of
  **2.0–5.5 KB in every band**, no step. Its rejection was correct *within* the late era (B864's
  FINDINGS is 3.7 KB — short and dense, exactly the case that motivated the choice) and does not
  generalise across eras. *Both decisions were locally right; the composition of them is the gap.*

## 3. THE CONSEQUENCE — this arc reverses its own plan

The intended repair was to **stratify the ledger's rows by that bar** — 19 above, 215 below.
**Refused.** Every one of the 19 is **≥ B870**; applying the bar would silently discard the entire
pre-B800 corpus, importing the blindness just measured. **The rows stand unstratified.**

> A calibrated threshold is only as portable as the field it reads. This one was tuned on a
> fourteen-arc window and then written as a rule about *"every substantial banked arc"* — and the
> field it reads had changed meaning three hundred arcs earlier.

## 4. A SECOND, SMALLER CORRECTION — a citation to a document that does not contain the claim

B1024 and B1026 (both mine, this pass) say *"`docs/ERROR_LEDGER.md` names E1 the programme's most
recurrent error class."* **`ERROR_LEDGER.md` never uses the phrase** — it registers E1 with **3**
known instances, fewer than E4's or E12's. **The claim is real and binding**, and it lives in
**`GOVERNANCE.md` §13** (*"the program's single most recurrent error class is undeclared choice
drift"*) and **`WORKING_RULES.md`**.

**A misattribution, not a false claim** — stated at that size deliberately, because the first read
of the evidence looked like a false claim and the spread-check is what corrected it. All three loci
are repointed in place with the correction inline. Recorded as a retraction row because a citation
to a document that does not contain the statement is exactly the corpus's **E11 (overextended
record)**.

## 5. A NOTE ON THE COUNT, WHICH MOVED THREE TIMES: 245 → 251 → 234

The measurement is **moving by construction** — every consolidation row added retires a debt row,
and this pass added eleven arcs' worth. **234** is measured against the tree at B1032. *The lock
bounds the share rather than pinning the integer*, precisely so ordinary consolidation work does
not break it.

**And one of those movements was not consolidation.** The 251 was computed against a working tree
that had been rewound to an earlier commit; the restored tree gives 234. **The structural findings
were unaffected** — 0 of 731, the step function, the lowest above-bar row at B870 — which is what a
structural finding should do under a change of substrate, but the *counts* were wrong and were
recomputed before publication rather than after.

---

**Verdict: PROVED** as an audit. 24 mechanical checks over banked artifacts, the gate's own sweeper
module (imported, not reimplemented), and curated surfaces.

**Self-correction — one hazard, now at SIX instances across five arcs, and this time it moved a
published number.** An arc that both **measures** a gap and **fills** it invalidates its own metric
unless scoped by **authorship**. Three separate bites in this arc alone:

1. the register's new scope-limit note is what puts era language into the register, so the check
   for its absence had to exclude this arc's own block;
2. **this arc's `LAW_MAP` row cites B976** — the very arc whose absence from curated surfaces is
   part of the finding — silently retiring it from the set being counted;
3. **the arc counts itself.** Scoping the *rows* was not enough; B1033's own `arc_verdict.json`
   made it a PROVED, uncited member of its own debt set. Both the rows **and** the arc's own
   B-number are now excluded, and the published figure is stated as *"the corpus at B1032"*.

Bite (2) moved the headline from 234 to 232 before it was caught. **`THE_LADDER`'s X31 row named
the shape first** — *"Registering a gap creates hits for the gap, so the coverage count
self-inflates"* — and the lesson has now cost enough re-runs to be worth stating as a rule: **a
measurement published by the same commit that changes what it measures must name its own exclusion
set, in the artifact, next to the number.**
