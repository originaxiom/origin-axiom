# B1473 — THE THREE KINDS COVER A THIRD AT MOST: the web seat's taxonomy of negatives (pairing / flatness / non-uniqueness) read against every kill in the record — 154 of 460 by first readers, 84 by an adversarial second reader — and the rest is the construction failing, not the interface

**Verdict: PROVED** (a census; scope: the kill graph's 460 kills; reach general for the record; a reading, with
every quote verified verbatim and every three-kind assignment read twice). cc (main), 2026-10-04. Pays L244 (a)
(the owner's "treat it seriously", 2026-10-03): *does every NEGATIVE sort into pairing / curvature / uniqueness with
nothing left over?* **No.** The SM seat's 14 of 26 on the chirality chain (sm:B1531) is confirmed in direction and
explained in proportion. **The prize first:** none for the derivation; the reading is placed. **0 of 19.**

## 0. Seen first

- **Repo, by sweep.** `topic_sweep.py "three kinds|symmetry pairing|absence of curvature|absence of uniqueness|FACE-ONLY|taxonomy of (the )?negatives"`: VERDICT 5 of 1345 arcs on main match (NEGATIVE 1, OPEN 1, PROVED 3) — no settled census of the kill graph by kind exists on main. L244 as registered (B1466/B1467) with the three kinds and three remedies in the web seat's words;
  sm:B1531's census of the chirality chain's 26 negatives (symmetry 8, flatness 3, non-uniqueness 3, other 12 — "the
  taxonomy is incomplete"), read, its list not re-used; `frontier/B738_pathfinder_compiler/kill_graph.json` (803
  entries) and `KILL_GRAPH_SUMMARY.md`; B842 (the FACE-ONLY records). **Literature:** none; the taxonomy is the web
  seat's and is tested as a reading.

## 1. The population — and a fact about the kill graph found on the way

The kill graph has 803 entries. **343 carry no `claim_killed`** — they are B842's FACE-ONLY records (329 on PROVED
arcs, 11 OPEN, 2 RETRACTED, 1 NEGATIVE): a note of the faces an arc consulted, not a kill. The first readers found
this (every one of them reported an empty batch rather than inventing a kind), and the census population is the
**460 entries with claim text** — 413 arc kills (323 NEGATIVE, 80 kills of a sub-claim inside PROVED arcs, 7 RETRACTED,
3 OPEN) and 47 wall records W1–W47. The 343 FACE-ONLY readings are kept on disk (`readers/out_r*.json`) and excluded.
**Instrument note:** any census that treats "an entry in kill_graph.json" as "a kill" overcounts by 343; the field
`priority: FACE-ONLY` is the discriminator.

## 2. The two readings

**First reading** (eight readers, 101 entries each, the brief `readers/BRIEF.md`: one kind per entry from the text
of `claim_killed` / `kill_form` / `hatch` only, a verbatim quote of at most 20 words, confidence): 460 of 460 quotes
verified verbatim against the text (`aggregate.py`; 0 discarded).

| kind | first readers | share |
|---|---|---|
| PAIRING | 24 | 5 % |
| FLATNESS | 32 | 7 % |
| NON-UNIQUENESS | 98 | 21 % |
| **three kinds** | **154** | **33 %** |
| OTHER | 306 | 67 % — no-landing-site 77, premise-false 64, arithmetic-mismatch 36, instrument 31, value-miss 24, kind-mismatch 20, scope 19, genericity 15, unstated 9, eleven others |

**Second reading** (two adversarial readers over the 154, briefed to DEMOTE unless the text itself names the pairing,
the flatness or the non-selection): **CONFIRM 84** (PAIRING 16, FLATNESS 17, NON-UNIQUENESS 51), DEMOTE 70 — of which
19 are "fitted / numerology / short catalogue", which both briefs class under NON-UNIQUENESS (a match that does not
single out) and which the second reader demoted anyway: a disagreement with the brief, reported as its own line;
51 are genuine demotions (genericity 7, no mechanism named 6, vacuity/tautology 4, computed-zero 2, premise-false 2,
null-test-chance 2, value-miss 1, …).

| | count | share of 460 |
|---|---|---|
| adversarial core | 84 | 18 % |
| core + the fitted cases | 103 | 22 % |
| first readers | 154 | 33 % |

## 3. What it means for L244

- **The taxonomy is incomplete, as the SM seat said — and the proportion says what it is a taxonomy of.** The three
  kinds are *object-level*: the object had the quantity and it cancelled (pairing), was flat (flatness), or was not
  selected (non-uniqueness). Between a fifth and a third of the record's kills are of that shape. The rest are
  *construction-level*: a premise that was false, a construction with nowhere to land, a number or field that did
  not match, an instrument that failed, a value compared to data and missed. **No remedy of the three (a breaking
  mechanism and a choice; a bulk with curvature; a selection principle) addresses a construction-level kill**; only
  doing the construction right does — which is what the record's own corrections (E-classes, retractions) are.
- **Why the chirality chain scored 54 % and the whole record 18–33 %:** the chirality chain is the interface the web
  seat was describing; object-level negatives concentrate there. The reading is right about its subject and was
  generalised past it — the "local fact promoted to a general law" shape it named in the record, in the reading itself.
- **Nothing selects a state.** The census sorts kills; it produces no positive. **The imported expectation, stated
  separately:** none. **0 of 19.**

## 4. Limits

A reading of kill text, not of the arcs; two readers per three-kind entry, one per OTHER entry; the kill texts are
of uneven length (the wall records W1–W47 are one line each). The counts are stable to ±1 reader disagreement only
where both readers agreed (84); the band 84–154 is the honest answer, not a point.

**Provenance.** `verification/readers/` (BRIEF.md, VERIFY_BRIEF.md, batch_*.json, out_*.json, verify_*.json,
verified_*.json), `verification/aggregate.py` → `census.json`, `verification/combine.py` → `census_final.json`. Lock
`tests/test_b1473_three_kinds.py`. Cross-refs L244, B1466, B1467, sm:B1531, B738, B842.
