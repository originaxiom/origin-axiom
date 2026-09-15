# MEMO 159 — THE STATE-CLAIM LINTER: THE INSTRUMENT FOR MY OWN REPEATED FAILURE

**Banked 2026-08-30.** Seal `seals/STATE_CLAIM_LINTER_PREREG.md`, pushed before the instrument was
written. Certificate `certificates/state_claim_linter.py`; output vendored.

---

## 0. WHY AN INSTRUMENT AND NOT ANOTHER RESOLUTION

Three failures this session share one shape — **a claim about the state of the record, asserted from
prose rather than checked against the artifact**: #15 (a result with no committed certificate), #16
(an audit cell hardcoding what it audited), #17 (an arc's *future tense* repeated as present state).
Each was fixed by adopting a rule. **The rule then failed twice in two consecutive memos.**

`B1202` faced exactly this and said the useful thing: *"Review 52 raised the class to a standing
audit item; **an audit item is not an instrument — this is the instrument.**"* So: the instrument.

**Exhausted first.** None of the twelve `scripts/checks/` tools covers it. `already_banked.py`
searches the corpus for a MISSING claim's *topic*; **nothing checks a memo's state assertion about a
named arc against that arc's own directory** — the crack #17 fell through, since memo 157 *named*
`B632` and asserted "queued and unrun" in the same sentence.

## 1. OUTCOMES

| cell | outcome |
|---|---|
| **L-1** control | **L1-DISCRIMINATES** — flags memo 157 as first banked; clears the corrected text |
| **L-2** sweep | **L2-FINDINGS → now clean**, over 172 lane files: **1 true positive fixed, plus 1 more from the warning class** |

## 2. THE CONTROL, AND WHAT IT COST TO PASS

The seal made two-sided discrimination binding — `B1202`'s *"an instrument that cries wolf gets
ignored, which is precisely how the four misses happened."* **It took four rounds, and every failure
was the instrument's, not the lane's:**

1. **Negative control fired** — and it was **right**. Memo 157's wrong sentence was still standing,
   unmarked, in the body, with my correction 100 lines below. **That is exactly the currency defect
   this bench charged `THE_TOE_GAP.md` and `THE_SM_VERDICT.md` with — *"a reader never reaches the
   correction"* — committed by me the day before.** Fixed by marking the passage superseded **in
   place**: addendum-only forbids rewriting history, not marking a passage as superseded.
2. **Still fired** — the sentence splitter cut the `SUPERSEDED` marker away from the claim it
   marked. **Correction is a block-level property, not a sentence-level one.**
3. **4 of 5 sweep flags were false**, all one class: **the claim's subject was the bench, not the
   arc** — *"I did not run it"*, *"this bench had never run it"*, *"not executed here"*. This
   instrument is for claims about the **record's** state; what this bench did is a different
   sentence. Guard added by rule.
4. **One residual** — and it was a **dead regex**: `\b(?:…|#1[0-9]\b|…)` can never match, because
   `#` is not a word character and space→`#` is not a word boundary. Those alternatives had been
   inert since I wrote them. **Caught by the instrument's own last flag.**

## 3. WHAT THE SWEEP FOUND

**One true positive in the flag class:** `THE_OWNER_REGISTER.md` repeated memo 157's wrong claim,
with its correction two blocks below and no marker at the claim. Marked in place.

**And one from the weaker warning class, which justifies keeping it:**
`THE_CLOSURE_ROUTES.md` carries **"D4 — the S4 quine (unbuilt)"** in two places. **`B1184`
dispositioned the S4 rung.** This is the *third* document in this lane carrying that same stale
claim — after `THE_FULL_ACCOUNTING.md` (memo 153) — **and it is a document I had never audited.**
Both rows marked.

**The honest reading of `L2-CLEAN`:** the lane is clean **because I cleaned it in this cell**. It
started with one flagged live claim and one stale warning, and the sweep is what found them. My
declared prior said *"if L2-CLEAN comes back I will suspect the detector before believing the
lane"* — and the sequence bears that out: clean only arrived after four instrument repairs and two
document repairs.

## 4. WHAT IS ADOPTED

> **Run `state_claim_linter.py` before banking any memo. A flagged state claim means: list that
> arc's directory before repeating the claim.**
>
> And the rule that generated it, now enforceable rather than remembered: **a future-tense sentence
> inside an arc is evidence about the day it was written and nothing else.**

## 5. FENCES

- **A flag is a retrieval aid, not an adjudicator** — `B1202`'s own fence, and every flag in this
  cell was **adjudicated by reading**; 4 of the first 5 were discarded.
- **Lexical.** A state claim phrased off-list still slips. **This reduces the class; it does not
  abolish it** — which is exactly what `B1202` says about its own.
- The 43 warnings are **not** adjudicated individually; the class is reported as a prompt, and one
  of them was run down here because it named a rung this lane had already got wrong once.
