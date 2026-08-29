# SEAL — THE CLAIM TRACE: P3's WRITTEN DRAFT AGAINST ITS OWN ARCS

**Sealed 2026-08-29, committed and pushed BEFORE any retrieval or adjudication.**
Follows memo 148, which could not run this check because §§5–6 carry no arc references.
Subject: `papers/P3_THE_PAPER/main.tex` at **`89affd5b`**, against the 1122 `arc_verdict.json`
records at the same commit.

## 0. What this cell is, and what it is not

The spec lists *"the 467-row disposition feeding §§4–6 with per-claim citations"* as outstanding.
That disposition — marking each pooled arc **IN / SUP / OUT** — is explicitly *"an editorial call"*
and belongs to cc and the owner. **This cell does not make it.**

This cell runs the other direction, which is verification and therefore this bench's: **take the
claims the draft actually makes, find the arc that backs each, and decide whether the arc says what
the draft says.** B1210 measured the *spec's* coverage of the corpus. Nobody has measured the
*written draft* against the corpus at all.

## 1. The extraction rule, fixed before extracting

A **claim** is any assertion in the abstract or §§2–8 that (a) states a mathematical or historical
fact about the object, the corpus, or the literature, and (b) a referee could reasonably demand a
citation for. Excluded: statements of intent, section signposting, methodological remarks, and the
non-claims box (which asserts nothing). **The full extracted list is published in the memo**, so
the extraction is itself auditable and a later seat can dispute any row.

## 2. The cells

### D1 — is mechanical retrieval trustworthy here? **BLIND**
For each claim, retrieve candidate arcs by token overlap against `claim_one_line` over all 1122
records. Then adjudicate every candidate **by reading the arc text**. Compare.
- **D1-CLEAN** — adjudication changes fewer than 25% of the mechanical verdicts.
- **D1-NOISY** — it changes 25% or more.

**Binding, and the reason this cell is first:** B1210's own sweep found clause-scoped matching cut
its flag count from 15/24 to 5/24 — *"mostly noise"* — and this bench has produced three keyword
false positives of its own this session (`vol`/`involves`, the Q2 staleness flag, the first-pass
audit drift). **No mechanical hit may be reported as a verdict without reading the arc.** D1 exists
to measure, and publish, how bad the unread version would have been.

### D2 — do the draft's claims survive their arcs? **BLIND**
Per claim, one of:
- **BACKED** — an arc asserts the claim at the strength the draft states it;
- **DRIFT** — an arc is found, but the draft states it *stronger, wider, or otherwise differently*
  than the arc supports (the direction of the drift is recorded for each);
- **UNLOCATABLE** — no arc found. *This is not an accusation.* The corpus is 1122 arcs and my
  retrieval is imperfect; UNLOCATABLE means **this cell could not trace it**, and is reported as a
  fact about the audit as much as about the draft.
- **LITERATURE** — the draft attributes it to outside work, so no arc is expected; checked instead
  for whether the draft marks it as outside work.
- **Cell verdict: D2-CLEAN** (zero DRIFT) vs **D2-DRIFT** (one or more).

### D3 — currency **BLIND**
For every BACKED claim, check whether a later arc or a document addendum corrects it. The spec's §9
names this hazard by name (`THE_SM_VERDICT.md`'s table contradicted by its own addenda 220 lines
down), so it is the failure mode the programme already knows it has.
- **D3-CURRENT** — no BACKED claim is corrected downstream.
- **D3-STALE** — at least one is.

### D4 — the reverse direction **BLIND**
B1210 measured the **spec** against the corpus: it cited 11 of 85 arcs from its own last ten days
and 1 of 48 law-creating arcs. Re-measure against the **written draft**, which is a different
document and has never been measured.
- **D4-COVERED** — the draft's coverage of the strongest recent arcs is materially better than the
  spec's was.
- **D4-GAPS** — it is not.

## 3. What this cell may not conclude

It may not conclude a claim is false because it is UNLOCATABLE. It may not mark a row IN, SUP or
OUT. It may not rank the defects by severity. And a DRIFT finding is a statement about **the draft
against the arc**, never about whether the underlying mathematics is right — memo 148 already
established that this draft's mathematics survives while its text does not always describe it, and
this cell should be expected to find more of that same shape rather than treated as surprising if
it does.

## 4. Gate 5

No measured SM value enters any computation. This cell reads text and compares text.

## 5. Standing

Nothing is transmitted. Bench memo on `claude/outside-bench`. `golden_gate` receives nothing.
