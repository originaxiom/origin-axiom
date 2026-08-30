# SEAL — THE STATE-CLAIM LINTER

**Sealed 2026-08-30, pushed BEFORE the instrument is written.**

## 0. Why

Three failures this session share one shape: **a claim about the state of the record, asserted from
prose rather than checked against the artifact.**

- **#15** — a result reported with no committed certificate.
- **#16** — an audit cell that hardcoded the draft it audited, re-run as if it were a test.
- **#17** — an arc's *future-tense* sentence (*"cell 2, queued"*) repeated as present state, in the
  memo whose own finding was that a gate fails to cite the material answering it.

Each was fixed by adopting a resolution. **A resolution that has failed twice in two consecutive
memos is not working.** The corpus's own answer to exactly this, at `B1202`: *"Review 52 raised the
class to a standing audit item; **an audit item is not an instrument — this is the instrument.**"*

**Exhausted first:** none of the twelve `scripts/checks/` instruments covers this.
`already_banked.py` searches the corpus for a MISSING claim's *topic*; **nothing verifies a memo's
state assertion about a *named arc* against that arc's own directory.** That is the crack #17 fell
through — memo 157 **named** `B632` and asserted "queued and unrun" in the same sentence, so listing
one directory would have caught it.

## 1. What it does

Scan `outside_bench/**/*.md` for **state claims** — *unrun, never run, not run, queued, unbuilt,
never built, not started, never executed, uncommitted, no committed certificate, does not exist* —
and, where the same sentence names an arc `B####`, **list that arc's directory** and flag the claim
when the directory holds artifacts contradicting it (code, outputs, cell files, preregistrations).

Secondary, weaker: a state claim naming **no** arc and stating **no** searched terms violates the
rule adopted in memo 153 and is reported as a warning, not a finding.

## 2. The binding design constraint

`B1202`'s own words: *"an instrument that cries wolf gets ignored, which is precisely how the four
misses happened."* So:

**Two-sided control, and the cell fails without it:**
- **positive** — memo 157's original sentence, retrieved from git *before* its correcting addendum,
  **must be flagged**;
- **negative** — the corrected text, and this lane's true state claims, **must not be**.

**Quotation exemption, on principle rather than convenience:** a wrong claim *quoted in order to
correct it* is not a live claim — the same live-vs-quoted distinction `retraction_sweep.py` already
makes. Blockquoted lines, and lines carrying correction markers, are exempt.

## 3. Outcomes

- **L-1 CONTROL** — `L1-DISCRIMINATES` (flags the original, clears the correction) vs `L1-USELESS`
  (fires on both, or on neither). **`L1-USELESS` voids the instrument** and it will not be adopted.
- **L-2 SWEEP** — run over the lane. `L2-CLEAN` (no live unflagged state claim survives) vs
  `L2-FINDINGS` (some do; each named and adjudicated **by reading**, per the standing rule).

**Declared prior:** I expect `L1-DISCRIMINATES` and `L2-FINDINGS` — 158 markdown files written fast
over many sessions almost certainly carry more of these. If `L2-CLEAN` comes back I will suspect the
detector before believing the lane.

## 4. Fences

- A flag means **read that arc's directory before repeating the claim** — not that the claim is
  false. Retrieval aid, not adjudicator, exactly as `B1202` fences its own.
- Lexical matching: a state claim phrased in words not on the list still slips. **This reduces the
  class; it does not abolish it.**
- No measured value enters. Gate 5 untouched.
