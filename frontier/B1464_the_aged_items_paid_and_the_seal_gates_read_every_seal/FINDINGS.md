# B1464 — THE AGED ITEMS PAID, AND THE SEAL GATES READ EVERY SEAL

**Verdict: PROVED** (a process arc, Review 59's; scope: the repository's review loop and its seal, pretense and
representation gates; reach general for the record). cc (main), 2026-10-03. The first review under B1461's carry-age
rule had eleven items at their third carry or beyond; this arc pays the seven that can be paid in one sitting and
names the reasons for declining the other four. The headline is what paying R55-13/14/15 uncovered.

## 0. Seen first

- **Repo, by sweep and by the review tools.** Review 55's §7 and action block (the items' origin); `scripts/gates/gates.py`
  (`_seal_ledger_rows`, the two seal gates, the parser B1456 had already widened to "cells from the right"),
  `scripts/seal_ledger.py` (the generator), `scripts/checks/representation_sweep.py` and `coverage_candidates.py`,
  `docs/CHAIN_COVERAGE.json`'s `_criterion`, `docs/REPRESENTATION_TRIAGE.md`, `review_tools.PHRASES`; `topic_sweep.py
  "seal.provenance|BANKED IDENTITY|PRIOR ART|pretense|external reviewer|short-claim|in-degree"` run at the review (its
  verdict line in the review entry). **Literature:** none; the repository's own governance.

## 1. The headline: 41 of 46 seals in the provenance rule's range carried neither marker, and the gate said ok

`docs/SEAL_LEDGER.md` has two row shapes — the date first, or the arc id first with the date in a later cell. The seal
parser read the first shape only: 24 rows of 50 digests, 19 recomputed by `seal-digests` ("19 of 49", R55-15), and
`seal-provenance` checked the provenance markers on the same 19 rows' files. Reading the sealed files themselves
(`sealed_files`, 255 of them; 46 from B995 on, where the rule binds): **3 carry the markers `BANKED IDENTITY:` and
`PRIOR ART:`, 2 carry the sections "Seen first" and "Disclosed" that replaced them from B1454, and 41 carry neither** —
B995–B1104 of August, and B1410, B1434–B1451 of September, this seat's own. R55-13 had seen four. The rule was, in
practice, unenforced for two months while its gate printed ok: E66's shape, a gate iterating the wrong population.

**Repair, on the ratchet.** `_seal_ledger_rows` reads both shapes (46 of 46 digests recomputed, all matching).
`seal-provenance` iterates the files from B995 on and accepts the two markers or, from B1454, the two sections; the
41 are `SEAL_PROVENANCE_BASELINE`, named, exempt, a list that may only shrink — sealed text is not repaired. Every seal
after this fix is bound; a planted new seal without the halves fails (`test_gate_failing_paths.py`). The ledger was
regenerated (325 files listed; `DECLARATION.md` added to the generator's patterns) and `seal-ledger-current` keeps it
so. (`verification/seal_census.py` holds the counts.)

## 2. The eleven items, dispositioned

| item | disposition | what was done, or why not |
|---|---|---|
| R55-2 | **RESOLVED** | the chain-coverage criterion is machine-read: `review_tools.gather` runs `coverage_candidates.py --chain-gap` and `render` prints the top of the ranked list for the review to adjudicate; `CHAIN_COVERAGE.json` says so |
| R55-4 | **RESOLVED** | the short-claim lane: an arc two or more arcs depend on is substantial whatever its claim's length (`SHORT_CLAIM_INDEG = 2`); it surfaced one arc, B804, rowed PENDING with the surface it is owed; every other queue arc is on a surface or triaged |
| R55-6 | resolved (B1461) | the H-CUSP status column |
| R55-9 | **RESOLVED** | the two live misnomers fixed (TERMINOLOGY:324, STRATEGIC_SYNTHESIS:210 → "the audit seat"); gate `pretense-phrases` on the strong family with a negation window, ledgers and history exempt, baseline zero; "independently verified" stays, as PROVENANCE §0's internal language |
| R55-13 | **RESOLVED** | §1 |
| R55-14 | **RESOLVED** | §1; the ledger had in fact been regenerated since Review 55 — three files were missing, not 530 |
| R55-15 | **RESOLVED** | §1; the docstring is now true (46 of 46) |
| R55-1 | **DECLINED** | B1247 tried the in-degree screen and refused it with reasons, and the triage register replaced screening by judgement; the two screens named are not owed |
| R55-7 | **DECLINED as stated** | the rule "a correction is not done until every artifact carrying the claim is updated" is enforced piecemeal — `retraction-sweep` (phrases), `supersession-backlinks`, `retraction-debt`, `lead-debt` — and by the correcting-old-bankings practice; a single checklist gate would duplicate four; declined, the rule kept |
| R55-12 | **DECLINED, blocker named** | B1259 and B1260 §1 are value-channel positives from before THE_BAR; a promotion to CLAIMS now needs a card and a grade (GENESIS FK9, THE_BAR), and the owner's reframe of 2026-10-01 moved the value channel off the root; UNJUDGED until carded |
| R56-1 | **DECLINED as stated** | "harvest the debt" cannot resolve as an item; the harvest-debt gate ages rows on its own ratchet, and the day's harvests (B1453, B1457, B1462) are its payments; today's live number is in the gate's output |
| R56-3 | **DECLINED as a loop item** | CLAIMS.md's rewrite against GENESIS is Stage 6 of THE_FOUNDATION_LOCK_PLAN and a declared debt of `doc_currency`; not an action item for the review loop |

## 3. Errors in this arc

None found at landing. The error this arc records is the record's: two seal gates green over a rule honoured by 3 of 46.
