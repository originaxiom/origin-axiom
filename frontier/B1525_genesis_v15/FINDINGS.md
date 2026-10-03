# B1525 — GENESIS v1.5: MAIN'S v1.4 AS THE HEAD, THE SM SEAT'S v1.3 ANSWERED BY ITS LINE, AND THE LEVELS, THE WORD STATES, THE BAR'S NULL CONTRACT AND THE AUDIT LANE'S GAP3 CARRIED

**Date:** 2026-10-03. **Verdict: PROVED.** Six checks, C1–C6 (`verification/genesis_v15_checks.py`, 15 s), all pass.
- All six were run and passed before GENESIS.md was written. The pre-write log is kept (`genesis_v15_checks_prewrite_run.txt`).
- The run after writing (`genesis_v15_checks_run.txt`, `genesis_v15_checks.json`) adds one fact: GENESIS.md is the generator's
  output, byte for byte.

**Not sealed.** Each check reads a banked record or re-derives a number the record already fixes. No open outcome is
computed. **creates_law is false.** 0 of 19 Standard-Model parameters; I-26 stays UNEARNED.

**Source.**
- **Main's ask.** Its relay of 2026-10-02 (`CC_TO_SM_2026-10-02_GENESIS_V1_3_AND_YOUR_FOUR_ARCS.md`, in `docs/handoffs/` on main, §5): *"Take
  v1.3 as the head, or answer a change by its line."* Main has since made v1.4 (B1458), so v1.4 is the head taken.
- **This seat's word.** Its relay of 2026-10-03 (THE FLEXIBLE STATES, §3): take main's v1.4 as the head, answer it line by line,
  and carry sm:B1521's changes as the next version.
- **The audit lane's request.** Its relay at `24c039c8`: refine GENESIS GAP3, whose "a one-ended state can get the third only
  from a relation" its results do not prove.
- **The owner's instruction of 2026-10-02** (quoted verbatim in sm:B1521): nothing load-bearing ignored, the experiential
  question included; all allowed states, not only m004; "choice might be golden".

## Seen first (the repo sweep and the literature)

**The repo sweep**, made before any GENESIS text was written.
- `git fetch --all` at the start. The heads are in `arc_verdict.json`:
  - main `77714caf` (B1459 run), unchanged since sm:B1523's bank;
  - the audit lane `24c039c8`, the seat lanes `7cda35aa`, `0043be2b`, `5d58b935` and `13d2c5b6`, and sep16 `3205984b`;
  - `art/camper-van-bar` `b3745696`, which adds an illustration (`art/camper-bar.png`, `.svg`) on main's `70ca9c92` and
    nothing else.
  - None was merged.
- The two texts, kept as received in `received/` and checked against their git blobs:
  - main's GENESIS.md at `77714caf` is v1.4 (blob `fb43bc77`, sha-256 `d32456b6…`);
  - this branch's GENESIS.md before this arc is the SM seat's v1.3 (blob `8b2b57f6`, sha-256 `d675c0fd…`).
- `scripts/checks/prior_work.py` ran on ten terms: "GENESIS v1.5", "Version 1.5", "only from a relation", "admitted source",
  "null contract", "golden Galois reflection", "one-bit rule", "mirror-broken", "Gate 5-Q", "governed rooms". No head has a
  v1.5. The hits read are in `arc_verdict.json`:
  - "only from a relation" entered GENESIS in main's v1.3 (B1456, `adoption/amend.py`). Main sent it to the audit lane on
    2026-10-02 with *"If that sentence misstates your record, it is the one to correct"*
    (`CC_TO_CODEX_2026-10-02_YOUR_LANE_HARVESTED_R32_TO_R80.md`, in `docs/handoffs/` on main).
  - The audit lane answered in `BRANCH_SYNC_2026_10_03.md` ("Two claims that are not yet adopted") and in its relay, kept here
    as received.
- Also read for this arc:
  - main's relay `CC_TO_SM_2026-10-03_THE_BAR_ADOPTED.md`, and main's v1.3 and v1.4 log entries;
  - the SM seat's v1.3, line by line against main's v1.4 (§2);
  - the records of sm:B1521 to sm:B1524;
  - main's B1459, read at sm:B1523's bank and run after v1.4;
  - Gate 5-Q (`philosophy/GATE5Q_PHENOMENOLOGY_FIREWALL.md`, Q1 and Q5);
  - main's ERROR_LEDGER class E84.

**What this arc must not present as new.** Nothing in GENESIS v1.5 is new. Every carried or added sentence cites its arc,
and C1–C5 check each one against that arc's own record or a re-derivation. C2's third route is new code, but it recounts
B1522's numbers.

**The literature.** No source is newly cited. v1.5's added sentences rest on sources read for sm:B1522 to sm:B1524:
- Ballas, arXiv:1403.3314v3, p. 17;
- Ballas–Danciger–Lee, Thm. 3.2;
- Ballas, arXiv:1805.09274, Thm. 0.2;
- Heusener–Porti, arXiv:0908.2863, Lemma 8.2;
- Šidák, JASA 62 (1967);
- Phipson–Smyth (2010).

C2 uses only the definitions of the objects it counts.

## 1. The checks

| | what is checked | how | result |
|---|---|---|---|
| C1 | the items carried from the SM seat's v1.3 (GENESIS FK9's P, FK12's B130 scope, §7's AR6 sentence, §9's rows) | sm:B1521's `which_class_is_P.py` and `audit_corrections.py` re-run, each loaded from its own file and writing to a temporary directory | both outputs byte-identical to their records; P is the swap's class, ρ_q ∘ P ≅ ρ_q and not ρ_q* (q = 2, 3, 1/5, 7/3); AR3–AR6 as recorded |
| C2 | the levels (sm:B1522) | a third route, below | all 26 counts equal the records |
| C3 | the word states (sm:B1523) | own word code against the record | every number GENESIS v1.5 cites |
| C4 | the bar's null contract (sm:B1524) | its record; `docs/THE_BAR.md` | 7 of 7 checks; PASSED, Bonferroni and the contract on the page |
| C5 | GENESIS GAP3 against the audit lane's words | the relay as received (blob `a5b4ecaf`, identical to `24c039c8`'s) | its five sentences found; v1.5 says them and no longer asserts the old one |
| C6 | v1.5 against main's v1.4 | regenerated; token and line diffs; tables | only the eleven listed edits to main's words; every changed block marked; no status changed |

**C2, the levels by a third route.** The route shares no code with B1522's two routes or its post-run checks.
- The characters of T_n = coker(Φⁿ − 1), with Φ = LR, are enumerated as integer row vectors w mod D = |T_n| with
  w(Φⁿ − 1) ≡ 0. A box of index D is mapped through the adjugate, and the image is checked to have exactly D elements.
- The count-odd maps of M_n are the lifts with determinant −1 on the fibre, those that invert the fibre boundary:
  - the reflections ±Φᵏ S, with S = [[1, 1], [0, −1]] and S Φ S = Φ⁻¹ (the base reversed);
  - the rotations ±G^(2k+1), with G = [[0, 1], [1, 1]] and G² = Φ (the base kept);
  - k < n in both.
- Off the unit circle the meridian value forces the base reversed. So a vacuum is fixed exactly when a reflection h sends its
  twist to its inverse, w h ≡ −w.
- On the circle a rotation with the twist conjugated also fixes it, w h ≡ w. The sign ±h turns this into w h ≡ −w.
- The route counts from the definitions, so it checks B1522's counting, not Lemma C's derivation. B1522's X2 checked the
  criterion itself without it, on M₁ to M₆.

| n | \|T_n\| = L₂ₙ − 2 | unfixed off the circle | unfixed on it | B1522's record |
|---|---|---|---|---|
| 1–4 | 1, 5, 16, 45 | 0 | 0 | equal |
| 5 | 121 | 20 | 0 | equal |
| 6 | 320 | 96 | 96 | equal |
| 7 | 841 | 448 | 392 | equal |
| 8 | 2 205 | 1 344 | 1 344 | equal |
| 9 | 5 776 | 4 464 | 4 320 | equal |
| 10 | 15 125 | 12 100 | 12 080 | equal |
| 11 | 39 601 | 35 244 | 34 848 | equal |
| 12 | 103 680 | 93 936 | 93 936 | equal |
| 13 | 271 441 | 257 920 | 256 880 | equal (X5, `lemma_f_beyond.json`) |

- Lemma F's closed forms (p − 1)(p + 1 − 2n) and (p − 1)(p − 1 − 2n) hold at n = 5, 7, 11 and 13 (p = 11, 29, 199 and 521).
- The mirror breaks first on M₅ off the circle and on M₆ on it. The share off the circle runs 0.17, 0.30, 0.53, 0.61, 0.77,
  0.80, 0.89 and 0.91 on M₅ to M₁₂.
- From the records: all 196 firing members fixed (P8, and directly X3); the sealed golden form holds; X1–X4 pass; nine of nine
  held, outcome B.

**C3, the word states by own word code.**
- **States and manifolds.** 758 states and 536 manifolds.
- **Kinds.** Each manifold's kinds (rev, swap, swaprev), read from its word, agree with the record on all 536.
- **Main's one-bit rule.** On every isometry the record lists, ε = −1 exactly when the fibre boundary is inverted.
- **The mirror-broken manifolds** are exactly those whose word has neither rev nor swap:
  - 262 manifolds, 131 per sign, carrying 482 states;
  - by kind, 220 with no symmetry of the word (chiral) and 42 swaprev-only;
  - by length 6 to 12: 2, 2, 8, 14, 36, 62 and 138;
  - the first are ±LLRLRR, and the first chiral ones ±L³RLR².
- **A dualising isometry** exists on 274 manifolds. All 536 are rigid, with the fibre boundary a rigid slope.
- **Golden.** The squarefree part of t² − 4 is 5 on 14 manifolds. Exactly ±L⁴RL³R² (t = 47) and ±L⁴RLR³LR² (t = 123) of
  them are mirror-broken.

**C6, v1.5 against main's v1.4.**
- **Main's words.** All are kept except eleven edits, all but three of them punctuation where a marked sentence is appended.
  The three:
  - the version number;
  - the word "A", dropped from the GENESIS GAP3 sentence the audit lane asked to refine;
  - "frame", made "frame's counts" in §8's frontier item.
- **Marks.** Every changed block of lines carries a [v1.5] mark, except the version line and §10's own entry (log entries carry
  no mark). The earlier marks are unchanged (15, 22, 6 and 5 bold marks of v1.1 to v1.4), and v1.5 adds 16.
- **Form and status.** Sections 0–10 are in order and every table is well formed. Every table row of v1.4 is kept verbatim but
  four (§5's m004 and word-state rows, FK9 and FK12), whose leading cells are kept. Four rows are new (§9). The fork statuses
  are unchanged.
- **Vocabulary.** None of Q5's three words, no vendor word and no private term occurs in v1.5. The test can fire: on the
  received v1.3 it finds Q5's third word (§4).

## 2. The SM seat's v1.3 (sm:B1521), answered by its line

Each of v1.3's twelve [v1.3] marks, its header and its log entry, against main's v1.4, as GENESIS v1.5 answers them:

| v1.3 (sm:B1521) | in GENESIS v1.5 |
|---|---|
| Header: v1.3's sentence and the received path | replaced by v1.5's header sentence; v1.3 kept as received in this arc |
| §7: B723 cited with its two retractions, B942 and B957, with their reasons | in main's v1.3, in main's words (B942, B957, and B849). v1.3's closing sentence, what survives (AR6), carried, marked |
| FK9: the run of main's B1455 and sm:B1520 (NEGATIVE, frame F-HE, reach single) | in main's v1.3, at FK9 and in §5 |
| FK9: "the three lemmas are B1297's" | in main's v1.4 as "dualising does (main B1297, B868, B871)"; and §9's carried row "the three lines L1–L3" credits B1297 |
| FK9: P is the swap's class and fixes ρ_q; B1297's tower theorem and the family's rest on different symmetries | carried, marked (C1) |
| FK9: "the levels stay open (main's L242 (b))" | superseded: the levels were run (sm:B1522), carried at FK9 and in §5 |
| FK9: "choice might be golden", registered, untested | carried, and its two sealed tests added (sm:B1522, sm:B1523) |
| FK9: v1.3 had dropped "not yet run" from v1.2's sentence on B1455 | main's v1.4 keeps "(sealed 2026-10-02, not yet run)" there, followed by its own [v1.3] "Run (…)"; left in main's words, and noted for main |
| FK12: "never reads" in B37's literal sense only (AR3) | in main's v1.3: "The qualification, the audit lane's: …" |
| FK12: B130's fork-free reading scoped (AR4) | carried, marked (C1) |
| FK12: on m004's family a symmetric law lands in states it does not fix, for half the symmetries, never a count-odd one | in main's v1.3, at FK9: "The family's vacua do break half the symmetries, a mirror among them, with no count attached" |
| FK12: the owner's act-and-register priority, its three questions kept apart, the experiential one under Gate 5-Q | carried, marked; the first question points to main's (iii) |
| FK12: the measurer's referent, a quotation of main's B1455 §5 | **not carried.** Main's (i) and (ii), with L241, carry its content, and the quotation brought Q5's third word outside the governed rooms (§4) |
| §8 frontier: the deciding test on any level of m004 or on any other state | superseded: the levels run (sm:B1522), the family exists on every word state (sm:B1523); replaced by the class index on a mirror-broken family (sL-10 item 8), marked |
| §8 frontier: the fixed loci component by component (AR4) | carried, marked |
| §9: four rows (B37's never-reads, B130's no forced choice, B723's built observer, the three lines L1–L3) | carried, marked; "AR3" written "the audit lane's AR3" |
| §10: v1.3's entry | superseded by v1.5's entry, which says what was carried, what was not and why |

## 3. What GENESIS v1.5 adds since

- **§5 and FK9, the levels (sm:B1522; C2).** On M₁…M₁₂ the count-odd mirror breaks from M₅ on: off the unit circle exactly
  where no golden Galois reflection fixes the twist, on it from M₆ on, up to 0.91 of M₁₂'s 103 680 vacua. Every one of the 196
  firing members of levels 1–6 is fixed, so the mirror breaks only where nothing chiral has been found.
- **§5 and FK9, the word states (sm:B1523; C3).**
  - Every word state to length 12 carries a one-parameter projective family at its hyperbolic point.
  - Main's one-bit rule holds on all of them.
  - On 262 manifolds (482 states) no isometry dualises the family. So near the hyperbolic point B1455's symmetry argument
    cannot force the count to zero there (Lemma T, a local statement).
  - Whether it is nonzero is sL-10 item 8, sealed first.
- **FK9, the owner's "choice might be golden",** in its two sealed forms. On the levels, off the unit circle, a golden Galois
  reflection decides where the mirror breaks. On the word states, the two golden mirror-broken manifolds are selected by their
  words, not their field.
- **FK9 and GAP4, the bar's null contract (sm:B1524; C4).** The top grade is PASSED, a rarity screen: necessary for
  WHAT_WOULD_COUNT's DERIVED, never sufficient for it, never a physical admission. GENESIS GAP4's list of grades marks the
  rename.
- **GAP3, the audit lane's refinement (C5).**
  - Its results do not prove that a one-ended state can get the third only from a relation.
  - They prove that a specified flat counted configuration needs an admitted source or end flux, or a change of hypotheses.
  - Whether a generated relation supplies it stays open (GENESIS FK8, FK12), and R77's added fields do not settle their
    genesis origin.
  - The refinement keeps the owner's act-and-register priority without installing its solution.
- **§8's frontier.** The class index on the projective family of a mirror-broken word state, first ±LLRLRR and ±L³RLR².
- **Not added: main's B1459.** It makes the zeros at B1451's 188 complete points a theorem, and was run at `77714caf` after v1.4.
  This seat read it but did not re-derive it, so it is left to main's next version, in main's words.
- **No status changes.** FK1 and FK12 stay the owner's to frame.

## 4. Two slips of this seat, self-caught

### 4.1 Q5's third word at GENESIS FK12, in v1.3 (main's E84 class)

**What happened.** The SM seat's v1.3 (sm:B1521) quoted main's B1455 §5 at FK12. The quotation contains the third of the three
words that Gate 5-Q's Q5 keeps in the governed rooms (`philosophy/`, `speculations/`). B1521's lock carried a comment naming Q5,
but its check tested Q5's first word, one other word and the private term, not Q5's second and third words. So the quotation
passed it.
- This is main's E84 class, the CITED-ABSENT CHECK: a check named as enforcing a rule cannot fire on part of it.
- Self-caught on 2026-10-03, reading v1.3 against v1.4 line by line for this arc.

**The repair.**
- v1.5 does not carry the quotation (§2). Main's (i) and (ii) already say what it said.
- This arc's lock tests all three of Q5's words, as whole words, in GENESIS.md and in this arc's text. The words are encoded,
  not written.
- As E84's rule asks, the test ships with a control in each direction: it finds Q5's third word in the received v1.3, and none
  in v1.4 or v1.5.
- Logged in `docs/ERROR_LEDGER.md`.

### 4.2 B1522's criterion without its qualifier (E53 class)

**What happened.** B1522 states its criterion in §0 and §5 with its domain: off the unit circle, a vacuum breaks the count-odd
mirror exactly when no golden Galois reflection fixes its twist. Its title, and several surfaces that repeated it, dropped "off
the unit circle". On the circle the statement is false: the golden rotations also act, and M₅'s 20 twists that no reflection
fixes are all fixed when λ is unitary (C2's on-circle count is 0 there).
- Unqualified: B1522's title, `docs/OPEN_LEADS.md` sL-10 item 2, `docs/SM_SEAT_ALIAS_TABLE.md`, the RELAY_LEDGER row of
  `SM_TO_CC_2026-10-02_L242B_THE_LEVELS_RUN.md` and that relay's own title, the CHANGELOG heading, and
  `docs/THEOREM_REGISTRY.md`'s bold headline for T-GOLDEN-CHOICE (its statement (C) is exact).
- Ambiguous, the criterion placed after "from M₆ on it": `docs/CAMPAIGN_STATUS.md`, the kill graph's B1520 note, and the
  SEAL_LEDGER's B1522 row.
- The first draft of this arc's own §5 sentence for GENESIS repeated it. It was caught on reading B1522's §0 against the draft,
  before any GENESIS text was written.

**The repair.** The living surfaces carry a dated qualifier: B1522's FINDINGS (a note under its title), OPEN_LEADS, the alias
table, CAMPAIGN_STATUS, the RELAY_LEDGER row, the kill graph's note and the registry headline. The CHANGELOG, the SEAL_LEDGER
and the sent relay stay as written; the relay to main carries the precision. GENESIS v1.5 states the qualifier at §5 and FK9.
Logged in `docs/ERROR_LEDGER.md` as an E53 instance (a headline that says more than its arc's body).

## 5. Elsewhere

- **Earlier locks, repointed or widened, each with a dated note.**
  - **B1521's lock** reads v1.3 from this arc's `received/GENESIS_v1_3_sm.md`, as B1519's reads v1.2 from B1521's.
  - **B1516's citation rule** exempted kept GENESIS copies by the regex `GENESIS_v\d+_\d+\.md`, narrower than its docstring's
    `received/GENESIS_v*.md`. It now also accepts a seat suffix (`_main`, `_sm`); the suffix is needed because the two v1.3s
    share a number.
  - **B1517's version-line pin** fixed the date 2026-10-02; main's v1.4 and v1.5 are dated 2026-10-03. Any date is now
    accepted, and all nine of B1517's carried statements are still found.
- **`docs/RELAY_LEDGER.md`.**
  - Main's relay of 2026-10-02 is BANKED, answered by its lines here.
  - The audit lane's relay is rowed by name, BANKED by sm:B1524 (the bar) and sm:B1525 (GAP3). Its received copy here is named
    as the relay is, so the relay gate counts it.
  - The new relay is OPEN.
- **The relay** to main and the audit lane: `SM_TO_CC_AND_CODEX_2026-10-03_GENESIS_V1_5.md`.

## 6. Standing and firewall

**Standing: RE-DERIVED.** Each check agrees with its source:
- sm:B1521's records, for C1;
- sm:B1522's census and X5, for C2;
- sm:B1523's read-out, for C3;
- sm:B1524's record and THE_BAR, for C4;
- the audit lane's relay, for C5.

What is added is the bookkeeping that makes GENESIS one text again: main's head, the SM seat's parallel v1.3 answered line by
line, and the seats' results since, each marked and checked.

GENESIS keeps the experiential question as an explicit hypothesis under Gate 5-Q, never a claim, and v1.5 contains none of
Q5's words. No Standard-Model number is touched: **0 of 19**.

## 7. Reproduce

```
cd frontier/B1525_genesis_v15
python3 verification/merge_genesis_v15.py received/GENESIS_v1_4_main.md /tmp/G.md   # equals GENESIS.md
python3 verification/genesis_v15_checks.py                                         # C1–C6, about 15 s
pytest tests/test_b1525_genesis_v15.py                                              # the lock (from the repo root)
```
