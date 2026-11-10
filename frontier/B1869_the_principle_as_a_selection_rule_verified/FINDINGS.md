# B1869 — The founding principle read as a selection rule: the advisor seat's sealed run, re-derived on main

*Main, 2026-11-10 (S306o). The owner's eleventh confirmed ruling: "lets try that" — the founding principle, read at a
level, as the rule that selects a departure. The advisor seat ran it as a sealed, exhaustive enumeration
(`non_cancellation/` on its branch; harvest row 1638). A seat's run is not a result on main until main repeats it
(P-762). Main read the seat's pre-registration and result in full, ran none of its code, and enumerated with its own
code, on main's own definitions (B1853), in exact integers. Data-free: words and integers only. 0 of 19.*

## 1. The answer first

- **The seat's result holds, entry for entry.** All seven of its hypotheses come out on main as the seat reports,
  and so do its counts of what is allowed.
- **What the rule does.** Read as "what remains is the least departure that no counted level detects", the principle
  picks the run of 6, alone, in one corner of its open choices: when "detect" means the whole level, and only the
  golden background's own level, 5, counts.
- **Why that is not a selection yet.** At any single level N the same rule picks the single run of N + 1. So the run
  of 6 comes out because 5 goes in. The rule's content is which level counts.
- **Change any one choice and the answer changes.** Under the other sense of "detect" the run of 6 ties with (2,2,2).
  With more levels counted the least departure is a mirror pair of 17 or 18 letters. Counted by extra letters,
  fifteen departures tie. On the silver and bronze backgrounds the rule gives no single run.
- **What survives without "least".** The allowed set itself, which is what the owner's confirmed ruling asks about
  (the claim is about all allowed histories together). To 12 letters at level 5 there are 8 departures with sign +,
  9 with sign −, and 77 more that fix the line only.

## 2. The seven hypotheses, on main

A departure replaces m consecutive runs of the background by runs S, whose first and last differ from the
background's. E(S) is the departure's matrix against the background's. "Not detected at level N" has two senses: the
whole level (E is +1, or ±1, mod N) and the line (E commutes with the period mod N). Every departure with at most 20
letters is enumerated: 262 144 on golden, 589 824 on silver, 802 816 on bronze.

| | the seat's hypothesis | the seat's result | main |
|---|---|---|---|
| 1 | golden, level 5, sign +: the least by letters is (6), alone | holds; next has 11 | **the same:** (6) alone at 6; next 11 |
| 2 | the same with sign − allowed | holds; the shortest with sign − has 10 letters: (2,2,1,5), (3,4,3), (5,1,2,2) | **the same,** the same three |
| 3 | golden, level 5, the line: the least is (6), alone | fails: a tie at 6 between (2,2,2) and (6); next 7 | **the same** |
| 4 | by extra letters no reading gives one departure | holds: 15 tie with sign +, 16 with either sign; the line gives the family (2,1,…,1,2) | **the same:** 15, 16, and three of that family within 20 letters |
| 5a | at level 2, 3 or 4 alone the least is the single run of N + 1 | holds | **the same:** (3), (4), (5), each alone |
| 5b | with levels 2 to 5 together nothing has 20 letters or fewer | fails: 18 letters, (2,2,2,2,1,1,4,4) and its mirror | **the same;** with levels 4 and 5: 17 letters, a mirror pair |
| 6 | silver at level 8 and bronze at 13: the least is the single run, alone | fails: silver ties at 10 letters between (10) and (1,2,1,2,1,2,1); bronze has four of 13 letters, none the single run (16) | **the same,** the same departures |
| 7 | the controls 7 and 11 on golden also give the single run of N + 1 | holds: (8), (12) | **the same** |

**The seat's clarification on signs** also reproduces. With several levels, "either sign" can mean a sign chosen at
each level or one sign for all. With one sign for all: 18 letters for levels 2 to 5 (the mirror pair), and 15 letters
for levels 4 and 5 (four departures). With a sign at each level: 16 letters (one departure, its own mirror) and 13
letters (a mirror pair).

**The background's own level.** The period L^b R^b has trace b² + 2, so it is minus a unipotent mod N exactly when N
divides b² + 4: 5 for golden, 8 with its divisors for silver, 13 for bronze. The level is the background's, not a
choice. That only the own level counts is a choice.

## 3. What main adds

- **The line reading on the other backgrounds,** which the seat's result does not state: on silver at level 8 the
  least is (1,2,1), alone, with 4 letters; on bronze at 13 it is a tie at 6 between (1,1,2,1,1) and (1,4,1). So the
  line reading gives a single departure on silver and on no other background.
- **The pattern of mirrors.** Wherever more than one level counts, the least departures come as a departure and its
  reverse, or as one that is its own reverse. B1867's law says why: the reverse is the same bundle with the base
  turned round, so a rule that counts letters cannot tell the two apart.

## 4. What it means for the programme

- **The selection criterion stays an input.** The rule passes the choice to two others: which sense of "detect"
  (P-721: does the frame live on one line or on the whole level) and which levels count. Neither is derived.
- **For the claim about all histories together,** what matters is the allowed set, and it is now verified on main to
  20 letters under each reading. The pick at the top of a list is a thread result.
- **The seat has since recorded the owner as saying that no "least" was meant.** That sentence is relayed and not
  confirmed to main (P-768). This arc does not depend on it: it verifies arithmetic.

## Seen first

- **The repo sweep:** B1853 (the departures' premises, main's definitions, to runs of 6), B1855 (the single run is
  not least once several levels are conserved, in the metric's count), B1856 and B1862 (the two signs of the charge
  premise), P-721, P-717. The enumeration by letters to 20, the other backgrounds, and the single-level controls are
  not on main before this arc.
- **The literature:** none needed.

## Disclosed

- **Main read the seat's result before enumerating.** The code is main's own and uses exact integers where the
  seat's works modulo a product of the levels; the reading was not blind.
- **Statements of "least" and "alone" are exact for 20 letters or fewer** and say nothing beyond.
- **The rule itself is not argued for here.** It is a reading of the principle, as the seat says.

## Reproduce

```
python3 -B frontier/B1869_the_principle_as_a_selection_rule_verified/verification/nc_on_main.py 20
python3 -m pytest -q frontier/B1869_the_principle_as_a_selection_rule_verified/verification/
```
