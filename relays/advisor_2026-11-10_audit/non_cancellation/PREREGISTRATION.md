# PREREGISTRATION — the foundation's own principle as a selection rule (data-free)

**From:** the advisor seat. **Written and committed before the enumeration is run.** No measured number appears and
nothing is compared with one. The instrument is exact integer arithmetic; the search is exhaustive below a stated
bound.
**The owner's word it follows:** 2026-11-10, to the seat's remark that the founding principle, read at a level, is a
selection rule the foundation already contains: "lets try that".

## 0. Disclosure

The seat is not a blind reader: it knows that the record's attention came to level 5 and the run of 6 from the data
(P-717's disclosure). Exact enumeration cannot be bent by that knowledge, but definitions can. So every definition
below is fixed here, the alternatives a reasonable reader could have chosen are all run, and every one is reported
whether or not it gives the run of 6.

## 1. The reading under test

PF1 says existence is what remains when cancelling to nothing cannot complete. **The reading (NC):**

> A departure from the background that some level of the background can detect is undone. What remains is the least
> departure that no counted level detects.

NC is a reading of PF1, not a consequence of it (as P008's reading of PF1 is). The test cannot prove the reading. It
can show what the reading picks, and whether that depends on choices the reading leaves open. Three are open, and
all are run:

| Open choice | Options run |
|---|---|
| what "detect" means | **charge+**: E ≡ +I mod N · **charge±**: E ≡ ±I mod N · **line**: E commutes with the background's period mod N |
| which levels count | the background's own level alone · each of 2, 3, 4 alone · {4, 5} · the ladder {2, 3, 4, 5} · the controls 7 and 11 |
| what "least" counts | **letters**: the size of the departure as a word, Σrᵢ · **extra letters**: Σrᵢ − b·m |

"Least" by letters is the primary order: it is the grammar's own count and uses no metric. Extra letters is reported
beside it. No action, length or volume enters.

## 2. Definitions (fixed)

As in `nc_enumerate.py` (this folder), which follows B1853's definitions and extends them to the metallic backgrounds:
a background (L^b R^b)^k with b = 1 (golden), 2 (silver), 3 (bronze); a defect replaces m consecutive background runs
by runs S = (r₁ … r_m), every rᵢ ≥ 1, r₁ ≠ b and r_m ≠ b; E(S) = D_S · D_bg(m)⁻¹.

**The background's own level** is defined before computing as the moduli N at which the period A_b = L^b R^b is
−(unipotent): since A_b has trace b² + 2, its characteristic polynomial is (t + 1)² mod N exactly when N divides
b² + 4. That gives 5 for golden, 8 (and its divisors 4, 2) for silver, 13 for bronze.

**The bound:** every defect with at most B = 20 letters is enumerated. Statements of "least" and "unique" are exact
for letters ≤ 20 and say nothing beyond.

**The instrument's control** (run before this file was committed; no hypothesis read): on four cases with known
answers — (6) gives E ≡ +I mod 5; (3,4,3) gives −I; (2,1,1,1,2) gives E ≡ LR, which commutes; (2) gives E ≡ L, which
does not — the script returns all four correctly.

## 3. Hypotheses, each with the seat's expectation written first

| # | Hypothesis | Expectation | It fails if |
|---|---|---|---|
| **NC-1** | golden, own level 5, charge+: the least defect by letters is the single run (6), and it is the only one with that many letters | likely true (about 75%) | another defect with ≤ 6 letters has E ≡ +I mod 5 |
| **NC-2** | the same under charge±: allowing −I does not change the answer | likely true (the shortest −I defect known is (3,4,3), 10 letters) | a defect with E ≡ −I mod 5 has ≤ 6 letters |
| **NC-3** | golden, level 5, line: the least defect by letters is again (6) alone | **uncertain (about 50%)**: the line reading admits ten matrices where charge admits two | a line-invisible defect has fewer than 6 letters, or ties at 6 |
| **NC-4** | by extra letters the answer is not unique under any reading | likely true: interior runs of length b cost nothing, so families tie | the least by extra letters is a single defect |
| **NC-5** | the levels matter: at 2, 3, 4 alone the least defect is the single run N + 1, and under the ladder {2,3,4,5} no defect has ≤ 20 letters | likely true for the single levels; for the ladder the single run needs 61 letters, and whether a shorter defect exists is not known to the seat | reported as found |
| **NC-6** | **the second thread:** on silver at its own level 8 and bronze at 13 the least charge+ defect is the single run b + N (10 and 16 letters), alone | uncertain (about 60%) | another defect is as short or shorter |
| **NC-7** | the controls 7 and 11, which are not the golden background's own level, also give the single run N + 1 as least under charge+ | likely true | — |

## 4. What each outcome would mean (written first)

- **NC-1, NC-2 and NC-6 hold:** under the charge reading at the background's own level, the rule "least by letters"
  picks the single run on every background tried — a uniform rule that needs no metric. That would make the run of 6
  the pick of a rule stated in the grammar's own terms. It would not make the charge reading or "own level alone"
  forced; those stay the open choices of section 1.
- **NC-7 holds as well:** the rule picks "the single run N + 1" at any level. Then the content of the selection is
  entirely in which level counts, and the rule itself adds nothing beyond "L^N ≡ I mod N". That is the vacuity check
  on NC-1, and the seat expects it to hold: **if it does, NC selects the run of 6 only because 5 was put in.**
- **NC-3 fails:** the line reading picks something else, so the pick depends on what "detect" means, and P-721 (one
  line or the whole level) decides it.
- **NC-5's ladder gives a short defect, or none within the bound:** reported as it is; it bears on B1855.
- **NC-1 fails:** the reading does not pick the run of 6 even under the most favourable definitions, and the seat's
  remark to the owner was wrong.

## 5. What is not done here

No value of τ is read, no geometry is computed, nothing is compared with data, and no claim about the weave is made:
every result is about one background at a time and carries `domain: named set (three metallic backgrounds)`.
