# B[[N]] — The moves: what "no period" removes among the grammar's words, and the status of each of the four items

*Main, 2026-11-12 (S306p). The first step of the plan's package WP-1.3: which of the grammar's remaining postulates
follow from the principle, and which are declared. Exact integer matrices, 11 checks. No measured number is read.
0 of 19.*

## 1. The answer first

- **None of the four items is derived from the principle here.** Each gets a terminal status: three are declared and
  one is a reading adopted by a ruling that the computation made.
- **"No period" does less than its row says, and how much depends on the alphabet.**
  - With the two shears alone, no word has finite order at all. The only words that are not hyperbolic are the words
    in one letter. "No period" removes none of them. What removes them is the clause that both letters occur.
  - With the inverse letters, words of finite order appear, of orders 3, 4 and 6. "No period" removes exactly those.
    A single shear still stays.
- **So the item "no period" is two clauses:** no finite order, and both letters. The second is not in the principle's
  formal statement, as B1867 found; this arc computes that it is the whole of what the item does on positive words.

## 2. One line for each item

| item | what it says | what the principle's second postulate gives | status |
|---|---|---|---|
| GM2, the unit shears | elementary updates are L and R; descriptions are words in them | nothing computed. Every hyperbolic class is plus or minus a positive word in both letters (B1867, on 168 matrices), so the alphabet loses no state | declared |
| GM3, no period | the description is not periodic, so the act is hyperbolic | the candidate, "inexhaustible description", removes finite order by the formal statement's own test and does not remove a single shear. On positive words the item is the clause that both letters occur | declared, as two clauses |
| GM5a, reversible updates | the updates are invertible matrices | nothing computed | declared |
| GM5b, inverse moves are legal | the inverse of an update is an update | adopted at version 1.48 as a reading of the cancelling, chosen by a computation (B1662) and not derived | adopted |

## 3. What was computed

| | statement | on what |
|---|---|---|
| 1 | no positive word has finite order; every entry is non-negative and the diagonal is at least 1 | all 8,190 positive words of length at most 12 |
| 2 | a positive word in one letter has trace 2 and is not the identity | 24 words |
| 3 | a positive word in both letters has trace at least 3; the trace is 3 at LR and RL alone | 8,166 words |
| 4 | with inverse letters every trace from −2 to 2 occurs; the words of trace −1, 0 and 1 have orders 3, 4 and 6 | words of length at most 6 in four letters; the least are L³R⁻¹, L²R⁻¹ and LR⁻¹ |
| 5 | a word of trace 2 or −2 other than plus or minus the identity never has finite order | 1,504 words |
| 6 | a single shear is the identity at no power up to 24; the least word of trace 1 is at its sixth power | L, R, and LR⁻¹ |

**For every length.** A product of L's and R's has non-negative entries and diagonal entries at least 1, so its trace
is at least 2 and it is never of finite order unless it is the identity, which no non-empty positive word is. If
both letters occur, rotate the word so that it ends in LR: it is U·LR with U such a product, and its trace is
2u₁₁ + u₁₂ + u₂₁ + u₂₂, at least 3.

## 4. What is not shown

- **That the principle forces any of the four.** B1867 holds the three rows of the forcing ledger that are one clause
  short; this arc settles one of them as a declaration and does not prove the clause.
- **That both letters must occur.** With two records (GM1) a word in one letter updates one record only. Whether the
  principle excludes that is an argument, not a computation.

## Seen first

`python3 scripts/checks/topic_sweep.py` for the period, finite order and the single shear: B1867 § 3 holds the
finding that the formal statement removes finite order and not a fixed direction, and its check of positivity on 168
matrices; B749's fork F2 holds that every periodic alternative is degenerate. This arc adds the exact content of the
item on positive words and with inverse letters.

**The literature:** not searched. The classification of elements of SL(2, ℤ) by trace is standard.

## Disclosed

- **This is a statement of statuses with one computation under it,** as the package's first step asks. It moves no
  grade of the foundation by an argument.

## Reproduce

```
python3 -B frontier/B[[N]]_[[slug]]/verification/the_moves_on_main.py
python3 -m pytest -q frontier/B[[N]]_[[slug]]/verification/
```
