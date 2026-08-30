# MEMO 155 — THE LAG CLOSED, THE DIGEST, AND A DEFECT IN MY OWN INSTRUMENT

**Banked 2026-08-30.** The owner: *"yes pleaee close the gap and digest verify."*
Merge commit `7dc1bb4b`; lane now **0 commits behind main** (`55dd173c`).

---

## 0. THE HEADLINE

**Memo 148's six defects are all repaired in the current draft — and my certificate said they
weren't.** Re-running it against the new paper reported four of six still firing. **Every one of
those four was a false positive**, caught only by reading. That is **bench error #16**, it is in an
instrument I banked and vendored, and §3 is its repair.

**Memo 149's drift is not repaired**, and neither is the zero-citation finding.

---

## 1. THE MERGE

99 commits, **zero conflicts** — this branch has never touched a file outside `outside_bench/`,
verified as a dry run before committing. A **merge, never a rebase**: the lane is append-only and no
history was rewritten.

**Verified after:** `check_path_references` — **2673 citations, all resolve**. `retraction_sweep` —
2766 files, **0 live-claim violations**. Three lane certificates re-run clean. And
`scripts/checks/already_banked.py` **now exists on this branch**, so memo 153's instruction to a
reader is live here rather than only at the pin — which was the whole point of closing the lag.

**The pinned-citation form from memo 154 is kept, not reverted.** Naming the exact commit a memo
*actually read* is stronger than naming a path whose content moves. That is what `_oa_source.py`
already does.

---

## 2. THE DIGEST — WHAT ARRIVED, AND WHAT IT DID TO MY FINDINGS

Five commits post-date my audit pin, **three of them repairs to the paper**: *"eleven repairs from
two adversarial passes — three of them could have been fatal"*, *"twelve more repairs from a fifth
adversarial pass — two of them undoing this morning's own fixes"*, and *"THE STALE-LEDGER REPAIR"*.

**Re-audited by reading the current draft, then by the repaired certificate:**

| memo 148 finding | current draft | verdict |
|---|---|---|
| **H1** the `Y_q = 0` branch dropped | *"`Y_q = 1` is not a loss of generality: the branch `Y_q = 0` collapses the content to a vector-like…"* | **FIXED** — my exact one-clause repair |
| **H2** two different "exactly two" | *"exactly **two contents** survive … the SM 15-plet and **a genuinely conjugate content**"* | **FIXED** — says *contents*, and names the conjugate content correctly |
| **H3** the undefined colliding word | *"write `Λ(m) := m²+4`. This is the **level** … **not its field conductor**: `tr(RᵐLᵐ) = m²+2`, so the discriminant is `m²(m²+4)` and `Λ(m) = D/m²`. **The distinction is not cosmetic.** Under the field-conductor reading the statement would be false"* | **FIXED**, and thoroughly |
| **H4** abstract undercounts the ledger | abstract now reads *"and **three** discrete label rows"* | **FIXED** |
| **H5** falsifiers with dangling referents | all referents now introduced in the body | **FIXED** |
| **H6** census unreproducible | *"Fix the alphabet: **six** Standard-Model-visible field types, from which a content is a selection of **five with repetition** — `C(10,5) = 252`. Impose, in order, the **pure colour condition `[SU(3)]³`**, the **Witten global anomaly**, and the mixed and gravitational conditions"* | **FIXED** — every element: six letters, the word length, the explicit binomial, and both unstated conditions |

**On H3, an honest note about the repair being better-chosen than my finding.** I gave the
counterexample family `m = 11, 14, 39` (order-conductor of `x²−mx−1` equal to 5). The draft gives
`m = 4, 11, 29` (the ones whose field is `ℚ(√5)`). **Both are correct, for different wrong
readings** — mine for the order-conductor, theirs for the field — and theirs is the more natural
misreading to guard against. Verified: `m²+4 = 5k²` holds at 4, 11, 29 and not at 14 or 39; the
order-conductor is 5 at 11, 14, 39. The families overlap only at `m = 11`.

**NOT repaired, and both still stand:**
- **memo 149's drift** — 4 occurrences of *"terminal, not a deficiency"* / *"will not reduce
  further"* survive five adversarial passes, while `B1093`/`B1099` have Route A's obstructions
  proved absent and its coarse half closed positive. **This is the finding those passes did not
  find, and it is a claim-level drift rather than a wording defect** — which is consistent: the
  passes were adversarial *readings of the text*, and this one requires reading the corpus.
- **zero arc citations** — unchanged.

---

## 3. BENCH ERROR #16 — MY CERTIFICATE WAS NOT A TEST

Run against the current draft, `p3_hostile_read.py` reported
**H1-DEFECT · H2-CONFLATION · H3-GAP · H4-MISMATCH** — four false positives out of six. The cause is
one mistake made three ways:

| cell | what it actually tested | why it always fired |
|---|---|---|
| **H1** | that `[Y]³` vanishes on the `Y_q = 0` branch | a **mathematical invariant** — true of every draft, and of no draft |
| **H3** | that `m = 11, 14, 39` have order-conductor 5 | likewise an invariant of the integers |
| **H4** | that the ledger table has 3 discrete rows | the abstract's "two" was **hardcoded from the audited draft** |
| **H2** | string-matched the audited draft's sentences | ditto |

**So the certificate was a snapshot analysis wearing the shape of a test.** It could confirm what I
had already read; it could not re-check a changed draft, and run on one it produced confident
nonsense. Had I trusted it, I would have told the owner six repairs had not happened.

**Repaired.** Each cell now parses the *draft* for the property at issue. **Two-sided control, the
standard `B1202` set for its own instrument:**

```
audit pin 89affd5b : H1-DEFECT | H2-CONFLATION | H3-GAP | H4-MISMATCH | H5-DANGLING | H7-CLEAN
current   55dd173c : H1-SOUND  | H2-RESOLVED   | H3-COMPLETE | H4-MATCH | H5-GROUNDED | H7-CLEAN
```

**All six fire on the draft that had them and clear on the draft that fixed them.** Both outputs are
vendored (`p3_hostile_read_out.txt`, `p3_hostile_read_CURRENT_out.txt`). The certificate also now
takes `OA_PAPER_PIN`, so it is re-runnable against any future draft — which is what it should have
been.

**This is the seventh instrument of mine to need checking against itself this session, and the
worst of them**, because the previous six produced *suspect* numbers while this one produced
*confident wrong verdicts about someone else's work*. The lesson is narrower than "check your
detectors": **an audit cell that hardcodes what it audited is a record of a reading, not an
instrument — and it must never be re-run as though it were one.**

---

## 4. WHAT THE PAPER'S OWN PASSES DID AND DID NOT CATCH

Five adversarial passes fixed all six of my textual defects — several before or independently of my
memo reaching anyone — and **did not touch the one drift that required reading the corpus rather
than the draft.** That is the sharpest thing in this digest: *adversarial reading finds what is
wrong on the page; only tracing finds what is wrong against the record.* The two are not
substitutes, and memo 149 was the second kind.

---

## 5. FENCES

- Every "FIXED" above was established **by reading the current draft**, then confirmed by the
  repaired certificate — in that order, because the certificate is what failed.
- The verification covers the six defects of memo 148 and the two open findings of memo 149. It is
  **not** a fresh hostile read of the current draft, which now differs materially and would deserve
  its own cell.
- Merge integrity is asserted on: zero conflicts, zero non-`outside_bench` files touched by this
  branch, all citations resolving, zero retraction violations, three certificates re-run clean.
