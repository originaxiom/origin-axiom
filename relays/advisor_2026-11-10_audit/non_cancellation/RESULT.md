# RESULT — the foundation's own principle as a selection rule

**From:** the advisor seat. **To:** the owner and cc. **Kind:** `result:` — data-free, exact, exhaustive to 20
letters; `domain: named set (the golden, silver and bronze backgrounds)`.
**Sealed before the run:** `PREREGISTRATION.md` and `nc_enumerate.py` at commit `8a776f7c4`
(sha256 `767551e1…` and `24babdeb…`, `ARTIFACT_HASHES.txt`). Neither file was changed after the seal.
**Outputs:** `nc_enumerate_B20_out.txt` (the run), `nc_enumerate_B20.json`, `nc_second_check_out.txt` (an independent
code path), `nc_joint_sign_out.txt` (one clarification, section 4).

## 1. The answer

**The reading picks the run of 6, alone and by a wide margin, in exactly one corner of its open choices — and the
rule itself is empty: at any single level N it picks the single run of N + 1.**

Granted two things — "detect" means the whole level (the charge reading), and only the background's own level
counts — the least departure by letters is (6) with 6 letters, the only one, and the next has 10 or 11. Change either
of the two, or the way of counting, and the answer changes or stops being unique. On the silver and bronze
backgrounds the same rule does not give a single run at all.

So the owner's principle does single out (6), but it does so by passing the question to two others. It narrows the
choice; it does not remove it.

## 2. The seven hypotheses

| # | Hypothesis | Seat's expectation | Result |
|---|---|---|---|
| **NC-1** | golden, level 5, charge+: least by letters is (6), alone | about 75% | **HOLDS.** 6 letters, one defect; the next has 11, (2,1,1,1,1,5). |
| **NC-2** | the same with −I allowed | likely | **HOLDS.** (6) alone; the shortest with E ≡ −I has 10 letters ((2,2,1,5), (3,4,3), (5,1,2,2)). |
| **NC-3** | golden, level 5, line: least is (6), alone | about 50% | **FAILS.** A tie at 6 letters: **(2,2,2)** and (6). The next is (2,1,1,1,2) at 7. |
| **NC-4** | by extra letters no reading gives one defect | likely | **HOLDS at the own level:** 15 defects tie under charge+, 16 under charge±, and the line reading gives the family (2,1^(5j+3),2). (At some other level sets one defect is least within the bound.) |
| **NC-5** | at 2, 3, 4 alone the least is the single run N + 1; under the ladder {2,3,4,5} nothing has ≤ 20 letters | first part likely; second not known | **First part HOLDS** ((3), (4), (5), each alone under charge+). **Second part FAILS:** the ladder has defects of 18 letters, (2,2,2,2,1,1,4,4) and its mirror, against 61 for the single run. Under {4,5}: 17 letters, a mirror pair, against 21. |
| **NC-6** | silver at 8 and bronze at 13: least under charge+ is the single run, alone | about 60% | **FAILS.** Silver: a tie at 10 letters between (10) and (1,2,1,2,1,2,1). Bronze: four defects of 13 letters, none of them the single run (16 letters). |
| **NC-7** | the controls 7 and 11 on golden also give the single run N + 1 under charge+ | likely | **HOLDS.** (8) and (12), each alone. |

Four of the seat's expectations were right and two were wrong (NC-6, and NC-5's second part); NC-3 was a coin flip
that came down against.

## 3. What it means, against what was written first

1. **The vacuity check held (NC-7 with NC-5's first part).** On the golden background, under charge+, the least
   departure at any single level N — 2, 3, 4, 5, 7, 11 — is the single run of N + 1. The rule adds nothing beyond
   "L^N is the identity mod N". **The run of 6 comes out because 5 goes in.** As a selection, the whole content is
   which level counts.
2. **Which level counts has an exact partial answer.** 5 is the only modulus at which the golden period is
   −(unipotent): its characteristic polynomial is (t + 1)² mod N exactly when N divides 5. So "the background's own
   level" is defined by the background, not picked. What stays an assumption is that only the own level counts.
3. **If more levels count, the answer changes and is no longer one.** Under the ladder or {4,5} the least departure
   is a gapped defect of 17 or 18 letters, in a mirror pair. This is B1855's result — the single run is not least
   once several levels are conserved — now in the grammar's own count as well as in the metric's.
4. **What "detect" means decides between (6) and a tie.** Under the line reading (2,2,2) is as short as (6). So the
   pick depends on whether the frame lives on one line or on the whole level: register row P-721.
5. **How "least" is counted matters.** By extra letters, fifteen defects tie, because golden runs inside a departure
   cost nothing. Only the count of the departure's own letters separates them.
6. **The rule does not carry to the other backgrounds.** On silver the single run ties; on bronze it loses to four
   shorter defects. A departure there may shorten a run as well as lengthen one, which the golden background does
   not allow. Of the three backgrounds, golden is the only one where this rule gives one answer at the own level —
   noted as a post hoc observation, not as a selection of the golden background.

## 4. One clarification made after the run (disclosed)

For a set of levels the sealed script tests "E ≡ ±I at each level", the record's definition (B1853), which lets the
sign differ from level to level. The independent check tested one sign for all levels and so disagreed on two
defects; both are right under their own definition. Re-run with one sign for all (`nc_joint_sign_out.txt`): under the
ladder the least is still the 18-letter mirror pair; under {4,5} it is 15 letters (four defects) with ± and 17 with
+. No hypothesis changes. NC-1, NC-2, NC-3 and NC-7 concern a single level and are untouched.

## 5. What the reading now rests on

| Granted | Status on record | If not granted |
|---|---|---|
| a departure some level detects is undone | **the reading itself** — a reading of PF1, as P008 is; not derived | there is no rule |
| "detect" is the charge reading (the whole level) | open: P-721; B1856 argues for it conditionally, with the gap of finding E3 | a tie between (6) and (2,2,2) |
| only the background's own level counts | not on record as a ruling; 5 is forced as *the own level* (section 3, item 2) | a mirror pair of 17 or 18 letters |
| "least" counts the departure's letters | the grammar's own count; no metric | a fifteen-way tie |

Against that: under those four, (6) is picked with a margin of 6 letters to 10, by a rule that uses no geometry and
no action. That is a cleaner statement of why the run of 6 than "least volume with a single state", which is post
hoc on record. It is still conditional on four things, two of them open.

## 6. For the closed loop

The result fits the loop's Adm link as follows. "The frame's data extends over the history" (the design of back-edge
A, §2.3) is the same condition as "the departure is not detected". So NC and the loop agree on what is allowed; NC
adds an order — least by letters — to pick one. Under ruling R10 that pick is a thread result, and the claim is
about all allowed histories together. What this run contributes to that claim is the allowed set itself, to 20
letters and exactly. To 12 letters at level 5 there are 8 departures with E ≡ +I, 9 with E ≡ −I and 77 more that fix
the line only (`nc_second_check_out.txt`); the least ones under every reading, to 20 letters, are in
`nc_enumerate_B20.json`.

## 7. Not done

No geometry, no τ, no state, no comparison with any measurement. Nothing beyond 20 letters. The reading NC is not
argued for here; it is only run.
