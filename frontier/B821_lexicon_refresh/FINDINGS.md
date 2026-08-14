# B821 — the lexicon refresh FAILED its own sealed criteria, and the failure corrects B820

cc banking seat, 2026-07-30. **Prereg `590aeb5021478197`, sealed and committed at `52f8169e`
before any edit to `LEXICON`.** Repository-instrument scope; Gate 5 untouched.

## Verdict: FAILURE. Reverted, per the seal.

| sealed criterion | required | got | |
|---|---|---|---|
| matches ≥ 5 of the 7 substantial blind arcs | ≥ 5 | **5** (B770, B793, B798, B818, B819) | ✅ |
| matches ≤ 25 % of the corpus | ≤ 25 % | **46.2 %** (345/746) | ❌ |

**The vacuity ceiling fired exactly as it was written to.** A motif catching the 7 by matching half
the repository would have made the atlas *look* healthier while telling a reader less. The lexicon
is reverted to 18 motifs and the blind count is back to 21.

**My pre-stated expectation was SUCCESS. It was wrong**, and the seal is what makes that a result
rather than an embarrassment.

## Why it failed — the meta-layer is the medium, not a motif

The self-audit vocabulary is not a *topic* in this corpus. It is the **ambient register of the house
method**, present almost everywhere:

| term | arcs containing it |
|---|---|
| `prereg` | **207 / 750 = 27.6 %** |
| `audit` | 110 / 750 = 14.7 % |
| `census` | 87 / 750 = 11.6 % |
| `falsifier` | 29 / 750 = 3.9 % |
| `reproducib` | 28 / 750 = 3.7 % |

> **A motif must distinguish. "The programme examining itself" cannot, because nearly a third of all
> arcs preregister — that is the method, not their subject.**

## The bug the sealed criteria caught on the first run

The insertion anchor `"bridge_construction"` exists in **two** dictionaries — `LEXICON` *and*
`OBSTACLES` — and the edit landed in `OBSTACLES`, whose values are keyword **lists**. The obstacle
classifier does `low.count(k) for k in kws`; handed a dict, it would have iterated the **keys**
(`kind`, `conserved`, `domain`, `gloss`, `patterns`) and silently scored every arc against those
words.

**The two-outcome test caught it instantly — 0/7 matched and 0.0 % of the corpus, an impossible
result for a live motif.** A quality gate found a wiring fault before it found a quality problem.
That is an argument for two-outcome criteria on *instrument* changes, not only on claims.

## The blind count decomposes — and this CORRECTS B820

B820 concluded, from a 12.2 % vs 2.3 % blindness rate, that **"the lexicon is rotting, not merely
outgrown."** With the composition now known, **that reading is wrong.** The 21 blind arcs are:

| group | n | correct? |
|---|---|---|
| **thin stubs** (409–1988 B, vs a 4078 B median) — *"Logged observation, not a claim."* | **14** | correctly invisible — there is nothing to match |
| **pure-instrument arcs** (censuses, gate reports, verdict vocabulary, coverage frames) | **6** | correctly invisible — the atlas is an **object** lexicon, and these have no object content |
| **genuine lexicon gap** | **1** | **B537** — the Markov-type surface `x²+y²+z²−xyz=c` and SL(2,ℤ) trace triples `(tr A, tr B, tr AB)`, a real object topic no motif covers |

> **The real lexicon gap is one arc, not twenty-one.** The 5.4× recent-blindness rate reflects a
> **shift in what the programme has been doing** — more instrument work — not decay in the lexicon.

B820's *instrument* improvement stands (the gate now reports rate alongside count, which is what
made this decomposition easy to ask for). Its *diagnosis* is corrected here.

## What follows, and what does not

- **Do not refresh the lexicon on the strength of the blind count.** It is dominated by arcs that
  should be blind.
- **The one substantive addition worth making is a character-variety/Markov-surface motif** for
  B537's topic — small, specific, and testable by the same two-outcome shape. Not done here: this
  arc's seal was spent on a different hypothesis, and reusing it would be moving the goalposts.
- **The gate's metric should exclude thin stubs and pure-instrument arcs**, since it currently
  counts 20 arcs that no lexicon can or should reach. That needs its own seal; it is not smuggled
  in behind a failed one.
- The ceiling stays at 21 (B820's debt marker), now understood as **mostly not a debt**.

## The transferable point

> **A gap in a measuring instrument is not the same as a defect, and the difference is composition.**
> "21 arcs are invisible" and "the lexicon is failing" looked like the same statement for two
> commits. They were not.

`tests/test_b821_lexicon_refresh.py`
